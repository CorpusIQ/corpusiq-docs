---
title: "DrillerDB MCP - Field Service Data for Drilling Contractors"
description: "Official remote MCP connector for DrillerDB, the operating system for water-well and drilling contractors: 45 tools (37 read-only) over projects, customers, invoices, work orders, crews, schedules, equipment, compliance and well logs, with OAuth 2.0 PKCE, tenant isolation, audit logging and approval-gated writes."
category: ERP
stars: 0
added: 2026-08-27
source: "mcp.so GitHub issue #3793"
relevance: ★★★
tags: [field-service, drilling, erp, project-management, invoicing, remote-mcp]
---

# DrillerDB MCP

**Remote MCP server (Streamable HTTP, OAuth 2.0 with PKCE and Dynamic Client Registration) for DrillerDB - the operating system for water-well and drilling contractors.** Forty-five tools (37 read-only, 8 write) over drilling projects, customers, contacts, invoices, proposals, quotes, work orders, crews, schedules, field reports, equipment, inventory, timecards, compliance forms, geology and well logs. Every tool declares `readOnlyHint` or `destructiveHint` and `openWorldHint: false`; tenant scoping is enforced by a `company_id` bound to the OAuth token rather than tool input; every call is audit-logged and high-risk writes are approval-gated. Official MCP registry name `com.drillerdb/drillerdb` v1.0.0 (DNS-verified namespace, published Aug 27, 2026). The endpoint answered a live anonymous initialize with HTTP 401 `missing_token`, confirming the OAuth gate.

```
Server type: Remote (Streamable HTTP), managed by DrillerDB, LLC
Auth: OAuth 2.0 Authorization Code + PKCE with Dynamic Client Registration
Endpoint: https://mcp.drillerdb.com
Registry: com.drillerdb/drillerdb v1.0.0 (official, active)
Tools: 45 (37 read-only, 8 write; high-risk writes approval-gated)
Docs: https://drillerdb.com/connectors/claude
Account: Requires an active DrillerDB account (app.drillerdb.com)
Category: ERP
Repo: github.com/CraigVG/drillerdb-mcp (MIT docs, hosted server closed-source)
```

## Why This Matters for Operators

Drilling and water-well contractors run on a vertical stack - well logs, rig maintenance, compliance forms and geology records do not fit horizontal field-service tools. DrillerDB's MCP connector is the first catalog entry that exposes a contractor's entire operating system to AI agents: an operator can ask which jobs are ready to schedule, what a customer still owes and how old it is, how revenue is pacing, and which rigs have maintenance coming due, and get answers grounded in their own tenant data. The permission model is the notable design detail: three granular scopes (`mcp:read`, `mcp:write:low`, `mcp:write:high`) plus a proposals scope, approval gates on state-changing writes (scheduling, dispatching, sending invoices), and tenant isolation enforced server-side by the token-bound `company_id`.

## Tools & Capabilities

**Read tools (37)** - representative of the surface:

| Group | Tools |
|---|---|
| Projects and jobs | `list_my_projects`, `list_projects_by_customer`, `get_project_detail`, `get_project_financials`, `get_job_profitability`, `update_project_status` (write) |
| Customers and money | `list_customers`, `list_contacts`, `list_invoices`, `get_invoice_detail`, `ar_aging_report`, `customer_ltv_report`, `total_billed_by_contact`, `revenue_pipeline` |
| Scheduling and crews | `query_schedule`, `list_crews`, `list_timecards`, `get_timecard_summary`, `schedule_project` (write), `dispatch_project` (write), `plan_crew_route` (write) |
| Field operations | `list_field_reports`, `submit_field_report` (write), `list_work_orders`, `get_work_order_detail`, `list_equipment`, `get_maintenance_due`, `list_inventory` |
| Well and compliance | `query_well_logs`, `get_geology_at_location`, `get_compliance_form`, `get_project_compliance_status`, `list_project_files`, `list_communications` |
| Proposals and quotes | `list_proposals`, `get_proposal_detail`, `get_company_proposal_habits`, `list_quotes`-adjacent `get_quote_detail`, `get_quote_engagement`, `run_report` |

**Write tools (8):** `attach_note_to_project`, `submit_field_report`, `plan_crew_route` (low-risk, not gated); `schedule_project`, `dispatch_project`, `import_vendor_invoice`, `send_invoice`, `update_project_status` (high-risk, approval-gated - the tool returns an `approval-required` result first and runs only after console approval). Nothing that contacts a customer or moves money executes without explicit confirmation.

## Installation

```bash
# Claude Code
claude mcp add --transport http drillerdb https://mcp.drillerdb.com
```

Claude desktop/web: Settings, Connectors, Add custom connector, paste `https://mcp.drillerdb.com`. For Cursor, VS Code and other clients:

```json
{
  "mcpServers": {
    "drillerdb": {
      "type": "http",
      "url": "https://mcp.drillerdb.com"
    }
  }
}
```

OAuth sign-in happens automatically on first use - the client discovers OAuth endpoints from `/.well-known/oauth-protected-resource` and the `WWW-Authenticate` header on the 401, so no client ID or secret is configured by hand.

## Configuration

- **Scopes:** `mcp:read` (projects, customers, invoices, proposals, work orders, crews, schedules, field reports, equipment, timecards, communications, inventory, well logs), `mcp:write:low` (trivially reversible writes), `mcp:write:high` (state-changing writes), `mcp:proposals:write` (proposal generation and delivery).
- **Security:** tenant isolation by token-bound `company_id` (no path to another contractor's data), full audit log of every tool call, per-consumer rate limits, revocable access from the DrillerDB account.
- **Pricing:** the connector is included with an active DrillerDB account; the vendor does not publish standalone connector pricing.

## Business Relevance

- **Contractor operations teams** ask scheduling, aging and maintenance questions in plain English instead of clicking through modules.
- **Owners and office managers** get revenue pacing, LTV and profitability answers grounded in their own data.
- **Field crews** draft and submit field reports from an agent, with high-risk actions still flowing through console approval.

## Integration with CorpusIQ

Complementary vertical depth to CorpusIQ's horizontal connectors: CorpusIQ covers general business systems (QuickBooks, Stripe, HubSpot and 30+ more), while DrillerDB covers the drilling-specific objects - well logs, geology, rig maintenance, compliance forms - that horizontal tools do not model. An agent can combine CorpusIQ financial connectors with DrillerDB's project and well-log data for a full picture of a drilling contractor's business.

## Limitations

- Requires an active DrillerDB account; there is no anonymous or demo surface.
- Closed-source hosted server: the GitHub repo holds documentation and the registry manifest only.
- Vertical scope - value concentrates in water-well and drilling contractors, not general field service.
- The connector is brand new (registry published Aug 27, 2026); the 45-tool surface is vendor-documented and 401-verified live, but not anonymous-probed beyond the OAuth gate.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [ATLASS OS MCP - Field-Service Business Platform for AI Agents](/docs/hermes/mcp/servers/external/atlass-os-mcp)
- [Centipid ISP Billing MCP - Subscriber and Network Operations Data](/docs/hermes/mcp/servers/external/centipid-billing-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/servers)
