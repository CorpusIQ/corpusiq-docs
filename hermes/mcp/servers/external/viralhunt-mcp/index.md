---
title: ViralHunt MCP - Trending Discovery and Social Publishing
description: 20-tool MCP server for viral content discovery across 12 networks, best-time-to-post data, hashtags, trending sounds, communities, and scheduling/publishing to connected social accounts. Free token, MIT.
category: Social Media Management
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [social-media, trending, scheduling, tiktok, instagram, marketing, content-research, remote-mcp]
---

# ViralHunt MCP

**Trending discovery + cross-network publishing in one MCP server** - 20 tools that drive the full agent loop: discover what is going viral on TikTok, Instagram, X, Facebook, Pinterest, Reddit, Bluesky, Mastodon, Douyin, Tumblr, Hacker News and news RSS, time the post, publish it, then verify and correct. A BuzzSumo alternative with a built-in scheduler that an AI agent can drive end to end.

```
Server type: npm package (npx viralhunt-mcp, Node >= 18) + hosted ViralHunt API
Auth: Free API token (vhk_... from viralhunt.io -> Account -> API Access, 7-day trial, no card)
Registry: io.github.rodvan/viralhunt-mcp (Official MCP Registry)
License: MIT
Tools: 20
Pricing: Free token for trial; paid plans via ViralHunt.io
Built by: ViralHunt.io
```

## Why This Matters for Operators

Content teams spend hours manually hunting trends, guessing post timing, and copy-pasting posts across networks. **ViralHunt turns that into one agent-drivable loop** - every number (best time, hashtag strength, trend velocity) comes with its sample size and time window, so an agent can state how much to trust it instead of hallucinating confidence. The `growth_24h` field on trending posts shows how much a post moved between readings, which is the difference between catching a trend early and chasing it late.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `viralhunt_trending` | What is going viral per network, ranked by viral score with `growth_24h` velocity |
| `viralhunt_best_time` | Best weekday + hour per network from measured viral posts (365-day sample, hit rate, sample size) |
| `viralhunt_top_hashtags` | Top tags per network or across all, by engagement, posts or per-post |
| `viralhunt_trending_sounds` | Trending audio on TikTok, Instagram Reels and Douyin with the posts that used it |
| `viralhunt_best_communities` | Best subreddits (peak per 1,000 members, timing, top posts) and Bluesky feeds for a topic |
| `viralhunt_targets` | Your brands/projects and the connected accounts you can post to |
| `viralhunt_schedule` | Publish now or schedule a post (text + media) across connected accounts |
| `viralhunt_get_post` | Check a post's status and per-network permalinks |
| `viralhunt_update_post` | Edit a still-scheduled post (body / media / networks / time) |
| `viralhunt_cancel_post` | Cancel a scheduled post |
| `viralhunt_create_card` / `viralhunt_move_card` / `viralhunt_my_cards` / `viralhunt_card_comments` / `viralhunt_board_context` | Team curation board - cards, comments and shared context |
| `viralhunt_assign_template` / `viralhunt_list_templates` / `viralhunt_get_template` | Brand templates for recurring post formats |

## Installation

```bash
VIRALHUNT_API_KEY=vhk_... npx viralhunt-mcp
```

Node >= 18. `VIRALHUNT_BASE_URL` is optional and defaults to the production API.

## Configuration

```json
{
  "mcpServers": {
    "viralhunt": {
      "command": "npx",
      "args": ["viralhunt-mcp"],
      "env": { "VIRALHUNT_API_KEY": "vhk_..." }
    }
  }
}
```

The free token covers a 7-day trial with no card required - enough to run a full discover -> schedule -> publish cycle and evaluate the trend data before committing to a plan.
