---
title: Ozon MCP Server - Marketplace Seller Operations for Agents
description: Self-hosted MCP server for the Ozon Seller and Performance API with 158 tools covering products, prices, promotions, ads, orders (FBS/FBO), returns, reviews, finance and analytics. Multi-store support with Fernet-encrypted tokens, a web dashboard, built-in self-diagnostics, and measured context budgeting to keep tool responses within model windows.
category: Commerce & E-Commerce
stars: 4
added: 2026-09-04
source: "mcp.so GitHub issue #3921"
relevance: ★★
tags: [ozon, marketplace, e-commerce, seller-api, russia, stdio, self-hosted, multi-store]
---

# Ozon MCP Server

**Self-hosted MCP server (stdio or Docker with SSE)** - the full Ozon Seller and Performance API surface (Russia's largest marketplace) exposed as 158 agent tools: products, prices, promotions, ads, orders, returns, reviews, finance and analytics. Multi-store, with tokens encrypted at rest and a web dashboard showing every call.

```
Server type: Self-hosted (uvx ozon-mcp-server for stdio, Docker SSE on port 8000)
Auth: Ozon Client-Id + API key per store; optional MCP_AUTH_TOKEN protects the SSE endpoint
Tools: 158 (PyPI v2.5.0, MIT)
Registry: io.github.DeviceIngineering/ozon-mcp-server
Repo: DeviceIngineering/ozon-mcp-server
```

## Why This Matters for Operators

Ozon sellers run their marketplace business from a dashboard built for humans - hundreds of screens for prices, stock, orders and campaigns. This server makes the same surface agent-operable, which matters because Ozon catalog and pricing operations are volume operations: repricing hundreds of SKUs, syncing stock across warehouses, reading finance accruals. **An agent holding this toolset can watch margins, reprice against the category tree and reconcile FBO returns without exporting a single CSV.**

The engineering discipline is the trust signal: tokens are Fernet-encrypted at rest, the bundled scripts measure real response sizes (a live corpus went from 476,158 to 63,845 tokens after server-side field presets and truncation), and self-diagnostics ping every Ozon host to flag degraded tools after API changes - the failure mode that silently breaks marketplace integrations.

## Tools & Capabilities

Representative tool families (158 total, grouped by domain):

| Family | Coverage |
|---|---|
| `ozon_get_prices` / pricing tools | Current prices, price history, repricing inputs |
| `ozon_product_*` | Product cards, attributes, category tree (`ozon_category_tree`), stock by warehouse |
| `ozon_returns_fbo` | FBO/FBS returns and return status |
| `ozon_finance_*` | Finance accruals, cash flow, transaction reports |
| `ozon_analytics` | Sales and performance analytics |
| `ozon_degradations` / `ozon_diagnostics` | Self-diagnostics: which tools degraded after an Ozon API change |
| `ozon_warehouse_list` | Warehouse and fulfillment mapping |

Use `OZON_TOOLSETS` to trim the catalogue for clients without tool search.

## Installation

```bash
uvx ozon-mcp-server          # stdio
# or Docker with the dashboard and SSE on port 8000
```

Configure store credentials via environment: `OZON_CLIENT_ID` and `OZON_API_KEY` per store. Multi-store setups add stores in the dashboard (browser-based, dashboard at `http://localhost:8000/`).

## Configuration

```json
{
  "mcpServers": {
    "ozon": {
      "command": "uvx",
      "args": ["ozon-mcp-server"],
      "env": {
        "OZON_CLIENT_ID": "your Client-Id",
        "OZON_API_KEY": "your API key"
      }
    }
  }
}
```

For the Docker deployment, generate a bearer token with `openssl rand -hex 32` and set it as `MCP_AUTH_TOKEN` - it protects the `/sse` endpoint and the dashboard. An empty `MCP_AUTH_TOKEN` means no authentication, acceptable only on a private network. On first use a Fernet key is created in `DATA_DIR`; the dashboard shows encrypted tokens with a red banner when any tool that moves real money is called.

## Business Relevance

- **Ozon sellers** run pricing, stock and order operations from an agent instead of the web console.
- **Multi-store operators** manage several shops from one dashboard with per-store credentials.
- **Analytics teams** pull finance accruals and performance data directly into agent workflows.
- **Integration engineers** get degradation alerts when Ozon changes its API, before reports silently break.

## Integration with CorpusIQ

CorpusIQ's marketplace connectors cover Western platforms; this server covers the Russian marketplace stack operators selling into that market need. A CorpusIQ agent managing a multi-marketplace seller can hold Ozon operations in this toolset while CorpusIQ reconciles the aggregated financial picture across all platforms.

## Limitations

- Self-hosted: the operator runs the server, manages credentials and keeps it updated.
- Ozon is a Russia-focused marketplace; cross-border sellers face currency, logistics and sanctions-compliance constraints the server does not address.
- 158 tools is a wide surface - use `OZON_TOOLSETS` trimming; write tools move real marketplace state.
- Small community (4 stars); PyPI releases are regular but the project is young.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Wildberries MCP Server - Seller API Operations for Agents](/docs/hermes/mcp/servers/external/wb-mcp-server)
- [SellerMate MCP - Amazon Ads Operations for AI Agents](/docs/hermes/mcp/servers/external/sellermate-mcp)
- [Neonjelly MCP - Shopify Store Intelligence for Agents](/docs/hermes/mcp/servers/external/neonjelly-mcp)
