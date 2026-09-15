---
title: "SenderKit MCP - Transactional Messaging from Your Assistant"
description: "Official SenderKit MCP server for transactional and marketing messaging: send templated or raw emails, SMS, push, and web-push, manage templates, inspect delivery, and handle inbound addresses and domains. 18 tools, hosted endpoint or local stdio."
category: Communication & Email
stars: n/a (hosted)
added: 2026-08-25
source: mcpservers.org /all listing
relevance: ★★
tags: [mcp-server, email, sms, push, notifications, templates, transactional]
---

# SenderKit MCP

**Transactional notifications that live in a dashboard, dispatched from your assistant.** SenderKit is a transactional messaging platform (email, SMS, push, web-push). Its MCP server exposes the core operations as 18 tools: send a templated message or raw inline content, scaffold and edit templates, inspect message delivery, and manage inbound addresses and domains. Tool names are prefixed `senderkit_` so they never collide in multi-server setups.

```
Server type: Remote Streamable HTTP (hosted) or local stdio
Endpoint: https://mcp.senderkit.com
Tools: 18 (identical across hosted endpoint and local stdio server)
Docs: docs.senderkit.com/mcp
```

## Why This Matters for Operators

Template edits and test sends are the highest-friction part of notification work: a copy tweak means a deploy or a dashboard trip. SenderKit's MCP moves that loop into the chat where the work is being discussed. Every hosted tool declares an MCP `outputSchema` and returns `structuredContent` conforming to it, so results are machine-readable, with the same object serialized as JSON text for older clients.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `senderkit_send` | Send a templated message |
| `senderkit_send_raw` | Send raw inline content |
| `senderkit_context` | Server context and configuration |
| `senderkit_templates_list` / `get` / `create` / `regenerate` | Template lifecycle, including AI regeneration |
| `senderkit_messages_list` / `get` / `cancel_message` | Delivery inspection and cancellation |
| `senderkit_inbound_addresses_list` / `create` / `delete` | Inbound address management |
| `senderkit_inbound_messages_list` / `get` | Inbound message reading |
| `senderkit_inbound_domains_list` / `create` / `delete` | Inbound domain management |

No MCP prompts or resources are exposed, tools only.

## Installation

Hosted:

```json
{
  "mcpServers": {
    "senderkit": { "type": "http", "url": "https://mcp.senderkit.com" }
  }
}
```

A local stdio server is available for headless or air-gapped setups; the 18 tools are identical across both.

## Configuration

The hosted endpoint authenticates with your SenderKit account credentials or API key per the vendor's quickstart (docs.senderkit.com/mcp/quickstart). Sending uses the same templates and key prefixes your application already uses.

## Business Relevance

- **Marketing ops:** draft, edit, and send campaign messages from chat.
- **Lifecycle automation:** welcome, password-reset, and billing notices as agent actions.
- **Delivery visibility:** inspect message status without leaving the editor.
- **Inbound handling:** manage inbound addresses and domains for two-way flows.

## Integration with CorpusIQ

SenderKit's structured results pair with CorpusIQ connectors for attribution: join message sends and delivery status against GA4 or CRM data in CorpusIQ, track notification-driven conversions in HubSpot, and render send-volume dashboards from the structured outputs.

## Limitations

- Focused surface: sending, templates, delivery inspection, inbound management; no full campaign builder.
- Authentication details are account-specific; follow the vendor quickstart.
- Vendor docs describe the platform as developer-facing; agent authors and AI-coding-tool users are the stated audience.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [LiveSend MCP](/docs/hermes/mcp/servers/external/livesend-mcp)
- [MisarMail MCP](/docs/hermes/mcp/servers/external/misarmail-mcp)
