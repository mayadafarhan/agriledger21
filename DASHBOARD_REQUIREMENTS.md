# DASHBOARD_REQUIREMENTS.md - AgriLedger Dashboard Requirements

## Purpose

This document defines the required dashboard content for each AgriLedger role.

Dashboards must be accurate, role-aware, and aligned with the existing supply-chain and ML modules.

Dashboards must not invent metrics that the backend cannot provide.

---

## Shared Dashboard Rules

All dashboards must support:

- summary cards
- recent activity
- status indicators
- charts or tables when relevant
- clear loading and error states
- source labels for DB, ML, and blockchain data

All dashboards must respect access control.

Each dashboard must define:

- primary actions
- required API calls
- empty state
- error state
- loading state
- permission fallback

---

## Admin Dashboard

### Must show

- total products
- active shipments
- completed shipments
- pending verifications
- fraud alerts
- blockchain health
- model health
- API health
- recent transactions
- recent predictions

### Must allow

- view all actor dashboards
- inspect audit trails
- monitor system health
- review flagged items
- inspect model status per module

### Data sources

- database for totals and operational records
- gateway for module health
- blockchain API for ledger status and recent proof events
- ML module APIs for model health

---

## Farmer Dashboard

### Must show

- crop registration status
- crop count
- quality prediction
- freshness prediction
- blockchain proof
- recent harvests
- verification history

### Must allow

- register crop
- upload crop image if applicable
- view prediction result
- generate or view proof
- view crop history

### Data sources

- database for crop records
- farmer ML API for freshness prediction
- blockchain API for crop proof and QR payload

---

## Manufacturer Dashboard

### Must show

- batches
- defects
- transfer history
- processing status
- quality analytics
- model output summary
- blockchain proof

### Must allow

- inspect batch lifecycle
- flag defective items
- transfer ownership records
- review verification results

### Data sources

- database for batches and process status
- manufacturer ML API for demand, supply, price, and risk where available
- blockchain API for ownership transfer and audit proof

---

## Distributor Dashboard

### Must show

- shipment tracking
- delay prediction
- active routes
- delayed shipments
- shipment exceptions
- blockchain event history

### Must allow

- create or update shipment records
- inspect delay risk
- view route timeline
- review shipment proofs

### Data sources

- database for shipment records
- distributor ML API for delay prediction
- blockchain API for shipment update proof

---

## Retailer Dashboard

### Must show

- inventory
- demand prediction
- product categories
- low stock alerts
- incoming shipments
- recent sales or stock changes

### Must allow

- review inventory status
- inspect demand forecast
- verify received products
- manage availability view

### Data sources

- database for inventory and stock movements
- retailer ML API for product category or demand support
- blockchain API for received product verification

---

## Consumer Dashboard

### Must show

- QR verification
- product history
- authenticity status
- product owner trail where applicable
- fraud warnings
- verification timestamp

### Must allow

- scan QR code
- verify product
- view full history
- view proof hash

### Data sources

- blockchain API for verification and proof history
- database for public product metadata
- consumer API for consumer-facing prediction or risk checks where available

---

## Health Panels

Every dashboard should expose, when available:

- backend API health
- model health
- blockchain health
- database sync status

If a health value is unavailable, the UI must display that clearly instead of guessing.

---

## Dashboard Data Rules

- Admin data may aggregate all roles.
- Actor dashboards must focus on role-specific tasks.
- Operational counts come from the database.
- Prediction values come from ML services.
- Proofs and receipts come from blockchain services.

No dashboard may mix these sources without labeling them.

---

## Dashboard Acceptance Criteria

A dashboard is complete only if:

- all metrics have a documented source
- all primary actions map to an API contract
- role permissions are enforced
- loading and error states are visible
- missing backend data is shown as unavailable, not fabricated
- blockchain failures do not block non-blockchain dashboard data
