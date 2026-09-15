---
title: "WhatsMCP MCP - Real WhatsApp Numbers for AI Agents"
description: "Hosted remote MCP server that puts an AI agent on a real WhatsApp number: link a number, mint a workspace-scoped key, and agents send and read messages over JSON-RPC. OAuth or API key auth, per-number message/contact/call pages, inbound webhooks, and plan-capped usage. Verified and featured on mcp.so."
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 morning) + vendor docs at whatsmcp.com/docs/mcp (re-check promoted after the Sep 14 evening disposition)"
relevance: ★★★
tags: [whatsapp, messaging, webhooks, customer-communication, numbers, oauth, api-key, remote-mcp]
---

# WhatsMCP MCP

**An agent that answers on your real WhatsApp number.** WhatsMCP exposes regular WhatsApp accounts to LLM agents over JSON-RPC: a complete Model Context Protocol server that turns phone numbers into addressable tools. Link a number, mint a key, and the assistant sends and reads messages in the workspace's plan caps.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect) or a workspace-scoped API key (Bearer or x-api-key header)
Endpoint: https://app.whatsmcp.com/mcp
Tools: plan-dependent tool set served from the endpoint (the directory listing shows no extracted list; the console lists which tools each plan includes)
Pricing: free plan with usage caps; paid plans raise the caps
Category: Communication & Email / WhatsApp
Built by: WhatsMCP (whatsmcp.com), repo github.com/whatsmcp/mcp
```

## Why This Matters for Operators

WhatsApp is where customers already are, and the gap between "customer sends a message" and "agent replies" is the inbox hours an operator cannot staff. WhatsMCP puts an AI agent on a real WhatsApp number, so the assistant reads incoming messages, drafts and sends replies, and works through per-number message, contact and call pages in the console.

The security model is workspace-scoped: the key is the workspace, every tool is scoped to it, there is no tenant argument to pass, and no way for one workspace to reach another's messages. OAuth clients register through the server's own metadata and are approved in the console, revocable one client at a time. Inbound webhooks deliver messages to the operator's endpoint for integration into existing systems.

## Tools & Capabilities

The live tool list is served from the endpoint after connection, and the console's Help page lists which tools each plan includes. The documented capability surface:

| Area | What it covers |
|---|---|
| Messages | Send and read WhatsApp messages from linked numbers |
| Accounts | List linked WhatsApp accounts per workspace |
| Contacts | Per-number contact pages in the console |
| Calls | Per-number call pages in the console |
| Webhooks | Inbound delivery endpoint with recent-attempt visibility |
| Usage | Messages sent against plan caps |

## Installation

```bash
claude mcp add --transport http wamcp https://app.whatsmcp.com/mcp
```

Then run `/mcp` in Claude Code, pick Authenticate, and sign in via the browser window (or `claude mcp login wamcp` from the shell). Setup path: create a workspace, link a number, mint a key (optional for OAuth clients), optionally point a webhook at your endpoint.

## Configuration

```json
{
  "mcpServers": {
    "wamcp": {
      "type": "http",
      "url": "https://app.whatsmcp.com/mcp"
    }
  }
}
```

Clients that cannot sign in (curl, CI, no OAuth) use a key in a header instead: `Authorization: Bearer <key>` or `x-api-key: <key>`.

## Business Relevance

- **Support teams** get a WhatsApp inbox the assistant can triage and answer with plan-capped usage.
- **Founders** get a personal line an agent monitors, with human review in the console.
- **Operations teams** get webhooks that pipe WhatsApp messages into existing systems.
- **Agencies** get per-workspace isolation so one assistant serves multiple clients without cross-access.

## Integration with CorpusIQ

WhatsMCP carries the conversation; CorpusIQ carries the facts. A support workflow pairs them: the agent answers a WhatsApp inquiry through WhatsMCP, pulls the customer's order state from CorpusIQ's Shopify or Stripe connectors, and confirms delivery details from the books via QuickBooks, all read-only and all in one session. The webhook layer means the same pipeline can log every interaction next to the CRM record in HubSpot through CorpusIQ, keeping the WhatsApp thread and the business data in one view.

## Limitations

- Tool list is account-gated: the exact tool names are served after connection, and the free plan caps usage.
- WhatsApp platform restrictions apply to business messaging (template rules for marketing and re-engagement).
- Hosted service only; no self-host option published.
- Directory listing still shows "No tools detected," so the capability surface above is derived from the vendor docs.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
