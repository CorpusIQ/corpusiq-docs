---
title: "Layer Skills - AI Game Asset Creation Suite Setup"
description: "Setup guide for layerai/skills - 15 agent skills for Layer's AI game asset creation: image editing, 3D, pixel art, audio, video, and art direction."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/layerai-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "game assets", "image generation", "3d"]
---

# Layer Skills - Setup Guide

**Source:** [layerai/skills](https://github.com/layerai/skills) (pushed Sep 27, 2026)
**Skill:** `layerai/skills` (15 installable skills)
**Installs:** ~925 per skill, ~13K combined (Sep 27, 2026 snapshot)
**Category:** Generative Media / Game Asset Creation
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

Layer (layer.ai) publishes the official agent skills for its generative-AI platform. The 15-skill suite covers the full asset-creation pipeline: image editing, 3D model generation, pixel art, audio, video timelines, workflows, reference sets, quality control, and art direction. Skills are installable via the skills CLI and call Layer's APIs, so an agent can produce game-ready assets in-session.

---

## Installation

```bash
# Full suite
npx skills add layerai/skills

# Single domain
npx skills add layerai/skills --skill layer-3d
```

A Layer account/API key is required for the underlying generation calls.

## Roster - Core Skills

| Skill | Installs | Does |
|---|---|---|
| layer | 927 | Platform entry skill: session setup and API auth |
| layer-image-editing | 926 | Edit existing images (backgrounds, objects, style transfer) |
| layer-3d | 926 | 3D asset and model generation |
| layer-pixel-art | 925 | Pixel-art sprite and tileset generation |
| layer-audio | 925 | SFX and music generation |
| layer-workflows | 924 | Multi-step asset pipelines |
| layer-video | 924 | Video generation and clips |
| layer-video-timeline | 924 | Timeline-based video composition |
| layer-reference-sets | 924 | Style/character reference management |
| layer-quality | 924 | Quality review and iteration |
| layer-image | 924 | Text-to-image generation |
| layer-art-direction | 924 | Coherent art direction across a project |
| layer-game-assets | 923 | In-game art as a system: characters, NPCs, environments, parallax layers, HUD/icon sets, Spine-ready parts |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC video assets** | `layer-image` and `layer-video` feed the CorpusIQ daily UGC pipeline |
| **Visual answers** | `layer-art-direction` keeps agent-generated report graphics on-brand |
| **Game-adjacent client work** | Asset packs for clients shipping games or gamified marketing |
| **Illustration workflow** | Pairs with `book-illustration-workflow`-style skills for content visuals |

## Limitations / Verification

- Requires a Layer account; generation is API-metered, not free
- Suited to asset production, not final-game engineering
- Verify: `npx skills add layerai/skills --list` shows 15 skills; then check the Layer API key is valid

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Generative Media Skills Setup](/docs/hermes/skills/catalog/generative-media-skills-setup)
- [Picsart Gen-AI Skills Setup](/docs/hermes/skills/catalog/picsart-gen-ai-skills-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
