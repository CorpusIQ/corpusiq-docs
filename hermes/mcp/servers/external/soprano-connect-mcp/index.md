---
title: Soprano Connect MCP - Multi-Channel Business Messaging for Agents
description: Self-hosted MCP server over the Soprano Connect CPaaS - SMS, voice, RCS, WhatsApp templates, Viber, push and email with batch sending, status lookups and pluggable per-request upstream auth. MIT, Python.
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [sms, whatsapp, rcs, messaging, communication, cpaas, self-hosted]
---

# Soprano Connect MCP

**One MCP server across every messaging channel an operator runs** - build agents that send SMS, voice, RCS, WhatsApp template messages, Viber, push notifications and email through the Soprano Connect platform. You run it yourself (stdio or deployed behind an ALB, Lambda Function URL or API Gateway), with upstream credentials supplied per request and never stored.

```
Server type: Self-hosted (Python 3.12, uv) - stdio or Streamable HTTP
Auth: Pluggable upstream auth per channel - API Key, OAuth2 client credentials, Basic, Legacy OAuth2
Install: git clone soprano-mcp/mcp && uv sync && uv run mems-mcp --transport stdio
Endpoint: /mcp on your deployment (http://127.0.0.1:8000 locally)
License: MIT
Built by: Soprano Design (enterprise CPaaS)
```

## Why This Matters for Operators

Customer communication tools multiply: SMS here, WhatsApp there, email somewhere else - each with its own console and API. **Soprano Connect collapses them into one tool surface an agent can use**: one `send_message` call reaches any channel, batch and broadcast tools handle campaign volume, and status lookups give delivery truth instead of fire-and-forget. Because it is self-hosted with per-request credentials selected by the caller, the operator keeps full control of which channels and credentials any agent session may touch.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `send_message` | Send one message over any configured channel |
| `send_batch` / `send_broadcast` | Campaign sending at volume |
| `get_message_status` / `get_batch_status` | Delivery status and batch progress |
| `sms` / `voice` / `rcs` / `viber` / `pushnotification` / `email` | Per-channel send primitives |
| `list_whatsapp_templates` | WhatsApp template catalogue (WABA) |
| `upload_whatsapp_media` / `delete_whatsapp_media` | Media management for WhatsApp sends |

## Installation

```bash
git clone https://github.com/soprano-mcp/mcp.git
cd mcp && uv sync
uv run mems-mcp --transport stdio
# or serve over HTTP:
uv run mems-mcp --transport streamable-http   # http://127.0.0.1:8000/mcp
```

## Configuration

Supply Soprano Connect upstream credentials in the server's environment or per request. For deployed use, point your MCP client at the server's `/mcp` endpoint behind an ALB, Lambda Function URL or API Gateway, with access control at your own layer - the server itself holds no stored secrets.
