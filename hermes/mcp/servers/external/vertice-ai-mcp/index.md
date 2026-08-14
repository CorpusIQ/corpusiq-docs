---
title: Vertice AI MCP
description: Official MCP connector for the Vertice procurement platform. Query contracts, vendors, and SaaS spend in natural language from any MCP-compatible assistant.
category: Finance
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★★
tags: [procurement, saas-spend, contracts, finops, vendor-management, cost-optimization, finance, remote-mcp]
---

# Vertice AI MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 PKCE)** — the official hosted connector from Vertice that puts your procurement workspace inside an AI assistant. Query contracts, vendors, and SaaS spend in natural language, then trigger Vertice workflows on your behalf. It exposes the same data and actions as the Vertice web app, governed by the same role-based access controls.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with PKCE (S256)
Endpoint: Provisioned per tenant (Preview program)
Tools: Contract expiry, vendor spend, renewal terms, purchase requests
Pricing: Included with Vertice subscription (Preview access on request)
Category: Finance
Built by: Vertice (vertice.one)
```

## Why This Matters for Operators

Procurement questions live in spreadsheets and inboxes today. Which contracts expire in the next 90 days? What is our total annual spend with this vendor, and which other vendors sit in the same category? An operator has to assemble that answer from the Vertice dashboard, exports, and email threads.

**The Vertice connector answers those questions in one chat turn and can act on them.** Connecting an assistant grants nothing beyond what you can already see in Vertice yourself — the RBAC model from the web app carries straight through to MCP. That governance model, not the tool count, is the differentiator: procurement spend visibility inside an agent without loosening a single permission.

## Tools & Capabilities

The connector is an additional access channel to the Vertice platform. Illustrative workflows from the official documentation:

| Capability | What the assistant can do |
|---|---|
| Contract portfolio | "Which contracts expire in the next 90 days?" |
| Vendor spend | "What is our total annual spend with this vendor, and who else is in the same category?" |
| Renewal intelligence | "Find the latest signed contract for this vendor and summarize the renewal terms." |
| Purchase requests | "Open a new purchase request for an additional 25 seats of this vendor's product." |

The exact tool set is determined by Vertice's orchestration layer at request time and is scoped per tenant.

## Installation

```bash
claude mcp add vertice --transport http <provisioned-endpoint>
```

The connector works with any MCP-compatible assistant that supports the Streamable HTTP transport and OAuth 2.1 with PKCE (S256). Browser OAuth on first connect; subsequent calls reuse the session.

## Configuration

```json
{
  "mcpServers": {
    "vertice": {
      "type": "http",
      "url": "<provisioned-endpoint>"
    }
  }
}
```

Access is granted on request through your Vertice Account Manager while the connector is in Preview.

## Business Relevance

- **CFOs and finance leads** get vendor spend and renewal questions answered without exporting reports
- **Procurement managers** open purchase requests from the assistant they already use
- **Ops teams** run contract-expiry sweeps on a schedule instead of manually
- **Fractional CFOs** onboard new clients to spend visibility without dashboard training

## Integration with CorpusIQ

Vertice pairs with the CorpusIQ finance stack: QuickBooks provides the general ledger view of what was paid, Stripe shows the payment rail, and Vertice MCP adds the procurement layer — which contracts, which vendors, what renewals are coming. A composed workflow runs the renewal sweep in Vertice, matches vendors against QuickBooks spend, and checks Stripe for the payment history on the same account. The read-only governance posture complements CorpusIQ's own read-only connector design.

## Limitations

- Preview program — access is limited and granted on request through your Vertice Account Manager
- Requires an active Vertice tenant and user account in good standing
- Exact tool list is not published; surface depends on Vertice's orchestration layer
- Commercial SaaS — no self-host path

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
