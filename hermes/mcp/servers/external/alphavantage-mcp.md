---
title: "Alpha Vantage MCP — Financial Market Data for AI Agents"
description: "Connect Alpha Vantage to Hermes Agent. Access real-time and historical stock, ETF, forex, crypto, and commodities data. Technical indicators, fundamentals, and economic data — all via MCP."
category: mcp
tags: [mcp-server, alpha-vantage, finance, market-data, stocks, forex, crypto, technical-analysis]
last_updated: 2026-07-03
---

# Alpha Vantage MCP Server ★ New (July 3)

## Overview

Alpha Vantage MCP (`alphavantage/alpha_vantage_mcp`) wraps the industry-standard Alpha Vantage financial data API into an MCP server. AI agents get direct access to 20+ years of historical market data, real-time quotes, technical indicators, and fundamental data across stocks, ETFs, forex, crypto, and commodities.

**Key advantage**: Alpha Vantage is the most widely used free financial data API (used by 500K+ developers). The MCP server makes this data instantly available to AI agents — no API integration code required.

## Key Features

- **Real-time quotes**: Current prices for stocks, ETFs, forex pairs, and cryptocurrencies
- **Historical data**: 20+ years of daily, weekly, and monthly OHLCV data
- **Technical indicators**: 50+ indicators including SMA, EMA, RSI, MACD, Bollinger Bands, Fibonacci
- **Fundamental data**: Income statements, balance sheets, cash flow, earnings, and company overviews
- **Forex & Crypto**: Real-time and historical FX rates, 500+ crypto pairs
- **Commodities**: Gold, silver, oil, natural gas, copper, and agricultural commodities
- **Economic indicators**: GDP, inflation, unemployment, interest rates, and treasury yields
- **Hosted endpoint**: Remote MCP at `mcp.alphavantage.co`

## Installation

```bash
# Add to Hermes (remote endpoint)
hermes mcp add alphavantage --url https://mcp.alphavantage.co/mcp

# Set API key
export ALPHA_VANTAGE_API_KEY="your-free-api-key"
hermes mcp config alphavantage --env ALPHA_VANTAGE_API_KEY
```

## Manual Configuration

```json
{
  "mcpServers": {
    "alphavantage": {
      "type": "sse",
      "url": "https://mcp.alphavantage.co/mcp",
      "headers": {
        "x-api-key": "${ALPHA_VANTAGE_API_KEY}"
      }
    }
  }
}
```

## Prerequisites

1. **Free API Key**: Get at [alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key) (free tier: 25 requests/day)
2. **Premium Key** (optional): For higher rate limits and intraday data

## Business Use Cases

1. **Market Monitoring**: AI agent tracks your watchlist and alerts on significant price movements, volume spikes, or technical signals
2. **Financial Analysis**: "Compare Apple and Microsoft's revenue growth over the last 5 years" — agent pulls fundamental data
3. **Technical Screening**: "Find S&P 500 stocks with RSI below 30 and above-average volume" — agent runs multi-condition scans
4. **Portfolio Reporting**: Generate weekly portfolio performance reports with charts, indicators, and fundamental summaries
5. **Forex & Crypto Trading**: Monitor FX rates and crypto pairs with real-time technical indicators

## Business Relevance

Alpha Vantage MCP democratizes financial data for AI agents. Where previously operators needed to write API integration code, configure data pipelines, and manage API keys, they can now simply ask their agent for financial data. The free tier makes this accessible to every operator, not just institutional investors. Combined with Co-Invest MCP and SentiSense MCP, operators now have a complete AI-driven investment research stack.

## Limitations

- Free tier: 25 API requests/day (premium: 75/min for $49.99/month)
- Real-time data has 15-minute delay on free tier (US equities)
- No options data (use HPSILab Quant MCP for options)
- US-centric equity coverage; international coverage varies
- Not suitable for high-frequency trading (rate limits)

## See Also

- Co-Invest MCP — for investment management and trade execution
- SentiSense MCP — for market sentiment and news analysis
- HPSILab Quant Finance MCP — for options analytics and Monte Carlo simulations
- Kalshi MCP — for prediction markets and event contracts
