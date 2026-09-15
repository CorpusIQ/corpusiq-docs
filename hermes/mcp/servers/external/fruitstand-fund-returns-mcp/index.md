---
title: Fruit Stand Fund Returns MCP - US Fund and ETF Performance
description: Hosted MCP server for trailing and calendar-year total returns across 32,000+ US mutual funds and ETFs, refreshed daily from end-of-day pricing. Six tools with search, fetch and batch endpoints, authenticated by a free API key. Same curated data Fruit Stand sells through Snowflake Marketplace, callable directly from an agent."
category: Finance
stars: "n/a (hosted, no public repo)"
added: 2026-09-02
source: "mcp.so GitHub issue #3903"
relevance: ★★
tags: [funds, etf, returns, performance, finance, investment]
---

# Fruit Stand Fund Returns MCP - US Fund and ETF Performance Data

**Hosted Streamable HTTP MCP server** - trailing and calendar-year total returns for 32,000+ US mutual funds and ETFs, refreshed daily. Built for AI agents with search, fetch and batch tools; the same curated dataset Fruit Stand sells through the Snowflake Marketplace.

## Spec Block

| Field | Value |
|---|---|
| Server name | Fruit Stand Fund Returns |
| Registry | dev.fruitstand/fund-returns v1.0.0 |
| Endpoint | https://api.fruitstand.dev/mcp |
| Transport | Streamable HTTP |
| Auth | API key (free key at app.fruitstand.dev) |
| Repo | none public (commercial hosted service) |
| Docs | https://fruitstand.dev (Mintlify, llms.txt index) |

## Why This Matters for Operators

Fund performance data usually lives inside a Bloomberg terminal or a Snowflake warehouse. This server puts 32,000+ fund and ETF return series one tool call away from an agent, so a financial operator can answer client questions about fund performance, build comparison tables for proposals, and batch-pull return histories for portfolio reviews without leaving the conversation.

## Tools & Capabilities (6 tools)

| Tool | Description |
|---|---|
| searchFunds | Find funds by name or ticker |
| getFund | Fund metadata by identifier |
| getTrailingReturns | Trailing-period returns for one fund |
| getCalendarReturns | Calendar-year returns for one fund |
| batchTrailingReturns | Trailing returns for up to batch_max_codes funds in one call |
| batchCalendarReturns | Calendar-year returns for a batch, with an optional as-of year |

## Installation

Add as a remote MCP server with the endpoint above and your key. Discovery and tool listing require the key (verified live: anonymous initialize returns 401 "No Authorization Header"). Keys are issued free at app.fruitstand.dev.

## Configuration

- Get a free key at https://app.fruitstand.dev
- Attach it as the authorization header on the MCP endpoint
- Usage-based pricing tiers start free and scale up; see https://fruitstand.dev/pricing

## Business Relevance

Useful for: RIAs and wealth managers answering client fund questions, compliance teams documenting fund performance, fintech products embedding return data, and investment memos that need current trailing and calendar-year figures for specific funds and ETFs.

## Integration with CorpusIQ

Combine with CorpusIQ finance connectors: pull fund returns into the same agent context as portfolio, accounting and market data for end-to-end investment analysis workflows.

## Limitations

US funds and ETFs only. API key required even for discovery. No fund holdings or risk statistics, just returns. Data is refreshed daily, not intraday.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [FinBridge MCP - Korean and US Market Data for Agents](/docs/hermes/mcp/servers/external/finbridge-mcp)
- [Stock Market MCP Server - Real-Time Financial Data](/docs/hermes/mcp/servers/external/stock-market-mcp-server)
