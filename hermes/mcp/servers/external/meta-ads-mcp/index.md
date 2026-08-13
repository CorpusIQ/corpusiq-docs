---
title: "Meta Ads MCP — Integration Guide"
description: Connect AI agents to Facebook/Instagram Ads for campaign management, creative analysis, and performance optimization through MCP.
github: https://github.com/pipeboard-co/meta-ads-mcp
stars: 1112
status: Verified (Meta Business badge)
transport: Hosted Remote MCP
auth: OAuth 2.0 (Meta Business Login)
category: Advertising & Marketing
added: 2026-07-29
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/meta-ads-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Meta Ads MCP — Integration Guide

## Overview

The Pipeboard Meta Ads MCP server connects AI agents directly to Facebook and Instagram advertising — campaign management, ad set optimization, creative analysis, audience insights, and performance reporting. Part of Pipeboard's 5-platform advertising family (also Google Ads, TikTok Ads, Snapchat Ads, and Reddit Ads).

For e-commerce and DTC operators, this is transformative: "Which ad set has the highest ROAS this week and should I scale it?" becomes a single conversation with your AI agent instead of 20 minutes navigating Ads Manager.

## Quick Start

### Prerequisites
- Meta Business account with Ads Manager access
- Facebook App with Ads Management permissions
- Node.js 18+ or use the hosted endpoint

### Installation

**Option 1: Hosted Remote (Recommended)**
```bash
npx mcp-remote https://mcp.pipeboard.co/meta-ads
```

**Option 2: Local Setup**
```bash
npx @pipeboard-co/meta-ads-mcp
```

### MCP Client Config

```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "npx",
      "args": ["@pipeboard-co/meta-ads-mcp"],
      "env": {
        "META_APP_ID": "your-app-id",
        "META_APP_SECRET": "your-app-secret",
        "META_ACCESS_TOKEN": "your-access-token",
        "META_AD_ACCOUNT_ID": "act_123456789"
      }
    }
  }
}
```

### Authentication

OAuth 2.0 via Meta Business Login. Required permissions:
- `ads_read` — Read campaign/ad set/ad data
- `ads_management` — Create/edit campaigns (optional, for write tools)
- `business_management` — Access business-level settings

For operators: generate a System User token in Meta Business Settings → System Users for persistent agent access.

## Tools

Meta Ads MCP exposes 20+ tools across these categories:

| Category | Tools | Description |
|----------|-------|-------------|
| **Campaigns** | `list_campaigns`, `get_campaign`, `create_campaign`, `update_campaign` | Full campaign lifecycle management |
| **Ad Sets** | `list_ad_sets`, `get_ad_set`, `update_ad_set` | Budget, audience, placement management |
| **Ads** | `list_ads`, `get_ad`, `create_ad` | Creative and copy management |
| **Insights** | `get_insights`, `get_breakdown` | Performance metrics (impressions, clicks, CTR, CPC, ROAS, conversions) |
| **Audiences** | `list_audiences`, `get_audience_overlap` | Custom and lookalike audience analysis |
| **Creatives** | `list_creatives`, `analyze_creative` | Creative performance and analysis |

## Business Operator Use Cases

### 1. Performance Monitoring
```
User: "Which campaigns have ROAS below 1.5x this week?"
Agent: [queries all active campaigns, filters by ROAS, flags underperformers with spend and recommendations]
```

### 2. Budget Optimization
```
User: "If I have $5,000 more budget, where should I put it?"
Agent: [analyzes marginal ROAS across ad sets, recommends allocation with projected impact]
```

### 3. Creative Analysis
```
User: "Which ad creative performed best in the prospecting campaign?"
Agent: [pulls creative-level breakdown by CTR, CVR, CPA; ranks creatives; notes common elements in top performers]
```

### 4. Audience Insights
```
User: "What's the overlap between my 5% lookalike and my email list audience?"
Agent: [runs audience overlap analysis, returns overlap percentage and size]
```

### 5. Automated Scaling Rules
Combine with cron: have AI agents check ROAS thresholds daily, increase budget on winning ad sets, pause underperformers.

## Security Considerations

- **Ad Account Isolation:** Each MCP instance connects to one ad account — use separate configs for multiple accounts
- **Permission Scope:** Start with `ads_read` only for analytics use cases. Add `ads_management` only when you trust the agent with budget changes
- **Approval Gates:** Consider implementing a human-approval step before executing budget changes >$X
- **Meta Rate Limits:** Meta API has strict rate limits. The MCP handles basic throttling but avoid querying insights every minute
- **Token Rotation:** System User tokens expire. Set calendar reminders to rotate every 60 days

## Pricing

- **Meta Ads MCP:** Free and open source (MIT license)
- **Meta Ads API:** Included with any Meta Ads account (no additional API cost)
- **Pipeboard Hosted:** Currently free during beta; pricing TBD

## Comparison: Meta Ads MCP vs OpusGrowth MCP

| Feature | Meta Ads MCP | OpusGrowth MCP |
|---------|-------------|----------------|
| Stars | 1,112⭐ | Pre-launch |
| Platforms | Meta only (FB + IG) | Google, Microsoft, TikTok, LinkedIn |
| Depth | Deep Meta features | Broad cross-platform |
| Write tools | Yes (campaign CRUD) | Yes (with approval gates) |
| Best for | Meta-heavy advertisers | Cross-platform agencies |

They're complementary: Meta Ads MCP for deep Facebook/Instagram operations, OpusGrowth for unified cross-platform management.

## See Also

- [OpusGrowth MCP Guide](/hermes/mcp/servers/external/opusgrowth-mcp/) — Cross-platform ad management
- [Ahrefs MCP Guide](/hermes/mcp/servers/external/ahrefs-mcp/) — SEO and organic traffic context
- [Stripe MCP Guide](/hermes/mcp/servers/external/stripe-mcp/) — Revenue-side validation
- [Pipeboard Documentation](https://pipeboard.co/docs)
