---
title: OmniSocials MCP - Multi-Platform Social Publishing
description: "Official hosted MCP server from the OmniSocials social media management platform: 42 tools that create, schedule, publish, and analyze posts across 11 platforms including Instagram, LinkedIn, TikTok, X, and YouTube from any MCP client."
category: Marketing
stars: "19 (github.com/OmniSocials/omnisocials-agent-skills)"
added: 2026-08-28
source: mcp.so feed
relevance: ★★★
tags: [mcp-server, social-media, scheduling, analytics, instagram, linkedin, tiktok, remote-mcp]
---

# OmniSocials MCP

**Official hosted MCP server from OmniSocials, a social media management platform.** 42 tools matching the full public API let an AI assistant create, schedule, publish, retry, and analyze posts across 11 platforms (12 channels with LinkedIn split into a personal profile and a company page) from a single Streamable HTTP endpoint. Auth is scoped API keys (`omsk_live_`/`omsk_test_`) or OAuth 2.1 with dynamic client registration; a local stdio package (`npx -y @omnisocials/mcp-server`) ships as an alternative.

```
Server type: Remote (Streamable HTTP); stdio via npm package
Auth: API key (scoped) or OAuth 2.1 with dynamic client registration
Endpoint: https://mcp.omnisocials.com/
Tools: 42 (posts, media, analytics, hashtag sets, social inbox, webhooks)
Pricing: Free tier; API key required for MCP access
Category: Marketing / Social media management
Built by: OmniSocials (omnisocials.com, GitHub OmniSocials/omnisocials-agent-skills, MIT)
```

## Why This Matters for Operators

Running a multi-platform launch usually means eleven browser tabs, eleven UIs, and a calendar that never matches what actually published. OmniSocials collapses that into one endpoint: the assistant holds the content plan, the account list, and the schedule in a single context, then drafts once and cross-posts to every channel with per-platform captions, media, and chained threads where each platform supports them.

Two details separate it from a thin wrapper. First, the analytics and inbox tools mean the assistant can both run and read a campaign: per-post and account-level stats, best-times-to-post guidance, and a social inbox for DMs, comments, and mentions. Second, webhooks notify on post lifecycle events (scheduled, published, failed), so an operator can wire the publish loop into automations instead of polling.

**The assistant can plan, publish, and measure the same campaign in one conversation, across every major network.**

## Tools & Capabilities

| Area | Capability |
|---|---|
| Posts | Create, update, delete, publish, and retry posts (`POST /v1/posts/create`, `/v1/posts/create-and-publish`, `/v1/posts/:id/publish`); read full post details including per-platform captions, media, and chained threads on X, Bluesky, Mastodon, and Threads |
| Accounts | List every connected social account for the workspace (`GET /v1/accounts`) |
| Media | Upload images, video, and PDFs (auto-split into carousel slides) with per-platform compatibility verdicts (`POST /v1/media/upload`); pass external URLs directly via `media_urls` |
| Analytics | Per-post and account-level stats, best-times-to-post recommendations |
| Hashtag Sets | Save and reuse tagged groups across posts |
| Social Inbox | Read and reply to DMs, comments, and mentions |
| Webhooks | Subscribe to post lifecycle events |

## Installation

```bash
claude mcp add omnisocials --transport http https://mcp.omnisocials.com/
```

Or the local stdio package, which requires Node.js 18+:

```bash
claude mcp add omnisocials -- npx -y @omnisocials/mcp-server
```

## Configuration

```json
{
  "mcpServers": {
    "omnisocials": {
      "type": "http",
      "url": "https://mcp.omnisocials.com/"
    }
  }
}
```

Create an API key in the OmniSocials app under Settings - API, pick the scopes the integration needs (start with `posts:write`, `media:write`, and `accounts:read`), and pass it as a query parameter or OAuth Bearer token. Social accounts are connected once through OAuth in the dashboard and then become available to every API key in the workspace; account connection cannot be done through the API.

## Business Relevance

- **Marketing operators** run a full content calendar across 11 platforms from one chat thread, with per-network scheduling and rescheduling.
- **Agencies** compose multi-client posting flows and pull per-account analytics without dashboard logins.
- **Social media managers** get best-time-to-post guidance plus a unified inbox for DMs, comments, and mentions.
- **E-commerce teams** coordinate launch campaigns across Instagram, TikTok, X, and LinkedIn with consistent captions and media compatibility checks.
- **Content operators** wire webhooks on post lifecycle events into internal automations instead of polling for status.

## Integration with CorpusIQ

OmniSocials handles the publish side; CorpusIQ handles the numbers behind the post. A composed workflow: the assistant reads Shopify sales and GA4 traffic via CorpusIQ connectors to pick the top-performing products, drafts a campaign in chat, schedules it across Instagram, TikTok, and X through OmniSocials, then returns a week later to pull post analytics from OmniSocials and join them with GA4 conversions and HubSpot pipeline movement from CorpusIQ for a full performance read. CorpusIQ's read-only business data and OmniSocials's read-write social execution are complementary halves of one measurement loop.

## Limitations

- Young listing: the MCP server and agent-skills repo (19 stars) launched in 2026, currently at release 1.21.0 with an active maintainer.
- API key required for all access; anonymous calls return 401 (verified live at the endpoint).
- Social accounts connect only through the OmniSocials dashboard, not through the API or MCP.
- Write actions publish to live accounts; scopes gate them, but a misdirected prompt can still act.
- Hosted service: publishing depends on OmniSocials availability and each platform's rate limits.
- Instagram, TikTok, Pinterest, stories, and reels require media; some platforms reject text-only posts.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [SocialRobot MCP - Social Media Scheduling and Analytics for AI Agents](/docs/hermes/mcp/servers/external/socialrobot-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
