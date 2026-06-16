# SECURITY_RULES.md

## Purpose

This file defines blockchain security and secret-handling rules.

---

## Secrets

Never hardcode:

- private keys
- mnemonics
- RPC credentials
- contract deployment secrets

Always use environment variables.

---

## Failure Isolation

Blockchain errors must not break:

- FastAPI services
- ML inference
- prediction APIs
- dashboard rendering

Errors must be isolated with:

- exception boundaries
- retries where appropriate
- explicit fallback modes

