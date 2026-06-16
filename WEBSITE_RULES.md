# WEBSITE_RULES.md - AgriLedger Web Application Rules

## Purpose

This document defines the mandatory rules for building the AgriLedger website layer.

The website must integrate the supply-chain modules, the ML services, the API gateway, the database layer, and the blockchain verification layer without breaking the existing repository architecture.

These rules apply before any new website file is created, and before any modification is made to existing code that the website depends on.

---

## Required Companion Documents

Before building the website, contributors must read these files together:

- `FRONTEND_ARCHITECTURE.md`
- `WEB_BACKEND_ARCHITECTURE.md`
- `DASHBOARD_REQUIREMENTS.md`
- `UI_SCREEN_MAP.md`
- `API_CONTRACTS.md`
- `DATABASE_SCHEMA.md`
- `AUTH_RBAC_RULES.md`
- `USER_JOURNEY.md`
- `WEBSITE_FEATURE_MATRIX.md`
- `WEBSITE_IMPLEMENTATION_PLAN.md`
- `TESTING_QA_CHECKLIST.md`
- `DEPLOYMENT_ENVIRONMENT.md`
- `OBSERVABILITY_MONITORING.md`

No website implementation should start from only one document.

---

## Scope

The website layer includes:

- Frontend pages and UI components
- Backend API aggregation and routing
- Authentication and role-based access
- Dashboard views
- Traceability views
- Prediction and evaluation views
- Report and analytics views
- Database read/write coordination

The website layer does NOT include:

- ML model training logic
- ML preprocessing logic
- Blockchain smart contract logic
- Blockchain transaction logic
- Contract deployment logic

Those responsibilities remain in their dedicated modules unless a verified bug or wrong output requires a minimal fix.

---

## Core Rule

The website must be built around the existing supply-chain and ML structure.

The correct integration order is:

1. Farmer
2. Manufacturer
3. Distributor
4. Retailer
5. Consumer
6. Gateway aggregation
7. Database persistence
8. Blockchain verification

The website must not skip any module in this flow.

The website must preserve both tracks at the same time:

- supply-chain workflow: product movement, ownership, shipment, verification
- ML workflow: prediction, confidence, model status, evaluation metadata

Neither track may hide, replace, or invalidate the other.

---

## Module Alignment Rule

The website must respect the repository structure and the existing module responsibilities:

- `consumer_module` for consumer-facing predictions and checks
- `distributor_module` for logistics delay prediction and analytics
- `farmar_module` for fruit freshness classification
- `manufacturer_module` for manufacturing defect and operational analytics
- `retailer_module` for retailer-side classification and predictions
- `blockchain` for verification, proof, and audit history
- `api/` and `gateway.py` for unified exposure to the web layer

The website must consume these modules through their exposed APIs and service boundaries.

It must not directly embed module internals into UI logic.

---

## Architecture Rules

### 1. Separation of Concerns

- UI must remain thin.
- Business logic must stay in services.
- Prediction logic must stay in ML modules.
- Validation must stay in schemas.
- Environment settings must stay in core configuration files.

### 2. Single Entry Point

- The website should preferably talk to one unified gateway or backend aggregator.
- The gateway should fan out to module APIs where necessary.
- The UI should not hardwire direct calls to private module internals.

### 3. Role-Based Views

The website must support distinct views for:

- Admin
- Farmer
- Manufacturer
- Distributor
- Retailer
- Consumer

Each role must only see actions and data relevant to that role.

### 4. Traceability First

- The website must show product history from origin to consumer.
- Operational records must come from the database.
- Verification proofs must come from blockchain.
- ML outputs must be displayed as predictions, not as authoritative ledger state.

---

## Supply Chain Rules

The website must preserve the real agricultural supply chain lifecycle:

1. Crop created or registered
2. Product harvested
3. Product processed
4. Product packaged
5. Product shipped
6. Product received
7. Product sold
8. Product verified

Any dashboard or workflow screen must map to this lifecycle.

Invalid transitions must be blocked in the UI and in the backend.

The website must never treat blockchain as the operational database.

---

## ML Integration Rules

The website must use ML outputs carefully:

- Predictions are decision support, not final business truth.
- The website must display confidence and model metadata where available.
- The website must not modify model training flow unless a verified issue exists.
- The website must not duplicate preprocessing logic.
- The website must not bypass existing prediction services.

### Verified Change Rule for ML

The ML code may be touched only if:

- it has a confirmed error,
- it fails to produce the intended result,
- it causes an import/runtime conflict,
- and the fix is minimal, isolated, and compatible with the repository structure.

Before any ML change:

- inspect related files first,
- verify the issue,
- confirm no module conflict,
- confirm no duplicate implementation already exists,
- confirm the change will not break another actor module.

---

## Blockchain Integration Rules

The website must treat blockchain as a verification layer only.

Rules:

- Never store raw operational state only on-chain.
- Never store full dataset content on-chain.
- Never expose private keys in the website.
- Never call blockchain code directly from UI code.
- Always route blockchain actions through a dedicated service or wrapper.

Blockchain should be used for:

- proof hashes
- ownership history
- shipment events
- verification records
- fraud flags

If blockchain is unavailable, the website must fail gracefully and keep the rest of the system functional.

---

## Database Rules

The database is the operational source of truth.

The website must use the database for:

- users
- roles
- products
- shipments
- predictions
- uploaded files
- reports
- audit logs
- model run history

The website must not use blockchain as the primary database.

The website must not duplicate authoritative state between database and blockchain.

Database writes must be synchronized with blockchain proofs where applicable, but the database remains the live system of record.

---

## API Rules

### 1. Unified API Contract

- The website must use consistent request and response shapes.
- Responses must be structured and predictable.
- Error responses must be standardized.

### 2. Thin Routes

- API routes must remain thin.
- Routes must validate input.
- Routes must delegate to services.
- Routes must not contain heavy business logic.

### 3. Compatibility

- New endpoints must not break existing module endpoints.
- Existing module contracts must remain compatible with the gateway.
- If a response shape changes, downstream consumers must be updated together.

### 4. Documentation

- Every public endpoint used by the website must be documented.
- Each role-based page must map to one or more documented API endpoints.

### 5. Existing vs Target API Rule

If existing module APIs differ from the target website contract, the website backend must add an adapter or gateway facade.

Do not rewrite working ML or blockchain APIs just to match the frontend.

---

## UI Rules

The website must:

- be responsive on desktop and mobile
- show module status clearly
- separate operational views from analytics views
- show loading, success, and error states
- show validation feedback for user input
- show traceability history in a readable timeline or table

The website must not:

- hide critical errors
- misrepresent model predictions as guaranteed truth
- mix blockchain events and database records without labeling their source
- expose raw internal stack traces to users

---

## Verification Rules

Before a website feature is considered complete:

1. Confirm the API endpoint exists and responds correctly.
2. Confirm the database read/write path is correct.
3. Confirm the blockchain path is isolated and optional where needed.
4. Confirm the ML service returns the expected output.
5. Confirm the feature does not break another module.
6. Confirm the feature respects repository structure.

No feature is complete if it only works in isolation but breaks the system as a whole.

---

## Website Readiness Definition

The website documentation is considered complete only when it defines:

- frontend folders and ownership
- page map and route map
- role permissions
- dashboard requirements
- API contracts
- database entities
- user journeys
- blockchain verification boundaries
- ML integration boundaries
- testing checklist
- deployment environment
- monitoring and logging

If any item is missing, the implementation is not ready to begin as a full website build.

---

## Change Control Rules

### Allowed Changes

- New website pages
- New frontend components
- New API aggregation routes
- New dashboard views
- New database models for website usage
- New integration adapters

### Restricted Changes

- ML code changes are restricted to verified defects or wrong outputs.
- Blockchain code changes are restricted to verified defects or wrong outputs.
- Shared contract or model interfaces must not be changed casually.

### Disallowed Changes

- Duplicate modules
- Duplicate routes
- Hardcoded machine paths
- Circular imports
- Temporary hacks
- Placeholder production logic
- Unverified rewrites of working code

---

## Repository Compatibility Rules

The website must remain compatible with the current project layout.

- Do not move files without reason.
- Do not break module import paths.
- Do not introduce a conflicting architecture.
- Do not create a second unrelated application structure.
- Do not duplicate logic that already exists in the modules.

If a new file is added, it must fit the existing architecture and naming style.

---

## Module Priority Order for Website Work

When implementing or reviewing website work, use this order:

1. Common configuration and shared helpers
2. Supply-chain flow mapping
3. ML module integration
4. API gateway integration
5. Database persistence
6. Blockchain verification hooks
7. UI dashboards
8. Reports and analytics

This order must not be reversed casually, because it keeps the website aligned with the existing codebase.

---

## Safety Rules

- Never change a working ML module just because the website needs a different shape.
- Never change blockchain behavior just because the UI is incomplete.
- Never add code that depends on an unverified module import.
- Never assume a missing file exists unless it has been confirmed.
- Never introduce a website feature that cannot be traced back to the backend source of truth.

---

## Golden Rule

If a website change risks:

- breaking ML modules
- breaking blockchain verification
- creating duplicate logic
- violating the repository structure
- causing runtime errors
- making the system inconsistent

then do not apply the change until the risk is resolved and verified.
