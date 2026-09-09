---
title: "Charlie Hills Social Media Skills - 17-Skill Content System Setup for Hermes Agents"
description: "charlie947/social-media-skills - the complete 17-skill content system behind Charlie Hills' 415K-follower operation: voice-builder foundation, LinkedIn posts, carousels, hook generation, post scoring, Reels scripting, thumbnails. 17.2K skills.sh installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/charlie-hills-social-media-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "social media", "content system", "linkedin", "brand voice"]
---

# Charlie Hills Social Media Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/charlie947/social-media-skills/voice-builder) (17 skills, ~17,200 combined installs)
**GitHub:** [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) (3,357⭐, 789 forks, MIT, active Aug 2026)
**Category:** Marketing / Social Media
**First Seen:** Sep 9, 2026 sweep (cluster surfaced via failed-query compensation; not previously evaluated)
**Quality Tier:** 🟡 Production with per-skill caveats (15 of 17 skills Pass all audits; `voice-builder` carries a Snyk CRITICAL flag, `reels-scripting` carries Trust Hub + Snyk Warns — see Security)

The complete skill system behind [Charlie Hills](https://charliehills.substack.com)' content operation — 415K+ followers across LinkedIn, Instagram, Substack, X, and YouTube with 100M+ views per year. Every skill reads shared context: `voice-builder` produces `about-me.md` and `voice.md`, and every other skill checks those files before drafting a line, so everything ships in one consistent brand voice.

---

## Installation

```bash
npx skills add charlie947/social-media-skills
```

For Hermes Agent, copy into the skills directory from a clone:

```bash
git clone https://github.com/charlie947/social-media-skills.git
cp -r social-media-skills/skills/* ~/.hermes/skills/
```

**Order matters:** run `voice-builder` first. Every other skill reads `about-me.md` + `voice.md` and degrades without them.

## Prerequisites

| Variable | Needed for |
|---|---|
| `APIFY_API_TOKEN` | `post-scorer`, `reels-scripting` |
| `GOOGLE_AI_API_KEY` | `reels-scripting` (Gemini 2.5 Flash video analysis) |

```bash
export APIFY_API_TOKEN=your_token
export GOOGLE_AI_API_KEY=your_key
```

The image skills (`gemini-infographic`, `gemini-carousel`, `quote-post`, `youtube-thumbnail`, `profile-optimizer`) output ready-to-paste Gemini prompts — no API key needed.

## Skill Roster

| Group | Skills |
|---|---|
| **Voice foundation** | `voice-builder` (interview + writing samples → `about-me.md`, `voice.md`) · `newsletter-voice` (newsletter rules on top) |
| **LinkedIn** | `profile-optimizer` (full profile rebuild) · `post-writer` (drafts in your voice) · `graphic-designer` (HTML/CSS graphic or AI infographic) · `post-formatter` (PAS/AIDA/BAB/STAR/SLAY frameworks) · `hook-generator` (6 hook variations per topic) · `post-scorer` (scores drafts against post history) · `content-matrix` (pillars × formats ideation) · `niche-research` (7-day niche research) · `gemini-infographic` · `gemini-carousel` · `quote-post` (two-step quote workflow) |
| **Instagram Reels** | `reels-scripting` (Apify + Gemini 2.5 Flash reference analysis, newsletter-aligned script) |
| **YouTube** | `youtube-thumbnail` (title → Gemini thumbnail prompt) |
| **Community** | `pinned-comment` (meme-style pin + image prompt) |
| **Analytics** | `analytics-dashboard` (LinkedIn export → dashboard + 5 recommendations) |

## Quick Start

1. Install skills, set env vars for the analytics/reels skills
2. Run `voice-builder`: answer a short interview, paste 3-5 writing samples
3. Draft: "Write me a post about AI agents" → `post-writer`; "Score this draft against my history" → `post-scorer`; "Make me a carousel from this" → `gemini-carousel`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Brand voice lock** | CorpusIQ's content voice rules get a working voice-profile mechanism (`about-me.md` + `voice.md`) that every post draft reads — consistency across all platforms |
| **LinkedIn growth ops** | Operator-facing LinkedIn posts with hook variants and history-scored drafts — the lead-generation channel |
| **Newsletter-first repurposing** | `newsletter-voice` + per-platform skills mirror the CorpusIQ belief-bridge content flow (one source piece, platform-adapted output) |
| **Reels/Shorts pipeline** | `reels-scripting` feeds the UGC video pipeline script selection; `youtube-thumbnail` feeds thumbnail prompts |

## Limitations / Verification

- **Voice profile files live in the project** — `about-me.md`/`voice.md` are written into the working project, not the agent install; keep them under version control to reuse across sessions
- **External deps for 2 skills** — `post-scorer` and `reels-scripting` need Apify; `reels-scripting` also needs a Gemini key
- **Security flags on 2 skills** — see below; install the other 15 freely

```bash
# Verify skill installed
ls ~/.hermes/skills/voice-builder/SKILL.md ~/.hermes/skills/post-writer/SKILL.md
```

## Security

Spot-checked Sep 9, 2026: `post-writer`, `hook-generator` Pass all three audits. Two flagged skills:

| Skill | Trust Hub | Socket | Snyk | Note |
|---|---|---|---|---|
| `voice-builder` | Pass | Pass | **Fail (CRITICAL)** | E004: contradictory instruction detected — the skill states it must produce `voice.md` and later says "Do not produce an voice.md file"; Snyk reads it as a hidden directive (0.80). Also W011 (third-party content ingestion — inherent to its interview workflow). Use with care; review SKILL.md before running, or build the voice files manually |
| `reels-scripting` | **Warn** | Pass | **Warn** | W011 third-party content exposure via Apify/Gemini reference analysis — inherent to the workflow |

The remaining 15 skills carry clean audits. The publisher is a well-known creator (3.4K⭐ repo, public newsletter, contributions welcome) — the CRITICAL flag reads as a wording bug, not injected content, but treat the skill with the usual untrusted-input discipline and review its instructions before first run.

## Related

- [Blacktwist Social Media Skills - 14-Skill Content Suite Setup](/hermes/skills/catalog/blacktwist-social-media-skills-setup/)
- [Content Strategy - Skills Marketplace](/hermes/skills/marketplace/)

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
