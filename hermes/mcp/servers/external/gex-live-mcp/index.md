---
title: "Gex Live MCP - SPX Dealer Positioning for AI Agents"
description: "Measurement-only MCP server for SPX dealer positioning from the 0DTE options tape: zero-gamma flip, call and put walls, hold band for 1000+ finished sessions, plus a backtesting Lab with plain-language idea compilation. Three free tools, no key required."
category: Finance
stars: n/a (new listing)
added: 2026-08-22
source: mcpservers.org
relevance: ★★
tags: [options, spx, market-intelligence, gamma, backtesting, trading-data, remote-mcp]
---

# Gex Live MCP

**A hosted MCP server that serves measured SPX dealer positioning - zero-gamma flip, call/put walls and hold band for 1,000+ finished sessions - with a backtesting Lab behind an account login.** gex.live is measurement-only by design: no buy/sell signals, no trade recommendations, just derived per-session aggregates verifiable against the free history on the site. Three tools are open with no account and no key; five more drive the Lab conveyor that turns a plain-English trading idea into a compiled rule, a backtest and a quant optimization. The endpoint (`mcp.gex.live/mcp`) is live and returned the full free tool list to an anonymous probe.

```
Server type: Remote (Streamable HTTP)
Auth: None for 3 free tools; OAuth sign-in or labk_ token for Lab tools
Endpoint: https://mcp.gex.live/mcp
Registry: live.gex/gex-mcp (official MCP registry)
Tools: 8 (3 free archive reads + 5 Lab: compile, run, state, thread, idea)
Pricing: Free archive tools; Lab runs cost 1 credit each (refunded on failure)
Built by: gex.live
```

## Why This Matters for Operators

Options-market context has always been expensive to obtain and easy to misread. **Gex Live turns dealer-positioning research into a plain-English question your agent can answer in seconds** - "where was the zero-gamma flip on August 13, and where did the session close against the call wall?" - with every figure traceable to a finished session in the public archive. The measurement-only posture (no signals, by design) is what makes it safe to wire into an agent: nothing here tells you to trade, it tells you what the tape showed.

The Lab is the second half. An analyst describes a rule in words ("fade a +3 sigma stretch above vwap on top-decile volume"), the conveyor compiles it into a testable spec, backtests it with era tables, then quant-optimizes variants, and returns every variant instead of picking a winner. The judgment stays human, which is exactly where it belongs.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_sessions` | Finished SPX trading days in the archive, newest first, up to 50 per call |
| `get_session` | One session: OHLC, zero-gamma flip and crossings, call/put walls, hold band, net-gamma percentile, ATM IV |
| `get_levels` | Just the level set and where the session closed against it |
| `lab_compile` | Turn a plain-words idea into a testable rule or amend an existing one (free) |
| `lab_run` | Run the current conveyor step - backtest, then quant optimize (1 credit each) |
| `lab_state` | All your ideas, stages, results, the current conveyor holder and credit balance |
| `lab_thread` | The compile-chat history for one idea - how the rule reached its wording |
| `lab_idea` | Desk actions: desk, drop, delete, set display and alert options |

## Installation

```bash
claude mcp add --transport http gex https://mcp.gex.live/mcp
```

The free tools appear immediately. Sign in with your gex.live account (Connect flow) to unlock the Lab tools; scripts can attach a `labk_` token as a Bearer header instead.

## Configuration

```json
{
  "mcpServers": {
    "gex": {
      "type": "http",
      "url": "https://mcp.gex.live/mcp"
    }
  }
}
```

## Business Relevance

- **Fund managers and RIA analysts** verify dealer-positioning context against a public, dated archive instead of vendor decks.
- **Options educators** generate concrete session examples with real level sets for teaching material.
- **Quant-curious operators** compile and backtest rule ideas without standing up their own data pipeline.
- **Trading-desk juniors** query the same tape measurements the desk argues about, with answers sourced to a session date.

## Integration with CorpusIQ

Gex Live is a research feed, and it composes cleanly with the financial data CorpusIQ already exposes. An agent can pull a company's fundamentals through CorpusIQ's financial connectors, then use Gex Live's `get_session` to check the market regime on the relevant dates - earnings-day dealer positioning, say - so the context around a number is as explicit as the number itself.

The Lab output flows the other way: backtest verdicts and era tables from `lab_run` are structured JSON an agent can log or compare alongside portfolio metrics pulled through CorpusIQ. The measurement-only design means nothing in this pipeline fabricates a signal; both tools just answer the questions an operator asks.

## Limitations

- New listing: no established track record as an MCP server yet.
- SPX-focused and 0DTE-derived: useful context, not a complete market picture.
- Lab tooling requires an account and a credit balance; paid runs return 402 when credits run out.
- Measurement-only by design - if you want signals, you bring them yourself.
- Not investment advice; backtested performance does not guarantee future results.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
