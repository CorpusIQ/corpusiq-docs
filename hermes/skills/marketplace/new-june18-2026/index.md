---
title: New Skills — June 18, 2026 (nousresearch/hermes-agent expansion)
description: 32 new Hermes Agent skills discovered June 18, 2026 from nousresearch/hermes-agent — macOS desktop automation, Node.js/Python debugging, smart home control, subagent workflows, music generation, and more.
---

# New Skills — June 18, 2026

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) via [skills.sh](https://skills.sh/nousresearch/hermes-agent)
**Date:** June 18, 2026
**Total new:** 32 skills (7 with 100+ installs, 25 additional)

## High-Value Skills (100+ installs)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 1 | `heartmula` | 136 | Suno-like song generation from lyrics + tags via HeartMuLa |
| 2 | `node-inspect-debugger` | 136 | Debug Node.js via --inspect + Chrome DevTools Protocol CLI |
| 3 | `openhue` | 135 | Control Philips Hue lights, scenes, rooms via OpenHue CLI |
| 4 | `macos-computer-use` | 134 | Drive macOS desktop: screenshots, mouse, keyboard, scroll, drag — without stealing focus |
| 5 | `teams-meeting-pipeline` | 133 | Operate Teams meeting summary pipeline: summarize, inspect, replay, manage Graph subscriptions |
| 6 | `python-debugpy` | 133 | Debug Python: pdb REPL + debugpy remote (DAP) |
| 7 | `godmode` | 130 | Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN |

## Additional Skills (13–89 installs)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 8 | `pixel-art` | 89 | Pixel art with era palettes (NES, Game Boy, PICO-8) |
| 9 | `writing-plans` | 87 | Write implementation plans: bite-sized tasks, paths, code |
| 10 | `subagent-driven-development` | 85 | Execute plans via delegate_task subagents (2-stage review) |
| 11 | `minecraft-modpack-server` | 83 | Host modded Minecraft servers (CurseForge, Modrinth) |
| 12 | `linear` | 80 | Linear: manage issues, projects, teams via GraphQL + curl |
| 13 | `webhook-subscriptions` | 80 | Webhook subscriptions: event-driven agent runs |
| 14 | `pokemon-player` | 80 | Play Pokemon via headless emulator + RAM reads |
| 15 | `spotify` | 75 | Spotify: play, search, queue, manage playlists and devices |
| 16 | `debugging-hermes-tui-commands` | 76 | Debug Hermes TUI slash commands: Python, gateway, Ink UI |
| 17 | `kanban-codex-lane` | 72 | Hermes Kanban worker → Codex CLI for isolated implementation lane |
| 18 | `blender-mcp` | 15 | Control Blender via socket: 3D objects, materials, animations, Python |
| 19 | `weights-and-biases` | 15 | Log ML experiments, sweeps, model registry, dashboards via W&B |
| 20 | `audiocraft-audio-generation` | 14 | AudioCraft: MusicGen text-to-music, AudioGen text-to-sound |
| 21 | `one-three-one-rule` | 14 | Structured decision-making for technical proposals and trade-offs |
| 22 | `qmd` | 14 | Search personal knowledge bases with hybrid retrieval (BM25 + vector + LLM) |
| 23 | `evaluating-llms-harness` | 14 | Benchmark LLMs (MMLU, GSM8K, etc.) via lm-eval-harness |
| 24 | `llama-cpp` | 14 | llama.cpp local GGUF inference + HuggingFace Hub model discovery |
| 25 | `obliteratus` | 13 | Abliterate LLM refusals via diff-in-means |
| 26 | `mcporter` | 13 | List, configure, auth, and call MCP servers/tools via mcporter CLI |
| 27 | `whisper` | 13 | OpenAI Whisper: speech recognition, 99 languages, transcription + translation |
| 28 | `modal-serverless-gpu` | 13 | Serverless GPU cloud for ML workloads: deploy models as APIs |
| 29 | `chroma` | 13 | Open-source embedding database: vector + full-text search, metadata filtering |
| 30 | `1password` | 13 | 1Password CLI (op): install, sign in, inject secrets into commands |
| 31 | `segment-anything-model` | 13 | SAM: zero-shot image segmentation via points, boxes, masks |
| 32 | `stable-diffusion-image-generation` | 13 | Text-to-image generation with Stable Diffusion via HuggingFace Diffusers |

## Detailed Skill Descriptions

### ⭐ development-workflow (combined): writing-plans + subagent-driven-development

These two skills form a complete development workflow for Hermes agents:

**writing-plans (87 installs):** Write implementation plans with bite-sized tasks, file paths, and code. Breaks complex features into executable steps with clear boundaries and dependencies.

**subagent-driven-development (85 installs):** Execute plans via `delegate_task` subagents with a 2-stage review process. Spawns isolated worker agents for each task, reconciles results, and handles retries.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill writing-plans
npx skills add nousresearch/hermes-agent --skill subagent-driven-development
```

**Use for:** Multi-file refactors, feature implementation, parallel task execution with review gates.

### godmode (130 installs) — LLM Jailbreaking

Jailbreak LLMs using Parseltongue, GODMODE, and ULTRAPLINIAN techniques. For red-teaming, safety testing, and understanding model boundaries.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill godmode
```

### macos-computer-use (134 installs) — Desktop Automation

Drive the macOS desktop in the background — screenshots, mouse, keyboard, scroll, drag — without stealing the user's cursor, keyboard focus, or Space. Works with any tool-capable model.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill macos-computer-use
```

**Prerequisites:** macOS, Accessibility permissions, `computer_use` tool available.

### linear (80 installs) — Project Management

Manage Linear issues, projects, and teams via GraphQL API + curl. Create/update issues, query project state, manage team workflows.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill linear
```

**Prerequisites:** Linear API key.

### webhook-subscriptions (80 installs) — Event-Driven Automation

Set up webhook subscriptions for event-driven agent runs. Trigger agents on external events — GitHub pushes, API calls, scheduled events.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill webhook-subscriptions
```

### teams-meeting-pipeline (133 installs) — Meeting Automation

Operate the Teams meeting summary pipeline via Hermes CLI. Summarize meetings, inspect pipeline status, replay jobs, manage Microsoft Graph subscriptions.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill teams-meeting-pipeline
```

**Prerequisites:** MSGRAPH_TENANT_ID, MSGRAPH_CLIENT_ID, MSGRAPH_CLIENT_SECRET.

### node-inspect-debugger (136 installs) — Node.js Debugging

Debug Node.js via `--inspect` + Chrome DevTools Protocol CLI. Set breakpoints, inspect variables, step through code programmatically.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill node-inspect-debugger
```

### python-debugpy (133 installs) — Python Debugging

Debug Python with pdb REPL + debugpy remote (DAP). Attach to running processes, set conditional breakpoints, inspect stack frames.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill python-debugpy
```

### openhue (135 installs) — Smart Home

Control Philips Hue lights, scenes, and rooms via OpenHue CLI. Agent-driven lighting automation — set scenes, adjust brightness, trigger room presets.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill openhue
```

**Prerequisites:** Philips Hue Bridge on local network, OpenHue CLI configured.

### heartmula (136 installs) — Music Generation

Suno-like song generation from lyrics + tags. Generate complete songs with vocals, instrumentation, and production.

**Install:**
```bash
npx skills add nousresearch/hermes-agent --skill heartmula
```

### Additional Skills Quick Reference

| Skill | Category | Use Case |
|-------|----------|----------|
| `spotify` | Media | Play, search, queue music; manage playlists + devices |
| `kanban-codex-lane` | DevOps | Isolated Codex CLI implementation lane for Kanban workers |
| `debugging-hermes-tui-commands` | Dev | Debug Hermes TUI slash commands |
| `pixel-art` | Creative | Generate pixel art with retro console palettes |
| `blender-mcp` | Creative | Control Blender for 3D modeling + animation |
| `weights-and-biases` | MLOps | Track ML experiments and model registry |
| `audiocraft-audio-generation` | Media | MusicGen + AudioGen for AI music/sound |
| `one-three-one-rule` | Dev | Structured decision-making framework |
| `qmd` | Research | Hybrid retrieval for personal knowledge bases |
| `evaluating-llms-harness` | MLOps | Benchmark LLMs with standard evaluation suites |
| `llama-cpp` | MLOps | Local GGUF inference + HF Hub model discovery |
| `obliteratus` | MLOps | Abliterate LLM refusals |
| `mcporter` | Dev | MCP server management CLI |
| `whisper` | Media | Speech recognition (99 languages) |
| `modal-serverless-gpu` | MLOps | Serverless GPU for ML workloads |
| `chroma` | MLOps | Embedding database for vector search |
| `1password` | Dev | CLI secret management |
| `segment-anything-model` | MLOps | Zero-shot image segmentation |
| `stable-diffusion-image-generation` | Media | Text-to-image generation |
| `minecraft-modpack-server` | Gaming | Host modded Minecraft servers |
| `pokemon-player` | Gaming | Headless Pokemon emulator |


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
