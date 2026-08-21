---
title: "Maeve Social MCP — Social Publishing with Scope-Gated Agent Access"
description: "Hosted MCP server from Maeve Social for planning, scheduling, media, analytics and social publishing: reading is open, drafting and scheduling need permission, and anything public or permanent must be confirmed by name before it runs."
category: Social Media Management
stars: n/a (new listing)
added: 2026-08-21
source: mcpservers.org
relevance: ★★★
tags: [social-media, scheduling, publishing, analytics, content-planning, instagram, tiktok, remote-mcp]
---

# Maeve Social MCP

**Give agents the context, keep control of the actions.** Maeve Social's hosted MCP server points Claude, Codex or Cursor at the live workspace — drafts waiting on media, the week's schedule, the last thirty days of analytics — so the agent answers from what is really in Maeve rather than a pasted screenshot. Reading is open; drafting and scheduling need permission; and anything public or permanent must be confirmed by name before it runs.

```
Server type: Remote (Streamable HTTP)
Auth: API scopes; publish requires mcp:dangerous scope + explicit confirmation
Endpoint: https://api.maevesocial.com/mcp (live-probed: HTTP 401 auth gate, the expected MCP pattern)
Pricing: 3 days free, then Maeve Social plans
Category: Social Media Management
Built by: Maeve Social (maevesocial.com)
```

## Why This Matters for Operators

Social teams run on context that lives in a platform: which drafts are waiting on media, what goes out this week, how last month's campaign performed. Agents without that context hallucinate schedules; agents with full write access eventually publish the wrong thing. **Maeve's scope model splits the difference deliberately** — read freely, draft with permission, publish only after a by-name confirmation — so the agent can do real work (fill the research rows, draft posts that open in the Composer, compare what's scheduled across platforms) without ever owning the publish button.

## Tools & Capabilities

The tool landscape follows the permission tiers:

| Tier | Capability |
|---|---|
| Read (open) | List drafts and their status, compare what's scheduled across platforms, list media, pull the last 30 days of analytics |
| Draft & schedule (permission) | Create drafts in the Composer, fill the workbench, propose calendar slots |
| Publish (`mcp:dangerous` + confirmation) | `publish_now` — requires an explicit confirm like `publish_now:cnt_8f3k2` before anything goes live |

What the agent does lands back in the surfaces the team already uses — drafts open in the Composer, scheduled posts show on the Calendar.

## Installation

Connect any MCP client to the workspace endpoint and authorize the scopes in the Maeve dashboard. Vendor walkthroughs for Claude, Codex and Cursor are published on the MCP feature page and in the setup guide.

## Configuration

```json
{
  "mcpServers": {
    "maeve-social": {
      "type": "http",
      "url": "https://api.maevesocial.com/mcp"
    }
  }
}
```

Scopes decide how far an agent reaches: read-only grants answer questions, drafting grants add the `mcp:dangerous` tier only when you choose it. Publishing still depends on the connected platform's API, so nothing bypasses platform constraints.

## Business Relevance

- **Social media managers** offload context-gathering ("what's waiting on media this week?") to the agent
- **Agencies** let client workspaces be read by agents without handing over publish rights
- **Content teams** get drafts pre-filled into the Composer from research the agent gathered
- **Operators who fear auto-publishing** get a by-name confirmation gate on every public action

## Integration with CorpusIQ

Maeve Social covers the publishing layer; CorpusIQ covers the business proof behind it. A composed workflow has Maeve's tools pull campaign analytics and schedule posts while CorpusIQ's GA4 connector ties those posts to site traffic and Stripe ties them to revenue — the agent can answer "what did last month's social push actually earn" across both surfaces. For teams running paid social, Meta Ads data in CorpusIQ pairs with Maeve's organic schedule for one channel view.

## Limitations

- MCP surface is posting-focused: no Inbox, approvals, client review or PDF reports through MCP (those live in the app, REST API and CLI)
- Publish confirmation is by name — extra friction by design
- 3-day trial, then a paid Maeve plan; hosted vendor platform
- Does not manage API keys or bypass platform/API constraints
- Brand new MCP listing (Aug 2026)

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
