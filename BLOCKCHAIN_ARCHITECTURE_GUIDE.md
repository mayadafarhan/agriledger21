# BLOCKCHAIN_ARCHITECTURE_GUIDE.md

## Purpose

This file defines the architecture and governance model for AgriLedger blockchain.

It is the main design guide for agents and developers.

---

## Architecture Principles

- Blockchain is a trust layer, not the application backend.
- ML stays off-chain.
- Operational databases stay authoritative for live business data.
- Blockchain stores immutable proofs and audit history only.
- One shared blockchain service is used by all modules.

---

## Source of Truth

- Databases are the operational source of truth.
- Blockchain is the immutable verification authority.
- `SupplyChainCore.sol` is the on-chain source of truth.

---

## Deployment Model

For MVP:

- deploy only `SupplyChainCore.sol`
- avoid fragmented contracts
- avoid duplicate on-chain state

Actor contracts are optional future abstractions only.

---

## Safe Expansion Rule

If the project grows, actor contracts may be added only if they:

- do not duplicate state
- do not store authoritative business logic
- do not fragment audit history
- remain thin adapters around the core contract

