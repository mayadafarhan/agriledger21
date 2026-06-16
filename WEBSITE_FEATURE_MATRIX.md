# WEBSITE_FEATURE_MATRIX.md - AgriLedger Website Feature Matrix

## Purpose

This document maps website features to roles, modules, and backend dependencies.

It exists so the frontend is built from a defined matrix instead of assumptions.

---

## Feature Matrix

| Feature | Farmer | Manufacturer | Distributor | Retailer | Consumer | Admin | Backend Dependency |
|---|---|---|---|---|---|---|---|
| Login | Yes | Yes | Yes | Yes | Yes | Yes | Auth service |
| Register | Yes | Yes | Yes | Yes | Yes | Yes | Auth service |
| Dashboard | Yes | Yes | Yes | Yes | Yes | Yes | Gateway summary + verification status + prediction history |
| Supply chain flow | Yes | Yes | Yes | Yes | Yes | Yes | Gateway summary + role dashboards |
| ML module matrix | Yes | Yes | Yes | Yes | No | Yes | Prediction history + model status |
| Product list | Yes | Yes | Yes | Yes | Yes | Yes | Product service |
| Product detail | Yes | Yes | Yes | Yes | Yes | Yes | Product service |
| Crop registration | Yes | No | No | No | No | No | Farmer ML and blockchain |
| Quality prediction | Yes | Yes | No | No | No | No | Farmer ML service |
| Defect prediction | No | Yes | No | No | No | No | Manufacturer ML service |
| Shipment tracking | No | No | Yes | No | No | Yes | Distributor service |
| Delay prediction | No | No | Yes | No | No | Yes | Distributor ML service |
| Inventory view | No | No | No | Yes | No | Yes | Retailer service |
| Demand prediction | No | No | No | Yes | No | Yes | Retailer ML service |
| QR verification | No | No | No | No | Yes | Yes | Verification service |
| Product history | Yes | Yes | Yes | Yes | Yes | Yes | DB + blockchain |
| Blockchain proof | Yes | Yes | Yes | Yes | Yes | Yes | Blockchain service |
| Reports | Yes | Yes | Yes | Yes | No | Yes | Reporting service |
| Audit trail | Yes | Yes | Yes | Yes | Yes | Yes | Reporting + verification data |
| Model health | Yes | Yes | Yes | Yes | No | Yes | Model status service |
| Blockchain health | Yes | Yes | Yes | Yes | Yes | Yes | Blockchain service |
| Fraud alerts | No | Yes | Yes | Yes | Yes | Yes | Alert service |

---

## Feature Priority

### P0

- login
- register
- dashboard
- supply chain flow
- ML module matrix
- product detail
- product history
- blockchain verification
- role-based access

### P1

- crop registration
- quality prediction
- defect prediction
- shipment tracking
- delay prediction
- inventory
- demand prediction

### P2

- reports
- analytics
- health panels
- audit / traceability views
- export actions
- dashboard flow cards
- ML module matrix

---

## Dependency Rules

Each feature must declare:

- source module
- backend endpoint
- expected response
- failure state
- loading state

If any of these are missing, the feature is incomplete.

---

## Source of Truth Rules

- Operational counts come from the database.
- Prediction values come from ML services.
- Proofs and hashes come from blockchain.
- UI labels must always show the source of each piece of data.

---

## Conflict Prevention Rules

- Do not implement two different screens for the same feature unless the user journey requires it.
- Do not repeat the same backend query in multiple components without a shared service.
- Do not add a feature if its backend contract is undefined.
- Do not build a dashboard metric if the source cannot be verified.
