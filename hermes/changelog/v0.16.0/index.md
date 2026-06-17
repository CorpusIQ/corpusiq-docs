---
title: Hermes Agent v0.16.0 — The Surface Release
description: Desktop app, remote gateway, web admin panel, fuzzy model picker, /undo, Simplified Chinese translation, leaner skills, NVIDIA/skills tap. June 5, 2026.
---

# Hermes Agent v0.16.0 (v2026.6.5) — The Surface Release

**Release Date:** June 5, 2026
**Since v0.15.2:** 874 commits · 542 merged PRs · 1,962 files changed · 205,216 insertions · 46,217 deletions · 399 issues closed (2 P0, 62 P1, 16 security-tagged) · 170 community contributors

> **The Surface Release.** Hermes meets you wherever you work — desktop app, web admin, fuzzy model picker everywhere, `/undo`, and a leaner default install.

---

## ✨ Highlights

### 🖥️ Hermes Desktop App (NEW)
A real native Electron app for macOS, Linux, and Windows — not a terminal wrapper. One-click install, in-app self-update. Features:
- Proper chat window with streaming
- Drag-and-drop files + clipboard image paste
- Session list with archive/search
- Cmd+K command palette
- Inline model picker in status bar
- **Remote gateway support** — point at a remote Hermes over OAuth or username/password
- Concurrent multi-profile sessions with cross-profile `@session` links
- **Simplified Chinese (简体中文)** — full translation across every UI surface, switchable in Appearance settings

### 🌐 Web Dashboard → Full Admin Panel
The dashboard is now a complete browser-based administration surface:
- **Channels page** — configure Telegram, Discord, Slack from the browser
- **MCP catalog** with enable/disable toggles
- **Credential management**, webhooks, memory config
- **Gateway controls** and System page with check-before-update + Debug Share
- Pluggable OIDC / username-password login

### 🧠 Agent Improvements
- **`/undo [N]`** — take back the last N turns (CLI, TUI, and all messaging platforms)
- **Fuzzy model picker** everywhere — desktop, web, TUI, CLI
- **Quick Setup via Nous Portal** — from install to first message in seconds
- **Configurable default interface** — `cli` or `tui`
- New models: `deepseek-v4-flash`, `MiniMax-M3` (1M context), `qwen3.7-plus`

### 📦 Skills & Ecosystem
- **Leaner default skill set** — redundant/niche skills moved to optional, `environments:` relevance gates
- **NVIDIA/skills** joins OpenAI, Anthropic, HuggingFace as trusted Skills Hub tap
- Curator can now prune unused built-in skills with usage tracking
- Blank-slate installs: `hermes install --no-skills`

### 🛡️ Security & Reliability
- **CVE-2026-48710** (Starlette BadHost) — patched Starlette ≥1.0.1
- SSRF checks off the event loop in async paths
- Subprocess credential stripping
- 399 issues closed (2 P0, 62 P1, 16 security-tagged)

---

## 🖥️ Desktop App Details

### Install & Lifecycle
- macOS desktop install + in-app self-update
- Build desktop in dedicated `desktop` stage with content-hash stamps
- Boot-failure recovery + live API-key validation
- Windows: recover from corrupt Electron cache
- Linux: arm64 binary detection, Electron sandbox config

### Remote Gateway & Multi-Profile
- Connect to OAuth-gated remote gateways
- Username/password login for remote gateways
- Per-profile remote gateway hosts
- Concurrent multi-profile sessions
- Cross-profile `@session` links

### Chat UX
- Drop files anywhere in the chat area
- Clipboard image paste with dedupe
- Background needs-input indicator
- Cmd+K command palette
- Inline model picker + YOLO toggle in status bar
- Full Simplified Chinese translation (typed i18n layer)

---

## 🌐 Web Dashboard

### Administration Panel
- MCP catalog with enable/disable toggles, pairing, webhooks
- Channels page for all messaging platforms
- Credential management, memory, gateway controls
- System page: check-before-update + Debug Share
- Bulk sessions, schedule picker

### Auth
- Pluggable username/password login (Option B)
- Generic self-hosted OIDC provider
- Dashboard session rotation via refresh token
- `hermes dashboard register` for self-hosted OAuth client

---

## 🏗️ Core Agent

### Model Support
- `deepseek-v4-flash` (+ trimmed variants)
- `MiniMax-M3` with 1M context
- `qwen3.7-plus` (Nous + OpenRouter)
- `gemini-3.5-flash` (Gemini OAuth + API-key pickers)

### Agent Loop
- `/undo [N]` — full parity across CLI, TUI, messaging platforms
- Progressive tool disclosure for MCP and plugin tools
- Universal task-completion guidance
- Uncap delegation `max_spawn_depth`
- `perf(read_file)`: compact line-number gutter (~14% fewer tokens)

### Sessions & Memory
- `perf(state)`: merge FTS5 segments on VACUUM
- Honcho: fail-open on startup
- Supermemory: session-level ingest + kebab aliases
- Session DB optimization via `hermes sessions optimize`

---

## 🧩 Multi-Agent & Skills

### Kanban
- `goal_mode` cards run workers in a `/goal` loop
- File attachments on tasks
- Attach images to worker vision
- Per-profile concurrency cap

### Skills
- Removed: `spotify`, `linear`, `kanban-codex-lane`, `debugging-hermes-tui-commands`, empty category markers
- Bundled → optional: Baoyu creative set, `dspy`, `subagent-driven-development`, `minecraft-modpack-server`, `pokemon-player`, `hermes-s6-container-supervision`
- `environments:` relevance gate keeps context-specific skills out of the index
- NVIDIA/skills trusted tap with `skills.sh.json` sidecar
- Blank-slate installs + curator prune for built-in skills

---

## 📱 Messaging Platforms

- Structured stream-event protocol + Telegram draft formatting parity
- Per-platform streaming defaults (Telegram on, Discord off)
- Discord voice-channel mixer — ambient idle bed + verbal acks
- Handle Feishu meeting invitations
- Matrix bang-command aliases + fail-closed approval reaction auth

---

## 🔧 CLI, TUI & Setup

- Configurable default interface (cli vs tui) + `--cli` flag
- TUI single `/model` command + unified Sessions overlay
- Quick Setup via Nous Portal + Full Setup defaults
- Process title set to `hermes` in ps/top/htop
- TUI perf: stop slow/dead MCP servers from freezing startup
- Auto-recover session on unexpected gateway death

---

## 🐳 Docker & Deployment

- Container reuse + bounded-sync cleanup + orphan reaper
- Auto-join Docker socket group for docker-in-docker backend
- Tag containers with hermes-agent labels for identification
- Point TUI launcher at prebuilt bundle via `HERMES_TUI_DIR`

---

## 🔒 Security

- CVE-2026-48710 (Starlette BadHost) — pin patched Starlette ≥1.0.1
- Run URL SSRF checks off the event loop in async paths
- Strip Bedrock inference bearer token from subprocess env
- Add `bws_cache.json` to file-safety read guard
- Restore approval/sudo context in `execute_code`
- Add docker restart/stop/kill to `DANGEROUS_PATTERNS`
- Sanitize invisible unicode in vetted skill content

---

## 📚 Documentation

- New Desktop App guide + remote-backend sections
- Dashboard auth-provider suitability + registration docs
- Network egress isolation guide for Docker

---

## 👥 Contributors

**170 community contributors** (including co-authors). Top contributors:
- **@OutThisLife** (52 PRs) — desktop app end-to-end
- **@benbarclay** (44 PRs) — Docker hardening, dashboard auth
- **@kshitijk4poor** (29 PRs) — fuzzy model picker, setup onboarding
- **@ethernet8023** (18 PRs) — desktop build pipeline, managed-uv
- **@austinpickett** (8 PRs) — dashboard theme, desktop Providers
- **@alt-glitch** (7 PRs) — Nous tool-pool, FAL video-gen, supermemory
- **@helix4u** (6 PRs) — gateway service-restart, update guard
- **@jquesnelle** (4 PRs) — installer, desktop tooling
- **@JimLiu** — Simplified Chinese translation + i18n layer

---

**Full Changelog:** [v2026.5.29.2...v2026.6.5](https://github.com/NousResearch/hermes-agent/compare/v2026.5.29.2...v2026.6.5)

*← [Changelog Index](/hermes/changelog/) | [Home](/hermes/) →*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
