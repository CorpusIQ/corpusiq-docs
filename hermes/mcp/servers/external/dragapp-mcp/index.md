---
title: Drag MCP - Gmail Shared Inbox Operations for AI Agents
description: Drag exposes 47 MCP tools across 12 categories so agents can triage, reply and report on a Gmail shared inbox. Threads, boards, cards, contacts, knowledge base, analytics, automations and WhatsApp messaging through a hosted endpoint or an MIT-licensed local server.
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [gmail, shared-inbox, email-ops, customer-support, whatsapp, knowledge-base, oauth, remote-mcp]
---

# Drag MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 PKCE or API key)** - the official DragApp connector, 47 tools across 12 categories giving an assistant full access to boards, emails, cards, contacts, knowledge base, analytics and automations. Connect to the hosted endpoint or run the MIT-licensed server locally; same tools, same permissions either way.

```
Server type: Remote (Streamable HTTP) or local stdio (npm, MIT)
Auth: API key entered once on the connect page (OAuth 2.1 PKCE + DCR under the hood)
Endpoint: https://app.dragapp.com/mcp (hosted) or npx @dragapp/mcp-server (local)
Tools: 47 across 12 categories
Pricing: DragApp plans
Category: Communication & Email
Built by: Drag (DragApp), server open source under MIT
```

## Why This Matters for Operators

Shared inboxes like support@ or billing@ drown teams in triage work: move it, label it, reply, repeat. Drag turns Gmail into boards and columns, and the MCP server hands that structure to an assistant. **An agent can find the Support board, list unread threads in the right column, reply to the latest email from a customer and report average response time, all from one conversation.**

The connection inherits existing Drag permissions, so the assistant can only do what the operator's own account can do. Every tool asks permission on first use, which keeps bulk moves and replies observable.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Email | `list_threads`, `get_thread`, `reply_to_thread`, `send_new_email`, `search_threads`, `filter_threads`, `move_thread`, `move_threads_bulk` |
| Boards | `list_boards`, `get_board`, `list_columns`, `list_board_members`, `list_teams` |
| Cards | `list_cards_in_column`, `get_card`, `create_card`, `update_card`, `move_card`, `archive_card` |
| Tags | `list_tags`, `add_tag_to_card` |
| Tasks | `create_task` |
| Contacts | `search_contacts`, `get_contact_conversations`, `create_contact` |
| Knowledge Base | `list_articles`, `get_article`, `create_article`, `update_article`, `search_knowledge` |
| Analytics | `get_response_times`, `get_avg_response_time`, `get_daily_activity`, `get_closed_activity` |
| Automations | `list_automations`, `toggle_automation`, `toggle_ai_drafts` |
| WhatsApp | `get_whatsapp_conversation`, `list_whatsapp_templates`, `send_whatsapp_message`, `send_whatsapp_template` |

## Installation

```bash
claude mcp add --transport http drag https://app.dragapp.com/mcp
```

Or run locally with `npx -y @dragapp/mcp-server` and the Drag API key in the DRAG_API_KEY environment variable. The connect page takes the key once and hands it to the client as its access token; nothing is stored on the MCP service's servers.

## Configuration

```json
{
  "mcpServers": {
    "dragapp": {
      "command": "npx",
      "args": ["-y", "@dragapp/mcp-server"],
      "env": {
        "DRAG_API_KEY": "your-api-key"
      }
    }
  }
}
```

Auth notes: generate the API key under Settings, Integrations inside Drag. It grants full access to your DragApp workspace, so keep it secret and revoke it there at any time. The hosted route uses OAuth 2.1 with PKCE and dynamic client registration.

## Business Relevance

- **Support teams** triage, reply and report on a Gmail shared inbox from a chat instead of the queue UI.
- **Billing and finance inboxes** bulk-move threads by label and assign them to the right owner.
- **Knowledge-driven teams** search and update the knowledge base alongside the ticket thread.
- **WhatsApp-connected businesses** send approved templates and free-text replies inside the customer-service window.

## Integration with CorpusIQ

Drag runs the inbox; CorpusIQ runs the books. A support operator handling a billing thread can have the assistant pull the customer's Stripe subscription and QuickBooks invoices through CorpusIQ while replying through Drag, then close the loop by moving the thread to Resolved. The composed flow is CorpusIQ for financial context, Drag for conversation context, one assistant for both.

## Limitations

- The API key grants full workspace access; treat it like a root credential and revoke freely.
- WhatsApp free-text messages only work inside the 24-hour customer-service window; templates required outside it.
- Hosted endpoint requires a DragApp plan; the local npm route needs Node and the same key.
- Analytics cover response times and activity, not revenue or conversion metrics.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/docs/hermes/mcp/servers/external/imap-mcp)
- [BoldDesk MCP - Helpdesk Ticket Operations for AI Agents](/docs/hermes/mcp/servers/external/bolddesk-mcp)
