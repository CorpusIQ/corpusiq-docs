---
title: InstantReply MCP - Instagram, WhatsApp and Messenger Inbox
description: "Local MCP server that connects an agent to a real Instagram, WhatsApp or Messenger inbox. 29 annotated tools for conversations, contacts, WhatsApp template lifecycle (validate, submit, track), journey delivery and delivery debugging, with 11 prompt commands and scope-mapped API keys. npm package, MIT."
category: "Communication"
stars: 0 (new repo)
added: 2026-09-12
source: "chatmcp/mcpso #4083 + vendor page instantreply.co/mcp + npm @instantreply.co/mcp"
relevance: ★★
tags: [instagram, whatsapp, messenger, inbox, customer-support, sales, npm]
---

# InstantReply MCP

**Local MCP server (npm, stdio)** - connects an agent to a real Instagram, WhatsApp or Messenger inbox (the InstantReply AI-inbox product). Agents read conversations, draft and send replies, track leads, run the WhatsApp template lifecycle (validate, submit to Meta, monitor), trigger journeys and debug delivery failures - all through 29 tools that advertise `readOnlyHint` and `destructiveHint` so compliant clients confirm before writes.

```
Server type: Local (stdio via npx)
Auth: InstantReply API key (ir_live_...; test keys run send simulations only)
Scopes: conversations:read, messages:send, templates:write, templates:submit
Package: @instantreply.co/mcp (npm, v0.2.0)
Source: github.com/suleimandoescsec/instantreply-mcp (MIT)
Category: Communication
Built by: InstantReply (instantreply.co/mcp)
```

## Tools (29)

| Group | Tools |
|---|---|
| Inbox and messages | list_conversations, get_conversation, list_messages, send_message, assign_conversation, close_conversation |
| Contacts and channels | list_contacts, get_contact, update_contact, list_channels |
| Analytics and usage | get_analytics_summary, get_usage |
| WhatsApp templates | list_templates, get_template, validate_template, validate_template_draft, submit_template, submit_stored_template, delete_template, send_whatsapp_template |
| Journeys and delivery | trigger_journey, trigger_journey_batch, validate_journey_trigger, check_journey_status, list_journey_history, explain_delivery_failure |
| Developer ops | get_developer_onboarding, get_developer_capabilities, get_developer_limits |

## Prompts (11)

Slash-ready commands: /draft_reply, /summarize_conversation, /find_urgent_unanswered, /weekly_inbox_digest, /suggest_macros, /escalation_note, /audit_template_cost, /utility_rewrite_loop, /journey_recommendation, /image_to_whatsapp_template_brief, /debug_last_failure. The vendor also ships downloadable skill packs (WhatsApp operator, business-owner growth, best practices, API integration, creative studio).

## Connection

1. Generate a key: InstantReply dashboard, Settings, API Keys. Live keys work with tenant data; test keys only run documented send simulations.
2. Add the block to your client config:

```json
"instantreply": {
  "command": "npx",
  "args": ["-y", "@instantreply.co/mcp"],
  "env": { "INSTANTREPLY_API_KEY": "ir_live_..." }
}
```

3. Restart the client and ask in plain English, for example: "Find unanswered DMs from today, draft a reply for each, send only after I confirm."

## Safety model

Every tool maps to an API key scope - read tools need `conversations:read`, sends need `messages:send`, template submissions need `templates:submit`. Use a read-only key for observing agents and a full-scope key for sending agents; every tool advertises read and destructive hints so clients can gate writes.

## Verification (Sep 12, 2026 midday sweep)

Vendor MCP page documents the full 29-tool reference, 11 prompts and 2 resources; npm `@instantreply.co/mcp` live at v0.2.0; source repo github.com/suleimandoescsec/instantreply-mcp public under MIT (pushed Sep 12, 2026). The server is stdio local (no remote endpoint); the underlying REST API is documented at instantreply.co/api-reference. Note: the directory submission cites an older package name (`@instantreply/mcp`); the published package is `@instantreply.co/mcp`.

## See Also

- [Mobile Text Alerts MCP - Official SMS Sending for Agents](/hermes/mcp/servers/external/mobile-text-alerts-mcp)
- [Mellow Hub MCP - Multi-Network Social Publishing with Guardrails](/hermes/mcp/servers/external/mellow-hub-mcp)
