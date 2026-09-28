---
title: Odichat MCP - WhatsApp and Instagram Inbox for Agents
description: "Odichat's MCP connector gives agents 126 tools over the WhatsApp, Instagram and Facebook business inbox, with sales pipeline updates."
category: Business Operations
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + odichat.app blog"
relevance: ★★★
tags: [whatsapp, instagram, facebook, business-inbox, sales-pipeline, customer-support, remote-mcp]
---

# Odichat MCP

**A 126-tool connector that lets an agent run the entire business inbox.** Odichat's MCP connector links an AI assistant directly to an Odichat account, giving it 126 tools to view and manage the WhatsApp, Instagram and Facebook business inbox: search conversations, identify unanswered contacts, assign conversations to teams, update the sales pipeline and automate follow-ups. The MCP URL includes the operator's personal token and must be treated like a password.

```
Server type: Remote (Hosted)
Auth: personal token embedded in the per-account MCP URL
Endpoint: per-account URL from the Odichat app
Tools: 126 (inbox, contacts, pipeline, follow-ups)
Pricing: Odichat plans
Category: Business Operations / Messaging
Built by: Odichat (odichat.app)
```

## Why This Matters for Operators

Businesses that sell through WhatsApp, Instagram and Facebook live inside those inboxes, and missed follow-ups are lost revenue. Odichat's connector turns the triage problem into a conversation: ask for all open conversations, ask which contacts never got an answer, ask the agent to assign a conversation to the sales team, and it does the work inside Odichat rather than just describing the data.

The connection model is two minutes and no developers, but the security note is real: the MCP URL carries a personal token, so it must be stored like a credential and never shared.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Conversations | Search and read WhatsApp, Instagram and Facebook threads |
| Contacts | Identify unanswered contacts and conversation state |
| Pipeline | Update the sales pipeline from conversation context |
| Follow-ups | Automate follow-up sequences |
| Assignment | Route conversations to teams |

## Installation

Take the personal MCP URL from the Odichat app and add it in any MCP client:

```bash
claude mcp add odichat <your-personal-odichat-mcp-url>
```

The same URL works with ChatGPT and Claude Code. Vendor docs are currently in Spanish at odichat.app.

## Configuration

```json
{
  "mcpServers": {
    "odichat": {
      "type": "http",
      "url": "<your-personal-odichat-mcp-url>"
    }
  }
}
```

## Business Relevance

- **Sales teams** catch unanswered prospects before they churn to a competitor
- **Support teams** triage three messaging networks from one chat surface
- **Founders** run WhatsApp-first businesses with agent-driven follow-ups
- **Agencies** manage client inboxes per account without cross-bleed

## Integration with CorpusIQ

Odichat pairs with CorpusIQ's CRM connector: conversations resolved in Odichat update the sales pipeline, and CorpusIQ reads the pipeline through HubSpot or LeadConnector for recaps. The inbound-communication monitoring doctrine can watch Odichat alongside Gmail, with CorpusIQ triaging which conversations need human escalation.

## Limitations

- The MCP URL embeds a personal token; handle it as a secret
- Primary documentation is Spanish-language today
- Single inbox platform focus (Meta messaging networks)
- New listing; tool surface is large but young

## FAQ

### How does the connector authenticate?

The per-account MCP URL embeds a personal token, so it must be treated like a password.

### How many tools does it expose?

126 tools across conversations, contacts, pipeline and follow-ups.

### Which networks does it cover?

WhatsApp, Instagram and Facebook business inboxes managed in Odichat.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
