---
title: "AppSigma App Store Data MCP — ASO & App Analytics for AI Agents"
description: "Full public App Store search results as users see them — rankings, reviews, ASO keywords, sponsored slots, charts, and app analytics from any MCP client."
category: mcp
tags: [mcp-server, app-store, aso, ios, app-analytics, keyword-research, app-marketing]
last_updated: 2026-07-08
---

# AppSigma App Store Data MCP — ASO Intelligence

## What It Is

AppSigma's App Store Data MCP (`appsigma.io`) gives AI agents the full public App Store — search results as users actually see them (sponsored slots included), full review text, ranking charts, ASO keyword data, and app analytics. Mobile growth teams can research competitors, track keyword rankings, and analyze reviews without leaving their AI assistant.

## Tools Available

| Tool | Description |
|------|-------------|
| App search | Search results with sponsored slot visibility |
| Review analysis | Full review text, ratings distribution, sentiment |
| Keyword research | ASO keyword rankings and search volume |
| Charts & rankings | Category and overall chart positions |
| App analytics | Downloads estimates, revenue estimates |

## Quick Start

```bash
npx mcp-remote https://api.appsigma.io/mcp
```

## Business Use Cases

1. **Competitor ASO audit**: "What keywords is Competitor X ranking #1 for that we're not targeting?"
2. **Review intelligence**: "Summarize the top 3 complaints in our last 100 reviews — group by theme"
3. **Launch monitoring**: "How did our keyword rankings change in the first week after the v3.0 launch?"
4. **Market sizing**: "Estimated monthly downloads for top 10 apps in the Health & Fitness category"

## Limitations

- **iOS App Store only**: No Google Play Store support
- **Public data only**: No private App Store Connect analytics
- **Remote-hosted**: API via appsigma.io

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Marketing Connectors — GA4, Google Ads, Semrush](/hermes/mcp/connectors/)
