---
title: "DialogBrain MCP - Omnichannel Business Inbox"
description: "One URL turns a business workspace into MCP tools: answer WhatsApp, Telegram, Instagram, email and SMS, place calls, and keep contacts and tasks current."
category: "Business Operations"
stars: n/a (closed source, hosted service)
added: 2026-10-16
source: "chatmcp/mcpso issue #5515 (October 16, 2026 midday sweep)"
relevance: ★★★
tags: [customer-inbox, whatsapp, telegram, instagram, email, sms, calls, crm, oauth, remote-mcp]
last_updated: "2026-10-19"
---

# DialogBrain MCP

**A business inbox exposed as MCP tools. A DialogBrain workspace already holds the conversations a business has with its customers across WhatsApp, Telegram, Instagram, email and SMS, plus its contacts, calls, tasks and knowledge. Point an assistant at one URL and that workspace becomes callable tools - the same tools the company's own agents use, with the same permissions. Hosted remote server, OAuth 2.1 sign-in, nothing to install.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://api.dialogbrain.com/mcp/
Auth: OAuth 2.1 (PKCE, dynamic client registration, S256); one URL for every client, the workspace is chosen by who authenticates
Transport: Remote only - there is no package and no local process
Clients: Claude, ChatGPT, Cursor, VS Code, Devin Desktop (formerly Windsurf), Claude Desktop, Claude Code, Codex, Gemini CLI, Antigravity, Grok, or any MCP-over-HTTP client
Scope: one connection is scoped to one workspace, and everything the assistant reads or sends belongs to it
Publisher: DialogBrain (dialogbrain.com)
Registry: com.dialogbrain/dialogbrain v1.0.0 (official MCP registry)
Listing: chatmcp/mcpso issue #5515, October 16, 2026
```

## Why This Matters for Operators

A small business answers customers in five places and keeps the record of who they are in a sixth. An assistant that can only see a chat window cannot tell you who is still waiting on a reply, which conversation belongs to the account that just paid, or what was promised on last week's call. That context is spread across apps and it does not come to the model by itself.

DialogBrain treats the whole workspace as the unit of connection. The assistant gets the inbox, the contact record, the call history, the task board and the knowledge base through one authenticated URL, scoped to one workspace. The permission model is the same one the company's own agents run under, so the assistant sees exactly what that workspace sees and nothing from any other.

## What You Can Do Today

| Capability area | What the assistant can reach |
|---|---|
| Customer inbox | Read the conversations across WhatsApp, Telegram, Instagram, email and SMS, and send replies in the same threads |
| Contacts | Look up and search the contact record the conversations belong to |
| Calls | Place calls and work with call transcripts |
| Tasks | Read and update the task board that the conversations generate |
| Knowledge | Use the workspace knowledge base the agents answer from |
| Agents and calendar | Manage the workspace's AI agents and the calendar |

The server ships with six skills in a bundled Claude Code plugin (`claude plugin install dialogbrain@dialogbrain`) that know how to set up a widget, connect a channel, build an agent, run the task board and write a lead report. Exact tool names are served by the live endpoint at connection; the workspace, not the URL, carries the data.

## Installation

```bash
claude mcp add --transport http dialogbrain https://api.dialogbrain.com/mcp/
```

The vendor publishes a per-client walkthrough for Claude, ChatGPT, Cursor, VS Code, Devin Desktop, Claude Code, Codex, Gemini CLI, Antigravity and Grok. In Claude on the web it is Settings, then Connectors, then Add custom connector; in ChatGPT it is Plugins, then Add custom MCP server (the free plan works too). Antigravity is the one client that takes an API key from the start, because its OAuth for remote MCP does not hand the token on.

## Configuration

```json
{
  "mcpServers": {
    "dialogbrain": {
      "type": "http",
      "url": "https://api.dialogbrain.com/mcp/"
    }
  }
}
```

The URL is the same for every client and every workspace because the workspace is decided by who authenticates, not by the address. Treat the address as public and the credential as private. OAuth metadata resolves at `https://api.dialogbrain.com/.well-known/oauth-protected-resource` (resource `https://api.dialogbrain.com/mcp/`) and the authorization server names the authorize, token and dynamic-registration endpoints over PKCE S256.

## Business Relevance

- **Support and sales teams** see every customer channel in one assistant session and can answer, look up the contact and log the task without switching apps
- **Operations leads** get the same permission-scoped view their own agents use, so an assistant reply follows the same rules as a human one
- **Agencies** keep each client workspace separate: one URL, and who signs in decides which client's inbox the assistant reaches
- **Owners** can ask who is still waiting for a reply, what was promised on a call, or what the task board looks like, without exporting anything first
- **Multi-channel businesses** get WhatsApp, Telegram, Instagram, email and SMS in one tool surface instead of five integrations

## Integration with CorpusIQ

Conversations are one half of the picture and the numbers are the other. CorpusIQ connects the business systems over read-only tools - Stripe, QuickBooks, Shopify, GA4, Search Console, Google Ads and the rest - so an assistant can read what a customer asked in DialogBrain, then pull that customer's orders, invoices or traffic from a connector and answer with both the conversation and the figures in the same reply. DialogBrain holds the customer's words; CorpusIQ holds the business record they are checked against.

## Limitations

- **Hosted only:** there is no local stdio build and no package to self-host; the server is DialogBrain's and it is reached over HTTPS
- **Workspace required:** a DialogBrain workspace is the unit of connection, so there is nothing to probe without an account
- **Account and pricing:** the service has free and paid plans; the MCP connection is included with a workspace
- **Closed source:** the server is not open source, so the tool surface is whatever the vendor serves at connection
- **Brand new listing:** published to the official MCP registry at v1.0.0; treat the tool surface as the current revision

## FAQ

### Does the assistant see other workspaces?

No. A connection is scoped to one workspace and everything the assistant reads or sends belongs to it; which workspace you land in is decided by who authenticates, not by the URL.

### Do I need to install anything?

No. There is no package and no local process, and you add one URL to your client.

### Which clients are supported?

Claude, ChatGPT, Cursor, VS Code, Devin Desktop, Claude Desktop, Claude Code, Codex, Gemini CLI, Antigravity and Grok, plus any client that speaks MCP over HTTP. The vendor publishes a per-client guide.

### Is the server address a secret?

No. The address is the same for every client and every workspace; the credential is the secret.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
