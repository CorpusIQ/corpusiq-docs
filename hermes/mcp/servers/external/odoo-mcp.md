---
title: "Odoo MCP — Zero-Setup ERP Connector for AI Agents"
description: "Free AI layer for Odoo ERP v16+. Connects any MCP client to accounting, inventory, CRM, and sales — no Odoo App Store module required. Business operators can query live ERP data directly from Claude, Cursor, or any MCP-compatible agent."
category: mcp
tags: [mcp-server, odoo, erp, accounting, inventory, crm, business-operations]
last_updated: 2026-07-02
---

# Odoo MCP — ERP Connector for AI Agents

## What It Is

Odoo MCP (`tuanle96/mcp-odoo`) provides a free AI layer for Odoo ERP — any edition, any version 16+. Unlike traditional ERP integrations that require installing Odoo App Store modules or admin-side configuration, this MCP server connects directly via the XML-RPC API with zero Odoo-side setup. Business operators can query live ERP data (invoices, inventory levels, CRM pipelines, sales orders) directly from any MCP-compatible AI agent.

## Tools Available

| Tool | Description |
|------|-------------|
| Query models | Read/query any Odoo model (sale.order, account.move, stock.quant, etc.) |
| Search & filter | Domain-filtered searches across all enabled Odoo modules |
| Field access | Full access to model fields the authenticated user has permission to read |

## Quick Start

```bash
ODOO_URL={your-odoo-url} ODOO_DB={database-name} ODOO_USERNAME={user} ODOO_PASSWORD={pass} npx -y @tuanle96/mcp-odoo
```

## Business Use Cases

1. **Monthly close queries**: "Show me all unpaid invoices over 30 days and their customer names" — without logging into Odoo
2. **Inventory alerts**: "Which products are below reorder threshold across Warehouse A and B?"
3. **CRM pipeline review**: "Summarize opportunities in 'Negotiation' stage with deal values over $10K"
4. **Sales performance**: "Show total revenue by salesperson this quarter vs last quarter"
5. **Cross-source analysis**: Combine Odoo data with GA4/Stripe data via CorpusIQ for end-to-end business intelligence

## How It Compares to CorpusIQ

| Feature | Odoo MCP | CorpusIQ (QuickBooks, Stripe, Shopify) |
|---------|----------|----------------------------------------|
| ERP scope | Odoo-only | Multi-platform (36+ connectors) |
| Setup | Zero Odoo-side setup | OAuth 2.1, one-time connect |
| Write access | Read-only (current) | Read-only |
| Auth model | User/password XML-RPC | OAuth 2.1 PKCE |
| Best for | Odoo-native businesses | Multi-platform operators |

## Limitations

- **Read-only**: Current implementation is read-only — no write-back to Odoo
- **Odoo 16+ only**: Requires Odoo version 16 or newer
- **Authentication**: Uses XML-RPC user/password — ensure credentials are stored securely
- **No Odoo.sh support yet**: Self-hosted Odoo instances only; Odoo.sh compatibility not confirmed
- **Permission-bound**: Agent sees only what the authenticated Odoo user can access

## See Also

- [CorpusIQ MCP Connectors — 36+ business data sources](/hermes/mcp/connectors/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [QuickBooks Integration via CorpusIQ](/hermes/mcp/connectors/#quickbooks)
