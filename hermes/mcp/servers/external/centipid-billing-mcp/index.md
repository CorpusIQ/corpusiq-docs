---
title: Centipid ISP Billing MCP - Subscriber and Network Operations
description: "Query a Centipid ISP billing workspace from any MCP client: revenue and payment reports, subscriber status and expirations, MikroTik router sessions and diagnostics, plus voucher stock. 23 tools, 20 read-only, with in-app operator approval required for the three that change network state."
category: Finance
stars: n/a (hosted, no public repo)
added: 2026-08-26
source: "mcp.so GitHub issue #3785"
relevance: ★★★
tags: [isp, billing, network-operations, mikrotik, mpesa, revenue, remote-mcp, api-key]
---

# Centipid ISP Billing MCP

**Remote MCP server (Streamable HTTP) for Centipid, billing and network-management software for internet service providers and WISPs.** One endpoint answers the operator questions that usually mean opening the billing app: how much did we collect today, who is expiring in the next 24 hours, who owes us money, which router is overloaded, why is this subscriber offline, how many vouchers are left. The server covers hotspot and PPPoE subscribers, RADIUS sessions, MikroTik RouterOS routers, and mobile-money payments including M-Pesa. 23 tools, 20 read-only; the three that can change network state never act on their own.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (created in the billing app, Settings -> Developer)
Endpoint: https://mcp.centipidbilling.com/mcp
Tools: 23 (20 read-only, 3 operator-approved actions)
Pricing: Included with a Centipid operator account
Category: Finance / ISP Billing
Built by: Centipid (registry com.centipidbilling/billing)
```

## Why This Matters for Operators

ISP ops run on a handful of daily numbers that live inside the billing platform: collections, expirations, overdue accounts, router load, voucher inventory. An operator running a WISP usually pulls these by hand, or waits for a support agent to click through the app. Centipid's MCP puts the same workspace inside the AI assistant that is already answering "how did this week go".

**The safety model is the approval queue, not the API.** Every tool carries a `readOnlyHint` annotation. The three that can change network state - `reconnect_subscriber`, `disconnect_no_expiry`, `apply_mikrotik_fix` - file a request that an administrator confirms inside the billing app, and return `pending_confirmation` until then. The agent can prepare an action but cannot execute it alone.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Revenue & payments | `revenue_summary`, `payments_report`, `outstanding_invoices`, `amount_due`, `voucher_stock` |
| Subscribers | `subscriber_lookup`, `subscriber_status`, `list_subscribers`, `expiring_subscribers`, `top_data_users` |
| Network & MikroTik | `active_sessions`, `nas_status`, `router_resources`, `mikrotik_config`, `mikrotik_logs`, `mikrotik_read_command`, `run_mikrotik_diagnosis` |
| Plans & support | `packages`, `open_tickets`, `search_documentation` |
| Operator-approved actions | `reconnect_subscriber`, `disconnect_no_expiry`, `apply_mikrotik_fix` |

## Installation

Add the server to your MCP client with the endpoint and your workspace API key:

```json
{
  "mcpServers": {
    "centipid": {
      "url": "https://mcp.centipidbilling.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

Reference docs: https://docs.centipidbilling.com/reference/mcp-access

## Configuration

The API key is created by the operator in the billing app under Settings -> Developer. One endpoint serves every ISP, and data is scoped to the key's own workspace, so the key identifies which ISP the request belongs to. The key attaches as the authorization header on every call; there is no per-user OAuth flow. Requires an existing Centipid operator account - the server is not usable without one.

## Business Relevance

For WISP operators, this turns the daily operations recap into a chat answer: revenue collected, subscribers at risk of churn (expirations), overdue invoices, overloaded routers, and voucher inventory in one session. The MikroTik read tools (`mikrotik_read_command`, `run_mikrotik_diagnosis`) extend that to the network layer without granting write access - diagnostics only, with fixes gated behind the in-app approval queue. The M-Pesa payment surface matters for African ISPs where mobile money is the primary collection rail.

## Integration with CorpusIQ

CorpusIQ's revenue connectors (Stripe, QuickBooks) cover SaaS finance; Centipid covers the ISP/telecom niche with a different data shape: subscriber lifecycle and network sessions. Operators running both can join the billing view (Centipid) with the accounting view (QuickBooks) in one agent session. The read-only discipline matches CorpusIQ's read-only philosophy, and the pending-confirmation pattern for mutations is a model for approval-gated write surfaces.

## Limitations

- Workspace-scoped: one API key sees only its own ISP's data; no cross-tenant view.
- No public GitHub repo found for the connector (hosted only); documentation lives at docs.centipidbilling.com.
- The three action tools require a human confirmation in the billing app, which means an agent cannot autonomously restore a subscriber or apply a router fix.
- MikroTik read commands are diagnostics, not a full RouterOS management plane.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [QuickBooks MCP](/docs/hermes/mcp/servers/external/quickbooks-mcp)
- [Stripe MCP](/docs/hermes/mcp/servers/external/stripe-mcp)
- [MCP Billing Gateway](/docs/hermes/mcp/servers/external/mcp-billing-gateway)
