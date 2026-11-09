---
title: "TradingData MCP - 48-Tool Market Data for Agents"
description: "48 market-data tools over one hosted MCP URL: quotes, options greeks, SEC filings and macro series, keyless discovery with an OAuth tier"
category: Finance
stars: "n/a (hosted; keyless discovery and tool listing, OAuth or API key for calls)"
added: 2026-11-09
source: "mcp.so feed card published 2026-11-09T17:44:15Z (slug tradingdata); the endpoint at mcp.tradingdata.io, where a keyless initialize answered 200 with 48 tools listed; and both OAuth protected-resource documents"
relevance: ★★★
tags: [finance, market-data, stocks, options, etf, crypto, macro, sec-filings, remote-mcp]
last_updated: "2026-11-09"
---

# TradingData MCP

**The question that breaks an agent is the follow-up. "What is Apple trading at" is easy. "Is Apple expensive against its own five-year range, what do the options imply, and what did the last 10-Q actually say" is three vendors, three vocabularies and three timestamp conventions. TradingData puts 48 tools on one hosted endpoint and returns a timestamp and a delay with every quote.**

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.tradingdata.io
Protocol:    2025-06-18
Server:      tradingdata 0.1.0
Auth:        OAuth (scope market:read) or API key for tools/call;
             initialize and tools/list answer without one
Tools:       48
Listing:     mcp.so, Finance & Commerce, verified and featured
Docs:        tradingdata.io/docs
```

## What the endpoint says about itself

The discovery half is open, which is why this guide can state the surface rather than quote a brochure. A keyless `initialize` returned `200` with the server name `tradingdata` at version `0.1.0` and declared the `tools`, `prompts` and `resources` capabilities, with `listChanged` set on tools. `tools/list` returned **48 tools**, all 48 of them listed below.

The call half is closed and says so in the protocol's own voice:

```text
tools/call get_quotes {"symbols":["AAPL","SPY"]}  ->  200
{"jsonrpc":"2.0","id":null,
 "error":{"code":-32001,
          "message":"A valid API key or OAuth access token is required to call tools."}}
```

The protected-resource document names the terms: resource `https://mcp.tradingdata.io`, authorization server `https://tradingdata.io`, bearer method `header`, and exactly one scope, `market:read`. A free account is the entry point the vendor advertises, and it is OAuth rather than a key pasted into a config.

One measurement worth keeping: the two well-known routes disagree about the resource identifier. `/.well-known/oauth-protected-resource` returns `https://mcp.tradingdata.io`, while `/.well-known/oauth-protected-resource/mcp` returns `https://tradingdata.io/mcp`. Both answer `200`, both name `https://tradingdata.io` as the authorization server, and both advertise the same single scope. A client that validates the resource field against the URL it connected to will pass on one route and may object on the other, so register against the host you actually call.

## The 48 tools, grouped

| Family | Tools |
|---|---|
| Discovery | `search_symbols` |
| Quotes and bars | `get_quotes`, `get_ohlcv`, `get_market_overview`, `compare_stocks` |
| Company fundamentals | `get_company_profile`, `get_financial_statements`, `get_financial_ratios`, `get_financial_metrics`, `get_segment_financials`, `get_earnings_kpis` |
| Filings and ownership | `get_sec_filings`, `search_sec_filings`, `read_sec_filing`, `get_filing_items`, `get_insider_transactions`, `get_institutional_holders`, `get_beneficial_owners` |
| Estimates and calendar | `get_analyst_estimates`, `get_earnings_release`, `get_earnings_calendar` |
| Options and derivatives | `get_options_chain`, `get_crypto_options`, `get_crypto_derivatives`, `get_short_interest`, `get_cot_positioning` |
| Funds and indices | `get_etf_holdings`, `get_index_constituents`, `get_dividends`, `get_bond_yields` |
| Crypto and on-chain | `get_crypto_markets`, `get_crypto_asset`, `get_oracle_prices`, `get_defi_stats`, `get_onchain_metrics`, `get_tokenized_stock` |
| Commodities and FX | `get_commodities` |
| Macro | `get_macro_series`, `search_macro_series`, `get_macro_snapshot`, `compare_macro_series`, `get_macro_calendar`, `get_macro_release`, `get_macro_revisions`, `get_macro_updates`, `get_regional_data`, `screen_stocks` |
| News | `get_news` |

Two of those are the reason this entry is worth a guide rather than a line. **`get_options_chain`** is the one that matters to anyone hedging rather than narrating: an assistant asked "what is the market pricing for a move" needs strikes, implied volatility and greeks, and a quote API cannot fake it. **`get_macro_revisions`** and **`get_macro_release`** are the other end: macro series get restated, and a model answering from a stale snapshot produces a number that was true last month and is now wrong, which is the failure mode that erodes trust faster than a refusal.

The vendor states the coverage as 800,000+ US and international macro series, and states that every quote carries its timestamp and delay. Treat those two as vendor claims, not measurements: this pass verified the tool surface and the auth tier by protocol, and could not exercise a call without a token.

## Why this belongs in an operator's stack

For a business, market data is rarely a trading problem. It is a pricing problem, a treasury problem and a board-deck problem. A CFO asking "what did the dollar do against the euro in the quarter we just closed, and what does the forward curve say about the next one" is running `get_macro_series` and `get_commodities`, not a trading terminal. A founder preparing a raise is running `compare_stocks` and `get_analyst_estimates` against the public comparables, then `get_sec_filings` to check what those comparables actually disclosed.

The value of one endpoint with one scope is auditability. When the answer to "why is our gross margin down" has to sit next to a quote, a filing and a macro print, four vendors means four credential sets, four rate-limit budgets and four sets of timestamp conventions that do not agree. One scope, `market:read`, is also a small permission to hand an agent: read-only by construction, with nothing in the tool list that places an order, moves money or writes anything.

## The class it enters, with the owners named

Financial data is the densest class in this catalog and this entry does not pretend to be first. [Gloom](/hermes/mcp/servers/external/gloom-mcp/) is the Bloomberg-shaped terminal for agents. [Ultralayer](/hermes/mcp/servers/external/ultralayer-mcp/) covers market news and developments with impact scores, which is the narrative layer. [aiworker-data](/hermes/mcp/servers/external/aiworker-data-mcp/) sells per-call DeFi and prediction-market data over x402. The [Stock Market MCP Server](/hermes/mcp/servers/external/stock-market-mcp-server/) is the free local option, 90+ tools on SEC filings, insider trades, FRED and 13F, run through `npx` with your own key.

TradingData's distinct ground is the intersection it holds in one hosted endpoint: **options chains with greeks** at the same address as **SEC XBRL statements** and a macro set that distinguishes a release from a revision. The local option has filings and FRED but not options greeks. The news layer has neither. The pay-per-call option is crypto-first. If the question is "price the risk and cite the filing in the same answer", this is the shortest path.

## Limits, stated as limits

A keyless client can discover the surface and cannot use it: every `tools/call` needs an OAuth token or API key, so the 48 tools are a menu until you sign in. The free tier's call ceiling is not published on the endpoint, so budget it as a trial rather than a production allowance. Data is delayed, by the vendor's own statement on every quote, so nothing here should be used for execution timing. The scope is `market:read`, which means no portfolio write, no order, no watchlist mutation: good for safety, and it means your own positions have to come from somewhere else. And this guide verified the protocol surface, not the data: whether a given international listing carries a full options chain is a per-symbol question to test with your own token before relying on it.

## Frequently asked questions

### Can I use TradingData MCP without an account?

Partly. `initialize` and `tools/list` answer without credentials and return all 48 tools, which makes the surface inspectable. Any `tools/call` returns JSON-RPC error `-32001`, "A valid API key or OAuth access token is required to call tools", so the free account is required before the first real answer.

### What scope does it request?

One: `market:read`, declared on both protected-resource documents alongside `https://tradingdata.io` as the authorization server. There is no write scope in the document, and no tool in the 48 that places an order or moves money.

### Does it cover options, or only spot quotes?

`get_options_chain` returns chains with greeks, and `get_crypto_options` and `get_crypto_derivatives` carry the crypto equivalents. `get_short_interest` and `get_cot_positioning` cover positioning, which is the part of the picture a spot quote leaves out entirely.

### How are macro revisions handled?

There are three separate tools for it: `get_macro_series` for the series itself, `get_macro_release` for a specific print and `get_macro_revisions` for restatements, with `get_macro_calendar` for what is due and `get_macro_updates` for what changed. A model that only reads the level cannot tell you a series was restated, which is why the split exists.

### Is this a trading system?

No. It is a read-only data surface with one scope. There is no order entry, no position management and no execution path; the vendor states every quote carries its timestamp and delay.
