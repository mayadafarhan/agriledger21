import asyncio
import importlib
import logging
from datetime import datetime
from typing import Any, Callable, Awaitable

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from api.dependencies import get_current_user
from src.shared.database.models.user import User


logger = logging.getLogger("gateway")


def _load_app(module_path: str, attr_name: str = "app"):
    """Import a sub-application defensively so one broken module does not block the gateway."""
    try:
        module = importlib.import_module(module_path)
        app_obj = getattr(module, attr_name)
        return app_obj
    except Exception as exc:
        logger.warning("Skipping %s due to import failure: %s", module_path, exc)
        return None


app = FastAPI(title="AgriLedger Global API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_modules = [
    ("/consumer", "src.consumer_module.app.main"),
    ("/distributor", "src.distributor_module.app.main"),
    ("/farmer", "src.farmar_module.app.main"),
    ("/manufacturer", "src.manufacturer_module.app.main"),
    ("/retailer", "src.retailer_module.app.main"),
    ("/blockchain", "src.blockchain", "blockchain_app"),
]

mounted_modules = []
for item in _modules:
    if len(item) == 2:
        prefix, module_path = item
        app_obj = _load_app(module_path)
    else:
        prefix, module_path, attr_name = item
        app_obj = _load_app(module_path, attr_name)
    if app_obj is not None:
        app.mount(prefix, app_obj)
        mounted_modules.append((prefix, module_path))


def _serialize_model_response(payload: Any) -> Any:
    if hasattr(payload, "model_dump"):
        return payload.model_dump()
    if isinstance(payload, dict):
        return payload
    return payload


def _latest_matching_event(events: list[dict[str, Any]], names: set[str]) -> dict[str, Any] | None:
    for event in reversed(events):
        if event.get("event") in names:
            return event
    return None


async def _load_module_snapshot(label: str, docs_url: str, loader: Callable[[], Awaitable[Any]]) -> dict[str, Any]:
    try:
        payload = await loader()
        return {
            "key": label.lower(),
            "label": label,
            "docs_url": docs_url,
            "available": True,
            "model_info": _serialize_model_response(payload),
        }
    except Exception as exc:
        logger.warning("Module snapshot failed for %s: %s", label, exc)
        return {
            "key": label.lower(),
            "label": label,
            "docs_url": docs_url,
            "available": False,
            "error": str(exc),
        }

@app.get("/", response_class=HTMLResponse)
async def root():
    links = "\n".join(
        f'<li><a href="{prefix}/docs">{prefix.strip("/") or "root"} Module API</a></li>'
        for prefix, _ in mounted_modules
    )
    return """
    <html>
        <head><title>AgriLedger API Gateway</title></head>
        <body style="font-family: Arial, sans-serif; padding: 2rem;">
            <h1>🌾 AgriLedger API Gateway</h1>
            <p>Select a module to view its Swagger UI:</p>
            <ul>{links}</ul>
        </body>
    </html>
    """.replace("{links}", links)


@app.get("/api/dashboard/summary", tags=["Dashboard"])
async def dashboard_summary(current_user: User = Depends(get_current_user)) -> dict[str, Any]:
    """Aggregate module metadata and blockchain snapshot for the preview dashboard."""
    from src.blockchain.web3_client import web3_client
    from src.consumer_module.app.api.model_info import model_info as consumer_model_info
    from src.distributor_module.app.api.model_info import model_info as distributor_model_info
    from src.manufacturer_module.app.api.routes.model_info import model_info as manufacturer_model_info
    from src.retailer_module.app.api.model_info import model_info as retailer_model_info
    from src.farmar_module.app.api.model_info import model_info as farmer_model_info

    snapshots = await asyncio.gather(
        _load_module_snapshot("Farmer", "/farmer/docs", farmer_model_info),
        _load_module_snapshot("Manufacturer", "/manufacturer/docs", manufacturer_model_info),
        _load_module_snapshot("Distributor", "/distributor/docs", distributor_model_info),
        _load_module_snapshot("Retailer", "/retailer/docs", retailer_model_info),
        _load_module_snapshot("Consumer", "/consumer/docs", consumer_model_info),
    )

    blockchain_snapshot = web3_client.get_dashboard_summary()
    recent_events = blockchain_snapshot.get("recent_transactions", [])

    module_chain_map = {
        "farmer": {"event_names": {"CropRegistered"}},
        "manufacturer": {"event_names": {"ShipmentUpdated"}, "states": {2, 3}},
        "distributor": {"event_names": {"ShipmentUpdated"}, "states": {4}},
        "retailer": {"event_names": {"OwnershipTransferred", "ShipmentUpdated"}, "states": {5, 6}},
        "consumer": {"event_names": {"ProductVerified", "FraudFlagged"}},
    }

    for snapshot in snapshots:
        key = snapshot["key"]
        rules = module_chain_map.get(key, {})
        relevant_event = None
        for event in reversed(recent_events):
            if event.get("event") not in rules.get("event_names", set()):
                continue
            if "states" in rules:
                args = event.get("args", {})
                if args.get("state") not in rules["states"]:
                    continue
            relevant_event = event
            break
        snapshot["blockchain"] = {
            "contract": "SupplyChainCore.sol",
            "mode": blockchain_snapshot.get("mode"),
            "last_event": relevant_event,
        }

    return {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "modules": snapshots,
        "blockchain": blockchain_snapshot,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
