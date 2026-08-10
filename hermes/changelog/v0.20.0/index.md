---
title: Hermes Agent v0.20.0 — The Herald Release
description: Hermes Agent v0.20.0 (v2026.8.3) — The Herald Release. Streaming conversational voice with barge-in, A2A v1.0 agent protocol, signed outbound webhooks, grounded research citations, desktop artifacts & plugin SDK, CLI power commands, tool self-recovery, and smarter compression. ~3,650 commits, 647 contributors. August 3, 2026.
---

# Hermes Agent v0.20.0 (v2026.8.3)

**Release Date:** August 3, 2026
**Since v0.19.1:** ~945 commits · ~300 files changed · 82 contributors

> **The Herald Release.** Voice becomes conversational, Hermes talks to other agents, research gets citations you can verify, the desktop becomes a platform, and the CLI gets a power-user upgrade.

---

## ✨ Highlights

- **Streaming Conversational Voice with Barge-In** — Clause-by-clause TTS synthesis, interrupt by voice mid-sentence, busy-aware silence detection. Works across CLI voice mode, desktop, and gateway adapters. Talking to Hermes finally feels like a conversation.

- **Wake Words & Hands-Free Control** — Open-vocabulary wake phrases ("hey Hermes" or anything you pick), on-device detection (no audio leaves your machine), multi-profile voice routing. Say "stop" to end voice chat hands-free on every surface.

- **Voice on Every Platform** — Voice notes on WhatsApp, Feishu, DingTalk, LINE, QQ, Photon, Weixin transcribed and answered with platform-aware auto-TTS replies. Fully configurable STT with its own `hermes tools` category, GUI toggles, and OpenAI gpt-transcribe support.

- **Grounded Citations & Fact-Checking** — The new `grounded-citations` skill matches quotes against actual page text (not hallucinated), links citations to exact evidence, and a fact-checking mode verifies any document or claim. Research goes from "sounds right" to "provably sourced."

- **Outbound Webhooks** — Hermes pushes signed lifecycle events (session activity, turn completions, tool events) to any HTTP endpoint with HMAC signatures. Wire Hermes into CI, home automation, dashboards, or any HTTP-speaking service — no polling loop.

- **Desktop Becomes a Platform** — Artifacts (sandboxed live preview in right-rail viewer), plugin SDK (Kanban as founding plugin, `ctx.download`, floating panes, multiple GUI windows), global-hotkey quick-entry window. The desktop is now a workbench, not just a chat client.

- **Agent-to-Agent Protocol (A2A v1.0)** — Bundled plugin implementing the A2A standard. Hermes can discover, talk to, and be driven by other A2A-compatible agents. Closes issue #514 — one of the oldest feature requests.

- **CLI Power-User Wave** — `!command` runs shell instantly without a model turn. `/init` generates AGENTS.md. `/diff` shows staged/all/session changes. `/context` breaks down context window usage. `/focus` enables reduced-output view. Ctrl+S stashes prompts. `hermes import-agent` migrates from Claude Code/Codex CLI in one command.

- **Mid-Turn Redirects** — Correct the agent while it works — the active turn is redirected with your new guidance, preserving in-flight work and the original prompt. Double-ESC discards drafts, composer undo stack built in.

- **Tools That Fix Themselves** — Truncated terminal output spills to a readable file. `patch` detects already-applied edits and diagnoses whitespace mismatches. Searches probe near-misses and recover. `write_file` verifies on-disk content. Table stakes for long autonomous runs. Default tool iteration limit raised from 90 to 500.

- **Smarter, Gentler Compression** — Proactive tool-result pruning, per-turn micro-compaction, guaranteed N-user-message tail survival, progress-aware timeouts, ghost-skill defense. Long sessions stay coherent and stop stalling.

- **Smart Approvals Grow Up** — `hermes approvals suggest` mines history into allowlist proposals. Operator-customizable smart-approval policy. Consecutive-denial circuit breaker stops misbehaving loops cold. Desktop pairing approvals are profile-correct.

- **Faster Everywhere, Again** — Prompt caching covers tool schemas on native Anthropic. `hermes -w` cold start: ~14s → ~1.8s. Config reads 54× faster. Desktop 60fps wave 2: streaming cost independent of transcript length, idle CPU near zero.

---

## 🎙️ Voice & Speech

- Streaming conversational TTS with barge-in across all surfaces; clause-by-clause synthesis
- Voice chat UX: busy-aware silence, stop hint, thinking sounds, full-duplex turn listener
- On-device wake words with open-vocabulary phrases + multi-profile voice routing
- Model is told when the user interrupts its spoken reply
- Unified spoken-text preprocessing + unified STT language resolution (fixes wrong-language transcription)
- Fully configurable STT: `hermes tools` category, GUI toggle, dashboard dropdowns, OpenAI gpt-transcribe
- Platform-aware auto-TTS voice delivery (opus platforms, streamed gaps, captions)
- Inbound voice classification/routing for Feishu, DingTalk, LINE, QQ, Photon, WhatsApp, Weixin
- Sync per-sentence TTS pipelined with playback; Discord voice PCM streams to ffmpeg stdin

## 🏗️ Core Agent & Architecture

### Compression & Context
- Proactive tool-result pruning for large-window models; per-turn micro-compaction
- N-user tail guarantee (`compression.min_tail_user_messages`); bounded summarizer with head+tail retention
- Ghost-skill defense; progress-aware timeouts; lock-contended compression soft-defers
- Per-model threshold overrides; absolute token threshold; opt-in idle-triggered compaction
- Strict redaction at every compaction text boundary

### Prompt Caching & Performance
- Tool schemas cached on native Anthropic without history loss
- DeepSeek prompt caching on OpenCode gateways; per-API-call token accounting
- Readonly config loader at 29 call sites (28× cheaper reads); per-turn deepcopies killed (telemetry gate 54×)
- Lazy heavy-SDK imports (−8-10% import cost); streaming hot loop ~3× cheaper accounting
- Cold-start ~14s GIL stall mitigated; turn flush batched into one SQLite transaction

### Approvals & Agent Loop
- `hermes approvals suggest` mines approval history into allowlist proposals
- Consecutive-denial circuit breaker; docker/podman daemon-redirect approval gate
- Mid-turn redirects — user corrections steer the active turn
- Delegation: structured timeout/stall metadata, live per-child `/agents` status, subagent `execute_code` access
- Default tool iteration limit 90 → 500; tool_search validates blind tool_call args

### Tool Self-Recovery Wave
- Terminal: recoverable truncation (full output spilled to file), cwd echoed on directory change, failure hints
- Patch: already-applied edits return success no-op, whitespace-visualized diagnosis, ambiguous-match locations
- Search: zero-match probes + multi-path recovery, auto-multiline for newline patterns
- read_file default limit 500 → 2000; negative-result cache for misses; write_file verifies on-disk content
- execute_code recovery hints; skill_view dedup stub; tiered tool disclosure for large catalogs

### Providers & Models
- Vercel AI Gateway provider + Vercel Sandbox terminal backend return (SDK 0.7.2)
- Gemini 3.1 Pro + 3.6 Flash in catalogs; claude-opus-5 in OpenRouter + Nous Portal; deepseek-v4-flash-0731
- Bedrock Converse API prompt caching (cachePoint)
- OpenAI data-residency endpoints get declared transport + correct catalog
- MCP lazy server startup from fingerprint-keyed on-disk tool-schema cache

### Secrets & Config
- Command-helper secret source (composes with all vaults); one-command token rotation
- `${env:VAR}` SecretRef parity between config.yaml and MCP config
- Canonical config loaders + table-driven migration registry; auto-migration support floor at v12

## 🌐 Gateway, Relay & Fleet

- Session activity heartbeats, stall watchdog, bounded compression waits
- SessionState consolidation (19 session-keyed dicts → one scoped object)
- Relay parity waves: media, interactive prompts, thread lifecycle; egress typing indicators
- HSP skill sync: personal + org-skills client with token-gated discovery
- **Buzz** (Block/Nostr) platform adapter with native WebSocket transport + NIP-42 auth
- Photon: native polls, effects, clarify-as-poll, rich links
- Slack: native Block Kit clarify buttons; opt-in reaction triggers
- Discord auto-thread sessions; WhatsApp configurable inbound read receipts
- **Outbound webhooks** — push signed lifecycle events to external endpoints

## 🖥️ Desktop App — The Platform Wave

### Artifacts, Plugins & Quick Entry
- **Artifacts** — versioned cards, sandboxed live preview, right-rail viewer
- **Plugin SDK** — Kanban founding plugin, `ctx.download`, widget-app SDK, widget-grid layout engine
- **Quick-entry window** (global hotkey → any session); multiple GUI windows; floating pane placement
- SSH remote-backend connection mode; event-driven live sync replaces always-on polls
- Agent can drive the shell (preview pane + pane focus) AND inspect the desktop app it's developing

### Composer & UX
- Attach files/folders/links via picker; composer chips for @paths and pasted links
- Composer undo stack; double-ESC discards draft; double-Enter sends; type-to-focus
- 2-keypress model switching (⌘⇧M); YOLO in ⌘K with live toggle; keyboard-first pickers
- Grouped, live-ticking tool-activity line; @session links resolve to clickable titles
- iMessage-style emoji reactions (opt-in, two-way); double-click to heart
- Sidebar date dividers + pinned section; credit-usage toasts; Cron Blueprints + Webhooks pages

### Desktop Performance (60fps Wave 2)
- Streaming cost independent of transcript length; 60fps on real sessions
- Drag at 60fps with five streaming tabs; multitab streaming fast
- Idle CPU near zero in background; sidebar/overlay render churn killed
- ⌘K opens instantly; renderer cold start keeps shiki/mermaid off the boot path
- Playwright E2E suite with visual regression diffs

## 🖥️ CLI, TUI & Dashboard

- `!` shell mode; `/init` AGENTS.md generation; `/diff` (staged/all/session); `/context` breakdown; `/focus` reduced-output
- Ctrl+S prompt stash; persistent `/goal` indicator; multi-select clarify across CLI/gateway/TUI
- `hermes import-agent` — one-command migration from Claude Code/Codex CLI
- Per-turn summary line + live token flow in spinner; cross-surface theme SDK
- `hermes -w` startup ~14s → ~1.8s; banner update-check 6× faster
- Dashboard lazy-loads routes + GROUP BY session stats; session filtering tabs
- Arabic (ar) locale with RTL across desktop/dashboard/agent

## 🧩 Skills, Plugins & MCP

- **A2A v1.0** agent protocol plugin (closes #514)
- Curator: surface unmanaged skills + `curator adopt`; grounded-citations skill + fact-checking mode
- Office skills bundled: docx, xlsx, pdf + refreshed powerpoint
- Skills-tree debloat (yuanbao, segment-anything, jupyter → optional-skills)
- MCP: Comfy Cloud catalog entry with curated 20-tool default; lazy server startup from tool-schema cache
- NeMo Relay observability integration

## 🔒 Security & Reliability

- Iron-proxy credential-injection egress firewall
- DNS-pinned SSRF-safe fetches + Slack CDN allowlist; ReDoS eliminated in config-key redaction
- Tier-3 credential reads scoped; CVE dependency pins refreshed
- Windows hardening: text-mode subprocess decode bug class closed, console flashes hidden
- Four session-state fixes; compact v23 FTS layout + `hermes sessions optimize`
- OpenViking memory-provider hardening — fail closed on blocked endpoints

## 👥 Contributors

**647 contributors** shipped this release.

**Core:** @teknium1, @OutThisLife (desktop, voice, perf), @kshitijk4poor (perf, caching, salvage), @ethernet8023 (runtime, E2E, desktop), @benbarclay (relay, HSP, auth)

Thank you to all 647 contributors who contributed code, co-authored fixes, filed the ~1,200 issues this release closes, and had their PRs salvaged into main.

---

## Updating

```bash
hermes update
# or fresh install:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Full Changelog**: [v2026.7.20...v2026.8.3](https://github.com/NousResearch/hermes-agent/compare/v2026.7.20...v2026.8.3)

---

*← [v0.19.1 — Patch Release](/hermes/changelog/v0.19.1/) | [Changelog Home](/hermes/changelog/) →*

*↑ [Changelog Home](/hermes/changelog/)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
