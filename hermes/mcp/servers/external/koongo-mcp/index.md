---
title: Koongo MCP - Product Feed and Marketplace Operations
description: Manage product feeds, marketplace listings and orders across 500+ sales channels in plain language - attribute mapping, category mapping, enrichment and feed export with confirmation gates.
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★★
tags: [ecommerce, product-feeds, marketplaces, amazon, ebay, feed-management, remote-mcp]
last_updated: "2026-10-24"
---

# Koongo MCP

**Remote MCP server (Streamable HTTP, OAuth)** - run a Koongo account by chatting instead of clicking. Koongo connects online merchants' product catalogues to 500+ sales channels through product feed management and marketplace integration; the MCP surface lets an agent inspect projects, build integrations, map attributes and categories, enrich products, export feeds and track marketplace orders in plain language.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (or personal token)
Endpoint: https://mcp.koongo.com/mcp
Tools: Feed, marketplace, enrichment and order operations (live list served from the endpoint)
Pricing: Koongo account plans; MCP included
Category: Commerce & E-Commerce
Built by: Koongo.com
```

## Why This Matters for Operators

Feed management is the unglamorous tax of multi-channel commerce. Every marketplace wants a different attribute mapping, a different category tree and a different export schedule, and agencies managing dozens of channels burn their days clicking through wizards.

Koongo MCP moves all of that into conversation, with safety built into the model: **anything that would publish products to a live channel is protected by a confirmation step, and you can set MANUAL mode to dry-run a single product before releasing the rest.** The agent shows each step before it commits.

## Tools & Capabilities

| Area | What the tools do |
|---|---|
| Projects and feeds | Browse and inspect projects, feeds, marketplaces and ads |
| Channel integrations | Create and configure Google Shopping, Amazon, eBay, Kaufland, Bol, Zalando, Cdiscount and more via step-by-step wizards |
| Attribute mapping | Map channel output attributes to store fields, fixed values or rules |
| Category mapping | Map store categories to each channel's category tree |
| Product enrichment | Add AI-derived attributes like colour, material or size and reuse them across feeds |
| Feed operations | Build, filter, verify and export product feeds |
| Orders | Track and manage marketplace orders and order connections |

The listing page does not publish a static tool list; the live tool list is served from the endpoint after OAuth, and the capability table above is drawn from the vendor's published MCP documentation.

## Installation

```bash
claude mcp add koongo-mcp --transport http https://mcp.koongo.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "koongo-mcp": {
      "type": "http",
      "url": "https://mcp.koongo.com/mcp"
    }
  }
}
```

You sign in with your own Koongo account via OAuth, or use a personal token. The agent only ever acts on the projects your account can access.

## Business Relevance

- **Multi-channel merchants** manage 500+ channels of listings from one conversational surface
- **E-commerce agencies** configure client integrations, mappings and feeds without clicking through wizards
- **Catalog teams** enrich products with AI-derived attributes once and reuse them across every feed
- **Order operations** track marketplace orders without leaving the assistant

## Integration with CorpusIQ

Koongo covers the marketplace-operations side of commerce; CorpusIQ covers the money and the storefront. Composed, an agent can build a feed export in Koongo for a new Amazon channel while CorpusIQ's Shopify connector supplies the product catalogue ground truth and Stripe confirms which SKUs actually sell. For an operator optimizing channels, the loop is concrete: Koongo publishes the listings, CorpusIQ reads the resulting revenue and ad spend, and the agent re-maps attributes for the channels that underperform.

## Limitations

- Brand new MCP surface with no published static tool reference yet
- Requires a Koongo account; MCP is an interface to that platform, not a standalone data source
- Publishing is confirmation-gated by design, which slows bulk operations
- Value is concentrated for merchants already selling through Koongo
