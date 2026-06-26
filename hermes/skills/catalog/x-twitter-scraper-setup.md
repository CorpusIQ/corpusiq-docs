---
title: X/Twitter Scraper — Full Setup Guide for Hermes Agents
description: Install and configure the x-twitter-scraper skill from sickn33/antigravity-awesome-skills. Comprehensive X/Twitter automation — tweet search, follower export, posting, DMs, webhooks, MCP, Hermes Tweet plugin, and TweetClaw. 148 installs.
---

# X/Twitter Scraper — Setup Guide

**Source:** [sickn33/antigravity-awesome-skills](https://skills.sh/sickn33/antigravity-awesome-skills) (148 installs) | [GitHub](https://github.com/sickn33/antigravity-awesome-skills) (41,720⭐)
**Category:** social, data

Comprehensive X/Twitter automation skill for Hermes Agent. Covers the full Twitter API surface: tweet search, advanced search, profile tweets, user lookup, follower export, media download, posting, replies, DMs, giveaway draws, account monitoring, webhooks, 23 bulk extraction tools, MCP integration, the Hermes Tweet plugin, and the TweetClaw OpenClaw plugin.

---

## Installation

```bash
npx skills add sickn33/antigravity-awesome-skills --skill x-twitter-scraper
```

This is a documentation-only skill — it doesn't bundle executable code. The external tools (Xquik, Hermes Tweet plugin, TweetClaw) must be installed separately.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **X/Twitter Account** | Required for authenticated actions (posting, DMs, monitoring) |
| **Xquik API Key** | For Xquik-based search and extraction: [xquik.com](https://xquik.com) |
| **Hermes Tweet Plugin** | For `tweet_explore`, `tweet_read`, `tweet_action` tools |
| **TweetClaw Plugin** | OpenClaw-based alternative to direct REST/MCP setup |
| **Hermes Agent** | Any recent version with plugin support |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Tweet search | "search tweets for [keyword]" | Keyword, hashtag, or user-based search |
| Advanced search | "advanced search on X for [query]" | Full Twitter search syntax |
| User lookup | "look up @[username] on X" | Bio, follower counts, profile data |
| Follower export | "export followers of @[username]" | Bulk extraction to CSV/JSON |
| Tweet metrics | "get engagement for [tweet URL]" | Likes, retweets, views |
| Post tweet | "post this to X: [content]" | Requires explicit approval |
| Send DM | "DM @[username] on X: [message]" | Requires explicit approval |
| Account monitoring | "monitor @[username] for new tweets" | Real-time webhook delivery |
| Giveaway draw | "run giveaway from [tweet URL] replies" | Random selection from replies |
| Bulk extraction | "bulk extract [data type] from X" | 23 extraction tools available |

### Hermes Tweet Plugin Tools

| Tool | Function |
|---|---|
| `tweet_explore` | Search and browse tweets |
| `tweet_read` | Read specific tweet details |
| `tweet_action` | Post, reply, like, repost (approval-gated) |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social mining** | Search X for operator pain points, competitor mentions, market signals |
| **Competitive intelligence** | Monitor competitor accounts for product launches, feature announcements |
| **Brand monitoring** | Track @CorpusIQ mentions and respond via DMs |
| **Lead discovery** | Export followers of target accounts, identify potential customers |
| **Content amplification** | Schedule and post UGC content, track engagement metrics |
| **Community growth** | Run giveaway draws from announcement tweets |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "Xquik API key required" | Register at xquik.com and set `XQUIK_API_KEY` env var |
| Posting blocked | tweet_action requires explicit user approval per Hermes security model |
| Rate limiting | X/Twitter API has rate limits; use bulk extraction for large datasets |
| Webhook not firing | Verify webhook URL is publicly accessible (use ngrok for local dev) |
| Hermes Tweet plugin not found | Install separately: check plugin directory at `~/.hermes/profiles/<name>/plugins/` |

## Verification

```bash
# Verify skill installed
hermes skills list | grep x-twitter-scraper

# Test tweet search (read-only, no auth needed for basic search)
# Ask Hermes: "search X for 'hermes agent' and show me the top 5 results"

# Verify Hermes Tweet plugin (if installed)
hermes tweet_explore --query "test" --count 1
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june25-2026-update/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
