---
title: Guizang Social Card Skill — Setup Guide for Hermes Agents
description: Generate polished social card images for Xiaohongshu, WeChat, and platform thumbnails — 3.7K+ installs
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/guizang-social-card-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Guizang Social Card Skill — Setup Guide

**Source:** [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) (Community)
**Skill:** `guizang-social-card-skill` · **Installs:** 3,700+ · **Category:** Content & Media
**Platform:** Linux, macOS, Windows

The Guizang Social Card Skill creates polished social card packages for Xiaohongshu (Rednote), WeChat Official Accounts, article covers, and platform thumbnails. It produces carousel image sets, Live Photo motion cards, triple-collage layouts, and WeChat cover pairs — all with Swiss-style editorial design. Perfect for Hermes agents managing social media content pipelines.

## Installation

```bash
npx skills add op7418/guizang-social-card-skill@guizang-social-card-skill
```

## What It Does

The skill generates multiple social card formats:

| Format | Platform | Description |
|--------|----------|-------------|
| Carousel image sets | Xiaohongshu | Cover + content pages in 3:4 ratio |
| Live Photo motion cards | Xiaohongshu | Short motion cards from video |
| Puzzle layouts | Xiaohongshu | Multi-grid video collages |
| Cover pairs | WeChat | 21:9 main + 1:1 square covers |
| Screenshot posts | Cross-platform | Product/tutorial carousels |

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v1.0+ |
| Content assets | Screenshots, photos, videos, or article text |
| Image generation | Access to image generation tools |
| Output directory | Task-specific folder (not skill root) |

## Usage with Hermes

Trigger with natural language:

```
"Create a Xiaohongshu carousel for our product launch"
"Generate social card images from this article"
"Make Live Photo motion cards from this video"
"Create WeChat cover pair for our blog post"
"Build a screenshot tutorial carousel"
```

### Example: Product Launch Carousel

```
"Create a 6-slide Xiaohongshu carousel for CorpusIQ — cover slide with product name, then 5 feature slides with screenshots"
```

The skill produces:
1. Cover slide (3:4 ratio, Swiss-style layout)
2. Five content slides with screenshots and description text
3. All rendered as HTML for visual checking before export

## Design Style

The skill applies Guizang-style Swiss/editorial magazine layouts:
- Clean, minimal typography
- Screenshot-heavy content with subtle frames
- Material-first approach for video content
- Consistent color palettes and spacing

## Important Rules

- **Generated work lives in task folders** — Default: `local-tests/<slug>/` or user-specified output directory
- **Never create root-level folders** — No `social-card-*`, `livephoto-*`, `wechat-*`, or `output/` at project root
- **Self-contained** — Doesn't modify the original PPT skill, templates, or references

## Related Skills

- [AI Video Generation Setup](/docs/hermes/skills/catalog/ai-video-generation-setup/) — Video content creation
- [HyperFrames Setup](/docs/hermes/skills/catalog/hyperframes-setup/) — Programmatic video generation
- [Skills Collective AI Media Setup](/docs/hermes/skills/catalog/skills-collective-ai-media-setup/) — Image and video skills

## Source

- **skills.sh:** [op7418/guizang-social-card-skill@guizang-social-card-skill](https://skills.sh/op7418/guizang-social-card-skill)
- **GitHub:** [github.com/op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)
