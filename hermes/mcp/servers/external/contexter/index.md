---
title: "Contexter MCP - Shared Project Context Across AI Assistants"
description: "Hosted MCP server that gives a project one shared context across ChatGPT, Claude, Telegram, and any MCP client. Save results, share contexts with people who use their own AI, and deliver artifacts to Telegram groups through 26 OAuth-scoped tools."
category: Productivity
stars: n/a (new listing, github.com/maaakso/contexter-mcp)
added: 2026-08-29
source: "mcp.so GitHub issue #3812"
relevance: ★★
tags: [mcp-server, collaboration, knowledge, context-sharing, telegram, productivity, oauth, remote-mcp]
---

# Contexter MCP

**A hosted MCP server that gives a project one shared context across ChatGPT, Claude, Telegram, and any MCP client - save what matters in one assistant, continue it in another, and share it with people who use their own AI.** Today that means re-explaining the project at every hop, and the person you work with cannot pick it up at all. Contexter replaces the per-tool copies with one context: assistants read and write the same records, and humans join through their own assistants or a Telegram bot. 26 tools, OAuth 2.1 with dynamic client registration, free during early access.

```
Server type: Remote (Streamable HTTP), hosted
Auth: OAuth 2.1 with dynamic client registration (sign in through Telegram)
Endpoint: https://contexterai.com/mcp
Scopes: contexts:read, messages:read, artifacts:write
Tools: 26 (8 reading, 7 saving, 5 sharing, 6 removing)
Pricing: Free during early access
Category: Productivity / Collaboration
Built by: maaakso; repo github.com/maaakso/contexter-mcp (docs), registry io.github.maaakso/contexter
```

## Why This Matters for Operators

Operators run the same project through several assistants - planning in ChatGPT, drafting in Claude Code, discussing in a Telegram group - and every hop re-explains the project. The collaborator who uses their own AI cannot pick up the thread at all. Contexter gives the project one context instead of a copy per tool: save an assistant's result as an artifact, open it in a different assistant, and share the context with a teammate who reads it through their own assistant.

The sharing rail is designed around consent and proof. Share steps show how many records and whose a new member would read before an invitation is issued; invitations arrive as Telegram cards where you pick the recipient with the chat picker, so no link is ever printed into a chat. Deliver-to-chat never sends by itself - a confirmation card shows the chat, the text, and the readership count, and the message leaves only when you press it.

**Project context becomes one shared, permissioned surface across assistants and people.**

## Tools & Capabilities

| Group | Tools |
|---|---|
| Reading (8) | list_contexts, get_context_card, get_context_feed, list_records, list_sources, get_artifact, get_file, read_image_content |
| Saving (7) | save_artifact, save_file, create_context, add_records_to_context, update_artifact, update_context, set_context_notifications |
| Sharing (5) | share_context, revoke_context_access, check_share_audience, deliver_to_chat, invite_room_to_context |
| Removing (6) | remove_record_from_context, delete_record, leave_context, restore_record, delete_context, restore_context |

## Installation

Nothing to install. Add the endpoint as a custom connector in any client that speaks Streamable HTTP, then sign in through Telegram when the OAuth flow opens.

```bash
claude mcp add --transport http contexter https://contexterai.com/mcp
```

Per-client step-by-step guides are on the help page at contexterai.com.

## Configuration

```json
{
  "mcpServers": {
    "contexter": {
      "type": "http",
      "url": "https://contexterai.com/mcp"
    }
  }
}
```

The endpoint publishes discovery, dynamic client registration, and OAuth 2.1 metadata from the same origin, so the URL alone is enough - no API key. The token carries the scopes of whoever completed the Telegram sign-in, and anything that widens an audience waits for a human yes.

## Business Relevance

- **Founders and project leads** keep one living context for a project instead of re-explaining it in every assistant.
- **Teams using different assistants** share context with people who use their own AI, with per-person visibility.
- **Telegram-group operators** deliver assistant results into group chats with a confirmation card and readership count.
- **Client-facing operators** share a context with a counterparty and revoke access cleanly when the engagement ends.

## Integration with CorpusIQ

Contexter pairs with CorpusIQ's Telegram-centric operations: CorpusIQ runs its team coordination through Telegram topics, and Contexter's deliver_to_chat and invite_room_to_context tools let a CorpusIQ-driven assistant publish results into a group with the same confirmation-gate discipline CorpusIQ applies to outbound content. For multi-agent work, a CorpusIQ workflow can save research artifacts to a client context (save_artifact, save_file), share the context with the operator's own assistant (share_context with check_share_audience first), and keep the audit trail in Contexter's feed instead of email chains. The read tools give CorpusIQ's reporting loop a single queryable surface for everything saved across assistants.

## Limitations

- Early access - free now, pricing unannounced, and the product can change shape.
- Repo is docs-only (no server source); you trust the hosted endpoint.
- Tools are scoped to one person's contexts; the value compounds with adoption, not solo use.
- Telegram is the sign-in rail - no email sign-in today.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [n8n MCP Server - Workflow Automation](/docs/hermes/mcp/servers/external/n8n-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
