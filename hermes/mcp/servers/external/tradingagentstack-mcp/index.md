---
title: "TradingAgentStack MCP - Who Places the Order"
description: "A read-only directory of 143 AI trading tools and broker MCP servers, ranked by Agent Risk Score, with the order-placing party named per broker."
category: Finance / Agent Trust
stars: n/a (free, read-only, MIT)
added: 2026-10-27
source: "live JSON-RPC probes on https://tradingagentstack.com/api/mcp answering initialize as tradingagentstack 0.5.0 and the full tools/list, the executed calls list_category, broker_order_gating, get_incidents and search_tools, the submission issue chatmcp/mcpso 6243, the docs page https://tradingagentstack.com/mcp/ and the MIT repository intoApex/tradingagentstack-mcp"
relevance: ★★★
tags: [trading, broker-mcp, agent-risk, custody, incidents, finance, keyless, streamable-http]
last_updated: "2026-10-27"
---

# TradingAgentStack MCP

**An agent that can place an order is a different kind of agent from one that can read a balance, and almost no MCP directory records which one a given server is. TradingAgentStack exists to answer that single question per server, with the vendor's own documentation as the source for the answer.**

```
Server type: Remote (Streamable HTTP), local stdio also published
Endpoint:    https://tradingagentstack.com/api/mcp
Auth:        none, read-only, no account touched
Tools:       8 live (search_tools, get_tool, list_category,
             compare_tools, broker_order_gating, get_risk,
             get_incidents, check)
Directory:   143 tools across 19 categories, last checked 2026-10-26
License:     CC BY 4.0 on the data, MIT on the server
Built by:    intoApex (tradingagentstack.com)
```

## Why This Matters for Operators

Every other finance server in this catalog answers questions about money. This one answers a question about the server itself, and it answers it before the connection is made. The difference is not academic: on the broker list the server returns, six of the fourteen broker MCP servers let the model submit and cancel orders on its own, and the notes say so per vendor.

The same pattern runs through the whole tool set. `get_risk` returns an Agent Risk Score built from custody and order-approval facts rather than from marketing copy. `get_incidents` returns security incidents with an official disclosure URL each, so the claim can be checked instead of trusted. `check` takes a name, a link, a Telegram or X handle, a GitHub repo or an app store link and reports whether it is official, listed, a known fake, a lookalike or unknown.

For an operator evaluating an AI trading product, or writing a policy on what an agent is allowed to touch, that is the difference between a demo and a decision.

## What It Returns, Verified

The tool count is the first correction: the submission documents five tools and the live `tools/list` returns eight. The three undocumented ones are `get_risk`, `get_incidents` and `check`, which are the three that carry the trust argument.

`list_category` with no argument returns an error string and the full category list, which is the documented way to enumerate categories. Nineteen of them, 143 tools in total, concentrated in broker MCP servers and AI trading bot platforms at fourteen each, then market data APIs at ten, and market data servers, risk tools, prediction markets and AI research copilots at nine each.

`broker_order_gating` groups all fourteen official broker MCP servers by who places the order. In the "AI trades directly" group:

- Alpaca MCP Server, 68 percent safety score, toolset limits available
- Longbridge MCP, 68 percent, vendor advises starting read-only
- NinjaTrader MCP (beta), 58 percent, the client decides whether the agent asks first
- moomoo MCP, 58 percent, trade scope submits and cancels, paper is authorized separately
- Tradier MCP Server, 50 percent, no separate confirmation step documented
- Public Hosted MCP Server, 28 percent partial, vendor says trades may run without per-order input

Each entry carries a page URL, the vendor's own source URL and a `last_checked` date. That is the shape the whole directory uses, and it is what makes the risk score auditable rather than a number.

`get_incidents` since January 2026 returned eleven entries, each tied to an official disclosure. Two from the week of this sweep: Foundation reported phishing sent from its own domains after a self-hosted application vulnerability let attackers reach part of its backend, with API keys revoked and email access cut in about ten minutes; Keystone reported a third-party monitoring tool vulnerability that took 25,964 buyer records, 12,873 unpaid checkout records and the WebAuth key used to check device authenticity, which means the exposure is counterfeit devices passing the check, and 18,835 inventory units are being destroyed because of it.

`search_tools` with `can_trade_live: true` and the query "broker mcp server" returned twenty matches, ordered with the safety score visible per row. CCXT MCP Server sits highest at 85 percent, because out of the box it serves public market data only and trading has to be enabled per account.

## Limits Worth Recording

- **Not financial advice, and it says so on every response.** The scores are rule-based heuristics over custody and approval facts, not audits.
- **Trading only.** There is no coverage of general business tooling, and no read across to non-trading MCP servers.
- **Public directory data, refreshed by hand.** `last_checked` runs 2026-10-26 or 2026-10-27 on the rows we read, so a vendor change inside a day will not appear.
- **Directory size is small by design.** 143 tools is a curated set, not a crawl, so a missing tool is not evidence the tool does not exist.
- **US-centric broker coverage on the gating tool.** The fourteen broker servers are the ones with public MCP documentation, not the full market.

## Wiring It Up

```json
{"type": "streamable-http", "url": "https://tradingagentstack.com/api/mcp"}
```

Local option, same server over stdio:

```json
{"mcpServers": {"tradingagentstack": {"command": "npx", "args": ["-y", "tradingagentstack-mcp"]}}}
```

No key, no account, no OAuth. A call to `check` before any trading server is connected is the highest-value single use: it costs nothing and returns official, listed, fake, lookalike or unknown plus the stored custody facts.

## FAQ

### Which broker MCP servers let the AI place the order itself?

Six of the fourteen, per `broker_order_gating`: Alpaca, Longbridge, NinjaTrader beta, moomoo, Tradier and Public. The tool returns the grouping for all fourteen, including the ones where the user confirms each order.

### Does it need a key or an account?

No. The endpoint answers `initialize` and the full tool list without authentication, all tools are read-only, and the server touches no trading accounts.

### How current is the data?

Every tool row carries its own `last_checked` date, and the rows read in this sweep were checked 2026-10-26 or 2026-10-27. The published dataset sits at tradingagentstack.com/data under CC BY 4.0.

### Can it tell me if a trading bot is a scam?

`check` accepts a name, a link, a Telegram or X handle, a GitHub repo or an app store link and returns official, listed, known fake, lookalike or unknown, plus any stored custody and incident facts. It is a sourced directory lookup, not a fraud determination.
