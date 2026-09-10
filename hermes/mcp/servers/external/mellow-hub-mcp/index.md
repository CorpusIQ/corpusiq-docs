---
title: Mellow Hub MCP - Multi-Network Social Publishing with Guardrails
description: Hosted MCP server that publishes one post to Instagram, TikTok, YouTube, X, LinkedIn, Threads, Bluesky, Pinterest and Facebook with per-network validation, previews, idempotency keys and scoped autopilot or review keys.
category: Social Media Management
stars: n/a (new listing)
added: 2026-09-10
source: mcpservers.org
relevance: ★★★
tags: [social-media, publishing, multi-platform, scheduling, instagram, tiktok, remote-mcp]
---

# Mellow Hub MCP

**One post to nine networks, with every network's rules checked before anything goes out** - a hosted publishing hub exposed as 12 MCP tools. Posts are validated per channel before publishing, rendered as previews, protected by idempotency keys against double-posting, and gated by per-key grants that decide whether an agent can autopilot-publish or only prepare posts for a human to approve.

```
Server type: Remote (hosted, Streamable HTTP)
Auth: Mellow Hub key (autopilot or review mode) - endpoint live-verified (key challenge) Sep 10, 2026
Endpoint: https://www.mellow.world/mcp
Networks: Instagram, TikTok, YouTube, X, LinkedIn, Threads, Bluesky, Pinterest, Facebook
Tools: 12 documented
Built by: mellow.world
```

## Why This Matters for Operators

Cross-posting usually means either a fragile browser-automation stack or a pile of separate platform APIs with different limits. **Mellow Hub compresses that into one API call with guardrails operators actually need**: `validate_post` returns every problem per channel before anything publishes, `preview_post` renders what the post will look like on each network, and a timeout-safe idempotency key means a retry returns the original post instead of publishing a second one. The key design is the delegation model - a review-mode key only prepares posts for a person to approve, while an autopilot key publishes within its scoped channels and daily post quota. Per-channel outcomes come back individually (a YouTube rejection on a five-network post is a partial with the failure named, not a silent miss).

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `whoami` | What this credential may do: mode, scopes, channels, posts remaining today |
| `list_platforms` | Every network's rules: caption limits, media kinds, required fields, placements |
| `list_channels` | Connected accounts and their channel ids |
| `connect_channel` | Returns a link a person must open to connect a network (human-in-the-loop) |
| `register_media` | Validate a public media URL, or request an upload URL for bytes and video |
| `validate_post` | Check a post against every named channel, publishes nothing |
| `preview_post` | Render the post as it will look on each network |
| `create_post` | Publish now or schedule (scheduledAt), idempotency key required |
| `get_post` | Per-channel outcome with public links, partial-failure detail |
| `list_posts` | Recent posts with status filters |
| `cancel_post` | Withdraw a scheduled but unpublished post |

## Installation

```bash
claude mcp add mellow https://www.mellow.world/mcp
```

Create the key at mellow.world/hub/agents. The key is a delegation: pick autopilot (publishes alone, within channel and daily-post limits) or review (prepares posts and stops for human approval).

## Configuration

```json
{
  "mcpServers": {
    "mellow": {
      "type": "http",
      "url": "https://www.mellow.world/mcp",
      "headers": { "Authorization": "Bearer YOUR_MELLOW_KEY" }
    }
  }
}
```

One post payload carries one caption, one media list, and a channels array; per-network differences go in options (per network) or perChannel (per account). Everything done with the key is recorded in a journal the owner reads, and revocation is immediate.
