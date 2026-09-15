---
title: "Packy Tracking MCP - Parcel Tracking and Courier Webhooks"
description: "Official hosted MCP server for the Packy Tracking API: create and manage parcel trackers, list and auto-detect couriers, and wire delivery-status webhooks through 10 tools at mcp.parceltracking.app. OAuth 2.1 or API-key auth, credit-based pricing on tracking creation, and public health endpoints for liveness checks."
category: Commerce & E-Commerce
stars: n/a (new listing, github.com/packy-tracking/packy-tracking-mcp)
added: 2026-08-29
source: mcpservers.org homepage
relevance: ★★
tags: [mcp-server, tracking, logistics, shipping, couriers, webhooks, e-commerce, remote-mcp]
---

# Packy Tracking MCP

**Official hosted MCP for the Packy parcel-tracking API: create and manage trackers, list and auto-detect couriers, and wire delivery-status webhooks from an AI assistant.** It exposes 10 tools mapped one-to-one onto the Packy Tracking API, runs as a hosted Streamable HTTP endpoint with no local installation, and supports both OAuth 2.1 and plain API-key auth. Only tracker creation consumes credits (one per unique tracking number); reads, courier detection, and webhook tools are free.

```
Server type: Remote (Streamable HTTP), hosted
Auth: OAuth 2.1 (recommended) or Packy API key (bearer or X-API-Key header)
Endpoint: https://mcp.parceltracking.app/mcp
Health: https://mcp.parceltracking.app/health and /ready (no auth needed)
Pricing: 1 credit per unique tracking number created; all other tools free
Category: Commerce & E-Commerce / Logistics
Built by: Packy (packyapp.com); repo github.com/packy-tracking/packy-tracking-mcp, license not declared
```

## Why This Matters for Operators

E-commerce operators already live in carrier tracking portals, pasting tracking numbers one at a time. Packy turns that into a queryable API surface an assistant can drive: register a shipment, ask for its latest events, detect the carrier from the number format, and get pushed when status changes instead of polling. The webhook tools are the operator-relevant part - create and update delivery-status webhooks without writing a line of integration code, so an AI workflow can react to "delivered" or "exception" events the moment the carrier reports them.

For multi-carrier operations, the courier tools answer the questions ops teams answer manually: which couriers does Packy cover, and which carrier does this tracking number belong to. The credit model keeps cost predictable - reads and webhook management cost nothing, so monitoring loops are free and only new tracker registrations are metered.

**Shipment tracking and delivery-event automation become assistant-driven instead of portal-driven.**

## Tools & Capabilities

Tool names verified from the repository's Tools table (exact API-operation mapping); the endpoint requires authentication, and anonymous enumeration is refused (401 confirmed live).

| Tool | Tracking API operation |
|---|---|
| trackings_create | POST /v1/trackings (1 credit per unique tracking number) |
| trackings_list | GET /v1/trackings |
| trackings_get | GET /v1/trackings/{id} |
| trackings_delete | DELETE /v1/trackings/{id} |
| couriers_list | GET /v1/couriers |
| courier_detections_create | POST /v1/courier-detections |
| webhooks_list | GET /v1/webhooks |
| webhooks_create | POST /v1/webhooks |
| webhooks_update | PATCH /v1/webhooks/{id} |
| webhooks_delete | DELETE /v1/webhooks/{id} |

## Installation

Hosted endpoint - no local server or package install. First, create an account at lk.parceltracking.app and generate an active API key.

OAuth (Claude):

```bash
claude mcp add packy-tracking --transport http https://mcp.parceltracking.app/mcp
```

Then follow the browser consent flow, select the API key to bind, and approve.

OAuth (Codex):

```bash
codex mcp add packy-tracking-mcp \
  --url https://mcp.parceltracking.app/mcp \
  --oauth-resource https://mcp.parceltracking.app/mcp
```

## Configuration

API-key fallback for clients without MCP OAuth support (the key is the same one used with the regular Packy Tracking API):

```json
{
  "mcpServers": {
    "packy-tracking-mcp": {
      "url": "https://mcp.parceltracking.app/mcp",
      "headers": {
        "Authorization": "Bearer pk_your_api_key"
      }
    }
  }
}
```

The server also accepts the key as an X-API-Key header. OAuth is recommended because the key is selected inside the Packy account instead of copied into client configuration. OAuth tokens are short-lived and refresh automatically; a failed consent flow requires starting a new connection attempt rather than reopening the old authorization URL.

Verify the service before wiring it into a workflow (no key required):

```bash
curl -fsS https://mcp.parceltracking.app/health
curl -fsS https://mcp.parceltracking.app/ready
```

Both return `{"status":"ok"}`; /ready additionally confirms the MCP service can reach its API gateway.

## Business Relevance

- **E-commerce operators** register and monitor shipments across the couriers Packy covers from a single assistant-driven surface.
- **Ops teams** replace portal polling with delivery-status webhooks that fire on carrier events.
- **Logistics workflows** auto-detect the carrier from a tracking number, then route handling accordingly.
- **Support teams** answer "where is my order" with the latest tracking events instead of opening the carrier site.

## Integration with CorpusIQ

Packy tracks the physical shipment; CorpusIQ tracks the money and the customer. A composed workflow: the assistant confirms a Shopify order through CorpusIQ connectors, registers the shipment in Packy, and sets a delivery webhook - when the carrier reports delivered, the assistant cross-checks the order and payment state in Shopify and Stripe through CorpusIQ and closes the loop from checkout to doorstep.

## Limitations

- Fresh listing: repo created Aug 26, 2026, 0 stars, license not declared; no official MCP registry record found yet.
- Repo is integration documentation only - the MCP implementation is hosted, so behavior depends on Packy's service availability.
- Tracking creation is metered (1 credit per unique tracking number); reads and webhook tools are free but rate limits apply per plan.
- Tool-level detail beyond the README's API-operation mapping requires an authenticated session.
- Consumer-facing brand (packyapp.com); the API-key and webhook surface is the operator-relevant layer.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Ship24 Tracking MCP - Package Tracking Across 2,500+ Carriers](/docs/hermes/mcp/servers/external/ship24-tracking)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
