---
title: Graspil MCP
description: Telegram analytics, broadcast, and automation over MCP. Build reports, read funnels and referral stats, and manage broadcasts without opening the dashboard.
category: Marketing
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★
tags: [telegram, analytics, broadcast, automation, referral-tracking, community, marketing, remote-mcp]
---

# Graspil MCP

**Remote MCP server (Streamable HTTP, API key)** — Graspil's own MCP server connects an AI agent directly to your Telegram bots, channels, and groups. Build reports and dashboards, read stats and funnels, manage broadcasts and automations, and view conversation history and referral earnings — without opening the dashboard.

```
Server type: Remote (Streamable HTTP)
Auth: API key
Endpoint: Graspil-hosted MCP endpoint (graspil.com)
Tools: Reports, stats, funnels, broadcasts, automations, referrals
Pricing: Commercial; plan restrictions apply
Category: Marketing
Built by: Graspil (graspil.com)
```

## Why This Matters for Operators

Telegram has become a serious acquisition and community channel for operators — payment funnels, referral programs, broadcast marketing. But operating it means another dashboard, another login, another set of manual reports.

**Graspil MCP puts Telegram operations in plain language.** Ask "how many new users joined last week compared to the week before," "build a payment funnel report for June and save it," or "create a broadcast with this text and send it to all active users" — the agent calls the right tools and answers. The MCP server is a thin layer on the regular Graspil API, so the agent works with the same bots and permissions your API key allows.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Reports | List available events and resources (bots), build and preview reports |
| Stats | New-user counts, week-over-week comparisons |
| Funnels | Payment funnel reports by period |
| Referrals | Referral program earnings |
| Broadcasts | Create and send broadcasts to user segments |
| Automations | Manage automations from chat |

## Installation

```bash
claude mcp add graspil --transport http <graspil-mcp-endpoint> --header "Authorization: Bearer <api-key>"
```

Full documentation index at graspil.com/llms.txt; markdown versions of docs pages are available by appending `.md`.

## Configuration

```json
{
  "mcpServers": {
    "graspil": {
      "type": "http",
      "url": "<graspil-mcp-endpoint>",
      "headers": {
        "Authorization": "Bearer <api-key>"
      }
    }
  }
}
```

## Business Relevance

- **Community operators** run Telegram groups from the assistant they already use
- **Growth leads** pull funnel and referral reports without dashboard time
- **Content teams** schedule broadcasts conversationally
- **Founders** keep Telegram economics visible in daily agent workflows

## Integration with CorpusIQ

CorpusIQ itself runs on Telegram, so Graspil's surface is directly familiar. Graspil's funnel and referral analytics complement the CorpusIQ connectors: Graspil reads Telegram economics while CorpusIQ reads the business systems behind them (Stripe for payments, GA4 for traffic, Postiz for publishing). A composed workflow monitors Telegram funnel revenue through Graspil and reconciles it against Stripe charges through CorpusIQ.

## Limitations

- Commercial; plan restrictions apply exactly as through the dashboard or API
- API-key scoping means the agent inherits the key's bot permissions
- Telegram-only surface
- Brand new — no track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
