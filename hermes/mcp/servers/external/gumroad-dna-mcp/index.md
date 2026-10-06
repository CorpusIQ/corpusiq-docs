---
title: "GumroadDNA MCP - Gumroad Store Operations"
description: "44 tools over the Gumroad API from chat: products, files, sales, refunds, licenses, subscribers, offer codes and niche scans - local, MIT."
category: Commerce & E-Commerce
stars: n/a (local server, MIT)
added: 2026-10-05
source: "chatmcp/mcpso issues (#4791)"
relevance: ★★
tags: [gumroad, ecommerce, creators, products, sales, license-keys, stdio, self-hosted, mit]
---

# GumroadDNA MCP

**A creator storefront, operated from the conversation.** GumroadDNA puts the Gumroad API v2 behind 44 tools so an assistant can run a Gumroad store end to end: create a product (file, cover, thumbnail, publish), manage images and stock, read and refund sales, resend receipts, manage license keys, offer codes, custom fields and webhooks, and pull a today, week and month revenue snapshot. It also reads the public Gumroad storefront for any keyword - how many products, the price spread, top sellers - so a niche can be sized before entering it.

```
Server type: Local (stdio, Python 3.10+; optional HTTP via PORT)
Auth: Your own Gumroad access token (GUMROAD_ACCESS_TOKEN)
Install: git clone the repository, pip install -r requirements.txt
License: MIT
Built by: VibeDNA
```

## Why This Matters for Operators

Gumroad is where a lot of small software, ebooks and courses get sold, and its dashboard is where creators lose evenings. This server moves the routine operations into the agent: restocking a product file, refunding an order, resending a receipt, checking which license keys are still valid, creating an offer code for a launch. The niche scan adds the market side: point it at a keyword and it reads the public storefront for product counts, price spread and top sellers by rating count, with no token needed at all.

**Writes act on your live store, so the workflow stays deliberate.** The vendor's guidance is that the AI client asks before calling a write tool unless you have allowed it; destructive tools like `refund_sale` and `archive_product` are labeled as such. For a store measured in evenings, that is the right shape: everything reachable, nothing silent.

## Tools

44 tools across eleven areas:

| Area | Tools |
|---|---|
| Market research | `scan_gumroad_niche` (public storefront, no token needed) |
| Products | `create_product`, `launch_product`, `update_product`, `publish_product`, `archive_product`, `list_products`, `download_product_files` |
| Files and images | `add_product_file`, `set_product_cover`, `add_product_image`, `list_product_images`, `remove_product_image`, `reorder_product_images`, `download_product_images` |
| Sales | `get_revenue_snapshot`, `list_sales`, `get_sale`, `refund_sale`, `resend_receipt`, `mark_as_shipped` |
| Subscribers | `list_subscribers`, `get_subscriber` |
| License keys | `verify_license`, `enable_license`, `disable_license`, `decrement_license_uses` |
| Discounts and checkout | `list_offer_codes`, `create_offer_code`, `delete_offer_code`, `list_custom_fields`, `create_custom_field`, `delete_custom_field` |
| Stock | `get_stock_status`, `update_stock`, `bump_stock` |
| Webhooks | `list_webhooks`, `create_webhook`, `delete_webhook` |
| Extras | `scan_unlisted_assets`, `sync_buyers_to_resend` |
| Account and meta | `get_account`, `vibedna_info`, `check_for_update` |

## Installation

Get an access token from Gumroad under Settings, Advanced, Applications. Then:

```bash
git clone https://github.com/marstudio360/gumroad-dna-mcp
cd gumroad-dna-mcp
pip install -r requirements.txt
claude mcp add gumroad-dna --scope user \
  -e GUMROAD_ACCESS_TOKEN=your_token \
  -- python /absolute/path/to/gumroad-dna-mcp/server.py
```

JSON clients use the same shape:

```json
{
  "mcpServers": {
    "gumroad-dna": {
      "command": "python",
      "args": ["/absolute/path/to/gumroad-dna-mcp/server.py"],
      "env": { "GUMROAD_ACCESS_TOKEN": "your_token" }
    }
  }
}
```

The token can live in the MCP entry or in a .env file next to server.py. The repository ships an INSTALL.md written to be pasted into an AI chat and installed by the assistant itself.

## Business Relevance

- **Indie sellers and creators** restock files, launch products and answer revenue questions without opening the Gumroad dashboard.
- **Small teams** handle refunds, receipts and shipped orders from wherever the conversation happens.
- **Software sellers** check, enable and disable license keys from the same chat that answers support.
- **Anyone validating a niche** reads the public storefront for counts, price spread and top sellers before building.

## Integration with CorpusIQ

The store is one revenue surface among several. GumroadDNA answers what sold on Gumroad and what the store looks like; CorpusIQ reads the surrounding picture from Stripe, GA4, the ad platforms and 40+ connectors. An operator can compare how a launch performed on the store against where the traffic came from, both pulled read-only at answer time - and unlike the read-only connectors, decide for themselves when to let the agent act on the store through the Gumroad tools.

## Limitations

- Local install: it runs on your machine over stdio; there is no hosted endpoint.
- Write tools act on the live store immediately; destructive ones are labeled and should keep the client's confirmation step on.
- A Gumroad access token is required for everything except the public niche scan; token custody is yours.
- Scoped to Gumroad only; other storefronts need their own connectors.
- The niche scan reads the public storefront surface, not Gumroad's internal analytics.

## FAQ

### Do I need a paid Gumroad plan?

No. The server works with a standard Gumroad access token; the same API surfaces apply across plans, and the niche scan needs only public storefront data.

### Can an agent create and publish a product end to end?

Yes: `create_product` plus file, cover and thumbnail tools, then `publish_product`. The client asks before writes unless you have allowed them.

### What is the niche scan?

`scan_gumroad_niche` reads the public Gumroad storefront for a keyword and returns how many products exist, the price spread, and top sellers by rating count - useful before committing to a product idea.

### Where does it run?

Locally over stdio with Python 3.10+, from the MIT-licensed repository. Setting the PORT variable serves it over streamable HTTP instead, for clients that need that.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Shop MCP - Read-Only Shopify Catalogue and Stock](/hermes/mcp/servers/external/shop-mcp/)
- [Ozon MCP Server - Marketplace Seller Operations for Agents](/hermes/mcp/servers/external/ozon-mcp-server/)
- [ShopSynch MCP - E-Commerce Operations for AI Agents](/hermes/mcp/servers/external/shopsynch-mcp/)
