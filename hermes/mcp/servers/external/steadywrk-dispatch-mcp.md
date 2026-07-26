---
title: STEADYWRK Dispatch MCP Server Integration Guide
description: Field-service dispatch for AI agents — instant quotes, tracked work orders, and public evals across 8 trade verticals. Connect field operations to Hermes Agent.
category: mcp
tags: [mcp, field-service, dispatch, work-orders, quotes, trade-operations, hermes-agent]
last_updated: 2026-07-26
---

# STEADYWRK Dispatch MCP — Field-Service Operations for Hermes Agent

STEADYWRK Dispatch connects AI agents to real-world field operations — price jobs, create tracked work orders, and inspect published capability evaluations across 8 trade verticals. Built by a sovereign AI company in Aqaba, Jordan.

## What It Does

STEADYWRK Dispatch turns your AI agent into a field-service dispatcher:

- **Instant quotes** — Price any job across 8 trade verticals with `dispatch.quote`
- **Tracked work orders** — Create and monitor work orders through completion with `dispatch.order`
- **Public evals** — Inspect published capability evaluations and trade indexes with `dispatch.evals` and `dispatch.index`
- **Zero-setup public tools** — Evals and index are free, no API key required
- **Audit log** — Every decision is logged and traceable

## Quick Setup

### Prerequisites
- **STEADYWRK account:** Sign up at [steadywrk.app](https://steadywrk.app) for API key (quote/order access)
- **No setup needed** for public read tools (evals, index)

### Add to Hermes Agent

```json
{
  "mcpServers": {
    "steadywrk-dispatch": {
      "type": "streamableHttp",
      "url": "https://steadywrk.app/api/mcp",
      "headers": {
        "x-api-key": "your_api_key"
      }
    }
  }
}
```

For public-only access (evals and index), omit the `x-api-key` header.

## Key Capabilities

| Tool | Auth | Description |
|------|------|-------------|
| `dispatch.evals` | Public | Browse published capability evaluations across trade verticals |
| `dispatch.index` | Public | Search and filter the trade services index |
| `dispatch.quote` | API Key | Generate an instant job quote with pricing breakdown |
| `dispatch.order` | API Key | Create a tracked work order with milestones and status |

## Use Cases for Business Operators

### 1. Automated Quote Generation
Have your agent price jobs from customer requests:

```
Agent prompt: "A customer needs HVAC maintenance for a 2,500 sq ft
commercial space in Phoenix. Get me a quote with line items for
inspection, filter replacement, and coil cleaning."
```

### 2. Work Order Dispatch
Create and track field-service work orders from natural language:

```
Agent prompt: "Create a work order for the plumbing repair at
123 Main St — leaking water heater, tenant reports water damage.
Priority: high. Schedule for tomorrow morning. Notify the tenant
when the tech is en route."
```

### 3. Trade Capability Discovery
Find qualified trades for project planning:

```
Agent prompt: "I'm opening a restaurant in Miami. What trades
are available for kitchen equipment installation, health-code
compliance prep, and fire suppression system setup? Show me their
published evals and response times."
```

### 4. Field Operations Dashboard
Monitor active work orders across properties:

```
Agent prompt: "Show me all open work orders across our 12 properties.
Which ones are overdue? Are any blocked waiting on parts? Which
trades have the fastest average completion times this quarter?"
```

## Integration with CorpusIQ

STEADYWRK Dispatch + CorpusIQ = end-to-end field operations:

1. **CorpusIQ email connector** → Parse customer requests into dispatch quotes
2. **CorpusIQ calendar connector** → Schedule work orders against tech availability
3. **AI agent** → Correlate work-order costs with QuickBooks P&L via CorpusIQ
4. **CorpusIQ Stripe connector** → Auto-invoice completed work orders

This replaces the manual "receive email, call trades, get paper quote, type invoice" loop with an agent-native dispatch surface.

## Pricing

- **Public tools (evals, index):** Free, no signup required
- **Quote and order tools:** API key required — contact STEADYWRK for pricing
- **8 trade verticals:** HVAC, plumbing, electrical, roofing, general contracting, landscaping, pest control, cleaning

## Limitations

- Currently 8 trade verticals — specialized trades (elevator, fire systems, industrial) not yet covered
- Quote accuracy depends on published trade evals being current
- API key required for write operations (quote, order)
- No webhook/event callback for status changes (polling required)

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
