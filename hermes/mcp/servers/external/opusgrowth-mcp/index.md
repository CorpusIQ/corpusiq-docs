---
title: OpusGrowth MCP — Ad Platform Connector
description: Hosted MCP connector for Google Ads, Microsoft Advertising, TikTok Ads, and LinkedIn Ads — 233 tools with write-action approval gates
severity: ★★★ (high business value)
source: mcpservers.org · GitHub
created: 2026-07-25
topics: ads, ppc, marketing, google-ads, linkedin-ads, tiktok-ads, microsoft-advertising
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/opusgrowth-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# OpusGrowth MCP — Ad Platform Connector

## Overview

OpusGrowth MCP is a hosted MCP connector that brings Google Ads, Microsoft Advertising, TikTok Ads, and LinkedIn Ads under a single agent-native interface. With 233 tools and real write actions (protected by approval gates), it lets AI agents manage paid campaigns across all four major ad platforms from Claude, ChatGPT, or any MCP-compatible client.

**Why it matters for operators:** Ad spend management is one of the highest-ROI use cases for AI agents. Instead of logging into 4 different dashboards, an operator can describe a budget reallocation or bid adjustment in natural language and have the agent execute it — with approval gates keeping a human in the loop for spend decisions.

| Detail | Value |
|--------|-------|
| **GitHub** | [opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms](https://github.com/opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms) |
| **Created** | July 10, 2026 |
| **Updated** | July 24, 2026 |
| **Stars** | 0 (new) |
| **Type** | Hosted MCP (API endpoint) |
| **Auth** | OAuth per ad platform |
| **Pricing** | Not yet published (pre-launch) |

## Supported Platforms

| Platform | Tools | Write Actions |
|----------|-------|---------------|
| **Google Ads** | Campaign management, keyword planning, bid adjustments, performance reports | Yes (approval-gated) |
| **Microsoft Advertising** | Campaign CRUD, ad group management, budget controls | Yes (approval-gated) |
| **TikTok Ads** | Creative management, audience targeting, campaign metrics | Yes (approval-gated) |
| **LinkedIn Ads** | Campaign creation, audience builder, lead gen form management | Yes (approval-gated) |

## Key Capabilities

### 1. Cross-Platform Campaign Management
Create, pause, or modify campaigns across all four platforms through a unified interface. Adjust budgets, bids, and targeting without switching dashboards.

### 2. Write Actions with Approval Gates
All spend-affecting operations (budget changes, bid adjustments, campaign activation) require explicit approval. Read operations (reporting, metrics, audit) are gate-free. This matches the operator workflow: research freely, execute deliberately.

### 3. Performance Intelligence
Pull cross-platform performance data into a single view. Compare ROAS, CPA, and CTR across Google, Microsoft, TikTok, and LinkedIn in one query.

### 4. Agent-Native Design
Built specifically for MCP clients (Claude, ChatGPT, Cursor, etc.) rather than retrofitted from a REST API. Tools are discovered automatically and surfaced in the agent's context.

## Integration Setup

```json
{
  "mcpServers": {
    "opusgrowth": {
      "type": "http",
      "url": "https://api.opusgrowth.com/mcp",
      "headers": {
        "Authorization": "Bearer ${OPUSGROWTH_API_KEY}"
      }
    }
  }
}
```

1. Sign up at [opusgrowth.com](https://opusgrowth.com) (pre-launch — join waitlist)
2. Connect your ad platform accounts via OAuth
3. Add the MCP endpoint to your agent config
4. Start with read-only queries to verify data access
5. Enable write actions per platform as needed

## Business Operator Use Cases

- **Budget rebalancing:** "Move $500 from underperforming TikTok campaigns to the top Google Search campaign"
- **Performance audit:** "Show me yesterday's ROAS across all platforms, sorted worst to best"
- **Competitive response:** "What keywords is competitor X bidding on? Increase our bids on overlapping terms by 15%"
- **Reporting:** "Generate a Monday morning performance summary across Google, Microsoft, TikTok, and LinkedIn"

## Limitations

- **Pre-launch:** Product is not yet publicly available (July 2026). Waitlist only.
- **New project:** 0 stars, early stage. Production reliability unproven.
- **Hosted only:** No self-hosted option. Data flows through OpusGrowth's infrastructure.
- **Platform API dependencies:** Subject to each ad platform's API rate limits and policy changes.

## Verdict

**Watch closely.** This is the right architecture (MCP-native, approval-gated writes, cross-platform) for a high-value operator problem (ad spend management). If OpusGrowth executes well, this could become an essential tool for any business operator running paid acquisition. For now, join the waitlist and monitor for the public launch.

## See Also

- [[hermes/mcp/servers/external/google-ads-mcp]] — Google Ads MCP (individual platform)
- [[hermes/mcp/servers/external/gainium-mcp]] — Gainium trading MCP (finance)
- [[hermes/mcp/servers/external/capital-com-mcp]] — Capital.com trading MCP
