---
title: xRocket Exchange MCP - Spot Market Data and Trading
description: "Community MCP server for xRocket Exchange: hosted endpoint serves 10 public market tools (symbols, tickers, candles, order book, trades, rates, fees) with no key; stdio mode adds account trading bounded by an operator-set daily limit. MIT licensed."
category: Finance
stars: 0
added: 2026-08-25
source: "mcp.so GitHub issue #3735"
relevance: ★★
tags: [mcp-server, crypto, trading, market-data, exchange, finance, order-book]
---

# xRocket Exchange MCP

**Market data and bounded spot trading for AI agents on xRocket Exchange.** An unofficial, open-source MCP server for xRocket Exchange with a clean split: the hosted endpoint exposes public market data with no key, and stdio mode unlocks account access and trading guarded by an operator-set daily limit. Every send is protected by a fail-closed chain-id guard.

```
Server type: Streamable HTTP (hosted public market data) + stdio (local account trading)
Hosted endpoint: https://xrocket-mcp-production.up.railway.app/mcp
Auth: None for hosted market data; account key required for stdio trading
Repo: github.com/nakazanie-ton/myrocket (MIT, Aug 2026)
Tools: 10 verified by live probe (xrocket_market_snapshot, xrocket_market_symbols,
  xrocket_market_tickers, xrocket_market_candles, xrocket_market_orderbook,
  xrocket_market_trades, xrocket_asset_info, xrocket_rates, xrocket_trade_fees,
  xrocket_onboarding_links)
Version: v0.6.0 (live probe confirmed)
```

## Why This Matters for Operators

Agents that trade need two things: reliable market context and hard limits on what they can move. xRocket MCP provides both. The hosted endpoint gives any agent live symbols, tickers, candles, order books, recent trades, rates, and fee schedules without an account, which is enough for watchlists, pricing dashboards, and pre-trade checks. The stdio trading mode adds explicit rails: a daily trade limit set by the operator, chain-id verification before every send, and no margin or leverage, so an agent can execute simple spot trades without being able to drain an account.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `xrocket_market_snapshot` | Aggregated snapshot of current market state across symbols |
| `xrocket_market_symbols` | Lists available spot trading symbols on the exchange |
| `xrocket_market_tickers` | Live ticker data for one or all symbols |
| `xrocket_market_candles` | OHLCV candle history for technical analysis |
| `xrocket_market_orderbook` | Current bid/ask depth for a symbol |
| `xrocket_market_trades` | Recent public trades for a symbol |
| `xrocket_asset_info` | Metadata for supported assets |
| `xrocket_rates` | Current exchange rates |
| `xrocket_trade_fees` | Trading fee schedule |
| `xrocket_onboarding_links` | Links for account onboarding |

## Installation

Hosted market data: connect directly, no install:

```bash
claude mcp add --transport http xrocket https://xrocket-mcp-production.up.railway.app/mcp
```

Local trading: run the server via stdio with your account credentials, which never leave your machine:

```bash
git clone https://github.com/nakazanie-ton/myrocket
cd myrocket && npm install && npm start
```

## Configuration

- **Hosted mode:** no configuration; all 10 market-data tools work anonymously.
- **Stdio trading:** configure your account key locally. Set the daily trade limit in the server config; the fail-closed chain-id guard verifies the network (chain id 4663) before any signed transaction. Trade sizes are capped inside the daily limit you set, and the server is spot-only (no margin).

## Business Relevance

- **Market watch:** agents monitor xRocket prices, depth, and recent trades without an API account.
- **Bounded execution:** small, limit-bounded spot orders through an agent you supervise, with a daily ceiling that cannot be exceeded programmatically.
- **Pre-trade data:** order book and fee data feed pricing decisions before any order is placed.

## Integration with CorpusIQ

Use xRocket market data as a signal source alongside CorpusIQ's finance connectors: pull market context from xRocket, then reconcile fiat-side accounting in QuickBooks or track the overall position with CorpusIQ's Stripe or database connectors. Keep the trading key on the same host as the stdio server; it is never exposed to the hosted endpoint.

## Limitations

- Unofficial community server, not operated by xRocket Exchange; the exchange can change its API at any time.
- Trading is spot-only with a daily limit; no margin, leverage, or advanced order types.
- Hosted endpoint covers public data only; account features require running the stdio server yourself.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Ice Juice Trading MCP - Automated Trading on Your Alpaca Account](/hermes/mcp/servers/external/ice-juice-trading)
- [Stock Market MCP Server](/hermes/mcp/servers/external/stock-market-mcp-server)
