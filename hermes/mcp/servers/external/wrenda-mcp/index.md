---
title: "Wrenda MCP - Edge AI-Visibility Optimization for Websites"
description: "Wrenda puts a per-domain MCP server in front of your website at the edge: AI agents call POST /.well-known/mcp to list tools and act on the site. The edge rewrites pages into enriched markdown with schema, FAQs and entity expansion (up to 12x tokens), pre-renders JavaScript-heavy pages for crawlers, and tracks AI citations across ChatGPT, Perplexity, Gemini, AI Overviews, Copilot and Grok with drift alerts."
category: SEO
stars: n/a (new listing)
added: 2026-09-15
source: "mcpservers.org /all page 1 + vendor page at wrenda.ai"
relevance: ★★★
tags: [geo, ai-visibility, edge-proxy, prerendering, schema-markup, citation-tracking, search-console, ab-testing, remote-mcp]
---

# Wrenda MCP

**A website your agents can read, and answer engines can cite.** Wrenda intercepts crawler requests at the edge and routes them through AI optimization, pre-rendering or caching, so AI systems receive enriched content they can parse, understand and cite. Each domain gets its own MCP server: agents discover tools, execute actions and interact with the site programmatically via JSON-RPC 2.0 at `POST /.well-known/mcp`.

```
Server type: Per-domain edge MCP (JSON-RPC 2.0 at POST /.well-known/mcp) plus edge proxy via DNS CNAME
Auth: account-based (wrenda.ai dashboard); domain activation provisions SSL, worker routes and cache slots automatically
Endpoint: your-domain/.well-known/mcp (tools/list, tools/call)
Tools: domain-scoped action set served per site (list and call via JSON-RPC)
Pricing: plans with weekly AI-citation refreshes; daily on Scale (early-access onboarding)
Category: SEO / AI Visibility
Built by: Wrenda (wrenda.ai)
```

## Why This Matters for Operators

AI systems skip what they cannot parse. Raw HTML, JavaScript shells and schema-free pages tokenize badly, so answer engines either miss the page or cite a competitor that ships clean structure. Wrenda attacks all three failure modes at the edge: an AI engine rewrites each page as enriched markdown, injecting schema metadata, FAQ sections, entity expansions and semantic relationships (up to 12x the usable tokens), while a real headless browser pre-renders JavaScript-heavy pages into complete HTML for crawlers that cannot execute JS. Ratings, prices and claims are never invented; only facts on the page are structured.

The measurement layer closes the loop: Wrenda tracks how ChatGPT, Perplexity, Gemini, Google AI Overviews, Microsoft Copilot and Grok answer the questions the category gets asked, with mention rate, share of voice against competitors, persona fan-out (CMO, SEO lead, founder, buyer), competitor source-gap analysis and citation drift alerts when visibility moves. A Search Console-backed causal-impact tool splits URLs into control and variant groups to measure title, meta or schema changes (early access).

## Tools & Capabilities

The per-domain MCP server exposes its tool set via JSON-RPC 2.0:

| Capability | What it does |
|---|---|
| `tools/list` | Agent discovers the actions available for the domain |
| `tools/call` | Agent executes domain actions (site management, content checks, monitoring) |
| Edge enrichment | Page-by-page markdown transformation with schema, FAQs and entity expansion |
| Pre-rendering | Full browser rendering at the edge for JS-heavy SPAs |
| AI citation tracking | Per-model mention rate, share of voice, source-gap analysis, drift alerts |
| Experiments | Control/variant URL splits with causal-impact analysis on Search Console data (early access) |

## Installation

```bash
# 1. Point your DNS at Wrenda (CNAME); origin auto-detected, SSL provisioned,
#    worker routes created automatically. DNS propagation can take up to 24h.
# 2. Activate the domain in the wrenda.ai dashboard.

# Verify the per-domain MCP server:
curl -X POST https://your-domain/.well-known/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'
```

## Configuration

```json
{
  "mcpServers": {
    "wrenda": {
      "type": "http",
      "url": "https://your-domain/.well-known/mcp"
    }
  }
}
```

Agent access and citation tracking are managed in the wrenda.ai account. The vendor is onboarding early-access sites now.

## Business Relevance

- **E-commerce operators** get product pages with schema, FAQs and entities that answer engines can cite, without replatforming.
- **SEO and GEO leads** get AI citation tracking across six models with drift alerts and competitor source-gap analysis.
- **Marketing teams** get A/B-style title, meta and schema experiments measured on Search Console data.
- **Engineering-light teams** get pre-rendering and enrichment from a DNS change instead of a frontend project.

## Integration with CorpusIQ

Wrenda makes the site legible to AI; CorpusIQ makes the business legible to AI. Together they close the two halves of GEO: Wrenda ensures the pages parse, carry schema and get cited, while CorpusIQ serves the business data that grounds the claims (Stripe revenue, QuickBooks books, GA4 traffic, Shopify catalog) to any agent that asks. The citation tracker then measures the outcome, and its Search Console experiments test the changes, with CorpusIQ's GA4 and Google Ads connectors supplying the business-side effects of any visibility lift.

## Limitations

- Early access: the vendor is onboarding sites now; the experiment tool is explicitly early-access.
- Edge proxy architecture: DNS must point at Wrenda, which takes time to propagate and makes Wrenda a dependency in the serving path.
- Citation refreshes are weekly on most plans; daily only on Scale.
- Tool list is per-domain and dynamic; no static published schema at sweep time.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
