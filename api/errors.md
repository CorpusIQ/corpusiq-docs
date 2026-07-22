# API Errors

The CorpusIQ API uses standard HTTP status codes and returns consistent error responses.

## Error Response Format

```json
{
  "error": {
    "code": "connector_not_found",
    "message": "No connector found with id conn_abc123",
    "details": {}
  }
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad request — check your parameters |
| 401 | Unauthorized — invalid or missing API key |
| 403 | Forbidden — your plan doesn't include this feature |
| 404 | Not found |
| 429 | Rate limit exceeded |
| 500 | Server error — we're on it |

## Common Error Codes

| Code | Description |
|------|-------------|
| `invalid_api_key` | The API key is missing or invalid |
| `connector_not_found` | The specified connector doesn't exist |
| `connector_auth_failed` | The connector's authentication expired |
| `query_timeout` | The query took too long (over 30 seconds) |
| `plan_limit` | Your plan doesn't support this action |
| `rate_limit` | Too many requests — slow down |

## Getting Help

If you encounter errors not listed here, check our [troubleshooting guide](../troubleshooting/README.md) or contact support.
