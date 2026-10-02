---
title: BoldDesk MCP - Helpdesk Ticket Operations for AI Agents
description: Hosted MCP server from BoldDesk by Syncfusion that brings customer support operations into AI workflows. Agents create, update and reply to support tickets, retrieve message history, search contacts, groups and agents, and drive approval workflows through the MCP standard.
category: Business Operations
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [helpdesk, customer-support, ticketing, syncfusion, support-ops, oauth, streamable-http, remote-mcp]
---

# BoldDesk MCP

**Remote MCP server (Streamable HTTP, OAuth 2.0 or API key)** - the hosted BoldDesk connector from Syncfusion, a fully managed bridge between AI assistants and a production helpdesk. Agents create, update and reply to support tickets, retrieve conversation history, search contacts and agents, and run approval workflows from any MCP client.

```
Server type: Remote (Streamable HTTP, fully managed and hosted)
Auth: OAuth 2.0 or x-api-key header
Endpoint: https://your-subdomain.bolddesk.com/mcp
Tools: Ticket lifecycle, conversations, contact and agent search, approvals, activities
Pricing: BoldDesk plans (free trial available)
Category: Business Operations
Built by: Syncfusion (BoldDesk)
```

## Why This Matters for Operators

Support teams spend their day inside a helpdesk UI that AI assistants could not touch. BoldDesk's MCP server removes that wall: the same agent that drafts a reply can now file the ticket update, pull the message history for context and search who owns what, all inside the conversation. **The vendor publishes capability documentation but not a numbered tool list, so the live tool set is served from the endpoint on connect; the capabilities below are derived from the official BoldDesk MCP docs.**

Every tool call is scoped to the authenticated user's permissions and associated brands. If an account cannot make a change in the dashboard, the tool cannot make it either, so role-based control carries over to the agent unchanged.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Ticket creation and updates | Create, update and manage support tickets |
| Conversation replies | Reply to ticket conversations from the assistant |
| Ticket retrieval | Retrieve ticket details and full message history |
| Contact search | Search contacts by name or address |
| Group and agent search | Search groups and agents for assignment decisions |
| Approval workflows | Handle approval workflows from the chat |
| Activities | Create and track activities against tickets |

## Installation

```bash
claude mcp add --transport http bolddesk https://your-subdomain.bolddesk.com/mcp
```

The vendor documents setup for Claude Code, ChatGPT, GitHub Copilot and Code Studio. Replace the subdomain with your BoldDesk account subdomain (a mapped custom domain works too).

## Configuration

```json
{
  "mcpServers": {
    "bolddesk": {
      "url": "https://your-subdomain.bolddesk.com/mcp"
    }
  }
}
```

Auth notes: authenticate with OAuth 2.0 or by attaching an API key as the x-api-key header. The endpoint is per-account, never a shared public URL. All tool calls act as the signed-in user under their existing role and brand assignments.

## Business Relevance

- **Support team leads** run conversational ticket management instead of switching between chat and helpdesk tabs.
- **Customer-success operators** get real-time ticket insights and message history directly in an assistant for account reviews.
- **Ops managers** keep approval workflows human-gated because tool permissions mirror the dashboard roles.
- **Support automation builders** wire agents into reply drafting, ticket updates and activity tracking without a local server.

## Integration with CorpusIQ

BoldDesk covers the conversational layer of support operations; CorpusIQ covers the data layer. A support operator can ask an assistant to pull a customer's Stripe revenue and HubSpot tickets through CorpusIQ read-only connectors, then have BoldDesk update the ticket with the resolution and reply to the thread. CorpusIQ reads the business, BoldDesk runs the support workflow, and the operator never leaves the conversation.

## Limitations

- The vendor does not publish a numbered tool list or public endpoint for probing; the surface is documented as capabilities and served per-account on connect.
- Tool calls inherit the signed-in user's permissions, so automation depth depends on that user's role.
- Per-account subdomain endpoints mean agency or multi-tenant setups need one connection per BoldDesk account.
- No self-host route; the server is hosted by BoldDesk only.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Drag MCP - Gmail Shared Inbox Operations for AI Agents](/hermes/mcp/servers/external/dragapp-mcp)
- [Modem MCP - Customer Feedback Intelligence for AI Agents](/hermes/mcp/servers/external/modem-mcp)
