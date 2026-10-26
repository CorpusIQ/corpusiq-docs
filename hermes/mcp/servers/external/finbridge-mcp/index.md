---
title: FinBridge MCP - Korean and US Market Data for Agents
description: Korean and US stock data for AI agents - DART filings, KRX prices, SEC EDGAR, FRED and 13F, strategy screeners and portfolio backtests over one Streamable HTTP endpoint.
category: Finance
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★★
tags: [stocks, korea, sec-edgar, screeners, backtesting, fred, remote-mcp]
last_updated: "2026-10-19"
---

# FinBridge MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** - Korean and US stock market data in one normalized schema, built by Jake Cho at GRONOX. Thirty-three tools cover DART filings and fundamentals, KRX adjusted prices and indicators, SEC EDGAR, FRED and 13F, server-side strategy screeners and fixed-weight portfolio backtests. The Korean coverage is the differentiator: every KR listing (2,800+ companies, 1,300+ ETFs) that most US providers skip or paywall.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in or bearer API key
Endpoint: https://mcp.gronox.kr/mcp
Tools: 33 (Korean fundamentals, US fundamentals, prices, screeners, backtests, macro, crypto)
Pricing: Free tier 100 calls/day, no card; paid from $10/mo with 7-day trial
Category: Finance
Built by: Jake Cho (GRONOX), github.com/Jakechj/finbridge-mcp
```

## Why This Matters for Operators

Cross-border market research breaks down exactly where the data formats change: Korean disclosures live in DART, US ones in EDGAR, macro series in FRED, and no single provider normalizes them. Analysts stitch these together by hand, in spreadsheets, with different schemas per source.

FinBridge puts both markets behind one endpoint with one schema, and pushes the heavy computation server-side. **Screeners like the Minervini trend template, CAN SLIM and VCP run over the whole market inside the server, so an agent asks for a ranked list instead of pulling raw data and filtering it itself.** Questions can be asked in English or Korean, with Korean company names resolving the same way US tickers do.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Korean fundamentals (OpenDART) | Filings, normalized financial statements, insider trades, major corporate events |
| US fundamentals (SEC EDGAR) | Filings, financials, Form 4 insider trades, 13F institutional holdings |
| Prices and technicals | Daily adjusted prices for every KR and US listing, indicators, valuation |
| Strategy screeners | Minervini trend template, CAN SLIM, VCP and more, run server-side |
| Backtests | Fixed-weight portfolio backtests on the FinBridge database |
| Macro and crypto | FRED series, USD/KRW, crypto tickers via ccxt |

## Installation

```bash
claude mcp add finbridge --transport http https://mcp.gronox.kr/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "finbridge": {
      "type": "http",
      "url": "https://mcp.gronox.kr/mcp"
    }
  }
}
```

OAuth sign-in covers claude.ai custom connectors; a bearer API key covers server clients. The free tier needs no card and resets at 100 calls per day.

## Business Relevance

- **Analysts covering Korean equities** get DART and KRX data most US terminals skip, in English or Korean
- **US-focused researchers** consolidate EDGAR, FRED and 13F reads in the same session as Korean comparisons
- **Fund operators** run pre-built strategy screeners and portfolio backtests without standing up their own data pipeline
- **Fintech builders** get one normalized schema instead of four data contracts

## Integration with CorpusIQ

FinBridge is the market-data complement to CorpusIQ's company-operating-data connectors. An agent researching a Korean or US company can pull its filings and insider activity through FinBridge while CorpusIQ supplies the operating picture - QuickBooks financials, Stripe revenue, Google Ads spend - for the companies the operator actually runs or tracks. For an investor operator, the composed workflow is natural: FinBridge screens the market, CorpusIQ reads the portfolio companies' business data, and the agent produces a diligence note that joins both.

## Limitations

- Brand new listing with no track record yet
- Free tier is rate-limited to 100 calls per day
- Retail-investing grade data; not a terminal replacement for institutional depth
- Paid plans gate depth of history rather than just call volume
