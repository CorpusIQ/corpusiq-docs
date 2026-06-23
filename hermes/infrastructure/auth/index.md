---
title: Authentication Management
description: OAuth token lifecycle, API key rotation, and authentication monitoring for autonomous Hermes agents
---

# Authentication Management

Autonomous agents require persistent, reliable authentication across multiple services. Authentication is treated as infrastructure  --  monitored, refreshed, and alerted  --  not one-time configuration.

## Managed Services

| Service | Auth Type | Management |
|---------|-----------|------------|
| Gmail (team@, info@) | OAuth 2.0 | Token refresh automation |
| YouTube | OAuth 2.0 | Brand account support |
| HeyGen | API Key | Rotation monitoring |
| Postiz | API Key | Multi-platform publishing |
| CorpusIQ MCP | OAuth 2.0 | Client credentials |
| GitHub | PAT | File-based storage on Mac Mini |

## Token Lifecycle

Provision → Monitor → Refresh → Rotate → Deprecate

Each token tracked for expiration date (alerted 7 days before), scope validity (verified on each use), and usage patterns (anomaly detection).

## Implementation

### Storage
- **macOS**: Keychain for OAuth tokens, `~/.github-token` for GitHub PAT
- **Linux (DGX)**: Environment variables for API keys

### Refresh Automation
OAuth tokens auto-refresh before expiry. Failures trigger P1 alerts. API keys monitored for rotation.

### Security
- Tokens never logged or included in debug output
- File permissions restricted (600 for token files)
- Separate tokens per service  --  no shared credentials
- Regular rotation schedule enforced

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
