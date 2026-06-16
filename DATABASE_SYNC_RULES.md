# DATABASE_SYNC_RULES.md

## Purpose

This file defines how module databases synchronize with blockchain.

---

## Source of Truth

- Databases are the operational source of truth.
- Blockchain is the immutable verification source.

---

## Stored Data

Databases store:

- operational records
- predictions
- images
- reports
- live workflow data

Blockchain stores:

- cryptographic hashes
- ownership history
- shipment events
- verification proofs
- audit events

---

## Sync Rules

- never duplicate authoritative state across contracts
- never store raw dataset content on-chain
- never use blockchain as the main database

