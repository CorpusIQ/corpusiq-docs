# Error Codes

All CorpusIQ API errors follow a consistent JSON structure with a machine-readable `type` field and a human-readable `message`. Use the `type` field for programmatic error handling.

## Error Response Format

```json
{
  "error": {
    "type": "unauthorized",
    "message": "Invalid or expired Bearer token"
  }
}
```

## Error Types

| HTTP Status | `type` | Description |
|-------------|--------|-------------|
| **400** | `bad_request` | The request body is malformed, missing required fields, or contains invalid values. Check the `details` field for field-level errors. |
| **401** | `unauthorized` | The Bearer token is missing, invalid, or expired. Obtain a new token. An `X-Token-Expired: true` header accompanies expired tokens. |
| **403** | `forbidden` | The authenticated user does not have permission to access the requested resource or connector. Verify connector OAuth scopes. |
| **404** | `not_found` | The requested resource (query ID, connector, or endpoint) does not exist. Check the URL and resource identifiers. |
| **409** | `conflict` | The request conflicts with the current state. Common for duplicate `Idempotency-Key` submissions with different request bodies. |
| **413** | `payload_too_large` | The request body exceeds the maximum allowed size of 1 MB. Reduce `max_results` or split the query. |
| **429** | `rate_limited` | The rate limit for the endpoint has been exceeded. A `retry_after_seconds` field indicates when to retry. See [Rate Limits](/docs/api/rate-limits). |
| **500** | `server_error` | An unexpected internal error occurred on the CorpusIQ side. Retry with exponential backoff. If errors persist, contact api@corpusiq.io. |

## Handling Errors Programmatically

### Retry Logic for 429 Rate Limited

When you receive a `429 Too Many Requests`, inspect the `retry_after_seconds` field:

```python
import time

response = requests.post("https://api.corpusiq.io/v1/query", ...)

if response.status_code == 429:
    retry_after = response.json()["error"].get("retry_after_seconds", 60)
    time.sleep(retry_after)
    response = requests.post("https://api.corpusiq.io/v1/query", ...)
```

### Handling 401 Token Expiry

```javascript
let response = await fetch("https://api.corpusiq.io/v1/query", {
  headers: { Authorization: `Bearer ${token}` },
});

if (response.status === 401 && response.headers.get("X-Token-Expired")) {
  token = await refreshToken(); // Re-authenticate
  response = await fetch("https://api.corpusiq.io/v1/query", {
    headers: { Authorization: `Bearer ${token}` },
  });
}
```

### Retry with Exponential Backoff for 500 Errors

For transient server errors, implement exponential backoff:

```python
import time
import requests

max_retries = 3
for attempt in range(max_retries):
    response = requests.post("https://api.corpusiq.io/v1/query", ...)
    if response.status_code < 500:
        break
    if attempt < max_retries - 1:
        wait = 2 ** attempt
        time.sleep(wait)
```

## Idempotency and 409 Conflicts

A `409 Conflict` with `Idempotency-Key` means the same key was used with a different request body. Generate a new key for each unique request. If the request body is identical, the API returns the cached response with a `200` status.
