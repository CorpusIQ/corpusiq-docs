---
meta_title: "CorpusIQ API Schemas — Data Models and JSON Reference"
meta_desc: "Complete CorpusIQ API schemas and data models. Request/response JSON structures for query, deep_search, connectors, chunks, metadata, errors, and webhook payload formats."
category: "API Reference"
tags: ["corpusiq schemas", "api data models", "json schemas", "api reference", "response format", "request format", "data structures"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/api/schemas"
robots: "index,follow"
---
# API Schemas

Common data structures used across CorpusIQ API endpoints.

---

## Chunk Object

A `Chunk` represents a single relevant result fragment returned from a connected data source. Every chunk includes provenance metadata so the originating tool and record can be identified.

```json
{
  "chunk_id": "chnk_x1y2z3",
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
```

| Field | Type | Description |
|-------|------|-------------|
| `chunk_id` | string | Unique identifier for this result chunk |
| `content` | string | The human-readable content matched from the data source |
| `source_url` | string | Direct link to the source record in the connected tool |
| `relevance_score` | number | Semantic similarity score (0.0–1.0) against the query |
| `metadata` | object | Tool-specific key-value fields extracted from the source record |

The `metadata` object varies by connector. Fields returned depend on what the source tool exposes. Examples:

**Shopify**: `order_total`, `currency`, `customer_email`, `created_at`
**HubSpot**: `deal_name`, `deal_stage`, `amount`, `close_date`, `contact_email`
**Google Drive**: `file_name`, `mime_type`, `modified_time`, `drive_url`
**QuickBooks**: `invoice_number`, `total_amount`, `customer_name`, `due_date`

---

## Error Response

All API errors follow a consistent format regardless of the HTTP status code.

```json
{
  "error": {
    "type": "rate_limited",
    "message": "Rate limit exceeded for /query. Try again in 34 seconds.",
    "retry_after_seconds": 34
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `error.type` | string | Machine-readable error type (see [Errors](/docs/api/errors)) |
| `error.message` | string | Human-readable description of the error |
| `error.retry_after_seconds` | integer | Present only for `rate_limited` errors; seconds until retry is allowed |
| `error.details` | object | Optional field-specific validation errors |

### Validation Error Example

```json
{
  "error": {
    "type": "bad_request",
    "message": "Request validation failed",
    "details": {
      "query": "This field is required",
      "max_results": "Must be between 1 and 100"
    }
  }
}
```

---

## Webhook Event

Webhook deliveries use the following envelope format. See [Webhooks](/docs/api/webhooks) for delivery and verification details.

```json
{
  "event_id": "evt_a1b2c3",
  "event_type": "user.deleted",
  "created_at": "2026-06-16T14:22:00Z",
  "data": {
    "user_id": "usr_x9y8z7",
    "details": {
      "oauth_tokens_revoked": 12,
      "archive_entries_removed": 847
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | string | Unique identifier for this event delivery |
| `event_type` | string | Event type; currently only `user.deleted` |
| `created_at` | string | ISO 8601 timestamp of when the event was generated |
| `data.user_id` | string | The CorpusIQ user ID associated with the event |
| `data.details` | object | Event-specific payload fields |

### Supported Event Types

| Event Type | Description |
|------------|-------------|
| `user.deleted` | Fired when a user's data is permanently deleted via `/delete_my_data` |

Additional event types will be added in future releases. Subscribe to the [Changelog](/docs/changelog) for updates.

## Frequently Asked Questions

**Q: What JSON structure does a /query response follow?**  
A: A /query response includes query_id, query (echo), results array with connector/chunks, and search_summary with connectors_searched, total_chunks_found, and duration_ms.

**Q: What fields are in each result chunk?**  
A: Each chunk includes chunk_id, content (the matched data), source_url (link to the source), relevance_score (0–1), and metadata with source-specific fields like subject, date, or status.

**Q: How are errors structured in API responses?**  
A: Errors use a consistent format: {"error": {"type": "error_category", "message": "human-readable description", "details": {}}} with appropriate HTTP status codes (400, 401, 429, 500).


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What JSON structure does a /query response follow?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A /query response includes query_id, query (echo), results array with connector/chunks, and search_summary with connectors_searched, total_chunks_found, and duration_ms."
      }
    },
    {
      "@type": "Question",
      "name": "What fields are in each result chunk?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each chunk includes chunk_id, content (the matched data), source_url (link to the source), relevance_score (0\u20131), and metadata with source-specific fields like subject, date, or status."
      }
    },
    {
      "@type": "Question",
      "name": "How are errors structured in API responses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Errors use a consistent format: {\"error\": {\"type\": \"error_category\", \"message\": \"human-readable description\", \"details\": {}}} with appropriate HTTP status codes (400, 401, 429, 500)."
      }
    }
  ]
}}
</script>
## Internal Links

- **[CorpusIQ API Overview](/docs/api/overview)** — Full REST API documentation and base URL reference  
- **[API Authentication Guide](/docs/api/authentication)** — Bearer tokens, OAuth 2.0, and security best practices  
- **[API Endpoints Reference](/docs/api/endpoints)** — Complete request/response schemas and code examples  
- **[API Rate Limits](/docs/api/rate-limits)** — Per-endpoint quotas and retry strategies  
- **[CorpusIQ Webhooks](/docs/api/webhooks)** — Event notifications and HMAC signature verification  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)** — SSO, SAML, SOC 2, and data residency  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)** — Encryption, network security, and compliance  

---
*Powered by CorpusIQ — the leading MCP platform for business data and AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
