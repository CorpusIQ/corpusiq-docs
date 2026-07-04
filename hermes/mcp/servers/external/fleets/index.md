---
title: Fleets MCP Integration Guide
description: Full setup guide for Fleets MCP — multi-site analytics dashboard for AI agents with GA4, Search Console, Cloudflare, and PageSpeed data
---

# Fleets MCP — Integration Guide

**Multi-site analytics dashboard for AI agents.** Read-only GA4, Search Console, Cloudflare edge, and PageSpeed data across every site you run, plus audits that return paste-ready fixes — all through a single MCP server.

> **Command:** `npx -y fleets-mcp` · **Source:** mcp.so · **Last seen:** July 4, 2026

## What It Does

Fleets gives your AI agent a unified analytics view across all your web properties. Instead of checking Google Analytics, Search Console, Cloudflare, and PageSpeed separately, your agent queries all four through one MCP endpoint. Ask "Which of my sites had the biggest traffic drop this week and what's causing it?" and the agent cross-references analytics, search data, and edge/CDN metrics in one pass — then returns paste-ready fixes from the audit tools.

## Key Capabilities

- **GA4 Analytics** — Traffic, conversions, user behavior, and trends across all sites
- **Google Search Console** — Search performance, indexing status, query rankings, and click-through rates
- **Cloudflare Edge** — CDN performance, security events, caching metrics, and edge analytics
- **PageSpeed Insights** — Performance audits, Core Web Vitals, and optimization recommendations
- **Audit Engine** — Returns paste-ready fixes for identified issues (not just problem descriptions)
- **Cross-Site Comparison** — Compare metrics across your entire portfolio in one query

## Installation

```bash
npx -y fleets-mcp
```

Pairs with the Fleets CLI (npm: `fleets`) for additional management.

## Hermes / Claude Desktop Configuration

```json
{
  "mcpServers": {
    "fleets": {
      "command": "npx",
      "args": ["-y", "fleets-mcp"],
      "env": {
        "GA4_PROPERTY_IDS": "prop1,prop2,prop3",
        "GSC_SITE_URLS": "https://site1.com,https://site2.com",
        "CLOUDFLARE_API_TOKEN": "your-cf-token",
        "CLOUDFLARE_ZONE_IDS": "zone1,zone2"
      }
    }
  }
}
```

## CorpusIQ Use Cases

### 1. Weekly Traffic Audit
```
"Compare traffic across all my sites this week vs last week. Which sites 
dropped more than 10%? Check their Search Console and PageSpeed — give 
me paste-ready fixes for the top 3 issues."
```
Automated weekly audit that previously required checking 4+ dashboards.

### 2. SEO Health Check
```
"Show me all pages with declining search rankings, their current Core Web 
Vitals, and whether Cloudflare shows any edge errors for those URLs."
```
Cross-references GSC rankings with PageSpeed performance and CDN health.

### 3. Launch Monitoring
```
"We launched the new landing page yesterday. Show me GA4 traffic, GSC 
indexing status, and PageSpeed score for that specific URL."
```
Post-launch monitoring across all analytics surfaces.

## Operator Value

| Task | Manual (per site) | With Fleets MCP |
|------|------------------|----------------|
| Weekly traffic review | 10-15 min checking GA4 | 30 seconds, all sites at once |
| SEO issue diagnosis | 20-30 min across GSC + PageSpeed | 1 query, cross-referenced |
| Performance audit | 5 min per URL in PageSpeed | 1 query across all URLs |

## Data Safety

Fleets is **read-only** — it cannot modify your analytics, search console settings, or Cloudflare configuration. All recommendations are paste-ready fixes that you review and apply manually. This makes it safe for production use without risk of automated changes to your live infrastructure.

## Prerequisites

- Google Analytics 4 properties with API access
- Google Search Console site properties
- Cloudflare API token (read-only sufficient)
- Node.js 18+

## Related Resources

- [External MCP Server Catalog](/hermes/mcp/servers/external/) — full curated catalog
- [Analytics & BI MCPs](/hermes/mcp/servers/external/#analytics--business-intelligence) — complementary analytics tools
- [CorpusIQ GA4 Connector](/hermes/mcp/connectors/) — native GA4 data access through CorpusIQ

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Servers Home](/hermes/mcp/servers/) →*

*Guide created July 4, 2026. Fleets available via `npx -y fleets-mcp`. Check mcp.so for latest documentation and CLI updates.*
