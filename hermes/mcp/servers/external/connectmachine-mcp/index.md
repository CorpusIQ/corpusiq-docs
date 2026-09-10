---
title: ConnectMachine MCP - Digital Business Cards and Contact CRM for Agents
description: Hosted MCP server for the ConnectMachine contact platform - manage contacts, networks, digital business cards and meeting transcripts in natural language, with dedupe detection, CSV export and an AI query tool.
category: CRM & Sales
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [crm, contacts, business-cards, networking, meetings, sales, remote-mcp]
---

# ConnectMachine MCP

**Contact relationship management in natural language** - ConnectMachine's digital business-card and contact platform exposed as a hosted MCP server. Create and search contacts, group them into networks, manage digital cards, and turn meeting transcripts into action items. Nothing to install or self-host.

```
Server type: Remote (hosted)
Endpoint: https://mcp.connectmachine.ai/mcp
Auth: Account-based (hosted server, no API key management)
Tools: 20+ (contacts, networks, cards, meetings, imports)
Pricing: ConnectMachine platform plans
Listed: Glama, Smithery (connectmachine/cm-mcp), Official MCP Registry (ai.connectmachine)
Built by: ConnectMachine.ai
```

## Why This Matters for Operators

Networking data dies in card stacks and scattered spreadsheets. **ConnectMachine keeps the contact graph live and agent-queryable**: an assistant can find who you met at an event, what was discussed (via meeting transcript Q&A), and who in your network is overdue for a touchpoint - then export a clean CSV for the next campaign. Duplicate detection and network grouping keep a growing contact base from turning into sludge.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `create_contact` / `find_contact` / `get_contact` / `list_contacts` / `search_contacts` | Contact CRUD with search across name, company, title, email, phone, notes, location and events |
| `get_contact_counts` / `get_duplicate_contacts` / `delete_contacts` | Hygiene - counts, duplicate detection, removal |
| `create_network` / `assign_contacts_to_network` / `delete_network` | Group contacts into networks |
| `create_card` / `get_card` / `delete_card` | Digital business-card management |
| `add_events_to_contact` | Attach events to a contact's history |
| `event_meeting_transcript_qa` / `generate_meeting_action_items` | Q&A over meeting transcripts and automatic action items |
| `ai_query` | Natural-language queries over your contact data |
| `create_import_session` / `abort_import` / `export_contacts_csv` | Bulk import/export |

## Installation

```bash
claude mcp add --transport http connectmachine https://mcp.connectmachine.ai/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "connectmachine": {
      "type": "http",
      "url": "https://mcp.connectmachine.ai/mcp"
    }
  }
}
```

Works in Claude Desktop, Claude Code, Cursor (plugin at github.com/connectmachine/cursor-plugin) and any MCP client. Sign in with your ConnectMachine account when the client opens the browser.
