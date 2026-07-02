---
title: Hermes Agent v0.18.0 — The Judgment Release
description: P0/P1 clean sweep (692 items, 100% closed). Mixture-of-Agents as first-class model, verification & completion contracts, /learn distillation, /journey timeline, background fan-out, desktop coding Projects, scale-to-zero gateway, Google Vertex AI, security hardening. July 1, 2026.
---

# Hermes Agent v0.18.0 (v2026.7.1) — The Judgment Release

**Release Date:** July 1, 2026
**Since v0.17.0:** ~1,720 commits · 998 merged PRs · 2,215 files changed · ~251,000 insertions · ~41,000 deletions · 949 issues closed · 381 community contributors

> **The Judgment Release.** Over the last week and a half the team put nearly all of its effort into one goal: resolve **every P0 and P1 issue and PR in the entire Hermes Agent repo** — and as of this release, **100% of them are closed.** Zero open P0s. Zero open P1s. On top of that clean-sweep, v0.18.0 is about how *well* Hermes thinks and how it *knows when its work is actually done*.

---

## 🎯 The P0/P1 Clean Sweep — 100% Resolved

This is the release headline. Every single P0 and P1 across the whole repo is now closed:

| Priority | Issues Closed | PRs Merged |
|---|---|---|
| **P0** (critical) | 3 | 8 |
| **P1** (high) | 493 | 188 |
| **Total** | **496** | **196** |

**~692 highest-priority items resolved** in twelve days. The team intends to keep P0/P1 at zero from here forward.

---

## ✨ Highlights

### 🧠 Mixture-of-Agents — First-Class Model
MoA graduated from a mode to a first-class model provider. Every named MoA preset appears as a selectable model under a `moa` provider alongside Claude, GPT, and Grok in every model picker (CLI, TUI, desktop, gateway). Pick "my-council" the same way you'd pick any model.

- **See every model's reasoning** — each reference model's full output renders as its own labelled block
- **Aggregator streams live** — watch the answer form in real time instead of waiting for the whole response
- **Reference models see full tool state** and fire on every user/tool response
- **Opt-in full-turn trace persistence** to JSONL for debugging and eval

### ✅ Verification & Goals — The Agent Proves Its Work
Hermes now records verification evidence and can decide it's finished by actually running your project's checks, not by claiming success.

- **Completion contracts for `/goal`** — state what "done" looks like; the loop judges completion against evidence, not the model's say-so
- **Coding verification evidence ledger** — profile-scoped record of canonical project checks
- **`pre_verify` hook** for wiring in custom verification
- **`/goal wait <pid>`** — park the standing-goal loop on a background process

### 🎓 Self-Improvement: `/learn` & `/journey`

- **`/learn <anything>`** — distill a reusable skill from a directory, URL, or workflow you just walked through. Honors CONTRIBUTING.md skill standards automatically.
- **`/journey`** — CLI + TUI learning timeline of accumulated memories and skills, with in-place edit/delete
- **Memory graph** in desktop — playable radial timeline of memories + skills over time
- **Cheaper background review** — aux-model routing + context digest + adaptive cadence for the post-turn self-improvement fork

### 🖥️ Desktop Coding Cockpit
The desktop app gained real, per-profile **Projects** — a sidebar of your codebases, a coding rail, a review pane, git worktree management, and agent-facing project tools.

- **First-class Projects** with `project → repo → lane` model
- **Multi-terminal panel** with read-only agent terminals; persist & restore across relaunch
- **PR-style file diffs** in chat; in-app spot editor for file previews
- **Conversation timeline rail** for long threads
- **Composer refactor wave** — god-file de-entanglement into isolated engine hooks
- **Pets** — roaming pet (opt-in), pop-out overlay, notifications

### 🤖 Background Subagent Fan-Out
`delegate_task` can now fan out multiple subagents that all run in the **background**: your chat is never blocked, and when every subagent finishes, their results come back as a single consolidated turn. Kick off "research these five competitors in parallel" and carry on with something else.

### 🌐 Scale-to-Zero Gateway
The gateway can go **dormant when idle** and quiesce cleanly before a restart, migration, or auto-update — without dropping in-flight conversations. External drain coordination ensures nobody gets cut off mid-turn. Running Hermes at scale for a team is now production-grade.

### 🔌 Google Vertex AI Provider
Vertex AI is now a first-class provider for Gemini over the OpenAI-compatible endpoint. Hermes auto-mints and refreshes short-lived OAuth2 tokens from a service-account JSON or Application Default Credentials — no static key, no mid-session expiry.

### ✍️ `/prompt` — Compose in Your Editor
`/prompt` opens your `$EDITOR` so you can hand-write a long, multi-line prompt in real markdown instead of fighting a one-line input box.

### 🔒 Security Hardening
- MCP-config persistence attack surface locked down
- Cron `base_url` overrides that could exfiltrate provider credentials blocked
- Non-reusable sentinel for prefix secrets in file reads
- Slack `xapp-` token redaction
- Browser cloud-metadata floor enforced on every backend
- `aiohttp` CVE floor across lazy messaging paths

---

## 🖥️ Desktop App Details

### Coding Cockpit
| Feature | Description |
|---------|-------------|
| Projects sidebar | Per-profile codebases with `project → repo → lane` model |
| Multi-terminal panel | Read-only agent terminals, persist & restore across relaunch |
| PR-style diffs | File diffs rendered in chat with inline annotations |
| Spot editor | Edit files directly in the preview pane |
| Git cockpit | Status, review, worktrees from the desktop |
| Conversation timeline | Navigate long threads with a visual rail |

### UX & Surfaces
| Feature | Description |
|---------|-------------|
| Read aloud (TTS) | Auto-TTS toggle on the composer |
| Window state persistence | Size, position, maximized remembered across launches |
| Context-usage popover | See where your context budget is going |
| Shared overlay Panel | Reused across cron, profiles, agents |
| Floating composer | Pop the input into a draggable window |
| Backup management | Import/create/download from web UI |

---

## 🧠 Core Agent & Architecture

### Delegation & Subagents
- **Background fan-out** — parallel subagents run in background, one consolidated return when all finish
- Background subagent tracking in CLI + TUI status bar

### Agent Loop & Tools
- One-shot LLM helper + `llm.oneshot` gateway RPC
- Coding-context project facts exposed via `project.facts` RPC
- `web_extract` truncate-and-store instead of LLM summarization
- Friendly human-phrased tool labels for built-in tools
- `/reasoning full` — uncapped thinking
- `/timestamps` + timestamps in `/history`
- Multiple `HERMES_WRITE_SAFE_ROOT` directories

### Compression & Sessions
- In-place compaction option (single session ID)
- Backup includes `projects.db` and kanban boards in pre-update snapshot

---

## 🌐 Gateway, Fleet & Relay

### Scale-to-Zero & Drain
- Idle detection + dormant-quiesce (Phase 0)
- External drain coordination (Phase 2) — safe-shutdown without dropping conversations
- Persist in-flight transcript on restart/shutdown drain timeout
- Self-heal gateway stranded in draining/degraded state

### Relay (Phase 5/6)
- Wake primitive (gateway side)
- Going-idle / buffered-flip primitive
- Multi-platform-per-agent identity
- Authorize relay-delivered events by delivery, not source platform

### Gateway Core
- Typed send-error classification (`SendResult.error_kind`)
- Per-platform `typing_indicator` toggle
- Per-category context breakdown in `/usage`
- Configurable concurrent-run cap to prevent DoS

---

## 📱 Messaging Platforms

| Platform | New in v0.18.0 |
|----------|----------------|
| **Telegram** | Configurable command menu, rich draft preview gating, drain send pool |
| **Slack** | Opt-in Block Kit rendering, `--no-assistant` manifest flag |
| **Discord** | Reasoning rendered as `-#` subtext via `display.reasoning_style` |
| **WhatsApp** | Native media delivery via Baileys bridge |
| **Signal** | AAC voice-note remux, shared markdown formatting |
| **Teams** | Native `send_video`/`send_voice`/`send_document` |
| **All** | Cron continuations — thread-preferred with DM-mirror fallback |

---

## 🔧 Tool System, Skills & MCP

- **Blank Slate setup mode** — minimal agent, opt in to everything
- MCP config persistence attack surface hardened; `base_url` exfil blocked
- Kanban: task lifecycle plugin hooks (claimed/completed/blocked); typed block reasons
- LSP: PowerShellEditorServices language server
- mem0: v3 API + OSS mode + update/delete tools
- `cloudflare-temporary-deploy` optional skill
- Creative-ideation v2.1.0 method library

---

## ⚡ Performance

| Improvement | Impact |
|-------------|--------|
| Lazy-load gateway platform adapters | Faster cold start |
| libyaml `CSafeLoader` for config/plugins | Parse speed boost |
| FTS5 segment merge + `handoff_state` index | Reduced SQLite write-lock contention |
| Single-pass `list_profiles` + skill-count cache | Faster profile enumeration |

---

## 👥 Contributors

**381 people** contributed to this release — the largest cohort yet.

### Core
- **@teknium1** — release lead; MoA first-class, verification/goals, `/learn`, background review, security, providers, P0/P1 sweep
- **@OutThisLife** — desktop app (Projects, memory graph, `/journey`, multi-terminal, composer refactor, pets, verification UX)
- **@kshitijk4poor** — P0/P1 backlog burn: cron reliability, state perf, security, gateway
- **@benbarclay** — relay Phase 5/6, scale-to-zero/drain, dashboard auth/keys
- **@ethernet8023** — CI/docker (unified jobs, faster builds)
- **@helix4u** — Windows hardening

---

## 🔁 Notable Reverts

- Cron job storage returned to per-profile
- `auth.json` cloning removed (duplicating OAuth grant causes sibling revocation)
- Windows terminal-popup PRs rolled back
- `prompt_caching.enabled` toggle backed out for re-evaluation

---

## 📊 Release Stats

| Metric | Value |
|--------|-------|
| Commits | ~1,720 |
| Merged PRs | 998 |
| Files Changed | 2,215 |
| Insertions | ~251,000 |
| Deletions | ~41,000 |
| Issues Closed | 949 |
| Contributors | 381 |
| P0/P1 Open at Release | **0** |

---

*← [v0.17.0 — The Reach Release](/hermes/changelog/v0.17.0/) | [Changelog Home](/hermes/changelog/) →*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
