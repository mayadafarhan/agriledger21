# TODO - Supply Chain AI FastAPI (Clean Architecture)

- [x] Create 5 module services with exact folder names: farmer_module, manufacturer_module, distributor_module, retailer_module, consumer_module

- [ ] For each module: implement FastAPI app + Clean Architecture layers (routes/services/schemas/models/core/utils/ml) + /predict + /health + swagger
- [ ] Implement async /predict endpoints with Pydantic validation and DI
- [ ] Implement per-module ML inference loaders using existing artifacts in `models/`
- [ ] Add .env support per module (python-dotenv + Pydantic settings)
- [ ] Add logging + exception handling (global handlers)
- [ ] Add production files per module: requirements.txt, Dockerfile, README.md, .gitignore
- [ ] Create root `gateway/` FastAPI service connecting all module services; include API communication example
- [ ] Add root-level `docker-compose.yml` to run gateway + all module services
- [ ] Add root-level `requirements/` files alignment (base.txt, api.txt, ml.txt, dev.txt, blockchain.txt)
- [ ] Add root-level example .env files and example request/response JSON for all endpoints
- [ ] Add startup commands for local dev and production
- [ ] Run basic syntax checks (compileall) and minimal docker build/run verification

