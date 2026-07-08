---
title: "SentiSense MCP — Market Intelligence for AI Agents"
description: "Connect SentiSense market intelligence to Hermes Agent. US market mood, stock sentiment, analyst ratings, 13F filings. Five read-only tools, zero-config OAuth, no API key."
category: mcp
tags: [mcp-server, sentisense, finance, market-intelligence, sentiment, stocks, investing]
last_updated: 2026-07-08
---

# SentiSense — Market Intelligence MCP Server

## What It Is

SentiSense brings institutional-grade market intelligence into AI agents. Ask your agent about US market mood, a stock's sentiment and SentiSense Score, market-moving news, analyst ratings, and who's buying or selling (13F filings).

**Key advantage**: Zero-config OAuth. No API key to manage. Five read-only tools.

## Tools Available

| Tool | Description |
|------|-------------|
| `get_market_mood` | Overall US market sentiment and mood indicators |
| `get_stock_sentiment` | SentiSense Score + sentiment analysis for any ticker |
| `get_market_news` | Market-moving news with sentiment overlay |
| `get_analyst_ratings` | Consensus analyst ratings and price targets |
| `get_institutional_activity` | 13F filing data — who's buying and selling |

## Quick Start

```bash
# Add to Hermes
hermes mcp add sentisense --url https://api.sentisense.ai/mcp

# Authenticate (OAuth — no API key needed)
hermes mcp auth sentisense
# → Opens browser: Log in with Google/GitHub
# → Done. 5 tools available.
```

## Manual Configuration

```json
{
  "mcpServers": {
    "sentisense": {
      "url": "https://api.sentisense.ai/mcp",
      "transport": "sse"
    }
  }
}
```

## Business Use Cases

1. **Investment Research**: Query analyst consensus, institutional flows, and sentiment before making investment decisions
2. **Market Monitoring**: Have your agent monitor market mood shifts and alert on sentiment regime changes
3. **Portfolio Sentiment**: Aggregate sentiment scores across holdings for portfolio-level risk assessment
4. **Earnings Prep**: Pull analyst ratings and institutional activity ahead of earnings calls

## Limitations

- US markets only (no international coverage)
- Read-only — no trading execution
- Sentiment data has inherent lag (daily updates, not real-time)

## See Also

- HPSILab Quant Finance MCP — for options analytics and Monte Carlo simulations
- pipeworx-io/mcp-tradier — for real-time stock & options market data
- Kalshi MCP — for prediction market analysis
