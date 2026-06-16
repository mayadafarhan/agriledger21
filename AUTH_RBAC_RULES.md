# AUTH_RBAC_RULES.md - AgriLedger Authentication and RBAC Rules

## Purpose

This document defines authentication and role-based access control rules for the AgriLedger website.

No website implementation is complete without role-aware routing, API authorization, and protected data access.

---

## Roles

Required roles:

- admin
- farmer
- manufacturer
- distributor
- retailer
- consumer

Role names must stay consistent across frontend, backend, database, and blockchain adapters.

---

## Authentication Rules

- Passwords must be hashed.
- Tokens must be signed server-side.
- Private keys must never be sent to the frontend.
- Login must return user identity, role, and token metadata.
- Logout must clear local session state.
- Expired sessions must redirect to login.
- Failed login must not reveal whether email or password was wrong.

---

## Frontend Route Access

### Public

- login
- register
- public product verification if allowed

### Authenticated

- dashboard
- products
- inventory
- shipments
- predictions
- verification
- notifications
- audit
- reports
- settings
- profile

### Consumer

- product verification
- product history
- QR actions inside verification

### Admin

- all dashboards
- users
- system health
- fraud alerts
- model health
- blockchain health
- audit
- reports

---

## Permission Matrix

| Action | Admin | Farmer | Manufacturer | Distributor | Retailer | Consumer |
|---|---|---|---|---|---|---|
| View own dashboard | Yes | Yes | Yes | Yes | Yes | Yes |
| View all dashboards | Yes | No | No | No | No | No |
| Register crop | Yes | Yes | No | No | No | No |
| Create batch | Yes | No | Yes | No | No | No |
| Create shipment | Yes | No | No | Yes | No | No |
| Update shipment | Yes | No | No | Yes | No | No |
| Manage inventory | Yes | No | No | No | Yes | No |
| Run prediction | Yes | Yes | Yes | Yes | Yes | Limited |
| Verify product | Yes | Yes | Yes | Yes | Yes | Yes |
| Flag fraud | Yes | No | Yes | Yes | Yes | Yes |
| View reports | Yes | Limited | Limited | Limited | Limited | No |
| View system health | Yes | No | No | No | No | No |

## Route Enforcement Notes

- `GET /api/dashboard/summary` must require authentication.
- `GET /dashboard/*` role-specific routes must enforce backend role checks.
- `POST /products`, `PUT /products/{id}`, and `DELETE /products/{id}` are admin-only.
- `GET /inventory` and `POST /inventory` are retailer/admin-facing operations.
- `POST /shipments` and shipment mutation routes are distributor/admin-facing operations.
- `POST /api/predict/{module}` must enforce module-to-role alignment.
- `GET /verification/products/{product_id}/history` and `/qr` must require authentication.
- `GET /reports` is authenticated and excluded for consumers.
- `GET /users` and user status changes are admin-only.

---

## Backend Authorization Rules

- Every protected endpoint must check authentication.
- Every role-specific endpoint must check role permission.
- The frontend route guard is not a security boundary.
- Backend services must validate ownership before returning private data.
- Admin access must be explicit, not inferred.

---

## Blockchain Authorization Rules

- Blockchain write actions must map to actor roles.
- The backend must decide whether a role is allowed to request a blockchain write.
- The frontend must never sign blockchain transactions directly for this MVP unless a wallet integration document is created.

---

## ML Authorization Rules

- Prediction endpoints must require authenticated users unless explicitly public.
- Training endpoints should be admin-only or disabled from the public website.
- Evaluation endpoints should be admin-only or restricted to technical users.

---

## Audit Rules

Audit events must be recorded for:

- login failures when appropriate
- crop registration
- shipment updates
- ownership transfer
- fraud flagging
- product verification
- model training trigger
- admin changes
