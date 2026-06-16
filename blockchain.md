# BLOCKCHAIN.md

## Purpose

This file is the central index for the AgriLedger blockchain specification.

It defines the high-level architecture and points to the detailed rule files that govern implementation.

This document must be used together with:

- `AGENT.md`
- `CLAUDE.md`
- `DEVELOPMENT_RULES.md`
- `BLOCKCHAIN_ARCHITECTURE_GUIDE.md`
- `SMART_CONTRACT_RULES.md`
- `API_INTEGRATION_RULES.md`
- `SECURITY_RULES.md`
- `EVENT_SYSTEM_RULES.md`
- `DATABASE_SYNC_RULES.md`

---

## Core Mission

The blockchain layer is a trust, audit, and verification layer only.

It must:

- hash important data off-chain
- register cryptographic proofs on-chain
- track ownership and shipment transitions
- expose verifiable audit history

It must not:

- replace databases
- replace ML systems
- replace the FastAPI backend
- store raw datasets on-chain
- store model artifacts on-chain
- run inference or training
- interfere with existing APIs

---

## Contract Simplification Rule

For MVP and initial deployment:

- `SupplyChainCore.sol` SHOULD remain the only deployed contract unless modular expansion becomes necessary.

Actor contracts are optional abstractions and must not duplicate:

- ownership state
- shipment state
- verification logic
- audit tracking

All authoritative chain state must remain inside `SupplyChainCore.sol`.

Supporting actor contracts may be introduced later, but only as thin wrappers or adapters and only if they do not fragment the source of truth.

---

## Blockchain Event Rules

Smart contracts must emit events for all critical operations.

Required events include:

- `CropRegistered`
- `OwnershipTransferred`
- `ShipmentUpdated`
- `ProductVerified`
- `FraudFlagged`

Frontend dashboards and listeners must rely on events for realtime synchronization.

Direct blockchain polling should be minimized.

---

## Product Lifecycle Rules

All supply chain assets must follow a strict lifecycle state machine.

Example states:

- `Created`
- `Harvested`
- `Processed`
- `Packaged`
- `InTransit`
- `Delivered`
- `Sold`
- `Verified`

Invalid transitions must revert transactions.

---

## Access Control Rules

Blockchain write operations must enforce role-based permissions.

Example roles:

- `Farmer`
- `Manufacturer`
- `Distributor`
- `Retailer`
- `Consumer`
- `Admin`

Unauthorized writes must revert immediately.

---

## Data Synchronization Rules

Operational data lives inside module databases.

Blockchain stores only:

- verification proofs
- ownership history
- immutable audit events
- cryptographic hashes

Databases remain the operational source of truth.

Blockchain remains the immutable verification authority.

---

## Listener Rules

Blockchain listeners may subscribe to smart contract events for:

- realtime dashboard updates
- audit synchronization
- transaction indexing
- notification systems

Listeners must not modify ML pipelines directly.

---

## Error Isolation Rules

Blockchain failures must not crash:

- FastAPI services
- ML inference
- prediction APIs
- dashboard rendering

All blockchain errors must be isolated through:

- graceful fallbacks
- retry mechanisms
- simulation mode
- exception boundaries

---

## QR Traceability Rules

Each tracked product may expose a QR-based verification layer.

QR payloads should contain:

- product ID
- blockchain transaction hash
- verification endpoint
- immutable traceability reference

Consumers must verify products through backend APIs only.

---

## Direct Web3 Access Is Forbidden

Application modules must not interact directly with:

- `web3.py`
- contracts
- RPC providers

All blockchain communication must pass through:

- `blockchain_service.py`
- validation layers
- integration wrappers

---

## Recommended File Layout

```text
src/blockchain/
├── api/
├── services/
├── utils/
├── schemas/
├── listeners/
├── integrations/
├── contracts/
├── tests/
├── web3_client.py
├── config.py
└── exceptions.py
```

---

## File Responsibilities

### `config.py`

- loads blockchain settings
- validates environment variables
- keeps secrets out of source code

### `exceptions.py`

- defines blockchain-specific exceptions
- isolates RPC, contract, and validation failures

### `web3_client.py`

- manages Web3 connection logic
- loads contract instances
- signs and submits transactions
- reads state and receipts

### `services/`

- contains business orchestration
- hashes payloads
- coordinates contract calls
- returns structured responses

### `api/`

- exposes FastAPI routers
- keeps routes thin
- delegates to services only

### `schemas/`

- contains request and response models
- validates blockchain inputs and outputs

### `utils/`

- contains hashing and normalization helpers
- keeps reusable support logic isolated

### `listeners/`

- subscribes to contract events
- indexes history
- supports dashboard sync

### `integrations/`

- contains module-specific adapters
- maps domain payloads to blockchain service calls

### `contracts/`

- stores Solidity source
- stores ABI artifacts
- keeps contract logic versioned

### `tests/`

- contains blockchain unit and integration tests
- validates hashing, service logic, routing, and event behavior

---

## Implementation Order

Recommended order:

1. create `config.py`
2. create `exceptions.py`
3. create `utils/hashing.py`
4. create `web3_client.py`
5. create `services/blockchain_service.py`
6. create `schemas/request.py`
7. create `schemas/response.py`
8. create `contracts/SupplyChainCore.sol`
9. add ABI artifacts
10. create `listeners/`
11. create integration wrappers
12. add tests

---

## Final Rule

If any blockchain change risks:

- breaking ML
- altering inference
- breaking APIs
- changing Swagger contracts
- modifying existing schemas
- affecting current models
- creating dependency conflicts

do not apply the change.
