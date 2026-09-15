---
title: "Otto MCP - Live Marketing Data and Website Operations in Chat"
description: "Hosted MCP connector that brings live Meta Ads, Google Analytics 4, and Search Console data into Claude, ChatGPT, Cursor, and other assistants, plus website updates, SEO, and performance checks through conversation. Commercial plans from $99/mo."
category: Marketing
stars: n/a (new listing, no public repo)
added: 2026-08-29
source: mcpservers.org /all page 1
relevance: ★★
tags: [mcp-server, marketing-analytics, meta-ads, ga4, search-console, website-ops, analytics, remote-mcp]
---

# Otto MCP

**A hosted MCP connector positioned as a digital webmaster: live Meta Ads, GA4, and Google Search Console data inside Claude or ChatGPT, plus website updates, SEO, and performance checks through conversation.** Otto connects the three marketing data sources operators check most and keeps them answerable in chat instead of behind dashboards. Commercial plans start at $99/mo (founding price locked forever for the first 100 organizations), with a 7-day trial.

```
Server type: Remote (Streamable HTTP), hosted
Auth: Otto account (Clerk) with connector OAuth to Meta, GA4, and Search Console
Endpoint: https://otto.islaintel.com/api/mcp
Pricing: $99/mo founding (first 100 orgs, locked forever), $199/mo after; 7-day trial, card required
Category: Marketing / Marketing Analytics
Built by: Isla Intel (otto.islaintel.com); listing slug ottowebmaster-com-mcp
```

## Why This Matters for Operators

The three questions an operator asks every morning - how did yesterday's spend perform, what did the site do, what is search telling us - live in three different dashboards with three different UIs. Otto collapses them into one connector: ask in Claude or ChatGPT, get Meta Ads, GA4, and Search Console numbers in the same thread, and follow up with website operations like updates, SEO checks, and performance checks without leaving the conversation.

The tool surface is gated behind account auth (the endpoint returns 401 without authorization, confirming it is live), and the vendor publishes no public tool list - capability level from the vendor's product pages. The pricing model is straightforward per organization, with the founding cohort locked at $99/mo forever, which matters for operators who want a fixed line item rather than metered credits.

**The daily marketing check-in becomes one chat surface across Meta, GA4, and Search Console.**

## Tools & Capabilities

Capability-level from vendor product docs; anonymous enumeration is refused (401 confirmed live), and exact tool names require sign-in.

| Capability area | What the assistant can do |
|---|---|
| Meta Ads | Pull campaign and ad performance, spend, and delivery data into chat |
| Google Analytics 4 | Read traffic, conversion, and audience numbers conversationally |
| Search Console | Query search performance, impressions, clicks, and position data |
| Website operations | Updates, SEO checks, and performance checks executed through conversation |

## Installation

```bash
claude mcp add --transport http otto https://otto.islaintel.com/api/mcp
```

Paste the connector URL into Claude, ChatGPT, Cursor, or Claude Code, start the 7-day trial (card required), and connect Meta first - the onboarding flow then walks through GA4 and Search Console.

## Configuration

```json
{
  "mcpServers": {
    "otto": {
      "type": "http",
      "url": "https://otto.islaintel.com/api/mcp"
    }
  }
}
```

Authentication is account-based (Clerk), with connector OAuth scoped per data source. The same connector URL works across all supported clients.

## Business Relevance

- **Founders and marketing leads** get the daily Meta/GA4/GSC check-in in one chat thread instead of three dashboards.
- **Agencies** keep a fixed per-org line item ($99/mo founding, locked) instead of metered credits across client accounts.
- **Website operators** fold updates and performance checks into the same conversation as the analytics reads.
- **Teams standardized on Claude or ChatGPT** add marketing data without building an integration.

## Integration with CorpusIQ

Otto's Meta Ads and GA4 reads slot into CorpusIQ's attribution stack: CorpusIQ already pulls GA4 signup attribution (the run_report path) and SocialGlass-style channel data, and Otto adds the conversational Meta Ads surface for operators who want the paid-side numbers alongside organic. A CorpusIQ-driven workflow can cross-check Otto's Search Console reads against CorpusIQ's own docs SEO/AEO/GEO pass, so search visibility answers carry both the raw GSC data and the optimization actions. For the weekly operator report, Otto's chat-native outputs feed the same recap-answer rendering CorpusIQ uses, keeping paid, organic, and site-health numbers in one report format.

## Limitations

- Paid commercial product - $99/mo founding, $199/mo after the first 100 orgs, trial requires a card.
- No public tool list; the surface must be discovered after sign-in.
- No public repo - trust the hosted endpoint and vendor docs.
- Data scope is Meta, GA4, and Search Console plus site ops - not a general marketing data warehouse.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Askline MCP - AI Search Visibility and Brand Monitoring](/docs/hermes/mcp/servers/external/askline-mcp)
- [AstroFabric MCP - Agentic Growth Missions for Operators](/docs/hermes/mcp/servers/external/astrofabric-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
