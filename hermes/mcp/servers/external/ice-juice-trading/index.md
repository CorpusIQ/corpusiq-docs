---
title: Ice Juice Trading MCP - Automated Trading on Your Alpaca
description: "Hosted MCP server that lets an AI assistant build, backtest, deploy and manage rules-based trading strategies on your own Alpaca brokerage account, on paper or live. OAuth 2.1 or API key, Streamable HTTP at mcp.icejuicetrading.com/mcp, broker connect and billing stay human-only. Free paper trading on every plan."
category: Finance
stars: n/a (new listing)
added: 2026-08-24
source: "mcp.so feed + live endpoint probe (HTTP 401 auth gate)"
relevance: ★★
tags: [alpaca, automated-trading, algorithmic-trading, backtesting, trading-bot, finance, paper-trading, remote-mcp]
---

# Ice Juice Trading MCP

**Hosted remote MCP server that turns your AI assistant into the operator of a rules-based trading account on your own Alpaca brokerage** - the same account controls you would drive from the dashboard, executed through your AI. Build strategy drafts, backtest them over history, deploy to paper or live, and tune risk knobs, while broker connect, billing and the emergency "flatten everything" control stay human-only. Built by Ice Juice Trading, listed on mcp.so under Finance & Commerce.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: OAuth 2.1 (dynamic client registration + PKCE) or first-party API key
Endpoint: https://mcp.icejuicetrading.com/mcp
Tools: not published (live tool list served from the endpoint; auth-gated)
Pricing: free paper trading on every plan; live trading is the paid tier
Category: Finance & Commerce
Built by: Ice Juice Trading (icejuicetrading.com)
```

## Why This Matters for Operators

Trading automation has historically been two jobs: writing the strategy and babysitting the execution. Ice Juice collapses the first job into conversation and keeps the second one human. **The safety model is the differentiator: whether an order is real depends on the connected account (paper vs live), and broker connect, billing, and the emergency flatten stay human-only** - so an AI can tune risk knobs and deploy strategies without ever being able to wire money out of the account.

The live endpoint is confirmed (initialize returns HTTP 401 to anonymous probes - the expected OAuth/API-key gate, same posture as Antwork and other verified hosted servers). The strategy lifecycle is documented end to end: read positions and balances, search the tradable universe, backtest ideas, author drafts, deploy, pause, resume, stop.

## Tools & Capabilities

The endpoint is auth-gated, so the live tool list is not published (mcp.so shows "No tools detected"). The vendor overview documents the capability surface; names below are capability labels, not confirmed tool names:

| Capability | Purpose |
|---|---|
| Account read | Positions, balances, all-time P&L, runs, trades, decision logs |
| Universe search | Search the tradable universe; read the strategy-primitive registry |
| Backtesting | Backtest strategy ideas over history; preview options-contract selections |
| Strategy authoring | Draft strategies and baskets (symbol lists) |
| Deployment control | Deploy strategies; pause, resume, stop; tune risk knobs - on paper or live |
| Human-only rails | Broker connect, billing, and emergency "flatten everything" never pass through the AI |

## Installation

```bash
claude mcp add ice-juice-trading --transport http https://mcp.icejuicetrading.com/mcp
```

Works with Claude Code, Codex, Cursor, VS Code and any MCP-compatible client. First connect triggers the OAuth browser flow (or paste a first-party API key).

## Configuration

```json
{
  "mcpServers": {
    "ice-juice-trading": {
      "type": "http",
      "url": "https://mcp.icejuicetrading.com/mcp"
    }
  }
}
```

Auth is OAuth 2.1 (dynamic client registration + PKCE) or a first-party API key. The server is remote and hosted - nothing to install. Start on paper trading (free on every plan) before any live account is connected.

## Business Relevance

- **Active traders and quant-curious operators** get strategy iteration without writing execution code: describe a rules-based idea, backtest it, deploy it on paper, promote to live only when ready.
- **Portfolio managers** get an audit trail: runs, trades and decision logs are readable through the same endpoint, so every AI-made move is reviewable.
- **Fintech builders** get a reference for the human-approval architecture: AI runs the desk, humans hold the kill switch.

## Integration with CorpusIQ

CorpusIQ answers questions about the business's own books (QuickBooks, Stripe, bank data); Ice Juice runs a personal trading account. They pair cleanly: an agent can read portfolio performance and decision logs from Ice Juice and reconcile outcomes against the operator's cash position and expenses in CorpusIQ - trading desk reality checked against company financials. Trading verification from Ice Juice, business truth from CorpusIQ.

## Limitations

- Brand new listing (submitted Aug 24, 2026) - no track record yet; treat the OAuth flow and live trading as early-stage surfaces.
- Tool names are not published; the capability table above is from the vendor overview, not a live tool list (endpoint is auth-gated).
- Live trading is a paid tier; paper trading is the free surface.
- US-focused brokerage (Alpaca); operators outside supported regions need a compatible broker account.
- Not advice: the vendor states plainly it is not a hedge fund and automates your rules, not its own.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Gex Live MCP](/hermes/mcp/servers/external/gex-live-mcp) - SPX dealer positioning for market context
- [Dados B3 MCP](/hermes/mcp/servers/external/dados-b3-mcp) - auditable Brazilian stock fundamentals
