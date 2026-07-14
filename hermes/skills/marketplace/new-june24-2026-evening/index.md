---
title: June 24, 2026 (Evening) — Skills Discovery Roundup
description: Evening sweep — 28 new Hermes repos discovered including ContextForge RAG profile, Math via Code skill, Memory Stack OS, Loop Maker, Skywork Skills Hub (18 skills), and 18+ more integrations and tools
---

# 🆕 June 24, 2026 (Evening) — Skills Discovery Roundup

**28 repos discovered, 5 setup guides created. Evening sweep following the morning roundup.**

---

## ⭐ Top Picks (with Setup Guides)

| # | Repo | Stars | Type | Setup Guide |
|---|------|:-----:|------|:-----------:|
| 1 | `codegraphtheory/context-forge-rag` | ⭐1 | Hermes Profile (RAG) | [ContextForge RAG Setup](/docs/hermes/skills/catalog/context-forge-rag-setup.html) |
| 2 | `tommulkins/hermes-skill-math-via-code` | ⭐0 | Skill (Math) | [Math via Code Setup](/docs/hermes/skills/catalog/math-via-code-setup.html) |
| 3 | `Chukwuemeka001/hermes-memory-stack` | ⭐0 | Memory OS | [Memory Stack Setup](/docs/hermes/skills/catalog/hermes-memory-stack-setup.html) |
| 4 | `EricTechPro/loop-maker` | ⭐0 | Loop Scaffolding | [Loop Maker Setup](/docs/hermes/skills/catalog/loop-maker-setup.html) |
| 5 | `Victor-F-M-A-R/skywork-skill-skill-repo-manager` | ⭐0 | Skill Management | [Skill Repo Manager Setup](/docs/hermes/skills/catalog/skill-repo-manager-setup.html) |

---

### 1. ContextForge RAG — Installable Hermes Profile (codegraphtheory)

A complete Hermes Agent profile for production RAG architecture — not just a single skill, but a full agent identity bundle. Built from the `hermes-profile-template`.

**Bundles 5 skills:** principal-ai-architect, technical-roadmapping, production-rag-architecture, rag-evaluation-observability, agentic-workflow-issue-factory.

Install with: `hermes profile install github.com/codegraphtheory/context-forge-rag --name context-forge-rag --yes`

**Why it matters:** First Hermes Agent *profile* (not skill) discovered. Represents a new distribution pattern — full agent identities as installable packages. MIT licensed.

---

### 2. Math via Code — Zero Arithmetic Errors (tommulkins)

Hard rule: all arithmetic with 3+ numbers goes through code execution. Born from repeated financial modeling errors where LLM in-head math produced wrong numbers on SDE, P&L, and facility rollups.

**Why it matters:** Directly applicable to CorpusIQ's business operator use case. Every financial calculation in lead qualification, pricing analysis, and growth metrics should route through this skill. MIT licensed.

---

### 3. Hermes Memory Stack — Memory OS Layer (Chukwuemeka001)

228 tests across 4 remediation areas + semantic retrieval + auto-extraction + temporal versioning. The most comprehensive memory solution found in the ecosystem to date.

**Components:** semantic session search, conservative auto-extraction, temporal versioning, state.db remediation, MEMORY.md audit, pointer rewrite, temporal migration.

**Why it matters:** Addresses a universal Hermes Agent pain point — memory overload and state.db bloat. 19KB README with production-ready tooling. Apache-2.0 licensed.

---

### 4. Loop Maker — Cross-Harness Loop Scaffolding (EricTechPro)

7-question wizard that interviews you and outputs a ready-to-run loop folder (SKILL.md + STATE.md + verifier.py + stop conditions). Works across Claude Code, Codex, Hermes, and OpenClaw.

**Key differentiator from Perfectloop:** Cross-harness portability. If you're building loops that need to run on multiple agent platforms, Loop Maker's abstract tool references handle it.

**Why it matters:** Complements Perfectloop for quick prototyping scenarios. MIT licensed.

---

### 5. Skill Repo Manager + Skywork Skills Hub (Victor-F-M-A-R)

Two-part system:
- **Skill Repo Manager:** Sync, audit, and manage Hermes skill repos with 3 scripts
- **Skywork Skills Hub:** Monorepo bundling 18 Hermes skills as Git submodules

The hub includes skills for: animations, architecture design, artifacts building, content marketing, PRD creation, data science, design extraction, frontend design, marketing psychology, short drama writing, stock market analysis, APA papers, business analysis reports, competitive analysis, legal agreements, web design, YouTube watching, and repo management.

**Why it matters:** Largest single-author Hermes skill collection discovered (18 skills). The submodule pattern is novel — enables monorepo-style management of distributed skill repos.

---

## 📋 Full Discovery List (28 repos)

### Skills & Profiles (5 repos — setup guides created)

| Repo | Notes |
|------|-------|
| `codegraphtheory/context-forge-rag` | ✅ Setup guide — Hermes profile for RAG |
| `tommulkins/hermes-skill-math-via-code` | ✅ Setup guide — arithmetic via code |
| `Chukwuemeka001/hermes-memory-stack` | ✅ Setup guide — memory OS (228 tests) |
| `EricTechPro/loop-maker` | ✅ Setup guide — cross-harness loop tool |
| `Victor-F-M-A-R/skywork-skill-skill-repo-manager` | ✅ Setup guide — skill repo management |

### Collections & Hubs (1 repo)

| Repo | Notes |
|------|-------|
| `Victor-F-M-A-R/skywork-skills-hub` | 📦 18-skill monorepo as Git submodules |

### Infrastructure & DevOps (4 repos)

| Repo | Description |
|------|-------------|
| `dhoman/dockter-hermes` | ⭐1 — Docker + Tailscale configs for Hermes |
| `Sanjeever/hermes-dock` | Wails desktop launcher for Hermes Docker |
| `LIDASHUN88/cookiecutter-hermes-workspace` | Cookiecutter template: constitution layer + .devlog/ skeleton |
| `Christian-Starcke/code-server-hermes-railway` | code-server + Hermes ACP on Railway |

### Agent Platforms & Control (4 repos)

| Repo | Description |
|------|-------------|
| `nemesis-agent/Nemesis` | Autonomous trading agents on Base via Hermes + MCP |
| `genildof/AgentDesk` | Browser-based Claude Code, Codex, Hermes runner |
| `IEatCodeDaily/olympus` | AI control plane for Hermes (React + Convex + Bun) |
| `yannbonzom/hermes-company-brain-starter` | Discord-native company brain with GitHub + cron |

### Mobile & Companion (2 repos)

| Repo | Description |
|------|-------------|
| `prasta1/psychopomp` | Hermes Agent iOS companion |
| `tulip-ai2/hermes-mobile` | Android app for Hermes via Termux |

### MQTT & IoT (1 repo)

| Repo | Description |
|------|-------------|
| `Phill93/hermes-mqtt-agentpet` | MQTT bridge — Blacky status, menubar, AgentPet |

### Config & Community (3 repos)

| Repo | Description |
|------|-------------|
| `mole-bi-com/hermes-config` | Hermes config sharing (Korean community) |
| `seyonv/hermes-hackathon-intel` | Hackathon intelligence dashboard |
| `nx107/novavoice` | Model-agnostic smart speaker (Hermes supported) |

### Cross-Agent Bridges (2 repos)

| Repo | Description |
|------|-------------|
| `XFSeven7/cursor2api` | Cursor CLI → OpenAI API bridge (for Hermes/OpenClaw) |
| `octer-ai/octer-shell` | Shell scripts for Octer.ai model on Hermes |

### OpenClaw-Topic (2 repos — noted, not Hermes-native)

| Repo | Description |
|------|-------------|
| `mrgizmo212/make-no-mistakes` | Agent harness research ebook (5.5KB README) |
| `obuchowski/openclaw-cron-to-transcript` | Cron-to-transcript delivery capture |

---

## 📊 Stats

| Metric | Count |
|--------|:-----:|
| New repos discovered | 28 |
| Setup guides created | 5 |
| Skills & profiles | 5 |
| Collections & hubs | 1 (18 skills) |
| Infrastructure/DevOps | 4 |
| Agent platforms | 4 |
| Mobile/Companion | 2 |
| Config/Community | 3 |
| Cross-agent bridges | 2 |
| OpenClaw-topic (not Hermes-native) | 2 |
| Marketplace total | 394+ curated skill repos |

---

*← [Marketplace Home](/hermes/skills/marketplace/) | [Skills Catalog](/hermes/skills/catalog/) →*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills). Built by [CorpusIQ](https://www.corpusiq.io).*
