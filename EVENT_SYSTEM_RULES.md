# EVENT_SYSTEM_RULES.md

## Purpose

This file defines event-driven synchronization for AgriLedger blockchain.

---

## Event Model

Contracts must emit events for critical state changes.

Required events:

- `CropRegistered`
- `OwnershipTransferred`
- `ShipmentUpdated`
- `ProductVerified`
- `FraudFlagged`

---

## Listener Behavior

Listeners may:

- subscribe to contract events
- index transactions
- update dashboards
- power notifications

Listeners must not:

- modify ML pipelines
- write contract state directly
- bypass service layers

---

## Sync Strategy

Dashboards should prefer event subscription over heavy polling.

