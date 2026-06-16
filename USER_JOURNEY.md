# USER_JOURNEY.md - AgriLedger User Journeys

## Purpose

This document defines the required user flows for the AgriLedger website.

The UI must follow these journeys instead of inventing unrelated flows.

---

## Farmer Journey

```text
Login
↓
Open Farmer Dashboard
↓
Register Crop
↓
Request ML Prediction
↓
Review Freshness Result
↓
Save Record
↓
Generate or View Blockchain Proof
↓
View History
```

### Farmer goals

- register crops
- review quality prediction
- confirm traceability
- verify proof

---

## Manufacturer Journey

```text
Login
↓
Open Manufacturer Dashboard
↓
Review Incoming Batches
↓
Inspect Defect Prediction
↓
Update Batch Status
↓
Transfer Record
↓
View Blockchain Proof
```

### Manufacturer goals

- inspect batch quality
- review defect risk
- manage transfer history
- preserve audit trail

---

## Distributor Journey

```text
Login
↓
Open Distributor Dashboard
↓
Track Shipment
↓
Request Delay Prediction
↓
Update Shipment Status
↓
Write Proof Event
↓
Review Shipment History
```

### Distributor goals

- monitor shipments
- predict delays
- keep shipment traceability

---

## Retailer Journey

```text
Login
↓
Open Retailer Dashboard
↓
Review Inventory
↓
Request Demand Prediction
↓
Manage Stock View
↓
Inspect Product Verification
↓
Review Reports
```

### Retailer goals

- manage inventory
- anticipate demand
- verify incoming goods

---

## Consumer Journey

```text
Login
↓
Open Consumer Dashboard
↓
Scan QR
↓
Verify Product
↓
See Full History
↓
Review Fraud or Authenticity Flags
```

### Consumer goals

- verify authenticity
- inspect product history
- trust the traceability layer

---

## Admin Journey

```text
Login
↓
Open Admin Dashboard
↓
Review Platform Health
↓
Inspect Products and Shipments
↓
Review Fraud Alerts
↓
Check Model Health
↓
Check Blockchain Health
↓
Open Reports
```

### Admin goals

- oversee system health
- monitor each role
- review platform risk

---

## Journey Rules

- Each journey must end in a real backend-supported action.
- The UI must not skip prediction or verification steps where they are required.
- Blockchain proof generation must happen after the operational record is created.
- Consumers must verify by QR or product ID, then view the history.
- The frontend must not merge unrelated journeys into a single generic flow.

