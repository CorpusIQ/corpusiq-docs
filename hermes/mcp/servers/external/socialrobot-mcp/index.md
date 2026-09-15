---
title: "SocialRobot MCP - Social Media Scheduling and Analytics for AI Agents"
description: "Remote MCP server that schedules and analyzes social posts across Instagram, LinkedIn, X, TikTok, Facebook, Threads, Pinterest, Bluesky, and Mastodon - create, reschedule, delete, upload media, and pull analytics plus best-time-to-post insights from any AI assistant."
category: Marketing
stars: n/a (new listing)
added: 2026-08-26
source: mcp.so feed
relevance: ★★★
tags: [mcp-server, social-media, scheduling, analytics, instagram, linkedin, tiktok, remote-mcp]
---

# SocialRobot MCP

**Nine social platforms, operated from chat.** SocialRobot's hosted MCP server lets an AI assistant create, schedule, reschedule, and delete posts across Instagram, LinkedIn, X, TikTok, Facebook, Threads, Pinterest, Bluesky, and Mastodon - then pull account and post analytics, follower demographics, and best-time-to-post guidance. It is a remote Streamable HTTP server with OAuth 2.0 PKCE or API-key auth, and MCP access is included on every plan including the free tier.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.0 with PKCE (scoped) or API key
Endpoint: https://socialrobot.io/api/mcp
Tools: 18 (posts, analytics, media, platform extras)
Pricing: Free tier; MCP included on all plans
Category: Marketing / Social media management
Built by: SocialRobot (socialrobot.io, GitHub socialrobot-io/socialrobot-mcp)
```

## Why This Matters for Operators

Scheduling a multi-platform launch from a chat window removes the calendar-tab hop: the assistant holds the content plan, the account list, and the schedule in one context. SocialRobot's server makes that real with a single endpoint covering all nine networks, so an operator can ask for a LinkedIn post on Tuesday 9am EST, an X thread Thursday, and an Instagram Story Friday without opening a single platform app.

The analytics side is the differentiator: account-level analytics series, per-post analytics snapshots, follower demographics (country, seniority, industry on LinkedIn Pages), and personalized best-posting-time guidance for Instagram based on past performance. **The assistant can both plan and measure the same campaign in one conversation.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_connected_accounts` | List every connected social account for the authenticated user |
| `create_post` | Create one scheduled item publishing to one or more accounts (TikTok direct-post or inbox-draft modes) |
| `list_posts` / `update_post` / `delete_post` | Manage scheduled, draft, publishing, and published posts |
| `reschedule_post` | Move a post to a new future publication date |
| `get_media_upload_url` | Generate a presigned upload URL for image or video before posting |
| `get_account_analytics` / `get_post_analytics` | Account-level series and per-post platform metric sets |
| `get_posts_with_analytics` | Published posts with latest analytics snapshots and history |
| `get_follower_demographics` | Audience breakdowns (Instagram/Facebook/Threads followers; LinkedIn Page country, seniority, industry) |
| `instagram_best_post_times` | Personalized best-posting-time guidance from past performance |
| `tiktok_get_creator_info` | Creator nickname, avatar, privacy options, posting limits - call before TikTok posts |
| `linkedin_search_geo_locations` / `linkedin_search_people_mentions` / `linkedin_search_organizations` | LinkedIn Company Page targeting: geo locations, @mention resolution, org lookup |
| `pinterest_list_boards` / `pinterest_create_board` | Pinterest board management |

## Installation

```bash
claude mcp add socialrobot --transport http https://socialrobot.io/api/mcp
```

The first connection opens a browser OAuth window to approve scoped permissions (nothing publishes without approval); alternatively paste an API key from the SocialRobot dashboard.

## Configuration

```json
{
  "mcpServers": {
    "socialrobot": {
      "type": "http",
      "url": "https://socialrobot.io/api/mcp"
    }
  }
}
```

## Business Relevance

- **Marketing operators** run a full content calendar across nine platforms from one chat thread, with per-network scheduling and rescheduling.
- **Agencies** compose multi-client posting flows and pull per-account analytics without dashboard logins.
- **Social media managers** get follower demographics and best-time-to-post signals to inform content strategy.
- **E-commerce teams** coordinate launch campaigns across Instagram, TikTok, X, and LinkedIn with consistent captions and media.
- **Content operators** use the analytics tools to report reach and engagement without exporting from each platform.

## Integration with CorpusIQ

SocialRobot handles the publish side; CorpusIQ handles the numbers behind the post. A composed workflow: the assistant reads Shopify sales and GA4 traffic via CorpusIQ connectors to pick the top-performing products, drafts a campaign in chat, schedules it across Instagram, TikTok, and X through SocialRobot, then returns a week later to pull post analytics from SocialRobot and join them with GA4 conversions and HubSpot pipeline movement from CorpusIQ for a full performance read. CorpusIQ's read-only business data and SocialRobot's read-write social execution are complementary halves of one measurement loop.

## Limitations

- Brand new listing - no track record yet; MCP server launched with the current tool surface.
- Write actions (create/delete/reschedule) execute on connected accounts; approval scopes gate them, but a misdirected prompt can still act.
- Best-time-to-post and demographics depth vary by platform (LinkedIn requires a Company Page with 300+ followers for geo targeting).
- Hosted service - posting depends on SocialRobot platform availability and rate limits.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
