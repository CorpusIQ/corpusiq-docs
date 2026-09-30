---
title: "Dumpster Controls MCP - Field Service Operations"
description: "Run a dumpster rental business from AI: orders, dispatch, invoices and customers with propose-then-confirm writes and role-scoped access."
category: Business Operations
stars: n/a (no public repo)
added: 2026-09-29
source: "mcp.so server page (dumpstercontrols.io)"
relevance: ★★
tags: [field-service, dispatch, invoicing, waste-management, business-operations, remote-mcp, oauth]
---

# Dumpster Controls MCP

**Plain-language operations for a roll-off business.** Dumpster Controls is free dumpster rental software for US and Canadian companies, and its MCP server lets owners, dispatchers and office staff work their account from Claude, ChatGPT or any MCP client: orders, dispatch, customers, invoices and landfill receipts, with every write behind a propose-then-confirm gate. Available in Claude's connector directory and in the official MCP Registry as io.dumpstercontrols/dumpster-controls.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1
Endpoint: https://mcp.dumpstercontrols.io/mcp
Tools: 24 (12 read-only, propose-then-confirm writes, app-only confirmations)
Pricing: Free
Category: Business Operations
Built by: Dumpster Controls (dumpstercontrols.io)
```

## Why This Matters for Operators

Field service operators live in dispatch boards and invoice lists, not dashboards. This server puts the daily questions in plain language: which dumpsters are late for pickup, who is driving the next task, which invoices are past due, and what a customer owes. The assistant shows exactly what will change before anything does, and nothing happens until the operator says yes.

Money never moves through the server: price changes and cancellations are prepared in chat and confirmed inside the Dumpster Controls app, and the server never charges cards. Every request runs as the signed-in user, limited to their company and role.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| get_connection_context | Your company, role and which actions you can use |
| list_orders / get_order | Find orders by customer, date or status including late pickups; one order's address, size, notes, timeline and next driver |
| search_customers / get_customer | Find customers by name, email or phone; contact details and address |
| get_order_landfill_receipt | Landfill weight and cost for an order |
| list_invoices / get_invoice | Invoices by status including past due; one invoice's items, total and due date |
| get_order_finance / get_finance_summary | Paid, refunded and owed on an order; daily totals received (admins) |
| list_drivers | Active drivers and trucks |
| check_proposal | Status of a pending change |
| propose/confirm_task_completion | Mark a delivery, pickup or landfill run as done |
| propose/confirm_task_assignment | Assign or reassign a driver |
| propose/confirm_order_update | Edit dates, address or notes (never the price) |
| propose/confirm_invoice_send | Send or resend an invoice by email or SMS |
| propose/confirm_customer_upsert | Create or edit a customer |
| propose_price_change / propose_order_cancel | Prepared in chat, confirmed inside the Dumpster Controls app |

## Installation

```bash
claude mcp add dumpster-controls --transport http https://mcp.dumpstercontrols.io/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "dumpster-controls": {
      "type": "http",
      "url": "https://mcp.dumpstercontrols.io/mcp"
    }
  }
}
```

The first connection opens a browser window to sign in and authorize access; credentials are reused for later sessions. Developer docs are published at dumpstercontrols.io/developers/mcp.

## Business Relevance

- **Owners and dispatchers** ask which dumpsters are late and who drives the next task
- **Office staff** pull customers, invoices and what is past due in plain language
- **Admins** review paid-versus-owed per order and daily totals
- **Field service operators generally** get a reference pattern: propose-then-confirm writes, role-scoped access, and no money moving through the agent

## Integration with CorpusIQ

Dumpster Controls is the vertical-operations layer that CorpusIQ complements with financial context. A composed workflow: CorpusIQ reports cash flow and customer revenue from QuickBooks or Stripe, the assistant reconciles it against the field picture from Dumpster Controls (invoices sent, past due, landfill costs), and the operator approves any follow-up in one session.

## Limitations

- Dumpster rental vertical only (US and Canada)
- Writes require explicit confirmation; price changes and cancellations confirm inside the app
- Every request is scoped to the signed-in user's company and role
- No public repo; the hosted endpoint is the only install path

## FAQ

### Can the server charge cards or move money?

No. The server never charges cards or moves money. Price changes and cancellations are prepared in chat and confirmed by you inside the Dumpster Controls app.

### What does propose-then-confirm mean?

The assistant shows exactly what will change and nothing happens until you say yes. Each write is a propose call followed by a confirm call.

### Who can see and change what?

Every request runs as the signed-in user, limited to their company and role. Admin-only tools like finance summaries are gated to admins.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Worklittle Jobs MCP - Job Search and Market Data for AI Agents](/hermes/mcp/servers/external/worklittle-jobs/)
