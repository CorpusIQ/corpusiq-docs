---
title: "Claude Code Video Toolkit — Video Pipeline Skills Setup"
description: "digitalsamba/claude-code-video-toolkit — 13 skills, 14.5K installs: ffmpeg, Remotion, ElevenLabs, MoviePy, and Playwright recording for agent-driven video production."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-code-video-toolkit-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "video", "ffmpeg", "remotion"]
---

# Claude Code Video Toolkit — Setup Guide

**Source:** [digitalsamba/claude-code-video-toolkit](https://skills.sh/digitalsamba/claude-code-video-toolkit)
**GitHub:** [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit)
**Skills:** 13 skills · 14.5K total installs
**Category:** Video Production
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟡 Trusted (individual publisher, multi-skill suite; individual audit pages not fetched)

A complete agent video-production stack: ffmpeg encoding, Playwright screen recording, ElevenLabs voice, Remotion composition, MoviePy editing, LTX2 video generation, RunPod GPU orchestration, and more. Directly relevant to Hermes video pipelines — Remotion and ffmpeg are the same primitives our UGC video system is built on.

---

## Installation

```bash
npx skills add digitalsamba/claude-code-video-toolkit
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **ffmpeg** | For encoding skills |
| **Playwright** | For recording skills |
| **API keys** | ElevenLabs and RunPod for their respective skills |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| ffmpeg | 6.4K | Video encoding, cutting, and effects |
| playwright-recording | 923 | Record browser sessions to video |
| elevenlabs | 887 | Voice generation and narration |
| remotion | 862 | React-based video composition |
| qwen-edit | 723 | Qwen video editing |
| frontend-design | 694 | Design for video content |
| remotion-best-practices | 688 | Remotion production guidance |
| ltx2 | 649 | LTX2 video generation |
| moviepy | 639 | Python video editing |
| video_toolkit | 639 | General video operations |
| runpod | 637 | GPU orchestration for rendering |
| acestep | 589 | AceStep automation |
| ideogram4 | 232 | Ideogram image generation |

## Quick Start

1. Install: `npx skills add digitalsamba/claude-code-video-toolkit`
2. Start with `ffmpeg` and `remotion` — the highest-install pair
3. Ask: "record this browser session, add an ElevenLabs voiceover, and render a Remotion composition"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC video pipeline** | ffmpeg and remotion skills as reference patterns for our HyperFrames and Remotion stacks |
| **Voiceover production** | elevenlabs skill pairs with our existing TTS workflows |
| **Screen recordings** | playwright-recording for demo and tutorial content |
| **GPU rendering** | runpod skill for offloading renders from local hardware |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- Several skills (playwright-recording, elevenlabs, remotion) show under 1K installs — treat as newer, less-proven content
- Requires ffmpeg on PATH and paid API keys for ElevenLabs, RunPod, and generation services

```bash
npx skills add digitalsamba/claude-code-video-toolkit   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
