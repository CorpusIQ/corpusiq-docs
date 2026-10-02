---
title: PurrPlan MCP - Agent-Driven Social Scheduling and Inbox
description: Official remote MCP server for PurrPlan, the social media scheduler agents can drive. 18 tools with granular scopes cover planning, publishing, inbox and analytics across 12+ networks including LinkedIn, X, Instagram, TikTok and YouTube. Confirmation-gated outbound replies, audit logging, and per-scope tokens with rate limits.
category: Social Media Management
stars: n/a (official vendor)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [social-media, scheduling, publishing, social-inbox, analytics, marketing, remote-mcp, multi-network]
---

# PurrPlan MCP

**Remote MCP server (Streamable HTTP)** - the official PurrPlan endpoint that turns a social scheduler into agent tooling: plan, publish, inbox and analytics across 12+ networks (LinkedIn, X, Instagram, TikTok, Facebook, YouTube, Threads, Bluesky, Pinterest, Telegram, Mastodon). 18 tools with granular scopes, confirmation-gated outbound actions and full audit logging.

```
Server type: Remote (Streamable HTTP, protocol 2025-06-18)
Auth: Bearer token (created in-app) or OAuth 2.0 with DCR + PKCE
Endpoint: https://app.purrplan.ai/api/mcp (health check keyless at /api/mcp/health)
Tools: 18, scoped read / write / ai / media / inbox:read / inbox:reply / analytics:read
Pricing: Included in PurrPlan plans from EUR 9/mo (MCP from Pro); 7-day trial; EUR 597 lifetime
```

## Why This Matters for Operators

Social scheduling tools are built for humans clicking a calendar. PurrPlan is built for agents: every tool carries an explicit scope, outbound actions (replying to inbox messages, scheduled sends) require a confirmation flag, and everything is audit-logged in-app. **An operator can hand an agent the marketing calendar with inbox replies gated behind `inbox:reply`, keeping the reply scope on a separate token from publishing.**

The safety design is unusual for a social tool: inbox content is treated as data never as instructions, SSRF protection on all client-supplied URLs, and rate limits per surface (100 req/min API+MCP, 20/min AI, 30/min media). The lifetime deal (pay once, your agent posts forever) makes it the only scheduler with a one-time pricing option for agent-driven workflows.

## Tools & Capabilities

| Tool | Scope | Purpose |
|---|---|---|
| `list_workspaces` / `list_accounts` | read | Workspaces and connected social accounts with auth status |
| `list_posts` / `get_post` | read | Posts with per-network versions, filterable by status |
| `generate_ai_text` | ai | Copy generation in the workspace's brand voice |
| `create_draft_post` | write | Draft or scheduled post; array content = thread (X, Threads, Bluesky, Mastodon) or first comment |
| `create_stories` | write | Cascade of stories (Instagram, Facebook), up to 30 |
| `update_draft_post` / `delete_post` | write | Edit or delete drafts and scheduled posts |
| `upload_media_from_url` | media | Ingest an image or video from a URL (max 50 MB) |
| `list_inbox` / `get_inbox_thread` | inbox:read | Comments, DMs and mentions across networks |
| `manage_inbox_messages` | inbox:read | Mark read/unread, archive, assign |
| `reply_to_inbox_message` | inbox:reply | Send a real reply as the connected account (confirm:true required, hourly cap) |
| `get_analytics` | analytics:read | Followers, reach, impressions, engagement, clicks, per-network breakdown |
| `get_top_posts` | analytics:read | Best posts with audience and engagement curves |
| `plan_my_week` | write + ai | Turn a brief into N scheduled posts across the week |

## Installation

```bash
claude mcp add --transport http purrplan https://app.purrplan.ai/api/mcp
```

Create a token in the in-app MCP integration page (app.purrplan.ai/app/mcp-integration), pick scopes, then attach the token as a bearer authorization header. The health endpoint answers without auth for connection checks.

## Configuration

```json
{
  "mcpServers": {
    "purrplan": {
      "type": "http",
      "url": "https://app.purrplan.ai/api/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    }
  }
}
```

Tokens carry only the scopes you grant. Inbox replying and analytics are deliberately separate scopes, so a publishing token cannot read DMs and an inbox token cannot publish.

## Business Relevance

- **Marketing teams** run the content calendar from agent workflows with brand-voice generation.
- **Community managers** triage comments, DMs and mentions across networks in one inbox surface.
- **Analysts** get per-network reach, engagement and click breakdowns without exporting platform data.
- **Agencies** scope tokens per client workspace and per function.

## Integration with CorpusIQ

PurrPlan is the publishing layer; CorpusIQ is the measurement layer. An operator can schedule cross-network campaigns through PurrPlan while CorpusIQ dashboards attribute the business outcomes - the engagement data PurrPlan reports and the revenue and pipeline data CorpusIQ connects meet in one operating picture.

## Limitations

- New listing (repo created Sep 3, 2026); no license declared on the client repo.
- MCP access starts at the Pro plan; the free plan covers the web app only.
- `reply_to_inbox_message` carries an hourly cap, so real-time community response is throttled.
- French-first vendor; docs exist in FR and EN.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [BulkPublish MCP - Multi-Platform Social Publishing for Agents](/hermes/mcp/servers/external/bulkpublish-mcp)
- [Buska MCP - Social Listening and Buying Signals for AI Agents](/hermes/mcp/servers/external/buska-mcp)
