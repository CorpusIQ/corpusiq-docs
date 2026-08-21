---
title: "TomTicket MCP — Helpdesk Operations from Any MCP Client"
description: "MCP server for the TomTicket helpdesk API: list tickets, reply as an operator with work time, comment, transfer, start/close status and finish tickets, plus customers, organizations, chats, departments and the knowledge base. Local stdio install with a bearer token."
category: Customer Support
stars: n/a (new listing)
added: 2026-08-21
source: "mcp.so GitHub issue #3679"
relevance: ★★
tags: [helpdesk, tickets, support, knowledge-base, tomticket, stdio, self-hosted]
---

# TomTicket MCP

**Full helpdesk operation from an MCP client — tickets, replies with logged work time, statuses and the knowledge base.** mcp-tomticket wraps the TomTicket helpdesk API v2 as a local stdio server: an agent can list open tickets, read a thread, reply as an operator while recording work time, comment internally, transfer ownership, move status and finish tickets — plus search customers, organizations, chats, departments and the KB articles.

```
Server type: Self-hosted (stdio)
Auth: Bearer token (TOMTICKET_TOKEN env)
Install: npx -y mcp-tomticket
Tools: 12+ (tickets, replies, statuses, customers, orgs, chats, KB)
Pricing: Free (open source); requires a TomTicket account
Category: Customer Support
Built by: glira (github.com/glira/mcp-tomticket)
```

## Why This Matters for Operators

Support teams lose hours to the ticket UI — clicking between the queue, the thread and the KB for every reply. **mcp-tomticket puts the whole helpdesk behind typed tools**, so an agent can triage the queue ("what's open and older than a day"), draft operator replies with work time recorded, and answer from the knowledge base without leaving the session. The reply-as-operator path is the key one: because work time is a first-class field on replies, billable support stays billable even when the agent writes the response.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `tomticket_list_open_tickets` / `tomticket_list_tickets` | The queue: open tickets or all tickets |
| `tomticket_get_ticket` | Full ticket detail |
| `tomticket_reply_ticket` | Reply as operator, recording work time |
| `tomticket_comment_ticket` | Internal comment without replying to the customer |
| `tomticket_finish_ticket` | Finish and close out a ticket |
| `tomticket_start_status` / `tomticket_close_status` | Status transitions |
| Plus | Customers, organizations, chats, departments and knowledge-base tools |

## Installation

```bash
npx -y mcp-tomticket
```

Add it to your MCP client with the token in the environment:

```json
{
  "mcpServers": {
    "tomticket": {
      "command": "npx",
      "args": ["-y", "mcp-tomticket"],
      "env": { "TOMTICKET_TOKEN": "your_token_here" }
    }
  }
}
```

## Configuration

One env var: `TOMTICKET_TOKEN` from your TomTicket account. Local stdio means ticket data passes through your machine, not a third-party host.

## Business Relevance

- **Support leads** triage the queue and draft replies with work time from an agent session
- **Solo operators** handle TomTicket support without switching between chat and dashboard
- **Support ops** keep the KB consulted by the agent for consistent answers
- **Agencies** run multi-client support desks with per-account tokens

## Integration with CorpusIQ

TomTicket is the front-line layer; CorpusIQ is the customer truth behind it. A composed workflow has mcp-tomticket open the ticket while CorpusIQ pulls the customer's record — Stripe charges, QuickBooks invoices, HubSpot deal — into the same session, so the agent replies with the account's actual state instead of asking the customer what they bought. Escalations from the ticket queue can be routed into CorpusIQ's CRM connectors for follow-up.

## Limitations

- TomTicket only — no Zendesk, Freshdesk or other helpdesks
- Local stdio server; the token lives in your client config
- New listing (Aug 2026); single-maintainer open-source project
- Requires a TomTicket account and API access
- No hosted option — runs where you install it

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
