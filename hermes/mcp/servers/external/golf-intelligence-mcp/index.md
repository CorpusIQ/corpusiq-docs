---
title: "Golf Intelligence MCP - Golf Course Data for AI Agents"
description: "Proprietary golf course dataset by Stracka: 20 years of course-by-course mapping (laser, drone, airplane, satellite), updated daily. Free course-group search, then credit-metered scorecards, GPS geometry, course details and green slope images over a read-only Streamable HTTP API."
category: Data & Analytics
stars: 0
added: 2026-08-27
source: "mcp.so GitHub issue #3787"
relevance: ★★
tags: [golf, sports-data, geo-data, course-mapping, data-api, remote-mcp]
---

# Golf Intelligence MCP

**Remote MCP server (Streamable HTTP, client-credentials auth) for Golf Intelligence by Stracka - a proprietary golf course dataset with 20 years of course-by-course mapping.** Five read-only tools: free course-group search, then credit-metered scorecards, GPS geometry, detailed course data, and green slope images. The endpoint answered a live anonymous initialize (serverInfo `golf` v1.0.0, protocol 2025-06-18) and `/health` returns ok; all five tools were confirmed via tools/list. The dataset is built by a ten-person mapping team working daily since 2007, using laser, drone, airplane, and satellite capture - explicitly not a scrape of any existing golf API.

```
Server type: Remote (Streamable HTTP)
Auth: Client credentials via X-GI-Client-ID and X-GI-Active-Token headers (exchanged for a short-lived bearer token)
Endpoint: https://mcp.golfintelligence.com/mcp
Health: https://mcp.golfintelligence.com/health
Tools: 5 (all read-only, idempotent, no destructive hints)
Pricing: Search free; paid lookups 1-3 credits with explicit confirm_spend; Personal $49 (50 test credits), Starter $399/mo (10,000 credits)
Category: Data & Analytics
Built by: Stracka / Golf Intelligence (registry io.github.golf-data/golf v1.0.0)
```

## Why This Matters for Operators

Golf course data normally means either scraping course websites or licensing expensive GIS datasets. Golf Intelligence is the structured alternative: a continuously maintained, proprietary course-group database where search is free and lookups are metered in credits. For anyone building or operating a golf product - booking platforms, travel operators, course-management software, market analysts - the scorecard, geometry, and greens data comes pre-normalized instead of as a multi-month scraping and cleanup project.

**The spend gate is the notable design detail.** Before every paid call the user must explicitly confirm the stated credit cost (`confirm_spend=true`); without confirmation the server refuses paid tools. Agents cannot burn credits by looping.

## Tools & Capabilities

| Tool | Purpose | Credits |
|---|---|---|
| `search_course_groups` | Free search over the Golf Intelligence course-group dataset before any paid call | 0 |
| `get_course_group_scorecard` | Scorecard data for a course group (holes, pars, distances) | 1 |
| `get_course_group_gps` | Mapped course geometry and coordinates | 2 |
| `get_course_group_detail` | Detailed course-group data record | 3 |
| `get_green_slope_image` | Portrait or square green slope image for a hole | 1 |

All five tools were confirmed by a live probe; annotations declare the surface read-only, idempotent, and non-destructive.

## Installation

Create an API account at console.golfintelligence.com, then add the hosted endpoint with the credential headers:

```json
{
  "mcpServers": {
    "golf": {
      "type": "http",
      "url": "https://mcp.golfintelligence.com/mcp",
      "headers": {
        "X-GI-Client-ID": "your-client-id",
        "X-GI-Active-Token": "your-active-token"
      }
    }
  }
}
```

A local stdio build is also available from the repo (`node dist/index.js` with `GI_CLIENT_ID` and `GI_ACTIVE_TOKEN` env vars), and a Fly.io container deploy is documented in the README.

## Configuration

- **Credentials:** the two header values come from the Golf Intelligence console. The Active Token is NOT itself a bearer token; the server exchanges it via `POST https://api.golfintelligence.com/auth/authenticateToken` (client-credentials grant) for a short-lived access token, cached in memory and refreshed after an HTTP 401.
- **Plans:** Personal ($49, 50 test credits, own-app use) and Starter ($399/month, 10,000 credits, shipping an app to other users; arranged by emailing data@golfintelligence.com).
- **Spend safety:** paid tools require `confirm_spend=true` per call; `search_course_groups` is always free.

## Business Relevance

- **Golf product builders** skip dataset construction entirely: search first (free), then pull scorecards, geometry, and greens imagery for the courses their product covers.
- **Travel and booking operators** enrich itineraries with mapped course data and GPS coordinates instead of hand-maintained venue records.
- **Analysts and course operators** compare structured course-group detail records against the industry without GIS or scraping tooling.

## Integration with CorpusIQ

Complementary surface to CorpusIQ's commerce and analytics connectors: an agent can pull a business's own bookings, revenue, and customer context from CorpusIQ, then use Golf Intelligence to enrich golf-related offerings with course scorecards, geometry, and greens data. Both surfaces are read-only, and Golf Intelligence's explicit spend-confirmation design aligns with CorpusIQ's read-only connector philosophy.

## Limitations

- Credit-metered lookups require explicit per-call spend confirmation, so batch enrichment needs planned credit budgeting.
- The repo is brand new (created Aug 27, 2026, 0 stars) and the plugin code is MIT while the underlying data remains subject to Golf Intelligence's API terms at golfintelligence.com.
- Niche domain: value concentrates in golf-specific products, travel, and market analysis rather than general business operations.
- Course data is the only surface - no tee-time booking, pricing, or availability functions.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [PopOff Data MCP - Reality-TV Social Analytics for AI Agents](/hermes/mcp/servers/external/popoff-data)
- [Alpha Sophia MCP - US Healthcare Provider and Market Data](/hermes/mcp/servers/external/alpha-sophia-mcp)
- [CorpusIQ Connectors](/hermes/mcp/servers)
