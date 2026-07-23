---
title: Skills Collective AI Media — Image & Video Generation for Hermes Content Agents
description: AI image generation, image-to-video conversion, and video editing. 100K+ combined installs across 2 new skills from skills-collective (plus ai-video-generation already catalogued).
---

# Skills Collective — AI Media Skills Setup Guide

**Source:** [skills-collective/skills](https://skills.sh/skills-collective/skills) (100K+ combined for 2 new skills)
**Category:** AI Media / Content Creation
**Quality Tier:** 🟡 Beta

Two new AI media generation skills from skills-collective, complementing the already-catalogued `ai-video-generation` (49K installs). Covers AI image generation and image-to-video conversion — both with ~49K+ installs each.

---

## Installation

```bash
npx skills add skills-collective/skills --skill ai-image-generation
npx skills add skills-collective/skills --skill image-to-video
npx skills add skills-collective/skills --skill video-edit
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **ai-image-generation** | 49.9K | Generate images from text prompts using multiple AI models |
| **image-to-video** | 49.5K | Animate static images into short video clips |
| **video-edit** | 49.3K | Video editing operations — trim, merge, transitions, captions |

---

## Quick Start

```bash
# Generate social media images
npx skills use skills-collective/skills@ai-image-generation

# Animate product screenshots into video
npx skills use skills-collective/skills@image-to-video

# Edit and polish video content
npx skills use skills-collective/skills@video-edit
```

---

## Verification

```bash
npx skills list | grep skills-collective
```

---

## Notes

- `ai-video-generation` from same publisher already catalogued at [ai-video-generation-setup](/hermes/skills/catalog/ai-video-generation-setup/) (49K installs)
- `image-to-video` complements HeyGen/HyperFrames video pipelines for quick animated content
- `ai-image-generation` useful for social media and blog post images
- Quality tier 🟡 Beta: 100K+ combined for 2 new skills, 149K+ including ai-video-generation
