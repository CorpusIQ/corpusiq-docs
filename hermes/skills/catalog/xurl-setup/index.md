---
title: xurl (X/Twitter) - Full Setup Guide for Hermes Agents
description: Install, configure, and use the xurl skill from nousresearch/hermes-agent. Post, search, DM, and manage media on X/Twitter from Hermes agents.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/xurl-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# xurl (X/Twitter Integration) - Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (171 installs)
**Category:** Social Media

Provides full X/Twitter API v2 access from Hermes agents - posting, searching, direct messages, media uploads, and account operations. Replaces browser-based Twitter automation with native API calls.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill xurl
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **X/Twitter API credentials** | An app in the [X Developer Console](https://developer.x.com). The X API v2 runs on pay-per-usage credits: reads are billed per resource returned (for example $0.005 per post) and writes per request, with no subscription, plus starter credits for a first purchase. |
| **`xurl` CLI** | The skill drives the official X CLI, not a Hermes subcommand. Install with `curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh \| bash`, or `brew install --cask xdevplatform/tap/xurl`, `npm install -g @xdevplatform/xurl`, `go install github.com/xdevplatform/xurl@latest`. |
| **Hermes Agent** | Any version with skills support |

Credentials do not live in Hermes environment variables. `xurl` stores them in `~/.xurl` as YAML, per app profile, and OAuth 2.0 tokens auto-refresh. The one-time setup is run by the user, outside the agent, because it pastes secrets:

```bash
# 1. Create an app at developer.x.com with redirect URI http://localhost:8080/callback
# 2. Register it locally
xurl auth apps add my-app --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET

# 3. Authenticate (opens the browser for OAuth 2.0 PKCE) and bind it as default
xurl auth oauth2 --app my-app
xurl auth default my-app

# 4. Verify
xurl auth status
xurl whoami
```

If OAuth returns `UsernameNotFound` or 403 on the `/2/users/me` lookup, pass the handle explicitly: `xurl auth oauth2 --app my-app YOUR_USERNAME`. Never print or upload `~/.xurl`, and avoid `--verbose` in an agent session - it can expose auth headers.

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Post tweets | "Post a tweet about X" | 280 char limit, supports media attachments |
| Search tweets | "Search X for 'hermes agent'" | v2 recent search, `xurl search "query" -n N`, billed per post returned |
| Send DMs | "DM @user about Y" | Recipient must follow you or have DMs open |
| Read timeline | "Show my X timeline" | Home timeline or user-specific |
| Upload media | "Post this image to X" | Images, GIFs, videos |
| Get user info | "Look up @username on X" | Profile, follower count, bio |

### CLI Command Reference

The skill calls the `xurl` binary directly. `hermes xurl` is not a Hermes subcommand.

```bash
# Post a post
xurl post "Hello from Hermes"

# Search posts (returns raw post JSON with IDs you can engage)
xurl search "hermes agent" -n 10

# Home timeline / mentions
xurl timeline -n 20
xurl mentions -n 10

# Send a DM
xurl dm @username "Message text"

# Upload media, then attach it to a post
xurl media upload path/to/image.png
xurl post "Check this out" --media-id MEDIA_ID

# Reply, quote, delete
xurl reply POST_ID "Nice post!"
xurl quote POST_ID "My take"
xurl delete POST_ID
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social mining** | Search for business pain points: `xurl search "my data pipeline" -n 10` |
| **Help-first engagement** | Reply to users asking about agent orchestration, data integration |
| **Brand monitoring** | Track @CorpusIQ mentions, competitor keywords |
| **Content distribution** | Post daily tips, product updates, skill spotlights |
| **Lead discovery** | Search for "need MCP" / "AI agent for business" / "CRM automation" |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `401 Unauthorized` | Re-run `xurl auth status`. If the app is missing, register and authenticate again with `xurl auth apps add` then `xurl auth oauth2 --app my-app`; check you bound the default app with `xurl auth default my-app`. |
| `403 Forbidden` | Usually an app permission or account-tier limit rather than a fixed free tier: check the app's access level in the [Developer Console](https://developer.x.com), then verify credits remain. |
| `429 Rate Limit` | Per-endpoint rate limits apply. Check the `x-rate-limit-*` response headers, back off, and space batches of read calls. |
| DM fails "not following" | Recipient must follow you OR have open DMs. Build engagement first. |

---

## Verification

```bash
# Verify skill installed
hermes skills list | grep xurl

# Verify the CLI and auth
xurl --help
xurl auth status

# Quick functional test - read who the token belongs to
xurl whoami
```

---

*← [Skills Catalog](/hermes/skills/catalog) | [June 30 Update 2 Discovery](/hermes/skills/marketplace/new-june30-2026-update2) →*
*Powered by CorpusIQ*
