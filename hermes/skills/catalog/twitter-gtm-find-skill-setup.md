---
title: Twitter GTM Find Skill Setup Guide
description: End-to-end pipeline for scraping X/Twitter for GTM and DevRel tech startup jobs — via Apify, TweetClaw (OpenClaw), or Hermes Tweet (Hermes Agent). From varnan-tech/opendirectory (564⭐).
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/twitter-gtm-find-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Twitter GTM Find Skill — Setup Guide

**Source:** [varnan-tech/opendirectory](https://github.com/Varnan-Tech/opendirectory) (564 ⭐)
**Skill:** `twitter-gtm-find-skill` — 13 installs (skills.sh)
**Category:** Social Media & Growth

## Installation

```bash
npx skills add varnan-tech/opendirectory --skill twitter-gtm-find-skill
```

Or install the full opendirectory pack (50+ marketing/growth skills):

```bash
npx skills add varnan-tech/opendirectory
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.8+ (for Hermes Tweet integration) |
| Apify account | Required for X/Twitter scraping (Apify actor deployment) |
| Apify API token | Set as `APIFY_TOKEN` env var or in Hermes config |
| X/Twitter auth | For Hermes Tweet mode: xurl or Twitter API credentials |

## Capabilities

| Capability | Trigger | Description |
|-----------|---------|-------------|
| Twitter job scraping | `find GTM jobs on Twitter` | Scrapes X/Twitter for GTM and DevRel job postings at tech startups |
| Apify pipeline | `scrape Twitter for {role} jobs` | Deploys Apify actor to scrape X/Twitter with configurable search terms |
| Hermes Tweet mode | `use Hermes Tweet to find jobs` | Alternative path using Hermes Agent's native Twitter integration |
| OpenClaw fallback | `use TweetClaw` | Third option for OpenClaw-based Twitter scraping |

## CLI / Command Reference

```bash
# Install the skill
npx skills add varnan-tech/opendirectory --skill twitter-gtm-find-skill

# Run a GTM job search
hermes run twitter-gtm-find-skill --query "GTM lead startup" --source apify

# With Hermes Tweet
hermes run twitter-gtm-find-skill --query "DevRel engineer" --source hermes-tweet
```

## CorpusIQ Use Cases

1. **Competitor GTM hiring intelligence** — Monitor what GTM roles competitors are hiring for to identify market moves
2. **Lead generation** — Find tech startups actively hiring GTM/DevRel roles (they're growing → need tooling)
3. **Market research** — Aggregate hiring patterns across the AI/SaaS ecosystem to spot trends
4. **Content sourcing** — Find real operator discussions about GTM challenges for help-first content
5. **Partnership discovery** — Identify startups with complementary products hiring overlapping roles

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Apify actor fails | Verify `APIFY_TOKEN` is set and Apify account is active |
| No results | Broaden search terms; try "GTM", "DevRel", "growth" separately |
| Hermes Tweet not working | Ensure xurl or Twitter API credentials are configured in Hermes |
| Rate limited | Space out queries; Apify handles rate limiting automatically |

## Related Skills

- [x-twitter-automation](/hermes/skills/catalog/x-twitter-automation-setup/) — Design safe X/Twitter automation workflows
- [reddit-icp-monitor](/hermes/skills/marketplace/) — Monitor Reddit for ICP conversations (also from opendirectory)
- [hackernews-intel](/hermes/skills/marketplace/) — HN intelligence gathering (also from opendirectory)

## Verification

```bash
# Verify the skill is installed
hermes skills list | grep twitter-gtm-find-skill

# Test with a simple query
hermes run twitter-gtm-find-skill --query "test" --dry-run
```

---

*Catalog guide created July 30, 2026. Skill source: varnan-tech/opendirectory.*
