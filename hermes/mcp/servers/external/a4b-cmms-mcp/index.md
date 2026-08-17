---
title: "A4B CMMS MCP - CorpusIQ Docs"
description: Asset and maintenance management over MCP — 24 tools for assets, workspaces, maintenance tasks, users and QR codes, with OAuth 2.1, multi-tenancy and audit logging.
category: ERP
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [asset-management, maintenance, cmms, oauth, audit-logging, multi-tenant, operations, remote-mcp]
---

# A4B CMMS MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 + PKCE)** — a4b.ai gives AI assistants secure, real-time access to asset and maintenance data: 24 tools covering assets, workspaces, maintenance tasks, users, invites, and QR codes, plus 9 read-only resource templates browsable via `a4b://` URIs. Multi-tenant, with every tool call logged for compliance.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 + PKCE with dynamic client registration
Endpoint: https://a4b.ai/mcp
Tools: 24 (assets, workspaces, maintenance tasks, users, invites, QR codes) + 9 resource templates
Pricing: not published on the docs page
Category: ERP
Built by: a4b.ai
```

## Why This Matters for Operators

Asset tracking is where operational discipline dies — equipment lists drift, maintenance schedules lapse, and the QR code on the machine was printed two vendors ago. Bringing it into MCP means the agent that runs procurement and maintenance can actually see the asset register it is acting on.

**The compliance posture is the standout**: OAuth 2.1 with PKCE (no client secrets), organization-scoped multi-tenant tokens, and audit logging with 90-day retention — where permanent-deletion entries are explicitly not pruned. For regulated operators, that retention nuance means the audit trail cannot be laundered by deleting records.

## Tools & Capabilities

| Area | Purpose |
|---|---|
| Assets | Register, query, and update physical assets |
| Workspaces | Location and site structure |
| Maintenance tasks | Create, assign, and track maintenance work |
| Users & invites | Team access management |
| QR codes | Asset tagging and scan workflows |
| Resource templates | 9 read-only `a4b://` URIs for browsable data |

## Installation

```bash
claude mcp add a4b --transport http https://a4b.ai/mcp
```

OAuth 2.1 flow with PKCE — browser authorization, no client secrets. Vendor publishes quickstart, authentication, and usage-example pages; also available in the ChatGPT app directory.

## Configuration

```json
{
  "mcpServers": {
    "a4b": {
      "type": "http",
      "url": "https://a4b.ai/mcp"
    }
  }
}
```

## Business Relevance

- **Operations leads** get maintenance schedules the agent can act on instead of a spreadsheet nobody owns.
- **Facility managers** get QR-coded asset tracking with scan workflows from any MCP client.
- **Integrators** get dynamic client registration for building multi-tenant automation on top of asset data.
- **Compliance-driven organizations** get audit logging with deletion-resistant retention semantics.

## Integration with CorpusIQ

A4B slots into the ERP and operations stack CorpusIQ already connects. Asset and maintenance data pairs with the Odoo connector's inventory and stock movements, and QuickBooks items give the financial view of the same register — so an agent can trace an asset from the maintenance task through to its book value. The multi-tenant, audit-logged design matches CorpusIQ's governed-write doctrine: agent reads are scoped, and every write leaves a compliance-grade trail.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- Pricing not published on the docs page — vendor sales motion required.
- CMMS scope is asset/maintenance only — no purchasing, invoicing, or finance modules.
- OAuth-only, so non-browser automation needs a client that supports the full 2.1 + PKCE flow.
- Tool-level detail beyond the 24-tool count is thin; the quickstart covers the essentials.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
