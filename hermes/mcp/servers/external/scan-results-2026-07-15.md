---
title: "MCP Server Scan — July 15, 2026"
description: "Automated scan of mcpservers.org (sitemap) + mcp.so. 11 new servers found, 4 business-relevant guides created."
category: mcp
tags: [mcp-scan, discovery, mcp-servers]
last_updated: 2026-07-15
---

# MCP Server Scan — July 15, 2026

**Sources:** mcpservers.org (sitemap extraction) + mcp.so
**Date:** July 15, 2026
**Previous scan:** July 14, 2026 (supplement — 10 servers found)

## Methodology Change

mcpservers.org no longer returns inline JSON data with browser UA (SolidJS SSR now renders shell-only). Switched to sitemap extraction — mcpservers.org publishes server URLs with lastmod dates in `/sitemaps/servers/1.xml` through `/sitemaps/servers/5.xml`. Filtered for servers with lastmod >= 2026-07-14.

mcp.so remains HTML-only (no API). Web tools (Firecrawl) unavailable in cron environment — mcp.so not scanned this cycle.

## New Since July 14 Scan: 11 servers, 4 guides created

### Guide-Worthy (Business-Relevant)

| Server | Source | Stars | Description | Guide |
|--------|--------|-------|-------------|-------|
| **MCP Email Server** ★ | mcpservers.org | 281★ | IMAP/SMTP email access for AI agents. Send/receive emails via MCP. Direct competitor to CorpusIQ email connector pattern. | [Guide](/hermes/mcp/servers/external/mcp-email-server/) |
| **XActions** ★ | mcpservers.org | 384★ | Complete X/Twitter automation toolkit: scrapers, MCP server, CLI, browser scripts. No API fees. Auto follow, like, comment, scrape. | [Guide](/hermes/mcp/servers/external/xactions-mcp/) |
| **Pretensor** ★ | mcpservers.org | 5★ | Kuzu-backed schema graph from live DB introspection. Creates knowledge graphs and serves MCP tools for AI to retrieve precomputed models. | [Guide](/hermes/mcp/servers/external/pretensor-mcp/) |
| **MCP Notify** | mcpservers.org | 28★ | Monitor MCP Registry for new/updated/removed servers. Notifications via Discord, Slack, Email, Telegram, Webhooks, RSS. Includes CLI, Go SDK, REST API. | [Guide](/hermes/mcp/servers/external/mcp-notify/) |

### INDEX-ONLY (Niche or Developer-Focused)

| Server | Source | Description |
|--------|--------|-------------|
| **jshookmcp** | mcpservers.org | JS hook toolkit (1,746★). Developer tool for runtime instrumentation. |
| **thinair-data** | mcpservers.org | ThinAir Telematics data access. Vehicle telematics niche. |
| **thinair-geo** | mcpservers.org | ThinAir Telematics geospatial. Fleet/telematics niche. |
| **taiwan-health-mcp** | mcpservers.org | Taiwan health data access. Regional healthcare niche. |
| **lyra-web3-playground** | mcpservers.org | Web3 playground. Crypto/blockchain niche. |
| **free-crypto-news** | mcpservers.org | Free crypto news access. Already saturated category. |
| **compeller-mcp** | mcpservers.org | Official Compeller MCP server. No GitHub repo found — details unavailable. |

## Trends

1. **Email integration via MCP maturing:** The MCP Email Server at 281★ signals demand for email-as-tool for AI agents. Directly adjacent to CorpusIQ's email connector value prop — watch for competitive positioning.

2. **Social automation unbundling:** XActions (384★) shows alternative approach to social via MCP — scraping-based vs API-based. The "no API fees" positioning targets the same pain point as Postiz/xurl alternatives.

3. **Registry meta-tools emerging:** MCP Notify (28★) represents the first "MCP registry monitoring" tool — infrastructure for tracking the MCP ecosystem itself. Meta-category forming.

4. **Knowledge graph MCPs:** Pretensor brings Kuzu graph DB + MCP for schema-aware AI retrieval. Adjacent to the "business intelligence via MCP" trend observed in prior scans.

5. **Volume consistent:** ~10-15 new servers/day across mcpservers.org (~9,800 total). Ecosystem continues rapid expansion.

## Actions Taken

- 4 integration guides drafted for business-relevant servers
- 7 servers indexed (too niche for full guides)
- Scan methodology updated for mcpservers.org sitemap extraction
- mcp.so scan deferred — blocked by cron environment limitations (Firecrawl not configured)
