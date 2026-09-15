---
title: "Sorank MCP - Search Console, PageSpeed and AI Citability"
description: "Ask your assistant why a page underperforms: Search Console data, PageSpeed and Core Web Vitals, and an AI-citability score in one OAuth-connected, free MCP endpoint."
category: SEO
stars: n/a (no public repo)
added: 2026-09-03
source: mcp.so
relevance: ★★★
tags: [seo, search-console, pagespeed, core-web-vitals, geo, ai-citability, remote-mcp]
---

# Sorank MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - Sorank connects Google Search Console, PageSpeed Insights and AI-citability scoring to an assistant, so the agent can diagnose why a page underperforms and say exactly what to change. Twelve tools in three families, no API key, no paid plan.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (Google account with Search Console access)
Endpoint: https://mcp.sorank.com/functions/v1/mcp
Tools: 12 (Search Console, speed, AI-search families)
Pricing: Free, no paid plan documented
Category: SEO
Built by: Thibault Besson-Magdelain (sorank.com)
```

## Why This Matters for Operators

The standard SEO loop is export, spreadsheet, re-export: pull queries from Search Console, run a speed check, guess at AI visibility. Sorank collapses it into questions - "find the pages that rank on page two and rewrite their titles with the queries they impress on", "why does this URL refuse to index, in Google's own words", "compare this quarter to last before the drop shows up in revenue".

**The retention detail is the edge:** Google's Search Console keeps 16 months of history and then forgets. Sorank keeps history beyond that limit, so an operator can compare a season to the same season two years earlier - trends Google itself no longer shows. The AI-citability score, which rates whether ChatGPT, Perplexity and Google AI Overviews can lift a clean answer out of a page, is something no Search Console export provides.

## Tools & Capabilities

Twelve tools across three families (family-level description from the listing; individual tool names served from the endpoint):

| Family | Purpose |
|---|---|
| Search Console | List properties, performance with period comparison, quick wins, movers, long-term history, URL inspection (single or batch), sitemap health |
| Speed | Single-URL analysis, Core Web Vitals, full-site audit with the three fixes that move the needle |
| AI search | Score any page on how citable it is by AI assistants |

## Installation

```bash
claude mcp add sorank --transport http https://mcp.sorank.com/functions/v1/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "sorank": {
      "type": "http",
      "url": "https://mcp.sorank.com/functions/v1/mcp"
    }
  }
}
```

On first connect the client opens the Google OAuth flow; the account must have verified access to at least one Search Console property. Read-only: the server only reads what is asked for, and no data leaves the operator's account.

## Business Relevance

- **SEO freelancers** run several client properties and get diagnosis plus fix in one conversation
- **Founders running their own SEO** get quick wins without an SEO hire
- **Marketing teams** catch query slippage in the current quarter before it shows in revenue

## Integration with CorpusIQ

Sorank pairs with CorpusIQ's GA4 and Search Console coverage on the diagnostic side: CorpusIQ reports the revenue and conversion picture, Sorank explains the organic-search mechanics behind it. A composed workflow: GA4 shows a landing page losing signups, Sorank pulls its Search Console history to find which queries slipped and its citability score to explain AI-search visibility, and the operator gets the rewrite list. Operators running CorpusIQ dashboards get the "why" under the "what" without leaving the assistant.

## Limitations

- Brand new listing with no public track record yet
- OAuth Google account with Search Console access required - no key mode
- Individual tool names served from the endpoint; verify after connecting
- Requires Sorank's own history store to get the beyond-16-months advantage

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [SEOmatic MCP - Real Search Console Data with Approval-Gated Fixes](/docs/hermes/mcp/servers/external/seomatic-mcp)
- [Ranki MCP - Free SEO and AEO Audits for AI Agents](/docs/hermes/mcp/servers/external/ranki-mcp)
- [Tracetify MCP - SEO, GEO and Growth Reports for Agents](/docs/hermes/mcp/servers/external/tracetify-mcp)
- [HiBot MCP - ANSWER-Framework AI Visibility Audits](/docs/hermes/mcp/servers/external/hibot-mcp)
