---
title: xurl (X/Twitter) — Full Setup Guide for Hermes Agents
description: Install, configure, and use the xurl skill from nousresearch/hermes-agent. Post, search, DM, and manage media on X/Twitter from Hermes agents.
---

# xurl (X/Twitter Integration) — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (171 installs)
**Category:** Social Media

Provides full X/Twitter API v2 access from Hermes agents — posting, searching, direct messages, media uploads, and account operations. Replaces browser-based Twitter automation with native API calls.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill xurl
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **X/Twitter API credentials** | Free tier from [developer.x.com](https://developer.x.com). $100/month Basic, $5,000/month Pro for elevated access. |
| **Hermes Agent** | Any version with skills support |

Set credentials in your Hermes environment:

```bash
export X_API_KEY="your-api-key"
export X_API_KEY_SECRET="your-api-key-secret"
export X_ACCESS_TOKEN="your-access-token"
export X_ACCESS_TOKEN_SECRET="your-access-token-secret"
```

Or in `~/.hermes/config.yaml`:

```yaml
env:
  X_API_KEY: "your-api-key"
  X_API_KEY_SECRET: "your-api-key-secret"
  X_ACCESS_TOKEN: "your-access-token"
  X_ACCESS_TOKEN_SECRET: "your-access-token-secret"
```

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Post tweets | "Post a tweet about X" | 280 char limit, supports media attachments |
| Search tweets | "Search X for 'hermes agent'" | v2 recent search (7-day window on free tier) |
| Send DMs | "DM @user about Y" | Recipient must follow you or have DMs open |
| Read timeline | "Show my X timeline" | Home timeline or user-specific |
| Upload media | "Post this image to X" | Images, GIFs, videos |
| Get user info | "Look up @username on X" | Profile, follower count, bio |

### CLI Command Reference

```bash
# Post a tweet
hermes xurl post "Hello from Hermes"

# Search recent tweets
hermes xurl search "hermes agent" --limit 10

# Get user timeline
hermes xurl timeline @username --count 20

# Send DM
hermes xurl dm @username "Message text"

# Upload and post media
hermes xurl media --file /path/to/image.png --text "Check this out"
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social mining** | Search for operator pain points: `hermes xurl search "my data pipeline"` |
| **Help-first engagement** | Reply to users asking about agent orchestration, data integration |
| **Brand monitoring** | Track @CorpusIQ mentions, competitor keywords |
| **Content distribution** | Post daily tips, product updates, skill spotlights |
| **Lead discovery** | Search for "need MCP" / "AI agent for business" / "CRM automation" |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `401 Unauthorized` | Regenerate tokens at [developer.x.com/portal](https://developer.x.com/portal). Ensure OAuth 1.0a User Context. |
| `403 Forbidden` | Free tier restricts to posting only. Upgrade to Basic ($100/mo) for read access. |
| `429 Rate Limit` | Free tier: 1,500 tweets/month posting, 50 requests/24h for v2 search. Add 15-minute delays between batches. |
| DM fails "not following" | Recipient must follow you OR have open DMs. Build engagement first. |

---

## Verification

```bash
# Verify skill installed
hermes skills list | grep xurl

# Quick functional test — post a test tweet
hermes xurl post "xurl setup verified — CorpusIQ agent reporting for duty"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 30 Update 2 Discovery](/hermes/skills/marketplace/new-june30-2026-update2/) →*
*Powered by CorpusIQ*
