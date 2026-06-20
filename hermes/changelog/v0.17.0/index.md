---
title: Hermes Agent v0.17.0 — The Reach Release
description: iMessage via Photon, Raft agent network, background subagents, image editing, Automation Blueprints, desktop app overhaul, Skills Hub rehaul, WhatsApp Cloud API, Telegram rich text. June 19, 2026.
---

# Hermes Agent v0.17.0 (v2026.6.19) — The Reach Release

**Release Date:** June 19, 2026
**Since v0.16.0:** ~1,475 commits · ~800 merged PRs · 1,693 files changed · 235,390 insertions · 50,730 deletions · 300+ issues closed · 245 community contributors

> **The Reach Release.** v0.16.0 put Hermes on your desktop. v0.17.0 is about how far that reach extends — across new places to talk to it, deeper into the tools you already use, and smarter about how work gets done.

---

## ✨ Highlights

### 📱 iMessage Support via Photon (NEW)
No Mac relay required. Talk to Hermes through iMessage using Nous-managed Photon infrastructure.
- `hermes photon login` — one-command setup
- Blue-bubble delivery with full message fidelity
- No Apple hardware dependency

### 🌊 Raft Agent Network Gateway (NEW)
Connect Hermes to Raft via wake-channel bridge — a privacy-preserving agent-to-agent network.
- Cross-agent dispatch and coordination
- Privacy-preserving connection model
- Opt-in bridge architecture

### 🖥️ Desktop App Overhaul
Massive UX upgrade across the Electron desktop app:
- **Rebindable keyboard shortcuts** panel — customize every action
- **Native OS notifications** — system-level alerts when Hermes needs you
- **Live subagent watch-windows** — see what your subagents are doing in real time
- **Composer model selector** with per-model presets
- **VS Code theme support** — install any Marketplace theme
- Automatic RTL/bidi text direction
- Resizable VS Code-themed terminal pane
- Per-thread composer drafts

### 🤖 Background & Async Subagents
`delegate_task(background=true)` returns immediately — subagent runs in background, results come back when ready. No more blocking on long chains.

### 🖼️ Image Editing
The `image_generate` tool now supports editing and transforming existing images. Route edits to the appropriate endpoint automatically.

### 📋 Automation Blueprints (NEW)
Schedule recurring tasks via natural-language forms — no cron syntax required. "Every morning at 8 AM, check my calendar and summarize" just works.

### 🧠 Model & Provider Expansion
- **Cursor Composer model via xAI Grok** — `grok-composer-2.5-fast` with full 200k context via OAuth
- Full profile builder in dashboard — configure models, skills, MCP servers without touching `config.yaml`

### 🛒 Skills Hub Rehaul
- Featured skills with curated discovery
- Integrated security scans on every skill
- Real browser-based browsing experience
- Quality scoring and community ratings

### 🧩 Memory Tool Upgrade
Atomic batch operations (`add`/`replace`/`remove`) against a character budget. Smarter memory compaction with no loss of critical context.

### 🔐 Security & Dashboard
- **Hardened dashboard login** — proper 401 handling, `public_url` warning
- Promptware defense: Brainworm-class attack patterns blocked; memory scanned at load; tool outputs delimited
- `session_search` rebuilt: **4,500× faster**, zero LLM cost

### 📱 Messaging Platforms
- **Official WhatsApp Business Cloud API adapter** — native Meta-hosted channel
- **Rich text for Telegram** — Bot API 10.1 with native markup (on by default)

### 💰 Cost Optimization
- **Curator cost optimization** — LLM consolidation pass now off by default; deterministic pruning is free
- Token-aware tool dispatch reducing per-turn overhead

---

## 🖥️ Desktop App Details

### UX & Productivity
- Rebindable keyboard shortcuts panel — full customization
- Live subagent watch-windows with streaming output
- Composer model selector — switch models mid-conversation
- Per-model presets for quick switching
- Automatic RTL/bidi text direction detection
- Resizable VS Code-themed terminal pane
- Per-thread composer drafts (never lose an in-progress message)
- Install any VS Code Marketplace theme

### Notifications & Awareness
- Native OS notification integration
- Background needs-input indicators
- Subagent completion alerts

---

## 🌐 Network & Connectivity

### iMessage (Photon)
- `hermes photon login` for setup
- Managed infrastructure — no Mac required
- Full message fidelity on blue bubbles

### Raft Agent Network
- Wake-channel bridge for agent-to-agent communication
- Privacy-preserving connection model
- Cross-agent task delegation

### WhatsApp Business
- Official Meta Cloud API adapter
- Native business messaging support
- Template management and approval flows

---

## 🏗️ Core Agent

### Subagents
- `delegate_task(background=true)` — async, non-blocking
- Subagent results delivered when ready
- Live watch-windows in desktop app

### Tools
- `image_generate` now supports image editing/transformation
- `session_search` 4,500× faster, deterministic (no LLM cost)
- Memory tool: atomic batch operations with character budget

### Automation Blueprints
- Natural-language scheduling — no cron syntax
- Recurring task definitions with plain English
- One-off and repeating patterns supported

---

## 📦 Skills & Ecosystem

### Skills Hub 2.0
- Featured skills with curated discovery
- Per-skill security scanning
- Browser-based exploration experience
- Community ratings and quality scores

### Profile Builder
- Full model configuration from dashboard
- MCP server management without editing config.yaml
- Skill enable/disable from web interface

---

## 📱 Messaging Platforms

| Platform | New in v0.17.0 |
|----------|----------------|
| **iMessage** | Full support via Photon — no Mac required |
| **WhatsApp** | Official Business Cloud API adapter |
| **Telegram** | Rich text via Bot API 10.1 (native markup, on by default) |

---

## 🔒 Security

- **Promptware defense** — Brainworm-class attack patterns blocked; memory scanned at load time; tool outputs delimited
- Dashboard auth hardened — proper 401 handling, `public_url` exposure warning
- `session_search` rebuilt as deterministic tool (no LLM → no prompt-injection surface)
- Per-skill security scanning in Skills Hub

---

## ⚡ Performance

| Improvement | Impact |
|-------------|--------|
| `session_search` rebuild | 4,500× faster, zero LLM cost |
| Curator deterministic pruning | Free consolidation, no LLM calls |
| Token-aware tool dispatch | Reduced per-turn overhead |
| Background subagents | Non-blocking multi-agent workflows |

---

## 👥 Contributors

**245 community contributors** — the largest contributor cohort in Hermes Agent history.

---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
