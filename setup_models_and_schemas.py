import shutil
from pathlib import Path
import json

app_dir = Path("d:/agriledger/src/manufacturer_module/app")
ml_models_dir = app_dir / "ml" / "models"
ml_schemas_dir = app_dir / "ml" / "schemas"

# Create directories
ml_models_dir.mkdir(parents=True, exist_ok=True)
ml_schemas_dir.mkdir(parents=True, exist_ok=True)

# Copy and rename model files
models_to_copy = {
    "demand_model.pkl": "demand.pkl",
    "supply_model.pkl": "supply.pkl",
    "price_model.pkl": "price.pkl",
    "risk_model.pkl": "risk.pkl"
}

src_models_dir = app_dir / "models"
for src_name, dest_name in models_to_copy.items():
    src_path = src_models_dir / src_name
    dest_path = ml_models_dir / dest_name
    if src_path.exists():
        print(f"Copying {src_path} -> {dest_path}")
        shutil.copy2(src_path, dest_path)
    else:
        print(f"Warning: {src_path} does not exist!")

# Generate JSON schemas
features_list = [
    "ProductionVolume",
    "ProductionCost",
    "SupplierQuality",
    "DeliveryDelay",
    "DefectRate",
    "QualityScore",
    "MaintenanceHours",
    "DowntimePercentage",
    "InventoryTurnover",
    "StockoutRate",
    "WorkerProductivity",
    "SafetyIncidents",
    "EnergyConsumption",
    "EnergyEfficiency",
    "AdditiveProcessTime",
    "AdditiveMaterialCost",
    "Production",
    "Inventory",
    "StockoutR",
    "SupplierQ",
    "DeliveryD",
    "EnergyCost",
    "QualitySc",
    "Maintenance"
]

schema_payload = {"feature_columns": features_list}

for schema_name in ["demand.json", "supply.json", "price.json", "risk.json"]:
    schema_path = ml_schemas_dir / schema_name
    print(f"Writing schema to {schema_path}")
    with open(schema_path, "w") as f:
        json.dump(schema_payload, f, indent=2)

print("Setup completed successfully!")
