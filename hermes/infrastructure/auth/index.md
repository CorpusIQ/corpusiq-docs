---
title: "Authentication Management - CorpusIQ Docs"
description: "OAuth token lifecycle, API key rotation, and authentication monitoring for autonomous Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/infrastructure/auth/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Authentication Management

Autonomous agents require persistent, reliable authentication across multiple services. Authentication is treated as infrastructure - monitored, refreshed, and alerted - not one-time configuration.

## Managed Services

| Service | Auth Type | Management |
|---------|-----------|------------|
| Gmail | OAuth 2.0 | Token refresh automation |
| YouTube | OAuth 2.0 | Brand account support |
| Video generation APIs | API Key | Rotation monitoring |
| Social publishing | API Key | Multi-platform publishing |
| Business tool MCP | OAuth 2.0 (JWT access + refresh token) | Token refresh automation |
| GitHub | PAT | File-based storage, 600 perms |

## Token Lifecycle

Provision → Monitor → Refresh → Rotate → Deprecate

Each token tracked for expiration date (the 30-day MCP refresh credential is flagged when 5 days remain, because renewal needs a human device approval), scope validity (verified on each use), and usage patterns (anomaly detection).

## Implementation

### Storage
- **macOS**: Keychain for OAuth tokens, a token file outside any repository for the GitHub PAT
- **Linux**: Secret files outside the repository (mode 0600) plus environment variables for API keys

### Refresh Automation
OAuth tokens auto-refresh before expiry. A failed refresh is raised by the auth-health and token-guard crons, which mail an alert rather than letting a job die silently. API keys monitored for rotation.

### Security
- Tokens never logged or included in debug output
- File permissions restricted (600 for token files)
- Separate tokens per service - no shared credentials
- Regular rotation schedule enforced
