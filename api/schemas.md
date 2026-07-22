# API Schemas

Data models used across the CorpusIQ API.

## Connector

```json
{
  "id": "conn_abc123",
  "name": "Shopify",
  "status": "active",
  "connected_at": "2026-07-22T12:00:00Z",
  "last_sync": "2026-07-22T14:30:00Z"
}
```

## Query

```json
{
  "id": "qry_xyz789",
  "text": "What was my ROAS last month?",
  "status": "completed",
  "sources": ["meta_ads", "shopify"],
  "created_at": "2026-07-22T12:00:00Z",
  "completed_at": "2026-07-22T12:00:14Z",
  "result": {
    "answer": "Your ROAS across Meta Ads and Shopify was 3.2x last month...",
    "cited_sources": 4
  }
}
```

## Account

```json
{
  "id": "acct_001",
  "email": "user@example.com",
  "plan": "pro",
  "connectors_active": 12,
  "queries_this_month": 342
}
```

For the complete OpenAPI 3.1 schema, see [OpenAPI](openapi.md).
