---
title: "CorpusIQ API Reference — REST, Auth, and SDKs"
description: "Complete CorpusIQ API reference: authentication, endpoints, rate limits, error codes, OpenAPI spec, schemas, and webhooks. Everything you need to integrate with the CorpusIQ API."
category: "API Reference"
tags: ["corpusiq api", "rest api", "api documentation", "api authentication", "api endpoints", "api reference", "openapi"]
last_updated: "2026-07-04"
robots: "index,follow"
---

# CorpusIQ API Reference

Full REST API documentation for programmatic access to CorpusIQ. Authenticate with bearer tokens, query your connected business tools, and manage user data — all through a JSON API at `https://mcp2.corpusiq.io/mcp`.

## Quick Links

| Page | Description |
|------|-------------|
| [API Overview](overview.md) | Authentication, base URL, endpoints summary, quickstart examples in cURL/Python/JavaScript |
| [Authentication](authentication.md) | Bearer tokens, OAuth 2.0 device flow, token management, refresh detection, revocation |
| [Endpoints](endpoints.md) | Complete endpoint reference with request/response schemas and code examples |
| [Rate Limits](rate-limits.md) | Per-endpoint quotas, rate limit headers, retry strategies, 429 handling |
| [Error Codes](errors.md) | HTTP status codes, error types, troubleshooting guidance |
| [OpenAPI Spec](openapi.md) | OpenAPI 3.0.3 specification for Postman, Insomnia, and Swagger UI |
| [Schemas](schemas.md) | Data models, JSON structures for requests and responses |
| [Webhooks](webhooks.md) | Event notifications, HMAC-SHA256 signature verification, retry with exponential backoff |

## Base URL

```
https://mcp2.corpusiq.io/mcp
```

## Authentication

All API requests require a Bearer token in the `Authorization` header:

```bash
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
     https://mcp2.corpusiq.io/mcp
```

See [Authentication](authentication.md) for token creation, OAuth flow, and security best practices.

## Core Endpoints

```bash
# Query your connected business tools
POST /query

# Deep search across encrypted archives
POST /deep_search

# Delete your data and account
DELETE /delete_my_data
```

Full endpoint documentation with request/response examples: [Endpoints](endpoints.md)

---

*← [Docs Home](/docs/) | [Next: API Overview →](overview.md)*
