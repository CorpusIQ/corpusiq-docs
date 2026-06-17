---
meta_title: "CorpusIQ API Rate Limits — Quotas, Headers, and Best Practices"
meta_desc: "Complete guide to CorpusIQ API rate limits. Per-endpoint quotas, rate limit headers, retry strategies, 429 handling, fair-use policies, and how to request limit increases for enterprise accounts."
category: "API Reference"
tags: ["corpusiq rate limits", "api quotas", "rate limiting", "429 errors", "api throttling", "enterprise api", "fair use policy"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/api/rate-limits"
robots: "index,follow"
---
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

## Frequently Asked Questions

**Q: What are the CorpusIQ API rate limits?**  
A: Rate limits are per-endpoint with minute and daily windows. Exact limits are documented per endpoint and returned in response headers (X-RateLimit-*) for self-monitoring.

**Q: How do I check my current rate limit status?**  
A: Every API response includes rate limit headers: X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset showing your current quota consumption.

**Q: Can I get higher rate limits for enterprise use?**  
A: Yes. Enterprise plans include increased rate limits. Contact CorpusIQ sales for custom quota configurations tailored to your organization's query volume.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What are the CorpusIQ API rate limits?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rate limits are per-endpoint with minute and daily windows. Exact limits are documented per endpoint and returned in response headers (X-RateLimit-*) for self-monitoring."
      }
    },
    {
      "@type": "Question",
      "name": "How do I check my current rate limit status?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every API response includes rate limit headers: X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset showing your current quota consumption."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get higher rate limits for enterprise use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Enterprise plans include increased rate limits. Contact CorpusIQ sales for custom quota configurations tailored to your organization's query volume."
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
