---
title: "New Skills - October 1, 2026 - HeroUI, Redis, Vercel Plugin"
description: "Skills.sh sweep (Oct 1, 2026): 3 new publisher guides - heroui-inc/heroui (25.7K), redis/agent-skills (19.9K), vercel/vercel-plugin (4.8K)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct1-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-01"
tags: ["hermes skill", "agent skill", "skills.sh", "new skills", "heroui", "redis", "vercel"]
---

# New Skills - October 1, 2026 Sweep

Sweep snapshot: **714 unique skills** across 15 queries (0 failed). Tiered crossref: **16 NEW / 145 PARTIAL** (NEW ≥100 installs: 4; PARTIAL ≥100: 35, reconcile backlog deferred).

## New Publisher Guides

### heroui-inc/heroui - HeroUI React & Native UI Skills

| Field | Value |
|---|---|
| Source | [heroui-inc/heroui](https://github.com/heroui-inc/heroui) |
| Stars | 30,850⭐ (previously NextUI) |
| License | Apache-2.0 (LICENSE in-repo) |
| Installs | ~25,747 combined across 3 indexed listings |
| Skills | 3 installable (heroui-react, heroui-native, heroui-migration) |
| Quality Tier | 🟢 Verified (official org, Apache-2.0, same-day commits) |
| Setup Guide | [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup) |

HeroUI's official skill family teaches an agent the v3 component APIs (Tailwind CSS v4 + React Aria) instead of writing props from memory. `heroui-react` (11,508) is the flagship; `heroui-native` (10,339) covers React Native via Uniwind; `heroui-migration` (3,900) handles the v2→v3 upgrade. Note the default branch is `v3`, not `main`.

### redis/agent-skills - Official Redis Data & Caching Skills

| Field | Value |
|---|---|
| Source | [redis/agent-skills](https://github.com/redis/agent-skills) |
| Stars | 163⭐ |
| License | MIT (LICENSE in-repo; per-skill `license: MIT`) |
| Installs | ~19,866 combined across 12 indexed listings |
| Skills | 12 indexed (16 SKILL.md in-repo, plugin-duplicated) |
| Quality Tier | 🟡 Trusted (official Redis, Inc. publisher; low star count) |
| Setup Guide | [Redis Agent Skills - Official Data Modeling & Caching Setup](/hermes/skills/catalog/redis-agent-skills-setup) |

Redis, Inc.'s official skill collection covers the decisions agents get wrong most: data-structure selection (`redis-core`, 3,337), connections (2,375), security (2,055), observability (1,967), clustering (1,583), and search (1,308), plus AI-focused `redis-semantic-cache` (1,645) and `iris-development` (1,451, Redis Agent Memory).

### vercel/vercel-plugin - Full Vercel Ecosystem Plugin

| Field | Value |
|---|---|
| Source | [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) |
| Stars | 295⭐ |
| License | NOASSERTION (LICENSE file present, no recognized SPDX) |
| Installs | ~4,768 combined across 11 indexed listings |
| Skills | 11 indexed (50 SKILL.md in-repo) |
| Quality Tier | 🟡 Trusted (official Vercel org, same-day cadence; license unverified) |
| Setup Guide | [Vercel Plugin Skills - Full Vercel Ecosystem Agent Setup](/hermes/skills/catalog/vercel-plugin-skills-setup) |

The broad "teach an agent the whole platform" plugin - AI Gateway, AI SDK, backend architecture, deployment protection (`access-protected-vercel-deployment`, 2,433), `build-agents` (1,399), flags, and queues. Distinct from the three narrower Vercel guides already documented (vercel-labs/agent-skills, vercel/ai, vercel/eve).

## Roster Reconciles

**garrytan/gstack family → aicreator-wind/gstack-openclaw-skills.** A third-party **Chinese-language OpenClaw adaptation** of the gstack workflow surfaced as NEW (`aicreator-wind/gstack-openclaw-skills`, 164 installs, 44⭐, MIT, 24 SKILL.md). Below the guide floor (~165 combined) and a derivative of the already-documented [garrytan/gstack](https://github.com/garrytan/gstack) family (57 indexed listings, 40.1K installs). No new guide - noted here as an out-of-tree adaptation for awareness.

## Skipped (below floor)

12 NEW publishers under the 100-install guide floor, including: `learnprompt/awesome-seedance` (18), `inference-sh/skills` (11), `nvidia/cuopt` (99 combined across 27 skills - below floor; `cuopt-skill-evolution` also appears via the `nvidia/skills` family at 1,315), and several `costrict-plugins-repo` / `satnamrsm` re-published `sickn33/antigravity-awesome-skills` Odoo bundles (1 install each).

**PARTIAL reconcile backlog:** 35 PARTIAL items ≥100 installs across ~20 documented families deferred to a dedicated roster-reconcile pass.

---

*Sweep run: Oct 1, 2026, skills-monitor cron. Cross-ref: one-pass ripgrep on Mac Mini.*
