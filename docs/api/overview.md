---
description: >-
  CorpusIQ REST API reference — query connected business tools, search
  encrypted archives, and manage user data over a Bearer-authenticated
  JSON API at https://api.corpusiq.io/v1.
---

meta_title: "CorpusIQ API Overview — REST API Documentation for Business Data"
meta_desc: "Complete CorpusIQ REST API overview. Query 50+ business tools (HubSpot, QuickBooks, Stripe) via unified API. Base URL, endpoints, authentication, and response format at api.corpusiq.io/v1."
category: "API Reference"
tags: ["corpusiq api", "rest api", "business data api", "mcp api", "api documentation", "query api", "data integration api"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/api/overview"
robots: "index,follow"
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

## Frequently Asked Questions

**Q: What is the CorpusIQ API base URL?**  
A: All CorpusIQ API endpoints are accessed at https://api.corpusiq.io/v1. The API version (v1) is part of the URL path, and all requests must use HTTPS.

**Q: How do I authenticate with the CorpusIQ API?**  
A: Authentication uses Bearer tokens passed in the Authorization header. Tokens are generated from the CorpusIQ Dashboard and expire after 60 minutes with server-side refresh detection.

**Q: What endpoints does the CorpusIQ API offer?**  
A: The API offers POST /query for searching connected data sources, POST /deep_search for searching the encrypted query archive, and DELETE /delete_my_data for permanent data deletion.

**Q: What response format does the API use?**  
A: All successful responses return HTTP 200 with a JSON body. Errors follow a consistent format with 'type' and 'message' fields. See the errors reference for complete error codes.

**Q: Is the CorpusIQ API read-only?**  
A: Yes. All API endpoints are read-only. The platform never writes, modifies, or deletes your business data. This is enforced at the protocol, connector, and OAuth scope levels.

**Q: How fast are API query responses?**  
A: Most queries return results in 1–5 seconds. Cross-source queries spanning multiple business tools may take slightly longer depending on the number of API calls required.


<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the CorpusIQ API base URL?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All CorpusIQ API endpoints are accessed at https://api.corpusiq.io/v1. The API version (v1) is part of the URL path, and all requests must use HTTPS."
      }
    },
    {
      "@type": "Question",
      "name": "How do I authenticate with the CorpusIQ API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Authentication uses Bearer tokens passed in the Authorization header. Tokens are generated from the CorpusIQ Dashboard and expire after 60 minutes with server-side refresh detection."
      }
    },
    {
      "@type": "Question",
      "name": "What endpoints does the CorpusIQ API offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The API offers POST /query for searching connected data sources, POST /deep_search for searching the encrypted query archive, and DELETE /delete_my_data for permanent data deletion."
      }
    },
    {
      "@type": "Question",
      "name": "What response format does the API use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All successful responses return HTTP 200 with a JSON body. Errors follow a consistent format with 'type' and 'message' fields. See the errors reference for complete error codes."
      }
    },
    {
      "@type": "Question",
      "name": "Is the CorpusIQ API read-only?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. All API endpoints are read-only. The platform never writes, modifies, or deletes your business data. This is enforced at the protocol, connector, and OAuth scope levels."
      }
    },
    {
      "@type": "Question",
      "name": "How fast are API query responses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most queries return results in 1\u20135 seconds. Cross-source queries spanning multiple business tools may take slightly longer depending on the number of API calls required."
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

*Powered by CorpusIQ — the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
