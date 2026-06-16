# DATABASE_SCHEMA.md - AgriLedger Website Database Schema

## Purpose

This document defines the operational database model required for the AgriLedger website.

The database is the operational source of truth. Blockchain is the immutable verification layer. ML services provide predictions and model metadata.

---

## Database Rules

- Store operational records in the database.
- Store only hashes, receipts, and audit references on blockchain.
- Do not store raw model artifacts in the database.
- Do not store private keys or blockchain secrets in the database.
- Every blockchain write should have a matching database audit record.
- Every prediction shown in the UI should be persisted if it affects workflow decisions.

---

## Required Tables

### users

Stores application users.

Required fields:

- id
- email
- password_hash
- full_name
- role
- status
- created_at
- updated_at

### roles

Stores role definitions if roles are database-driven.

Required fields:

- id
- name
- description
- permissions

### products

Stores operational product or crop records.

Required fields:

- id
- product_code
- crop_type
- quantity
- unit
- current_owner_id
- lifecycle_state
- source_actor
- created_at
- updated_at

### product_metadata

Stores structured off-chain metadata used for ML and hashing.

Required fields:

- id
- product_id
- metadata_json
- metadata_hash
- created_at

### batches

Stores manufacturer-side batch records.

Required fields:

- id
- batch_code
- product_id
- manufacturer_id
- status
- defect_status
- created_at
- updated_at

### shipments

Stores shipment records.

Required fields:

- id
- shipment_code
- product_id
- distributor_id
- origin
- destination
- current_location
- status
- estimated_arrival
- created_at
- updated_at

### inventory_items

Stores retailer inventory.

Required fields:

- id
- retailer_id
- product_id
- quantity_available
- reorder_level
- status
- updated_at

### predictions

Stores ML prediction outputs used by the website.

Required fields:

- id
- module_name
- product_id
- shipment_id
- model_name
- model_version
- input_reference
- prediction_label
- confidence
- raw_output_json
- created_by
- created_at

### model_runs

Stores training or evaluation run metadata.

Required fields:

- id
- module_name
- model_name
- model_version
- run_type
- metrics_json
- artifact_path
- status
- started_at
- completed_at

### blockchain_receipts

Stores references to blockchain transactions.

Required fields:

- id
- product_id
- action_type
- tx_hash
- block_number
- contract_address
- chain_mode
- status
- receipt_json
- created_at

### audit_events

Stores application-level audit events.

Required fields:

- id
- actor_user_id
- actor_role
- entity_type
- entity_id
- event_type
- source
- details_json
- created_at

### fraud_alerts

Stores fraud or authenticity alerts.

Required fields:

- id
- product_id
- reason
- severity
- status
- reported_by
- blockchain_tx_hash
- created_at
- resolved_at

### uploaded_files

Stores references to user uploads.

Required fields:

- id
- owner_user_id
- product_id
- file_type
- storage_path
- checksum
- created_at

---

## Relationship Rules

- One product may have many predictions.
- One product may have many blockchain receipts.
- One product may have many shipments over time.
- One product may belong to one or more batches depending on manufacturing workflow.
- One shipment belongs to one product or batch.
- One fraud alert belongs to one product.
- Audit events may reference any entity through `entity_type` and `entity_id`.

---

## Lifecycle State Values

Recommended product states:

- created
- harvested
- processed
- packaged
- in_transit
- delivered
- sold
- verified
- flagged

Database lifecycle states must map cleanly to blockchain states.

---

## Data Sync Rules

When an operational event happens:

1. Validate the request.
2. Save or update the database record.
3. Generate deterministic metadata hash if needed.
4. Submit blockchain proof if required.
5. Save blockchain receipt.
6. Save audit event.
7. Return a normalized response to the frontend.

If blockchain fails:

- keep the operational record if business rules allow it
- mark proof status as pending or failed
- do not crash ML inference or dashboard loading
- expose retry options to authorized roles

---

## Minimum MVP Database

For the first website version, implement at least:

- users
- products
- shipments
- predictions
- blockchain_receipts
- audit_events

The remaining tables can follow once the core flow is stable.

