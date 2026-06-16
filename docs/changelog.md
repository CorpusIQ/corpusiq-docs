# Changelog

All notable changes to the CorpusIQ API are documented here. This project follows [Semantic Versioning](https://semver.org/).

---

## v1.0 — March 2026

### Initial API Release

The first public release of the CorpusIQ API, providing programmatic access to the platform's core query, archive search, and data management capabilities.

### New Endpoints

- **`POST /v1/query`** — Search across all connected business tools with natural-language queries. Supports connector scoping via the `connectors` parameter and idempotent submissions via the `Idempotency-Key` header. Returns semantically ranked, cited results from each matching connector.

- **`POST /v1/deep_search`** — Search the encrypted archive of previously executed queries and their results. Supports date-range filtering and returns similarity-scored matches.

- **`DELETE /v1/delete_my_data`** — Permanently delete all user data, including OAuth tokens, query history, archive entries, webhook registrations, and user profile. Triggers a `user.deleted` webhook event.

### Authentication

- Bearer token authentication via `Authorization` header
- 60-minute token expiry with server-side refresh detection
- Token issuance through the CorpusIQ Dashboard and ChatGPT Actions
- Immediate token revocation from the Dashboard

### OpenAPI Specification

- Complete OpenAPI 3.0.3 spec published at `https://api.corpusiq.io/v1/openapi.json`
- Importable into Postman, Insomnia, and Swagger UI
- Interactive documentation at `https://api.corpusiq.io/v1/docs`

### Webhooks

- Webhook delivery framework with HMAC-SHA256 signature verification
- `user.deleted` event type fired on data deletion
- Retry with exponential backoff: 60s → 5m → 15m → 1h
- Signed payloads via `CorpusIQ-Signature` header

### Rate Limiting

- Per-endpoint rate limits with minute and daily windows
- Rate limit headers on every response for self-monitoring
- `retry_after_seconds` field in `429` responses

### Security

- Read-only OAuth scopes across all connectors
- Zero data retention: embeddings deleted after each session
- TLS 1.3 for all API traffic
- AES-256-GCM encryption at rest
- SOC 2 Type II compliance program initiated

### Connectors

- 37+ native connectors spanning email, calendar, file storage, analytics, CRM, ecommerce, marketing, financial, social media, and databases
- Read-only OAuth for all cloud services
- Direct database connectors for PostgreSQL, SQL Server, MySQL, Azure Cosmos DB, and MongoDB

### Documentation

- Published [CorpusIQ Documentation](/docs/) covering API reference, authentication, rate limits, webhooks, security, and quick start
- Connector catalog with descriptions for all supported integrations
- Code examples in cURL, JavaScript, and Python for all endpoints

---

## Versioning Policy

| Version Component | Change Trigger |
|-------------------|----------------|
| **Major (X.0)** | Breaking changes to endpoint signatures, response schemas, or authentication |
| **Minor (1.X)** | New endpoints, new optional fields, new connector support |
| **Patch (1.0.X)** | Bug fixes, performance improvements, documentation updates |

CorpusIQ will provide at least 90 days' notice before deprecating any API version. Deprecated versions continue to function during the notice period with a `Deprecation` header on responses.
