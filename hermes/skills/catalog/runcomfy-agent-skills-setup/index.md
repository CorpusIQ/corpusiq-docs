---
title: "RunComfy Agent Skills - AI Video & Image Generation"
description: 30 production-grade media skills from prime-skills/runcomfy-agent-skills - AI video generation, avatar video, video editing, music generation. 11.5M+ combined installs via RunComfy cloud GPU platform (Oct 8, 2026 snapshot).
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/runcomfy-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# RunComfy Agent Skills - Setup Guide

**Source:** [prime-skills/runcomfy-agent-skills](https://skills.sh/prime-skills/runcomfy-agent-skills) (11.5M+ combined installs, Oct 8, 2026 snapshot)
**GitHub:** [prime-skills/runcomfy-agent-skills](https://github.com/prime-skills/runcomfy-agent-skills)
**Platform:** [RunComfy](https://www.runcomfy.com) - cloud GPU platform for AI media generation
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
| **video-edit** | 431.0K | Intent-routed video editing - restyle, motion transfer, outfit/background swap |
| **image-to-video** | 429.4K | Animate still images - HappyHorse I2V, Wan 2.7, Seedance 2.0 |
| **ai-video-generation** | 374.4K | Full text-to-video + image-to-video via single CLI |
| **ai-avatar-video** | 371.4K | Talking head / avatar video with lip-sync |
| **video-inpainting** | 369.5K | Remove objects/people from video |
| **video-outpainting** | 367.9K | Extend video frame boundaries |
| **video-extend** | 368.4K | Extend video duration - Veo-style, Kling, Seedance |
| **lipsync** | 368.9K | Audio-driven lip synchronization |

### Image Generation & Editing

| Skill | Installs | Purpose |
|---|---|---|
| **ai-image-generation** | 374.4K | Full RunComfy image-model catalog |
| **image-edit** | 428.7K | Intent-routed image editing |
| **gpt-image-2** | 75.8K | OpenAI GPT image generation |
| **gpt-image-edit** | 427.7K | OpenAI GPT image editing |
| **nano-banana-2** | 429.1K | Nano Banana 2 image generation |
| **flux-2-klein** | 427.5K | Flux 2 Klein generation |
| **flux-kontext** | 428.5K | Flux Kontext contextual generation |
| **controlnet-pose** | 369.0K | Pose-guided generation |

### Audio, Music & Effects

| Skill | Installs | Purpose |
|---|---|---|
| **ai-music** | 360.5K | AI music generation |
| **elevenlabs-music-generation** | 368.4K | ElevenLabs music via RunComfy |
| **relight** | 368.1K | Professional scene relighting |
| **face-swap** | 371.3K | Face swapping with identity preservation |

Full list: 30 skills including seedance-v2, wan-2-7, happyhorse-1-0, kling-3-0, ace-step, codex-pet, runcomfy-cli.

---

## CorpusIQ Use Cases

- **Daily UGC Video Pipeline** - RunComfy as HeyGen alternative for avatar video; HyperFrames for composition
- **Social Media Content** - Generate 60-second product demos from script + image
- **Brand Assets** - Programmatic image generation for posts, headers, ads
- **Multi-Model Routing** - Intent-based model selection: "animate this" picks best model automatically

---

## Configuration

```bash
npm i -g @runcomfy/cli
runcomfy login
# or: export RUNCOMFY_TOKEN=<token>
npx skills add prime-skills/runcomfy-agent-skills
```

## Mirror Listings (Oct 8, 2026 sweep)

This guide covers the `prime-skills/runcomfy-agent-skills` listing, which carries the install base. Related redistribution sources observed: `gencraft-labs/skills` republishes a partial RunComfy set (5 indexed listings, ~80K combined, first seen Oct 6, 2026; its README defers installs to `agentspace-so/runcomfy-agent-skills`). Treat other RunComfy skill sources as mirrors of this one.

## Related Skills

- **HyperFrames** - Hermes-native video composition (complementary)
- **HeyGen Video Automation** - Avatar video (RunComfy is an alternative)
- **media-use** - Asset resolution layer for video projects
