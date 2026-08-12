---
title: RunComfy Agent Skills — AI Video & Image Generation Platform for Hermes Agents
description: 30 production-grade media skills from prime-skills/runcomfy-agent-skills — AI video generation, avatar video, video editing, music generation. 61.1K+ combined installs via RunComfy cloud GPU platform.
---

# RunComfy Agent Skills — Setup Guide

**Source:** [prime-skills/runcomfy-agent-skills](https://skills.sh/prime-skills/runcomfy-agent-skills) (61.1K combined installs)
**GitHub:** [prime-skills/runcomfy-agent-skills](https://github.com/prime-skills/runcomfy-agent-skills)
**Platform:** [RunComfy](https://www.runcomfy.com) — cloud GPU platform for AI media generation
**Category:** AI Media / Video Production
**Quality Tier:** 🟡 Beta (first seen Jul 13, 2026)

RunComfy Agent Skills lets Hermes agents access 30+ AI models for video generation, image creation, avatar synthesis, and music production through a single CLI. For Hermes agents producing UGC videos, social content, or AI-generated media, RunComfy provides a complementary backend to HyperFrames and an alternative to HeyGen.

---

## Installation

```bash
# Full publisher install (all 30 skills)
npx skills add prime-skills/runcomfy-agent-skills

# Or individual skills
npx skills add prime-skills/runcomfy-agent-skills --skill ai-video-generation
npx skills add prime-skills/runcomfy-agent-skills --skill video-edit
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **RunComfy account** | Sign up at [runcomfy.com](https://www.runcomfy.com). Free tier available. |
| **RunComfy CLI** | `npm i -g @runcomfy/cli` then `runcomfy login` |
| **API token (CI)** | Set `RUNCOMFY_TOKEN=<token>` for headless/agent use |
| **Hermes Agent** | Any version with skills support |

---

## Core Skills

### Video Generation

| Skill | Installs | Purpose |
|---|---|---|
| **video-edit** | 401.7K | Intent-routed video editing — restyle, motion transfer, outfit/background swap |
| **image-to-video** | 400.3K | Animate still images — HappyHorse I2V, Wan 2.7, Seedance 2.0 |
| **ai-video-generation** | 345.1K | Full text-to-video + image-to-video via single CLI |
| **ai-avatar-video** | 342.5K | Talking head / avatar video with lip-sync |
| **video-inpainting** | 340.8K | Remove objects/people from video |
| **video-outpainting** | 339.2K | Extend video frame boundaries |
| **video-extend** | 339.7K | Extend video duration — Veo-style, Kling, Seedance |
| **lipsync** | 2.0K | Audio-driven lip synchronization |

### Image Generation & Editing

| Skill | Installs | Purpose |
|---|---|---|
| **ai-image-generation** | 2.1K | Full RunComfy image-model catalog |
| **image-edit** | 2.1K | Intent-routed image editing |
| **gpt-image-2** | 2.0K | OpenAI GPT image generation |
| **gpt-image-edit** | 2.0K | OpenAI GPT image editing |
| **nano-banana-2** | 2.0K | Nano Banana 2 image generation |
| **flux-2-klein** | 2.0K | Flux 2 Klein generation |
| **flux-kontext** | 2.0K | Flux Kontext contextual generation |
| **controlnet-pose** | 2.0K | Pose-guided generation |

### Audio, Music & Effects

| Skill | Installs | Purpose |
|---|---|---|
| **ai-music** | 2.0K | AI music generation |
| **elevenlabs-music-generation** | 2.0K | ElevenLabs music via RunComfy |
| **relight** | 2.0K | Professional scene relighting |
| **face-swap** | 2.0K | Face swapping with identity preservation |

Full list: 30 skills including seedance-v2, wan-2-7, happyhorse-1-0, kling-3-0, ace-step, codex-pet, runcomfy-cli.

---

## CorpusIQ Use Cases

- **Daily UGC Video Pipeline** — RunComfy as HeyGen alternative for avatar video; HyperFrames for composition
- **Social Media Content** — Generate 60-second product demos from script + image
- **Brand Assets** — Programmatic image generation for posts, headers, ads
- **Multi-Model Routing** — Intent-based model selection: "animate this" picks best model automatically

---

## Configuration

```bash
npm i -g @runcomfy/cli
runcomfy login
# or: export RUNCOMFY_TOKEN=<token>
npx skills add prime-skills/runcomfy-agent-skills
```

## Related Skills

- **HyperFrames** — Hermes-native video composition (complementary)
- **HeyGen Video Automation** — Avatar video (RunComfy is an alternative)
- **media-use** — Asset resolution layer for video projects
