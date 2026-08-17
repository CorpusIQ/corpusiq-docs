---
title: "RADAAR MCP - CorpusIQ Docs"
description: Social media management for AI agents. Publish, schedule, inbox and analytics across 20+ channels including Instagram, X, LinkedIn, TikTok and YouTube from Claude or ChatGPT.
category: Marketing
stars: n/a (new listing)
added: 2026-08-14
source: mcp.so
relevance: ★★★
tags: [social-media-management, social-scheduling, unified-inbox, social-listening, hashtag-research, analytics, marketing, remote-mcp]
---

# RADAAR MCP

**Remote MCP server (Streamable HTTP, OAuth)** — RADAAR's official bridge between MCP clients and its social media management platform. Read, create, schedule, and analyze content across 20+ channels, run a unified social inbox, and track keywords from Claude, ChatGPT, Cursor, or any agent — the same surface social teams get in the dashboard, exposed as tools.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect)
Endpoint: https://mcp.radaar.io
Tools: 6 tool modules — publishing_*, inbox_*, monitoring_*, analytics_*, utilities_*, settings_*/subscriptions_* (live tool list served from the endpoint)
Pricing: RADAAR workspace subscription
Category: Marketing / Social
Built by: RADAAR (radaar.io)
```

## Why This Matters for Operators

Social execution still eats operator time in dashboard hops: scheduling in one tab, inbox in another, analytics in a third, and the trending-hashtag or best-time-to-post lookup somewhere else. RADAAR MCP puts that entire loop in the assistant that already holds the brand calendar and the campaign context.

**Operators get the full social stack as one OAuth'd tool surface** — publishing, engagement, listening, and reporting — across the channels that matter, with agency-grade multi-brand workspaces, team roles, and RBAC. The same platform-MCP pattern as OnePostly, extended with a unified social inbox and listening included.

## Tools & Capabilities

The listing does not publish an extracted tool list (live tools are served from the endpoint); capabilities below are from RADAAR's published overview.

| Module | Purpose |
|---|---|
| `publishing_*` | Create, update, queue posts (images, carousels, reels, stories, threads, polls) with per-platform caption variations |
| `inbox_*` | Unified inbox: comments, DMs, SMS, reviews — reply, like/hide, rate sentiment, assign, label |
| `monitoring_*` | Keyword tracking, negative-keyword filters, language filters, sentiment rating, assignment |
| `analytics_*` | Channel and custom dashboards, granular metrics over custom date ranges |
| `utilities_*` | AI image generation, trending hashtags, best times to post, royalty-free stock library, branded URL shortener |
| `settings_*` / `subscriptions_*` | Multi-workspace switching, team roles (COMMUNITY_MANAGER, CONTENT_MANAGER, ANALYST), brand organization, billing |

Supported channels: Facebook, Instagram, X (Twitter), LinkedIn, TikTok, YouTube, Threads, Pinterest, Bluesky, Mastodon, Google Business Profile, and WordPress (20+ total).

## Installation

```bash
claude mcp add radaar --transport http https://mcp.radaar.io
```

The vendor publishes per-client setup snippets on the listing page (Claude Code, Codex, Cursor, VS Code).

## Configuration

```json
{
  "mcpServers": {
    "radaar": {
      "type": "http",
      "url": "https://mcp.radaar.io"
    }
  }
}
```

First connect opens a browser OAuth flow; the session is reused afterwards.

## Business Relevance

- **Social media managers and agencies** get scheduling, inbox triage, listening, and reporting in one conversational surface, with multi-brand workspaces and role-based access per team member
- **Founders and solopreneurs** run their own channels without a social tool specialist — the agent drafts, schedules, and reports
- **Performance marketers** pair post analytics with best-time-to-post recommendations and hashtag research in the same workflow
- **Content operators** generate AI images, pull stock assets, and shorten branded links without leaving the conversation

## Integration with CorpusIQ

RADAAR MCP pairs with CorpusIQ's analytics and CRM connectors to close the social loop. Post analytics from the `analytics_*` module feed the same reports GA4 and Google Ads data already power — one agent can correlate social performance with site traffic and paid spend across channels. HubSpot or LeadConnector contacts reached via DM or comments can be triaged against CRM records in the same session. For operators running a CorpusIQ social cadence, RADAAR is the execution layer where the publishing schedule actually lands.

## Limitations

- Brand new listing — submitted to mcp.so hours before this sweep; no track record yet
- Commercial — requires a RADAAR workspace subscription; no free MCP tier published
- No public repository; the server is closed-source and vendor-operated
- Live tool list is not published in the listing (served from the endpoint only)
- OAuth browser flow required on first connect

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
