# API

CorpusIQ exposes a REST API for managing connectors, running queries, and configuring your account programmatically.

## Overview

The CorpusIQ API lets you automate everything you can do in the dashboard. Connect data sources, run cross-source queries, and manage your account — all via HTTP.

Base URL: `https://api.corpusiq.io/v1`

## Key Capabilities

- **Connector management** — Add, remove, and configure data source connections
- **Query execution** — Run natural language or structured queries across connected sources
- **Account management** — Manage users, teams, and permissions
- **Webhooks** — Get notified when data changes or queries complete

## SDKs & Tools

The easiest way to use the API is through our MCP server, which gives your AI tools direct access:

```
https://mcp2.corpusiq.io/mcp
```

For programmatic access, see the sections below:

- [Authentication](api/authentication.md) — API keys and OAuth
- [Endpoints](api/endpoints.md) — Available API endpoints
- [Schemas](api/schemas.md) — Data models and types
- [Webhooks](api/webhooks.md) — Event subscriptions
- [Rate Limits](api/rate-limits.md) — Usage limits and throttling
- [Errors](api/errors.md) — Error codes and handling
- [OpenAPI](api/openapi.md) — OpenAPI specification
