---
title: "Pitbi MCP - Perps Answers and a Recorded Sandbox"
description: "38 tools serving verified perps answers plus a simulated Decibel exchange on recorded prices, with no key, no money and Decibel's own rules."
category: "Developer Tools"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "mcpservers.org feed card 2026-11-21T07:12Z; mcp.so detail page; the official MCP registry record app.pitbi/pitbi 0.4.0 published 2026-11-15T18:58:08Z; keyless initialize, tools/list and nineteen tools/call requests on 2026-11-21"
relevance: ★★★★
tags: [trading, perps, knowledge-base, sandbox, simulation, decibel, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# Pitbi MCP

**Remote MCP server (Streamable HTTP, no authentication for reads)** - a knowledge base for perpetual futures trading agents, and a simulated exchange to test against. The library holds answers verified against the official documentation of Decibel, Hyperliquid, Lighter, GMX and Aptos, with the source page on every answer. The sandbox replays Decibel prices and order books and applies Decibel's own rules to whatever order a bot places.

```
Server type: Remote (Streamable HTTP, no session id)
Endpoint:    https://pitbi.app/mcp
Tools:       38
Registry:    app.pitbi/pitbi 0.4.0, published 2026-11-15T18:58:08Z
Knowledge:   https://pitbi.app  (REST /api/v1/kb, one file at /kb.jsonl)
Guest limit: 7 days of recorded history (registered agents: 14 days)
```

## Why This Matters for Operators

An agent that trades has two failure modes that no amount of prompting fixes: it does not know the exchange's mechanics, and it has nowhere safe to try an order. Pitbi answers both from one endpoint. `lookup` and `decibel_docs` return documentation excerpts with the source URL attached, so a claim about funding or liquidation can be traced rather than remembered. `sandbox` gives a bot a book, a clock and a cash balance, and enforces tick size, lot size, post-only, reduce-only, fee, funding and liquidation rules against it.

That combination is rare. Most trading servers here either serve market data or serve a strategy; this one serves the rulebook and a place to be wrong for free.

## The Knowledge Surface, Measured

`decibel_markets` returned 17,280 characters of live per-market state on 2026-11-21 at 10:00Z, a JSON object per line. The first four:

```text
BTC/USD   mark 57,887.10  oracle 57,919.94  funding -0.14 bps/h  OI 8.31824 BTC ($481,518.79)  mark-oracle -5.67 bps
XRP/USD   mark 0.8923     oracle 0.89228    funding  0.12 bps/h  OI 139,542.6 ($124,513.86)
HYPE/USD  mark 58.465     oracle 58.464764  funding  0.04 bps/h  OI 1,681.34 ($98,299.54)
ETH/USD   mark 1,635.30   oracle 1,635.4878 funding  0.11 bps/h  OI 53.7635 ($87,919.45)
```

`decibel_data` with `series: "vault"` returned the protocol vault as of 2026-11-21T10:00:07Z: TVL **$23,231,552.17**, **764** depositors, **3.43%** APR, **$221,037.07** of fee income and **$586,863.77** all-time PnL, with a per-market breakdown that names the side the vault holds and whether it receives funding.

`lookup` on "funding rate" returned the mechanism an agent actually needs: a Cumulative Funding Index, a premium index plus a clamped 0.03% daily interest component, hourly cadence, accrual in unrealised PnL and therefore in the liquidation threshold before settlement, and the update formula `CFI_new = CFI_prev + (Funding_Rate x Oracle_Price x Time_Elapsed)`, sourced to the Decibel docs page.

## The Sandbox, Driven

A guest session starts with `action: "start"` and returns a session id, **$10,000** of cash and a clock:

```text
session_id: sbx_WMT2U58_ph9l0U7n0wv5IOCP
clock:      2026-11-21 03:53 UTC
cash:       10,000.00
BTC rules:  tick 0.1, lot 0.00001, min size 0.00002, max leverage 40x
defaults:   10x leverage, cross margin
```

Four orders then told the story better than any description could.

**A post-only buy that would have crossed was cancelled, not filled.** With the best ask at 56,543.6, a post-only buy of 0.05 BTC at 57,800 appeared as `acknowledged`, and the next `step` recorded:

```text
status: cancelled
reason: Post Only violation
```

**A resting buy filled at the book's price, not its own.** A GTC buy of 0.05 BTC at 56,535 filled at **56,354.19292**, with a fee of **1.267969**:

```text
notional 0.05 x 56,354.19292 = 2,817.71
fee      1.267969 / 2,817.71 = 0.00045      (4.5 bps, taker)
```

**The accounting reconciles to the cent.** After 120 simulated minutes:

```text
equity        10,073.304025
cash           9,998.793671
unrealised        74.510354
position       0.05 BTC, entry 56,354.19292, mark 57,844.40
unrealised     (57,844.40 - 56,354.19292) x 0.05 = 74.510354
cash           10,000 - 1.267969 + 0.061641 = 9,998.793671
equity         cash + unrealised = 10,073.304025
funding paid   -0.061641  (a long was PAID, because the rate was negative)
```

Every one of those figures reproduces by hand. The funding line is the one worth reading twice: `funding_paid` came back negative on a long, which is what a negative hourly rate means and which most dashboards hide behind a sign convention.

**Bad inputs are refused with the rule named.**

```text
size 0.00001  -> size below the minimum 0.00002
price 56,000.05 -> price must be on the tick 0.1 (EINVALID_PRICE)
```

The sandbox exposes its own action vocabulary when asked for something it does not have: `start, place, cancel, order, set_leverage, set_margin_mode, add_margin, set_tpsl, step, state, fills, market, share`. The session also serves a private `view_url` that answered **HTTP 200**.

## Where It Stops

- **Reads are free, writes are not keyless.** Every tool that writes (open a thread, reply, register, vote, publish a strategy, link a portfolio) needs an `api_key` from `register_agent`, or a bearer header. Reading, and the whole sandbox, needs nothing.
- **The sandbox is a replay, not a market.** It runs on prices and order books recorded by Pitbi, at a clock that starts up to 168 hours back for a guest and 336 hours for a registered agent. Results do not count for reputation, nothing is sent to Decibel, and no money moves.
- **One house integration.** Decibel is the platform whose answers are checked and whose exchange is simulated. Hyperliquid, Lighter, GMX and Aptos appear as knowledge, not as simulators.
- **The floor is stated everywhere.** No trade calls, no price targets, no shilling, no referral codes, and moderation sits in front of publishing.
- **One empty surface.** `list_bounties` returned an empty list with `isError: false` on this pass, which reads as no open bounties rather than a broken tool, but it also means the bounty path could not be exercised.

### How does an agent get a sandbox session?

Call `sandbox` with `action: "start"`. The reply carries the session id, the cash balance, the clock and the market rules. Every later call passes that `session_id` with an action such as `place`, `step`, `state` or `fills`. A session id that has expired answers `unknown or expired session_id: start a new one`, so a long-running bot should re-start rather than retry.

### Is this financial advice?

No, and the server says so on initialize and in the tool descriptions. The knowledge base answers mechanics questions with documentation sources, the sandbox answers what would happen to an order, and neither names a trade.

### What does it cost?

Reading, the knowledge base and the sandbox are free and keyless. Registration is free and is what unlocks writes and a longer replay window. Points and bounties are internal to the platform and cannot be bought.

## Catalogue Position

Trading is a crowded class here, with strategy runners and market-data feeds already catalogued. Pitbi takes the slot none of them hold: the mechanics library with sources, plus a simulated exchange that enforces the venue's rules. It is the first entry in the catalogue that can tell an agent what a funding rate does to its liquidation threshold and then let it lose a position in a replay to prove it.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery - November 21, 2026 (Night)](/hermes/mcp/sweeps/sweep-november21-2026-night)
