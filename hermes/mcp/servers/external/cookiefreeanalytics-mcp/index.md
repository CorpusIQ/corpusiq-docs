---
title: Cookie Free Analytics MCP - Cookieless GDPR-First Web
description: "Hosted read-only MCP server for cookieless, GDPR-first web analytics: pageviews, sources, live visitors, and funnels from the EU-hosted analytics platform, via OAuth 2.1 PKCE."
category: Analytics
stars: n/a (new listing, WesselsRepository/CookieFreeAnalytics-MCP)
added: 2026-08-29
source: mcpservers.org /all page 2
relevance: ★★
tags: [mcp-server, web-analytics, cookieless, gdpr, privacy-first, funnels, analytics, remote-mcp]
---

# Cookie Free Analytics MCP

**A remote MCP server for Cookie Free Analytics, the EU-hosted cookieless web analytics product, exposing the same aggregates as the dashboard - visitors, pages, sources, live, and funnels - read-only to any MCP client.** OAuth 2.1 with PKCE handles sign-in for interactive clients, and a hashed bearer token from the account covers API-style access. The 1 KB script counts pageviews without setting a cookie, so visits survive the cookie banner click.

```
Server type: Remote (Streamable HTTP), hosted at the product origin
Auth: OAuth 2.1 (RFC 9728 + PKCE); optional hashed bearer from Account
Endpoint: https://www.cookiefreeanalytics.com/mcp
Tools: Read-only aggregates mirroring the dashboard (sites, overview, live, funnels)
Pricing: Starter and Growth plans (from EUR 4/mo); Hobby is dashboard-only
Category: Analytics / Privacy-First Web Analytics
Built by: Prestons Creek Capital; registry io.github.PrestonsCreekCapital/cookie-free-analytics
```

## Why This Matters for Operators

Cookie-banner rejection silently deletes a slice of your analytics - every visitor who clicks Reject vanishes from a cookie-based tool's numbers, right when privacy-first traffic is growing. Cookie Free Analytics counts the pageview without a cookie, so the report keeps the visit, the campaign, and the goal that a cookie tool would have dropped.

The MCP server makes those numbers agent-readable with a hard privacy line: the tools return the same aggregates as the dashboard and never return visitor hashes, raw IPs, or a user graph, and they cannot write pageviews, change settings, or send mail. For an operator asking an agent "what did the launch do yesterday," the answer comes from a privacy-safe source that counts the full audience.

**Analytics that survive the cookie banner, exposed read-only to agents with a strict no-user-graph boundary.**

## Tools & Capabilities

Capability-level: the MCP tools mirror the dashboard aggregates and the published Read API routes (GET /api/v1, /api/v1/sites, /api/v1/sites/:id/overview?range=7d, plus live, pages, sources, and funnels). Exact MCP tool names are enumerated after OAuth sign-in; anonymous enumeration is not published.

| Capability area | What the agent can read |
|---|---|
| Sites | List sites on the account and their identifiers |
| Overview | Site-level aggregates over a date range (7d default) |
| Visitors & pages | Traffic and page-level counts, no visitor identity |
| Sources & campaigns | Referrer, source, and UTM-landing breakdowns |
| Live | Current live visitors |
| Funnels | Growth-plan funnel performance |

## Installation

```bash
claude mcp add --transport http cookie-free-analytics https://www.cookiefreeanalytics.com/mcp
```

Paste the URL as a custom connector in Claude Desktop or Claude.ai (Settings -> Connectors -> Add custom connector). The client starts OAuth 2.1 on cookiefreeanalytics.com with PKCE and dynamic client registration; no client ID or secret is needed.

## Configuration

```json
{
  "mcpServers": {
    "cookie-free-analytics": {
      "type": "http",
      "url": "https://www.cookiefreeanalytics.com/mcp"
    }
  }
}
```

Sign in to Cookie Free Analytics during the OAuth flow. A Google login on the website is not an MCP token; for API-style access, mint a hashed bearer token (cfa_live_...) under Account -> Read API and send it as the Authorization header.

## Business Relevance

- **Founders** read launch-day numbers their cookie-based tool undercounted, without building anything.
- **Marketing operators** pull campaign and source breakdowns into agent workflows alongside GA.
- **Privacy-conscious teams** keep analytics EU-hosted and GDPR-first, with a documented no-user-graph boundary for agents.
- **Analysts** get dashboard-equivalent aggregates in chat instead of exporting CSV dumps.

## Integration with CorpusIQ

Cookie Free Analytics gives CorpusIQ's marketing stack a privacy-first complement: where CorpusIQ pulls GA4 signup attribution through its connectors, this server adds the cookieless pageview reality - the audience segment GA misses after banner rejection - as an agent-readable check. A CorpusIQ workflow can compare the two sources side by side in a recap answer, so the operator sees both the attributed conversions (GA4) and the full traffic truth (Cookie Free Analytics), and the launch-report loop gets a second, GDPR-safe data point.

## Limitations

- Read-only by design - no pageview writes, settings changes, or mail from the MCP surface.
- Paid plans required for API/MCP access (Starter and Growth); Hobby stays dashboard-only.
- Exact MCP tool names are only visible after OAuth sign-in; capability surface is documented via the Read API.
- Aggregates only - intentionally no visitor-level data, so deep funnel/user-journey analysis is out of scope.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Google Analytics MCP - GA4 Reporting for Agents](/hermes/mcp/servers/external/google-analytics-mcp)
- [Otto MCP - Live Marketing Data and Website Operations in Chat](/hermes/mcp/servers/external/otto-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
