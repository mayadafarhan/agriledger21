# SMART_CONTRACT_RULES.md

## Purpose

This file defines the Solidity contract rules for AgriLedger.

---

## Contract Scope

The primary deployed contract must be `SupplyChainCore.sol`.

It must own the authoritative on-chain state.

---

## Required Events

Contracts must emit events for critical operations:

- `CropRegistered`
- `OwnershipTransferred`
- `ShipmentUpdated`
- `ProductVerified`
- `FraudFlagged`

---

## Lifecycle Rules

Assets must follow a strict state machine.

Example states:

- `Created`
- `Harvested`
- `Processed`
- `Packaged`
- `InTransit`
- `Delivered`
- `Sold`
- `Verified`

Invalid transitions must revert.

---

## Access Control

Write functions must enforce roles such as:

- `Farmer`
- `Manufacturer`
- `Distributor`
- `Retailer`
- `Consumer`
- `Admin`

Unauthorized writes must revert.

