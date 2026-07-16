---
title: "steipete/clawdis — 14 OpenClaw Skills"
description: "Complete setup guide for the clawdis skill collection: tmux, openai-whisper, ordercli, peekaboo, himalaya, clawhub, video-frames, session-logs, healthcheck, trello, model-usage, sonoscli, blogwatcher, spotify-player."
---

# Setup Guide: steipete/clawdis

**14 skills for Hermes/OpenClaw agents — terminal, media, monitoring, and productivity.**

## Quick Install

```bash
# Install individual skills
npx skills add steipete/clawdis/tmux
npx skills add steipete/clawdis/openai-whisper
npx skills add steipete/clawdis/ordercli
npx skills add steipete/clawdis/peekaboo
npx skills add steipete/clawdis/himalaya
npx skills add steipete/clawdis/clawhub
npx skills add steipete/clawdis/video-frames
npx skills add steipete/clawdis/session-logs
npx skills add steipete/clawdis/healthcheck
npx skills add steipete/clawdis/trello
npx skills add steipete/clawdis/model-usage
npx skills add steipete/clawdis/sonoscli
npx skills add steipete/clawdis/blogwatcher
npx skills add steipete/clawdis/spotify-player

# Or browse all: https://skills.sh/steipete/clawdis
```

## Prerequisites

- Hermes Agent or OpenClaw installed
- Node.js 18+ (for `npx skills`)
- Individual skill dependencies:
  - **tmux**: tmux installed (`sudo apt install tmux`)
  - **openai-whisper**: OpenAI API key
  - **himalaya**: himalaya CLI configured with email account
  - **trello**: Trello API key and token
  - **spotify-player**: spotifyd or librespot running
  - **sonoscli**: Sonos speakers on local network
  - **peekaboo**: `scrot` or `maim` for screenshots (Linux)

## Skills Overview

### Terminal & CLI (4 skills)

| Skill | Installs | Purpose |
|-------|:--------:|---------|
| **tmux** | 4,964 | Agent controls tmux sessions — create windows, split panes, send commands |
| **ordercli** | 3,388 | CLI-based ordering interface — agent can place orders programmatically |
| **peekaboo** | 3,112 | Screenshot capture — agent takes screenshots for visual context |
| **clawhub** | 2,859 | Central skill discovery hub — find and install ecosystem skills |

### Media & Audio (4 skills)

| Skill | Installs | Purpose |
|-------|:--------:|---------|
| **openai-whisper** | 3,781 | Speech-to-text transcription via OpenAI Whisper API |
| **video-frames** | 2,762 | Frame extraction and analysis from video files |
| **sonoscli** | 2,457 | Sonos speaker control — play, pause, volume, queue |
| **spotify-player** | 2,438 | Spotify playback — search, play, queue management |

### Monitoring & Logging (3 skills)

| Skill | Installs | Purpose |
|-------|:--------:|---------|
| **session-logs** | 2,616 | Agent session logging — searchable history across conversations |
| **healthcheck** | 2,594 | System health — CPU, memory, disk, process monitoring |
| **model-usage** | 2,458 | LLM token tracking and cost reporting across providers |

### Productivity (3 skills)

| Skill | Installs | Purpose |
|-------|:--------:|---------|
| **himalaya** | 2,907 | Terminal email — send, receive, manage emails |
| **trello** | 2,578 | Trello board management — create/move cards, add comments |
| **blogwatcher** | 2,451 | RSS/Atom feed monitoring — track blog updates |

## Configuration

Each skill uses standard Hermes skill configuration. After installing, configure in your agent's skill config:

```yaml
# Example: ~/.hermes/config.yaml skills section
skills:
  tmux:
    socket_path: "/tmp/tmux-default"
  openai-whisper:
    api_key: "${OPENAI_API_KEY}"
    model: "whisper-1"
  trello:
    api_key: "${TRELLO_API_KEY}"
    token: "${TRELLO_TOKEN}"
  spotify-player:
    device_name: "default"
```

## Use Cases

1. **Session-aware coding agent**: `tmux` + `session-logs` — agent works across tmux sessions with full context history
2. **Media production pipeline**: `video-frames` + `openai-whisper` — extract frames, transcribe audio, generate captions
3. **System operator agent**: `healthcheck` + `model-usage` — monitors system health and reports costs
4. **Content monitoring loop**: `blogwatcher` + `himalaya` — watches feeds, summarizes, emails digests

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `tmux` skill errors | tmux not installed | `sudo apt install tmux` |
| `openai-whisper` 401 | Missing API key | Set `OPENAI_API_KEY` env var |
| `himalaya` auth fails | himalaya not configured | Run `himalaya configure` first |
| `peekaboo` no output | No screenshot tool | Install `scrot` or `maim` |
| `sonoscli` can't find speakers | Network issue | Verify Sonos on same subnet |

## CorpusIQ Integration

These skills can be used to extend CorpusIQ agent capabilities:
- **session-logs** → feed into Honcho for persistent memory
- **model-usage** → complement CorpusIQ cost tracking
- **healthcheck** → integrate with system monitoring crons
- **blogwatcher** → feed competitive intelligence pipeline

---

*← [Marketplace](/hermes/skills/marketplace/) | [Clawdirect Setup →](/hermes/skills/catalog/clawdirect-setup/)*

*↑ [Skills Catalog](/hermes/skills/catalog/)*
