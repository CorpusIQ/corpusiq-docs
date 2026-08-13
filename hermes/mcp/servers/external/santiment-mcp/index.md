---
title: "Santiment MCP Connector — Integration Guide"
description: "Official Santiment MCP server for crypto market intelligence. On-chain metrics, social sentiment, trending narratives, and analyst insights — directly in AI"
category: mcp
tags: [mcp-server, crypto, market-intelligence, on-chain, sentiment, trading, fintech, hermes-agent]
last_updated: 2026-07-28
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/santiment-mcp/"
robots: "index,follow"

---

# Santiment MCP — Crypto Market Intelligence for Hermes Agent

The official Santiment MCP connector gives AI tools direct access to crypto market intelligence — on-chain metrics, social sentiment, trending narratives, and analyst insights across 500+ crypto assets.

## What It Does

Santiment MCP bridges AI agents to live crypto market data:

- **Metrics & Asset Discovery** — Browse 30+ metrics across 500+ crypto assets. Filter by asset, metric, or both.
- **Timeseries Data** — Historical metric data (price, volume, market cap, active addresses, exchange flows, social volume) with configurable intervals and time ranges.
- **Asset Screening** — Filter and rank assets by any metric using threshold comparisons (greater than, less than) or percentage changes with sorting and pagination.
- **Insights** — Full analyst insights published on Santiment, with tags, authors, and predictions.
- **Trending Stories** — What narratives are driving crypto markets right now, with bullish/bearish sentiment breakdowns.
- **Combined Trends** — Unified view of trending words, stories, and AI-summarized social media discussions.

### Supported Metrics

| Category | Examples |
|----------|----------|
| **Financial** | Price, volume, market cap, exchange flows |
| **On-Chain** | Active addresses, transaction volume, network growth, NVT ratio |
| **Development** | GitHub activity, dev activity contributors |
| **Social** | Social volume, social dominance, sentiment (positive/negative) |

## Quick Setup

### Prerequisites
- **Santiment account:** Free at [app.santiment.net](https://app.santiment.net). Core metrics available on free tier.
- **MCP-compatible client:** Claude Desktop, Claude Code, ChatGPT, or any Streamable HTTP MCP client

### Connection Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (Remote) |
| **Endpoint** | `https://api.santiment.net/mcp` |
| **Authentication** | OAuth 2.0 with PKCE |
| **Token Life** | 1 hour (auto-refresh) |
| **Tools** | 20+ (metrics, screening, insights, trends, timeseries) |

### Claude Desktop / Claude.ai Setup

1. Open Claude → Customize → Connectors → Add Custom Connector
2. Name: `Santiment`
3. Remote MCP server URL: `https://api.santiment.net/mcp`
4. Click Add — OAuth redirect to Santiment for authorization
5. Log in (or create free account) and approve the connection

### Claude Code CLI Setup

```bash
claude mcp add santiment --transport http https://api.santiment.net/mcp
# OAuth authorization on first use
```

### ChatGPT Setup

1. Settings → Apps → Advanced Settings → Developer Mode → Create App
2. Name: `Santiment`, URL: `https://api.santiment.net/mcp`, Auth: OAuth
3. Authorize via OAuth redirect
4. New chat → "+" → Santiment

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "santiment": {
      "transport": "http",
      "url": "https://api.santiment.net/mcp",
      "auth": "oauth"
    }
  }
}
```

## Key Tools

| Tool | Purpose |
|------|---------|
| `get_available_metrics` | List all 30+ metrics available for a given asset |
| `get_timeseries` | Fetch historical metric data with configurable intervals |
| `screen_assets` | Filter/rank assets by metric thresholds or % changes |
| `get_insights` | Fetch analyst-published insights with tags and predictions |
| `get_trending_stories` | Current market narratives with sentiment breakdowns |
| `get_combined_trends` | Unified trending words, stories, and AI summaries |

## Use Cases for CorpusIQ

### Market Research for Content
Ask your agent: "What are the top 5 trending narratives in crypto this week?" Santiment returns stories ranked by social traction with sentiment breakdowns. Use this to inform content strategy for fintech-adjacent audiences.

### Competitor Intelligence
For crypto-native competitors: "Screen assets in the AI-agent category by developer activity growth over 30 days." Identify which projects are gaining real traction vs. social hype.

### Due Diligence
When evaluating crypto-integrated partners: "Show me on-chain activity trends for [token] over the last 90 days, plus any divergence between social sentiment and active addresses." Catch tokens where hype outpaces actual usage.

## Example Queries

**Market research:** "What's trending in crypto right now? Give me the top 3 stories with sentiment."
**Validation:** "Is this token's hype backed by real usage? Show me social volume vs. active addresses for the last month."
**Screening:** "Find the top 10 assets by developer activity growth in the last 30 days."
**Divergence detection:** "Show me any assets where social sentiment is high but on-chain activity is declining."

## Pricing

- **Free tier:** Core metrics and signals available with free Santiment account
- **Pro/API tiers:** Higher rate limits, additional metrics, and historical depth available through [SanAPI](https://academy.santiment.net/sanapi/) subscriptions

## Limitations

- **Crypto-only:** No equities, commodities, or traditional finance data
- **Rate limits:** Free tier has call limits; production use requires Pro subscription
- **OAuth dependency:** Requires browser flow for initial authorization (not headless-friendly)
- **Metric coverage:** 500+ assets covered; niche tokens may have limited data

## Verdict

Santiment MCP is the most comprehensive crypto market intelligence MCP we've cataloged. For operators in fintech, crypto payments, or Web3 — this is essential infrastructure. The OAuth setup is clean, the free tier is genuinely useful, and the combined-trends tool provides signal that previously required manual dashboard-hopping.

**Rating: ★★ — Essential for crypto/fintech operators**
