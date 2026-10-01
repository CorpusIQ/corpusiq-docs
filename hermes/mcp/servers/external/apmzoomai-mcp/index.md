---
title: apMZoomAI MCP - Dongdaemun Wholesale Search
description: "Free read-only MCP server for searching Seoul's Dongdaemun wholesale fashion market, with items, new arrivals and stalls in eight languages."
category: Commerce & E-Commerce
stars: n/a (hosted service, apmzoom.com)
added: 2026-10-01
source: "mcpservers.org /all (apmleokeo-gif/apmzoom-mcp)"
relevance: ★★
tags: [wholesale, fashion, sourcing, ecommerce, suppliers, dongdaemun, remote-mcp]
---

# apMZoomAI MCP

**Search a wholesale fashion market from inside an agent.** apMZoomAI exposes the Dongdaemun market in Seoul over MCP: items listed by stalls, the newest arrivals, and stalls located by building and floor. It is public, read-only and multilingual, which makes it usable as a sourcing front end for an operator buying from the market.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: None (public, read-only)
Endpoint: https://www.apmzoom.com/mcp
Tools: 5 (search, arrivals, stalls, product, buildings)
Pricing: free
Category: Commerce & E-Commerce
Built by: apMZoomAI
```

## Why This Matters for Operators

Sourcing from a foreign wholesale market usually means a buying agent, a chat app, or a spreadsheet of stall numbers. This server turns the catalogue into a query: an agent can search items by short keyword, pull new arrivals from the last few hours, and locate a stall by building, floor and stall number, then return a link that opens the item on apMZoomAI.

The multilingual layer is the practical part. Queries are accepted in English, Korean, Chinese, Japanese, Vietnamese, Thai, Indonesian and Malay, and results come back in the language the caller asks for. For an operator or agent working in one language against a market that trades in another, that removes the translation step without a separate tool.

Prices are deliberately not returned through the tools; the buyer opens the item link to see price and wholesale ordering details. That keeps the server a discovery surface rather than a checkout, which is the right shape for a sourcing workflow where terms are negotiated.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_products` | Search wholesale items by short keyword in any supported language, with photos, category and stall location |
| `get_new_arrivals` | List the newest items uploaded in the last 1 to 168 hours, filterable by building and category |
| `find_stalls` | Find stalls by name or stall number, or by building and floor, with item counts and store pages |
| `get_product` | Get one item by id: name, up to three photos, category, stall location and link |
| `list_buildings` | List the market buildings covered, with stall counts |

## Installation

```
claude mcp add --transport http apmzoom https://www.apmzoom.com/mcp
```

The server is stateless and returns JSON responses, so no session or key is required. Any client that speaks Streamable HTTP can connect with the URL alone.

## Configuration

```json
{
  "mcpServers": {
    "apmzoom": {
      "type": "http",
      "url": "https://www.apmzoom.com/mcp"
    }
  }
}
```

## Business Relevance

- **E-commerce and DTC operators** can watch new arrivals from the market as a leading signal of what will appear in retail catalogues weeks later.
- **Buyers and sourcing agents** can search items, locate the stall behind each, and open the item link to see price and ordering terms.
- **Category and trend researchers** can filter arrivals by building and category to see what one part of the market is pushing.
- **Agents working across languages** can query in one language and return results in another without a translation detour.

## Integration with CorpusIQ

For an operator tracking an e-commerce business, apMZoomAI is the supply-side signal and CorpusIQ is the demand side. An agent can pull sales, inventory and customer data through CorpusIQ's Shopify and e-commerce connectors, then check what the Dongdaemun market is listing through this server, so a product decision is made with both the store's numbers and the source market's new arrivals in view. That pairing is useful for assortment planning, where the market's freshest items and the store's own sell-through are read together.

## Limitations

- Public and read-only, but limited to the Dongdaemun market and the stalls currently in business.
- Prices are not available through the tools; the buyer opens the item link for price and ordering details.
- Item results are capped at 20 per search, so broad categories need repeated queries.
- A focused sourcing surface rather than a full marketplace API, with no ordering or payment operations.

## FAQ

### What does the apMZoomAI MCP server do?

It lets an AI agent search the Dongdaemun wholesale fashion market in Seoul, returning items, new arrivals and stalls with links to open each on apMZoomAI.

### Is the apMZoomAI MCP server free?

Yes. It is a public, read-only server with no authentication and no API key.

### Which languages does it support?

English, Korean, Chinese, Japanese, Vietnamese, Thai, Indonesian and Malay, both for queries and for returned item names and labels.

### Can it return prices?

No. Prices are not exposed through the tools; the buyer opens the item link to see price and wholesale ordering details.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ](https://corpusiq.io) - 40+ business data connectors for AI agents
