# FRONTEND_ARCHITECTURE.md - AgriLedger Frontend Architecture

## Purpose

This document defines the required frontend architecture for the AgriLedger web application.

The frontend must reflect the agricultural supply-chain flow, integrate with the backend gateway, and remain compatible with the existing module structure.

It must not duplicate ML logic, blockchain logic, or database logic.

---

## Required Folder Structure

```text
frontend/
│
├── pages/
├── layouts/
├── components/
├── services/
├── hooks/
├── store/
├── routes/
├── dashboards/
└── blockchain/
```

Optional supporting folders are allowed only when the project needs them:

```text
frontend/
├── assets/
├── styles/
├── types/
├── utils/
└── tests/
```

These optional folders must not replace the required folders above.

---

## Folder Responsibilities

### pages/
Contains route-level pages only.

Examples:

- landing page
- login
- register
- dashboards
- products
- shipments
- predictions
- blockchain verification
- reports
- settings
- profile

Pages must stay thin and delegate business behavior to services, hooks, and store modules.

### layouts/
Contains shared page shells and structural wrappers.

Examples:

- authenticated layout
- public layout
- role-based dashboard layout
- admin layout

Layouts must not contain business logic.

### components/
Contains reusable UI pieces.

Examples:

- buttons
- tables
- cards
- status badges
- forms
- timeline views
- charts
- QR display widgets

Components must be reusable and presentation-focused.

### services/
Contains frontend API adapters and request orchestration.

Examples:

- auth service
- product service
- shipment service
- prediction service
- blockchain verification service
- report service

Services must call the backend, not internal ML or blockchain code directly.

Every service must map to `API_CONTRACTS.md`.

### hooks/
Contains reusable UI hooks.

Examples:

- authentication state hook
- dashboard data hook
- form state hook
- pagination hook
- websocket or polling hook

Hooks must not contain backend business rules.

### store/
Contains frontend state management.

Examples:

- user session state
- role state
- dashboard state
- notifications
- product traces
- prediction results

The store must reflect backend truth, not replace it.

### routes/
Contains route definitions and access guards.

Examples:

- public routes
- protected routes
- role-based route guards
- redirect rules

Routes must map to `UI_SCREEN_MAP.md`.

### dashboards/
Contains dashboard-specific UI composition.

Examples:

- admin dashboard
- farmer dashboard
- manufacturer dashboard
- distributor dashboard
- retailer dashboard
- consumer dashboard

### blockchain/
Contains UI helpers for blockchain-facing features only.

Examples:

- proof display widgets
- transaction hash renderers
- verification status cards
- audit timeline views

This folder must not contain smart contract logic.

---

## Recommended Page Modules

The first website implementation should define these page modules:

- `pages/Login`
- `pages/Register`
- `pages/Dashboard`
- `pages/Products`
- `pages/ProductDetail`
- `pages/Shipments`
- `pages/Predictions`
- `pages/BlockchainVerification`
- `pages/QRScanner`
- `pages/Reports`
- `pages/Settings`
- `pages/Profile`

Role-specific dashboards should live in `dashboards/`, not inside generic pages.

---

## Required Frontend Services

- `authService`
- `dashboardService`
- `productService`
- `shipmentService`
- `predictionService`
- `blockchainService`
- `reportService`
- `healthService`

No component should call `fetch` or an HTTP client directly unless it is inside a service.

---

## State Management Rules

The store should hold:

- current user
- current role
- auth token metadata
- active dashboard filters
- temporary prediction results
- notification state

The store should not hold:

- permanent product records
- blockchain source of truth
- ML model artifacts
- database replacement copies

---

## Frontend Design Rules

1. The frontend must be role-aware.
2. The frontend must support mobile and desktop layouts.
3. The frontend must show traceability clearly.
4. The frontend must keep operational data separate from verification data.
5. The frontend must clearly label ML predictions as predictions.
6. The frontend must clearly label blockchain proofs as verification artifacts.
7. The frontend must not guess screen flows that are not defined in this documentation.

---

## Data Flow Rules

The frontend must follow this order:

1. User authenticates.
2. Role is resolved.
3. Route guards select allowed views.
4. Dashboard data is fetched from backend services.
5. ML predictions are requested through API services.
6. Blockchain proofs are fetched or generated through service wrappers.
7. Results are rendered in the UI.

The frontend must not call internal module code directly.

---

## Architecture Boundaries

- UI code stays in `pages/`, `components/`, `layouts/`, and `dashboards/`.
- API communication stays in `services/`.
- Shared client state stays in `store/`.
- Route rules stay in `routes/`.
- Blockchain UI wrappers stay in `blockchain/`.

No folder may duplicate another folder's responsibility.

---

## Safety Rules

- Do not bypass the backend gateway.
- Do not duplicate module business logic in the frontend.
- Do not hardcode machine-specific paths.
- Do not invent endpoints that are not specified in API contracts.
- Do not create screens that cannot be backed by real data.
- Do not store private keys, mnemonics, RPC credentials, or database secrets in frontend code.
