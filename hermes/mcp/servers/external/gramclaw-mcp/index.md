---
title: "GramClaw MCP - Telegram Outreach Workflow for Agents"
description: "Remote Telegram MCP server from GramClaw that turns a Telegram outreach workflow into agent tools: search and read chats, list contacts, send messages from the right connected account, run personalized broadcasts with safe throttling, create multi-step drip campaigns and move chats through a pipeline CRM with analytics."
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-10
source: mcpservers.org /all via r.jina.ai
relevance: ★★★
tags: [telegram, outreach, campaigns, broadcast, crm, communication, remote-mcp]
---

# GramClaw MCP

**Remote MCP server (Streamable HTTP, scoped API key)** - a hosted connector that gives your AI agent hands on Telegram. Instead of clicking around, you tell Claude "find everyone who asked about pricing this week and send them the follow-up" - the agent searches, drafts and sends through tools scoped to the accounts the key is allowed to act on.

```
Server type: Remote (hosted, Streamable HTTP)
Auth: API key in the URL (?key=gc_live_...), scoped read/send, revocable from Settings
Endpoint: https://gramclaw.com/api/mcp
```

## Tool Groups

| Group | What the agent can call |
|---|---|
| Search & read | Search messages, list and open chats, list contacts, pull conversation history |
| Send messages | Start a new chat or reply in an existing one - from the right connected account |
| Broadcast | Push a personalized message to a whole segment with safe throttling |
| Campaigns | Create multi-step drip campaigns, then check their status and results |
| Pipeline & CRM | Move chats between pipeline stages and set custom column values |
| Analytics | Ask for sends, reply rates and campaign performance and get numbers back |

## Connection

1. Create an API key in GramClaw → Settings → API Keys, with the scopes you want (read / send).
2. Add `https://gramclaw.com/api/mcp?key=gc_live_...` to Claude Desktop, Cursor or any MCP client.
3. Ask the agent to search, message, broadcast or launch a campaign.

The key both identifies you and authorizes the tools, scoped to the accounts it is allowed to act on. Access requires an active subscription or trial. Developers who prefer raw HTTP can use the REST API instead - both hit the same Telegram outreach engine.

## Verification (Sep 10, 2026 night sweep)

Endpoint `https://gramclaw.com/api/mcp` live-probed over JSON-RPC: anonymous initialize answered with JSON-RPC error -32001 "Invalid or missing GramClaw API key. Append ?key=gc_live_... to the MCP URL" - live, key-challenged endpoint (Jitsu/Taskfolk liveness class). Tool groups, scoping model and trial terms published on the directory listing.

## See Also

- [Soprano Connect MCP - Multi-Channel Business Messaging for Agents](/docs/hermes/mcp/servers/external/soprano-connect-mcp)
- [AssistantMail MCP - Managed Mailboxes for Agents](/docs/hermes/mcp/servers/external/assistantmail-mcp)
