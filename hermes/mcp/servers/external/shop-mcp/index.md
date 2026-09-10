---
title: Shop MCP - Read-Only Shopify Catalogue and Stock
description: One-file stdlib-only MCP server that gives an agent read-only access to a Shopify store's catalogue and stock levels, answering what a store sells and what is about to run out without any write access.
category: Commerce & E-Commerce
stars: 0
added: 2026-09-10
source: "chatmcp/mcpso issue #4030"
relevance: ★★★
tags: [shopify, ecommerce, inventory, catalogue, read-only, stdio, python]
---

# Shop MCP

**Ask "what do we sell and what's about to run out" without giving the agent write access** - a single Python file, standard library only, no MCP SDK and no HTTP client, so the entire surface can be read before it is run. Four read-only tools over the Shopify Admin API using only the read_products and read_inventory scopes. Nothing in this server writes.

```
Server type: stdio (Python, uvx shop-mcp)
Auth: SHOPIFY_SHOP_DOMAIN + SHOPIFY_ADMIN_TOKEN (read_products, read_inventory scopes only)
Registry: io.github.hello532/shop-mcp 1.0.1 (Official MCP Registry, active)
License: MIT
Tools: 4, all read-only
Built by: hello532 (glama.ai scored: license A, quality A, maintenance B)
```

## Why This Matters for Operators

Most Shopify agents want the power to change orders, prices and products - which is exactly why operators are nervous about connecting one. **Shop MCP inverts the risk**: it cannot write, by construction. The toolset answers the two questions an operator actually asks an assistant daily - what do we sell, and what stock is running low - while a token compromise is limited to reading catalogue data. A deliberate design choice helps debugging too: with no credentials the server still completes the MCP handshake and serves tools/list, and only tools/call fails naming what to set, instead of the host reporting a broken server.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_products` | Query the catalogue by text |
| `get_product` | One product by id or handle |
| `check_inventory` | Stock by SKU, per location |
| `low_stock_report` | Restocking report for low-stock items |

## Installation

```bash
uvx shop-mcp
```

One Python file, standard library only - no MCP SDK, no GraphQL client dependency, no HTTP client library beyond urllib. The package ships with self-test assertions covering the tool surface.

## Configuration

```json
{
  "mcpServers": {
    "shop": {
      "command": "uvx",
      "args": ["shop-mcp"],
      "env": {
        "SHOPIFY_SHOP_DOMAIN": "your-shop.myshopify.com",
        "SHOPIFY_ADMIN_TOKEN": "shpat_..."
      }
    }
  }
}
```

Create the admin token in the Shopify admin with only the read_products and read_inventory scopes granted - the server needs nothing else and cannot use anything else.
