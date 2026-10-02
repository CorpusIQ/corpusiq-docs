---
title: "Apidojo Agent Skills - 100-Skill Social & Market Data"
description: "apidojo-io/apidojo-skills - 100 Agent Skills for social scraping and market research via Apify actors: 24 data primitives + 76 intent workflows for creator discovery, brand monitoring, and lead gen. 21K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apidojo-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "scraping", "social media", "data extraction", "apify", "lead generation", "market research"]
---

# Apidojo Agent Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/apidojo-io/apidojo-skills) (100 skills, ~21.0K combined installs)
**GitHub:** [apidojo-io/apidojo-skills](https://github.com/apidojo-io/apidojo-skills) (Apache-2.0, created May 13, 2026; 0 stars - traction flows through skills.sh)
**Category:** Social Media / Data Extraction
**First Seen:** Sep 11, 2026 sweep (companion repo to the guided apidojo-io/social-media-skills)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub Pass / Socket Pass / Snyk Warn on the flagship skill)

The larger companion to the already-guided [apidojo-io/social-media-skills](/hermes/skills/catalog/apidojo-social-media-skills-setup): 100 agent skills built on apidojo's Apify actors, organized in two layers - 24 primitives (raw platform data access: tweets by keyword, TikTok comments, YouTube trending) and 76 intent skills (named outcomes: "find Instagram creators by location", "build a full social audit for a brand", "find SaaS company leads on Twitter"). Same publisher, same architecture, ten times the workflow surface. Clears the 20K bar on combined installs.

---

## Installation

```bash
npx skills add apidojo-io/apidojo-skills
```

For Hermes Agent, copy selected skill folders from a clone:

```bash
git clone https://github.com/apidojo-io/apidojo-skills.git
cp -r apidojo-skills/skills/* ~/.hermes/skills/
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Apify account** | apidojo actors run on [Apify](https://apify.com/apidojo) - paid plan required for most actors (same as the sibling repo) |
| **APIFY_TOKEN** | `export APIFY_TOKEN="apify_api_..."` from the Apify console |

## Skill Roster (top 15 of 100)

| Skill | Installs | What It Does |
|---|---|---|
| `finding-instagram-creators-by-location` | 257 | Instagram creator discovery filtered by posting location |
| `building-full-social-audit-for-brand` | 249 | Multi-platform brand presence audit |
| `discovering-brand-ambassadors-across-platforms` | 248 | Ambassador candidate discovery |
| `scraping-tiktok-user-data` | 242 | TikTok profile and user data extraction |
| `scraping-instagram-location-content` | 241 | Instagram content by location |
| `finding-tiktok-creators-using-trending-sounds` | 239 | Trend-sound creator discovery |
| `monitoring-twitter-for-competitor-job-posts` | 236 | Competitor hiring intelligence |
| `analyzing-twitter-sentiment-for-topic` | 235 | Topic sentiment analysis |
| `finding-tiktok-shop-trending-products` | 232 | TikTok Shop product trend research |
| `monitoring-instagram-brand-mentions` | 230 | Brand mention monitoring |
| `finding-youtube-sponsorship-candidates` | 229 | Sponsorship lead discovery |
| `finding-saas-company-leads-twitter` | 224 | SaaS lead mining on X |
| `extracting-google-paa-questions-for-seo` | 223 | People-Also-Ask extraction for SEO |
| `scraping-youtube-videos-by-keyword` | 223 | YouTube video research |
| `finding-youtube-micro-influencers` | 228 | Micro-influencer discovery |

Remaining 85 cover competitor content analysis, brand sentiment tracking, healthcare/Google-search prospecting, internet-slang research, and platform-specific scraping primitives.

## Quick Start

1. Install the suite and export `APIFY_TOKEN`
2. Intent skills map one natural-language ask to one workflow - "find SaaS leads in Austin on Twitter" runs the full find → score → CSV pipeline
3. Primitives (24) are for raw data pulls when you want the extraction without the interpretation

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Creator & affiliate discovery** | Instagram/TikTok/YouTube creator-finding intent skills feed the affiliate and creator-partnership pipeline directly |
| **Competitor intelligence** | Brand audits, sentiment analysis, and competitor-content-strategy skills automate competitive research sweeps |
| **Lead generation** | `finding-saas-company-leads-twitter` and healthcare-practice prospecting produce outbound lists |
| **Social mining** | The 24 primitives complement the sibling x/instagram/tiktok-scraper trio with intent-shaped workflows |

## Limitations / Verification

- **Paid prerequisite:** apidojo actors require an Apify paid plan (free-tier calls are rejected) - budget before adopting.
- **Snyk Warn:** flagship skill renders Trust Hub Pass, Socket Pass, Snyk Warn - review-first per the sibling guide's precedent.
- **Young, zero-star repo:** created May 2026 with 0 GitHub stars; all traction is skills.sh installs. The sibling repo's README pattern (verified SKILL.md format, short API-pattern documents) applies here.
- **Data rights:** scraped platform data usage is the operator's responsibility - respect platform terms for public redistribution.

```bash
# Verify skill installed
ls ~/.hermes/skills/finding-instagram-creators-by-location/SKILL.md
```

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Warn |

## Related

- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/hermes/skills/catalog/apify-growth-skills-setup)
- [Apify Ultimate Scraper - Universal Web Scraping for 15+ Platforms Setup](/hermes/skills/catalog/apify-ultimate-scraper-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
