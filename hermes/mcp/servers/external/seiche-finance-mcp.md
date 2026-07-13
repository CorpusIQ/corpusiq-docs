---
title: "Seiche Finance MCP — US Money Market Stress Testing"
description: "Free open source funding stress terminal for US money markets. 22 engines, honest backtests, zero data cost using Fed/NY Fed/OFR/Treasury public APIs."
category: mcp
tags: [mcp-server, finance, money-markets, stress-testing, fed, treasury]
last_updated: 2026-07-12
---

# Seiche Finance MCP Server ★ New (July 12)

Free open source funding stress terminal for US money markets — 22 stress-testing engines, honest backtests, zero data cost. Pulls from Federal Reserve, NY Fed, OFR, and Treasury public APIs. Licensed under AGPL-3.0.

**Source:** mcp.so (submitted July 12, 2026) · **GitHub:** beepboop2025 (exact repo TBD)

## What It Is

Seiche is a specialized financial MCP server that models US money market stress scenarios. Using 22 distinct simulation engines, it backtests funding strategies against historical stress events and generates risk metrics. All data comes from free public APIs — no Bloomberg or Reuters terminal needed.

## Business Relevance

- **Treasury/finance operators** can stress-test funding positions from an AI agent
- **Risk managers** can run scenario analysis without expensive terminal subscriptions
- **Financial analysts** can backtest funding strategies across 22 engine variants
- **CorpusIQ complement** for fintech and banking operators monitoring treasury positions

## Tools Available

| Tool | Description |
|------|-------------|
| `run_stress_test` | Execute stress scenario across selected engines |
| `backtest_strategy` | Historical backtest of funding strategy |
| `get_market_data` | Current rates from Fed/NY Fed/OFR/Treasury |
| `list_engines` | Available simulation engines and their parameters |
| `compare_scenarios` | Side-by-side comparison of multiple stress runs |

## Quick Start

```bash
# Clone and run locally (AGPL-3.0)
git clone https://github.com/beepboop2025/seiche
cd seiche && pip install -e .

# Add to MCP client config
{
  "mcpServers": {
    "seiche": {
      "command": "python",
      "args": ["-m", "seiche.mcp_server"]
    }
  }
}
```

## Business Use Cases

1. **Daily liquidity check:** "Run a baseline stress test on our funding position and flag any engines showing risk"
2. **Scenario comparison:** "Compare the 2008, 2020, and 2023 stress scenarios on our current portfolio"
3. **Rate impact analysis:** "If the Fed raises rates 50bp, which of our funding sources is most vulnerable?"
4. **Regulatory prep:** "Generate a stress test report suitable for our next board meeting"

## Limitations

- US money markets only (no international/EM markets)
- AGPL-3.0 license (copyleft — review implications for commercial use)
- Requires Python environment with numpy/pandas dependencies
- New project — engine accuracy should be validated against established models
- Self-hosted (no cloud API); runs locally

## See Also

- [Financial News MCP](/hermes/mcp/servers/external/financial-news-mcp/) — Real-time financial news and sentiment
- [AlphaVantage MCP](/hermes/mcp/servers/external/alphavantage-mcp/) — Stock fundamentals and technical data
- [Kalshi MCP](/hermes/mcp/servers/external/kalshi-mcp/) — Prediction market data
