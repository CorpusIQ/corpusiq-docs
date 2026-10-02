---
title: Blacktwist Social Media Skills - 14-Skill Content Suite
description: "blacktwist/social-media-skills - 14 Agent Skills for social media content strategy, creation, and analysis across LinkedIn, X, Threads, Bluesky, Instagram, TikTok, and more. 21.4K skills.sh installs, all security audits pass."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/blacktwist-social-media-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "social media", "content strategy", "linkedin", "twitter"]
---

# Blacktwist Social Media Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/blacktwist/social-media-skills/social-media-context-sms) (14 core skills, ~21,400 combined installs)
**GitHub:** [blacktwist/social-media-skills](https://github.com/blacktwist/social-media-skills) (490⭐, 80 forks, MIT)
**Category:** Marketing / Social Media
**First Seen:** Sep 9, 2026 sweep (cluster surfaced via failed-query compensation; not previously evaluated)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

A 14-skill suite that turns an agent into a social media content engine: platform context capture, content strategy and calendaring, per-platform post/thread/carousel/caption writing, hook generation, content repurposing, and performance analysis. Built for text-first platforms (LinkedIn, X, Threads, Bluesky) with dedicated caption support for visual-first platforms (Instagram, TikTok, Facebook, Pinterest, YouTube). Every skill is standard Agent Skills format (SKILL.md) with no platform binding.

---

## Installation

Selective install via the skills.sh CLI (recommended - pick only what you need):

```bash
npx skills add blacktwist/social-media-skills --skill post-writer-sms hook-writer-sms
```

Full-suite install (all 14 skills):

```bash
npx skills add blacktwist/social-media-skills
```

List available skills first:

```bash
npx skills add blacktwist/social-media-skills --list
```

The CLI installs to `.agents/skills/` (and symlinks into `.claude/skills/`). For Hermes Agent, copy the skill folders into the agent's skills directory:

```bash
# From a clone
git clone https://github.com/blacktwist/social-media-skills.git
cp -r social-media-skills/skills/* ~/.hermes/skills/
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with a skills directory (`~/.hermes/skills/`) |
| **Node.js 18+** | For the `npx skills` path |
| **Platform context** | The suite is prompt-driven; no API keys required - supply platform handles, audience details, and content pillars to `social-media-context-sms` once |

## Skill Roster

| Group | Skills |
|---|---|
| **Foundation** | `social-media-context-sms` - captures platform context, audience details, content pillars, tone preferences used by every other skill |
| **Strategy** | `content-strategy-sms` (pillars, targeting, positioning) · `content-calendar-sms` (cadence, themes, scheduling) · `platform-strategy-sms` (per-platform approach) |
| **Creation** | `post-writer-sms` (standalone posts) · `thread-writer-sms` (multi-post threads with narrative arc) · `carousel-writer-sms` (slide-by-slide LinkedIn carousels) · `caption-writer-sms` (visual-platform captions) · `content-repurposer-sms` (cross-format adaptation) · `hook-writer-sms` (opening lines) |
| **Analysis** | `content-pattern-analyzer-sms` (what's working) · `performance-analyzer-sms` (metrics) · `optimization-advisor-sms` (iteration) · `audience-growth-tracker-sms` (follower/momentum tracking) |

## Quick Start

1. Install the skills (above)
2. Run `social-media-context-sms` first - feed it platform handles, audience, pillars, and tone
3. Ask for a post ("write a LinkedIn post about X") - the agent auto-selects `post-writer-sms`, `thread-writer-sms`, or `carousel-writer-sms` by request shape
4. Iterate with `optimization-advisor-sms` and track with `performance-analyzer-sms`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social cadence engine** | CorpusIQ's all-platform posting schedule gets structured per-platform drafting (LinkedIn posts, X threads, IG captions) with consistent voice via the shared context skill |
| **Content repurposing** | Turn newsletter/blog content into platform-adapted posts with `content-repurposer-sms` instead of one-size-fits-all cross-posting |
| **Help-first UGC** | Operator-problem posts drafted fast with `hook-writer-sms` + `post-writer-sms` - the help-first doctrine applied at draft time |
| **Growth experiments** | `content-pattern-analyzer-sms` + `performance-analyzer-sms` give the agent a structured loop for testing angles and doubling down on winners |

## Limitations / Verification

- **Repo cadence:** last pushed May 2026 - content reflects platform norms as of then; treat platform-specific claims (character limits, format rules) as re-verifiable
- **Prompt-workflow skills:** no API bindings - analysis skills read pasted/exported data rather than platform APIs
- **Alias noise on skills.sh:** the 7 extra 1-install listings (e.g. `post-writer` vs `post-writer-sms`) are index aliases; the 14 `-sms` skills are the real ones

```bash
# Verify skill installed
ls ~/.hermes/skills/post-writer-sms/SKILL.md
```

## Security

All three skills.sh security audits pass (verified Sep 9, 2026, spot-checked on `social-media-context-sms`, `post-writer-sms`, `content-strategy-sms`):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Pass |

## Related

- [Charlie Hills Social Media Skills - 17-Skill Content System Setup](/hermes/skills/catalog/charlie-hills-social-media-skills-setup)
- [Marketing Mindset - B2B Marketing OS for AI Agents Setup](/hermes/skills/catalog/marketing-mindset-setup)
- [Social Media - Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
