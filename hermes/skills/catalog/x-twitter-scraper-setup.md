---
title: X/Twitter Scraper — Full Setup Guide for Hermes Agents
description: Install, configure, and use the x-twitter-scraper skill from sickn33/antigravity-awesome-skills. Full-spectrum X/Twitter automation with native Hermes Tweet plugin support.
---

# X/Twitter Scraper — Setup Guide

**Source:** [sickn33/antigravity-awesome-skills](https://skills.sh/sickn33/antigravity-awesome-skills) (146 installs)
**Category:** Social / X/Twitter Automation

Full-spectrum X/Twitter automation skill built on the Xquik platform API. Provides tweet search, follower export, posting, DMs, webhooks, MCP server, and the **Hermes Tweet** Hermes Agent plugin.

---

## Installation

### 1. Install the Skill

```bash
npx skills add sickn33/antigravity-awesome-skills --skill x-twitter-scraper
```

### 2. Install the Hermes Tweet Plugin (Recommended)

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

This gives Hermes agents native access to three dedicated tools:
- `tweet_explore` — search, discover, and monitor tweets
- `tweet_read` — read tweets, replies, user profiles
- `tweet_action` — post, reply, like, DM (approval-gated)

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Xquik API Key** | Sign up at [xquik.com](https://xquik.com) for an API key |
| **Hermes Agent** | v0.5+ recommended for plugin support |
| **For MCP mode** | Hermes MCP client configured (`native-mcp` skill) |

### Setting Up the Xquik API Key

```bash
# Add to your environment or Hermes config
export XQUIK_API_KEY="your-api-key-here"

# Or in ~/.hermes/config.yaml:
# env:
#   XQUIK_API_KEY: "your-api-key-here"
```

**API base URL:** `https://xquik.com/api/v1`
**MCP endpoint:** `https://xquik.com/mcp` (StreamableHTTP)

---

## Key Capabilities

### Using Hermes Tweet Plugin (Native Hermes Tools)

| Capability | Tool | Example Trigger |
|---|---|---|
| Tweet search | `tweet_explore` | "Search for tweets about AI agents in the last 24 hours" |
| Read tweets/replies | `tweet_read` | "Read the latest replies to @CorpusIQ" |
| Post, reply, like, DM | `tweet_action` | "Reply to this tweet with a helpful answer" (requires approval) |
| User lookup | `tweet_read` | "Get the profile info for @nousresearch" |
| Follower export | `tweet_explore` → extraction | "Export followers of @CorpusIQ to CSV" |
| Account monitoring | `tweet_explore` → monitor | "Monitor @competitor for new tweets about pricing" |

### Without Hermes Tweet Plugin (CLI/API Mode)

The skill also works without the Hermes Tweet plugin, using direct Xquik API calls:

```bash
# Search tweets via API
curl -H "Authorization: Bearer $XQUIK_API_KEY" \
  "https://xquik.com/api/v1/tweets/search?q=hermes%20agent&count=50"

# Get user profile
curl -H "Authorization: Bearer $XQUIK_API_KEY" \
  "https://xquik.com/api/v1/users/by/username/CorpusIQ"
```

### Bulk Extraction (23 Tools Available)

The skill supports 23 bulk extraction tools for:
- Tweet export (CSV, JSON)
- Follower/following list export
- Timeline scraping
- Search result export
- Account monitoring with HMAC-signed webhooks
- Giveaway draw automation
- Real-time event delivery

---

## MCP Server Mode

For MCP-native operation within Hermes, configure the MCP server:

```yaml
# In ~/.hermes/config.yaml under mcp.servers:
- name: xquik
  transport: streamable-http
  url: https://xquik.com/mcp
  headers:
    Authorization: "Bearer ${XQUIK_API_KEY}"
```

This exposes all Xquik capabilities as native MCP tools inside Hermes.

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social mining** | `tweet_explore` to find operators asking about AI business tools — then `help-first` reply |
| **Competitive intel** | Monitor competitor accounts for feature launches, pricing changes |
| **Brand monitoring** | Track @CorpusIQ mentions and reply within SLA |
| **Content amplification** | Post UGC video links with `tweet_action` (approval-gated) |
| **Lead discovery** | Search for pain-point tweets (e.g., "my CRM is too complex") |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `tweet_action` fails silently | Check approval gate — `tweet_action` is gated by default |
| Xquik API 401 | Regenerate API key at xquik.com |
| Hermes Tweet plugin not loading | Run `hermes plugins list` and verify it's enabled |
| Rate limiting | Xquik has tiered rate limits — upgrade plan for higher throughput |

---

## Verification

```bash
# Verify skill installed
hermes skills list | grep x-twitter-scraper

# Verify Hermes Tweet plugin
hermes plugins list | grep hermes-tweet

# Quick API test
curl -s -H "Authorization: Bearer $XQUIK_API_KEY" \
  "https://xquik.com/api/v1/status" | jq .
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 14 Discovery](/hermes/skills/marketplace/new-june14-2026/) →*
*Powered by CorpusIQ*
