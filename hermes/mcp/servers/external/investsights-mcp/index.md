---
title: "InvestSights — Indian Stock Research MCP (NSE/BSE, 6000+ Stocks)"
description: "Research-grade Indian stock data for AI agents. Fundamentals, forensic accounting scores, DCF valuation, screening, prices & news for 6000+ NSE/BSE stocks."
source: github.com/InvestSights/investsights-indian-stock-research-mcp
stars: 0
language: Python
transport: stdio
auth: None (open data)
category: Finance & Fintech
last_updated: 2026-07-21
---

# InvestSights — Indian Stock Research MCP (6000+ NSE/BSE Stocks)

**Research-grade Indian stock market data MCP server.** Covers 6,000+ NSE/BSE stocks with fundamentals, forensic accounting scores, DCF valuation models, screening, real-time prices, and news. Built for serious equity research through AI agents.

## What It Does for Operators

- **6,000+ stocks** — Full NSE and BSE coverage, from large-caps to micro-caps
- **Forensic accounting** — Red-flag detection: promoter pledging, related-party transactions, auditor red flags, earnings quality scores
- **DCF valuation** — Built-in discounted cash flow models with customizable assumptions
- **Stock screening** — Multi-parameter screening across fundamentals, valuation, and technicals
- **Real-time prices** — Live NSE/BSE price feeds
- **News integration** — Stock-specific news aggregation

## Installation

```bash
git clone https://github.com/InvestSights/investsights-indian-stock-research-mcp.git
cd investsights-indian-stock-research-mcp
pip install -r requirements.txt
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "investsights": {
      "command": "python",
      "args": ["-m", "investsights.server"]
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `get_fundamentals` | Balance sheet, P&L, cash flow for any NSE/BSE stock |
| `forensic_score` | Accounting quality score with red-flag breakdown |
| `dcf_valuation` | Discounted cash flow model with adjustable assumptions |
| `screen_stocks` | Multi-parameter stock screening |
| `get_price` | Real-time or historical price data |
| `get_news` | Stock-specific news and announcements |
| `compare_peers` | Side-by-side comparison of peer companies |

*Note: Tool names are approximate. See github.com/InvestSights for full API.*

## Operator Use Cases

1. **Indian Market Investors** — Run full research workflows on any NSE/BSE stock through AI agent commands
2. **Portfolio Managers** — Screen the entire Indian market for value opportunities using forensic accounting filters
3. **Equity Analysts** — Generate DCF valuations with documented assumptions for client reports
4. **Family Offices** — Monitor Indian holdings with automated red-flag detection

## CorpusIQ Angle

InvestSights is the first India-focused MCP server and fills a major geographic gap in the MCP financial data ecosystem. Operators with India exposure or supply chains can pair InvestSights (Indian market data) with CorpusIQ (operational data from QuickBooks, Stripe) for holistic India business intelligence.

## Limitations

- India-only coverage (NSE/BSE). No US, EU, or other markets.
- Data sources not fully documented — verify accuracy for production use
- Python-only (no Node/TypeScript version)
- New project — active development, API may change
