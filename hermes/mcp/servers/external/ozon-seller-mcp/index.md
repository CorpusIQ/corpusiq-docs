---
title: "Ozon Seller MCP"
description: "MCP server for Ozon marketplace operations - 151 tools over the Ozon Seller API and Performance API covering prices, promotions, advertising, orders, returns, reviews and finance across multiple seller accounts. MIT, Python, stdio or SSE transport."
category: "Commerce & E-Commerce"
stars: 2
added: 2026-08-23
source: "mcpservers.org /all + GitHub README"
relevance: ★★
tags: [ozon, marketplace-ops, ecommerce, multi-seller, advertising, order-management, self-hosted]
last_updated: "2026-10-24"
---

# Ozon Seller MCP

**Run Ozon stores directly from a chat with an AI assistant - 151 tools over the Ozon Seller API and Performance API covering prices, promotions, advertising, orders, returns, reviews and finance, built for sellers who operate multiple shops.** Every call takes a `shop_id`, keys are stored encrypted on your server, and nothing leaves the machine. Unlike other Ozon MCP servers, this one also covers the advertising (Performance) API, and a built-in diagnostics layer shows which Ozon methods are broken before the assistant notices.

```
Server type: Local (stdio or SSE, Python package)
Auth: Ozon Seller API keys (Client-Id + Api-Key), stored locally
Package: pip install ozon-mcp-server (PyPI)
Tools: 151 (prices, promotions, ads, orders, returns, reviews, finance)
License: MIT, Python 3.10+
Category: Commerce & E-Commerce
Built by: DeviceIngineering (GitHub)
```

## Why This Matters for Operators

Ozon is the second-largest marketplace in Russia and a core channel for brands in the region, but its operational API surface is large and split: the Seller API for catalog and orders, the Performance API for advertising. Multi-store sellers multiply the pain - each store has its own key pair, and switching between stores mid-conversation is where manual workflows break. This server collapses that: one assistant, all stores, `shop_id` per call, keys encrypted at rest on your own machine.

The diagnostics layer is the quiet killer feature. Ozon deprecates and breaks methods periodically, and an agent that fails silently is worse than no agent. This server checks which upstream methods are broken and surfaces it before a pricing or advertising task fails mid-run. The same author ships a matching Wildberries server (`wb-mcp-server`) for sellers who trade on both marketplaces.

## Tools & Capabilities

151 tools across the major operational domains:

| Area | What it covers |
|---|---|
| Prices | Read and update product prices, price history |
| Promotions | Manage promotional campaigns and participation |
| Advertising | Performance API: campaigns, bids, budget, statistics |
| Orders | Order listing, status, shipment and fulfillment |
| Returns | Return requests and processing |
| Reviews | Review listing and response management |
| Finance | Transactions, accruals and seller reports |

The full tool reference ships in the repository at `docs/tools.md`. READMEs are published in Russian, English and Chinese.

## Installation

```bash
pip install ozon-mcp-server
```

Configure per-shop credentials (Ozon Client-Id and Api-Key pairs from the Ozon Seller Cabinet), then register the package as a stdio or SSE server with your MCP client.

## Configuration

```json
{
  "mcpServers": {
    "ozon": {
      "command": "ozon-mcp-server",
      "env": {
        "OZON_CLIENT_ID_1": "your-client-id",
        "OZON_API_KEY_1": "your-api-key"
      }
    }
  }
}
```

Keys are held encrypted on the server that runs the MCP process; `shop_id` selects the store per call.

## Business Relevance

- **Ozon sellers with multiple shops** run pricing, promotions, advertising and order ops from one chat surface instead of the Seller Cabinet.
- **Marketplace agencies** manage client stores without sharing raw API keys with AI clients.
- **Brands selling on both Ozon and Wildberries** get a matched server pair (ozon-mcp-server + wb-mcp-server) from the same maintainer.
- **Regional operators** in the RU/CIS ecommerce market get a maintained, MIT-licensed alternative to writing their own API glue.
