---
title: "ApexVol MCP - CorpusIQ Docs"
description: Options analytics over MCP — options chains, IV rank, Greeks, GEX, expected moves and screeners, 56 endpoints on one Pro API token, self-hosted client or remote connector.
category: Finance
stars: n/a (new listing)
added: 2026-08-15
source: mcp.so
relevance: ★★★
tags: [options, volatility, greeks, gamma-exposure, options-chain, trading-analytics, quantitative-finance, self-hosted]
---

# ApexVol MCP

**Self-hosted MCP client (Python, Bearer API token) with remote connector option** — ApexVol exposes a full options-analytics stack to AI agents: options chains, IV rank, VRP, Greeks, GEX, expected moves, skew, term structure, and screeners across 56 published data endpoints. The `apexvol-mcp` client calls the same REST API under the hood, so anything in the API reference is one natural-language question away. MIT, built by Ryan Silk (`github.com/ryansilk/apexvol-mcp`), works with any paid ApexVol plan.

```
Server type: Self-hosted (pipx/Python) or remote connector
Auth: Bearer API token (Pro plan, Account → API Access)
Endpoint: REST base https://apexvol.com, paths under /api/mcp/data/*
Tools: 43 analytics tools (56 REST endpoints)
Pricing: Paid ApexVol Pro plan; 60 req/min, 1000/hr per token
Category: Finance
Built by: github.com/ryansilk/apexvol-mcp
```

## Why This Matters for Operators

Options analytics used to mean a terminal subscription plus a quant to run the numbers. ApexVol collapses that into a token and an install: an agent can ask "what is the IV rank for SPY" or request a full options-chain snapshot and get structured answers instead of screen-clicks. **The same Pro token drives both the MCP client and direct REST calls, so operators get one billing line and one auth surface across agent and pipeline use.**

The reference design is agent-first: a single-file API reference sized for LLM context windows (`apexvol.com/docs/api/apexvol-api.md`) means agents can implement against the endpoints without wading through interactive docs. Error handling is explicit and machine-readable — 401/403/426/429 with distinct meanings, so an agent can tell a revoked token from a tier entitlement gap from a rate limit and act accordingly.

## Tools & Capabilities

Grouped from the published API reference (56 endpoints under `/api/mcp/data/`).

| Tool | Purpose |
|---|---|
| `chain`, `chain-at-time`, `simulate-chain` | Live and historical options chains, simulated post-move chains |
| `iv-rank`, `iv-crush`, `iv-opportunities`, `term-structure` | Volatility surface: rank, crush risk, opportunity scan, term shape |
| `gex`, `cross-index-gex`, `greeks-exposure`, `greeks-heatmap`, `portfolio-greeks` | Gamma exposure and Greeks at market and portfolio level |
| `expected-move`, `expected-vs-actual`, `historical-moves`, `post-earnings-drift` | Move expectations around events and earnings |
| `screen`, `search`, `mispricing-assessment`, `relative-value`, `relative-value-scan` | Screeners and relative-value scans across the universe |
| `analyze-strategy`, `build-strategy`, `optimize-strategy`, `scenario-analysis`, `stress-tests` | Strategy construction, optimization, and stress testing |
| `smart-money`, `flow`, `charm`, `skew`, `third-order-greeks`, `max-pain` | Advanced flow and microstructure analytics |

## Installation

```bash
pipx install apexvol-mcp
export APEXVOL_API_TOKEN=<your Pro token>
python -m apexvol_mcp.server
```

Setup walkthroughs: `apexvol.com/learn/claude-options-data-mcp`. REST reference: `apexvol.com/docs/api`.

## Configuration

```json
{
  "mcpServers": {
    "apexvol-mcp": {
      "command": "python",
      "args": ["-m", "apexvol_mcp.server"]
    }
  }
}
```

Create the token under Account → API Access on apexvol.com (Pro plan required). Rotate it there any time; a revoked token returns 401 immediately. Respect the 60/min and 1000/hr per-token limits and the monthly budget cap (`budget_exceeded` on 429).

## Business Relevance

- **Portfolio operators and RIAs** can run Greeks, stress tests, and scenario analysis in conversation instead of spreadsheets
- **Trading desks** get screeners, relative-value scans, and mispricing assessments on demand
- **Quant and risk teams** can automate volatility-surface checks and earnings-move expectations into pipelines over the same token
- **Fundamental analysts** can pull earnings calendars, verdicts, and post-earnings drift stats alongside price context

## Integration with CorpusIQ

ApexVol pairs with the CorpusIQ financial connectors as the analytics layer over the accounting and banking layer. An operator can have CorpusIQ pull holdings and cash positions from QuickBooks or Stripe, then ask ApexVol to stress-test the portfolio's option exposure or run a hedge-recommendation pass — the composition turns static financial data into a live risk conversation. Because the client is self-hosted and token-gated, it fits inside the same governed environment as CorpusIQ's read-only connectors; the API token can be stored alongside other credentials in the operator's secret store and rotated centrally.

## Limitations

- Pro plan required — no free tier on the API
- Rate limits (60/min, 1000/hr) and a monthly usage cap per token
- Brand-new MCP listing; the underlying REST API is documented but the MCP client has no community track record yet
- Options analytics is a specialist domain — surface-level use returns surface-level value
- US index and equity options focus; check coverage for your instruments before committing

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
