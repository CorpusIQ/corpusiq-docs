---
title: Apidojo Social Media Skills - 3-Skill Scraper Suite Setup
description: "apidojo-io/social-media-skills - 3 Agent Skills for scraping X (Twitter), Instagram, and TikTok data at scale via Apify actors. 8.0K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apidojo-social-media-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-10"
tags: ["hermes skill", "agent skill", "skill setup", "social media", "scraping", "data extraction", "apify", "twitter", "instagram", "tiktok"]
---

# Apidojo Social Media Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/apidojo-io/social-media-skills) (3 skills, ~8,000 combined installs)
**GitHub:** [apidojo-io/social-media-skills](https://github.com/apidojo-io/social-media-skills) (Apache-2.0 per README, pushed Sep 2, 2026)
**Category:** Social Media / Data Extraction
**First Seen:** Sep 10, 2026 sweep (cluster surfaced via failed-query compensation - the recurring `social media` / `content` collector-query failures)
**Quality Tier:** 🟡 Unverified (no skills.sh security audits published for this publisher)

A 3-skill suite that turns an agent into a social data extractor backed by Apify actors - no proxies, no login handling, just token-authenticated API calls that return structured JSON. Each skill is a single SKILL.md in standard Agent Skills format (`name` / `description` / `version` frontmatter) with sync and async curl patterns for the corresponding Apify actor. Platform-agnostic: works with any agent that can run `npx skills add` or read a SKILL.md.

---

## Installation

Install all three skills:

```bash
npx skills add apidojo-io/social-media-skills
```

Install a single skill:

```bash
npx skills add apidojo-io/social-media-skills --skill x-scraper
```

List available skills first:

```bash
npx skills add apidojo-io/social-media-skills --list
```

For Hermes Agent, copy the skill folders into the agent's skills directory from a clone:

```bash
git clone https://github.com/apidojo-io/social-media-skills.git
cp -r social-media-skills/skills/* ~/.hermes/skills/
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Apify paid plan** | All three actors reject API calls on the free plan - [sign up](https://apify.com/) and subscribe first |
| **APIFY_TOKEN** | From [console.apify.com/account/integrations](https://console.apify.com/account/integrations); `export APIFY_TOKEN="apify_api_..."` |
| **curl / wget + jq** | For the sync and async run patterns in the SKILL.md files |

## Skill Roster

| Skill | Installs | Platform | What It Extracts |
|---|---|---|---|
| `x-scraper` | 2,716 | X (Twitter) | Tweets by search query, profile, hashtag, keyword, conversation thread, date range, or list - uses Twitter advanced search syntax via the `searchTerms` input |
| `instagram-scraper` | 2,679 | Instagram | Posts, reels, hashtags, locations, comments, profiles, followers |
| `tiktok-scraper` | 2,631 | TikTok | Videos, profiles, hashtags, music, comments, location-based posts |

## Quick Start

1. Install the skills and export `APIFY_TOKEN`
2. Ask for data - "fetch the last 50 tweets from @NASA" - the agent invokes `x-scraper` with the sync pattern (short runs return dataset items directly; runs beyond 300s switch to the async start → poll → fetch-dataset pattern)
3. Every request passes a `"skill": true` field that returns the raw extraction in structured form instead of a summary

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social mining** | `x-scraper` pulls operator conversations by search query, profile, and hashtag - help-first engagement targets without manual browsing |
| **Competitor monitoring** | Scheduled hashtag / keyword pulls across X, Instagram, and TikTok feed competitive intelligence into research sweeps |
| **Creator & UGC research** | `instagram-scraper` + `tiktok-scraper` gather profiles, engagement, and content for creator-partnership vetting |
| **Lead intel** | Profile, comment, and follower data support outbound research before first contact |

## Limitations / Verification

- **Paid prerequisite:** every skill requires an Apify paid plan - API calls on the free tier are rejected. Budget before adopting.
- **No published security audits:** as of Sep 10, 2026 the skills.sh page renders no Trust Hub / Socket / Snyk verdicts for this publisher. The three SKILL.md files are short, single-purpose API-pattern documents - manual review takes minutes.
- **Young repo:** created Mar 2026, 1 GitHub star - install traction comes from skills.sh, not GitHub. Repo pushed Sep 2, 2026 (active).
- **Affiliate links:** README Apify links carry a referral tag (`fpr=yhdrb`); the skills themselves are Apache-2.0 (GitHub API license field is empty; README states Apache-2.0).
- **Data rights:** scraped platform data usage is the operator's responsibility - respect platform terms for any public redistribution.

```bash
# Verify skill installed
ls ~/.hermes/skills/x-scraper/SKILL.md
```

## Security

No skills.sh security audits published (verified Sep 10, 2026 - the skill page renders no audit verdicts). Treat as unverified until reviewed:

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Blacktwist Social Media Skills - 14-Skill Content Suite Setup](/docs/hermes/skills/catalog/blacktwist-social-media-skills-setup)
- [Charlie Hills Social Media Skills - 17-Skill Content System Setup](/docs/hermes/skills/catalog/charlie-hills-social-media-skills-setup)
- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/docs/hermes/skills/catalog/apify-growth-skills-setup)
- [Apify Ultimate Scraper - Universal Web Scraping for 15+ Platforms Setup](/docs/hermes/skills/catalog/apify-ultimate-scraper-setup)
- [Social Media - Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
