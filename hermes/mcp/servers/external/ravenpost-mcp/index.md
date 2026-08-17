---
title: Ravenpost MCP
description: Multi-platform social publishing over MCP — schedule and publish to Instagram, TikTok, X, LinkedIn, Facebook, Telegram, Threads, Bluesky and YouTube with network-accurate previews before anything goes live.
category: Marketing
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★★
tags: [social-media, scheduling, publishing, instagram, tiktok, cross-platform, oauth, remote-mcp]
---

# Ravenpost MCP

**Remote MCP server (Streamable HTTP, OAuth)** — Ravenpost exposes a hosted multi-platform social scheduler to any MCP client: list connected accounts, upload or reshape media, preview a post exactly as each network will render it, then publish now, schedule it, or drop it into a weekly posting queue across Instagram, TikTok, X, Telegram, Facebook, LinkedIn, Threads, Bluesky and YouTube.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (resource server) or personal access token
Endpoint: https://api.ravenpo.st/mcp
Tools: 21 across accounts, posts, media, analytics, reference
Pricing: free plan covers trial; Agency plan for multi-workspace
Category: Marketing
Built by: Ravenpost (ravenpo.st) — registry name st.ravenpo/ravenpost
```

## Why This Matters for Operators

Publishing from an agent is easy; publishing right is not. Caption limits differ per platform, thread models do not exist everywhere, some networks reject posts without media, and a platform-shape crop that looks fine in a preview can cut the subject when it goes live. Ravenpost's core mechanism is `preview_post` — a write-nothing render of the post as each destination will show it, plus the warnings a picture cannot carry.

**Preview-before-publish is the safety gate**: every tool declares read-only or destructive hints, so the client can tell what a call will do before allowing it. The server refuses to guess workspaces — a credential that can act in more than one workspace errors and names them rather than posting one client's content to another's accounts. Media reformats to the target platform shape, and `create_variants` cuts one image into several platform canvases at once, cropping on the subject rather than the middle.

For operators running recurring content, the weekly queue slots plus `best_times` (measured from the workspace's own posts, with an explicit not-enough-data answer) turn a posting tool into a cadence engine.

## Tools & Capabilities

| Group | Tools |
|---|---|
| Accounts | `list_workspaces`, `list_accounts` |
| Posts | `list_posts`, `get_post`, `preview_post`, `create_post`, `update_post`, `delete_post`, `schedule_post`, `publish_post` |
| Media | `upload_media`, `create_media_upload`, `attach_media`, `create_variants`, `list_media`, `image_formats` |
| Analytics | `get_analytics` (followers, engagement), `best_times` |
| Reference | `list_audio` (Instagram licensed audio), `list_queue_slots`, `platform_limits` |

## Installation

```bash
claude mcp add --transport http ravenpost https://api.ravenpo.st/mcp
```

OAuth runs automatically for clients that speak MCP authorization. For clients without a browser flow, generate a personal access token in Settings → MCP tokens (shown once, revocable) and pass it as a header or in the URL.

## Configuration

```json
{
  "mcpServers": {
    "ravenpost": {
      "type": "http",
      "url": "https://api.ravenpo.st/mcp"
    }
  }
}
```

You need a Ravenpost account with at least one connected social account; the free plan is enough to try it.

## Business Relevance

- **Growth operators** can run one approval-gated publishing loop across nine networks from any MCP client
- **Content teams** get per-platform previews and character warnings before anything is scheduled
- **Agencies** can scope credentials per workspace so client accounts never cross-post
- **Analytics-driven operators** get best-time recommendations measured from their own posting history

## Integration with CorpusIQ

Ravenpost complements the CorpusIQ analytics connectors at both ends of the funnel. Post-performance can be cross-checked against platform truth — CorpusIQ TikTok, YouTube and Instagram Business connectors read engagement from the platforms themselves, so Ravenpost's `get_analytics` can be validated rather than trusted alone. For the CorpusIQ content engine, Ravenpost's platform limits and queue tools give the social cadence scheduler a second execution surface: CorpusIQ drafts and approves, Ravenpost renders previews and publishes across networks the Postiz connector does not cover, like Telegram and Threads. The approval gate matches the CorpusIQ doctrine — the agent proposes, the human confirms, the audit trail records.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- Hosted only — no self-hosting; account required, vendor retains the platform connections
- Preview accuracy depends on the vendor keeping per-platform renderers current with network changes
- Free plan is a trial tier; multi-workspace separation sits on the paid Agency plan
- No engagement-reply tools — publishing and analytics only, no inbox or comment management

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
