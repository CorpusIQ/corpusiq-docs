# API Endpoints Reference

Complete reference for all CorpusIQ API endpoints with full request/response schemas and code examples.

---

## POST /query

Search across all connected data sources with a natural-language query.

### Request

```http
POST /v1/query
Content-Type: application/json
Authorization: Bearer <token>
Idempotency-Key: <unique-key>  (optional)
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `query` | string | Yes | Natural-language question to search across connected tools |
| `connectors` | string[] | No | List of connector IDs to scope the search; omit to search all |
| `max_results` | integer | No | Maximum results per connector (default: 10, max: 100) |

```json
{
  "query": "What were our top 5 Shopify orders this month?",
  "connectors": ["shopify"],
  "max_results": 5
}
```

### Response

```json
{
  "query_id": "qry_a1b2c3d4e5f6",
  "query": "What were our top 5 Shopify orders this month?",
  "results": [
    {
      "connector": "shopify",
      "source_label": "Shopify Orders",
      "chunks": [
        {
          "chunk_id": "chnk_x1y2",
          "content": "Order #12345 — $4,299.00 — Placed 2026-06-14 by customer@example.com",
          "source_url": "https://admin.shopify.com/store/.../orders/12345",
          "relevance_score": 0.98,
          "metadata": {
            "order_total": "4299.00",
            "currency": "USD",
            "customer_email": "customer@example.com",
            "created_at": "2026-06-14T10:30:00Z"
          }
        }
      ]
    }
  ],
  "search_summary": {
    "connectors_searched": 1,
    "total_chunks_found": 5,
    "duration_ms": 847
  }
}
```

### Idempotency

Pass an `Idempotency-Key` header to safely retry `/query` requests without creating duplicate query records. The key must be unique per request. Subsequent requests with the same key within 24 hours return the cached response.

```http
Idempotency-Key: req_2026-06-16_sales_report
```

### Code Examples

**cURL**

```bash
curl -X POST https://api.corpusiq.io/v1/query \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "query": "Show me recent HubSpot deals over $10,000",
    "connectors": ["hubspot"],
    "max_results": 5
  }'
```

**JavaScript**

```javascript
const response = await fetch("https://api.corpusiq.io/v1/query", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
    "Idempotency-Key": crypto.randomUUID(),
  },
  body: JSON.stringify({
    query: "Show me recent HubSpot deals over $10,000",
    connectors: ["hubspot"],
    max_results: 5,
  }),
});

const data = await response.json();
console.log(data.results);
```

**Python**

```python
import requests
import uuid

response = requests.post(
    "https://api.corpusiq.io/v1/query",
    headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4()),
    },
    json={
        "query": "Show me recent HubSpot deals over $10,000",
        "connectors": ["hubspot"],
        "max_results": 5,
    },
)

data = response.json()
for result in data["results"]:
    for chunk in result["chunks"]:
        print(chunk["content"])
```

---

## POST /deep_search

Search the encrypted archive of previously executed queries and results.

### Request

```http
POST /v1/deep_search
Content-Type: application/json
Authorization: Bearer <token>
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `query` | string | Yes | Search term to match against archived queries and results |
| `max_results` | integer | No | Maximum results (default: 20, max: 50) |
| `date_from` | string | No | ISO 8601 start date filter |
| `date_to` | string | No | ISO 8601 end date filter |

```json
{
  "query": "Q3 revenue projections",
  "max_results": 10,
  "date_from": "2026-01-01T00:00:00Z"
}
```

### Response

```json
{
  "query_id": "ds_a1b2c3d4e5",
  "query": "Q3 revenue projections",
  "archive_results": [
    {
      "original_query_id": "qry_abc123",
      "original_query": "What were our Q2 revenue projections from QuickBooks?",
      "matched_chunk": {
        "content": "Q2 projected revenue: $847,200 based on invoiced orders...",
        "source_connector": "quickbooks",
        "queried_at": "2026-04-15T14:22:00Z"
      },
      "similarity_score": 0.87
    }
  ],
  "total_matches": 1,
  "duration_ms": 312
}
```

### Code Examples

**cURL**

```bash
curl -X POST https://api.corpusiq.io/v1/deep_search \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Q3 revenue projections",
    "max_results": 10,
    "date_from": "2026-01-01T00:00:00Z"
  }'
```

**JavaScript**

```javascript
const response = await fetch("https://api.corpusiq.io/v1/deep_search", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    query: "Q3 revenue projections",
    max_results: 10,
    date_from: "2026-01-01T00:00:00Z",
  }),
});
```

**Python**

```python
import requests

response = requests.post(
    "https://api.corpusiq.io/v1/deep_search",
    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    json={
        "query": "Q3 revenue projections",
        "max_results": 10,
        "date_from": "2026-01-01T00:00:00Z",
    },
)
```

---

## DELETE /delete_my_data

Permanently delete all data associated with the authenticated user. This action is irreversible.

### Request

```http
DELETE /v1/delete_my_data
Authorization: Bearer <token>
```

No request body is required. The API returns a confirmation payload before executing deletion.

### Response

```json
{
  "status": "deletion_confirmed",
  "details": {
    "oauth_tokens_revoked": 12,
    "query_history_deleted": true,
    "archive_entries_removed": 847,
    "webhooks_unregistered": 2,
    "profile_deleted": true
  },
  "message": "All user data has been permanently deleted. This action cannot be undone."
}
```

### Code Examples

**cURL**

```bash
curl -X DELETE https://api.corpusiq.io/v1/delete_my_data \
  -H "Authorization: Bearer <token>"
```

**JavaScript**

```javascript
const response = await fetch("https://api.corpusiq.io/v1/delete_my_data", {
  method: "DELETE",
  headers: { Authorization: `Bearer ${token}` },
});
const result = await response.json();
console.log(result.message);
```

**Python**

```python
import requests

response = requests.delete(
    "https://api.corpusiq.io/v1/delete_my_data",
    headers={"Authorization": f"Bearer {token}"},
)
print(response.json()["message"])
```
