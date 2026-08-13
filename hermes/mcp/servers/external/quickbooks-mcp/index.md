---
title: QuickBooks MCP Server
description: QuickBooks MCP integration guide — connect AI agents to QuickBooks Online via OAuth2 with 550+ tools for invoicing, billing, reporting, and inventory.
source: datagrout.ai
category: Finance / Accounting
stars: N/A (hosted platform)
added: 2026-07-29
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/quickbooks-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# QuickBooks MCP Server (datagrout)

**First comprehensive QuickBooks MCP server** — connects AI agents directly to QuickBooks Online through OAuth2. 550+ tools covering the full scope of business accounting: invoices, bills, reports, inventory, and more.

> **Source:** [datagrout.ai/integrations/quickbooks-mcp-server](https://datagrout.ai/integrations/quickbooks-mcp-server)
> **Category:** Finance / Accounting
> **Transport:** Hosted remote (Streamable HTTP)
> **Auth:** OAuth 2.0
> **Pricing:** Datagrout platform pricing (check datagrout.ai for current plans)

## What It Does

The QuickBooks MCP Server exposes 550+ tools that let AI agents:

- **Invoicing** — Create, send, and track invoices directly from AI conversations
- **Bills** — Capture and manage bills, track payables
- **Reports** — Pull P&L, balance sheets, cash flow statements, and custom reports
- **Inventory** — Track stock levels, manage purchase orders, and reorder points
- **Write operations** — Disabled by default per integration (security-first). Enable selectively.

Write operations are **disabled by default** — you opt in to specific write capabilities per integration. This makes it safe for operators who want read-only reporting initially, then graduate to AI-assisted bookkeeping.

## Why This Matters for Operators

Before this, QuickBooks integrations required brittle Zapier zaps, clunky CSV exports, or expensive middleware. Now your AI agent can:

- **"Pull last month's P&L and highlight any expense categories that grew >20% MoM"**
- **"Send invoices to all clients with overdue balances >30 days"**
- **"Check inventory levels and flag items below reorder thresholds"**
- **"Compare actuals vs budget for Q3"**

All from any MCP-compatible AI client (Claude, Cursor, Codex, etc.).

## How It Compares

| Feature | QuickBooks MCP (datagrout) | CorpusIQ QuickBooks | Xero MCP (Official) | Laravel QuickBooks MCP |
|---------|---------------------------|---------------------|---------------------|------------------------|
| Tools | 550+ | 40+ (read-only) | ~30 (read+write) | ~10 (read+write) |
| Write support | ✅ (opt-in) | ❌ (read-only) | ✅ | ✅ |
| Auth | OAuth 2.0 | OAuth 2.1 PKCE | OAuth 2.0 | API key |
| Transport | Remote HTTP | Remote HTTP | Remote HTTP | Local stdio |
| Scope | Full QBO | Data connectors | Xero-specific | QBO-specific |
| Maturity | New (July 2026) | Production | Production | Community |

CorpusIQ's QuickBooks connector remains the best choice for multi-source business intelligence (combining QuickBooks with Shopify, Stripe, HubSpot, etc. in one query). The datagrout QuickBooks MCP is the best option for deep QuickBooks operations — especially if you need write capabilities for invoicing and bill management.

## Integration Setup

### 1. Create a Datagrout Account

Sign up at [datagrout.ai](https://datagrout.ai) and navigate to Integrations → QuickBooks MCP Server.

### 2. Connect QuickBooks Online

Datagrout will walk you through Intuit's OAuth flow. You'll grant permissions to the specific QuickBooks company file you want the AI agent to access.

### 3. Configure Your MCP Client

Add the QuickBooks MCP endpoint to your AI client. The exact URL is provided in your Datagrout dashboard after connecting QuickBooks.

**Claude Desktop (`claude_desktop_config.json`):**
```json
{
  "mcpServers": {
    "quickbooks": {
      "type": "url",
      "url": "https://datagrout.ai/mcp/quickbooks/YOUR_ENDPOINT",
      "headers": {
        "Authorization": "Bearer YOUR_DATAGROUT_TOKEN"
      }
    }
  }
}
```

**Cursor / VS Code (`.cursor/mcp.json`):**
```json
{
  "mcpServers": {
    "quickbooks": {
      "url": "https://datagrout.ai/mcp/quickbooks/YOUR_ENDPOINT",
      "headers": {
        "Authorization": "Bearer YOUR_DATAGROUT_TOKEN"
      }
    }
  }
}
```

### 4. Enable Write Operations (Optional)

By default, write operations are disabled. To enable invoicing, bill creation, or inventory adjustments:

1. Go to your Datagrout dashboard → Integration Settings → QuickBooks
2. Toggle on the specific write operations you want to enable
3. The AI agent can now perform those operations

## Security Model

- **OAuth 2.0** with Intuit — tokens are scoped to your QuickBooks company
- **Write operations disabled by default** — you explicitly opt in per integration
- **Per-tool audit** — every AI-initiated action is logged in Datagrout
- **Revocable** — disconnect the integration from either Datagrout or Intuit's side at any time

## Limitations

- **Requires Datagrout platform** — not a standalone open-source server
- **QuickBooks Online only** — no QuickBooks Desktop support
- **New platform** — July 2026 launch, expect rapid iteration
- **Write operations** require deliberate opt-in per integration

## See Also

- [[oracle-mcp]] — Oracle Fusion Cloud MCP (also by datagrout)
- [[xero-mcp]] — Official Xero MCP server
- [[laravel-quickbooks-mcp]] — Community PHP QuickBooks MCP
- [[corpusiq-quickbooks]] — CorpusIQ's multi-source QuickBooks connector
