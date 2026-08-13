---
title: Fetcher Skills — Social Platform API Cluster Setup Guide for Hermes Agents
description: Install the fetcher-sh/fetcher-skills cluster (971 installs, 7 skills) — twitter-api, x-api, instagram-api, tiktok-api plus scraper variants for agent-driven social platform data access.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fetcher-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Fetcher Skills — Setup Guide

**Source:** [fetcher-sh/fetcher-skills](https://www.skills.sh/fetcher-sh/fetcher-skills) (7 skills · 971 combined installs)
**Repo:** [github.com/fetcher-sh/fetcher-skills](https://github.com/fetcher-sh/fetcher-skills)
**Category:** Social API / Platform Integration
**First Seen:** August 13, 2026
**Quality Tier:** 🟡 Beta (`twitter-api` at 938 installs, trending on the hot leaderboard)

Fetcher.sh publishes API-access skills for the major social platforms. `twitter-api` carries almost the entire install base at 938 and was on the hot leaderboard during the August 13 sweep. The cluster covers API access patterns for X/Twitter, Instagram, and TikTok, with scraper variants as fallbacks. Useful as the procedural layer around API credentials an agent already holds.

---

## Installation

```bash
# Full cluster
npx skills add fetcher-sh/fetcher-skills

# Hermes: install individual skills by identifier
hermes skills install fetcher-sh/fetcher-skills/twitter-api
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `twitter-api` | 938 | X/Twitter API posting, reading, and engagement |
| `x-api` | 8 | Alternative X API patterns |
| `instagram-api` | 8 | Instagram API access patterns |
| `tiktok-api` | 8 | TikTok API access patterns |
| `x-scraper` | 3 | Scraper fallback for X data |
| `instagram-scraper` | 3 | Scraper fallback for Instagram data |
| `tiktok-scraper` | 3 | Scraper fallback for TikTok data |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Platform API credentials | Per-platform keys or sessions |
| Node.js + npx | For the skills.sh CLI install path |
| Platform terms compliance | Scraper variants must respect each platform's terms |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social monitoring** | API-first checks of mentions and replies |
| **Posting pipelines** | `twitter-api` as reference for X automation |
| **Competitive listening** | Structured reads of competitor activity |

---

## Limitations / Verification

- Small cluster — only `twitter-api` has meaningful install volume
- Scraper skills may conflict with platform anti-bot systems; prefer official APIs
- Verify install: `npx skills list | grep -E 'twitter|tiktok|instagram'`

---

## Related

- [Playwright Social Media Automation Setup](/hermes/skills/catalog/playwright-social-media-automation-setup/)
- [Content & Social category](/hermes/skills/catalog/)
- [Skills Catalog](/hermes/skills/catalog/)
