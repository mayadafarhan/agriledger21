# DEVELOPMENT_RULES.md — AgriLedger Engineering Standards

## Purpose

This document defines mandatory engineering, architecture, safety, and code quality rules for all contributors and AI agents working on the AgriLedger repository.

These rules MUST be followed before creating, modifying, or deleting any code.

---

# Core Development Principles

All code added to this repository must be:

- Clean
- Modular
- Scalable
- Maintainable
- Reusable
- Production-ready
- Fully runnable
- Conflict-free

Every implementation must preserve project stability and architecture consistency.

---

# Mandatory Architecture Rules

The existing repository structure is STRICT and must not be violated.

Every file must be placed in its correct location.

## Allowed Structure

```text
app/
├── api/
├── ml/
├── core/
├── schemas/
├── services/
├── models/
├── utils/
└── __init__.py
```

---

# Folder Responsibilities

## api/
Contains:
- FastAPI routers
- endpoints
- request/response handling

Must NOT contain:
- business logic
- ML training logic
- preprocessing logic

---

## services/
Contains:
- business logic
- prediction orchestration
- model execution
- workflow logic

---

## ml/
Contains:
- training pipelines
- preprocessing pipelines
- evaluation logic
- inference helpers
- feature engineering

---

## schemas/
Contains:
- Pydantic request schemas
- response schemas
- validation models

---

## core/
Contains:
- configuration
- environment settings
- security logic
- constants
- app initialization helpers

---

## utils/
Contains:
- reusable helper functions
- shared utilities
- generic helper methods

---

## models/
Contains:
- serialized models
- model weights
- checkpoints

---

# Conflict Prevention Rules

Before adding or modifying ANY code:

1. Analyze all related files in the module.
2. Check imports and dependencies.
3. Ensure no naming conflicts exist.
4. Ensure no duplicate routes exist.
5. Ensure no duplicate functions/classes exist.
6. Ensure no circular imports exist.
7. Ensure compatibility with all other modules.
8. Ensure no existing functionality is broken.
9. Ensure API contracts remain compatible.
10. Ensure dependency versions remain compatible.

---

# Runtime Validation Rules

Any generated or modified code MUST:

- Run successfully
- Pass syntax validation
- Import successfully
- Execute without runtime exceptions
- Produce the expected output
- Avoid placeholder implementations
- Avoid fake or mocked logic unless explicitly requested

No broken code is allowed.

---

# FastAPI Rules

Every API implementation MUST:

- Use APIRouter
- Use Pydantic schemas
- Separate business logic into services/
- Return structured JSON responses
- Use proper exception handling
- Avoid logic directly inside routes

Routes should remain thin.

---

# Machine Learning Rules

ML implementations MUST:

- Separate training from inference
- Save trained models inside models/
- Save metrics inside:
  src/reports/metrics/

- Save plots and figures inside:
  src/reports/figures/

- Avoid hardcoded dataset paths
- Use reusable preprocessing pipelines
- Prevent data leakage
- Use deterministic random states where applicable

---

# Clean Code Rules

All code MUST follow Clean Code principles.

## Naming

Use:
- meaningful names
- descriptive variables
- readable function names

Avoid:
- vague names
- single-letter variables
- unnecessary abbreviations

---

## Functions

Functions MUST:
- be small
- have a single responsibility
- avoid deep nesting
- avoid duplicated logic

---

## Imports

- Remove unused imports
- Avoid wildcard imports
- Use consistent import style
- Prefer absolute imports where possible

---

## Comments

- Add comments only when necessary
- Do not explain obvious code
- Keep comments updated

---

## Formatting

Code MUST:
- follow PEP8
- use type hints when possible
- maintain consistent spacing and formatting

---

# File Modification Rules

Contributors and AI agents MUST NOT:

- modify unrelated files
- move files without reason
- break existing APIs
- bypass architecture rules
- duplicate logic
- introduce temporary hacks
- use sys.path manipulation
- commit unfinished logic
- leave TODOs in production code

---

# Testing Rules

Before finalizing ANY feature:

- Verify all imports work
- Verify APIs start correctly
- Verify models load correctly
- Verify inference works
- Verify no runtime errors exist
- Verify outputs are correct
- Verify training pipelines run successfully
- Verify no module conflicts exist

---

# Dependency Rules

Before adding dependencies:

1. Check if the dependency already exists.
2. Ensure compatibility with existing requirements.
3. Add dependencies to the correct requirements file:
   - base.txt
   - ml.txt
   - api.txt
   - blockchain.txt
   - dev.txt

Avoid unnecessary packages.

---

# Path Rules

Never use:
- hardcoded Windows paths
- absolute local machine paths

Always use:
- pathlib.Path
- environment variables
- relative project paths

---

# AI Agent Mandatory Behavior

AI coding agents MUST:

- inspect related files before editing
- preserve repository structure
- maintain compatibility across modules
- avoid introducing regressions
- generate production-ready code only
- ensure generated code is executable
- avoid assumptions about missing files
- verify imports before finalizing changes

---

# Reports & Metrics Rules

Evaluation outputs MUST be saved in:

```text
src/reports/metrics/<ModuleName>/
src/reports/figures/<ModuleName>/
```

Examples:
- confusion_matrix.png
- roc_curve.png
- feature_importance.png
- metrics.json
- classification_report.txt

---

# Golden Rule

If a change risks:
- breaking another module
- causing import conflicts
- violating architecture
- introducing runtime errors
- reducing code quality

DO NOT APPLY THE CHANGE.