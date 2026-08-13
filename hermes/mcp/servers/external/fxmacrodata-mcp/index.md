---
title: "FXMacroData MCP — Integration Guide"
description: "Macroeconomic and FX data MCP server — 18 currencies, central bank announcements, COT data, commodities, and forex. AI agents get real-time economic"
category: "Finance & Data"
stars: "★★"
source: mcpservers.org
github: https://github.com/fxmacrodata/fxmacrodata
date_added: 2026-07-28
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/fxmacrodata-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# FXMacroData MCP

MCP server providing AI agents with real-time macroeconomic and foreign exchange intelligence — central bank announcements, Commitment of Traders (COT) data, economic calendars, commodity prices, and forex rates across 18 currencies.

## What It Does

- **FX Rates:** Real-time and historical exchange rates for 18 major currencies
- **Central Bank Calendar:** Upcoming policy meetings, interest rate decisions, and minutes
- **COT Data:** Weekly Commitment of Traders reports — positioning data from futures markets
- **Economic Calendar:** GDP, CPI, employment, PMI, and other macro releases with forecasts
- **Commodities:** Gold, oil, copper, and agricultural commodity prices
- **Cross-Rate Analysis:** Calculate implied rates and arbitrage opportunities

## Why It Matters for Operators

Before FXMacroData MCP, an operator managing international payments, import/export pricing, or currency exposure would need:
1. A Bloomberg Terminal ($2,000+/month) or
2. Multiple separate data sources (TradingView for rates, ForexFactory for calendar, CFTC for COT, investing.com for commodities)

Now: AI agent queries everything conversationally:
```
Agent: "What's the EUR/USD outlook given the ECB meeting next week and current COT positioning?"
→ FXMacroData returns rate + ECB calendar + COT data → AI synthesizes answer
```

For operators running e-commerce, SaaS with international pricing, or any business with FX exposure, this turns your AI agent into a treasury analyst.

## Setup

### Prerequisites
- FXMacroData account ([fxmacrodata.com](https://fxmacrodata.com))
- API key (free tier available)
- Python ≥ 3.10

### Install
```bash
pip install fxmacrodata-mcp
```

### Claude Desktop
```json
{
  "mcpServers": {
    "fxmacrodata": {
      "command": "python",
      "args": ["-m", "fxmacrodata_mcp"],
      "env": {
        "FXMACRODATA_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Cursor / VS Code
```json
{
  "mcpServers": {
    "fxmacrodata": {
      "command": "python",
      "args": ["-m", "fxmacrodata_mcp"],
      "env": {
        "FXMACRODATA_API_KEY": "${FXMACRODATA_API_KEY}"
      }
    }
  }
}
```

### Hermes Agent
```yaml
mcp_servers:
  fxmacrodata:
    command: python
    args: ["-m", "fxmacrodata_mcp"]
    env:
      FXMACRODATA_API_KEY: "${FXMACRODATA_API_KEY}"
```

## Tools

| Tool | Description |
|------|-------------|
| `get_fx_rate` | Get current or historical exchange rate for any currency pair |
| `get_central_bank_calendar` | Upcoming central bank meetings with expected rate decisions |
| `get_cot_report` | Weekly COT data — speculative vs commercial positioning |
| `get_economic_calendar` | Economic releases with actual, forecast, and previous values |
| `get_commodity_price` | Real-time commodity prices (gold, oil, copper, wheat, etc.) |
| `get_currency_profile` | Overview of a currency's fundamentals, central bank, and key drivers |
| `calculate_cross_rate` | Calculate implied cross rates and identify arbitrage |
| `get_interest_rates` | Current benchmark rates for all 18 currencies |
| `get_inflation_data` | CPI and PPI data with YoY/MoM changes |

## Currencies Covered

USD, EUR, GBP, JPY, CHF, AUD, CAD, NZD, SEK, NOK, DKK, SGD, HKD, KRW, MXN, BRL, ZAR, TRY

## Pricing

| Tier | Price | Includes |
|------|-------|----------|
| Free | $0/month | 100 API calls/day, current rates only, basic calendar |
| Pro | $29/month | 10,000 calls/month, historical data (5 years), COT reports |
| Business | $99/month | 50,000 calls/month, full historical (20 years), real-time streaming |
| Enterprise | Custom | Unlimited, dedicated endpoint, SLA |

## Use Cases

### International Pricing Strategy
```
Agent: "EUR/USD dropped 2% this month. How does that affect our European pricing if we want to maintain USD margins?"
→ get_fx_rate(EUR/USD, 30d history) → calculate margin impact → recommend price adjustment
```

### Treasury & Cash Management
```
Agent: "We hold GBP and EUR balances. Given next week's Bank of England and ECB meetings, should we convert to USD now or wait?"
→ get_central_bank_calendar(BoE, ECB) → get_cot_report(GBP, EUR) → analyze positioning → recommend
```

### Import/Export Cost Forecasting
```
Agent: "Our copper component costs are tied to LME prices. What's the 6-month outlook based on COT data and China PMI?"
→ get_commodity_price(copper) → get_cot_report(copper) → get_economic_calendar(China PMI) → forecast
```

### SaaS Multi-Currency Billing
```
Agent: "We bill in 8 currencies. Which ones have moved >1% this week and should we adjust pricing?"
→ get_fx_rate(all_pairs) → calculate_weekly_change → flag pairs >1% → recommend adjustments
```

### Travel & Expense Management
```
Agent: "Our team is traveling to Tokyo next month. Lock in JPY now or wait?"
→ get_fx_rate(USD/JPY) → get_central_bank_calendar(BoJ) → get_cot_report(JPY) → analyze trend → recommend
```

## Data Sources

FXMacroData aggregates from official sources:
- **FX Rates:** European Central Bank (ECB) reference rates + market feeds
- **COT Data:** Commodity Futures Trading Commission (CFTC) — weekly, released Fridays
- **Economic Calendar:** National statistics offices + consensus forecasts
- **Central Bank Calendar:** Official announcements from each central bank
- **Commodities:** LME, CME, ICE exchange data

All data is timestamped and source-cited in API responses.

## Limitations

- **Not real-time tick data:** FX rates have ~1-5 minute delay on Free/Pro tiers. Business tier offers real-time streaming.
- **COT data is weekly:** CFTC releases COT every Friday for the preceding Tuesday. Not suitable for intraday positioning analysis.
- **18 currencies:** Covers all major and most EM currencies but not every currency pair. Exotic pairs require Enterprise.
- **No trade execution:** This is a data server only. For trading, pair with Capital.com MCP or similar execution platforms.

## See Also

- [[capital-com-mcp]] — CFD trading execution (complementary)
- [[coinvest-mcp]] — AI-driven portfolio management
- [[mercury-mcp]] — Business banking (treasury operations)
