---
title: "marketplaces-mcp-ru - Russian Marketplace Seller Operations for Agents"
description: "marketplaces-mcp-ru connects an AI assistant to seller accounts on Wildberries, Ozon, Yandex Market and Avito through the official Seller APIs: sales, stocks, prices, finance, reviews and ads via 793 schema-driven methods exposed through generic search, describe and call tools plus typed convenience tools and seller workflows. Stdio, MIT."
category: Commerce & E-Commerce
stars: 25
added: 2026-09-07
source: "chatmcp/mcpso issue #3978"
relevance: ★★★
tags: [ecommerce, wildberries, ozon, yandex-market, avito, seller-api, stdio, russia]
---

# marketplaces-mcp-ru - Russian Marketplace Seller Operations for Agents

**Local stdio MCP server (Python, PyPI; Docker; optional Streamable HTTP)** - marketplaces-mcp-ru connects an agent to a seller's Wildberries, Ozon, Yandex Market and Avito accounts through the official Seller APIs. Every method is classified read, write or destructive, and writes require explicit confirmation before anything changes in the store.

```
Server type: Local (stdio via uvx marketplaces-mcp-ru; Docker ghcr.io/ilyautov/marketplaces-mcp-ru; HTTP with MCP_TRANSPORT=http)
Auth: Per-store API tokens held locally (~/.marketplace-mcp/cabinets.json)
Tools: 793 schema-driven methods (WB 307, Ozon Seller 441, Ozon Performance 45, plus Yandex Market and Avito) via generic and typed tools
Pricing: Free software
Category: Commerce & E-Commerce
Built by: Ilya Utov (github.com/ilyautov/marketplaces-mcp-ru)
```

## Why This Matters for Operators

Russian marketplaces are the region's e-commerce backbone, and sellers manage several cabinets at once with different API generations per platform. marketplaces-mcp-ru normalizes all four into one MCP surface with a deliberate safety model: generic search, describe and call tools expose the full schema, typed convenience tools cover the daily motions, and step-by-step seller workflows (reorder planner, ABC analysis, reviews pulse) package multi-step operations.

**The confirmation gate is the trust anchor: every method is classified read, write or destructive, and writes require explicit confirmation before anything changes in the store - the same staged-write posture as the AMZ Vault and Wildberries precedents.**

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Generic surface | search, describe and call tools reach all 793 schema-driven methods |
| Typed Wildberries tools | wb_get_sales, wb_get_stocks and the WB convenience set |
| Typed Ozon tools | ozon_get_products, ozon_get_prices plus Ozon Performance tools |
| Yandex Market and Avito | ym_get_orders, ym_set_price, avito_get_orders, avito_update_stock and siblings |
| Seller workflows | Reorder planner, ABC analysis, reviews pulse as step-by-step operations |

## Installation

```bash
uvx marketplaces-mcp-ru
```

## Configuration

```json
{
  "mcpServers": {
    "marketplaces-ru": {
      "command": "uvx",
      "args": ["marketplaces-mcp-ru"],
      "env": {
        "WB_API_TOKEN": "your_wb_token",
        "OZON_CLIENT_ID": "your_ozon_client",
        "OZON_API_KEY": "your_ozon_key"
      }
    }
  }
}
```

Keys stay local in ~/.marketplace-mcp/cabinets.json, and several stores can be switched from chat. Russian and English documentation are both published.

## Business Relevance

- **Marketplace sellers** manage WB, Ozon, Yandex Market and Avito cabinets from one agent.
- **E-commerce agencies** run reorder planning and ABC analysis across client stores.
- **Finance teams** pull sales and finance reports per platform without portal logins.
- **Developers** use the Docker image for self-hosted HTTP deployments.

## Integration with CorpusIQ

marketplaces-mcp-ru reads the marketplace layer; CorpusIQ consolidates it with the rest of the business. A composed workflow: the agent pulls Wildberries and Ozon sales through marketplaces-mcp-ru, then merges them with Stripe and Shopify revenue in CorpusIQ for a single P&L view across channels.

## Limitations

- Brand new to this catalog (issue #3978, Sep 7, 2026); 25-star repo, MIT, PyPI 0.5.2 verified.
- Russian-marketplace scope; schema coverage depends on each platform's Seller API generation.
- Stdio-first; HTTP mode requires MCP_TRANSPORT=http and self-hosting.
- Write operations require per-operation confirmation, which slows bulk mutations by design.

## See Also

- [Wildberries MCP Server - Seller API Operations for Agents](/docs/hermes/mcp/servers/external/wb-mcp-server)
- [Ozon MCP Server - Marketplace Seller Operations for Agents](/docs/hermes/mcp/servers/external/ozon-mcp-server)
- [Walmart Marketplace MCP - 234 Marketplace Operations via Spec-Driven Discovery](/docs/hermes/mcp/servers/external/walmart-marketplace-mcp)
- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
