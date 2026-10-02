---
title: "New Skills - September 9, 2026 (Morning)"
description: "skills.sh morning sweep: forcedotcom/sf-skills (~500K installs, official Salesforce library), agricidaniel/claude-seo (~160K, 31 SEO skills, July 23 rejection overturned), blacktwist/social-media-skills (21.4K, 14 skills), charlie947/social-media-skills (17.2K, 17 skills) - 4 new publisher clusters, 162+ skills, 4 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep9-2026/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills", "salesforce", "seo", "social media"]
sweep_id: "2026-09-09-morning"
new_publishers: 4
new_skills: 162
guides_drafted: 4
---

# New Skills - September 9, 2026 (Morning)

Forty-three-query skills.sh API sweep (3,776 unique skills; 2 queries failed - `social media` and `content` - and were compensated with targeted re-fetches that surfaced this batch), cluster-level cross-reference against the full hermes/ tree, hot-leaderboard coverage check (clean, all catalog-covered), and the tiered cross-reference sweep (65 NEW flags, all <100 installs, all standing rejections). Four genuinely new publisher clusters cleared the drafting bar.

## New Skills

| Skill | Publisher | Installs | Category | What It Does |
|---|---|---|---|---|
| 100+ skills (`platform-apex-generate`, `agentforce-generate`, ...) | forcedotcom/sf-skills | ~500K combined | CRM / Development | Salesforce's official agent skills library: Apex, Flow, SOQL, LWC, Agentforce, Experience Cloud, Commerce B2B, Data360, Omnistudio, DX DevOps - 334 SKILL.md files, Apache-2.0 |
| 31 skills (`seo`, `seo-audit`, `seo-geo`, ...) | agricidaniel/claude-seo | ~160K combined | SEO | Universal SEO suite: 500-page parallel audits, E-E-A-T content, schema, GEO/AEO, backlinks, local/ecommerce/international SEO + 8 extension skills. 16.6K⭐. July 23 "Claude-Code-specific" rejection overturned |
| 14 skills (`post-writer-sms`, `hook-writer-sms`, ...) | blacktwist/social-media-skills | 21,382 | Social Media | Strategy, creation, and analysis skills for LinkedIn, X, Threads, Bluesky + visual-platform captions. 490⭐, MIT. All audits Pass |
| 17 skills (`voice-builder`, `post-writer`, `reels-scripting`, ...) | charlie947/social-media-skills | 17,153 | Social Media | Charlie Hills' content system (415K followers, 100M+ views/yr): voice foundation, LinkedIn suite, Reels, thumbnails, analytics. 3.4K⭐, MIT |

## Setup Guides

- [Salesforce Skills Library (sf-skills) - Setup Guide](/hermes/skills/catalog/salesforce-sf-skills-setup)
- [Claude SEO - Setup Guide](/hermes/skills/catalog/claude-seo-setup)
- [Blacktwist Social Media Skills - Setup Guide](/hermes/skills/catalog/blacktwist-social-media-skills-setup)
- [Charlie Hills Social Media Skills - Setup Guide](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)

## Evaluated and Skipped

| Cluster | Installs | Reason |
|---|---|---|
| lignertys/reddit-research-skills | 18,539 | FAMILY-KNOWN - already covered by reddit-research-setup.md (source-line variant `reddit-research-skill`) |

All other sweep candidates (65 NEW flags from the tiered cross-reference) mapped to the standing-rejection roster recorded in the corpusiq-docs-management skill run-log; no other bar-clearers, no other overturns.

## Security Notes

Three of four clusters are 🟡 tier with disclosed per-skill audit flags: `charlie947` - `voice-builder` carries a Snyk CRITICAL (E004 contradictory instruction) and `reels-scripting` Trust Hub + Snyk Warns (15 of 17 skills clean); `agricidaniel` - Snyk Warn (W011 third-party content exposure, inherent to SEO workflows); `forcedotcom` - `experience-content-media-search` Snyk HIGH (W007 signed-URL handling) and `agentforce-generate` Socket Warn (98+ of 100 skills clean). `blacktwist` passes all three audits across spot-checks.

## Source

skills.sh API sweep (43 queries, 3,776 unique skills + compensated re-fetch of 2 failed queries), hot leaderboard scrape (clean), cluster-level cross-reference against hermes/, tiered cross-reference sweep (15 queries). Full playbook: corpusiq-docs-management skill, references/daily-skills-sweep-cron.md + references/sweep-run-log.md.
