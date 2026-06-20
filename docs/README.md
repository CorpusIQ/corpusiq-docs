---
meta_desc: "CorpusIQ Documentation. CorpusIQ is a private AI acceleration layer that connects 37+ business tools to ChatGPT, Claude, and Perplexity via the Model Context..."
---

# CorpusIQ Documentation

CorpusIQ is a private AI acceleration layer that connects 37+ business tools to ChatGPT, Claude, and Perplexity via the Model Context Protocol (MCP). One question. Cited answers from all your tools.

CorpusIQ acts as a read-only bridge between your SaaS applications and AI assistants, enabling natural-language queries across your entire data stack without moving or persisting your data. Every response includes citations back to the source tool, so you can verify accuracy in one click.

## Key Capabilities

- **37+ native connectors** — Gmail, Google Drive, Slack, HubSpot, Shopify, QuickBooks, PostgreSQL, and more
- **MCP-native** — Designed for AI assistants that speak the Model Context Protocol
- **Read-only by design** — OAuth scopes are restricted to read access; no write permissions are ever requested
- **Zero data retention** — Embeddings are computed per session and deleted immediately after
- **SOC 2 Ready & CASA Tier 2 Certified** — DEKRA-assessed, GDPR aligned, OWASP Top 10 verified

## Quick Links

| Section | Description |
|---------|-------------|
| [Quick Start](/docs/quick-start) | Get up and running in under 5 minutes |
| [API Overview](/docs/api/overview) | Base URL, endpoints, and core concepts |
| [API Reference](/docs/api/endpoints) | Full endpoint documentation with request/response schemas |
| [Authentication](/docs/api/authentication) | Bearer token management and security best practices |
| [Connectors](/docs/connectors) | Complete list of supported integrations |
| [Security](/docs/security) | Architecture, compliance, and data handling |
| [Rate Limits](/docs/api/rate-limits) | Per-endpoint rate limits and quotas |
| [Webhooks](/docs/api/webhooks) | Event subscriptions and signature verification |
| [OpenAPI Spec](/docs/api/openapi) | Importable OpenAPI 3.0.3 specification |
| [Changelog](/docs/changelog) | Release history and version notes |

## Architecture at a Glance

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│  AI Assistant │────▶│  CorpusIQ API │────▶│  Connected Tools  │
│ (ChatGPT,    │     │ (api.corpusiq │     │ (Gmail, Slack,   │
│  Claude,     │     │  .io/v1)     │     │  HubSpot, etc.)   │
│  Perplexity) │◀────│              │◀────│                  │
└──────────────┘     └──────────────┘     └──────────────────┘
```

CorpusIQ never stores your data. It translates AI assistant queries into read-only API calls, retrieves matching information from your connected tools, generates temporary embeddings for semantic ranking, and returns cited results. Once the session ends, all embeddings are purged.

## Getting Help

- **API Support**: api@corpusiq.io
- **Security Concerns**: security@corpusiq.io
- **Status Page**: status.corpusiq.io

For integration partners and enterprise deployments, contact sales@corpusiq.io.
# sitemap rebuild trigger

*[CorpusIQ](https://www.corpusiq.io) — AI answers grounded in your business data. 30-day free trial.*

*[CorpusIQ](https://www.corpusiq.io) — AI answers grounded in your business data. 30-day free trial.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
