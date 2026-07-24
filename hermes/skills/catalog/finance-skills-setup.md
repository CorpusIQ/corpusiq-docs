---
title: Finance Skills — Financial Analysis for Hermes Agents
description: Collection of financial analysis skills (yfinance, stock correlation, options, generative UI) with 8.6K+ combined installs. Enables Hermes agents to fetch market data, analyze stocks, and generate financial visualizations for business operators.
---

# Finance Skills — Setup Guide

**Source:** [himself65/finance-skills](https://skills.sh/himself65/finance-skills) (8.6K+ combined installs)
**Category:** Growth Operations / Business Intelligence
**Quality Tier:** 🟡 Beta

A collection of Python-based financial analysis skills that give Hermes agents the ability to fetch real-time market data, analyze stock correlations, evaluate options strategies, and generate financial UI components. Built on yfinance (Yahoo Finance) with 3,064 GitHub stars. Ideal for CorpusIQ agents serving business operators who need market intelligence.

---

## Installation

```bash
npx skills add himself65/finance-skills --skill yfinance-data
npx skills add himself65/finance-skills --skill stock-correlation
npx skills add himself65/finance-skills --skill options-payoff
npx skills add himself65/finance-skills --skill generative-ui
npx skills add himself65/finance-skills --skill hormuz-strait
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **yfinance-data** | 2.0K | Fetch stock prices, financials, options, dividends, analyst ratings |
| **stock-correlation** | 1.7K | Analyze correlations between multiple stocks |
| **options-payoff** | 1.7K | Model options payoff diagrams and strategies |
| **generative-ui** | 1.6K | Generate financial charts, dashboards, and UI components |
| **hormuz-strait** | 1.6K | Geopolitical risk analysis for market impact assessment |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3.9+** | Required for yfinance library |
| **yfinance** | Auto-installed by skills — `pip install yfinance` |
| **Internet** | yfinance fetches live data from Yahoo Finance |
| **Disclaimer** | Data is for research/educational purposes. Not financial advice. |

---

## Key Capabilities

### yfinance-data — Market Data Fetching
```python
import yfinance as yf

# Current stock price
ticker = yf.Ticker("AAPL")
print(ticker.info['currentPrice'])

# Historical data
hist = ticker.history(period="1mo")

# Financial statements
balance_sheet = ticker.balance_sheet
income_stmt = ticker.income_stmt

# Options chain
options = ticker.option_chain('2026-08-21')

# Multiple tickers
data = yf.download(["AAPL", "MSFT", "GOOGL"], period="6mo")
```
Covers 19 data categories: stock prices, history, financials, options, dividends, earnings, analyst targets, institutional holders, insider transactions, and more.

### stock-correlation — Portfolio Analysis
Analyze correlation matrices between tickers to understand diversification, sector exposure, and risk concentration. Useful for business operators evaluating market positions.

### options-payoff — Strategy Modeling
Model long calls, puts, covered calls, spreads, and iron condors with payoff diagrams. Decision-support for options-aware operators.

### generative-ui — Financial Visualization
Generate charts, dashboards, and interactive UI components from financial data. Output formats include matplotlib charts, HTML dashboards, and data tables.

### hormuz-strait — Geopolitical Risk
Analyze market impact of geopolitical events, supply chain disruptions, and macro shocks. Applies scenario analysis to portfolios.

---

## Quick Start for Hermes Agents

```bash
# 1. Ensure yfinance is installed
python3 -c "import yfinance; print('yfinance', yfinance.__version__)"

# 2. Fetch a stock quote
python3 -c "
import yfinance as yf
aapl = yf.Ticker('AAPL')
print(f\"AAPL: \${aapl.info.get('currentPrice', 'N/A')}\")
print(f\"Market Cap: \${aapl.info.get('marketCap', 0)/1e9:.1f}B\")
"

# 3. Get S&P 500 sector overview
python3 -c "
import yfinance as yf
spy = yf.Ticker('SPY')
info = spy.info
print(f\"S&P 500 (SPY): \${info.get('currentPrice', 'N/A')}\")
print(f\"50-Day Avg: \${info.get('fiftyDayAverage', 'N/A')}\")
"
```

---

## Verification

```bash
# Verify yfinance is functional
python3 -c "import yfinance as yf; msft = yf.Ticker('MSFT'); print('✓ MSFT:', msft.info.get('shortName', '?'))"

# Verify installed skills
npx skills list 2>&1 | grep himself65

# Test skill usage
npx skills use himself65/finance-skills@yfinance-data 2>&1 | head -5
```

---

## Notes

- **Not financial advice**: All data is for research and educational purposes. Never auto-trade or place orders.
- **Rate limiting**: Yahoo Finance may rate-limit frequent requests. Use `yf.download()` for bulk queries instead of individual `Ticker` calls.
- **Data accuracy**: yfinance is not affiliated with Yahoo, Inc. Data may have delays or discrepancies vs. official sources.
- **Hermes integration**: Combine with `timesfm-forecasting` for time-series predictions, or with the `corpusiq-research-intelligence-framework` for competitive market analysis.
- **Business operator use case**: CorpusIQ agents can use these skills to provide market context, competitor stock performance, and industry trend analysis to business operators.
