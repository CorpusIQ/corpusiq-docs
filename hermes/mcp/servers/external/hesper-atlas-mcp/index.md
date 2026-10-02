---
title: "Hesper Atlas Evidence MCP - Verifiable Stock-Signal Claims"
description: "Read-only hosted MCP for independently checking a rules-based stock-signal product: inspect the full historical replay including losing and open periods, static-tail and walk-forward validation, methodology versions, provenance hashes and the forward-publication ledger. Nine evidence tools work with no account; six subscriber tools expose the latest signal layer over OAuth 2.1."
category: Finance
stars: "n/a (new listing, SimonMaj/hesper-atlas-agent-plugin)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3877 (Sep 1, 2026 night sweep)"
relevance: ★★
tags: [mcp-server, finance, stock-signals, verification, provenance, backtesting, oauth, remote-mcp]
---

# Hesper Atlas Evidence MCP

**Verifiable evidence behind a rules-based stock-signal product.** Hesper Atlas is a read-only MCP server that lets an agent independently check Hesper Atlas's own claims: the full historical replay including losing and open periods, static-tail and rolling walk-forward validation, methodology and calculation versions, provenance hashes, and the deployment-onward forward-publication ledger. Live-probed Sep 1, 2026: all 15 tools captured from the endpoint, 9 working with no account.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://hesperatlas.com/mcp
Auth: 9 evidence tools open; 6 subscriber tools via OAuth 2.1 PKCE + DCR, scope signals:read
Tools: 15 (live-probed Sep 1, 2026)
Registry: com.hesperatlas/hesper-atlas v1.6.0 (active)
License: MIT
Built by: Hesper Atlas (hesperatlas.com)
```

## Why This Matters for Operators

Every signal vendor has a headline. Almost none make the losing periods, the methodology revisions and the look-ahead risks checkable by a machine. Hesper Atlas built the verification surface into the product.

First, **the losing periods are first-class data.** `get_track_record`, `get_ledger_stats` and `list_closed_trades` expose winners and losers alike, so an operator can test whether a headline hides an unfavorable distribution before allocating anything.

Second, **validation artifacts, not assertions.** `get_heldout_evidence` and `get_walk_forward_evidence` return the committed row-level artifacts behind the 152-name static-tail and time-ordered validations, so the checks can be reconstructed or challenged.

Third, **an immutable forward ledger.** `list_forward_publications` and `get_forward_record` expose what was actually published, when, and what changed field by field - the defense against retroactive editing of published calls.

## Tools and Capabilities

All 15 tools were captured live from the endpoint on Sep 1, 2026. The server does not return raw or real-time market data, does not place trades, and does not advise; "current" means the latest completed end-of-day snapshot.

| Surface | Tools |
|---------|-------|
| Track record evidence (open) | `get_track_record`, `get_ledger_stats`, `get_symbol_record`, `list_closed_trades` - headline support, drawdowns, per-ticker round trips, raw replay |
| Methodology and provenance (open) | `get_methodology`, `get_provenance`, `get_heldout_evidence`, `get_walk_forward_evidence`, `list_forward_publications` - assumptions, hashes, validation artifacts, publication history |
| Subscriber signal layer (OAuth) | `get_signal`, `list_signals`, `get_market_context`, `get_model_portfolio`, `get_forward_record`, `get_changes_since` - latest end-of-day signals, regime context, model book, changed-field events |

## Installation

```bash
claude mcp add --transport http hesper-atlas https://hesperatlas.com/mcp
```

Nine evidence tools work immediately with no account. For the six subscriber tools, sign in via OAuth; the server requests only the narrow `signals:read` scope. Read-only API keys are a developer fallback.

## Configuration

```json
{
  "mcpServers": {
    "hesper-atlas": {
      "type": "http",
      "url": "https://hesperatlas.com/mcp"
    }
  }
}
```

OAuth 2.1 with PKCE and dynamic client registration; tokens rotate and the grant is revocable. Subscriber tools are denied gracefully when access is missing - the server tells you to use replay data instead of substituting it.

## Business Relevance

- **Allocators and funds** verify a signal product's claimed track record before committing capital, including the losing periods vendors normally compress.
- **Due-diligence analysts** reconstruct the static-tail and walk-forward validations from the committed artifacts instead of trusting a backtest image.
- **Compliance and risk teams** keep an audit trail of methodology versions and forward publications when a strategy is being reviewed.
- **Quant researchers** use the publication ledger as a ready-made out-of-sample honesty dataset.

## Integration with CorpusIQ

Hesper Atlas composes with CorpusIQ as the verification layer over market-facing decisions. A CorpusIQ workflow can pull portfolio or watchlist context from its connectors, ask Hesper Atlas for the evidence behind a signal claim - track record, validation artifacts and provenance - and attach the findings to the decision log alongside the rest of the operator's financial data. The operator keeps one governance point: CorpusIQ holds the business context, while Hesper Atlas supplies the checkable evidence, with hashes and publication cursors that survive later review.

## Limitations

- Brand new listing (repo created Sep 1, 2026); no adoption track record of its own yet.
- The product verifies one vendor's signal engine - it is a transparency layer for Hesper Atlas, not a general market-data or trading server.
- Subscriber tools require OAuth sign-in; the open tools stop at completed end-of-day history, no intraday freshness.
- No raw market data, no order routing, no investment advice - "current" means the latest completed end-of-day snapshot.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Edgrapi MCP - SEC EDGAR Structured Data for Agents](/hermes/mcp/servers/external/edgrapi-mcp)
- [Hive Intelligence MCP - Live Crypto Market Data](/hermes/mcp/servers/external/hive-intelligence-mcp)
- [Trooth Network MCP - Witnessed Company Trust Records](/hermes/mcp/servers/external/trooth-mcp)
- [VulX Watch MCP - Independent Security Review for AI-Built Apps](/hermes/mcp/servers/external/vulx-watch-mcp)
