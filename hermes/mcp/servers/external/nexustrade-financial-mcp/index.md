---
title: NexusTrade Financial MCP
description: Hosted MCP server for quantitative research, backtesting, and copy trading on the NexusTrade platform — 125 tools with OAuth 2.1 and brokerage execution behind platform risk controls.
category: Finance
stars: n/a (new listing)
added: 2026-08-14
source: mcp.so
relevance: ★★★
tags: [finance, trading, stocks, backtesting, quantitative-research, portfolio-management, copy-trading, remote-mcp]
---

# NexusTrade Financial MCP

**Remote MCP server (Streamable HTTP, OAuth)** — the hosted MCP surface of NexusTrade, connecting AI agents to a quantitative research and trading platform: stock screening, historical and fundamental data, multi-regime backtesting, managed compute, creator strategy marketplaces, and paper or live copy trading with brokerage execution behind platform risk controls. Built by Austin Starks (nexustrade.io, github.com/austin-starks/nexustrade-ts).

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 PKCE with dynamic client registration
Endpoint: https://nexustrade.io/api/mcp
Tools: 125 (screening, data, backtesting, portfolio/risk, compute, marketplace, brokerage)
Pricing: Platform plans; live brokerage actions require platform permissions and confirmation
Category: Finance
Built by: Austin Starks / NexusTrade (nexustrade.io)
```

## Why This Matters for Operators

Retail quant tooling has historically been a chain of disconnected parts: one vendor for data, one for backtesting, a rented machine for compute, and a broker whose API you wire up yourself. The agent-friendly gap was worse — AI assistants could talk about markets but could not touch them safely.

**NexusTrade puts the whole quant lifecycle behind one OAuth'd MCP endpoint.** An agent screens stocks, pulls fundamentals, builds and validates a strategy with multi-regime and walk-forward backtests, runs research workflows in managed compute, and then executes on paper or live — all while every live-impact action stays behind NexusTrade permissions and confirmation controls.

The marketplace layer is the structural novelty. Agents can discover public strategy creators, inspect their portfolios, fork a strategy into an editable snapshot (`fork_shared_portfolio`), or set up continuous mirroring into a paper or live portfolio at an explicit allocation (`copy_trade_shared`). Payment for monetized strategies hands off to NexusTrade Checkout — the MCP tool never receives payment credentials or completes a charge.

## Tools & Capabilities

The mcp.so listing reports 125 tools but does not extract a live tool list (it is served from the endpoint — verify after connecting). The published Overview documents these capability groups; two tool names are published explicitly:

| Area | What agents can do |
|---|---|
| Screening & data | Screen stocks; retrieve historical, market, and fundamental data |
| Backtesting | Build and run strategy backtests with multi-regime and walk-forward validation |
| Portfolio & risk | Analyze portfolios, positions, risk, and performance |
| Managed compute | Run research and data workflows in managed compute environments |
| Brokerage | Prepare paper or live brokerage actions behind authentication and platform risk controls |
| Creator marketplace | Discover public strategy creators and inspect their marketplace portfolios |
| Strategy access | Validate monetized strategy access; payment hands off to authenticated NexusTrade Checkout |
| `fork_shared_portfolio` | Create a one-time editable copy of a marketplace strategy in a new or existing portfolio |
| `copy_trade_shared` | Continuously mirror a subscribed or accessible strategy into a paper or live portfolio at an explicit allocation |

## Installation

```bash
claude mcp add nexustrade-financial-mcp --transport http https://nexustrade.io/api/mcp
```

MCP setup and examples are published in the repo README (github.com/austin-starks/nexustrade-ts#mcp-server). The TypeScript SDK lives in the same repository.

## Configuration

```json
{
  "mcpServers": {
    "nexustrade-financial-mcp": {
      "type": "http",
      "url": "https://nexustrade.io/api/mcp"
    }
  }
}
```

No static API key belongs in the client config. NexusTrade uses OAuth 2.1 with PKCE and dynamic client registration — the first connect opens a browser window for NexusTrade sign-in and authorization, and the client reuses the credentials for later sessions.

## Business Relevance

- **Independent traders** get research, backtesting, and execution in one agent-addressable stack instead of three vendors and a glue script
- **Fund managers and advisors** can inspect creator strategies, fork the promising ones, and run paper copies before allocating live capital
- **Strategy creators** monetize their strategies through a marketplace with enforced access validation — revenue without sharing raw IP
- **Fintech builders** get a reference architecture for gated agentic finance: OAuth, permissioned live actions, checkout handoff

## Integration with CorpusIQ

NexusTrade MCP covers the markets side of an operator's finances; CorpusIQ covers the business side. A composed workflow: NexusTrade's screening and backtest tools evaluate a strategy while CorpusIQ's QuickBooks connector supplies the operator's actual cash position and Stripe confirms funding availability before any live allocation — the agent only proposes trades the business can actually fund. Klaviyo's revenue attribution feeds into the strategy's walk-forward validation so "market edge" and "business cashflow" are evaluated in the same loop.

For strategy creators, CorpusIQ's Stripe and GA4 connectors measure what the NexusTrade marketplace does not expose — conversion from profile view to paid subscription and the funnel quality of each audience segment.

## Limitations

- Brand new listing (Aug 2026) — no long track record yet
- Live tool list not published in the directory; verify actual tool names and signatures after OAuth connect
- Live brokerage execution is gated behind NexusTrade permissions and confirmation controls — by design, not a workaround
- Trading carries market risk; the platform provides rails, not investment advice
- Marketplace access depends on creator-set terms; monetized strategies require checkout handoff

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
