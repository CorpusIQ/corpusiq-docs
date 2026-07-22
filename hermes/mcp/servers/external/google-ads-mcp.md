---
title: Google Ads MCP Server Integration Guide
description: AI-powered Google Ads campaign management — create, monitor, and optimize campaigns, ad groups, keywords, and budgets directly from Hermes Agent.
category: mcp
tags: [mcp, google-ads, advertising, ppc, campaigns, marketing, sem, hermes-agent]
last_updated: 2026-07-21
---

# Google Ads MCP — Ad Campaign Management for Hermes Agent

Google Ads MCP gives your AI agent direct access to Google Ads campaign management. Create campaigns, adjust bids, pull performance reports, and monitor budgets — all through natural language commands to your agent.

## What It Does

Google Ads MCP connects your agent to the Google Ads API:

- **Campaign management** — Create, update, pause, and list campaigns
- **Ad group operations** — Manage ad groups within campaigns
- **Keyword management** — Add, update, and monitor keyword performance
- **Budget tracking** — Monitor spend, set budgets, and get alerts on overruns
- **Performance reports** — Pull campaign metrics (impressions, clicks, conversions, CPA, ROAS)

## Quick Setup

### Prerequisites
- **Google Ads account** with API access enabled
- **Developer token** from Google Ads API center
- **OAuth2 credentials** (client ID + client secret) from Google Cloud Console
- **Customer ID** (the 10-digit Google Ads account number)
- **Rust toolchain** (this MCP is written in Rust — `cargo build`)

### Add to Hermes Agent

```bash
git clone https://github.com/codeChap/mcp-server-google-adwords
cd mcp-server-google-adwords
cargo build --release
```

```json
{
  "mcpServers": {
    "google-ads": {
      "command": "path/to/mcp-server-google-adwords/target/release/google-ads-mcp",
      "env": {
        "GOOGLE_ADS_CLIENT_ID": "your_client_id",
        "GOOGLE_ADS_CLIENT_SECRET": "your_client_secret",
        "GOOGLE_ADS_DEVELOPER_TOKEN": "your_dev_token",
        "GOOGLE_ADS_CUSTOMER_ID": "1234567890",
        "GOOGLE_ADS_REFRESH_TOKEN": "your_refresh_token"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `list_campaigns` | List all campaigns with status, budget, and performance summary |
| `get_campaign` | Get detailed campaign metrics for a date range |
| `create_campaign` | Create a new Search, Display, or Performance Max campaign |
| `update_campaign_budget` | Adjust daily budget for a campaign |
| `pause_campaign` / `enable_campaign` | Toggle campaign status |
| `list_ad_groups` | List ad groups within a campaign |
| `get_keywords` | Get keyword performance data (impressions, clicks, CTR, CPC, conversions) |
| `add_keywords` | Add keywords to an ad group with match type and bids |
| `get_account_summary` | Account-level spend, impressions, conversions summary |
| `get_search_terms` | Pull search term report for negative keyword discovery |

## Use Cases for Business Operators

### 1. Campaign Health Check
Daily performance scan in one command:

```
Agent prompt: "Check all my Google Ads campaigns. Flag any with
CPA above $50, CTR below 1%, or daily budget fully consumed
before 2 PM. Recommend what to pause or adjust."
```

### 2. Budget Rebalancing
Shift spend based on performance:

```
Agent prompt: "Campaign A has a 3.2 ROAS, Campaign B has 0.8 ROAS.
Move $50/day from Campaign B to Campaign A. If Campaign A's ROAS
drops below 2.5 in the next 3 days, revert the change."
```

### 3. Negative Keyword Discovery
Prevent wasted spend automatically:

```
Agent prompt: "Pull this week's search term report for all campaigns.
Find queries that spent over $20 with zero conversions.
Add them as negative keywords. Show me what you blocked."
```

### 4. Performance Max Monitoring
Track PMax campaign performance:

```
Agent prompt: "How's my Performance Max campaign doing vs last week?
Show me impressions, clicks, conversions, and cost by asset group.
Flag any asset groups with below-average performance."
```

## Integration with CorpusIQ

Google Ads MCP + CorpusIQ = complete marketing operations:

1. **CorpusIQ GA4 connector** → correlate ad spend with on-site behavior
2. **CorpusIQ Stripe connector** → track ROAS to actual revenue, not just conversions
3. **CorpusIQ Search Console connector** → align paid + organic keyword strategy
4. **AI agent** → cross-reference ad performance with CRM pipeline data

This gives you a marketing command center where your agent monitors all paid channels, rebalances budgets, and catches wasted spend — before it burns through your monthly ad budget.

## Pricing

- **Google Ads MCP:** Open source (MIT), free
- **Google Ads API:** Free (token-based access, basic access sufficient for most use cases)
- **Google Ads spend:** Your ad budget (no additional API fees)

## Limitations

- Developer token requires application approval from Google (standard level sufficient for most)
- OAuth2 refresh token must be generated via playground or app
- Google Ads API has daily quota limits (typically 10,000-15,000 operations/day for basic access)
- Rust build required — `cargo` toolchain must be installed
- Performance Max campaign management is limited vs Search campaigns

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
