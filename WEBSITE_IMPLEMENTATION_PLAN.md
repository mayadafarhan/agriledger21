# WEBSITE_IMPLEMENTATION_PLAN.md - AgriLedger Website Implementation Plan

## Purpose

This document defines the safe implementation order for building the AgriLedger website.

The order protects the existing ML and blockchain modules while allowing the web application to grow into a full product.

---

## Phase 0 - Readiness Review

Complete before coding:

- read all website documentation
- inspect existing module APIs
- confirm current gateway behavior
- confirm database choice
- confirm frontend framework
- confirm auth strategy

Do not modify ML or blockchain files in this phase.

---

## Phase 1 - Web Backend Foundation

Build:

- auth routes
- RBAC dependencies
- database connection
- base schemas
- response envelope
- error handling

Acceptance:

- login and register contracts are defined
- protected endpoints reject unauthenticated users
- role checks are tested

---

## Phase 2 - Database and Operational Records

Build:

- users
- products
- shipments
- predictions
- blockchain receipts
- audit events

Acceptance:

- product records can be created and read
- shipment records can be updated
- audit events are saved

---

## Phase 3 - Existing Module Integration

Integrate:

- farmer API
- manufacturer API
- distributor API
- retailer API
- consumer API

Acceptance:

- health checks work through gateway
- predictions can be requested through a facade
- module failures are isolated

---

## Phase 4 - Blockchain Verification Integration

Integrate:

- crop registration proof
- ownership transfer proof
- shipment update proof
- product verification
- QR payload generation
- fraud flagging

Acceptance:

- blockchain receipts are saved
- simulation mode works
- blockchain failures do not crash the website

---

## Phase 5 - Frontend Shell

Build:

- app layout
- login
- register
- route guards
- role-based navigation
- dashboard shell

Acceptance:

- role redirects work
- unauthorized routes are blocked
- frontend services call backend contracts only

---

## Phase 6 - Role Dashboards

Build:

- admin dashboard
- farmer dashboard
- manufacturer dashboard
- distributor dashboard
- retailer dashboard
- consumer dashboard

Acceptance:

- dashboard metrics have sources
- loading and error states exist
- health panels render unavailable states correctly

---

## Phase 7 - Core Screens

Build:

- products
- product detail
- shipments
- shipment detail
- predictions
- blockchain verification
- QR scanner
- reports
- settings
- profile

Acceptance:

- every screen maps to `UI_SCREEN_MAP.md`
- every screen uses documented API contracts
- no screen depends on fake data in production mode

---

## Phase 8 - QA and Hardening

Complete:

- API tests
- frontend route tests
- role access tests
- failure mode tests
- responsive UI checks
- deployment smoke test

Acceptance:

- app starts cleanly
- critical user journeys work
- ML and blockchain modules remain intact

---

## Do Not Start With

- visual-only dashboard mockups
- direct Web3 frontend calls
- direct ML file imports from frontend or web backend
- training UI for normal users
- a new architecture that bypasses the existing modules

