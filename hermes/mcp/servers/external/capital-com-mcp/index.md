---
title: "Capital.com MCP — CFD Trading for AI Agents"
description: "Official MCP server for Capital.com — CFD trading across forex, indices, commodities, shares, and crypto. 4 GitHub stars, verified."
category: mcp
tags: [mcp-server, trading, finance, cfd, capital-com]
source: mcp.so
discovered: 2026-07-22
stars: 4
author: capital-com-sv
github: https://github.com/capital-com-sv
---

# Capital.com MCP

**Official MCP server** for Capital.com, a regulated CFD broker. Gives AI agents access to trading data, market analysis, and trade execution across forex, indices, commodities, shares, and crypto.

> ⚠️ **Risk Warning:** CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage. 81.31% of retail investor accounts lose money when trading CFDs with this provider. Ensure your agent workflows include position sizing and risk management guardrails.

## Why It Matters for Operators

For operators managing investment portfolios or running trading operations, Capital.com MCP brings professional trading capabilities directly into AI agent workflows:

- **Market Analysis:** AI agents can pull real-time quotes, charts, and market data
- **Trade Execution:** Programmatic trade placement with position management
- **Portfolio Monitoring:** Track open positions, P&L, and exposure
- **Risk Management:** Set stop-losses and take-profits through agent logic

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (remote) |
| **Auth** | OAuth / API Key (Capital.com account required) |
| **Category** | Finance & Commerce |
| **Source** | [mcp.so/servers/capital-com-mcp](https://mcp.so/servers/capital-com-mcp) |
| **Author** | capital-com-sv |
| **Stars** | ⭐ 4 |
| **Verified** | ✅ |

## Setup

### Claude Desktop
```json
{
  "mcpServers": {
    "capital-com": {
      "type": "streamable-http",
      "url": "https://api.capital.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_CAPITAL_API_KEY"
      }
    }
  }
}
```

## CorpusIQ Integration

Capital.com MCP adds trading capabilities alongside CorpusIQ's financial connectors:

1. **Trading + Accounting:** Trade on Capital.com → record in QuickBooks via CorpusIQ
2. **Portfolio + Business Metrics:** Combine trading P&L with business revenue in unified dashboards
3. **Risk Monitoring:** Cross-reference Capital.com exposure with business cash positions

## Limitations

- CFDs are high-risk — not suitable for all operators
- Requires Capital.com account and compliance with their terms
- 81.31% of retail accounts lose money — ensure agent guardrails
- Only 4 stars — relatively new listing

## See Also

- [[index]] — Full external MCP catalog
- [[sugra-api-mcp]] — Comprehensive business data MCP
- [[fintel-mcp]] — Financial data MCP
- [[alphavantage-mcp]] — Stock market data MCP
