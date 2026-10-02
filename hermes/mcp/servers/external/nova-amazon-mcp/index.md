---
title: Nova Amazon MCP - Seller Central Profit Analytics for Agents
description: Hosted Amazon MCP connecting Seller Central, Vendor Central and Amazon Ads to Claude, ChatGPT, Gemini and Cursor. 15 tools answer net profit per SKU with your own COGS, VAT and FBM shipping costs reconciled across 40+ Amazon fee types, plus PPC, inventory, listing health and Best Seller Rank queries over 477 data points.
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-09-10
source: mcp.so feed
relevance: ★★★
tags: [amazon-seller, seller-central, vendor-central, amazon-ads, profitability, ppc, inventory, e-commerce, remote-mcp]
---

# Nova Amazon MCP

**Remote MCP server (Streamable HTTP, OAuth)** - a hosted connector from Nova Data Analytics that puts your Amazon Seller Central, Vendor Central and Amazon Ads data in front of an AI agent, with one differentiator that changes the answers: Nova also holds **your own cost data**, so the agent can answer whether an ACoS is actually profitable instead of just whether it is low.

```
Server type: Remote (hosted, Streamable HTTP)
Auth: OAuth, per seller account, revocable at any time
Endpoint: https://mcp.novadata.io/api/mcp
Coverage: 477 documented data points, 21 Amazon marketplaces, 24 months of history
Freshness: Hourly sync
```

## Why Cost Data Changes the Answers

Amazon knows your fees. It does not know what your product cost to buy, how VAT is treated in each country you sell in, or what it costs to ship an FBM order. Without those, an assistant can tell you your revenue and your ad spend, but it cannot tell you whether a given ACoS is profitable.

Nova keeps COGS, VAT treatment and FBM shipping costs alongside the Amazon data, reconciled to SKU level across 40+ Amazon fee types. That is why it can answer "which keywords have a good ACoS but a negative contribution margin" - the question that actually matters. Those cost inputs are also **readable and writable through the MCP itself**, so you can audit and fix your own cost setup inside the conversation.

## Tools

| Tool | What it returns |
|---|---|
| `query_metrics` | Any metric over any period, grouped by SKU, ASIN, marketplace, account or time grain |
| `find_movers` | Biggest gainers and losers for a metric against a baseline period |
| `explain_movement` | Causal signals behind one SKU's move: traffic, conversion, price, buy box, ads, rank |
| `query_advertising` | Sponsored Products at campaign, ad group, targeting, keyword, ASIN or SKU grain |
| `query_search_terms` | Customer search queries behind ad spend, for negatives and discovery |
| `query_sqp` | Search Query Performance: impression, click and purchase share by query |
| `query_inventory` | FBA and AWD stock health, velocity, days of cover, out of stock risk |
| `query_listing_health` | Suppressed, not buyable, buy box lost, hijackers, catalog content |
| `query_bsr` | Best Seller Rank for your own ASINs, latest or as a time series |
| `list_cost_inputs` | Configured per SKU COGS, FBM cost and VAT category, for setup audits |
| `import_cogs`, `import_fbm_costs`, `import_vat_categories` | Maintain cost inputs conversationally, with a diff shown before commit |
| `list_metrics`, `describe_metric` | Metric catalogue and definitions |
| `list_accounts`, `list_tags` | Seller accounts and custom product filters |

## Example Questions

- **Profit:** "Show me profit by SKU for the last 30 days after PPC." "Which SKUs lost the most net profit versus last month, and why?" "What is my true TACoS by ASIN this quarter?"
- **Advertising:** "Which campaigns spent over $100 last week with zero orders?" "Find search terms with ACoS under 25% and at least 3 orders."
- **Inventory:** "What runs out of stock in the next three weeks across all marketplaces?" "Which SKUs are sitting on more than 120 days of cover?"
- **Listings:** "Which listings are suppressed or losing the buy box right now?"

## Connection

```
{ "mcpServers": { "nova": { "url": "https://mcp.novadata.io/api/mcp" } } }
```

Claude Code: `claude mcp add --transport http nova https://mcp.novadata.io/api/mcp`. Claude Desktop/web, ChatGPT and Gemini all accept the same URL as a custom/remote connector. You need a Nova account with Seller Central connected and at least one completed sync. Prompt library and setup notes: [github.com/nova-data-analytics/nova-amazon-mcp](https://github.com/nova-data-analytics/nova-amazon-mcp).

## Security

- OAuth against Nova. No Amazon password is ever shared with the MCP server.
- Credentials are per seller account and revocable at any time from Nova.
- The endpoint answers unauthenticated requests with a standard OAuth challenge and protected-resource metadata.

## Pricing

Commercial. Plans start at $29 per month with a 14-day free trial, no card required. The MCP server is included.

## Verification (Sep 10, 2026 night sweep)

Endpoint `https://mcp.novadata.io/api/mcp` live-probed over JSON-RPC: anonymous initialize rejected with HTTP 401 "Authentication required" - live, OAuth-gated endpoint. Full tool table, coverage matrix and pricing published on the listing and product pages.

## See Also

- [AMZ Vault MCP - Amazon Seller Central and Ads for Agents](/hermes/mcp/servers/external/amz-vault-mcp)
- [Kuudo Amazon MCP Suite - Selling Partner and Vendor Central Operations](/hermes/mcp/servers/external/amazon-kuudo-mcp-suite)
- [SellerMate MCP - Amazon Ads Operations for AI Agents](/hermes/mcp/servers/external/sellermate-mcp)
- [Shop MCP - Read-Only Shopify Catalogue and Stock](/hermes/mcp/servers/external/shop-mcp)
