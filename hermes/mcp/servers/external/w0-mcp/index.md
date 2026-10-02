---
title: w0 MCP Server - Brand AI Recommendation Rate Lookup
description: Keyless MCP lookup of a brand's AI Recommendation Rate and Recommendation Inclusion Rate - how often AI engines pick the brand as the number-one answer to buyer-intent questions.
category: SEO
stars: n/a (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3758"
relevance: ★★★
tags: [geo, aeo, brand-monitoring, ai-search, analytics, marketing, seo, remote-mcp]
---

# w0 MCP Server

**Remote MCP server (Streamable HTTP, no key)** - w0 looks up a brand's AI Recommendation Rate: the percentage of buyer-intent questions where the brand is the AI's number-one pick, plus its Recommendation Inclusion Rate, where the brand appears anywhere in the answer. Built on Modern AI's Discovery product and published in the official MCP registry as `io.github.modern-ai-inc/w0-mcp-server`. Free, keyless and rate-limited per caller; brands that are not yet measured return an honest "not measured" response instead of a fabricated number. Endpoint live - anonymous initialize answered by the Workers access layer (HTTP 403 for unauthenticated probes).

```
Server type: Remote (Streamable HTTP)
Auth: None required - free, rate-limited per caller
Endpoint: https://w0-mcp-server.modernai.workers.dev
Tools: 1 (lookup_brand_recommendation_rate)
Pricing: Free; 429 once the per-caller ceiling is reached
Category: SEO
Built by: Modern AI (repo github.com/modern-ai-inc/w0-mcp-server)
```

## Why This Matters for Operators

Generative search has quietly become the first stop for buyer-intent questions - and almost nobody can measure how often their brand wins those answers. Manual prompting of AI engines produces anecdotes, not a rate.

**w0 turns AI visibility into a number operators can track.** The Recommendation Rate answers the question that matters: of the questions where a customer is ready to buy, how often is your brand the AI's number-one pick? The Inclusion Rate shows how often you appear at all. And because unmeasured brands return "not measured" rather than an invented score, the number you get is a measurement, not an estimate.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `lookup_brand_recommendation_rate` | Returns a brand's AI Recommendation Rate and Recommendation Inclusion Rate |

## Installation

```bash
claude mcp add w0 --transport http https://w0-mcp-server.modernai.workers.dev
```

## Configuration

```json
{
  "mcpServers": {
    "w0": {
      "type": "http",
      "url": "https://w0-mcp-server.modernai.workers.dev"
    }
  }
}
```

No key or account - the endpoint is free and rate-limited per caller under Modern AI's published anti-scrape policy.

## Business Relevance

- **Marketing leads** baseline their AEO/GEO position before investing in AI-visibility programs.
- **Brand managers** track whether they are the recommended pick, not just a mention.
- **Agencies** add AI Recommendation Rate to client reporting alongside search rankings.
- **Growth teams** measure the impact of content and PR pushes on AI answers over time.

## Integration with CorpusIQ

w0 pairs with CorpusIQ's analytics connectors to close the AI-visibility loop. An operator can pull revenue and pipeline context from CorpusIQ's GA4, Stripe or HubSpot connectors, run w0 lookups for the brands and categories that matter, and compare AI Recommendation Rate movement against actual business outcomes - tying generative-search performance to money for the first time. It also complements the catalog's citerank and other GEO guides as the measurement layer for AI-visibility programs.

## Limitations

- Brand new - zero stars, no track record yet.
- Single tool - one metric pair per lookup, no history or trends in this release.
- Rate-limited per caller; bulk or scraping use hits the 429 ceiling quickly.
- Coverage depends on Modern AI's Discovery measurement base - unmeasured brands return "not measured".
- Keyless hosted endpoint - no self-host option published.

## See Also

- [CiteRank MCP - AI Search Visibility Audits](/hermes/mcp/servers/external/citerank-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
