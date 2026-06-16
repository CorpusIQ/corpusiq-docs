# Rate Limits

CorpusIQ enforces per-endpoint rate limits to ensure fair usage and system stability. Limits are applied per authenticated user and are measured in requests per minute and requests per day.

## Limit Tiers

| Endpoint | Per Minute | Per Day |
|----------|------------|---------|
| `POST /query` | 60 | 6,000 |
| `POST /deep_search` | 30 | 3,000 |
| `DELETE /delete_my_data` | 10 | 100 |

Rate limits are evaluated independently for each endpoint. A burst on `/query` does not affect your `/deep_search` allowance.

## Rate Limit Headers

Every API response includes rate limit headers indicating your current usage:

```http
X-RateLimit-Limit-Minute: 60
X-RateLimit-Remaining-Minute: 42
X-RateLimit-Reset-Minute: 1718551800
X-RateLimit-Limit-Day: 6000
X-RateLimit-Remaining-Day: 5891
X-RateLimit-Reset-Day: 1718582400
```

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit-Minute` | Maximum requests allowed in the current minute window |
| `X-RateLimit-Remaining-Minute` | Requests remaining in the current minute window |
| `X-RateLimit-Reset-Minute` | Unix timestamp when the minute window resets |
| `X-RateLimit-Limit-Day` | Maximum requests allowed in the current day window |
| `X-RateLimit-Remaining-Day` | Requests remaining in the current day window |
| `X-RateLimit-Reset-Day` | Unix timestamp when the day window resets |

## Exceeding Limits

When you exceed a rate limit, the API returns a `429 Too Many Requests` response:

```json
{
  "error": {
    "type": "rate_limited",
    "message": "Rate limit exceeded for /query. Try again in 34 seconds.",
    "retry_after_seconds": 34
  }
}
```

The `retry_after_seconds` field tells you exactly how long to wait before retrying. All subsequent requests within the cooldown period will also receive `429` responses.

## Best Practices

### Monitor Header Usage

Check `X-RateLimit-Remaining-Minute` before making burst requests. If remaining is low, pace your requests or wait for the window to reset.

```python
import time

response = requests.post("https://api.corpusiq.io/v1/query", ...)
remaining = int(response.headers.get("X-RateLimit-Remaining-Minute", 60))

if remaining < 5:
    time.sleep(10)  # Let the rate limit window catch up
```

### Use Idempotency Keys

For `/query`, use `Idempotency-Key` headers to safely retry without consuming additional rate limit quota. Duplicate requests with the same key within 24 hours return a cached response and do not count against your limit.

### Batch Questions

Rather than making many small queries, combine related questions into a single well-structured query when possible. A single `/query` with `max_results: 20` is more efficient than four queries with `max_results: 5`.

### Plan for Daily Quotas

The daily limits reset at midnight UTC. For high-volume use cases, distribute queries throughout the day. If you consistently approach daily limits, contact sales@corpusiq.io to discuss higher-tier plans.

## Rate Limit Increases

Enterprise plans include higher rate limits and custom quotas. For details, contact sales@corpusiq.io.
