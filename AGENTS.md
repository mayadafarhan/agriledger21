# AGENTS.md — AgriLedger Repository Guide

## Project Overview

**Smart Agricultural Supply Chain System** — a multi-module ML monorepo with five domain modules (consumer, distributor, farmer, manufacturer, retailer), a FastAPI layer, blockchain integration (stub only), and a chatbot (not implemented). Each module targets a different supply-chain actor and trains its own ML models on domain-specific data.

---

## Repository Structure

```
agriledger/
│
├── main.py
├── requirements/
│   ├── base.txt
│   ├── ml.txt
│   ├── api.txt
│   ├── blockchain.txt
│   └── dev.txt
│
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
│
├── data/
│   ├── raw/
│   │   ├── smart_logistics.csv
│   │   └── manufacturing_defect_dataset.csv
│   │
│   └── processed/
│       ├── retailer_train.csv
│       └── retailer_test.csv
│
├── notebooks/
│   ├── smart_logistics_delay_ml_project.ipynb
│   └── archive/
│       └── retraire.ipynb
│
├── src/
│   │
│   ├── common/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── database.py
│   │   └── helpers.py
│   │
│   ├── consumer_module/              # ❌ HAS ERRORS — WILL NOT RUN
│   │   └── app/
│   │       ├── __init__.py
│   │       │
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   └── consumer_api.py
│   │       │
│   │       ├── ml/
│   │       │   ├── __init__.py
│   │       │   └── consumer_ml.py
│   │       │
│   │       ├── core/
│   │       │   ├── __init__.py
│   │       │   ├── config.py
│   │       │   └── security.py
│   │       │
│   │       ├── schemas/
│   │       │   ├── __init__.py
│   │       │   ├── request_schema.py
│   │       │   └── response_schema.py
│   │       │
│   │       ├── services/
│   │       │   ├── __init__.py
│   │       │   └── prediction_service.py
│   │       │
│   │       ├── models/
│   │       │   ├── __init__.py
│   │       │   └── consumer_model.pkl
│   │       │
│   │       └── utils/
│   │           ├── __init__.py
│   │           └── preprocessing.py
│   │
│   ├── distributor_module/            # ❌ HAS ERRORS — WILL NOT RUN
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   └── distributor_api.py
│   │       ├── ml/
│   │       │   ├── __init__.py
│   │       │   └── distributor_ml.py
│   │       ├── core/
│   │       │   ├── __init__.py
│   │       │   ├── config.py
│   │       │   └── security.py
│   │       ├── schemas/
│   │       │   ├── __init__.py
│   │       │   ├── request_schema.py
│   │       │   └── response_schema.py
│   │       ├── services/
│   │       │   ├── __init__.py
│   │       │   └── prediction_service.py
│   │       ├── models/
│   │       │   ├── __init__.py
│   │       │   └── distributor_model.pkl
│   │       └── utils/
│   │           ├── __init__.py
│   │           └── preprocessing.py
│   │
│   ├── farmer_module/                 # ❌ HAS ERRORS — WILL NOT RUN
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   └── farmer_api.py
│   │       ├── ml/
│   │       │   ├── __init__.py
│   │       │   └── farmer_ml.py
│   │       ├── core/
│   │       │   ├── __init__.py
│   │       │   ├── config.py
│   │       │   └── security.py
│   │       ├── schemas/
│   │       │   ├── __init__.py
│   │       │   ├── request_schema.py
│   │       │   └── response_schema.py
│   │       ├── services/
│   │       │   ├── __init__.py
│   │       │   └── prediction_service.py
│   │       ├── models/
│   │       │   ├── __init__.py
│   │       │   └── freshness_model.h5
│   │       └── utils/
│   │           ├── __init__.py
│   │           └── image_processing.py
│   │
│   ├── manufacturer_module/
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   └── manufacturer_api.py
│   │       ├── ml/
│   │       │   ├── __init__.py
│   │       │   └── manufacturer_ml.py
│   │       ├── core/
│   │       │   ├── __init__.py
│   │       │   ├── config.py
│   │       │   └── security.py
│   │       ├── schemas/
│   │       │   ├── __init__.py
│   │       │   ├── request_schema.py
│   │       │   └── response_schema.py
│   │       ├── services/
│   │       │   ├── __init__.py
│   │       │   └── prediction_service.py
│   │       ├── models/
│   │       │   ├── __init__.py
│   │       │   └── defect_model.pkl
│   │       └── utils/
│   │           ├── __init__.py
│   │           └── preprocessing.py
│   │
│   ├── retailer_module/
│   │   └── app/
│   │       ├── __init__.py
│   │       ├── api/
│   │       │   ├── __init__.py
│   │       │   └── retailer_api.py
│   │       ├── ml/
│   │       │   ├── __init__.py
│   │       │   └── retailer_ml.py
│   │       ├── core/
│   │       │   ├── __init__.py
│   │       │   ├── config.py
│   │       │   └── security.py
│   │       ├── schemas/
│   │       │   ├── __init__.py
│   │       │   ├── request_schema.py
│   │       │   └── response_schema.py
│   │       ├── services/
│   │       │   ├── __init__.py
│   │       │   └── prediction_service.py
│   │       ├── models/
│   │       │   ├── __init__.py
│   │       │   └── retailer_model.pkl
│   │       └── utils/
│   │           ├── __init__.py
│   │           └── preprocessing.py
│   │
│   └── reports/
│       ├── figures/
│       │   ├── Consumer/
│       │   ├── Distributor/
│       │   ├── Farmer/
│       │   ├── Manufacturer/
│       │   └── Retailer/
│       │
│       └── metrics/
│           ├── Consumer/
│           ├── Distributor/
│           ├── Farmer/
│           ├── Manufacturer/
│           └── Retailer/
│
└── tests/
    ├── __init__.py
    ├── test_consumer.py
    ├── test_distributor.py
    ├── test_farmer.py
    ├── test_manufacturer.py
    └── test_retailer.py
```

---

## Common Commands

```bash
# Install all dependencies
pip install -r requirements.txt

# Install only ML dependencies
pip install -r requirements/base.txt -r requirements/ml.txt

# Run distributor training (most complete module)
python -m src.distributor_module.app.ml.train

# Run manufacturer training
python -m src.manufacturer_module.app.ml.train

# Run retailer pipeline
python src/retailer_module/app/ml/main.py --mode train

# Start distributor FastAPI app
uvicorn src.distributor_module.app.main:app --reload

# Start manufacturer FastAPI app
uvicorn src.manufacturer_module.app.main:app --reload

# Run tests (if any exist)
pytest

# Lint
ruff check src/
black --check src/
```

---

## Module Status

### ✅ Distributor Module — Most Complete
- **Location:** `src/distributor_module/`
- **Task:** Binary classification — predict `Logistics_Delay` from `smart_logistics.csv`
- **Models:** XGBoost, Random Forest (via RandomizedSearchCV tuning)
- **Stack:** sklearn pipelines, FastAPI app with CORS/routers/exception handlers
- **Key issue:** `app/core/config.py` has a hardcoded Windows path `r"D:\agriledger\data\raw\smart_logistics.csv"` — must be changed to a relative or env-based path.
- **Files:** config.py, data_pipeline.py, train.py, evaluate.py, model.py, predict.py, app/main.py

### ⚠️ Consumer Module — Broken
- **Location:** `src/consumer_module/app/ml/`
- **Task:** Same dataset/target as distributor (`Logistics_Delay`)
- **Models:** XGBoost, Random Forest, Logistic Regression + SMOTE
- **Critical bugs:**
  - `data_pipeline.py` has broken indentation inside `build_preprocessor()` — the `ColumnTransformer` body is at wrong indent level.
  - All files use `from src.consumer_module.config import ...` but the actual config is at `src/consumer_module/app/ml/config.py`.
  - `train.py` has typo: `numric_only` instead of `numeric_only`.
  - Uses `imblearn.over_sampling.SMOTE` but `imbalanced-learn` is **not** in any requirements file.

### ⚠️ Farmer Module — Missing Data & Callback
- **Location:** `src/farmar_module/app/ml/` (note: **farmar** not farmer)
- **Task:** Binary image classification (Fresh vs Rotten fruit) using EfficientNetB0 transfer learning
- **Stack:** TensorFlow/Keras, tf.data pipelines with augmentation
- **Critical bugs:**
  - `train.py` imports `from .callbacks import get_callbacks` but **no `callbacks.py` exists** in the module.
  - No fruit image dataset present in `data/` — the dataset path in config points to a non-existent directory.
  - TensorFlow is not listed in any requirements file.

### ⚠️ Manufacturer Module — Runnable with Minor Issues
- **Location:** `src/manufacturer_module/`
- **Task:** Binary classification — predict `DefectStatus` from `manufacturing_defect_dataset.csv`
- **Models:** XGBoost, Random Forest
- **Stack:** sklearn StandardScaler pipeline, FastAPI app
- **Status:** Dataset exists, code is relatively clean. May need import path adjustments depending on how it's invoked.

### ⚠️ Retailer Module — Partially Working
- **Location:** `src/retailer_module/app/ml/`
- **Task:** Multi-class classification (8 product categories)
- **Models:** Random Forest, XGBoost, Gradient Boosting
- **Key issue:** `train.py` has the `DataPipeline` import **commented out** and reads pre-processed CSVs directly from `data/processed/`. Those CSVs exist, so training may work, but the full pipeline from raw data does not.
- **Missing:** Raw retail dataset not present.

### ❌ Blockchain Module — Stub Only
- Requirements exist (`requirements/blockchain.txt`) but **zero implementation code** uses Web3 or any blockchain functionality.

### ❌ Chatbot — Not Implemented
- No chatbot code, no NLP dependencies, no related files anywhere in the repo.

### ❌ API Layer — Empty
- `api/main.py` and `api/routers/farmer.py` are both empty files.
- The distributor and manufacturer modules have their own internal FastAPI apps.

---

## Datasets

| File | Rows | Target | Used By |
|------|------|--------|---------|
| `data/raw/smart_logistics.csv` | ~10k | `Logistics_Delay` (binary) | Consumer, Distributor, Notebook |
| `data/raw/manufacturing_defect_dataset.csv` | ~1k | `DefectStatus` (binary) | Manufacturer |
| `data/processed/retailer_train.csv` | present | multi-class category | Retailer |
| `data/processed/retailer_test.csv` | present | multi-class category | Retailer |
| Fruit images | **MISSING** | Fresh/Rotten | Farmer |
| Elliptic Bitcoin CSVs | **MISSING** (only venv folder) | class (illicit) | Notebook only |

---

## Architecture Patterns

- **Config:** Each module has a `config.py` using either dataclasses or plain constants for paths, column names, model hyperparameters, and train/test split ratios.
- **Data Pipeline:** `data_pipeline.py` in each module handles loading, cleaning, feature engineering, and sklearn `ColumnTransformer` preprocessing. Distributor module is the gold standard — uses a `ProcessedData` dataclass and is leakage-safe.
- **Model Factory:** `model.py` provides a factory pattern (`ModelFactory` or `ModelBundle`) that builds configured sklearn/xgboost estimators.
- **Training:** `train.py` orchestrates the pipeline → model → evaluation → serialization flow. Distributor uses `RandomizedSearchCV`.
- **Evaluation:** `evaluate.py` computes metrics (accuracy, precision, recall, F1, ROC-AUC) and generates plots (confusion matrix, ROC curves, feature importance).
- **Prediction:** `predict.py` loads saved models and applies them to new data.
- **Serialization:** Models saved via `joblib` to `models/` directories within each module.

---

## Known Pitfalls

1. **Import paths are inconsistent.** Some files use `from src.module_name.app.ml.config import ...`, others use relative imports like `from .config import ...`. The working directory and `sys.path` must be set correctly.
2. **Hardcoded absolute paths** in `src/distributor_module/app/core/config.py` and `notebooks/retraire.ipynb`. Always grep for `C:/Users` or `D:\` before running.
3. **Missing dependencies:** `imbalanced-learn` (consumer), `tensorflow` (farmer), `torch` + `torch-geometric` (notebook) are not in any requirements file.
4. **The notebook `smart_logistics_delay_ml_project.ipynb` shows 100% accuracy** — this is data leakage, not a real result. The `Logistics_Delay_Reason` column leaks the target.
5. **The `farmar_module` directory is misspelled** (should be `farmer_module`). All imports referencing it must match the misspelling.
6. **No `__init__.py` audit** was fully done — some subdirectories may be missing them, causing import failures.

---

## Code Style

- Python 3.10+ assumed (type hints, dataclasses used throughout)
- Mixed Arabic and English comments (especially in notebooks and some module files)
- No consistent formatter enforced yet (`black` and `ruff` are in dev requirements but no config files exist)
- No existing tests in the repo

---

## Priority Fix Order (if resuming development)

1. **Fix consumer module** — correct indentation in `data_pipeline.py`, fix import paths, add `imbalanced-learn` to requirements
2. **Create `callbacks.py`** for farmer module (or remove the import in `train.py`)
3. **Replace hardcoded paths** with `pathlib.Path` relative to project root or environment variables
4. **Add missing deps** to requirements: `tensorflow`, `imbalanced-learn`, `torch`, `torch-geometric`
5. **Implement blockchain integration** or remove the stub
6. **Implement chatbot** or remove from project scope
7. **Fill empty API files** (`api/main.py`, `api/routers/farmer.py`) or consolidate with per-module FastAPI apps
8. **Add tests** — zero test coverage currently


---

# Development Rules Reference

All contributors, AI agents, and automation tools MUST follow the rules defined in:

```md
DEVELOPMENT_RULES.md
```

These rules are mandatory for:
- Codex
- Cursor
- Copilot
- AI coding agents
- Human contributors

No code should be added unless it follows the repository architecture and development safety rules.