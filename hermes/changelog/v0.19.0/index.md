---
title: Hermes Agent v0.19.0 — The Quicksilver Release
description: Hermes Agent v0.19.0 (v2026.7.20) — The Quicksilver Release. ~80% first-token speed improvement, terminal billing, Bitwarden/1Password integration, smart approvals, durable delivery, live subagent transcripts, new frontier models, and 2,245 commits from 450+ contributors. July 20, 2026.
---

# Hermes Agent v0.19.0 (v2026.7.20)

**Release Date:** July 20, 2026
**Since v0.18.0:** ~2,245 commits · ~1,065 merged PRs · ~2,465 files changed · ~300,000 insertions · ~36,000 deletions · **~3,300 issues closed** · **450+ community contributors**

> **The Quicksilver Release.** Hermes is the messenger god, and this window we made him move like it. First-turn time-to-first-token dropped **~80% on every platform**, reasoning streams live by default, the desktop app got a ~20-PR speed overhaul, and the TUI renders markdown incrementally. Around that speed spine: manage your Nous subscription without leaving the terminal, plug Bitwarden and 1Password straight into Hermes, let smart approvals judge flagged commands for you, watch your subagents work live, and trust that a finished response survives a gateway crash. This release also rolls up everything from the v0.18.1 and v0.18.2 infrastructure patch tags.

---

## ✨ Highlights

- **~80% faster first-token time** — Cold-start "Initializing agent..." dropped from ~4.3s to ~0.9s across CLI, gateway, TUI, desktop, and cron. Reasoning models now stream their thinking live by default, and the response box paints per token instead of per line. ([#59332](https://github.com/NousResearch/hermes-agent/pull/59332), [#59389](https://github.com/NousResearch/hermes-agent/pull/59389))

- **Desktop app speed wave — 20+ targeted perf PRs** — 14× faster streaming markdown, virtualized diffs, snappy session switching, pre-warmed profile backends, and idle-mount boot-hidden panes. The desktop app feels native under load. ([#67154](https://github.com/NousResearch/hermes-agent/pull/67154), [#67818](https://github.com/NousResearch/hermes-agent/pull/67818), [#65898](https://github.com/NousResearch/hermes-agent/pull/65898))

- **Terminal billing — `/subscription` and `/topup`** — See your plan, preview upgrade costs, schedule downgrades, and apply changes — all from the TUI or classic CLI. The desktop app got a matching billing settings tab. ([#51639](https://github.com/NousResearch/hermes-agent/pull/51639), [#61054](https://github.com/NousResearch/hermes-agent/pull/61054))

- **Smart approvals are now the default** — An LLM reviewer independently assesses flagged commands instead of asking you to approve every single one. Combined with user-defined deny rules and `/deny <reason>`, approval fatigue drops sharply without giving up control. ([#62661](https://github.com/NousResearch/hermes-agent/pull/62661), [#59164](https://github.com/NousResearch/hermes-agent/pull/59164))

- **Bitwarden & 1Password secret sources** — A pluggable `SecretSource` interface fetches API keys from Bitwarden and 1Password (`op://` references) at load time, with multiple vaults, deterministic precedence, and conflict warnings. ([#59498](https://github.com/NousResearch/hermes-agent/pull/59498))

- **Watch your subagents work — live transcripts + durable background delegation** — `delegate_task` dispatches return live transcript files you can `tail -f`. Background delegation completions are now durable through process restarts via an ownership-checked ledger. ([#67479](https://github.com/NousResearch/hermes-agent/pull/67479), [#63494](https://github.com/NousResearch/hermes-agent/pull/63494))

- **Delivery-obligation ledger** — Final responses are recorded in a durable ledger in `state.db` and redelivered on the next boot if the gateway crashes mid-delivery. Closes a P1 silent-loss window for Telegram, Discord, Slack, and every other channel. ([#67181](https://github.com/NousResearch/hermes-agent/pull/67181))

- **Profile-based message routing** — A single multiplexed gateway sharing one bot token can route specific guilds, channels, or threads to different profiles — each with fully isolated config, skills, memory, and secrets. ([#64835](https://github.com/NousResearch/hermes-agent/pull/64835), [#65700](https://github.com/NousResearch/hermes-agent/pull/65700))

- **New providers and frontier models** — Fireworks AI and DeepInfra as first-class providers. Model catalogs: GPT-5.6 (Sol/Terra/Luna + Pro), grok-4.5 (GA), moonshotai/kimi-k3, claude-fable-5 / claude-sonnet-5, tencent/hy3, plus LM Studio JIT loading. ([#62593](https://github.com/NousResearch/hermes-agent/pull/62593), [#63969](https://github.com/NousResearch/hermes-agent/pull/63969), [#61616](https://github.com/NousResearch/hermes-agent/pull/61616))

- **New reasoning effort tiers — `max` and `ultra`** — Selectable everywhere with per-model overrides, per-slot MoA preset effort, and per-task auxiliary effort. Thinking depth is now a dial, not a global switch. ([#62650](https://github.com/NousResearch/hermes-agent/pull/62650), [#64458](https://github.com/NousResearch/hermes-agent/pull/64458))

- **Session export to Markdown, Quarto, HTML, and Hugging Face formats** — With full filter surface, optional `--redact` secret-scrubbing, and compacted-session lineage stitching. ([#60186](https://github.com/NousResearch/hermes-agent/pull/60186))

- **Security hardening round** — Vertex credential scoping, media/vision file-read guards, webhook body-cap sweep, bot-token redaction, six P1 hardening PRs, and CI hardened against untrusted-ref interpolation. ([#57660](https://github.com/NousResearch/hermes-agent/pull/57660), [#58709](https://github.com/NousResearch/hermes-agent/pull/58709))

---

## ⚡ Performance — the speed spine

### First-turn latency (all platforms)
- **~80% TTFT cut** — Discord capability detection off the critical path (token-keyed 24h disk cache), Ollama probe skipped for non-Ollama providers, agent-init blocking work removed; cold submit→dispatch ~4.3s → ~0.9s ([#59332](https://github.com/NousResearch/hermes-agent/pull/59332))
- `display.show_reasoning` default ON (watch the model think instead of a spinner), per-token response-box painting, prompt-build caching, mtime-cached timezone resolution ([#59389](https://github.com/NousResearch/hermes-agent/pull/59389))
- Segment mixed tool batches to recover lost concurrency; drop per-call base64 re-serialization from request-size estimates ([#64460](https://github.com/NousResearch/hermes-agent/pull/64460), [#67788](https://github.com/NousResearch/hermes-agent/pull/67788))

### Desktop speed wave
- 14× less splitter CPU via incremental block lexing; virtualized review-pane diffs; snappy session switching; killed the layout-thrash cascade ([#67154](https://github.com/NousResearch/hermes-agent/pull/67154), [#67818](https://github.com/NousResearch/hermes-agent/pull/67818), [#65898](https://github.com/NousResearch/hermes-agent/pull/65898))
- Cut startup serialization + per-turn REST amplification; pre-warm profile backends and gateway sockets on hover intent; idle-mount boot-hidden panes ([#66747](https://github.com/NousResearch/hermes-agent/pull/66747), [#66347](https://github.com/NousResearch/hermes-agent/pull/66347), [#67857](https://github.com/NousResearch/hermes-agent/pull/67857))
- Stop per-token sidebar + tool-row re-renders during streaming; batch sidebar session slices; rAF-coalesced sash resizes ([#67742](https://github.com/NousResearch/hermes-agent/pull/67742), [#67842](https://github.com/NousResearch/hermes-agent/pull/67842), [#67245](https://github.com/NousResearch/hermes-agent/pull/67245))
- Systematized perf benchmark harness with trustworthy cold-start measurement ([#67466](https://github.com/NousResearch/hermes-agent/pull/67466), [#67697](https://github.com/NousResearch/hermes-agent/pull/67697))

### Everywhere else
- TUI renders streamed markdown incrementally per block ([#67236](https://github.com/NousResearch/hermes-agent/pull/67236))
- Skill discovery cached by scan signature; snapshot manifest builds ~5× faster ([#61414](https://github.com/NousResearch/hermes-agent/pull/61414), [#61131](https://github.com/NousResearch/hermes-agent/pull/61131))
- Copy-on-write message prep; model-metadata probe-cache cluster; gateway session resume from one SELECT ([#61133](https://github.com/NousResearch/hermes-agent/pull/61133), [#61368](https://github.com/NousResearch/hermes-agent/pull/61368), [#67247](https://github.com/NousResearch/hermes-agent/pull/67247))
- `hermes update` skips npm install when Node manifests are unchanged ([#61580](https://github.com/NousResearch/hermes-agent/pull/61580))
- Byte-stable gateway system prompts — pinned session-context render keeps the prompt cache alive ([#67403](https://github.com/NousResearch/hermes-agent/pull/67403))

---

## 🏗️ Core Agent & Architecture

### Providers & models
- **Fireworks AI** provider with cost estimation, promoted to #2 in provider pickers ([#62593](https://github.com/NousResearch/hermes-agent/pull/62593), [#65476](https://github.com/NousResearch/hermes-agent/pull/65476))
- **DeepInfra** hardened integration; **Upstage Solar** provider ([#63969](https://github.com/NousResearch/hermes-agent/pull/63969), [#64541](https://github.com/NousResearch/hermes-agent/pull/64541))
- **GPT-5.6 (Sol/Terra/Luna + Pro)** end-to-end — context lengths, native/Codex catalogs, pricing, compaction caps ([#61616](https://github.com/NousResearch/hermes-agent/pull/61616))
- **Claude Sonnet 5 fully wired** — curated lists, intro pricing, and metadata across every route ([#67932](https://github.com/NousResearch/hermes-agent/pull/67932))
- grok-4.5 (GA), kimi-k3, claude-fable-5, tencent/hy3, LM Studio JIT loading ([#60887](https://github.com/NousResearch/hermes-agent/pull/60887), [#65913](https://github.com/NousResearch/hermes-agent/pull/65913), [#65472](https://github.com/NousResearch/hermes-agent/pull/65472))
- **Hide providers you don't use** — `enabled: false` per-provider flag + `excluded_providers` config ([#67971](https://github.com/NousResearch/hermes-agent/pull/67971))
- Bedrock catalog wave: real context-window probing, 1M-context rows for Claude + Fable, Opus 4.8/4.7 rows ([#68007](https://github.com/NousResearch/hermes-agent/pull/68007), [#67977](https://github.com/NousResearch/hermes-agent/pull/67977))
- Provider pickers: Qwen providers folded into one group row; collapsible provider groups in desktop ([#67758](https://github.com/NousResearch/hermes-agent/pull/67758), [#67904](https://github.com/NousResearch/hermes-agent/pull/67904))

### Reasoning & MoA
- `max` + `ultra` effort levels across every surface and route ([#62650](https://github.com/NousResearch/hermes-agent/pull/62650))
- Per-model reasoning_effort overrides; per-task auxiliary effort; per-slot MoA preset effort; session-scoped `/reasoning` ([#64458](https://github.com/NousResearch/hermes-agent/pull/64458), [#64597](https://github.com/NousResearch/hermes-agent/pull/64597))
- MoA: `reference_max_tokens` to cap advisor output; per-preset fanout cadence; stale presets surfaced without retries ([#56756](https://github.com/NousResearch/hermes-agent/pull/56756), [#57591](https://github.com/NousResearch/hermes-agent/pull/57591))

### Delegation, approvals & the agent loop
- Live subagent transcripts + durable background completions ([#67479](https://github.com/NousResearch/hermes-agent/pull/67479), [#63494](https://github.com/NousResearch/hermes-agent/pull/63494))
- Smart approvals default + user-defined deny rules + `/deny <reason>` ([#62661](https://github.com/NousResearch/hermes-agent/pull/62661), [#59164](https://github.com/NousResearch/hermes-agent/pull/59164), [#54518](https://github.com/NousResearch/hermes-agent/pull/54518))
- `/model --once` — one-turn model override that reverts automatically ([#67113](https://github.com/NousResearch/hermes-agent/pull/67113))
- Stacked slash-skill invocations — `/skill-a /skill-b do XYZ` loads both skills in order ([#57987](https://github.com/NousResearch/hermes-agent/pull/57987), [#58763](https://github.com/NousResearch/hermes-agent/pull/58763))

### Secret sources
- Pluggable `SecretSource` interface; Bitwarden + 1Password vaults with deterministic precedence and conflict warnings ([#59498](https://github.com/NousResearch/hermes-agent/pull/59498))

### Sessions & compression
- Sessions export: Markdown/QMD/HTML/prompt-only/trace formats, HF upload, `--redact`, unified filters ([#60186](https://github.com/NousResearch/hermes-agent/pull/60186), [#60492](https://github.com/NousResearch/hermes-agent/pull/60492))
- Compression: preserve human intent and durable handoffs; retain prompt cache when memory is unchanged ([#67275](https://github.com/NousResearch/hermes-agent/pull/67275), [#67916](https://github.com/NousResearch/hermes-agent/pull/67916))
- Gateway session metadata consolidated into state.db; exact API bytes persisted in `api_content` sidecar ([#58899](https://github.com/NousResearch/hermes-agent/pull/58899), [#59203](https://github.com/NousResearch/hermes-agent/pull/59203))

---

## 🌐 Gateway, Fleet & Relay

- **Durable delivery-obligation ledger** for final responses ([#67181](https://github.com/NousResearch/hermes-agent/pull/67181))
- **Profile-based routing** for inbound messages + multiplex hardening wave 2 ([#64835](https://github.com/NousResearch/hermes-agent/pull/64835), [#65700](https://github.com/NousResearch/hermes-agent/pull/65700), [#60589](https://github.com/NousResearch/hermes-agent/pull/60589))
- Per-session turn lease + conversation-scope funnel; unified session reset boundaries ([#67401](https://github.com/NousResearch/hermes-agent/pull/67401), [#65783](https://github.com/NousResearch/hermes-agent/pull/65783))
- Session auto-reset default off; webhook payload filters + route scripts; platform HTTP event callback routing ([#60194](https://github.com/NousResearch/hermes-agent/pull/60194), [#57685](https://github.com/NousResearch/hermes-agent/pull/57685))
- Relay: generic OIDC client-credentials provisioning; Nous auth forensics + self-heal; Docker re-seeds terminally-dead bootstrap session on boot ([#60730](https://github.com/NousResearch/hermes-agent/pull/60730), [#59976](https://github.com/NousResearch/hermes-agent/pull/59976))

---

## 📱 Messaging Platforms

- **Inline choice pickers** for `/reasoning` and `/fast` on Telegram, Discord, and Matrix — one-tap native buttons ([#65799](https://github.com/NousResearch/hermes-agent/pull/65799))
- **WhatsApp**: native Baileys polls, locations, rich inbound metadata; dashboard pairing flow ([#58865](https://github.com/NousResearch/hermes-agent/pull/58865), [#60571](https://github.com/NousResearch/hermes-agent/pull/60571))
- **Discord**: recover messages missed during reconnect; auto-created threads renamed to session titles; configurable interactive view timeout ([#66149](https://github.com/NousResearch/hermes-agent/pull/66149), [#60187](https://github.com/NousResearch/hermes-agent/pull/60187))
- **Slack**: live per-tool status line ([#67080](https://github.com/NousResearch/hermes-agent/pull/67080))
- **Telegram**: per-topic free-response allowlist ([#65543](https://github.com/NousResearch/hermes-agent/pull/65543))
- **Voice**: `stt.echo_transcripts` toggle; MEDIA captions attached to media bubbles on standalone sends ([#58859](https://github.com/NousResearch/hermes-agent/pull/58859), [#61415](https://github.com/NousResearch/hermes-agent/pull/61415))

---

## 🖥️ Hermes Desktop App

- **Contribution-driven shell on a layout-tree model** — panes, zones, and layouts as data ([#60638](https://github.com/NousResearch/hermes-agent/pull/60638), [#67303](https://github.com/NousResearch/hermes-agent/pull/67303))
- **Capabilities page** — Skills/Tools/MCP + Hub in one place, with responsive overlay nav ([#57590](https://github.com/NousResearch/hermes-agent/pull/57590), [#57441](https://github.com/NousResearch/hermes-agent/pull/57441))
- **Hermes Cloud connection mode**; soft gateway switch + gateway-settings polish; terminal execution backend picker ([#61912](https://github.com/NousResearch/hermes-agent/pull/61912), [#67203](https://github.com/NousResearch/hermes-agent/pull/67203))
- Keybind hint tooltips + keybinds settings tab; unified worktree dialog; green unread dot for background-finished sessions ([#65204](https://github.com/NousResearch/hermes-agent/pull/65204), [#62243](https://github.com/NousResearch/hermes-agent/pull/62243))
- Session + project color system; unified active-project identity in chat status ([#67469](https://github.com/NousResearch/hermes-agent/pull/67469), [#67681](https://github.com/NousResearch/hermes-agent/pull/67681))
- Declarative memory-provider panel + full-config modal; config-defined TTS/STT providers; per-job cron model picker; UI scale setting; Ctrl/Cmd+wheel zoom ([#67206](https://github.com/NousResearch/hermes-agent/pull/67206), [#67759](https://github.com/NousResearch/hermes-agent/pull/67759))
- Full TypeScript conversion of the desktop tree ([#57855](https://github.com/NousResearch/hermes-agent/pull/57855))

---

## 📊 Web Dashboard

- Memory provider switching; safe session import flow; WhatsApp pairing; Discord-specific toolsets from web UI ([#60569](https://github.com/NousResearch/hermes-agent/pull/60569), [#63699](https://github.com/NousResearch/hermes-agent/pull/63699))
- Terminal keep-alive + reattach for dashboard chat sessions; heavy turns isolated in a compute host ([#60515](https://github.com/NousResearch/hermes-agent/pull/60515), [#65895](https://github.com/NousResearch/hermes-agent/pull/65895))
- Paste/drop images into Chat; profile + gateway topology on `/api/status`; mobile/hosted OpenAI OAuth login ([#61929](https://github.com/NousResearch/hermes-agent/pull/61929), [#60537](https://github.com/NousResearch/hermes-agent/pull/60537))
- `hermes serve` is a true headless backend (no web UI build/mount) ([#55923](https://github.com/NousResearch/hermes-agent/pull/55923))

---

## 🧰 CLI & TUI

- `/subscription` + `/topup` terminal billing ([#51639](https://github.com/NousResearch/hermes-agent/pull/51639))
- `/model --once` — one-turn model override ([#67113](https://github.com/NousResearch/hermes-agent/pull/67113))
- Stacked slash-skill invocations with autocomplete + ghost text ([#57987](https://github.com/NousResearch/hermes-agent/pull/57987), [#58763](https://github.com/NousResearch/hermes-agent/pull/58763))
- `--safe-mode` troubleshooting flag; uninstall dry-run; TLS failures fail fast with fix hints ([#45300](https://github.com/NousResearch/hermes-agent/pull/45300), [#60111](https://github.com/NousResearch/hermes-agent/pull/60111))
- TUI: model picker refresh support; custom skill bundles dispatched as agent turns ([#59782](https://github.com/NousResearch/hermes-agent/pull/59782), [#62859](https://github.com/NousResearch/hermes-agent/pull/62859))
- Hermes Console REPL + perf follow-ups; `hermes curator usage` all-skills view ([#57781](https://github.com/NousResearch/hermes-agent/pull/57781), [#36727](https://github.com/NousResearch/hermes-agent/pull/36727))

---

## 🔧 Tool System, Skills & MCP

- MCP: `mcp__server__tool` naming convention; server log notifications surfaced in agent.log; hosted OAuth completed across Dashboard + Desktop ([#52750](https://github.com/NousResearch/hermes-agent/pull/52750), [#57416](https://github.com/NousResearch/hermes-agent/pull/57416), [#66151](https://github.com/NousResearch/hermes-agent/pull/66151))
- Skills: `security/unbroker` (autonomous data-broker removal); `unreal-mcp` companion skill; blender-mcp reworked ([#57438](https://github.com/NousResearch/hermes-agent/pull/57438), [#57902](https://github.com/NousResearch/hermes-agent/pull/57902), [#65989](https://github.com/NousResearch/hermes-agent/pull/65989))
- Browser: full snapshots stored on truncation; computer_use follows cua-driver verify→escalate ladder ([#65923](https://github.com/NousResearch/hermes-agent/pull/65923), [#67123](https://github.com/NousResearch/hermes-agent/pull/67123))
- Kanban: modal create-task dialog + editable board project directory; grab-to-pan board scrolling ([#66333](https://github.com/NousResearch/hermes-agent/pull/66333), [#63638](https://github.com/NousResearch/hermes-agent/pull/63638))
- Cron: durable execution audit history; one-shot stale-removal race fixed ([#61791](https://github.com/NousResearch/hermes-agent/pull/61791), [#62014](https://github.com/NousResearch/hermes-agent/pull/62014))
- mem0: self-hosted dashboard backend + recall tuning + setup-wizard mode ([#56943](https://github.com/NousResearch/hermes-agent/pull/56943), [#60494](https://github.com/NousResearch/hermes-agent/pull/60494))
- Image gen: Codex image inputs; unsupported Codex image accounts classified; tool args recursively normalized by schema ([#57017](https://github.com/NousResearch/hermes-agent/pull/57017), [#63627](https://github.com/NousResearch/hermes-agent/pull/63627))

---

## 🔒 Security & Reliability

- Vertex: credential/project/region resolution through profile secret scope; `VERTEX_CREDENTIALS_PATH` stripped from subprocess env ([#56680](https://github.com/NousResearch/hermes-agent/pull/56680), [#56582](https://github.com/NousResearch/hermes-agent/pull/56582))
- Six P1 hardening PRs salvaged in one pass — browser guards, MEDIA anchoring, .env lockdown ([#57660](https://github.com/NousResearch/hermes-agent/pull/57660))
- Media/vision/image-gen local-file reads routed through shared credential-read guard; unified image-source resolver ([#58709](https://github.com/NousResearch/hermes-agent/pull/58709), [#58752](https://github.com/NousResearch/hermes-agent/pull/58752))
- Webhook body-cap sweep: explicit `client_max_size` on 3 uncapped aiohttp servers ([#59180](https://github.com/NousResearch/hermes-agent/pull/59180), [#59215](https://github.com/NousResearch/hermes-agent/pull/59215))
- Redaction: Fireworks token prefixes + Telegram transport errors; env-lookup false positives fixed ([#58501](https://github.com/NousResearch/hermes-agent/pull/58501), [#58534](https://github.com/NousResearch/hermes-agent/pull/58534))
- Dashboard: managed-files credential guard widened; OAuth token TOCTOU closed with atomic 0o600 writes ([#58222](https://github.com/NousResearch/hermes-agent/pull/58222), [#60236](https://github.com/NousResearch/hermes-agent/pull/60236))
- CI: untrusted refs passed through env, not `run:` interpolation; JS/TS tests wired into CI ([#57842](https://github.com/NousResearch/hermes-agent/pull/57842), [#60707](https://github.com/NousResearch/hermes-agent/pull/60707))
- Docker: terminal network toggle; Git Bash Mandatory-ASLR install failures detected ([#59149](https://github.com/NousResearch/hermes-agent/pull/59149), [#64651](https://github.com/NousResearch/hermes-agent/pull/64651))

---

## Updating

```bash
hermes update        # existing installs
pip install -U hermes-agent
```

---

## 👥 Contributors — 450+ people

### Core team
- **@teknium1** — release lead; TTFT perf wave, delivery + delegation durability, smart approvals, SecretSource, gateway multiplex, sessions export, security round, ~290-PR community salvage
- **@OutThisLife** — desktop app (speed wave, layout-tree shell, Capabilities page, session colors, TUI incremental markdown, perf harness)
- **@kshitijk4poor** — GPT-5.6 end-to-end, DeepInfra + Upstage Solar providers, perf cluster, compression integrity, mem0, dashboard guards
- **@ethernet8023** — CI overhaul, desktop keybinds/worktrees/status indicators, full desktop TypeScript conversion
- **@benbarclay** — relay OIDC provisioning, gateway multiplex override, Nous auth self-heal, hosted MCP OAuth
- **@alt-glitch** — terminal billing (`/subscription`, `/topup`), desktop billing tab
- **@helix4u** — desktop provider/model UX, TUI model picker refresh, Windows install/updater hardening
- **@austinpickett** — desktop custom endpoint settings
- **@SHL0MS** — unbroker + unreal-mcp skills, humanizer expansion

### Top community contributors
- **@srojk34** — Vertex credential scoping, subprocess env stripping, Raft chunked-request body limits
- **@HexLab98** — 11 fixes across MCP capability gating, Windows installer PATH, desktop cron editing
- **@UnathiCodex** — desktop stability: zoom, LaTeX rendering, resume-stall and runtime-readiness fixes
- **@xxxigm** — `<think>` leak fix, dashboard auth/theme/PTY fixes
- **@erosika** — desktop declarative memory-provider panel + honcho recall/timeout correctness
- **@Frowtek** — credential security: master stores never mounted into skill sandboxes, live-transcript redaction
- **@necoweb3** — browser private-page CDP guard, cron one-shot liveness, gateway compression fail-closed
- **@DavidMetcalfe** — desktop updater version pill, local/custom endpoint exposure
- **@shannonsands** — dashboard: mobile channel setup, Discord toolsets from web UI
- **@vishal-dharm** — Gemini request-context improvements
- **@PRATHAMESH75** — cron one-shot stale-removal race, dashboard multiplex port-binding guard

Plus 440+ additional contributors — the biggest contributor window yet.

---

**Full Changelog**: [v2026.7.1...v2026.7.20](https://github.com/NousResearch/hermes-agent/compare/v2026.7.1...v2026.7.20)

---

*← [v0.18.2 — WhatsApp Baileys Fix](/hermes/changelog/v0.18.2/) | [Changelog Home](/hermes/changelog/) →*

*↑ [Changelog Home](/hermes/changelog/)*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
