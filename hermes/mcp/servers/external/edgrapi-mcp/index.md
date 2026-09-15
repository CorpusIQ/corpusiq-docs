---
title: "Edgrapi MCP - SEC EDGAR Structured Data for Agents"
description: "Hosted MCP server turning raw SEC EDGAR filings into clean JSON: Form 4 insider trades, typed 8-K events, 13F holdings with quarter-over-quarter diffs, 13D/G activist stakes, fundamentals and ratios across nine tools at api.edgrapi.com/mcp."
category: Finance
stars: "0 (new listing, paperandbeyond23-gif/edgrapi-mcp)"
added: 2026-08-31
source: "chatmcp/mcpso issue #3848 (Aug 31, 2026 afternoon sweep)"
relevance: ★★★
tags: [mcp-server, sec, edgar, insider-trading, 13f, 13d, filings, finance, remote]
---

# Edgrapi MCP

**Hosted Streamable HTTP MCP server that turns raw SEC EDGAR filings into clean, queryable JSON.** Point an MCP client at one URL, authenticate with a free key, and nine tools appear: Form 4 insider trades with market-wide buy and cluster-buy detection, 8-K material events as typed items, a fund's 13F portfolio aggregated by CUSIP and diffed against the prior quarter, 13D/13G activist stakes, XBRL-parsed fundamentals, computed ratios, company records, recent filings, and the narrative sections of the latest 10-K or 10-Q as clean text.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://api.edgrapi.com/mcp
Auth: Free API key for data calls (catalog surface answers anonymously)
Server card: https://api.edgrapi.com/.well-known/mcp/server-card.json
Repo: github.com/paperandbeyond23-gif/edgrapi-mcp (MIT)
Homepage: edgrapi.com
Tools: 9 (get_insider, get_events, get_holdings, get_activist, get_fundamentals, get_ratios, get_company, get_filings, get_sections)
```

## Why This Matters for Operators

The SEC's data is free; parsing it correctly is the work. Edgrapi does the parsing once and exposes it as tools an agent can call repeatedly.

First, **insider and activist signals arrive pre-structured.** Instead of reading raw Form 4 XML, an agent gets owner, role, transaction code, and market-wide cluster-buy detection in one call - the exact signal analysts watch before a diligence call.

Second, **13F holdings come pre-aggregated and pre-diffed.** A fund's latest 13F portfolio arrives ranked by value, aggregated by CUSIP across sub-managers, and diffed against the prior quarter - quarter-over-quarter position changes without spreadsheet work.

Third, **the narrative sections are LLM-ready.** Risk Factors, MD&A, and Business sections extracted from the latest 10-K and 10-Q as clean text save the extraction step entirely for competitive intelligence and vendor diligence.

## Tools and Capabilities

All nine tools were live-probed and verified Aug 31, 2026:

| Tool | What it returns |
|------|-----------------|
| `get_insider` | Parsed Form 4 insider trades: owner, role, transaction code, plus market-wide buys and cluster-buy detection |
| `get_events` | 8-K material events as typed items (2.02 earnings, 5.02 executive change, 1.05 cybersecurity incident, 2.01 acquisition) |
| `get_holdings` | A fund's latest 13F portfolio, CUSIP-aggregated and diffed against the prior quarter |
| `get_activist` | Schedule 13D/13G filings - disclosures triggered when anyone crosses 5% of voting stock |
| `get_fundamentals` | Normalized income statement, balance sheet, and cash flow parsed from SEC EDGAR XBRL |
| `get_ratios` | Margins, ROE/ROA, leverage and liquidity ratios derived from EDGAR fundamentals |
| `get_company` | CIK, legal name, SIC industry, fiscal-year end, exchanges and website for a ticker |
| `get_filings` | Recent 10-K/10-Q/8-K filings with filing and report dates and document links |
| `get_sections` | Narrative sections (Risk Factors, MD&A, Business) from the latest 10-K/10-Q as clean text |

## Installation

Add the remote MCP server to any MCP client (Claude, Cursor, Cline, VS Code):

```json
{
  "mcpServers": {
    "edgrapi": {
      "type": "http",
      "url": "https://api.edgrapi.com/mcp"
    }
  }
}
```

## Configuration

Get a free API key at edgrapi.com and attach it to data calls as an authorization header. The catalog surface (initialize and tools/list) answers anonymously, so clients enumerate the tool list before any key is configured.

## Business Relevance

- **Operators and investors** track insider cluster-buys and 13F position shifts across watchlists without touching EDGAR's raw interface.
- **Competitive intelligence teams** diff 13F portfolios quarter over quarter to see where institutional money is rotating.
- **Diligence workflows** pull typed 8-K events and clean 10-K sections into vendor and counterparty checks.

## Integration with CorpusIQ

Edgrapi and CorpusIQ compose as the outside and inside halves of company intelligence. CorpusIQ's read-only connectors answer from the books you already run (QuickBooks, Stripe, HubSpot, GA4) with source-cited numbers, while Edgrapi answers from public filings: who insiders are trading, what institutions hold, and what a competitor disclosed in its last 10-K. Run both and an agent can reconcile public-market posture against internal operating data in one conversation.

## Limitations

- Brand new listing: repo created Aug 24, 2026, zero stars - expect early-stage roughness and evolving limits.
- US-listed tickers only (SEC EDGAR coverage); no OTC or private-company data.
- Data calls require the free key; anonymous access covers the catalog surface only.
- Pricing and rate-limit structure beyond the free key are not yet documented on the listing.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [SEC EDGAR MCP - Full-Text Filing Search for Agents](/docs/hermes/mcp/servers/external/sec-edgar-mcp)
