---
title: "Kaiva Bridge MCP - CorpusIQ Docs"
description: Turn any Postgres database or OpenAPI spec into a secure, hosted MCP server with per-tool access control and a full audit log. No server to write, nothing to host.
category: DevOps
stars: n/a (new listing)
added: 2026-08-16
source: mcp.so
relevance: ★★
tags: [database, postgres, openapi, gateway, access-control, audit-log, hosting, remote-mcp]
---

# Kaiva Bridge MCP

**Remote database gateway (Streamable HTTP, Bearer token)** — Kaiva Bridge turns any Postgres database or OpenAPI spec into a secure, hosted MCP server: it reads the schema, generates typed tools, and serves a live endpoint with per-tool access control and every call written to an audit log. Built by Kaiva (`kaiv.ai/bridge`). The mcp.so listing is a live read-only demo of a synthetic commerce dataset, so operators can try the pattern before connecting their own data.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer token (demo key public; per-tenant keys for your own servers)
Endpoint: https://api-demo.kaiv.ai/api/bridge/mcp/commerce-demo (demo)
Tools: 6 in the demo (products, orders, customers, inventory) — your own tools are generated from your schema
Pricing: Demo free and rate-limited — create your own server at kaiv.ai/bridge
Category: Development & Infrastructure
Built by: Kaiva (kaiv.ai/bridge)
```

## Why This Matters for Operators

Giving an AI agent access to a production database has historically meant a credentials handoff: hand the agent a connection string and hope it only reads what it should. Kaiva Bridge replaces that handoff with a scoped, audited connection — the operator points the gateway at a Postgres database or an OpenAPI spec, and the agent gets typed tools bounded by per-tool access control, while every call lands in an audit log.

**The key advantage: data access becomes a governed product instead of a shared password.** No server to write, nothing to host, and the human keeps a record of exactly what the agent queried. For a small ops team running agents against orders, inventory, or customer data, that is the difference between "we can't let the agent touch the DB" and "the agent runs the daily reconciliation."

## Tools & Capabilities

The demo exposes a synthetic commerce schema with 6 tools; a custom server's tools are generated from the schema it is pointed at.

| Tool | Purpose |
|---|---|
| `list_products` | List products in the dataset |
| `get_product` | Fetch a single product record |
| `list_orders` | List orders with their state |
| `get_order` | Fetch one order by ID |
| `list_customers` | List customer records |
| `get_inventory` | Read current inventory levels |

The live tool list is served from the endpoint — the demo above is illustrative of the commerce-schema pattern, not an exhaustive catalog.

## Installation

```bash
claude mcp add kaiva-bridge --transport http https://api-demo.kaiv.ai/api/bridge/mcp/commerce-demo --header "Authorization: Bearer kv_live_commerce_demo_public_ro"
```

The vendor publishes one-line setup snippets for Claude Code, Codex, Cursor, and VS Code on the listing page.

## Configuration

```json
{
  "mcpServers": {
    "kaiva-bridge": {
      "type": "http",
      "url": "https://api-demo.kaiv.ai/api/bridge/mcp/commerce-demo",
      "headers": {
        "Authorization": "Bearer kv_live_commerce_demo_public_ro"
      }
    }
  }
}
```

For your own data, create a server at kaiv.ai/bridge, connect your Postgres string or OpenAPI URL, and use the issued endpoint and token instead of the public demo.

## Business Relevance

- **Operations teams** can let agents run daily checks against order and inventory data without issuing database credentials
- **Data teams** turn an existing OpenAPI spec into an agent-facing surface with zero hosting work
- **Compliance-minded operators** get per-tool scoping plus a complete call audit trail for agent data access
- **Small e-commerce operators** follow the demo's commerce schema pattern to expose products, orders, and customers safely

## Integration with CorpusIQ

Kaiva Bridge complements CorpusIQ's managed connectors by covering the databases CorpusIQ does not. CorpusIQ reads Stripe, QuickBooks, Shopify, and HubSpot natively; Kaiva Bridge covers the internal Postgres warehouse or a custom operations database an operator wants agents to query — with an audit log attached to every call.

A composed workflow: the agent pulls revenue and payment data from CorpusIQ's Stripe and QuickBooks connectors, then uses a Kaiva-hosted endpoint to reconcile against raw order rows in the internal database, producing one governed, audited reconciliation pass across both surfaces.

## Limitations

- Brand new — submitted to mcp.so in mid-August 2026, no community track record yet
- Hosted gateway — connecting your database means the data path runs through Kaiva's infrastructure
- Pricing for custom servers is not published on the listing; verify before connecting production data
- The demo dataset is synthetic commerce data; production behavior depends on your own schema and scoping
- Access-control granularity details are thin in the published docs — confirm per-tool scoping matches your needs before rollout

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
