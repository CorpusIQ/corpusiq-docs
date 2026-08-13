---
title: Pika Plugins — Video Creation Skill Pack Setup Guide for Hermes Agents
description: Install the pika-labs/pika-plugins cluster (20.1K installs, 22 skills) — ugc-ads, build-a-brand, founder-product-video, app-sizzle, explainer, viral-hook, persona-builder, content-director, VFX family for Pika video generation.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pika-plugins-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Pika Plugins — Setup Guide

**Source:** [pika-labs/pika-plugins](https://www.skills.sh/pika-labs/pika-plugins) (22 skills · 20.1K combined installs)
**Repo:** [github.com/pika-labs/pika-plugins](https://github.com/pika-labs/pika-plugins)
**Category:** AI Media / Marketing Video
**First Seen:** August 13, 2026
**Quality Tier:** 🟢 Production core (`ugc-ads`, `build-a-brand`, `founder-product-video`, `app-sizzle` at 1.5K each)

Pika's official plugin pack turns a video model into a marketing production line. The business-relevant half covers UGC ads, brand building, founder product videos, app sizzle reels, app store screens, explainers, and podcast clips. The creative half covers hooks, personas, content direction, and the VFX family. For an agent that already has a video backend, these skills are the creative direction layer that decides what to generate and why.

---

## Installation

```bash
# Full cluster
npx skills add pika-labs/pika-plugins

# Hermes: install individual skills by identifier
hermes skills install pika-labs/pika-plugins/ugc-ads
hermes skills install pika-labs/pika-plugins/founder-product-video
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `ugc-ads` | 1.5K | User-generated-content style ad creative |
| `build-a-brand` | 1.5K | Brand identity video kits |
| `founder-product-video` | 1.5K | Founder-led product demos |
| `app-sizzle` | 1.5K | Fast-cut app feature reels |
| `app-store-screens` | 1.5K | Store screenshot motion |
| `explainer` | 1.5K | Explainer video structure |
| `podcast` | 1.5K | Podcast clip production |
| `viral-hook` | 757 | Opening hooks engineered for retention |
| `persona-builder` | 739 | On-screen persona design |
| `content-director` | 735 | Creative direction across clips |
| `language-swap` | 988 | Multi-language video variants |
| VFX family: `4k-vfx`, `vfx`, `fix-my-look`, `voxel-it`, `stagefight` | 365–508 | Visual effects and transformations |
| Sports/fun: `gameday`, `baseball-trend`, `kiss-cam`, `anime-soccer`, `world-cup-anime`, `anime-match` | 1–1.5K | Entertainment formats |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Pika account/API | The generation backend these prompts target |
| Node.js + npx | For the skills.sh CLI install path |
| Any agent runtime | Skills are procedural — no runtime-specific code |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC-style social video** | `ugc-ads` + `viral-hook` for TikTok and Reels creative |
| **Founder content** | `founder-product-video` structure for product walkthroughs |
| **App store assets** | `app-sizzle` and `app-store-screens` for listing creative |
| **Brand kits** | `build-a-brand` for consistent visual identity across clips |

---

## Limitations / Verification

- Requires Pika as the generation backend — prompts are Pika-tuned
- Sports/entertainment skills are niche — skip unless that content vertical matters
- Verify install: `npx skills list | grep pika`

---

## Related

- [GenMedia Skills Setup](/hermes/skills/catalog/genmedia-skills-setup/)
- [RunComfy Agent Skills Setup](/hermes/skills/catalog/runcomfy-agent-skills-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
