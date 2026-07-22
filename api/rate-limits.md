# Rate Limits

The CorpusIQ API enforces rate limits to ensure fair usage across all customers.

## Default Limits

| Plan | Requests per minute | Queries per hour |
|------|-------------------|-----------------|
| Trial | 30 | 10 |
| Pro | 120 | 60 |
| Enterprise | 500 | Unlimited |

## Rate Limit Headers

Every API response includes rate limit information:

```
X-RateLimit-Limit: 120
X-RateLimit-Remaining: 98
X-RateLimit-Reset: 1750000000
```

## Handling Rate Limits

When you exceed the limit, the API returns `429 Too Many Requests`. Best practices:

- Check `X-RateLimit-Remaining` before making requests
- Implement exponential backoff on 429 responses
- Spread queries across the hour instead of batching them

## Increasing Limits

Pro and Enterprise customers can request higher limits by contacting support at https://corpusiq.io.
