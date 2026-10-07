---
title: "aiworker-data MCP - x402 Pay-Per-Call Market Data for Agents"
description: "aiworker-data is a deterministic-first remote MCP server paid per call in USDC over x402 v2, no account or API key. 20 live-probed tools cover DeFi yields and protocol snapshots, Base token safety cards and wallet checks, Polymarket odds, resolution checks, backtests and screeners, crypto news search, Hacker News social mentions, claim checking and sourced briefs, priced $0.005 to $1 per call."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-12
source: "mcpservers.org /all page 1 (night crawl) + live JSON-RPC probe (20 tools captured)"
relevance: ★★★
tags: [x402, crypto, defi, polymarket, data, remote-mcp, streamable-http, pay-per-call]
---

# aiworker-data MCP

**Remote MCP server (Streamable HTTP, x402 v2 USDC pay-per-call)** - a deterministic-first data layer for agents with no account, no API key and no subscription. Each request carries a price in the x402 402 PAYMENT-REQUIRED response; the agent pays in USDC on Base or Solana and retries. Nothing settles unless the request succeeds. 20 tools live-probed in this sweep (server v0.2.0).

```
Server type: Remote (Streamable HTTP)
Auth: None (x402 v2 pay-per-call in USDC on Base and Solana)
Endpoint: https://aiworker.duckdns.org/mcp
OpenAPI: https://aiworker.duckdns.org/openapi.json
Tools: 20 (live-probed, keyless initialize + tools/list)
Pricing: $0.005 to $1 per call, per tool
Category: Data & Analytics
Built by: aiworker (ai-worker227 on GitHub)
```

## Why This Matters for Operators

The x402 model removes the friction that kills agent adoption of paid data: no signup, no key vault, no subscription - the agent sees the price in the 402 response, pays per call and gets deterministic results. For operators the interesting tools are the market ones: `news_search` covers twelve crypto and markets feeds refreshed every ten minutes, `social_mentions` searches Hacker News and Polymarket comments for any term, and `topic_brief` produces a sourced brief where every paragraph cites its source pages. Deterministic means no LLM in the loop for most routes, so the numbers do not hallucinate.

## Tools & Capabilities

| Tool | What it returns | Price |
|---|---|---|
| `defi_yields` | DeFi yield pools from DefiLlama, filtered by chain, project, symbol, min TVL | $0.02 |
| `defi_protocol` | One protocol snapshot: TVL by chain, category, 1d/7d change, audits | $0.01 |
| `yield_report` | LLM-written read of yield pools matching a filter, with risks and caveats | $0.10 |
| `token_check` | Base token safety card: contract, ownership, liquidity, honeypot simulation, 0-100 score | $0.05 |
| `token_info` | Cheapest Base token lookup: supply, holders, price, liquidity, FDV, 24h volume | $0.005 |
| `wallet_check` | Base wallet card: balances, activity, ERC-20 holdings, rule-based flags | $0.05 |
| `market_odds` | Polymarket odds for one market with 24h/7d moves | $0.01 |
| `resolution_check` | How a Polymarket market resolved: status, payout, resolver, timing | $0.05 |
| `rule_backtest` | Replay one fixed rule over resolved Polymarket markets | $0.25 |
| `odds_history` | Daily YES-price history with fills and volume (1-365 days) | $0.02 |
| `market_screener` | Ranked Polymarket markets under deterministic filters | $0.05 |
| `news_search` | Crypto and markets headlines from 12 feeds, newest first | $0.01 |
| `social_mentions` | HN stories/comments + Polymarket event comments matching a term | $0.01 |
| `claim_check` | Verdicts on factual claims against Wikipedia and supplied sources | $0.05 |
| `topic_brief` | Sourced 150-500 word brief with per-paragraph citations | $0.10 |
| `token_report` | Full pre-touch Base token report with verdict (avoid, caution, acceptable) | $1.00 |
| `trade_gate` | Rule-based pass/caution/block verdict before a swap | $0.05 |
| `airdrop_scan` | Wallet hygiene: honeypot, dust, batch-airdrop and spoof flags per token | $0.05 |
| `scrape_markdown` | One public page as clean Markdown | $0.02 |
| `scrape_summary` | Page Markdown plus a structured summary with key points | $0.04 |

All 20 tool names and the server version captured by live keyless probe in this sweep. Free pages (airdrop-spam watch, Polymarket backtest calibration, resolved-this-week, category counts) are served as HTML and JSON without payment.

## Installation

```bash
claude mcp add aiworker --transport http https://aiworker.duckdns.org/mcp
```

Send the request, read the price from the PAYMENT-REQUIRED header of the 402 response, pay it with any x402 client (`@x402/fetch`, `x402-axios`, the agentcash MCP) and retry. Framework wrappers for LangChain.js, the Vercel AI SDK and ElizaOS live in the ai-worker227/aiworker-examples repo.

## Configuration

```json
{
  "mcpServers": {
    "aiworker": {
      "url": "https://aiworker.duckdns.org/mcp"
    }
  }
}
```

No keys anywhere. The client handles payment; the health endpoint and all documentation pages are free.

## Business Relevance

- **Market researchers** get sourced briefs and claim checks with verbatim evidence at $0.05-$0.10 per call.
- **Crypto operators** run token and wallet due diligence (`token_report`, `trade_gate`) before exposure.
- **News and content teams** search twelve market feeds and HN mentions deterministically.
- **Quant-curious operators** replay published rules over resolved Polymarket markets at $0.25 a backtest.

## Integration with CorpusIQ

aiworker-data is a pay-per-call external evidence service that complements CorpusIQ's subscription model: a CorpusIQ-connected agent can spend cents on `news_search` and `social_mentions` when a report needs external market context, while first-party business data continues to flow through the CorpusIQ connectors. The x402 pattern also demonstrates the no-key model CorpusIQ could offer for metered external data in future.

## Limitations

- Homelab-hosted endpoint (duckdns): uptime and latency are not vendor-guaranteed.
- Pay-per-call means an agent in a loop can spend real money; cap calls at the client level.
- Solo-built project with no third-party track record or public server repo.
- Deterministic data comes from third-party sources (DefiLlama, Blockscout, Gamma); check freshness per tool.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [0xinsider MCP - Polymarket Trader Analytics for Agents](/hermes/mcp/servers/external/0xinsider-mcp)
