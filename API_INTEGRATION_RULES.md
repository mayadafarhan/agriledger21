# API_INTEGRATION_RULES.md

## Purpose

This file defines how FastAPI integrates with blockchain safely.

---

## Integration Boundary

Application modules must not call `web3.py` directly.

All blockchain access must go through:

- `blockchain_service.py`
- validation layers
- integration wrappers

---

## API Rules

- routes must be thin
- routes must validate inputs
- routes must return structured JSON
- routes must not contain contract logic

---

## Dashboard Compatibility

API responses should support:

- realtime sync
- verification lookups
- transaction receipts
- traceability views

