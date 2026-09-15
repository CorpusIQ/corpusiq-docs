---
title: PropRaven MCP - US Parcel and Property Intelligence
description: "PropRaven MCP gives agents access to 191.3M US parcels (110M mapped) across all 50 states with ownership, deeds, permits, hazard scores, valuations and deal screens. Eight stdio tools plus a hosted endpoint, a free API key with 1,000 monthly lookups, and pay-per-call x402 access to the paid deal products."
category: Real Estate
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3953"
relevance: ★★★
tags: [real-estate, property-data, parcels, deals, x402, remote-mcp, stdio]
---

# PropRaven MCP - US Parcel and Property Intelligence for Agents

**Remote MCP server (Streamable HTTP) with a local stdio package** - PropRaven serves canonical parcel intelligence to agents: 191.3M US parcels with ownership, valuation, permits, deeds, hazard and market data, exposed through 8 MCP tools with a hosted endpoint and an npm stdio package, plus a 40-endpoint REST API underneath for the deal-screen products.

```
Server type: Remote (Streamable HTTP) or local stdio (npm @propraven/mcp)
Auth: OAuth connector flow, or bearer API key (pz_...); free key gives 1,000 lookups/mo
Endpoint: https://propraven.com/mcp (probe-verified live; 401 without auth)
Tools: 8 (parcel.lookup, parcel.search, parcel.compare, owner.pierce, hazard.score, valuation.estimate, permits.history, sales.history)
Pricing: Free tier; paid deal products pay-per-call over x402 (USDC on Base)
Category: Real Estate
Built by: PropRaven (propraven.com); repo github.com/jdw2111/propraven-mcp
```

## Why This Matters for Operators

Property research today means jumping between county assessor portals, permit offices and hazard maps, each with its own lookup ritual. PropRaven MCP compresses that into eight agent tools over a single national dataset: an agent can answer "who owns this parcel, what are its permits and sales history, is it in a hazard zone, and what is it worth" in one call chain - and then run the deal screens (absentee owners, flips, portfolio owners) through the paid x402 products when a lead is worth paying for.

**The two-tool discovery surface is free, and the free API key is real: 1,000 lookups a month before any payment - enough for genuine evaluation, which is the correct posture for a pay-per-call data product.**

## Tools & Capabilities

| Tool | What it returns |
|---|---|
| parcel.lookup / parcel.search | Single-parcel detail and search across the national parcel set |
| parcel.compare | Side-by-side parcel comparison |
| owner.pierce | Ownership chain resolution through LLCs and trusts |
| hazard.score | Flood, fire and environmental risk scoring |
| valuation.estimate | Automated valuation with comps |
| permits.history / sales.history | Permit and transaction timelines per parcel |
| Deal screens (paid) | Absentee owners, flips, portfolio owners, market trends via the REST API's deal endpoints |

## Installation

Hosted: add the endpoint with the API key as bearer header, or connect through the OAuth connector from claude.ai. Stdio: npm install the package and run it locally with the key in the environment.

```bash
claude mcp add --transport http propraven https://propraven.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "propraven": {
      "url": "https://propraven.com/mcp",
      "headers": {
        "Authorization": "Bearer pz_YOUR_KEY"
      }
    }
  }
}
```

The same key works for the stdio server via the PROPRAVEN_API_KEY environment variable. Paid deal products bill per call over x402 (USDC on Base) with no account required beyond the wallet.

## Business Relevance

- **Real estate investors** run deal screens (absentee, flips, portfolio owners) without a data subscription.
- **Title and due-diligence firms** automate parcel, permit and hazard lookups per engagement.
- **Insurance and lending teams** get hazard scores and valuations in the underwriting workflow.
- **PropTech builders** embed the REST API for webhooks, geojson exports and comp packs.

## Integration with CorpusIQ

PropRaven identifies the property; CorpusIQ quantifies the business around it. An investor workflow: the agent screens parcels with PropRaven's deal tools, then models the portfolio economics with CorpusIQ's Stripe, QuickBooks and GA4 connectors to decide which opportunities clear the return threshold.

## Limitations

- Brand new listing (issue #3953, Sep 5, 2026); repo has 0 stars, no license file declared.
- The stdio package exposes 8 tools; the 31-tool count in the submission includes the paid deal-screen products behind the REST API, not the free MCP surface.
- Paid products are pay-per-call, so heavy prospecting costs scale with volume.
- Data coverage is US-only.

## See Also

- [DFX Real Estate Intelligence MCP - US Property, Parcel and Debt Data](/docs/hermes/mcp/servers/external/dfx-real-estate-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
