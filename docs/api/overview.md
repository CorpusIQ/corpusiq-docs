---
description: >-
  CorpusIQ REST API reference — query connected business tools, search
  encrypted archives, and manage user data over a Bearer-authenticated
  JSON API at https://api.corpusiq.io/v1.
---

# API Overview

CorpusIQ exposes a REST API at `https://api.corpusiq.io/v1` that allows AI assistants and client applications to query connected business tools, search encrypted archives, and manage user data. All requests are authenticated via Bearer tokens and respond with JSON.

## Base URL

```
https://api.corpusiq.io/v1
```

All endpoint paths are relative to this base. The API version (`v1`) is part of the URL path. Breaking changes will be released under a new version prefix.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/query` | Search across all connected data sources |
| `POST` | `/deep_search` | Search the encrypted archive of past queries and results |
| `DELETE` | `/delete_my_data` | Permanently delete all user data and tokens |

### POST /query

The primary endpoint for querying connected business tools. Accepts a natural-language question and an optional list of connector IDs to scope the search. CorpusIQ translates the query into read-only API calls, retrieves matching records, ranks them semantically, and returns cited results.

Each `/query` request generates a unique `query_id` that can be used for idempotency and debugging. The `Idempotency-Key` header protects against duplicate submissions.

### POST /deep_search

Searches the encrypted archive of previously executed queries and their results. This endpoint is useful for retrieving historical answers, auditing past queries, and discovering patterns across previous searches. The archive is encrypted at rest and indexed by embedding vectors.

Unlike `/query`, this endpoint does not make live calls to connected tools — it searches only the archive.

### DELETE /delete_my_data

Permanently deletes all data associated with the authenticated user, including:

- All OAuth tokens for connected services
- Query history and encrypted archive entries
- User profile and configuration
- Webhook registrations

This action is irreversible. A confirmation prompt is returned before deletion is executed.

## Response Format

All successful responses return HTTP `200` with a JSON body. Errors follow a consistent format with a `type` field identifying the error category and a `message` field with a human-readable description. See [Errors](/docs/api/errors) for the complete error reference.

## Content Type

All request and response bodies use `application/json`. Set the `Content-Type` header to `application/json` on all `POST` requests.

```http
Content-Type: application/json
Authorization: Bearer <token>
```

## Next Steps

- [Authentication](/docs/api/authentication) — Obtain and manage API tokens
- [Endpoints Reference](/docs/api/endpoints) — Full request/response schemas and code examples
- [Rate Limits](/docs/api/rate-limits) — Understand per-endpoint quotas
