---
title: "Mobile Text Alerts MCP - Official SMS Sending for Agents"
description: "Official remote MCP server from Mobile Text Alerts. Agents send and schedule SMS, manage subscribers and groups, and complete carrier registration from any MCP-compatible assistant - business texting for broadcast messages, reminders and subscriber flows."
category: Communication
stars: n/a (new listing)
added: 2026-09-11
source: mcp.so feed
relevance: ★★
tags: [sms, texting, business-communication, marketing, notifications, remote-mcp]
---

# Mobile Text Alerts MCP

**Remote MCP server (Streamable HTTP, bearer auth)** - the official MCP server from Mobile Text Alerts, an SMS platform for business texting. Agents send and schedule SMS, manage subscribers and groups, and complete carrier registration from any MCP-compatible assistant, which fits broadcast announcements, appointment reminders and subscriber-list workflows.

```
Server type: Remote (Streamable HTTP)
Auth: Authorization header (account credential from the vendor dashboard)
Endpoint: https://mcp.mobile-text-alerts.com/mcp
Tools: Live tool list requires an account key - the listing documents send/schedule SMS, subscriber and group management, and carrier registration
Pricing: Vendor plans at mobile-text-alerts.com
Category: Communication
Built by: Mobile Text Alerts (official)
```

## Capabilities

| Capability | Purpose |
|---|---|
| Send SMS | Send a text message to one or many recipients |
| Schedule SMS | Queue a message for a future send time |
| Manage subscribers | Add, remove and organize contacts on lists |
| Manage groups | Create and maintain recipient groups for broadcasts |
| Carrier registration | Complete carrier registration workflows (A2P 10DLC-style compliance) from the assistant |

The listing is the official vendor submission (verified and featured badges on mcp.so); the exact live tool names surface only after connecting with an account key.

## Connection

1. Create a Mobile Text Alerts account and obtain your credential from the vendor dashboard.
2. Add the endpoint to any MCP client as a remote Streamable HTTP server with the Authorization header.
3. Claude Code one-liner - `claude mcp add mobile-text-alerts-sms --transport http https://mcp.mobile-text-alerts.com/mcp`
4. First moves - list groups and subscribers, then draft a message, validate it, and schedule the send.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: anonymous initialize returned `{"error":"Unauthorized","message":"Missing or invalid Authorization header"}` - live and auth-gated exactly as documented. The vendor's main site has no /mcp docs page (404), so the mcp.so listing remains the canonical public surface for this server; the tool names above are drawn from the listing's own description rather than a published tool schema.

## See Also

- [Soprano Connect MCP - Multi-Channel Business Messaging for Agents](/hermes/mcp/servers/external/soprano-connect-mcp)
- [Comunicate MCP - Press Release Distribution for Agents](/hermes/mcp/servers/external/comunicate-mcp)
- [GramClaw MCP - Telegram Outreach Workflow for Agents](/hermes/mcp/servers/external/gramclaw-mcp)
