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
