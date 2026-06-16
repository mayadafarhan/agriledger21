# WEB_BACKEND_ARCHITECTURE.md - AgriLedger Web Backend Architecture

## Purpose

This document defines the backend layer required to support the AgriLedger website.

The existing ML modules and blockchain module should remain dedicated services. The web backend should aggregate, normalize, authorize, and persist website-facing workflows.

---

## Recommended Pattern

Use a Backend-for-Frontend style layer through the existing gateway or a dedicated web API module.

Responsibilities:

- authenticate users
- enforce roles
- aggregate module data
- normalize API responses
- coordinate database writes
- call ML prediction APIs
- call blockchain service APIs
- return frontend-friendly responses

The web backend must not duplicate ML training or blockchain transaction internals.

---

## Backend Folder Recommendation

If a dedicated website backend is added, use:

```text
api/
├── main.py
├── routers/
├── services/
├── schemas/
├── core/
└── dependencies/
```

This keeps website aggregation separate from actor-specific ML modules.

---

## Gateway Responsibilities

The gateway may expose:

- `/api/dashboard/summary`
- `/api/auth/*`
- `/api/products/*`
- `/api/shipments/*`
- `/api/predictions/*`
- `/api/reports/*`
- `/api/verification/*`

The gateway should mount existing module apps under:

- `/consumer`
- `/distributor`
- `/farmer`
- `/manufacturer`
- `/retailer`
- `/blockchain`

---

## Service Boundaries

### Auth service

- login
- register
- token validation
- role resolution

### Product service

- create product
- list products
- get product detail
- build traceability view

### Shipment service

- create shipment
- update shipment
- list shipments
- coordinate shipment proof

### Prediction service

- call correct ML module
- normalize prediction output
- persist prediction record

### Blockchain integration service

- call blockchain API or service wrapper
- store receipt references
- isolate blockchain failures

### Dashboard service

- aggregate database metrics
- aggregate model health
- aggregate blockchain health
- return role-specific summaries

---

## Response Normalization

The web backend should normalize:

- `ok` to `success`
- module-specific prediction outputs to a common prediction shape
- blockchain receipts to a common receipt shape
- errors to a common error envelope

---

## Failure Rules

- ML failure should not crash the whole dashboard.
- Blockchain failure should not crash non-blockchain features.
- Database failure should return a controlled error.
- Missing module imports should be surfaced as module unavailable.

---

## Training and Evaluation Rules

- Training endpoints should not be exposed to normal users.
- Evaluation endpoints should not be exposed to consumers.
- Admin-triggered training must be guarded, logged, and visibly long-running.

---

## Minimum MVP Backend

For the first website version, implement:

- auth routes
- role guards
- product routes
- shipment routes
- prediction facade
- verification facade
- dashboard summary
- database persistence

