---
title: "GReminders — Scheduling & CRM MCP for Professional Firms"
description: "Connect AI agents to your firm's scheduling, calendar, CRM, and client data. Claude can book meetings, retrieve CRM records, and answer client questions through one MCP endpoint."
source: api.greminders.com
stars: 0
language: N/A (Hosted SaaS)
transport: Streamable HTTP
auth: OAuth / API Key
category: Business Operations
last_updated: 2026-07-21
---

# GReminders — Scheduling & CRM MCP for Professional Firms

**Appointment reminder and scheduling platform with MCP integration.** GReminders gives AI agents secure access to your firm's scheduling, calendar, CRM, and client data. Agents can book and manage meetings, retrieve information from your CRM, answer questions about clients, and help advisors stay organized.

## What It Does for Operators

- **Calendar + CRM MCP** — Single endpoint for scheduling and client data access
- **Secure agent access** — AI agents get scoped access to firm data through OAuth
- **Meeting management** — Book, reschedule, cancel appointments through agent commands
- **Client data retrieval** — Query CRM records, financial information, and firm data from your AI agent
- **Multi-advisor support** — Works across teams with appropriate access controls

## Installation

```bash
# No installation — hosted endpoint
# Connect your GReminders account via OAuth
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "greminders": {
      "type": "url",
      "url": "https://api.greminders.com/mcp"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `book_meeting` | Schedule appointments with clients |
| `get_calendar` | View firm calendar with filters |
| `get_client_info` | Retrieve CRM records for a client |
| `search_clients` | Search CRM by name, email, or custom fields |
| `send_reminder` | Trigger appointment reminders |
| `get_firm_data` | Query firm-level data and metrics |

*Note: Tool names are approximate. Full documentation at api.greminders.com.*

## Operator Use Cases

1. **Financial Advisors** — "Claude, what meetings do I have tomorrow and what's the AUM for each client?"
2. **Law Firms** — Book client consultations and pull case files without leaving the AI conversation
3. **Medical Practices** — Manage patient appointments and retrieve intake information
4. **Consulting Firms** — Schedule discovery calls and pull engagement history in one query

## CorpusIQ Angle

GReminders is the first scheduling + CRM MCP server for professional services firms — one of CorpusIQ's core operator personas. Operators running service businesses can pair GReminders (client-facing scheduling) with CorpusIQ (back-office financial data) for a complete AI-powered operations stack.

## Limitations

- Requires active GReminders subscription
- Focused on professional services (not general scheduling)
- New MCP integration — API stability TBD
- CRM data scope depends on GReminders account tier
