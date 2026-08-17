---
title: DOS AI MCP
description: WhatsApp and Telegram AI assistant operations over MCP — projects, conversations, leads and analytics for chatbot operators, with no destructive tools by design.
category: Communication
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [whatsapp, telegram, chatbots, crm, lead-management, messaging, api-key, remote-mcp]
---

# DOS AI MCP

**Remote MCP server (Streamable HTTP, Bearer API key)** — DOS AI is a platform for AI assistants (chatbots) in WhatsApp and Telegram with a built-in CRM. The MCP endpoint exposes the same data a human operator sees in the cabinet: projects, conversations, messages, leads, analytics and balance — through 13 tools that carry no destructive operations by design.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (dos_sk_live_...)
Endpoint: https://dosai.pro/api/mcp
Tools: 13 (dosai_-prefixed, no destructive tools)
Pricing: starting balance granted on signup, no card required
Category: Communication
Built by: DOS AI (dosai.pro)
```

## Why This Matters for Operators

Chatbots on WhatsApp and Telegram are only useful if someone operates them: watching conversations, catching leads, correcting prompts, and handing the dialog to a human when the rules say so. The DOS AI MCP puts that operator loop in the agent itself. A CorpusIQ-style agent can read the conversations, file leads, update a bot's prompt, send an operator message into a live dialog, and pull conversion analytics — from any MCP client.

**Two design decisions make this safe to hand to an agent**: there is no delete-project, no payment, and no member management — the destructive tool list is empty and a test guards it — and every tool calls the public REST route over HTTP, so a read-only key stays read-only and project scoping applies exactly once. Keys can be scoped to a single project and to read-only access, and only a SHA-256 hash of the key is stored.

The OpenAPI spec, `llms.txt`, and a full public corpus (`llms-full.txt`) are published — agent-readable documentation as a first-class deliverable.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_projects` / `get_project` | Bot projects and their configuration |
| `get_prompt` / `update_prompt` | Read and revise a bot's instructions |
| `list_functions` | Functions the bot can call |
| `list_leads` / `get_lead` / `update_lead` | CRM leads with status and source |
| `list_conversations` / `get_messages` | Dialogs with filters and paging |
| `send_operator_message` | Interject into a live dialog as the operator |
| `get_analytics` | Dialogs, leads, conversion, response time |
| `get_balance` | Account balance and token history |

## Installation

```bash
# Register at dosai.pro, create a project, issue an API key in the cabinet
claude mcp add --transport http dosai https://dosai.pro/api/mcp \
  --header "Authorization: Bearer dos_sk_live_..."
```

Rate limit is 120 requests per minute per key with `Retry-After` on 429. Webhooks deliver new-lead, new-message and stage-change events to your own endpoint with signature verification.

## Configuration

```json
{
  "mcpServers": {
    "dosai": {
      "url": "https://dosai.pro/api/mcp",
      "headers": { "Authorization": "Bearer dos_sk_live_..." }
    }
  }
}
```

## Business Relevance

- **Chatbot operators** can supervise WhatsApp and Telegram assistants from any MCP client
- **Sales teams** get every conversation filed as a lead with source and status
- **Support leads** can interject into live dialogs as the operator when the rules say so
- **Growth teams** get conversion and response-time analytics per bot without a dashboard login

## Integration with CorpusIQ

DOS AI is the messaging front-end that feeds the CorpusIQ CRM backbone. Leads captured in WhatsApp or Telegram conversations can be pushed into HubSpot or LeadConnector through the CorpusIQ CRM connector, so a chat inquiry becomes a pipeline contact instead of a lost dialog. The CorpusIQ calendar connector closes the loop the platform already starts — DOS AI bots book Google Calendar slots natively, and CorpusIQ reads the same calendar for meeting context. Analytics from DOS AI (`get_analytics`) can sit beside CorpusIQ GA4 in cross-source reporting: bot dialogs versus site traffic, one attribution view.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- WhatsApp/Telegram only — no web or other messaging channels
- No destructive tools means deletions still happen in the human cabinet
- Rate limits (120 req/min per key) require pacing for heavy analytics pulls
- Hosted platform — conversation data lives on DOS AI infrastructure; webhooks help you take it out

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
