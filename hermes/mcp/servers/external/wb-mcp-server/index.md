---
title: Wildberries MCP Server - Seller API Operations for Agents
description: Self-hosted MCP server for the Wildberries Seller API with 197 tools covering product cards, prices, promotions, ads, orders, supplies, reviews, returns, finance and analytics. Multi-store with Fernet-encrypted tokens, a web dashboard, self-diagnostics that ping every WB host, and measured context budgeting documented with real corpus numbers.
category: Commerce & E-Commerce
stars: 3
added: 2026-09-04
source: "mcp.so GitHub issue #3920"
relevance: ★★
tags: [wildberries, marketplace, e-commerce, seller-api, russia, stdio, self-hosted, multi-store]
---

# Wildberries MCP Server

**Self-hosted MCP server (stdio or Docker with SSE)** - the complete Wildberries Seller API (Russia's largest marketplace) as 197 agent tools: product cards, prices, promotions, ads, orders, supplies, reviews, returns, finance and analytics. Sibling of the Ozon server from the same vendor, sharing the multi-store, encryption and context-budgeting architecture.

```
Server type: Self-hosted (uvx wb-mcp-server for stdio, Docker SSE on port 8001)
Auth: WB Client-Id + API key per store; optional MCP_AUTH_TOKEN protects the SSE endpoint
Tools: 197 (PyPI v2.6.0, MIT)
Registry: io.github.DeviceIngineering/wb-mcp-server
Repo: DeviceIngineering/wb-mcp-server
```

## Why This Matters for Operators

Wildberries dominates Russian e-commerce volume, and its seller workflow is heavily operational: card management, tariff and commission changes, supply planning and review handling at scale. This server makes that surface agent-operable. **An agent can reprice a card, check WB's own tariff and commission references, watch finance reports and respond to reviews without the operator navigating the seller console.**

The same context engineering as the Ozon sibling applies: a corpus of 27 live responses went from 770,506 to 74,947 tokens after field presets, truncation signals and size guards - with one commission-reference call alone measured at 881,232 tokens before the guards. Tool names carry the measurement (wb_tariffs_commission, wb_finance_report), so agents can predict which calls are expensive.

## Tools & Capabilities

Representative tool families (197 total, grouped by domain):

| Family | Coverage |
|---|---|
| `wb_cards_list` / card tools | Product cards, card lifecycle, content |
| Pricing and promotion tools | Current prices, promos, discount campaigns |
| `wb_advert_list` | Advertising campaigns and budgets |
| `wb_fbw_*` | FBW fulfillment and supply operations |
| `wb_finance_report` | Financial reports and reconciliation |
| `wb_tariffs_commission` | WB tariff and commission references |
| `wb_degradations` / `wb_diagnostics` | Self-diagnostics per WB host |
| `wb_token_info` | Token and store status |

Use `WB_TOOLSETS` to trim the catalogue for clients without tool search.

## Installation

```bash
uvx wb-mcp-server            # stdio
# or Docker with the dashboard and SSE on port 8001
```

Configure store credentials via environment variables (WB Client-Id and API key, same pattern as the Ozon sibling). Multi-store setups add stores in the dashboard at `http://localhost:8001/`.

## Configuration

```json
{
  "mcpServers": {
    "wildberries": {
      "command": "uvx",
      "args": ["wb-mcp-server"]
    }
  }
}
```

Docker deployments should set `MCP_AUTH_TOKEN` (generate with `openssl rand -hex 32`) to protect the SSE endpoint and dashboard. Tokens are Fernet-encrypted at rest with the key in `DATA_DIR/.encryption_key`; the dashboard flags tools that move real money.

## Business Relevance

- **Wildberries sellers** run cards, prices, supplies and reviews from an agent workflow.
- **Multi-store operators** manage WB and Ozon shops side by side with one dashboard pattern.
- **Finance teams** pull WB financial reports and tariff references into reconciliation.
- **Integration engineers** get per-host diagnostics when WB changes its API.

## Integration with CorpusIQ

Pairs with the Ozon sibling for the full Russian marketplace stack. CorpusIQ aggregates the operator's cross-marketplace financial picture from its own connectors while these servers handle the platform-specific seller operations CorpusIQ does not connect - a clean complement for sellers active in both markets.

## Limitations

- Self-hosted: operator responsibility for credentials, updates and security.
- Russia-focused marketplace; cross-border sellers carry currency, logistics and compliance constraints outside the server's scope.
- 197 tools is an even wider surface than the Ozon sibling - trim with `WB_TOOLSETS`; write tools change live marketplace state.
- Young project (3 stars) with a small but active maintainer.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Ozon MCP Server - Marketplace Seller Operations for Agents](/docs/hermes/mcp/servers/external/ozon-mcp-server)
- [SellerMate MCP - Amazon Ads Operations for AI Agents](/docs/hermes/mcp/servers/external/sellermate-mcp)
- [Neonjelly MCP - Shopify Store Intelligence for Agents](/docs/hermes/mcp/servers/external/neonjelly-mcp)
