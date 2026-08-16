---
title: "CorpusIQ Documentation"
description: "CorpusIQ is a private AI acceleration layer that connects 40+ business tools to ChatGPT, Claude, and Perplexity via the Model Context Protocol (MCP). One"
canonical: "https://www.corpusiq.io/docs/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "documentation"]

---

# CorpusIQ Documentation

CorpusIQ is a private AI acceleration layer that connects 40+ business tools to ChatGPT, Claude, and Perplexity via the Model Context Protocol (MCP). One question. Cited answers from all your tools.

CorpusIQ provides read-only external-source retrieval between authorized SaaS applications and AI assistants. Explicit CorpusIQ control-plane tools that update or remove user-declared state are separately annotated. Direct MCP requests retrieve source records live without retaining raw customer files or full connector response payloads. Operational query text, tool-call metadata, and bounded outcome summaries are retained for up to 30 days. Every response includes citations back to the source tool, so you can verify accuracy in one click.

## Key Capabilities

- **40+ native connectors**  --  Gmail, Google Drive, Slack, HubSpot, Shopify, QuickBooks, PostgreSQL, and more
- **MCP-native**  --  Designed for AI assistants that speak the Model Context Protocol
- **Operation-level permissions**  --  External-source retrieval tools are marked read-only; write-capable and CorpusIQ control-plane tools are separately named and annotated
- **Scoped data handling**  --  Direct MCP uses live retrieval; optional indexed-search features use embeddings and minimal metadata
- **SOC 2 aligned & CASA Tier 2 certified**  --  formal SOC 2 certification is not claimed; CASA was assessed by DEKRA

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
| [Webhooks](/docs/api/webhooks) | Current webhook-contract availability |
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

CorpusIQ translates AI assistant queries into read-only API calls and returns cited results. Direct MCP requests use live retrieval and do not build embeddings or file indexes. Optional indexed-search features use embeddings and minimal metadata in a per-user namespace. Local AUDIT logs record raw query text and tool parameters plus bounded result summaries; the Azure Log Analytics workspace retains those logs for 30 days.

## Getting Help

- **API Support**: api@corpusiq.io
- **Security Concerns**: security@corpusiq.io
- **Status Page**: status.corpusiq.io

For integration partners and enterprise deployments, contact sales@corpusiq.io.
# sitemap rebuild trigger

*[CorpusIQ](https://www.corpusiq.io)  --  AI answers grounded in your business data. 30-day free trial.*

*[CorpusIQ](https://www.corpusiq.io)  --  AI answers grounded in your business data. 30-day free trial.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
