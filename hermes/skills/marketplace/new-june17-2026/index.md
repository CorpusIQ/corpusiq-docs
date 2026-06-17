---
title: New Hermes Skills — June 17, 2026
description: Late-discovery sweep of nousresearch/hermes-agent — 39 additional skills not catalogued in previous sweeps. Official Hermes Agent repo now at 100% coverage.
---

# New Skills — June 17, 2026

**Discovery sweep:** June 17, 2026 at 04:00 MST
**Source:** skills.sh REST API (`q=nousresearch/hermes-agent`, limit=96)
**Total new:** 39 skills from `nousresearch/hermes-agent`
**Previously catalogued from this repo:** 57 skills
**Now catalogued:** 96/96 — complete coverage of the official Hermes Agent skill repo

## Discovery Summary

Previous sweeps (June 13-15) catalogued 57 skills from the official `nousresearch/hermes-agent` repository but missed 39. This late-discovery sweep fills the gap, bringing coverage to 100%. The new skills span 8 categories.

## New Skills

### Creative & Experimental — 6 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `godmode` | 129 | Elevated agent capabilities — unrestricted tool access, power-user mode |
| `pixel-art` | 88 | Pixel art generation and editing |
| `stable-diffusion-image-generation` | 12 | Stable Diffusion image generation via agent |
| `audiocraft-audio-generation` | 13 | Meta Audiocraft — AI music and audio generation |
| `blender-mcp` | 14 | Blender 3D scene creation via MCP |
| `qmd` | 13 | Quantum molecular dynamics simulation |

### Development & Debugging — 5 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `node-inspect-debugger` | 135 | Node.js debugging via Chrome DevTools Protocol |
| `python-debugpy` | 132 | Python debugging — breakpoints, step-through, variable inspection |
| `debugging-hermes-tui-commands` | 76 | Debug Hermes TUI commands — trace, diagnose, fix shell issues |
| `simplify-code` | 29 | Code simplification and refactoring assistance |
| `kanban-codex-lane` | 72 | Codex-integrated Kanban lane for task tracking |

### Infrastructure & DevOps — 5 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `hermes-s6-container-supervision` | 76 | S6 supervision for Hermes containers — health checks, restarts, logging |
| `teams-meeting-pipeline` | 132 | Microsoft Teams meeting recording and transcription pipeline |
| `docker-management` | 13 | Docker container and image lifecycle management |
| `webhook-subscriptions` | 80 | Webhook subscription management and event handling |
| `openclaw-migration` | 12 | Migration path from OpenClaw to Hermes Agent |

### ML & AI Research — 9 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `dspy` | 15 | DSPy framework — declarative language model programming |
| `weights-and-biases` | 14 | W&B experiment tracking and model visualization |
| `llama-cpp` | 13 | llama.cpp — local LLM inference with quantization |
| `evaluating-llms-harness` | 13 | LM Evaluation Harness — standardized LLM benchmarking |
| `segment-anything-model` | 12 | Meta SAM — image segmentation |
| `clip` | 12 | OpenAI CLIP — zero-shot image classification |
| `whisper` | 12 | OpenAI Whisper — speech-to-text transcription |
| `guidance` | 12 | Guidance — constrained text generation with LLMs |
| `fastmcp` | 12 | FastMCP — rapid MCP server development framework |

### macOS Automation — 1 skill

| Skill | Installs | Description |
|-------|----------|-------------|
| `macos-computer-use` | 133 | macOS screen/mouse/keyboard automation, window management |

### Productivity & Planning — 5 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `ideation` | 105 | Structured brainstorming and idea development frameworks |
| `writing-plans` | 87 | Writing plan generation — outlines, drafts, revision plans |
| `subagent-driven-development` | 84 | Delegate subtasks to worker agents in structured workflows |
| `one-three-one-rule` | 13 | 1-3-1 rule: define problem, 3 solutions, 1 recommendation |
| `linear` | 80 | Linear.app integration — issues, projects, cycles |

### Entertainment & Lifestyle — 4 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `minecraft-modpack-server` | 82 | Minecraft modpack server setup and management |
| `pokemon-player` | 79 | Play Pokemon games via agent — emulator control, strategy |
| `spotify` | 75 | Spotify music control — play, search, playlists |
| `heartmula` | 135 | Heart rate formula calculations and health metrics |

### Utilities & Infrastructure — 4 skills

| Skill | Installs | Description |
|-------|----------|-------------|
| `openhue` | 134 | Philips Hue smart lighting control |
| `modal-serverless-gpu` | 12 | Modal serverless GPU — deploy functions to cloud GPUs |
| `chroma` | 12 | Chroma vector database — embeddings storage and retrieval |
| `1password` | 12 | 1Password secrets management and retrieval |
| `mcporter` | 12 | Minecraft server porting and configuration |
| `obliteratus` | 12 | Secure file/data obliteration and deletion |

## Skill Count Update

| Category | Skills |
|----------|--------|
| Creative & Experimental | 6 |
| Development & Debugging | 5 |
| Infrastructure & DevOps | 5 |
| ML & AI Research | 9 |
| macOS Automation | 1 |
| Productivity & Planning | 5 |
| Entertainment & Lifestyle | 4 |
| Utilities | 4 |
| **Total new** | **39** |

## Why This Matters for CorpusIQ

**Infrastructure:** `hermes-s6-container-supervision` enables production-grade agent container management — directly applicable to DGX Spark deployment.

**Development workflow:** `subagent-driven-development` provides structured multi-agent delegation patterns. `debugging-hermes-tui-commands` helps diagnose agent shell issues.

**Productivity:** `ideation`, `writing-plans`, and `one-three-one-rule` provide structured thinking frameworks for market research and strategic planning.

**macOS ecosystem:** `macos-computer-use` enables GUI automation on Mac Mini worker nodes.

**ML integration:** `dspy`, `whisper`, `clip`, and others enable advanced AI pipelines directly from Hermes agents.

---

*← [June 16, 2026](/hermes/skills/marketplace/new-june16-2026/) | [Skills Marketplace](/hermes/skills/marketplace/) →*
