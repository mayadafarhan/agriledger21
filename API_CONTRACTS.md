# API_CONTRACTS.md - AgriLedger API Contracts

## Purpose

This document defines the target API contract required by the frontend and dashboard layers.

The frontend must rely on these contracts rather than guessing request or response shapes.

All endpoints must return structured JSON.

---

## Contract Rules

- Endpoints must be versioned or stable.
- Requests must validate input.
- Responses must include success or error state.
- Blockchain operations must go through a service boundary.
- ML operations must go through the module APIs or gateway.
- If an existing module returns `ok` instead of `success`, the website gateway should normalize it for the frontend.
- The frontend must not depend on raw internal module response quirks.

---

## Common Response Shape

```json
{
  "success": true,
  "message": "string",
  "data": {}
}
```

Error responses should keep a similar envelope when possible.

Existing blockchain responses currently use:

```json
{
  "ok": true,
  "message": "string",
  "data": {}
}
```

The web gateway should normalize `ok` to `success` when returning data to the frontend.

---

## Current Gateway Contracts

### GET /

Returns the mounted API module index.

### GET /api/dashboard/summary

Current implemented dashboard summary endpoint. Authentication required.

Mounted module base paths:

- `/consumer`
- `/distributor`
- `/farmer`
- `/manufacturer`
- `/retailer`
- `/blockchain`

Each mounted module exposes its own `/docs` path when mounted successfully.

### Current website backend routes

The web backend currently exposes:

- `POST /auth/login`
- `POST /auth/register`
- `GET /auth/me`
- `GET /dashboard/summary`
- `GET /dashboard/admin`
- `GET /dashboard/farmer`
- `GET /dashboard/manufacturer`
- `GET /dashboard/distributor`
- `GET /dashboard/retailer`
- `GET /dashboard/consumer`
- `GET /products`
- `GET /products/{product_id}`
- `POST /products`
- `PUT /products/{product_id}`
- `DELETE /products/{product_id}`
- `GET /shipments`
- `GET /shipments/{shipment_id}`
- `POST /shipments`
- `PUT /shipments/{shipment_id}`
- `DELETE /shipments/{shipment_id}`
- `GET /inventory`
- `POST /inventory`
- `PUT /inventory/{item_id}`
- `POST /api/predict/{module}`
- `GET /reports`
- `GET /users`
- `GET /users/{user_id}`
- `PATCH /users/{user_id}/status`
- `GET /verification/status`
- `POST /verification/products/{product_id}/register-crop`
- `POST /verification/products/{product_id}/transfer-ownership`
- `POST /verification/shipments/{shipment_id}/update`
- `POST /verification/products/{product_id}/verify`
- `GET /verification/products/{product_id}/history`
- `GET /verification/products/{product_id}/qr`
- `POST /verification/products/{product_id}/flag-fraud`

The UI `Audit Trail` screen is a traceability view backed by `GET /reports`; it is not a separate backend service.

---

## Blockchain Contracts

These are the current blockchain API paths when mounted through the gateway under `/blockchain`.

### POST /blockchain/crops/register

Request:

```json
{
  "product_id": "crop-001",
  "crop_type": "Tomato",
  "quantity": 100,
  "metadata": {
    "farm_id": "farm-001",
    "harvest_date": "2026-05-30"
  }
}
```

Response:

```json
{
  "success": true,
  "message": "Crop registered",
  "data": {
    "tx_hash": "0xabc...",
    "product_id": "crop-001"
  }
}
```

### POST /blockchain/ownership/transfer

Request:

```json
{
  "product_id": "crop-001",
  "to_address": "0x123..."
}
```

Response:

```json
{
  "success": true,
  "message": "Ownership transferred",
  "data": {
    "tx_hash": "0xabc..."
  }
}
```

### POST /blockchain/shipments/update

Request:

```json
{
  "product_id": "crop-001",
  "state": 4,
  "location": "Cairo Distribution Center",
  "details": "Temperature within accepted range"
}
```

Response:

```json
{
  "success": true,
  "message": "Shipment updated",
  "data": {
    "tx_hash": "0xabc..."
  }
}
```

### POST /blockchain/products/{product_id}/verify

Request:

```json
{
  "farm_id": "farm-001",
  "harvest_date": "2026-05-30"
}
```

Response:

```json
{
  "product_id": "crop-001",
  "is_valid": true,
  "on_chain_hash": "0xabc...",
  "computed_hash": "0xabc...",
  "is_fraudulent": false,
  "fraud_reason": null,
  "timestamp": 1710000000
}
```

### GET /blockchain/products/{product_id}/history

Response:

```json
{
  "product_id": "crop-001",
  "ownership_history": [],
  "shipment_history": []
}
```

### GET /blockchain/products/{product_id}/qr

Response:

```json
{
  "product_id": "crop-001",
  "qr_code_base64": "base64...",
  "verification_payload": {}
}
```

### POST /blockchain/products/flag-fraud

Request:

```json
{
  "product_id": "crop-001",
  "reason": "Metadata mismatch"
}
```

Response:

```json
{
  "success": true,
  "message": "Product flagged",
  "data": {
    "tx_hash": "0xabc..."
  }
}
```

### GET /blockchain/status

Response:

```json
{
  "status": "active",
  "mode": "simulation",
  "rpc_url": "http://127.0.0.1:8545",
  "contract_address": "0x0000000000000000000000000000000000000000",
  "default_account": "0x..."
}
```

---

## Dashboard Contracts

### GET /api/dashboard/summary

Response:

```json
{
  "success": true,
  "message": "Summary loaded",
  "data": {
    "total_products": 0,
    "active_shipments": 0,
    "fraud_alerts": 0,
    "blockchain_health": "healthy",
    "model_health": "healthy"
  }
}
```

Requires authentication.

### GET /dashboard/admin

Response must include:

- totals
- health indicators
- fraud status
- recent events

Target endpoint. Implement through gateway or BFF before frontend depends on it.

### GET /dashboard/farmer

Response must include:

- crop registrations
- freshness predictions
- proof status

Target endpoint. Implement through gateway or BFF before frontend depends on it.

### GET /dashboard/manufacturer

Response must include:

- batches
- defects
- transfers

Target endpoint. Implement through gateway or BFF before frontend depends on it.

### GET /dashboard/distributor

Response must include:

- shipments
- delays
- tracking status

Target endpoint. Implement through gateway or BFF before frontend depends on it.

### GET /dashboard/retailer

Response must include:

- inventory
- demand prediction

Target endpoint. Implement through gateway or BFF before frontend depends on it.

### GET /dashboard/consumer

Response must include:

- qr verification state
- product history

Target endpoint. Implement through gateway or BFF before frontend depends on it.

---

## Verification Contracts

### GET /verification/status

Response:

```json
{
  "success": true,
  "message": "Verification service is ready",
  "data": {
    "status": "active",
    "mode": "simulation",
    "rpc_url": "http://127.0.0.1:8545",
    "contract_address": "0x0000000000000000000000000000000000000000"
  }
}
```

---

## Prediction Contracts

### Current mounted prediction endpoints

When using `gateway.py`, module predictions are expected under:

- `POST /consumer/predict`
- `POST /consumer/predict/batch`
- `POST /distributor/predict`
- `POST /distributor/predict/batch`
- `POST /farmer/predict`
- `POST /farmer/predict/batch`
- `POST /retailer/predict`
- `POST /manufacturer/predict/demand`
- `POST /manufacturer/predict/supply`
- `POST /manufacturer/predict/price`
- `POST /manufacturer/predict/risk`

### Target facade: POST /api/predict/{module}

Supported modules:

- consumer
- distributor
- farmer
- manufacturer
- retailer

Response must include:

- predicted label or class
- confidence
- model name
- timestamp

The target facade may normalize current module-specific endpoints for frontend simplicity.

---

## Auth Contracts

### POST /auth/login

Request:

```json
{
  "email": "user@example.com",
  "password": "secret"
}
```

Response:

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access_token": "jwt...",
    "role": "farmer"
  }
}
```

### POST /auth/register

Request:

```json
{
  "email": "user@example.com",
  "password": "secret",
  "role": "consumer"
}
```

Response:

```json
{
  "success": true,
  "message": "Registration successful",
  "data": {
    "user_id": 1
  }
}
```

---

## Inventory and Product Contracts

### GET /products

Target endpoint. Requires database implementation.

### GET /products/{product_id}

Target endpoint. Requires database implementation.

### GET /shipments

Target endpoint. Requires database implementation.

### GET /shipments/{shipment_id}

Target endpoint. Requires database implementation.

### GET /reports

Response must include:

- totals
- recent audit events
- recent blockchain receipts
- recent model runs

The audit trail UI should consume this endpoint rather than a separate audit backend.

Each of these endpoints must return structured JSON and must clearly distinguish operational data from verification data.

---

## Compatibility Rules

- Do not break response envelopes once defined.
- Do not invent fields per screen without updating this document.
- Do not let the frontend guess the contract from internal code.
