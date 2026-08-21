---
title: "AskRentAI MCP — Property Portfolio Intelligence for Rent Manager Operators"
description: "Hosted read-only MCP server for Rent Manager property portfolios: plain-English questions about NOI, rent roll, delinquency, vacancy, lease expirations, work orders, vendor spend and financial reports answered from live data. OAuth sign-in, read-only by design, $10 per user per month with a seven-day free trial."
category: Real Estate & Property Management
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★★
tags: [property-management, rent-manager, real-estate, rent-roll, noi, read-only, oauth, remote-mcp]
---

# AskRentAI MCP

**Read-only Rent Manager intelligence for AI clients — plain-English portfolio questions answered from live data, with no write path back to the property management system.** AskRentAI is a hosted MCP server built on Rent Manager, the platform used across a large share of US rental housing, covering apartments, single-family, commercial, self-storage and mobile home / RV communities. Operators ask "which properties are below budget on NOI this quarter" and get the answer from the API at the moment they ask — no exports, no stale spreadsheets, no sync to configure.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://api.askrentai.com/mcp
Pricing: $10 per user per month, 7-day free trial (no credit card)
Category: Real Estate & Property Management
Built by: Brian Menold (github.com/brianmenold/askrentai-mcp)
```

## Why This Matters for Operators

Rent Manager ships a capable web API, but using it means knowing which endpoint holds the data, how the tables relate, how to authenticate and how to page results. Most property operators don't have a developer to spare for a reporting question, so API access sits switched on and unused while everyone goes back to exporting reports by hand.

**AskRentAI closes that gap: the AI calls the API for you, at the moment you ask.** The read-only architecture is the safety point, not a limitation — the server cannot post a charge, edit a lease or change a tenant record, so pointing a read-only Rent Manager API user at it gives a blast radius of zero.

## Tools & Capabilities

The listing does not publish a fixed tool list (the live tool set is served from the endpoint), but the documented coverage spans the operator's core surfaces:

| Area | What you can ask |
|---|---|
| NOI & financials | Which properties are below budget on NOI this quarter? |
| Delinquency | Who's more than 30 days delinquent, and how much in total? |
| Leases | Which leases expire in the next 90 days, and what are those units paying? |
| Work orders | How long are work orders staying open, by property? |
| Vendor spend | How much did I spend with each vendor last year, and did anyone's pricing jump? |
| Reporting | Run a year-over-year P&L and tell me which expense lines moved |

Coverage also includes vacancy and occupancy trends, prospects and lead sources, utility and water reconciliation, trial balance and stored documents.

## Installation

```bash
claude mcp add askrentai --transport http https://api.askrentai.com/mcp
```

Setup takes about ten minutes: connect through OAuth, point the server at your Rent Manager data, and start asking. Works with Claude, ChatGPT, Gemini, Grok and any MCP-compatible client. Vendor walkthroughs for Claude Code, Codex, Cursor and VS Code are published on the listing.

## Configuration

```json
{
  "mcpServers": {
    "askrentai": {
      "type": "http",
      "url": "https://api.askrentai.com/mcp"
    }
  }
}
```

OAuth sign-in on first connect. The vendor recommends a read-only Rent Manager API user so the server can never write back to your portfolio.

## Business Relevance

- **Property managers** get portfolio health answers without pulling and stitching reports
- **Asset managers and owners** can check NOI variance, delinquency aging and lease expiry risk across all properties in one session
- **Maintenance leads** track open work-order age by property to find the slow sites
- **Controllers** pull trial-balance and vendor-spend answers with the source numbers attached

## Integration with CorpusIQ

AskRentAI covers the property layer that CorpusIQ's 40+ connectors reach from the business side. A composed workflow can hold QuickBooks books, Stripe revenue and GA4 web traffic in CorpusIQ while AskRentAI answers the portfolio questions — delinquency aging, lease-expiry exposure, NOI variance — in the same agent session, so a single report can reconcile portfolio performance against the general ledger without exporting anything.

## Limitations

- Rent Manager only — no Buildium, AppFolio or Yardi coverage
- Read-only by design: no charges, lease edits or tenant-record changes
- Brand new (Aug 2026 listing), no track record yet; single-vendor hosted service
- $10 per user per month after the 7-day trial
- Tool list is served live from the endpoint, not documented statically

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
