---
title: Prognosite MCP - SEO and AEO Intelligence for Publishers
description: SEO and AEO intelligence platform with roughly 150 callable tools that read Search Console, Bing Webmaster Tools and Google Analytics and return diagnoses and actions instead of keyword walls.
category: SEO
stars: n/a (new listing)
added: 2026-09-02
source: mcpservers.org
relevance: ★★★
tags: [seo, aeo, search-console, analytics, publishing, audits, remote-mcp]
last_updated: "2026-10-19"
---

# Prognosite MCP

**Remote MCP server (Streamable HTTP, OAuth)** - an SEO and AEO intelligence platform for digital publishers, delivered as roughly 150 callable tools so an agent can investigate a site by asking questions instead of clicking through dashboards. It connects directly to Google Search Console, Bing Webmaster Tools and Google Analytics, reads first-party and third-party signals across a portfolio, and returns diagnoses and actionable recommendations.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth one-click sign-in, no API keys to manage
Endpoint: https://mcp.prognosite.com/mcp
Tools: ~149 (keyword research, audits, crawl analysis, reporting)
Pricing: Prognosite platform plans; connector page at claude.ai/directory/prognosite
Category: SEO
Built by: Prognosite
```

## Why This Matters for Operators

Most SEO tooling dumps keyword data on a dashboard and calls it insight. Prognosite is built on the opposite premise: the platform reads the signals and returns a diagnosis. **Think of it as an analyst that lives inside the workflow rather than another wall of data.**

For an operator running a content portfolio, that changes the questions you can ask: which pages lost the most traffic this week, where do we rank positions 4-10 with real volume behind them, which pages are one position away from page one, what does the technical audit say. The agent gets the analysis in conversation, with the actions attached.

## Tools & Capabilities

| Area | What the tools do |
|---|---|
| Keyword research | Demand, opportunity and rank-position analysis across the portfolio |
| Technical audits | Site-wide crawl and technical health checks |
| Crawl analysis | Page-level crawl behaviour and coverage diagnostics |
| Reporting | Portfolio-wide traffic, position and loss reports |
| AEO signals | AI-search visibility signals for answer-engine optimization |

The full catalogue of 149 tools is browsable in the platform's Tools page; the listing does not publish a static tool list, and the live roster is served from the endpoint after OAuth.

## Installation

```bash
claude mcp add prognosite --transport http https://mcp.prognosite.com/mcp
```

The Claude connector path is one click at claude.ai/directory/prognosite; manual clients use the server URL above.

## Configuration

```json
{
  "mcpServers": {
    "prognosite": {
      "type": "http",
      "url": "https://mcp.prognosite.com/mcp"
    }
  }
}
```

Authentication is OAuth with one-time sign-in: the assistant hands off to Prognosite, your portal session is recognized, and the connection completes. No API keys or config files to manage.

## Business Relevance

- **Content publishers** get traffic-loss and rank-opportunity answers in conversation, not dashboards
- **SEO teams** run audits and crawl analysis from the assistant they already work in
- **Media operators** monitor whole portfolios of sites with first-party and third-party signals
- **Founders** find the pages one position from page one without an SEO hire

## Integration with CorpusIQ

Prognosite reads search performance; CorpusIQ reads business performance. Composed, an agent can answer the question every operator actually asks: which content drives revenue, not just traffic. Prognosite surfaces pages that lost traffic or sit at positions 4-10, then the agent joins that list against CorpusIQ's GA4 and Stripe connectors to see what the affected pages earn - and prioritizes fixes by revenue, not by traffic rank. For a SaaS operator, the loop is direct: Prognosite finds the opportunity, CorpusIQ tells you what it is worth.

## Limitations

- Brand new listing with no track record yet
- No published static tool list; the 149-tool catalogue lives in the platform
- Requires a Prognosite account and OAuth connection for any data
- Publisher-focused; not a general keyword-research terminal for arbitrary competitor sites
