---
title: GenMedia Skills — AI Media Generation Cluster Setup Guide for Hermes Agents
description: Install the genmedia-labs/skills cluster (42.5K installs) — video-edit, ai-music, ai-video-generation, ai-image-generation, image-to-video plus 25 model-specific generation skills (FLUX, Kling, GPT Image, Seedance, Wan, Nano Banana).
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/genmedia-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# GenMedia Skills — Setup Guide

**Source:** [genmedia-labs/skills](https://www.skills.sh/genmedia-labs/skills) (30 skills · 42.5K combined installs)
**Repo:** [github.com/genmedia-labs/skills](https://github.com/genmedia-labs/skills)
**Category:** AI Media / Video & Image Generation
**First Seen:** August 13, 2026
**Quality Tier:** 🟢 Production (`video-edit` 8.7K, `ai-music` 8.6K, `ai-video-generation` 8.5K installs)

GenMedia is the fastest-moving media cluster on skills.sh right now — `ai-video-generation` gained 372 installs in a single hour during the August 13 sweep. Five core skills cover the editing and generation workflow, while 25 model-specific skills pin the exact generation backends: FLUX 2 Klein, Kling 3.0, GPT Image 2, Seedance V2, Wan 2.7, Nano Banana 2, and more. One install command gives an agent the whole modern image/video generation surface.

---

## Installation

```bash
# Full cluster
npx skills add genmedia-labs/skills

# Hermes: install individual skills by identifier
hermes skills install genmedia-labs/skills/video-edit
hermes skills install genmedia-labs/skills/ai-video-generation
```

If the CLI rejects the multi-skill source, clone [genmedia-labs/skills](https://github.com/genmedia-labs/skills) and copy the skill directories into the agent's skills folder.

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `video-edit` | 8.7K | Editing and assembling video from agent pipelines |
| `ai-music` | 8.6K | Music generation and audio scoring |
| `ai-video-generation` | 8.5K | Text-to-video and image-to-video orchestration |
| `ai-image-generation` | 8.4K | Image generation across multiple backends |
| `image-to-video` | 8.4K | Animating stills into motion clips |
| `lipsync` | 1 | Lip-sync for avatar and character video |
| `face-swap` | 1 | Face replacement in video |
| `relight` | 1 | Scene relighting for images and video |
| `video-extend` / `video-inpainting` / `video-outpainting` | 1 | Video extension, repair, and canvas expansion |
| Model pins: `flux-2-klein`, `flux-kontext`, `kling-3-0`, `gpt-image-2`, `gpt-image-edit`, `seedance-v2`, `wan-2-7`, `nano-banana-2`, `nano-banana-edit`, `happyhorse-1-0`, `codex-pet` | 1 | Backend-specific generation recipes |
| `ai-avatar-video`, `image-edit`, `image-inpainting`, `image-outpainting`, `controlnet-pose`, `elevenlabs-music-generation`, `runcomfy-cli`, `ace-step` | 1 | Avatar video, image editing, music via ElevenLabs, RunComfy integration |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| Generation API keys | Per-model keys (FLUX, Kling, OpenAI, etc.) only for the backends you use |
| Any agent runtime | Skills are procedural — no runtime-specific code |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC video pipeline** | `ai-video-generation` + `image-to-video` for product motion clips |
| **Voiceover pairing** | `ai-music` for background scoring, `lipsync` for avatar narration |
| **Ad creative variants** | `flux-2-klein` + `gpt-image-2` recipes for rapid asset iteration |
| **Video repair** | `video-inpainting` / `video-extend` to fix or lengthen existing clips |

---

## Limitations / Verification

- Model skills at 1 install each are new — treat as recipes, verify against provider docs
- API costs accrue per backend; only pin models you have keys for
- Verify install: `npx skills list | grep -E 'video|image|music'`

---

## Related

- [RunComfy Agent Skills Setup](/hermes/skills/catalog/runcomfy-agent-skills-setup/)
- [Skills-101 Superpowers Setup](/hermes/skills/catalog/skills-101-superpowers-setup/)
- [Skills Catalog](/hermes/skills/catalog/)
