---
title: "Kangarooking Skills - Agent Harness Suite Setup"
description: "Setup guide for kangarooking/kangarooking-skills - 19 custom agent skills: twitter monitor, book illustration, harness engineering, multi-agent image."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kangarooking-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "twitter", "harness", "multi-agent"]
---

# Kangarooking Skills - Setup Guide

**Source:** [kangarooking/kangarooking-skills](https://github.com/kangarooking/kangarooking-skills) (645⭐, pushed Sep 7, 2026)
**Skill:** `kangarooking/kangarooking-skills` (19 installable skills)
**Installs:** ~190 per top skill, ~1.5K combined (Sep 27, 2026 snapshot)
**Category:** Agent Engineering / Mixed Utility
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

A personal-but-popular collection (645 GitHub stars) of 19 custom agent skills covering agent engineering and content production: a Twitter monitor, book-illustration workflow, harness engineering and task-harness patterns, multi-agent image pipelines, viral topic/title research, and video downloading. The harness skills (`harness-engineering`, `task-harness`) document patterns for building skill harnesses around agents - useful reference material for anyone operating their own agent fleet.

---

## Installation

```bash
# Full suite
npx skills add kangarooking/kangarooking-skills

# Single skill
npx skills add kangarooking/kangarooking-skills --skill twitter-monitor
```

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| twitter-monitor | 198 | Monitor Twitter for topics/accounts |
| book-illustration-workflow | 190 | Illustrate books and long-form content |
| harness-engineering | 180 | Build skill harnesses around agents |
| multi-agent-image | 179 | Multi-agent image generation pipeline |
| reshape-your-life | 178 | Personal-systems workflow |
| task-harness | 176 | Task execution harness pattern |
| video-downloader | 88 | Download videos for analysis |
| viral-topic | 68 | Viral topic research |
| viral-title | 66 | Viral title generation |

Plus `apimart-image-gen`, `hy-3d-gen`, `scroll-promo-site-builder`, and more (19 total).

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Harness reference** | `harness-engineering` and `task-harness` inform CorpusIQ's own agent-harness design |
| **Social monitoring** | `twitter-monitor` is a reference for mining workflows |
| **Content research** | `viral-topic` / `viral-title` feed angle research for social cadence |

## Limitations / Verification

- Mixed-quality personal collection; vet each skill before production use
- Top install counts are modest (~200); long tail of the suite is niche
- Verify: `npx skills add kangarooking/kangarooking-skills --list` shows 19 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Vigiles - Agent Harness Quality Suite Setup](/hermes/skills/catalog/vigiles-setup)
- [Paperthin - Agentic Design Patterns Setup](/hermes/skills/catalog/paperthin-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
