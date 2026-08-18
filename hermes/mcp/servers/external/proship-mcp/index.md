---
title: "ProShip MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "MCP server for ProShip, a Thai order-management platform - create Thailand Post shipments, print PDF labels and track parcels from any AI agent"
category: Commerce
stars: n/a (new listing)
added: 2026-08-18
source: mcp.so GitHub issues
relevance: ★
tags: [shipping, logistics, thailand-post, order-management, tracking, labels, ecommerce, remote-mcp]
---

# ProShip MCP

**MCP server for ProShip, a Thai order-management platform connected to Thailand Post — AI agents create Thailand Post shipments, print PDF shipping labels, track parcels with universal Thai carrier tracking, and manage orders.** Includes in-chat account signup so new users receive an API token without leaving the conversation. MIT-licensed, stateless remote streamable HTTP.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: API token (issued via in-chat signup)
Endpoint: https://mcp.proship.me/mcp
Docs: mcp.proship.me/mcp (auto-generated from the tool registry)
License: MIT
Category: Commerce / Logistics
Built by: ProShip (repo: proship1/proship-mcp, docs include a Thai-language quick-start)
```

## Why This Matters for Operators

Thai ecommerce operators run their fulfillment through Thailand Post, and order management through platforms like ProShip. This MCP closes the last mile of that workflow inside the agent: an order that arrives in chat becomes a shipment with a printed PDF label and live tracking — without a human re-keying anything. The auto-generated docs page from the tool registry and Thai quick-start make it approachable for the operators who actually run these stores.

**The in-chat signup is the notable design decision.** Account creation and token issuance happen inside the conversation, so an agent can onboard a merchant, connect, and start creating shipments in one session.

## Tools & Capabilities

| Area | What it does |
|---|---|
| Shipment creation | Create Thailand Post shipments from order data |
| PDF labels | Print shipping labels directly |
| Tracking | Universal Thai carrier parcel tracking |
| Order management | Manage orders from the connected platform |
| Account | In-chat signup and API token issuance |

Stateless remote transport means no local install — point any MCP client at the endpoint.

## Installation

```json
{
  "mcpServers": {
    "proship": {
      "type": "http",
      "url": "https://mcp.proship.me/mcp"
    }
  }
}
```

Token issuance happens via the in-chat signup flow; the docs page at mcp.proship.me/mcp lists the full tool registry.

## Configuration

No local state — the server is remote and stateless. The token from signup identifies the account for order and shipment operations. Thai-language quick-start available for local operators.

## Business Relevance

- **Thai online sellers** get Thailand Post fulfillment inside their agent workflow
- **Order-operations teams** turn orders into shipped parcels with labels without manual entry
- **Cross-border operators with Thai fulfillment** track Thai-carrier parcels through one surface
- **Agents doing merchant onboarding** complete account setup without leaving the chat

## Integration with CorpusIQ

CorpusIQ's commerce connectors (Shopify, Amazon, eBay, SHOPLINE) surface orders, inventory, and revenue. ProShip executes the fulfillment leg those connectors don't cover in Thailand: shipment creation, labels, and Thai-carrier tracking.

The composed workflow: CorpusIQ reports the order and inventory picture, the agent hands fulfillment to ProShip, and tracking comes back into the same session. Order-to-delivery visibility spans the commerce platform and the carrier through two MCP surfaces instead of manual copy-paste.

## Limitations

- Thailand-only carrier coverage — no relevance outside Thai fulfillment
- Brand new submission (Aug 18, 2026), zero stars, no adoption track record
- Single-vendor service operated by a small team
- Tool list not yet auto-published in directories; inspect the docs page before integration
