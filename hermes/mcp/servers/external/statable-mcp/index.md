---
title: "Statable MCP - Cookieless Web Analytics for Agents"
description: "Remote MCP server for Statable, privacy-first cookieless web analytics hosted in the EU. 25 tools cover visitors, pages, traffic sources, UTM breakdowns, countries, goals, funnels and live traffic over OAuth, so an assistant answers site-analytics questions without a dashboard. Endpoint mcp.statable.com/mcp; stdio via npx @statable/mcp with an API key."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-14
source: "mcp.so feed (statable) + vendor docs at statable.com/docs/integrations/mcp/"
relevance: ★★
tags: [analytics, web-analytics, privacy, cookieless, gdpr, eu, oauth, remote-mcp]
---

# Statable MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the reporting interface for Statable, cookieless web analytics built and hosted in the European Union. Instead of opening a dashboard to check traffic, an operator asks the same assistant that holds the rest of the business data: visitors and pageviews for any window, which pages convert, where traffic came from, and who is on the site right now. 25 tools cover the reporting side of an account plus site, goal and funnel setup.

```
Server type: Remote (Streamable HTTP); stdio via npx @statable/mcp
Auth: OAuth (remote, browser consent on first use) or API key (stdio package)
Endpoint: https://mcp.statable.com/mcp
Tools: 25 (reporting plus site, goal and funnel setup; writes marked and rate-limited)
Pricing: Statable account required; plan details at statable.com
Category: Data & Analytics
Built by: Key Arg B.V. (statable.com, Netherlands)
```

## Why This Matters for Operators

Most analytics questions are simple - how many visitors yesterday, which five pages drove the most visits, is anyone on the site right now - but getting an answer usually means a dashboard trip, a filter session and a screenshot for the team. Statable MCP puts the same numbers behind an assistant, so the question and the answer stay in one conversation. The privacy model is the second half of the value: no cookies and no persistent identifiers, so sites running Statable need no consent banner, and visitors are counted with a keyed server-side hash that rotates every midnight UTC. Data is processed and stored in the EU.

## Tools & Capabilities

| Area | Coverage |
|---|---|
| Traffic | visitors, pageviews, visits, bounce rate, time series by day, week or month |
| Breakdowns | pages, entry and exit pages, traffic sources, UTM parameters, countries, regions, cities, browsers, operating systems, devices |
| Conversions | goals, custom events, funnels, conversion rates |
| Live | current visitors on a site |
| Setup | create and update sites, goals and funnels |

25 tools in total. Read tools are read-only; write tools are marked as such and rate-limited. The endpoint answers an anonymous initialize with HTTP 401 - live and auth-gated as documented - and the full tool list is served from the authorized connection.

## Installation

```bash
claude mcp add statable --transport http https://mcp.statable.com/mcp
```

Add the endpoint as a custom connector in Claude, Cursor, VS Code or any MCP-compatible client and complete the OAuth consent screen on first use. For stdio-only hosts there is also `npx @statable/mcp` with an API key (npm package verified: @statable/mcp 0.1.0).

## Configuration

```json
{
  "mcpServers": {
    "statable": {
      "type": "http",
      "url": "https://mcp.statable.com/mcp"
    }
  }
}
```

## Business Relevance

- **Marketing leads** get traffic, source and conversion answers inside the assistant, with no CSV exports.
- **Ecommerce operators** check which pages and campaigns drive visits before and after launches.
- **Agencies** connect client sites and answer reporting questions without switching accounts.
- **Privacy-sensitive teams** run analytics without a consent banner requirement, matching EU data handling.
- **Founders** keep a live pulse on the site from the same session where they read revenue.

## Integration with CorpusIQ

Statable answers the on-site question and CorpusIQ answers the business question. An agent with a CorpusIQ connection reads revenue, orders and pipeline (Stripe, Shopify, HubSpot, QuickBooks, GA4) and pairs it with Statable traffic and conversion data in one analysis, so a weekly review covers both sides of the funnel: what visitors did on the site and what the business booked. Site, goal and funnel setup through the MCP server keeps the tracking structure aligned with the metrics the team reviews in CorpusIQ.

## Limitations

- Brand new listing: no third-party track record and no public repo for the server itself.
- The individual tool names are not published in the docs; the live list is served from the authorized connection.
- OAuth only on the remote endpoint; the API key path exists only through the npm stdio package.
- A Statable account is required and no free tier is published on the MCP listing.
- Read-heavy but not read-only: setup tools create and update sites, goals and funnels.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Draxlr MCP - SQL Dashboards and Queries for Agents](/docs/hermes/mcp/servers/external/draxlr-mcp)
- [Pixelesq MCP - Website Management and SEO for Agents](/docs/hermes/mcp/servers/external/pixelesq-mcp)
