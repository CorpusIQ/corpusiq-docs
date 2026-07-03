---
title: "Co-Invest MCP — AI-Powered Investment Management"
description: "Connect Co-Invest to Hermes Agent. Research, analyze, and manage investments directly from AI assistants. Invest with Claude and other AI agents."
category: mcp
tags: [mcp-server, co-invest, finance, investing, trading, portfolio-management, ai-agent]
last_updated: 2026-07-03
---

# Co-Invest MCP Server ★ New (July 3)

## Overview

Co-Invest MCP (`co-invest-mcp`) enables AI agents to participate in investment research and management workflows. Built on Liquid Trade's investment infrastructure, this MCP server lets agents analyze markets, research assets, and execute investment strategies — all within the agent conversation. Official MCP from Liquid Trade.

**Key advantage**: Investment management becomes conversational. Instead of switching between Bloomberg, brokerage apps, and spreadsheets, operators can research and manage investments directly through their AI agent.

## Key Features

- **Market research**: Query real-time and historical market data across asset classes
- **Portfolio analysis**: Review holdings, performance metrics, and risk exposure
- **Trade execution**: Place and manage investment orders (with confirmation gates)
- **Strategy backtesting**: Test investment strategies against historical data
- **Alert monitoring**: Set and monitor price alerts, news triggers, and portfolio thresholds
- **Web-based platform**: Accessible at [liquid.trade/coinvest](https://www.liquid.trade/coinvest)

## Installation

```bash
# Add to Hermes (remote endpoint)
hermes mcp add coinvest --url https://api.liquid.trade/coinvest/mcp

# Authenticate
hermes mcp auth coinvest
```

## Manual Configuration

```json
{
  "mcpServers": {
    "coinvest": {
      "type": "sse",
      "url": "https://api.liquid.trade/coinvest/mcp",
      "headers": {
        "Authorization": "Bearer ${LIQUID_TRADE_API_KEY}"
      }
    }
  }
}
```

## Prerequisites

1. **Liquid Trade Account**: Sign up at [liquid.trade/coinvest](https://www.liquid.trade/coinvest)
2. **API Key**: Generate from account settings
3. **Linked Brokerage** (optional): Connect brokerage for trade execution

## Business Use Cases

1. **Research Assistant**: "Compare the PE ratios and revenue growth of these 5 SaaS companies" — agent pulls live data
2. **Portfolio Review**: "Show me my portfolio allocation and flag any positions over 20% concentration"
3. **Alert Monitoring**: Agent monitors positions and alerts you when a stock hits your target price
4. **Due Diligence**: "Research this company — management team, financials, competitive position, SEC filings"
5. **Strategy Execution**: Define investment rules and let the agent monitor for opportunities matching your criteria

## Business Relevance

Investment management has been fragmented across terminals, apps, and spreadsheets. Co-Invest MCP brings it into the AI agent workflow — operators managing personal or firm investments can research, monitor, and execute without context-switching. The "invest with Claude" paradigm signals where agentic finance is heading.

## Limitations

- Trade execution requires confirmation gates (by design — safety feature)
- Market data coverage varies by asset class and exchange
- Investment advice is AI-generated — not a substitute for professional financial advice
- US-focused initially with international expansion planned
- Beta product — API and tool surface may change

## See Also

- Alpha Vantage MCP — for financial market data
- SentiSense MCP — for market sentiment intelligence
- HPSILab Quant Finance MCP — for quantitative analysis and options
- Kalshi MCP — for prediction markets and event contracts
