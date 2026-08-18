---
title: "Secondhand MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Search Facebook Marketplace, eBay, Depop, and Poshmark from any MCP client for resale research, pricing comps, and sourcing
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-08-17
source: "mcp.so GitHub issue #3613"
relevance: ★★
tags: [resale, marketplace-search, ebay, poshmark, depop, facebook-marketplace, pricing-comps, remote-mcp]
---

# Secondhand MCP

**MCP server for searching secondhand marketplaces: Facebook Marketplace, eBay, Depop, and Poshmark, from any MCP client.** Filter by price, condition, category, size, and color; pull full listing details with photos, descriptions, and seller info; and run deep-research style `search`/`fetch` calls. Ships as a free local npm server (MIT) and as a hosted remote server with OAuth sign-in and a free tier.

```
Server type: Local (npm, stdio) or Remote (Streamable HTTP)
Auth: None (local) or OAuth (hosted remote)
Endpoint: https://secondhandmcp.com/mcp
Install: npx secondhand-mcp (local)
Pricing: Free (local, MIT) and hosted free tier
Category: Resale Market Intelligence
Built by: secondhandmcp.com
```

## Why This Matters for Operators

Resale is a pricing oracle. For any product an operator sells, buys, or competes with, the secondhand market shows what consumers actually pay, how supply moves, and where the pricing floor sits. That intelligence is normally gathered by hand across four marketplaces with four search interfaces.

Secondhand MCP makes it one query: pricing comps across eBay, Poshmark, Depop, and Facebook Marketplace in a single agent session. Resellers source inventory with saved filters, brands watch their own products' secondary-market prices, and marketplaces research the competition. The deep-research `search`/`fetch` contract keeps every result traceable to its listing.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Multi-marketplace search | Search Facebook Marketplace, eBay, Depop, and Poshmark in one call |
| Filters | Price, condition, category, size, and color refinements |
| Listing detail | Full listing data: photos, descriptions, and seller information |
| Deep-research search/fetch | Traceable multi-step research with cited listing sources |
| Local or hosted | Run it yourself (MIT, npm) or use the hosted remote with OAuth |

## Installation

Local:

```bash
npx secondhand-mcp
```

Hosted remote:

```bash
claude mcp add --transport http secondhand https://secondhandmcp.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "secondhand": {
      "type": "http",
      "url": "https://secondhandmcp.com/mcp"
    }
  }
}
```

## Business Relevance

- **Resellers** source inventory across four marketplaces from one agent query
- **Brands** monitor their products' secondary-market prices for counterfeits and channel drift
- **E-commerce pricing teams** anchor new-product pricing with real transaction comps
- **Marketplace analysts** map supply, demand, and price floors by category and geography
- **Pawn and consignment operators** verify items against live comps before quoting

## Integration with CorpusIQ

Secondhand MCP answers what the market pays; CorpusIQ answers what the business makes. A reseller runs Secondhand for comps and sourcing decisions, then tracks every flip in QuickBooks and Stripe through CorpusIQ connectors, joining market intelligence to actual margin per item. The research surface is read-only on both sides, so the sourcing conversation stays separate from the ledger.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Marketplace search coverage depends on each platform's public search surface, which can change without notice
- Local server is MIT but young: expect iteration before production dependence
- Hosted remote requires OAuth sign-in; free tier limits undisclosed at listing time
- No listing, messaging, or transaction tools: this is a research surface, not a selling one

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
