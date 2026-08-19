---
title: "Austin MLS MCP - Live Austin Real Estate Listings for AI Assistants"
description: "Free remote MCP server with live Austin-area MLS listings: active listing search by neighborhood, price, beds and schools, closed-sale comps, and market stats including median price, inventory, and days-on-market by ZIP or school district"
category: Real Estate Data
stars: n/a (new listing)
added: 2026-08-18
source: "mcpservers.org (neuhausre-com-austin-mls-mcp)"
relevance: ★★
tags: [real-estate, mls, austin, listings, comps, market-stats, remote-mcp, no-auth]
---

# Austin MLS MCP

**Live Austin-area MLS listings inside any MCP-capable AI assistant — active listings, property details, schools, taxes, and neighborhood data for the Austin metro.** A free remote MCP server with no install: one connector URL gives agents natural-language search over active listings, closed-sale comparables, and market statistics. Listings are updated every few minutes.

```
Server type: Remote (Streamable HTTP)
Auth: None (public read-only surface)
Endpoint: https://mls.neuhausre.com/mcp
Tools: 3 surfaces (listing search, comps, market stats)
Pricing: Free
Category: Real Estate Data
Built by: NeuhausRE.com (Austin real estate brokerage)
```

## Why This Matters for Operators

Austin real estate professionals, investors, and analysts currently answer "find 4-bed homes in Lakeway under $1M on at least an acre" by clicking through MLS filters and dashboards. This server replaces that with a single natural-language question inside the AI they already use, then backs it with comps and market statistics from the same source — brokerage-sourced MLS data refreshed every few minutes.

The brokerage-native source matters: listings are first-party, not scraped. And the free, no-auth design means agents can be pointed at it without managing credential lifecycles.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_listings` | Active Austin-area homes by neighborhood, price, beds, schools, and features |
| `pull_comps` | Closed-sale comparables within a radius, filtered by date and property type |
| `market_stats` | Median prices, inventory, and days-on-market by city, ZIP code, or school district |

## Installation

```bash
claude mcp add --transport http austin-mls https://mls.neuhausre.com/mcp
```

No account, no key. Works in Claude Desktop, claude.ai (Pro or Max via Settings → Connectors), and any MCP client that accepts remote HTTP servers.

## Configuration

```json
{
  "mcpServers": {
    "austin-mls": {
      "type": "http",
      "url": "https://mls.neuhausre.com/mcp"
    }
  }
}
```

## Business Relevance

- **Austin agents and teams** run listing searches and comps from chat instead of the MLS dashboard
- **Investors** screen neighborhoods by inventory and days-on-market trends
- **Appraisers and analysts** pull closed comps within a radius of a subject property
- **Relocation and property-management operators** answer client questions in one session
- **Developers** fold live MLS data into custom agent workflows with one URL

## Integration with CorpusIQ

CorpusIQ brings the money and pipeline layer (QuickBooks, Stripe, CRM) while Austin MLS brings the live property layer for the Austin metro. A real estate operator can run both in one agent session: CorpusIQ for commission accounting, deal pipeline, and financials, Austin MLS for current listings, comps, and market stats — then join the two on address or ZIP.

## Limitations

- Austin metro only; no other markets
- MLS data access may carry licensed-use terms from the brokerage
- No auth means no per-agent scoping (public read-only surface)
- Hosted-only: no self-host option published
- New listing (Aug 2026), no track record

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
