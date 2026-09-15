---
title: "AIsa MCP - One Key for 950+ Data APIs for AI Agents"
description: "Hosted remote MCP server that fronts 950+ data APIs across SEO and AI visibility, finance, social, web search, sales and agent mail behind one OAuth key and five tools. search finds an operation from a plain-language task, get_details returns its contract and price, and use runs it with a max_price_usd spend cap. Category endpoints preload 32-84 tools per domain."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 morning, submitted 5h before sweep) + vendor page at mcp.so/servers/aisa"
relevance: ★★★
tags: [seo, ai-visibility, finance, social-data, sales-intelligence, web-search, agent-mail, data-aggregation, oauth, remote-mcp]
---

# AIsa MCP

**One remote MCP endpoint in front of 950+ data APIs.** AIsa is a hosted GTM data stack: SEO and AI visibility (DataForSEO, Semrush, Ahrefs), finance (prices, fundamentals, filings, crypto, prediction markets), social (X/Twitter, Instagram, Reddit, Pinterest, YouTube), web search and research (Tavily, Firecrawl, Exa, Perplexity, Oxylabs), sales (Apollo, creator discovery, Similarweb) and agent mail (AgentMail). One key, one connection, one bill instead of a developer account, a contract and a rate limit per provider.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (RFC 9728 protected-resource metadata, RFC 7591 dynamic client registration) or a Bearer API key
Endpoint: https://mcp.aisa.one/mcp
Tools: 5 core tools; category endpoints preload 32-84 tools (SEO 65, finance 56, social 61, search 32, sales 84, mail 54, GTM 48)
Pricing: discovery free; use and batch_use billed per call with a max_price_usd cap enforced before any spend
Category: Data & Analytics / GTM stack
Built by: AIsa (one.aisa), official MCP registry one.aisa/mcp
```

## Why This Matters for Operators

Putting 950 operations in `tools/list` would cost more context than the work, so the endpoint lists five tools and resolves everything through them. This is the short-tool-list routing pattern that works: an agent states a task in plain language, `search` returns the matching operation with its schema and price, and `use` runs it. The agent never has to know which provider a metric comes from, and the operator never has to manage 20 API accounts.

The spend control is the real operator feature: every paid call accepts `max_price_usd`, which refuses anything above the cap before any spend. An agent cannot run up a bill by picking an expensive operation. `batch_use` runs up to 20 operations concurrently and one failure never cancels the others, and the same metric can be cross-checked across two providers (domain authority from DataForSEO, Semrush and Ahrefs; backlinks from several indexes) in one call when a decision depends on the number.

## Tools & Capabilities

| Tool | What it does | Price |
|---|---|---|
| `search` | Find an operation from a plain-language task; returns operation_id, input schema, price and match reasons | Free |
| `get_details` | Full contract for an operation: schemas, availability, price, known pitfalls | Free |
| `list_categories` | The catalogue at a glance | Free |
| `use` | Run one operation | Per call |
| `batch_use` | Run up to 20 operations concurrently; one failure never cancels the others | Per call |

Category endpoints serve a shorter `tools/list` from the same server: `https://mcp.aisa.one/seo/mcp` (65 tools), `/finance/mcp` (56), `/social/mcp` (61), `/search/mcp` (32), `/sales/mcp` (84), `/mail/mcp` (54), `/gtm/mcp` (48). `search` still reaches the whole catalogue from any of them.

## Installation

```bash
claude mcp add aisa --transport http https://mcp.aisa.one/mcp
```

Per-client walkthroughs are published on the mcp.so listing page. An unauthenticated request answers 401 naming its protected-resource metadata (RFC 9728), and the authorization server accepts an unregistered client (RFC 7591), so the client registers itself and signs the user in through a browser. A Bearer API key header works instead.

## Configuration

```json
{
  "mcpServers": {
    "aisa": {
      "type": "http",
      "url": "https://mcp.aisa.one/mcp"
    }
  }
}
```

Call `use` with `operation_id: "account"` (free) to see the key, balance and usage for today, 7 days and 30 days. The live catalogue is generated per request at mcp.aisa.one/servers, and the published server card is at mcp.aisa.one/.well-known/mcp/server-card.json.

## Business Relevance

- **Founders and growth operators** get prospecting, competitor research and brand monitoring from one key instead of an account-per-vendor sprawl.
- **SEO and GEO leads** get rank tracking, keyword research, backlinks and AI-visibility data across DataForSEO, Semrush and Ahrefs, with cross-provider checks in one batch call.
- **Finance operators** get prices, fundamentals, SEC filings, insider trades, crypto and prediction-market data alongside the GTM stack.
- **Agencies** get per-call billing with hard caps, so client work never produces a surprise invoice.

## Integration with CorpusIQ

AIsa complements CorpusIQ's 40+ business data connectors by covering the market data layer around them. CorpusIQ reads the business itself (Stripe revenue, QuickBooks books, Shopify catalog, Google Ads and GA4 performance, HubSpot pipeline); AIsa reads the market around it: competitor SEO and AI-visibility position, search volume, social presence, funding and filing signals. A composed workflow runs both in one session: pull this quarter's channel performance through CorpusIQ, then use AIsa's `search` and `use` tools to find which keywords the competitors are ranking for and cross-check domain authority across two providers in one `batch_use` call. The `max_price_usd` cap keeps the whole loop inside a defined spend envelope, matching CorpusIQ's read-only governance posture.

## Limitations

- Brand new: submitted to mcp.so hours before this guide; no public track record yet.
- mcp.so lists "No tools detected" because the endpoint intentionally serves five routing tools; the 950 operations resolve through `search`, so the live tool list is shorter than the capability surface.
- Per-call pricing means cost scales with usage; the cap protects you but does not create a flat-rate option.
- Hosted remote server only; no self-host option published.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
