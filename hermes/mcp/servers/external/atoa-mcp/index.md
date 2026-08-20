---
title: "Atoa MCP - UK Pay by Bank Payments for AI Agents"
description: "First-party MCP server for Atoa, the FCA-authorised UK payments platform: create and manage Pay by Bank and card payments, customers, refunds, transactions, bank feeds and approvals from any MCP client"
category: Commerce & E-Commerce
stars: n/a (no public repo)
added: 2026-08-20
source: mcpservers.org
relevance: ★★★
tags: [payments, pay-by-bank, uk-payments, payment-links, qr-payments, ecommerce-checkout, fintech, remote-mcp]
---

# Atoa MCP

**Remote MCP server (Streamable HTTP, Bearer token + environment header) — Atoa's first-party bridge that lets AI agents process payments, manage customers, handle refunds, read bank feeds and route approvals.** Atoa is a UK payments platform covering Pay by Bank (customers pay from their own banking app with Strong Customer Authentication), card payments, payment links, QR codes, ecommerce checkouts, card machines and recurring payments. The MCP server mirrors that surface as tools, with a hosted HTTP endpoint and a local npx mode for offline operation.

```
Server type: Hosted remote (Streamable HTTP) + local npx mode
Auth: Bearer SDK token + X-Atoa-Env header (sandbox | production)
Endpoint: https://mcp.atoa.me/mcp
Tools: 14+ (payments, customers, refunds, transactions, webhooks, bank feeds, approvals)
Pricing: platform pricing per Atoa; sandbox environment available
Category: Payments / Commerce
Built by: Atoa Payments Ltd (FCA authorised, PCI DSS, ISO 27001, SOC 2)
```

## Why This Matters for Operators

Payment operations usually means a human logged into a dashboard: check a payment, refund a customer, export transactions for the accountant. Atoa MCP moves that into the agent that is already handling the customer conversation. An agent that books a service can `process_payment` over a payment link, confirm with `get_payment`, and — when the customer cancels — `initiate_refund` without a second tool or a handoff. The token scoping and the sandbox/production environment header mean the write surface is explicit: a sandbox token cannot touch production, and mixing tokens and environments fails authentication rather than silently paying the wrong account.

The bank-feed and approvals surface is the operator-grade part. `get_transactions` gives the agent a settlement view for reconciliation, and the approvals flow keeps human sign-off on the money-out path — the agent drafts, a person approves. For UK businesses this is the difference between an agent that can read about payments and one that can run them end to end with an audit trail.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `process_payment` | Create a payment (link, QR, or checkout) for a customer to complete |
| `get_payment` | Check status of a single payment |
| `capture_payment` | Capture an authorised payment |
| `cancel_payment` | Cancel a payment before completion |
| `create_customer` / `get_customer` / `update_customer` / `delete_customer` | Full customer record management |
| `list_customers` | Enumerate customer records |
| `initiate_refund` / `cancel_refund` | Refund lifecycle |
| `get_transactions` | Transaction and settlement history for reconciliation |
| `create_webhook` / `delete_webhook` | Manage event delivery for agent-driven automation |
| Bank feeds & approvals | Read bank-feed data; route money-out actions through human approval |

## Installation

```bash
claude mcp add --transport http atoa https://mcp.atoa.me/mcp
```

Local mode runs the same surface over npx for offline work with credentials kept off HTTP:

```bash
npx -y @atoapayments/mcp-server   # run locally per the Atoa docs quick-start
```

## Configuration

```json
{
  "mcpServers": {
    "atoa": {
      "type": "http",
      "url": "https://mcp.atoa.me/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_SDK_TOKEN",
        "X-Atoa-Env": "sandbox"
      }
    }
  }
}
```

Optional headers: `X-Atoa-Payment-Redirect-Url` (where the customer returns after paying) and `X-Atoa-Ais-Redirect-Url` (return after bank authorisation). Generate the SDK token from the Atoa developer portal, then use the same token with `X-Atoa-Env: production` only after go-live. Full docs at docs.atoa.me/mcp-server with per-client (Claude, Cursor, VS Code) walkthroughs.

## Business Relevance

- **UK ecommerce and retail operators** get payment creation, capture, refunds and customer management inside the agent that runs the store ops
- **Service businesses** (trades, agencies, clinics) can raise payment links from a job record and confirm settlement in the same conversation
- **Finance teams** read `get_transactions` for daily reconciliation against the bank
- **Product teams** get an approvals-gated money-out path — agents can draft payouts, humans keep the keys

## Integration with CorpusIQ

Atoa MCP complements the CorpusIQ financial stack at the settlement edge. An operator reconciles Atoa settlements against QuickBooks through the CorpusIQ QuickBooks connector: the agent pulls Atoa transactions over MCP, matches them to invoices and payments in QuickBooks, and flags the gaps instead of exporting CSVs by hand. For UK ecommerce businesses running Shopify, the CorpusIQ Shopify connector shows order totals and payment state while Atoa MCP supplies the live settlement record — together they close the order-to-bank loop. The direction of flow: Atoa MCP executes and reads payments; CorpusIQ reads the accounting and store systems around them.

## Limitations

- UK market focus — Pay by Bank is a UK scheme; card acquiring applies to UK merchants
- Commercial platform — an Atoa account and SDK token are required; no free self-host path for the hosted server
- Money-out actions need the approvals workflow configured; do not assume default-open writes
- New MCP surface — tool set tracks the platform's own roadmap
- Sandbox and production tokens are not interchangeable; mixing them fails auth by design

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
