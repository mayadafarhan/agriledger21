# UI_SCREEN_MAP.md - AgriLedger UI Screen Map

## Purpose

This document defines the required user interface screens for the AgriLedger web application.

If a screen is not listed here, it must not be assumed silently by implementation code.

---

## Public Screens

### 1. Landing

- project overview
- role entry points
- login and register access

Current runtime note: there is no dedicated `/landing` route yet; the entry experience is effectively provided by the auth shell and root redirect.

### 2. Login

- email or username
- password
- role-aware redirect

### 3. Register

- account creation
- role selection if allowed
- validation feedback

---

## Core Screens

### 4. Dashboard

- role-specific summary
- recent activity
- health cards
- navigation to actor functions

Route: `/dashboard`

### 5. Products

- product list
- product detail
- lifecycle status
- traceability data

Routes:

- `/products`
- `/products/:productId`

### 6. Inventory

- stock list
- stock detail
- quantity adjustments
- reorder pressure

Routes:

- `/inventory`
- `/inventory/:itemId`

### 7. Shipments

- shipment list
- shipment detail
- route tracking
- shipment state history

Routes:

- `/shipments`
- `/shipments/:shipmentId`

### 8. Predictions

- input form
- model output
- confidence values
- prediction history

Routes:

- `/predictions`
- `/predictions/:module`

### 9. Blockchain Verification

- proof lookup
- transaction hash view
- verification timeline
- audit records

Routes:

- `/verify`
- `/verify/:productId`

### 10. QR Scanner

- scan QR code
- open verification result
- open product history

Current runtime note: there is no dedicated `/qr-scanner` route yet; QR actions are exposed inside the Verification screen.

### 11. Audit Trail

- merged traceability view
- audit events
- blockchain receipts
- model runs
- search and filter

Route: `/audit`

Note: this view is a traceability subview backed by reporting and verification data. It must not introduce a separate business journey.

### 12. Notifications

- notification list
- unread state
- mark read
- mark all read

Route: `/notifications`

### 13. Reports

- metrics
- evaluation charts
- exportable summaries

Route: `/reports`

### 14. Users

- user directory
- role data
- status management

Route: `/users`

### 15. Settings

- preferences
- security settings
- notification settings

Route: `/settings`

### 16. Profile

- account data
- role data
- session info

Route: `/profile`

---

## Required Detail Screens

### Product Detail

- product metadata
- lifecycle timeline
- prediction summary
- blockchain proof
- QR payload

### Shipment Detail

- shipment status
- route timeline
- delay prediction
- shipment proof event

### Prediction Detail

- submitted input summary
- model output
- confidence
- model metadata
- related product or shipment

### Report Detail

- metric source
- generated timestamp
- model or module name
- export option if supported

---

## Role-Specific Screen Mapping

### Admin

- Dashboard
- Products
- Inventory
- Shipments
- Predictions
- Blockchain Verification
- Audit Trail
- Notifications
- Users
- Reports
- Settings
- Profile

### Farmer

- Dashboard
- Products
- Predictions
- Blockchain Verification
- Audit Trail
- Profile

### Manufacturer

- Dashboard
- Products
- Inventory
- Shipments
- Predictions
- Blockchain Verification
- Audit Trail
- Reports
- Profile

### Distributor

- Dashboard
- Shipments
- Predictions
- Blockchain Verification
- Audit Trail
- Reports
- Profile

### Retailer

- Dashboard
- Products
- Inventory
- Shipments
- Predictions
- Blockchain Verification
- Audit Trail
- Reports
- Profile

### Consumer

- Dashboard
- Blockchain Verification
- Products
- Audit Trail
- Profile

---

## Screen Behavior Rules

- Every screen must map to a real backend capability.
- Screens must not be added without a defined data source.
- Screens must not duplicate the same business action in multiple places.
- Screens must show source labels when data comes from ML or blockchain.
- Screens must handle unauthorized access with a clear redirect or access denied state.
- Screens must handle unavailable backend modules gracefully.
