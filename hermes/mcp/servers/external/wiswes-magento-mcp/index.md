---
title: WisWes Magento MCP
description: Magento 2 store operations over MCP — catalog, cart, checkout, customer, sales and wishlist tools served from the store's own web server, powering an AI shopping assistant.
category: Commerce
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [magento, ecommerce, shopping-assistant, catalog-search, cart, storefront, php, self-hosted]
---

# WisWes Magento MCP

**Magento 2 module (self-hosted endpoint, shared-secret auth)** — the official WisWes module plugs a Magento 2 store into the WisWes AI shopping assistant over the Model Context Protocol: a stateless MCP HTTP endpoint at `/mcp` served through the store's own web server, 22 typed tools across catalog, cart, checkout, customer, sales, and wishlist, and a nightly catalogue push to a vector index for semantic product search.

```
Server type: Magento 2 module (stateless MCP HTTP endpoint on your web server)
Auth: shared install secret (minted by one-click admin handshake), plus customer/admin bearer scoping
Endpoint: https://<your-magento>/mcp
Tools: 22 (catalog, cart, checkout, customer, sales, wishlist)
Pricing: free module (GPL-3.0); WisWes assistant service per wiswes.com
Category: Commerce
Built by: WisWes (wiswes.com) — composer package wiswes/magento-mcp, v1.0.7
```

## Why This Matters for Operators

Most commerce AI demos stop at search. WisWes goes to the transaction: the Wes chat persona on the storefront can read live Magento data and act on the cart with no glue code. Shoppers ask questions in natural language, the assistant calls the right tool against the live store, and the store ships more orders.

**The endpoint is your own web server**: there is no separate process to manage, no third-party middleware holding a database copy, and the shared secret is minted server-to-server through an admin handshake the merchant never sees in the browser. Auth is tiered — catalog tools need only the install secret, cart and customer tools additionally forward the shopper's customer token, and order updates require customer (own orders) or admin (any order) context — so anonymous shoppers can browse but cannot read a cart until they sign in.

The nightly incremental push sends only enabled, visible products to the WisWes vector index in batches of 100, with a compact retrieval payload the LLM sees verbatim when a result matches.

## Tools & Capabilities

| Group | Purpose |
|---|---|
| Catalog | Product search, filtering, details, categories in public storefront context |
| Cart | Build and modify a real cart against the live store |
| Checkout | Checkout operations for signed-in shoppers |
| Customer | Customer account reads for identified chats |
| Sales | Order status and order updates (own orders or admin) |
| Wishlist | Wishlist operations for identified shoppers |

## Installation

```bash
composer require wiswes/magento-mcp:^1.0
bin/magento module:enable WisWes_MCP
bin/magento setup:upgrade
bin/magento setup:di:compile
bin/magento cache:flush
```

Then complete the one-click handshake: Stores → Configuration → WisWes Chat → WisWes Chat MCP → Connection, and install the widget from the WisWes Chat Widget section. Tested on Magento 2.4.4 through 2.4.7, PHP 8.1 to 8.4.

## Configuration

The MCP route is live once `setup:upgrade` runs. Verify with a tools-list call:

```bash
curl -X POST https://<your-magento>/mcp \
     -H 'Authorization: Bearer <your-shared-secret>' \
     -H 'Content-Type: application/json' \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Business Relevance

- **Magento merchants** get an AI shopping assistant reading their live catalog and acting on carts
- **E-commerce operators** get semantic product search over a nightly-synced vector index without building one
- **Developers** get a typed tool surface they can extend with their own tools
- **Multi-store operators** can install the same module per storefront with isolated secrets

## Integration with CorpusIQ

WisWes Magento pairs with the CorpusIQ analytics stack to close the loop between assistant conversations and store economics. CorpusIQ GA4 reads the traffic and conversion the WisWes widget drives; the CorpusIQ Stripe connector reads the settled revenue; the cross-source view tells the merchant whether the AI assistant lifts basket size or just shifts browsing. For operators running Shopify and Magento stores side by side, WisWes Magento gives the Magento side an assistant parity path with the Shopify tooling CorpusIQ already indexes. The commerce data stays in the store — WisWes holds only the embedded search payload, while CorpusIQ connectors read the financial truth.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- Magento 2 only (2.4.4+); no Magento 1 or OpenMage support
- The assistant itself is a WisWes service — the module is free, the workspace plan governs index size (`skipped_cap` when the plan limit is hit)
- Self-hosted endpoint means your web server must be reachable from WisWes (firewall/NAT considerations)
- No published tool-level API docs beyond the module README; extend-by-code for custom tools

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
