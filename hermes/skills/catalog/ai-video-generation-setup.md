---
title: ai-video-generation — AI Video Production for Hermes (196K installs)
description: Install and use 101-skills/skills@ai-video-generation (196K installs) for end-to-end AI video production. Script-to-video pipeline, AI avatars, voiceover synthesis, and multi-format export.
---

# ai-video-generation — Setup Guide

**Source:** [101-skills/skills](https://github.com/101-skills/skills) (196,300 installs)
**Category:** AI Media / Video Production
**Languages:** TypeScript, Python

Production-grade AI video generation skill for coding agents. Complete script-to-video pipeline: generate scripts, compose scenes, integrate AI avatars with lip-sync, synthesize voiceovers, and export in multiple formats. Companion skill `ai-avatar-video` (195.8K installs) adds synthetic presenter capabilities. At 196K installs, this is the most-installed AI video skill in the ecosystem.

---

## Installation

```bash
# Core video generation
npx skills add 101-skills/skills@ai-video-generation

# AI avatar presenters (optional, recommended)
npx skills add 101-skills/skills@ai-avatar-video
```

Verify:
```bash
npx skills list | grep "101-skills"
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **FFmpeg** | 5.0+ (`sudo apt install ffmpeg` or `brew install ffmpeg`) |
| **Hermes Agent** | Any version |
| **GPU (optional)** | Accelerates rendering; CPU fallback available |
| **HeyGen API key** | Required for AI avatar integration (`ai-avatar-video`) |
| **ElevenLabs API key** | Optional for premium voiceover quality |

---

## Key Capabilities

### Script-to-Video Pipeline

```
┌──────────────┐     ┌───────────────┐     ┌──────────────┐     ┌─────────────┐
│  Text/Outline │ ──▶ │  Scene Comp   │ ──▶ │  AV Render   │ ──▶ │  Export     │
│  → Full Script│     │  → Visual Plan│     │  → MP4/WebM  │     │  → Social   │
└──────────────┘     └───────────────┘     └──────────────┘     └─────────────┘
```

### Core Commands

| Command | Purpose | Example |
|---|---|---|
| `ai-video generate` | Generate video from text | `ai-video generate --script "product-demo.md" --style "corporate"` |
| `ai-video script` | Generate script only | `ai-video script --topic "How CorpusIQ saves 10hrs/week" --duration 60s` |
| `ai-video scene` | Design scene composition | `ai-video scene --script "demo.md" --scenes 5 --transitions "fade"` |
| `ai-video avatar` | Add AI presenter | `ai-video avatar --script "demo.md" --avatar "professional-female" --voice "sarah"` |
| `ai-video export` | Export final video | `ai-video export --format "mp4" --resolution "1080p" --platform "youtube"` |

### AI Avatars (`ai-avatar-video`)

```bash
# Generate a product demo with AI presenter
ai-video avatar \
  --script "corpusiq-overview.md" \
  --avatar "business-casual-male" \
  --voice "adam" \
  --background "modern-office" \
  --gestures "natural" \
  --output "corpusiq-demo.mp4"
```

**Available avatar styles:** professional, casual, creative, technical
**Voice options:** 20+ voices across male/female, accents (US, UK, AU, IN)
**Background options:** office, studio, gradient, transparent, custom-image

### Scene Composition

```yaml
# scene-plan.yaml
scenes:
  - duration: 10s
    type: intro
    content: "Logo animation + hook text"
    transition: fade-in
  - duration: 30s
    type: presenter
    content: "Problem statement — AI avatar on screen"
    avatar: business-casual-male
  - duration: 40s
    type: screen-recording
    content: "CorpusIQ dashboard walkthrough"
    overlay: presenter-pip
  - duration: 15s
    type: cta
    content: "Visit corpusiq.io — free trial"
    transition: zoom-out
```

### Multi-Format Export

| Format | Resolution | Best For |
|---|---|---|
| MP4 (H.264) | 1080p / 4K | YouTube, website, download |
| MP4 (Vertical) | 1080x1920 | TikTok, Reels, Shorts |
| WebM | 1080p | Web embedding |
| GIF | 480p | Twitter, Reddit, email |
| Social-optimized | Platform-specific | Auto-detects from `--platform` flag |

---

## Common Workflows for CorpusIQ

### Daily UGC Video (60s Product Tip)

```bash
# Generate script → avatar video → social export
ai-video script \
  --topic "How to find cash flow leaks with CorpusIQ" \
  --tone "technical,helpful" \
  --duration 60 \
  --output "daily-tip-script.md"

ai-video avatar \
  --script "daily-tip-script.md" \
  --avatar "technical-expert" \
  --voice "marcus" \
  --output "daily-tip-$(date +%Y%m%d).mp4"

ai-video export \
  --input "daily-tip-$(date +%Y%m%d).mp4" \
  --platforms "tiktok,reels,youtube-shorts"
```

### Product Launch Video (Multi-Scene)

```bash
# Generate complete launch video with presenter + screen recording
ai-video generate \
  --script "launch/corpusiq-v2-announcement.md" \
  --style "product-launch" \
  --avatar "professional-female" \
  --screenshots "launch/screenshots/" \
  --music "upbeat-corporate" \
  --duration 120 \
  --output "corpusiq-v2-launch.mp4"
```

### Blog-to-Video Repurposing

```bash
# Convert blog post to short-form video
ai-video generate \
  --source "https://corpusiq.io/blog/ai-for-operators" \
  --format "blog-to-video" \
  --duration 90 \
  --platforms "youtube,linkedin" \
  --output "ai-for-operators-video.mp4"
```

---

## Integration with CorpusIQ Video Stack

| Tool | Role | When to Use |
|---|---|---|
| **ai-video-generation** (this) | Script-to-video pipeline | Full AI video production |
| **HyperFrames** (108K) | Template-based video | Product demos, website-to-video |
| **Remotion** (430K) | Programmatic video (React) | Custom animations, data-driven video |
| **HeyGen API** | Avatar rendering | Underlying engine for ai-avatar-video |
| **ElevenLabs** | Premium voiceover | When default TTS quality insufficient |

**Recommendation:** Use `ai-video-generation` for daily content (fast, automated). Use `HyperFrames` for product launch videos (template-driven, polished). Use `Remotion` for data-driven videos (custom logic, charts).

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `ai-video: command not found` | Skill not installed | `npx skills add 101-skills/skills@ai-video-generation` |
| Avatar lip-sync misaligned | Audio/video timing drift | Add `--sync-mode "precise"` (slower but accurate) |
| Rendering slow (5+ min/video) | CPU rendering | Enable GPU acceleration or reduce resolution to 720p |
| Voice sounds robotic | Default TTS engine | Install ElevenLabs and pass `--voice-provider "elevenlabs"` |
| Export fails on TikTok format | Missing vertical template | Use `--platform "tiktok"` for auto-cropping |
| FFmpeg errors | Missing or outdated FFmpeg | `sudo apt update && sudo apt install ffmpeg` |

---

## See Also

- [remotion-best-practices](/hermes/skills/catalog/remotion-best-practices-setup/) — Programmatic video with React (430K installs)
- [hyperframes](/hermes/skills/catalog/) — Template-based AI video generation (108K installs)
- [corpusiq-ugc-video-strategy](/hermes/skills/catalog/) — CorpusIQ's UGC video content strategy
- [video-transcription-analysis](/hermes/skills/catalog/) — Extract insights from competitor videos
