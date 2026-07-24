# MCP Server Sweep — July 24, 2026 (Cron Run 2)

**Sweep time:** 2026-07-25T00:00 UTC (cron)
**Sources checked:** mcp.so, mcpservers.org
**Previous sweep:** 2026-07-24T18:00 UTC
**New servers found:** 3

## New Servers Discovered

| Server | Category | Source | Date Added |
|--------|----------|--------|------------|
| PLUR MCP | Memory & Knowledge | mcp.so | Jul 24 |
| Charming MCP | Development | mcp.so | Jul 24 |
| Gainium MCP | Finance / Trading | mcp.so | Jul 24 |

## Highlights

- **PLUR** (226★): Open, local-first memory for AI agents. Stores corrections, preferences, and conventions as plain-text engrams on your machine. MIT licensed. GitHub: `plur-ai/plur`.
- **Charming** (9★): Hosted MCP server that generates, hosts, and updates interactive web apps. Connect any MCP client, describe an app, get a live URL in seconds. OAuth-native. GitHub: `tambo-labs/charming-mcp`.
- **Gainium** (4★): AI-powered crypto trading automation platform. No-code strategy builder, backtesting engine, multi-exchange support. Docker Compose deployment with MCP tools for portfolio monitoring, strategy management, and market data. GitHub: `Gainium/docker-sh`.

## Integration Guides Created

All 3 new servers have integration guides at `servers/external/`:
- `plur-mcp/index.md`
- `charming-mcp/index.md`
- `gainium-mcp/index.md`

## Notes

- **mcp.so**: PLUR, Charming, and Gainium appeared in the "New arrivals" section on the mcp.so homepage. These were published today (July 24) and were not captured by the earlier 18:00 UTC sweep which focused on Groundwork MCP.
- **mcpservers.org**: No new servers detected in the "newest" listing that aren't already catalogued. Sitemap analysis shows ~30 servers with July 24 timestamps across 6 sitemaps, but most are low-star community projects. Notable sitemap entries (Apify MCP, Reddit Devvit MCP) still pending Firecrawl verification for guide quality.
- **Scraping method**: Used Playwright (headless Chromium) to scrape mcp.so homepage "New arrivals" section after Firecrawl API key was unavailable. mcpservers.org checked via sitemap XML (no JSON API available — SPA).
- **Firecrawl status**: Still not configured on this Hermes instance. Web tool calls fail with "FIRECRAWL_API_KEY not set" error.

## Catalog Stats

- Total servers in catalog: ~179 (3 new this sweep)
- Guides format: Standard (name, description, quick start, key tools, use cases, Hermes integration)
- Sources: mcp.so (3)

## Pending

- 27+ mcpservers.org servers from July 23 scan-results still without guides — pending Firecrawl restoration or Mac Mini Playwright scraping
- Apify MCP Server (mcpservers.org, Jul 24) — needs verification
- Reddit Devvit MCP (mcpservers.org, Jul 24) — needs verification
- Video Editing MCP (mcpservers.org, Jul 24) — needs verification
