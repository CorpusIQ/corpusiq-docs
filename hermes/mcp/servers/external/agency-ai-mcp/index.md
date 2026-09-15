---
title: "Agency AI MCP: Meta and Google Ads Management from Chat"
description: "Hosted remote MCP server that turns Claude and ChatGPT into a full ad manager for Meta and Google ad accounts. Create, update and pause campaigns, adsets and ads; read pacing, anomalies, performance time series, brand info and budget recommendations through 14 typed tools at s.agencyai.app/mcp. Apache-2.0 licensed, deepest automation on Shopify, works with any store."
category: Marketing
stars: n/a (new listing)
added: 2026-08-24
source: mcpservers.org /all page 1
relevance: ★★
tags: [meta-ads, google-ads, advertising, campaign-management, remote-mcp, shopify]
---

# Agency AI MCP

**Create, launch, and manage Meta and Google ads from Claude and ChatGPT with real-time performance insight and budget optimization.** Agency AI MCP exposes the Agency AI ad-management platform as a hosted remote MCP endpoint at `https://s.agencyai.app/mcp`, so an agent can read campaign data, get recommendations, and make real changes to live ad accounts without leaving the chat. Fourteen typed tools cover ad creation, editing, status control, pacing, anomaly detection, and performance time series. Works with any e-commerce platform or website, with the deepest automation on Shopify.

```
Server type: Remote (Streamable HTTP, hosted)
Endpoint: https://s.agencyai.app/mcp (platform at agencyai.app)
Repo: github.com/agency-ai-dev/agency-ai-mcp (Apache-2.0, Aug 2026)
Tools: 14 verified (create_ad, update_ad, update_adset, update_campaign, set_campaign_status, get_ads, get_adsets, get_campaigns, get_ad_creative, get_pacing, get_anomalies, get_performance_timeseries, get_recommendations, get_brand_info, get_operation_status)
```

## Why This Matters for Operators

Paid acquisition is where operator time leaks: checking pacing, comparing adsets, pausing losers, and scaling winners across two ad platforms that live in different dashboards. Agency AI MCP collapses that into one agent conversation with write access. Ask for anomalies, get the offending adset, tell the agent to pause it or bump the budget, and the change lands in the live account, all logged through the platform. For Shopify operators especially, the platform's automation covers the campaign lifecycle end to end.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_campaigns`, `get_adsets`, `get_ads` | Reads account structure with performance data from Meta and Google accounts |
| `create_ad`, `update_ad`, `update_adset`, `update_campaign` | Creates and edits ads, adsets, and campaigns in live accounts |
| `set_campaign_status` | Pauses, resumes, or changes campaign status |
| `get_pacing` | Reports budget pacing against schedule for campaigns |
| `get_anomalies` | Flags spend, CPC, or CTR anomalies across accounts |
| `get_performance_timeseries` | Returns time-series performance for trend analysis |
| `get_recommendations` | Surfaces budget and structural optimization recommendations |
| `get_brand_info`, `get_ad_creative` | Reads brand context and creative assets for consistent ad generation |

## Installation

```json
{
  "mcpServers": {
    "agency-ai": {
      "type": "http",
      "url": "https://s.agencyai.app/mcp"
    }
  }
}
```

The endpoint is hosted; no install, no repo checkout, and no SDK. Connect with Claude Code, ChatGPT, Cursor, or any MCP-compatible client, then authenticate the ad accounts through the platform.

## Configuration

Connect your Meta and Google ad accounts in the Agency AI platform, then link the MCP endpoint to your client. The platform holds the platform credentials; the agent receives scoped access through the server. Read-only tools are safe to run freely; mutation tools (create, update, set status) change live accounts, so operators should confirm the affected account before authorizing writes.

## Example Prompts

- "Which adsets are pacing over budget this week, and which have anomalies?"
- "Pause the two worst-performing Google campaigns and bump the best Meta adset by 10 percent."
- "Create a Meta ad for this Shopify product using our brand info and best creative."
- "Give me a weekly performance time series across both accounts and summarize the trend."

## Business Relevance

- **Shopify and DTC operators** run Meta and Google acquisition from one conversation
- **Performance marketers** get anomaly and pacing alerts without dashboard switching
- **Founders without a media buyer** get structured recommendations before making budget calls
- **Agencies** manage multiple client ad accounts through scoped platform access

## Integration with CorpusIQ

Agency AI MCP answers what the ads are doing; CorpusIQ answers whether it is working. An agent can pull campaign performance and spend from Agency AI, then join it against attributed revenue, orders, and customer cohorts from CorpusIQ connectors to compute true ROAS and LTV per campaign, closing the loop from ad click to retained customer.

## Limitations

- Young project (1 GitHub star at listing time, Aug 2026); platform maturity is unproven.
- Requires Agency AI platform accounts for Meta and Google, which adds a middle layer between the agent and the ad platforms.
- Mutation tools touch live ad spend; operators should gate writes with explicit approval.
- Ad platform API coverage depth should be validated against your specific account features.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Meta Ads MCP](/docs/hermes/mcp/servers/external/meta-ads-mcp) - Meta Ads management tools
- [Inside Ads MCP](/docs/hermes/mcp/servers/external/inside-ads-mcp) - ad account performance intelligence
- [AdWhispr MCP](/docs/hermes/mcp/servers/external/adwhispr-mcp) - Meta ad library research
- [OrbiAds GAM MCP](/docs/hermes/mcp/servers/external/orbiads-gam-mcp) - Google Ad Manager operations
