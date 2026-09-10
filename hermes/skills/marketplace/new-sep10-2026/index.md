---
title: "New Skills - September 10, 2026 (Morning)"
description: "skills.sh morning sweep: apidojo-io/social-media-skills (8.0K installs, 3 scraper skills for X, Instagram, and TikTok via Apify) - 1 new publisher cluster, 3 skills, 1 setup guide."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep10-2026/"
robots: "index,follow"
last_updated: "2026-09-10"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills", "social media", "scraping"]
sweep_id: "2026-09-10-morning"
new_publishers: 1
new_skills: 3
guides_drafted: 1
---

# New Skills - September 10, 2026 (Morning)

Forty-three-query skills.sh API sweep (3,775 unique skills; 2 queries failed — `social media` and `content` — and were compensated with targeted re-fetches that surfaced this batch), cluster-level cross-reference against the full hermes/ tree, hot-leaderboard coverage check (clean, 185 ranked / 32 sources, all catalog-covered), and the tiered cross-reference sweep (606 unique / 65 NEW / 99 PARTIAL, PARTIAL ≥100 empty, zero query errors). One new publisher cluster cleared the drafting bar.

## New Skills

| Skill | Publisher | Installs | Category | What It Does |
|---|---|---|---|---|
| 3 skills (`x-scraper`, `instagram-scraper`, `tiktok-scraper`) | apidojo-io/social-media-skills | 8,026 combined | Social Media / Data Extraction | Agent skills for scraping X (Twitter), Instagram, and TikTok data at scale via Apify actors — tweets by query/profile/hashtag/thread/date range, Instagram posts/comments/followers, TikTok videos/profiles/music. Standard Agent Skills format, `npx skills add` install |

## Setup Guides

- [Apidojo Social Media Skills - Setup Guide](/hermes/skills/catalog/apidojo-social-media-skills-setup/)

## Evaluated and Skipped

| Cluster | Installs | Reason |
|---|---|---|
| mathews-tom/armory (`prompt-lab`) | 77 | Claude Code / Claude.ai package collection — adapters generated for Cursor, OpenAI Codex, and Gemini CLI; zero Hermes targeting; no HERMES.md. Claude-family rejection class |
| vm0-ai/vm0-skills (`arga-labs`) | 9 | Agent Skills format, but install docs target Claude Code Marketplace / GitHub Copilot; no Hermes mention; far below the 40-install floor. Below-bar park (watch) |

All 63 other NEW flags from the tiered cross-reference mapped to the standing-rejection roster recorded in the corpusiq-docs-management skill run-log; no other bar-clearers, no overturns.

## Security Notes

The one drafted cluster is 🟡 tier: the publisher has no Trust Hub / Socket / Snyk audit verdicts published on skills.sh — stated honestly in the guide with a review-first recommendation. The SKILL.md files are short, single-purpose API-pattern documents (Apify actor sync/async curl patterns) and manually reviewable in minutes.

## Source

skills.sh API sweep (43 queries, 3,775 unique skills + compensated re-fetch of the 2 failed queries — the same `social media` / `content` pair that failed on Sep 9 and hid the Salesforce / Claude SEO mega-clusters), hot leaderboard scrape (clean), cluster-level cross-reference against hermes/, tiered cross-reference sweep (15 queries). Full playbook: corpusiq-docs-management skill, references/daily-skills-sweep-cron.md + references/sweep-run-log.md.
