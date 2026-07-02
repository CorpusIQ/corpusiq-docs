---
title: "Kalshi MCP — Prediction Markets for AI Agents"
description: "Connect Kalshi prediction markets to Hermes Agent. Get markets, positions, and place orders from any AI agent. First MCP for CFTC-regulated prediction markets."
category: mcp
tags: [mcp-server, kalshi, prediction-markets, finance, trading, event-contracts]
last_updated: 2026-07-02
---

# Kalshi MCP — Prediction Markets Server

## What It Is

Kalshi is the first CFTC-regulated prediction market in the US. This MCP server gives AI agents programmatic access to Kalshi markets — enabling programmatic event-driven analysis and trading.

**GitHub**: https://github.com/onofre-jauregui/kalshi-mcp (TypeScript, new)

## Tools Available

| Tool | Description |
|------|-------------|
| `get_markets` | List available prediction markets with prices and volume |
| `get_positions` | Check current positions across all markets |
| `place_order` | Place buy/sell orders on event contracts |
| `get_market_history` | Historical pricing and settlement data |

## Quick Start

```bash
# Clone and install
git clone https://github.com/onofre-jauregui/kalshi-mcp.git
cd kalshi-mcp
npm install

# Configure environment
export KALSHI_API_KEY="your-kalshi-api-key"
export KALSHI_PRIVATE_KEY="your-private-key-path"

# Add to Hermes
hermes mcp add kalshi --command "node" --args "dist/index.js" --workdir "$(pwd)" \
  --env KALSHI_API_KEY KALSHI_PRIVATE_KEY
```

## Manual Configuration

```json
{
  "mcpServers": {
    "kalshi": {
      "command": "node",
      "args": ["dist/index.js"],
      "env": {
        "KALSHI_API_KEY": "your-kalshi-api-key",
        "KALSHI_PRIVATE_KEY": "/path/to/private-key.pem"
      }
    }
  }
}
```

## Prerequisites

1. **Kalshi Account**: Sign up at [kalshi.com](https://kalshi.com)
2. **API Key**: Generate from Kalshi developer dashboard
3. **RSA Private Key**: Required for authenticated API calls (Kalshi uses RSA-based auth)

## Business Use Cases

1. **Event-Driven Analysis**: Have AI agents monitor prediction market probabilities for real-time event forecasting
2. **Market Scanning**: Scan all active markets for mispriced event contracts
3. **Portfolio Monitoring**: Track event-contract portfolio performance and risk exposure
4. **Programmatic Hedging**: Use prediction markets to hedge against defined-event risks

## Limitations

- US-only (Kalshi is CFTC-regulated for US residents)
- Kalshi API requires RSA key-pair authentication (more complex than Bearer tokens)
- New server — limited tool coverage, expect rapid iteration
- Prediction markets are not available in all US states

## See Also

- SentiSense MCP — for market sentiment intelligence
- HPSILab Quant Finance MCP — for options analytics and Monte Carlo
- pipeworx-io/mcp-tradier — for traditional stock/options market data
