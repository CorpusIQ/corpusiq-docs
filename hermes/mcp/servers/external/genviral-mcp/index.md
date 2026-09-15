---
title: Genviral MCP - Social Media Creation and Publishing
description: "Official hosted MCP server from Genviral: 16 tools across four OAuth scopes that let AI assistants generate images, videos and slideshows, write captions, and schedule or publish posts across 10 social platforms."
category: Marketing
stars: "n/a (no public repo)"
added: 2026-08-29
source: mcp.so feed
relevance: ★★★
tags: [mcp-server, social-media, content-creation, scheduling, publishing, analytics, oauth, remote-mcp]
---

# Genviral MCP

**Official hosted MCP server from Genviral, a social media creation and scheduling platform.** 16 tools across four OAuth scopes let an AI assistant read connected accounts and analytics, generate images, videos and slideshows in Genviral Studio, prepare posts, and schedule or publish them across 10 platforms (TikTok, Instagram, YouTube, Pinterest, LinkedIn, Facebook, X, Bluesky, Mastodon, Telegram) from one Streamable HTTP endpoint. OAuth binds each connection to a single workspace with scoped, revocable permissions, and every write carries an idempotency key so a retrying agent cannot post the same thing twice.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth with 4 scoped permissions (context:read, content:write, posts:publish, media:generate)
Endpoint: https://mcp.genviral.io/mcp
Tools: 16 (account reads, analytics, content library, post preparation, publishing, AI media generation)
Pricing: Free account; media generation spends credits, connected-account limits follow the plan
Category: Marketing / Social media management
Built by: Genviral (genviral.io)
```

## Why This Matters for Operators

Most social MCP servers can only schedule content you already made somewhere else. Genviral closes the whole loop inside one assistant session: it reads what already performed, generates the next batch in Studio, writes the captions, and queues it across 10 platforms, then returns analytics through the same connection so the next batch is written against what actually worked.

Two details matter for teams. First, the four OAuth scopes are approved per connection on a Genviral consent screen, so an agency can hand a client's assistant read-only analytics while keeping publish and credit-spending generation to itself. Second, publishing is always deliberate: publish_post is the only tool that can reach an audience, every write requires an idempotency key, and the connection is scoped to one workspace.

**An operator can run the entire plan, create, publish, measure loop from a chat thread without opening a single platform dashboard.**

## Tools & Capabilities

| Scope | Tools |
|---|---|
| context:read | `get_context` (accounts, workspaces, plan, credit balance, Studio models), `list_posts` (scheduled, drafted and published posts with per-account delivery status), `get_analytics` (post and account performance plus tracked accounts), `research_trends` (trend briefs for a niche, TikTok slideshow previews), `browse_library` (files, folders, influencer characters, image packs, templates, slideshows), `get_job` (render, generation and analytics refresh status) |
| content:write | `upload_media` (images and video into the library), `manage_library` (folders), `manage_assets` (image packs and reusable slideshow templates), `manage_slideshow` (duplicate, edit, render, delete, regenerate a single slide), `manage_analytics_targets` (accounts tracked for analytics), `create_post` (media, caption, per-platform settings, target accounts, schedule), `update_post` (reschedule, edit, retry, delete) |
| posts:publish | `publish_post` (commit a prepared post now or hand it to the scheduler) |
| media:generate | `generate_slideshow` (multi-slide carousel from a brief, or import one from TikTok, then render), `generate_studio_media` (images and videos in AI Studio from a prompt or reference image) |

## Installation

```bash
claude mcp add --transport http genviral https://mcp.genviral.io/mcp
```

Run `/mcp` afterwards to complete the OAuth sign-in. The vendor publishes per-client walkthroughs for Claude apps, ChatGPT, Cursor and VS Code.

## Configuration

```json
{
  "mcpServers": {
    "genviral": {
      "type": "http",
      "url": "https://mcp.genviral.io/mcp"
    }
  }
}
```

On first connect the client opens a Genviral consent screen where you sign in, pick the workspace the connection is bound to, and approve the scopes. There is no API key to paste. Clients that support discovery can read the endpoint, tool list and scopes from https://www.genviral.io/.well-known/mcp/server-card.json.

## Business Relevance

- **Marketing operators** run a weekly content calendar across 10 platforms from one chat thread, with trend research feeding the briefs.
- **Founders** turn a launch doc or changelog already in the conversation into drafted LinkedIn and X posts without leaving the assistant.
- **Agencies** bind each client connection to its own workspace and scope permissions per assistant, so draft-only assistants can never publish.
- **E-commerce teams** generate product slideshows and videos in Studio and queue them to TikTok, Instagram and Pinterest on a schedule.
- **Content operators** close the loop with post analytics returned through the same connection that queues the next batch.

## Integration with CorpusIQ

Genviral handles the social execution; CorpusIQ handles the business numbers behind it. A composed workflow: the assistant reads Shopify sales and GA4 traffic through CorpusIQ connectors to pick the top performers, generates slideshows and captions through Genviral Studio tools, queues the week across Instagram, TikTok and X, then joins Genviral post analytics with GA4 conversions and HubSpot pipeline movement from CorpusIQ for a full revenue-attributed read. CorpusIQ's read-only business data and Genviral's read-write social loop are complementary halves of one measurement cycle.

## Limitations

- Brand new listing with no public repo and no track record; treat the 16-tool contract as vendor-published.
- Remote only: there is no self-hosted or local stdio option.
- Media generation spends credits, and connected-account limits follow the plan tier, so heavier automation needs a paid plan.
- OAuth only: no API key mode for the MCP server (the separate Genviral CLI and Partner REST API use keys).
- Writes go to live accounts; scopes gate them, but a misdirected prompt in a publish-scoped connection can still act.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [OmniSocials MCP - Multi-Platform Social Publishing for AI Agents](/docs/hermes/mcp/servers/external/omnisocials-mcp)
- [SocialRobot MCP - Social Media Scheduling and Analytics for AI Agents](/docs/hermes/mcp/servers/external/socialrobot-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
