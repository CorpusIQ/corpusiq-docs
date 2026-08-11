---
title: DripRaven MCP
description: WhatsApp Business campaign automation for AI agents — import contacts, send approved templates, schedule broadcasts, and read delivery rates via the official WhatsApp Business API
category: Marketing
stars: 0 (brand new)
added: 2026-08-11
source: mcpservers.org
relevance: ★★
tags: [whatsapp, messaging, campaigns, sms, marketing, automation]
---

# DripRaven MCP

**Run WhatsApp Business campaigns from any AI assistant.** Import and segment contacts, send approved templates, schedule broadcasts, and read delivery rates — all through the official WhatsApp Business API via MCP.

```
Server type: Remote (Streamable HTTP)
Auth: API token
Pricing: Starter $49/mo (5K msgs), Growth $149/mo (30K msgs), Scale $399/mo (150K msgs)
Category: Marketing / Messaging
```

## Why This Matters for Operators

WhatsApp has 2B+ users and 98% open rates — it's the highest-engagement messaging channel available. But running WhatsApp campaigns traditionally requires either a dedicated dashboard or complex API integration. DripRaven MCP lets AI agents manage the full campaign lifecycle: segment contacts, write and send template-based messages, schedule drip sequences, and analyze delivery rates — all from Claude, ChatGPT, or any MCP client.

This is the first WhatsApp-specific marketing MCP server. For operators running webinars, product launches, or event-triggered messaging, this eliminates the dashboard altogether.

## Tools & Capabilities

| Capability | Description |
|---|---|
| **Contact Management** | Import, segment, and manage contact lists |
| **Template Messaging** | Send approved WhatsApp Business templates |
| **Campaign Scheduling** | Schedule drip sequences (before, during, after events) |
| **Broadcast Sending** | Send bulk messages through official WhatsApp API |
| **Delivery Analytics** | Read delivery rates, read receipts, and engagement data |
| **Multi-Platform** | Works with Claude, ChatGPT, Claude Code, Cursor, OpenClaw |

## Configuration

```json
{
  "mcpServers": {
    "dripraven": {
      "type": "streamableHttp",
      "url": "https://api.dripraven.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_DRIPRAVEN_API_KEY>"
      }
    }
  }
}
```

## Getting Started

1. **Sign up** at [app.dripraven.com](https://app.dripraven.com/onboarding)
2. **Connect your WhatsApp Business number** through Meta's approval process
3. **Get API token** from your DripRaven dashboard
4. **Add config** to your MCP client
5. **Start prompting**: "Import my webinar registrants, segment by timezone, schedule reminder drips 24h before and 1h before, and send them via WhatsApp"

## Use Cases for Business Operators

- **Webinar operators**: Schedule pre-event reminder drips to boost attendance
- **Product launches**: Send launch sequences to segmented contact lists
- **E-commerce**: Abandoned cart recovery via WhatsApp (higher conversion than email)
- **Agencies**: Manage client WhatsApp campaigns from a single AI agent
- **Event organizers**: Day-of coordination via scheduled WhatsApp messages

## Pricing

| Plan | Price | Messages/mo | Contacts | Numbers | Seats |
|---|---|---|---|---|---|
| Starter | $49/mo | 5,000 | 2,500 | 1 | 1 |
| Growth | $149/mo | 30,000 | 25,000 | 3 | 5 |
| Scale | $399/mo | 150,000 | 100,000 | 10 | Unlimited |
| Enterprise | Custom | Custom | Custom | Custom | Custom |

Note: You pay Meta directly for WhatsApp message costs. DripRaven is the software layer on top.

## Limitations

- Requires WhatsApp Business API approval (Meta's process)
- Template messages must be pre-approved by Meta
- Brand new server (August 2026) — may have rough edges
- Not open source (commercial SaaS)
- WhatsApp-specific; does not cover iMessage, Telegram, or other messaging platforms

## See Also

- [JaxSuite AI MCP](/hermes/mcp/servers/external/jaxsuite-ai-mcp/) — Cold email outreach + CRM
- [DripRaven Homepage](https://dripraven.com)
- [DripRaven YouTube Channel](https://youtube.com/@dripraven) — MCP walkthroughs
