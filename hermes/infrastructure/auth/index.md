---
title: Authentication Management
description: "OAuth token lifecycle, API key rotation, and authentication monitoring for autonomous Hermes agents."
---

# Authentication Management

Autonomous agents require persistent, reliable authentication across multiple services. Authentication is treated as infrastructure — monitored, refreshed, and alerted — not one-time configuration.

## Managed Services

| Service | Auth Type | Management |
|---------|-----------|------------|
| Gmail | OAuth 2.0 | Token refresh automation |
| YouTube | OAuth 2.0 | Brand account support |
| Video generation APIs | API Key | Rotation monitoring |
| Social publishing | API Key | Multi-platform publishing |
| Business tool MCP | OAuth 2.0 | Client credentials |
| GitHub | PAT | File-based storage, 600 perms |

## Token Lifecycle

Provision → Monitor → Refresh → Rotate → Deprecate

Each token tracked for expiration date (alerted 7 days before), scope validity (verified on each use), and usage patterns (anomaly detection).

## Implementation

### Storage
- **macOS**: Keychain for OAuth tokens, `~/.github-token` for GitHub PAT
- **Linux**: Environment variables for API keys

### Refresh Automation
OAuth tokens auto-refresh before expiry. Failures trigger P1 alerts. API keys monitored for rotation.

### Security
- Tokens never logged or included in debug output
- File permissions restricted (600 for token files)
- Separate tokens per service — no shared credentials
- Regular rotation schedule enforced
