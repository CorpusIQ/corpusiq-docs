---
title: "Kresmion MCP - Market Intelligence for Agents"
description: "Prediction markets, on-chain flows, equity signals, 13F positioning and macro regime scores with cited sources behind every record."
category: Finance
stars: n/a (no public repo)
added: 2026-09-30
source: "mcpservers.org server page (kresmion.com)"
relevance: ★★★
tags: [finance, market-intelligence, prediction-markets, equities, macro, sec-filings, webhooks, remote-mcp]
---

# Kresmion MCP

**Market intelligence with a cited source behind every record.** Kresmion is one HTTP API and hosted MCP server over prediction markets, on-chain crypto flows, equities and macro: Polymarket and Kalshi markets with smart-money flow, labeled whale transfers, ETF flows, SEC Form 4 insider clusters, congressional trades, 13F institutional positioning, a cross-asset regime score and a published signal track record with losses included. The hosted MCP server exposes 35 tools and every response carries a freshness stamp.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (self-serve, read-only)
Endpoint: https://kresmion.com/api/mcp
Tools: 35
Pricing: free during beta, 10,000 calls/month, 120 req/min
Category: Finance
Built by: kresmion.com
```

## Why This Matters for Operators

Market context arrives scattered across terminals, EDGAR, on-chain explorers and prediction platforms. Kresmion consolidates it behind one key with uniform, source-attributed records, and it is information-only: the API cannot write, delete or move anything, so an agent cannot trade or alter state.

Two mechanisms make it safe for autonomous use. Keys are read-only and can be allowlisted to source IP addresses, and every record states its source and coverage date. The published track record includes losses, which is the honesty signal that separates this from signal-marketing: forward returns after every signal are published, not cherry-picked.

## Tools & Capabilities

| Area | What it covers |
|---|---|
| Prediction markets | Polymarket and Kalshi markets, price history, order books, smart-money flow, cross-venue divergence, calibration, resolutions |
| Crypto | Labeled whale transfers, exchange wallet holdings, spot ETF flows, derivatives funding, open interest, options |
| Equities | Signal scores, Form 4 insider clusters, congressional trades, 13F institutional positioning, OHLCV history |
| Macro | Cross-asset regime score, CFTC Commitments of Traders, Treasury TIC flows, BIS systemic indicators |
| Signals | One cross-asset feed of scored events with source attribution |
| Intelligence | Signal track record, confluence composites, prediction-vs-options divergence, per-ticker smart-money scores, delta feed for polling |
| Bulk | Date-ranged gzip CSV exports for backfills: market history, resolutions, whales, signals |

Webhooks fire on signal.created, whale.transfer, prediction.repricing, prediction.divergence and etf.flow, each delivery signed so agents can verify provenance instead of polling.

## Installation

```bash
claude mcp add --transport http kresmion https://kresmion.com/api/mcp
```

Mint a key at kresmion.com/settings/api-keys and attach it as the Authorization header with the Bearer scheme. A standalone stdio server is also downloadable for local runs with the key in the environment.

## Configuration

```json
{
  "mcpServers": {
    "kresmion": {
      "type": "http",
      "url": "https://kresmion.com/api/mcp"
    }
  }
}
```

Keys are shown once at creation, revocable at any time, capped at five per account, and optionally locked to exact IPv4 or IPv6 source addresses.

## Business Relevance

- **Founders and operators** track macro regime and funding signals before financing decisions
- **Analysts** combine prediction-market probabilities with 13F and insider data in one call
- **Quant and trading teams** backfill research with dated gzip CSV bulk exports
- **Agent builders** subscribe to signed webhooks instead of polling the delta feed

## Integration with CorpusIQ

Kresmion adds the market backdrop to CorpusIQ's company-level answers. A composed workflow: CorpusIQ reports a company's private financials from QuickBooks or Stripe connectors, Kresmion reports the public positioning around it, 13F holdings, insider clusters and prediction-market pricing, and the operator reads both pictures in one session. For investor conversations, the signed webhooks give a provenance trail that matches CorpusIQ's evidence-first style.

## Limitations

- Free during beta with no uptime SLA; figures can lag or be revised
- Information-only, not investment advice, and stated as such
- Higher tiers beyond the free 10,000 monthly calls are on request only
- Crypto and on-chain data included, so usefulness skews toward multi-asset operators

## FAQ

### What does a read-only key mean?

The API cannot write, delete or move anything. Keys can also be allowlisted to source IPs and are rejected with 401 from other addresses.

### Is the signal track record honest?

It publishes forward returns after every signal, losses included, plus calibration and prediction-vs-options divergence data.

### What does it cost?

Free during beta with a self-serve key: 10,000 calls a month at 120 requests per minute, with 429 and Retry-After over the limit.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [fAlpha MCP - Read-Only US Equity Research for Agents](/hermes/mcp/servers/external/falpha-mcp/)
- [Gloom MCP - Bloomberg-Style Financial Terminal for AI Agents](/hermes/mcp/servers/external/gloom-mcp/)
- [SEC EDGAR MCP - Full-Text Filing Search for Agents](/hermes/mcp/servers/external/sec-edgar-mcp/)
