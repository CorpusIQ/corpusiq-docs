---
title: "Fincept MCP - A Trading Terminal for Your Agent"
description: "A finance terminal for agents: 440 tools and 15 quant engines for markets, options, filings, portfolios, backtests and forecasts."
category: Finance
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all + chatmcp/mcpso issues (October 9, 2026 night sweep)"
relevance: ★★★
tags: [finance, markets, trading, quant, sec-filings, portfolio, options, backtesting, paper-trading, oauth, remote-mcp]
---

# Fincept MCP

**Hosted MCP server that opens Fincept Terminal to your assistant** - quotes, options, global economic series, SEC filings, portfolio analytics, screeners, backtests, statistical models and machine-learning forecasts, all as tools behind one endpoint. 440 platform tools and 15 quant engines, on Fincept's Exclusive Pro plan, with trading tools reaching a paper account only.

```
Server type: Remote (Streamable HTTP at https://enterprise.fincept.in/mcp)
Auth: OAuth 2.1 browser sign-in through fincept.in (no API keys)
Tools: 440 platform tools and 15 quant engines; a short core set is listed and the agent searches the rest by name
Coverage: Quotes, OHLCV candles, option chains, futures curves, fundamentals, funds, symbol search, global economic series, SEC filings and deals
Analysis: Portfolio analytics, screeners, option models, rule and strategy backtests, regression, time-series and hypothesis tests, ML forecasts with conformal intervals, mean-risk optimization over 26 risk measures, Black-Litterman and whole-share allocation
Account: Your portfolios, ledgers and limits, plus the Fincept Paper account
Safety: Trading tools reach the Fincept Paper account only; tools spend credits and respect quotas exactly as the terminal does
Pricing: Exclusive Pro plan (other plans sign in but requests are refused with upgrade_required)
Category: Finance
Built by: Fincept Corporation (Fincept Terminal; docs repo github.com/Fincept-Corporation/fincept-mcp-docs)
```

## Why This Matters for Operators

Finance questions in chat usually stall at the data layer: the assistant knows the concept but not your numbers, the live prices, or the filing. This server closes that gap with the widest surface in the catalog so far - one sign-in and the agent can pull an option chain, read the latest 10-K sections, screen a universe, run a strategy backtest, fit a forecast and check a portfolio's risk, all in the same conversation. Because every call spends terminal credits and answers arrive in one structured envelope with large results paged, the tool behaves like the terminal rather than a chat toy.

## Tools & Capabilities

| Area | What it covers |
|---|---|
| Markets | Quotes, OHLCV candles, option chains, futures curves, fundamentals, funds, symbol search |
| Research | Global economic series, SEC filings, funds and deals, news, sentiment, monitors, maritime, trade and geopolitical data |
| Portfolios | Your portfolios, ledgers and limits; the Fincept Paper account; portfolio analytics |
| Quant engines | Screeners, option models, rule and strategy backtests, regression, time-series models, forecasts and hypothesis tests |
| Machine learning | ML forecasts of one series or a panel with conformal intervals, backtests and model search |
| Risk and allocation | Mean-risk optimization over 26 risk measures, risk parity, hierarchical portfolios; mean-variance and downside-risk portfolios, Black-Litterman, whole-share allocation |
| Statistics | Returns, volatility, rolling statistics, technical indicators, basket backtests, business-day calendars |

Two behaviors keep the surface manageable: a short core tool set is listed for discovery and the agent searches the rest and calls any tool by name, and every tool answers with the same structured envelope, with large results stored and readable page by page.

## Installation

```bash
claude mcp add --transport http fincept https://enterprise.fincept.in/mcp
```

Any MCP client that supports remote servers works the same way: add `https://enterprise.fincept.in/mcp`, sign in with your Fincept account in the browser once, and the connection is ready. There are no API keys to copy or rotate.

## Configuration and Safety

- Sign-in is OAuth 2.1 through fincept.in, so access is granted and revoked at the account level.
- Trading tools reach the Fincept Paper account only - no real money moves through MCP.
- Tools spend credits and respect quotas exactly as the Fincept Terminal does; the same account, the same rules.
- Results arrive in one result format; large outputs are stored and readable page by page.
- Docs: docs.fincept.in. Registry entry: in.fincept/mcp.
- Live probe: POST initialize returns 401 (authentication required).

## Example Prompts

- "Pull the option chain for NVDA for the next three expiries and summarize where the open interest sits."
- "Compare the last four quarters of free cash flow for these five chip companies, with the figures as filed."
- "Backtest a simple momentum rule on this basket over the last three years and show the drawdowns."
- "Forecast this revenue series next quarter with a conformal interval and list what the model searched."
- "Optimize this portfolio for risk parity and show the weights before and after."

## Integration with CorpusIQ

Fincept answers what the markets did and what the models say; CorpusIQ keeps the business numbers straight behind them. Ask Fincept for prices, filings and quant work, then ask CorpusIQ for revenue, customers, pipeline and spend from Stripe, Shopify, HubSpot, QuickBooks or your ad accounts in the same conversation - market context and business reality, one chat, no exports.

## Limitations

- Requires a Fincept account on the Exclusive Pro plan; other plans can sign in but every request is refused with `upgrade_required`.
- Tool counts and engine counts are vendor-stated (Fincept's documentation and submission, October 2026).
- Trading is paper-only by design; there is no path to live order placement through this server.
- Credits and quotas are shared with the terminal, so heavy agent use competes with terminal use on the same account.
- The GitHub repository is documentation, not source; the MCP server itself is proprietary and hosted.

## FAQ

### Can the agent place real trades?

No. Trading tools reach the Fincept Paper account only, by design.

### What do I need to connect?

A Fincept account with the Exclusive Pro plan, then a browser sign-in the first time a client connects - no API key.

### How does the agent find 440 tools without flooding the context?

A short core set is listed; the agent searches the catalog for the rest and calls any tool by name, and results share one envelope that pages large outputs.

## See Also

- [Silicon Floor MCP - AI and Chip Stock Research](/hermes/mcp/servers/external/silicon-floor-mcp/)
- [Market Eyes Live MCP - Stock Ratings and Mortgage Rates](/hermes/mcp/servers/external/market-eyes-mcp/)
- [ETFIQ MCP - US ETF Data](/hermes/mcp/servers/external/etfiq-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
