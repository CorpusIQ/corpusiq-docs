---
title: Ship24 Tracking MCP - Package Tracking Across 2,500+
description: "Official hosted MCP from Ship24: create and manage trackers, fetch full tracking events and delivery statistics, and list every supported courier through 11 tools at api.ship24.com/mcp. Authenticate with a standard Ship24 API key. Ideal for e-commerce logistics operations."
category: Commerce & E-Commerce
stars: n/a (hosted)
added: 2026-08-25
source: mcpservers.org homepage
relevance: ★★★
tags: [mcp-server, tracking, logistics, shipping, carriers, e-commerce, delivery]
---

# Ship24 Tracking MCP

**Universal parcel tracking as native MCP tools.** Ship24 hosts an official MCP server that exposes its Tracking API, so an AI assistant can create trackers, fetch tracking results, and list couriers without writing any HTTP code. One integration covers 2,500+ carriers and 3PLs worldwide: live shipment status, delivery updates, full event history, and courier metadata.

```
Server type: Remote Streamable HTTP (official, hosted by Ship24)
Endpoint: https://api.ship24.com/mcp
Auth: Ship24 API key (apik_...) passed as Authorization: Bearer header
Docs: docs.ship24.com/integrate-with-ai
Tools: 11 documented (create_tracker, bulk_create_trackers, track, list_trackers,
  get_tracker, update_tracker, get_tracking_results, search_tracking_by_number,
  get_couriers, search_tracking, resend_webhooks)
```

## Why This Matters for Operators

Support teams answering "where is my order" burn hours looking up tracking numbers across carrier sites. Ship24 MCP puts the whole loop in the agent: `track` creates a tracker and returns full results in one call, `bulk_create_trackers` registers up to 100 shipments at once, and `get_tracking_results` returns every event with delivery statistics. For e-commerce operators, that means an agent can answer a customer's order-status question, spot a stuck shipment across carriers, and trigger webhook resends, all inside the conversation.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `create_tracker` | Creates a tracker for a tracking number; idempotent, subscribes to webhook updates when configured |
| `bulk_create_trackers` | Creates up to 100 trackers in a single request |
| `track` | Creates a tracker and returns full tracking results in one call |
| `list_trackers` | Returns a paginated list of your trackers |
| `get_tracker` | Fetches a single tracker's metadata by trackerId or clientTrackerId |
| `update_tracker` | Partially updates a tracker (subscribe/unsubscribe, correct destination) |
| `get_tracking_results` | Full results for a tracker: status, all events, delivery statistics |
| `search_tracking_by_number` | Finds all tracking results for a raw tracking number without a trackerId |
| `get_couriers` | Lists every supported courier with its code and requirements |
| `search_tracking` | On-demand per-call lookup for per-call plans, no persistent tracker |
| `resend_webhooks` | Resends all webhook messages of an existing tracker |

## Installation

Create an API key in the Ship24 Dashboard (Integrations, API Keys), then connect:

```bash
claude mcp add --transport http ship24-tracking https://api.ship24.com/mcp \
  -H "Authorization: Bearer apik_your_key_here"
```

For JSON-config clients (Claude Desktop, Cursor):

```json
{
  "mcpServers": {
    "ship24-tracking": {
      "type": "http",
      "url": "https://api.ship24.com/mcp",
      "headers": { "Authorization": "Bearer apik_your_key_here" }
    }
  }
}
```

## Configuration

Ship24 auto-detects the courier from the tracking number, so omit `courierCode` unless you must force one. `get_couriers` returns the full courier list, which is large: fetch it once and cache it rather than calling it repeatedly. MCP calls count against your Ship24 plan quota exactly like direct API calls.

## Business Relevance

- **Order-status support:** one tool call answers "where is my order" across any carrier.
- **Proactive exception handling:** agents poll trackers for stuck shipments and alert the team before customers complain.
- **Bulk logistics ops:** register up to 100 shipments per call and track delivery performance across carriers.

## Integration with CorpusIQ

Pair Ship24 tracking with CorpusIQ's e-commerce connectors: look up order status via Ship24, then pull the order and customer record from Shopify or SHOPLINE through CorpusIQ to close a support ticket in one pass, or log delivery events to your database for carrier performance reporting.

## Limitations

- Requires a Ship24 API key and calls consume your plan quota.
- Webhook endpoint configuration, account/plan management, and API-key generation are Dashboard-only, not MCP tools.
- Per-call plans should prefer `search_tracking`; tracker-based plans should prefer tracker tools.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [ProShip MCP](/hermes/mcp/servers/external/proship-mcp)
- [ShipStar MCP](/hermes/mcp/servers/external/shipstar-mcp)
- [Walmart Marketplace MCP](/hermes/mcp/servers/external/walmart-marketplace-mcp)
