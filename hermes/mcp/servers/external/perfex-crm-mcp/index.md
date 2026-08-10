---
title: "Perfex CRM MCP — AI-Ready Self-Hosted CRM"
server: perfex-crm-mcp
rating: ★★★
category: CRM / Productivity
transport: stdio + HTTP
auth: Perfex API Keys (staff-scoped)
added: 2026-08-10
source: mcp.so
---

# Perfex CRM MCP — Integration Guide

## Overview

Perfex CRM MCP turns a self-hosted Perfex CRM installation into an MCP-compatible AI workspace. Every CRM module — leads, customers, invoices, tickets, projects, contracts, subscriptions — becomes a typed MCP tool that any AI assistant can query and update.

This is the first self-hosted CRM MCP server. Unlike SaaS CRM connectors that route through a third party, Perfex CRM MCP runs inside your own Perfex installation. Your data never leaves your server.

## Relevance to Business Operators

| Use Case | Value |
|----------|-------|
| Morning triage | "What changed overnight? New leads, tickets, overdue invoices." — one prompt |
| Sales prep | "Give me the full history on Client X before my call." |
| Data entry | "Create a lead from this email and assign to Maria." |
| Cross-module reporting | "Which clients have high ticket volume AND low invoice totals?" |
| Bulk cleanup | "Find duplicate contacts and leads stuck for 90+ days." |

## Setup

### Prerequisites
- Working Perfex CRM installation (self-hosted)
- PHP 7.4+
- HTTPS (strongly recommended for HTTP transport)

### Installation
1. Upload the MCP module through **Setup → Modules → Upload Module**
2. Activate the module
3. Open **MCP Settings** panel and generate an API key
4. Copy the generated config snippet

### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "perfex-crm": {
      "type": "http",
      "url": "https://your-perfex-install.com/api/mcp",
      "headers": {
        "X-API-Key": "your-generated-key"
      }
    }
  }
}
```

### Claude Code / Cursor / VS Code (stdio)
```json
{
  "mcpServers": {
    "perfex-crm": {
      "command": "perfex-mcp",
      "env": {
        "PERFEX_API_KEY": "your-generated-key",
        "PERFEX_URL": "https://your-perfex-install.com"
      }
    }
  }
}
```

## Security Model

Perfex CRM MCP inherits Perfex's native permission system:

| Feature | Description |
|---------|-------------|
| **Staff-scoped keys** | Each API key inherits the staff member's existing CRM permissions |
| **Read-only mode** | Flip a switch to disable all write tools globally |
| **Granular tool control** | Enable/disable individual capabilities from settings |
| **Full request logging** | Every call recorded: key, tool, parameters, response status |
| **Rate limiting** | Protects against runaway loops |
| **No third-party relay** | MCP server runs inside your Perfex installation |

## Tools

The server exposes Perfex CRM's full REST API as typed MCP tools:

| Module | Capabilities |
|--------|-------------|
| **Customers & Contacts** | Search, read, create, update |
| **Leads** | Create, read, update status, assign to staff |
| **Invoices** | Search, read, create, mark paid/overdue |
| **Estimates & Proposals** | Create, read, convert to invoice |
| **Credit Notes** | Create, read |
| **Payments** | Record, read |
| **Expenses** | Create, read, categorize |
| **Items & Products** | Search, read |
| **Tasks** | Create, read, update, assign |
| **Projects & Milestones** | Create, read, update progress |
| **Support Tickets** | Create, read, reply, assign, close |
| **Contracts** | Create, read, renew |
| **Subscriptions** | Create, read, manage |
| **Staff** | Read (list, details) |
| **Timesheets** | Create, read |
| **Custom Fields** | Read, write across all modules |

## Use Cases for Business Operators

### Daily Operations
```
> "Summarize every open support ticket for Acme Ltd and tell me which one has been sitting longest."
```

### Financial Oversight
```
> "Which clients have overdue invoices older than 45 days, and how much do they owe in total?"
```

### Sales Pipeline
```
> "Show me all leads in 'Proposal Sent' status that haven't been followed up in 7 days."
```

### Automation (with n8n)
```
> n8n workflow: "When a new lead is created, have the AI draft a personalized welcome email, create a task for the account manager, and schedule a follow-up."
```

## Limitations

- **Perfex-only** — no cross-CRM compatibility
- **Self-hosted dependency** — if your Perfex instance is down, MCP is down
- **Module purchase required** — not free (pricing via themesic.com)
- **No mobile push** — AI actions happen in your MCP client, not as push notifications

## Verdict

★★★ — **Essential for Perfex CRM operators.** This is the first MCP server that turns a self-hosted CRM into a conversational workspace. The security model (staff-scoped keys, read-only mode, full logging) is exactly right for production use. If you run Perfex CRM and use AI assistants, this is a day-one install. For operators on other CRMs, watch for similar MCP servers — this pattern will spread.

## Related MCP Servers in Catalog

- **Salesforce MCP** — Salesforce CRM connector (★★★)
- **Plyto** — Agentic CRM for small businesses (mcp.so listing)
- **Zeevou AI Connector** — Hospitality/property management MCP
