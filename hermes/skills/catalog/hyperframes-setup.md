---
title: HyperFrames  --  Full Setup Guide for Hermes Agents
description: Install, configure, and use the hyperframes skill from nousresearch/hermes-agent. Create HTML-based video compositions, animated title cards, social overlays, and audio-reactive visuals directly from Hermes.
---

# HyperFrames  --  Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/hyperframes) (13 installs on skills.sh¹)
**Category:** Media & Video
**Ecosystem:** [HyperFrames by HeyGen](https://skills.sh/heygen-com/hyperframes) (103K+ installs across 5 SDK skills)

Create HTML-based video compositions, animated title cards, social overlays, captioned talking-head videos, audio-reactive visuals, and shader transitions  --  all directly from Hermes Agent prompts. Wraps the HyperFrames SDK for agentic video generation.

*¹ The underlying HyperFrames ecosystem (heygen-com/hyperframes) has 103,094 installs for hyperframes, 99,994 for hyperframes-cli, and 96,452 for hyperframes-registry  --  making this one of the largest video creation ecosystems on skills.sh.*

---

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill hyperframes
```

The HyperFrames ecosystem dependencies (gsap, media, registry, CLI) are bundled and resolved automatically.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ (June 2026 release) |
| **HyperFrames SDK** | Bundled  --  no separate install needed |
| **Browser runtime** | Chromium-based browser for HTML canvas rendering (bundled or system) |
| **FFmpeg** | For video encoding/export (system install: `apt install ffmpeg` or `brew install ffmpeg`) |
| **Node.js** | 18+ for CLI operations |

Optional for advanced usage:
```bash
export HYPERFRAMES_OUTPUT_DIR="/home/hermes/output/videos"
export HYPERFRAMES_TEMPLATE_DIR="/home/hermes/.hermes/templates/hyperframes"
```

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Animated title cards | "Create an animated title card for [topic]" | Supports custom fonts, colors, timing |
| Social media overlays | "Generate a social overlay with [text] and [branding]" | Instagram/TikTok/YT aspect ratios |
| Captioned talking-head videos | "Add captions to this video with [style]" | Auto-syncs captions to audio |
| Audio-reactive visuals | "Create visuals that react to this audio track" | FFT-based frequency analysis |
| Shader transitions | "Apply a [type] shader transition between scenes" | GLSL shader support |
| HTML video compositions | "Compose a video from [elements] with [timing]" | Full HTML/CSS/JS canvas control |

### CLI Command Reference

```bash
# Render a HyperFrames composition
bash SKILL_DIR/scripts/render.sh --template title-card --text "Your Title" --output output.mp4

# List available templates
bash SKILL_DIR/scripts/templates.sh --list

# Preview a composition before rendering
bash SKILL_DIR/scripts/preview.sh --template social-overlay --text "Hello World"
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Daily UGC video series** | Generate 5 rotating video formats (tips, Q&A, case studies, tool demos, behind-the-scenes) automatically from agent-sourced content |
| **Social media video automation** | Create platform-optimized videos for Instagram Reels, TikTok, YouTube Shorts with correct aspect ratios and captions |
| **Product demo overlays** | Add animated title cards and feature callouts to screen recordings of CorpusIQ in action |
| **Growth content engine** | Programmatically generate video content from blog posts, changelogs, and customer success stories |
| **Multi-platform video repurposing** | Take one video source and generate variants optimized for each platform with different overlays and captions |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "FFmpeg not found" | `sudo apt install ffmpeg` (Linux) or `brew install ffmpeg` (macOS) |
| "Canvas rendering blank" | Ensure Chromium is installed: `npx playwright install chromium` |
| "Template not found" | Run `bash SKILL_DIR/scripts/templates.sh --sync` to pull latest templates |
| "Node.js version too old" | Upgrade to Node 18+: `nvm install 18 && nvm use 18` |
| "Output file permissions" | Set `HYPERFRAMES_OUTPUT_DIR` to a writable directory |

## Verification

```bash
# Verify skill installed
hermes skills list | grep hyperframes

# Quick functional test  --  list available templates
bash SKILL_DIR/scripts/templates.sh --list

# Render a test title card
bash SKILL_DIR/scripts/render.sh --template title-card --text "CorpusIQ Test" --output /tmp/test-hyperframes.mp4

# Check output
ls -la /tmp/test-hyperframes.mp4 && echo "✅ HyperFrames working"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june18-2026-update2/) →*
*Powered by CorpusIQ*
