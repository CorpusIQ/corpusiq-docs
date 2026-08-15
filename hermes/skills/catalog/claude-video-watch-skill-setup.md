---
title: Claude Video Watch Skill — Agent Video Input Setup
description: "bradautomates/claude-video — watch (10.1K installs): gives agents a video input via captions, frame extraction, and timestamped transcripts (native captions first, Whisper fallback). Snyk audit: Fail."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-video-watch-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "video", "transcription", "multimodal"]
---

# Claude Video Watch Skill — Setup Guide

**Source:** [bradautomates/claude-video](https://skills.sh/bradautomates/claude-video)
**GitHub:** [bradautomates/claude-video](https://github.com/bradautomates/claude-video) (15.4K stars)
**Skills:** 1 skill (`watch`) · 10.1K installs
**Category:** Video Understanding
**First Seen:** Apr 29, 2026 (catalogued August 15, 2026 midday sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub and Socket pass; Snyk Fail on the skill page — named in Limitations)

The watch skill gives an agent a video input. A bundled Python script fetches captions first, optionally downloads the video, extracts frames as JPEGs (scene-aware, or fast keyframes at efficient detail), builds a timestamped transcript (native captions first, Whisper API as fallback), and prints frame paths. The agent then reads frames and combines them with the transcript to answer questions about the video.

---

## Installation

```bash
npx skills add bradautomates/claude-video --skill watch
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3** | Runs the bundled watch.py script |
| **Node.js + npx** | For the skill installer |
| **ffmpeg** | For frame extraction (scene-aware mode) |
| **Whisper API key (optional)** | Fallback when native captions are absent |

## What It Provides

| Capability | Notes |
|---|---|
| Caption-first pipeline | Native captions used before any transcription |
| Frame extraction | Scene-aware or fast keyframe JPEG extraction at efficient detail |
| Timestamped transcript | Captions or Whisper API fallback |
| Harness-agnostic pathing | SKILL_DIR resolution works across Claude Code, Codex, Cursor, Gemini CLI |

## Quick Start

1. Install: `npx skills add bradautomates/claude-video --skill watch`
2. Resolve SKILL_DIR per the skill's layout table, then ask: "watch this video and summarize what happens at each timestamp"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Video intelligence** | Complements our video-transcript-analysis pipeline with frame-level grounding |
| **Creator research** | Extract timestamped insights from YouTube and TikTok content |
| **Multimodal answers** | Answer visual questions about recordings without a native video input |
| **Harness pattern** | The SKILL_DIR resolution pattern is reusable for multi-harness skills |

## Limitations / Verification

- Snyk audit Fail on the skill page — review the flagged dependency surface before production use
- Frame extraction requires ffmpeg; Whisper fallback requires an API key
- Publisher page verified: 10.1K installs, 15.4K GitHub stars

```bash
npx skills add bradautomates/claude-video   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
