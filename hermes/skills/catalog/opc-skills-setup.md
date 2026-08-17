---
title: "OPC Skills — Solopreneur Toolkit for AI Agents (SEO,"
description: resciencelab's OPC skills — solopreneur-focused agent skills for SEO-GEO, Reddit marketing, logo creation, product launches, and social media. 50K+ combined installs across 6 skills. Built for solo operators who need AI agents to handle growth work.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/opc-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# OPC Skills — Setup Guide

**Source:** [resciencelab/opc-skills](https://skills.sh/resciencelab/opc-skills) (50K+ combined installs)
**GitHub:** [resciencelab/opc-skills](https://github.com/resciencelab/opc-skills) (1,174 ⭐)
**Category:** Growth Operations / Solopreneur
**Quality Tier:** 🟢 Production

OPC (One-Person Company) Skills is a curated toolkit for solopreneurs who use AI agents to handle growth and operations work. Covering SEO-GEO, Reddit engagement, branding, product launches, and social media, these skills encode the playbooks that solo founders use to compete with funded teams. For CorpusIQ's operator audience and Hermes growth agents, OPC Skills provides ready-to-deploy growth workflows.

---

## Installation

```bash
# Growth & SEO (most-installed)
npx skills add resciencelab/opc-skills --skill seo-geo
npx skills add resciencelab/opc-skills --skill reddit

# Branding & creative
npx skills add resciencelab/opc-skills --skill logo-creator
npx skills add resciencelab/opc-skills --skill nanobanana

# Launch & social
npx skills add resciencelab/opc-skills --skill producthunt
npx skills add resciencelab/opc-skills --skill twitter
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **seo-geo** | 37.0K | Geo-targeted SEO — local search, multi-region strategy, hreflang, international ranking |
| **reddit** | 3.0K | Reddit marketing — subreddit discovery, post timing, comment engagement, karma-building |
| **logo-creator** | 2.6K | AI-assisted logo design — brief-to-concept, iteration, export-ready formats |
| **nanobanana** | 2.6K | Micro-branding assets — social profile images, favicons, banner templates |
| **producthunt** | 2.5K | Product Hunt launch playbook — listing optimization, hunter outreach, launch day tactics |
| **twitter** | 1.9K | Twitter/X growth — thread writing, engagement patterns, growth tactics for founders |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **skills.sh CLI** | `npx skills` (auto-installed) |
| **AI coding agent** | Any skills.sh-compatible agent (Hermes, Claude Code, Codex) |
| **SEO-GEO**: Google Search Console | For geo-performance data (optional) |
| **Product Hunt**: PH account | For launch scheduling and hunter coordination |
| **Logo-creator**: Image gen API | OpenAI DALL-E or local Stable Diffusion |

---

## Key Capabilities

### SEO-GEO (37.0K installs)
The most-installed solopreneur skill on skills.sh. Geo-targeted SEO strategies for international and local search: hreflang tag configuration, multi-region content strategy, local keyword research, Google Business Profile optimization, and country-specific ranking factors. 37K installs makes this the de facto standard for AI-assisted international SEO. Previously had a minimal platform entry — this publisher-level guide provides complete coverage.

### Reddit Marketing (3.0K installs)
Reddit engagement playbook for founders: subreddit discovery and analysis, post timing optimization (when each subreddit is most active), comment-first engagement patterns (provide value before promoting), karma-building strategy, and avoiding ban triggers. Directly applicable to CorpusIQ's Reddit growth operations.

### Product Hunt Launch (2.5K installs)
End-to-end Product Hunt launch workflow: listing copy optimization, hunter identification and outreach templates, launch day checklist (maker comment, social amplification, community engagement), post-launch follow-up, and badge integration on landing pages. For founders timing their first PH launch — this is the playbook.

### Twitter/X Growth (1.9K installs)
Founder-focused Twitter growth: thread writing patterns that drive engagement, reply-game strategy (which conversations to join), growth tactics (collaborative threads, quote-tweet value-adds), and content calendar structuring. Complements CorpusIQ's existing X/Twitter automation tools.

### Logo Creator (2.6K installs)
AI-assisted logo design workflow: brief-to-concept pipeline, style exploration across multiple directions, iteration based on feedback, and export-ready formats (SVG, PNG at multiple resolutions). Useful for rapid branding when you don't have a designer.

### Nanobanana (2.6K installs)
Micro-branding asset generation: social media profile images (optimized per platform), favicon generation, Open Graph image templates, email signature banners, and consistent color palette application across all assets. The "everything else" branding skill after the logo is done.

---

## Quick Start

```bash
# 1. Start with the big one
npx skills add resciencelab/opc-skills --skill seo-geo

# 2. Add your launch/growth stack
npx skills add resciencelab/opc-skills --skill producthunt
npx skills add resciencelab/opc-skills --skill reddit

# 3. Verify
npx skills list | grep opc-skills
```

---

## Verification

```bash
# Check installed OPC skills
npx skills list | grep resciencelab/opc-skills

# Expected output lists each installed skill
```

---

## Notes

- **Built for solopreneurs**: Every skill targets the "I'm doing this myself" use case — no enterprise complexity, no team-assumptions baked in.
- **SEO-GEO is the standout**: 37K installs is massive for a single skill. Geo-targeted SEO is one of the highest-ROI growth channels for SaaS products.
- **Reddit caution**: Reddit communities are sensitive to promotional content. The skill's "help-first" patterns align with CorpusIQ's own content doctrine — good synergy.
- **Product Hunt is tactical**: Launches are high-effort, high-reward events. This skill compresses weeks of research into an executable playbook.
- **Complementary skills**: Reddit skill pairs with CorpusIQ's `reddit-praw-automation`; Twitter skill pairs with `xurl` and Postiz social deployment; SEO-GEO pairs with upcoming SEO automation work.
