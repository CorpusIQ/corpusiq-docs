---
title: "RestoSignals MCP - Scored Restaurant Opening Leads"
description: "Remote MCP that returns deduped restaurant locations scored for opening likelihood, with the underlying signals, filterable by state, city and score."
category: "Sales"
stars: n/a (hosted platform, restosignals.com)
added: 2026-10-03
source: "mcpservers.org server page (restosignals-com)"
relevance: ★★★
tags: [sales, leads, prospecting, restaurants, hospitality, signals, remote-mcp]
---

# RestoSignals MCP

**Hosted MCP server** - RestoSignals returns scored restaurant-opening leads so an agent can pull the venues most likely to open soon, with the signals behind each score, filtered by state, city, signal or score.

```
Server type: Hosted (remote)
Auth: API key (100 free trial credits on signup)
Endpoint: https://www.restosignals.com (see vendor docs for the MCP path)
Category: Sales
Built by: RestoSignals (restosignals.com)
```

## Why This Matters for Operators

Outbound to the hospitality market usually starts with a list build: which restaurants are opening, where, and how soon. RestoSignals flips that into a scored feed. One request shape returns deduped venues with an `opening_score`, the signals that produced it, and dates, so an agent can pull a state's worth of qualified targets in a single call and hand a rep a prioritized queue.

The vendor names the buyers explicitly: POS systems, beverage distributors, commercial insurance, kitchen equipment, payment processors, design and build, linens and uniforms. Those are all vendors whose next customer is a venue that has not opened its doors yet, which makes early signal the whole game. The free trial credits let an agent validate a territory before any spend.

## Usage

```
GET /v1/openings?state=NY&min_opening_score=40
```

One request shape everywhere, filterable by state, city, signal or score. Returns deduped venues with the opening score, the signals behind them, and dates.

## Limitations

- US-focused, split by state and city.
- Signal depth varies by market; thin markets return fewer venues.
- Scored leads, not verified commitments; the score is a likelihood, not a contract.

## FAQ

### What is an opening_score?

A per-venue likelihood that the location is opening, built from the signals RestoSignals tracks. Filter with `min_opening_score` to set the bar.

### Do I need a card to try it?

No. Signup with email returns an API key and 100 free trial credits on screen, with no card.

### Which vendors use it?

POS systems, beverage distributors, commercial insurance, kitchen equipment, payment processors, design and build, and linens and uniforms are the listed buyer categories.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
