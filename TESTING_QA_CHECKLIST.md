# TESTING_QA_CHECKLIST.md - AgriLedger Website Testing and QA

## Purpose

This document defines the required testing checklist for the AgriLedger website.

No website feature should be considered complete until the relevant checks pass.

---

## Backend Tests

Required checks:

- app imports successfully
- API starts successfully
- auth routes work
- role guards work
- database connection works
- database migrations or schema setup work
- response envelopes are consistent
- errors are structured

---

## API Contract Tests

Required checks:

- `/api/dashboard/summary` returns expected shape
- prediction facade returns normalized output
- blockchain status returns controlled output
- product detail returns operational and verification sections
- unauthorized requests are rejected
- forbidden role access is rejected

---

## ML Integration Tests

Required checks:

- prediction endpoints are reachable through gateway
- model unavailable state is handled
- wrong input returns validation error
- prediction output includes model name or module identifier where available
- frontend does not call ML internals directly

Do not retrain models during normal website tests unless explicitly testing training.

---

## Blockchain Integration Tests

Required checks:

- simulation mode works
- crop registration proof can be created
- shipment update proof can be created
- product verification works
- QR payload can be generated
- blockchain failure returns controlled error

Do not expose private keys in tests.

---

## Database Tests

Required checks:

- product creation
- shipment update
- prediction persistence
- blockchain receipt persistence
- audit event persistence
- fraud alert persistence when used

---

## Frontend Tests

Required checks:

- login form validation
- role-based redirects
- protected routes
- dashboard loading state
- dashboard error state
- product detail render
- prediction result render
- QR verification render

---

## Responsive QA

Check at minimum:

- mobile narrow viewport
- tablet viewport
- desktop viewport

Required:

- no text overlap
- navigation remains usable
- tables have responsive behavior
- forms remain readable
- dashboards remain scannable

---

## User Journey QA

Validate:

- farmer journey
- manufacturer journey
- distributor journey
- retailer journey
- consumer journey
- admin journey

Each journey must be tested against `USER_JOURNEY.md`.

---

## Release Smoke Test

Before delivery:

1. Start backend.
2. Start frontend.
3. Login as each role.
4. Open each dashboard.
5. Run one prediction flow.
6. Run one verification flow.
7. Confirm blockchain failure isolation.
8. Confirm ML modules were not modified unnecessarily.

