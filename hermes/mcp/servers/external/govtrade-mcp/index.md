---
title: "GovTrade MCP - CorpusIQ Docs"
description: Congressional trading disclosures over MCP — STOCK Act filings with anomaly signals and per-politician trading baselines, paid per call via x402 in USDC on Base.
category: Finance
stars: n/a (new listing)
added: 2026-08-15
source: mcp.so
relevance: ★★
tags: [finance, congress, stock-act, insider-trading, market-intelligence, due-diligence, x402, self-hosted]
---

# GovTrade MCP

**Self-hosted stdio MCP server (Node, x402 payments)** — GovTrade wraps the live GovTrade x402 API so any agent can pull congressional trading disclosures with pre-computed anomaly scoring. Every trade is sourced from official STOCK Act filings for the House and Senate, scored for signal strength, and paid per call in USDC on Base with no subscription or API key. Built by Darcie Porter (`github.com/iamdarcie/govtrade-mcp`).

```
Server type: Self-hosted stdio (Node)
Auth: Funded wallet (EVM private key, USDC on Base)
Endpoint: GovTrade x402 API at govtrade-x402.onrender.com
Tools: 3 (congressional trade signals, trade history, politician baselines)
Pricing: Pay-per-call via x402 (USDC on Base), no subscription
Category: Finance
Built by: github.com/iamdarcie/govtrade-mcp
```

## Why This Matters for Operators

Congressional trading data is public but effectively unusable raw: STOCK Act filings are spread across two chambers, filed with lags, and carry no signal about which disclosures actually matter. GovTrade turns that into scored intelligence. **An agent doing market or diligence work gets, per trade, a signal strength score, a Low/Medium/High label, and natural-language reasoning for why the trade is notable** — unusual size versus the politician's own history, committee overlap, or federal contract ties.

For operators, this removes two manual workflows: keeping a watchlist of politically connected tickers, and eyeballing raw disclosure PDFs during due diligence. The server pays the underlying API per call from a funded wallet, so there is no account provisioning or key management to rotate — just a wallet with USDC and a stdio config block.

## Tools & Capabilities

The live tool list is served from the endpoint and was not extractable from the listing (no tools detected). Tools below are as described in the listing prose.

| Tool | Purpose |
|---|---|
| get congressional trade signals | Anomaly-scored congressional trades with signal strength and reasoning |
| get congressional trades | Full STOCK Act trade history for a politician or security |
| get politician trading baseline | Per-politician profile: trade count, average size, buy/sell ratio, top sector |

## Installation

```bash
git clone https://github.com/iamdarcie/govtrade-mcp
cd govtrade-mcp && npm install
```

## Configuration

```json
{
  "mcpServers": {
    "govtrade": {
      "command": "node",
      "args": ["/full/path/to/govtrade-mcp/index.js"],
      "env": {
        "EVM_PRIVATE_KEY": "0xYourKey"
      }
    }
  }
}
```

Setup requires a funded wallet with USDC on Base — the server pays the GovTrade API via x402 on every call. See the repository README for full instructions.

## Business Relevance

- **Fund managers and traders** can screen a ticker for recent congressional activity and whether any trade looks anomalous
- **Compliance and diligence teams** get a computed baseline per politician instead of raw filing dumps
- **Market-intelligence operators** can build reports that flag unusually active traders by sector
- **Newsroom and research agents** get source-attributed STOCK Act data with reasoning attached to every signal

## Integration with CorpusIQ

GovTrade feeds the financial-connector layer CorpusIQ already exposes. Pair it with the Stripe connector to reconcile any x402 wallet top-ups against business spend, and with QuickBooks to log data-procurement costs as research expense. An operator can compose a diligence workflow where CorpusIQ pulls the company profile and payment history from QuickBooks and Stripe, then asks GovTrade whether its executives or relevant committee members traded the stock recently — turning a disclosure hunt into one agent call. The wallet-based pricing means every call leaves a USDC settlement trail that operators can audit alongside the rest of the financial stack.

## Limitations

- Brand new — no track record yet, single-author repo
- Pay-per-call requires a funded Base wallet with USDC, an extra operational step versus API keys
- Congressional data is disclosed with lags — signals are computed on filings, not real-time trades
- No tools detected on the listing; verify the live tool list against the repo before production use
- Self-hosted stdio only — no published remote endpoint

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
