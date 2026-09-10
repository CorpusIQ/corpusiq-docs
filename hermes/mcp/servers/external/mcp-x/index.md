---
title: mcp-x MCP - Official X API v2 Tools for Agents
description: Go MCP server exposing the full X (Twitter) API v2 as 42 tools for posts, search, users, lists and media upload over official OAuth 1.0a user context, with destructive hints and cost guards.
category: Social Media Management
stars: 1
added: 2026-09-10
source: "chatmcp/mcpso issue #4031"
relevance: ★★★
tags: [x, twitter, social-media, oauth1, posting, remote-mcp, go]
---

# mcp-x MCP

**The official X API v2, not a cookie-driven browser** - 42 Go-implemented tools covering posts, search, users, lists, bookmarks and media upload. Every call runs as the real account the keys belong to, and every destructive tool carries the MCP destructiveHint annotation while reads carry readOnlyHint. Built around one constraint: X has no free tier anymore, so reads are billed per resource and the tool descriptions actively push the model toward the smallest result set that answers the question.

```
Server type: Go binary + container (stdio and Streamable HTTP, identical tools)
Auth: OAuth 1.0a user context (API key, secret, access token, secret)
Registry: io.github.Role1776/mcp-x 0.1.1 (Official MCP Registry, active)
License: MIT
Tools: 42
Pricing: Pay-per-use X API billing (reads billed per resource returned)
Built by: varmcp.com
```

## Why This Matters for Operators

X is where business operators live publicly, and most X MCP servers drive a browser session with your cookies - fragile, slow, and invisible to X's rate limits until the account is flagged. **mcp-x uses the official API instead**, which makes the agent a first-class client: media upload goes through the documented endpoint, deletes are real and irreversible (and flagged as destructive), and rate ceilings live in env vars the model cannot reach. The billing discipline is baked into the tool design - `x_posts_count` sizes a topic without touching the post-read budget, lookups are batched, and pagination is manual because every page is billed.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `x_posts_search` | Search recent posts with full operator support (from:, #tag, -term, lang:, has:media, url:) |
| `x_posts_count` | Size a topic's post volume without spending the post-read budget |
| `x_posts_lookup` | Batch lookup by post ids (1..100 per call) |
| `x_posts_by_user` | Posts by username with exclude and date window controls |
| `x_posts_mentions` / `x_posts_home` / `x_posts_liked` / `x_posts_quotes` | Mention, home timeline, liked and quote views |
| `x_post_create` | Publish (text, reply, quote, poll, media), reply_settings control |
| `x_post_delete` | Irreversible delete, destructive-hinted |
| `x_post_like` / `x_post_repost` (+ unlike/unrepost variants) | Engagement actions |
| `x_media_upload` | Media upload from a validated MEDIA_ROOT directory |
| `x_users_me` / `x_users_lookup` | Own profile and batch user lookup |
| `x_user_follow` / `x_user_followers` / `x_user_following` | Follow graph management |
| `x_user_mute` / `x_users_blocked` / `x_users_muted` | Moderation actions |
| `x_list_*` family (14 tools) | Create, update, pin, follow, member management and list posts |
| `x_bookmarks_list` | Bookmark reading |

## Installation

```bash
# Binary or container
docker run -e X_API_KEY=... -e X_API_SECRET=... -e X_ACCESS_TOKEN=... -e X_ACCESS_SECRET=... ghcr.io/role1776/mcp-x:0.1.1
```

Release binaries ship for darwin/linux/windows on amd64 and arm64, plus .mcpb bundles with checksums. The server refuses to start without valid credentials - a GET /2/users/me runs before any tool registers, so bad keys fail the process instead of every later call.

## Configuration

```json
{
  "mcpServers": {
    "mcp-x": {
      "command": "mcp-x",
      "env": {
        "X_API_KEY": "your-api-key",
        "X_API_SECRET": "your-api-secret",
        "X_ACCESS_TOKEN": "your-access-token",
        "X_ACCESS_SECRET": "your-access-secret",
        "MEDIA_ROOT": "/path/to/media/dir"
      }
    }
  }
}
```

Two startup guards worth knowing: the server detects the read-only token trap (an access token keeps the permissions the app had when generated, so flipping the app to Read and Write later leaves writes failing forever) and says so explicitly. Media upload only reads from MEDIA_ROOT, validated at startup with no default.
