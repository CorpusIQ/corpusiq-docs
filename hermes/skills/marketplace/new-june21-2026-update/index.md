---
title: New Hermes Skills — June 21, 2026 (Update)
description: 12 additional Hermes Agent skills discovered — decision frameworks, semantic skill routing, OpenSpec dashboard, browser event agent, and GEPA self-evolving skills
---

# New Skills: June 21, 2026 — Update

**Discovered:** June 21, 2026 (post-19:00 UTC sweep) — repos created after the morning discovery batch
**New repos:** 12 | **Key themes:** decision infrastructure, plugin architecture, automated skill routing

---

## Category 1: Architectural & Infrastructure Innovation (3 repos)

### varbees/council-decision-layer — Structured Decision-Making Skill (⭐0)

**High-impact.** A disciplined decision-making skill for Hermes Agent — stops ad-hoc architecture and strategy choices. Five proven decision patterns backed by DDIA and Google's Agent Guide, with a deterministic Python question engine (~600 LOC, stdlib-only) that logs every decision with rationale to SQLite.

| Feature | Detail |
|---------|--------|
| Patterns | tradeoff_matrix, failure_modes, end_to_end, ethics_triage, agentops_trajectory |
| Engine | Python stdlib-only, ~600 LOC question engine + SQLite decision log |
| Testing | 85 component tests with DB isolation, SQL injection hardened |
| Dependencies | Zero external deps, zero API keys |
| Install | `curl -fsSL https://raw.githubusercontent.com/varbees/council-decision-layer/main/install.sh \| bash` |

**Repo:** [varbees/council-decision-layer](https://github.com/varbees/council-decision-layer) | **Stars:** 0 | **Created:** June 21, 2026
**Built by:** [Antharmaya Labs](https://antharmaya.com/) / Harsha Vardhan

---

### freyandere/hermes-skill-router-plugin — Semantic Skill Router Plugin (⭐0)

**Architectural breakthrough.** Zero-VRAM semantic skill router using Semantic Router (Ollama + Qdrant). Auto-loads the correct SKILL.md before every LLM turn — 66 routes, ~17ms routing, bilingual (RU+EN), self-improving. A `pre_llm_call` plugin hook that injects matching skill context before every LLM call with fail-safe graceful degradation.

| Feature | Detail |
|---------|--------|
| Speed | 17ms total (15ms embed + 2ms search) |
| VRAM | Zero extra — all HTTP to existing Ollama + Qdrant |
| Routes | 66 routes covering all Hermes skills, ~1000 utterances |
| Threshold | 0.80 calibrated across 50+ test queries |
| Self-improving | Missed triggers auto-improve via cron daily |
| Fail-safe | Qdrant/Ollama down → agent continues without router |

**Repo:** [freyandere/hermes-skill-router-plugin](https://github.com/freyandere/hermes-skill-router-plugin) | **Stars:** 0 | **Created:** June 22, 2026
**Install:** `hermes plugins install freyandere/hermes-skill-router-plugin/plugin/semantic-router-preloader`

---

### FelineStateMachine/hermes-openspec — OpenSpec Dashboard Plugin (⭐0)

**Plugin with dashboard tab.** OpenSpec integration for Hermes Agent — agent tools that wrap the `openspec` CLI + a `/openspec` dashboard tab for browsing change proposals, specs, and branch diffs. Six agent tools (gated on CLI binary), kanban-style change board, spec browser with git diff comparison.

| Feature | Detail |
|---------|--------|
| Agent Tools | `openspec_context`, `openspec_list`, `openspec_show`, `openspec_validate`, `openspec_status`, `openspec_instructions` |
| Dashboard | Kanban board (ideas→done), spec browser, git diff view |
| Deep-linking | URL hash format for direct navigation |
| Gating | 5 of 6 tools gate on `openspec` binary; dashboard works without |
| Commits | 20 (actively developed) |

**Repo:** [FelineStateMachine/hermes-openspec](https://github.com/FelineStateMachine/hermes-openspec) | **Stars:** 0 | **Created:** June 22, 2026
**Install:** `hermes plugins install FelineStateMachine/hermes-openspec`

---

## Category 2: Browser & Event Automation (1 repo)

### washingtoneimae-dot/browser-event-agent — Event-Layer Browser Agent (⭐0)

**Paradigm innovation.** Browser extension + Hermes skill that intercepts every UI event directly from the browser's event loop — no screenshots, no CDP. Claims 100× speedup vs screenshot agents (~10ms/event vs ~5-10s). Captures 25+ event types with composite gesture detection plus DOM snapshots every 2 seconds.

| Feature | Detail |
|---------|--------|
| Events | click, keydown, scroll, touch, drag, pointer, clipboard (25+ types) |
| Gestures | Long press, pinch zoom, swipe detection |
| DOM Snapshots | Every 2 seconds — tags, IDs, text, aria-labels, bounding boxes |
| Agent Actions | click, type, scroll, hover, highlight, fill form, navigate |
| Architecture | Browser extension → WebSocket (127.0.0.1:9789) → Hermes LLM |

**Repo:** [washingtoneimae-dot/browser-event-agent](https://github.com/washingtoneimae-dot/browser-event-agent) | **Stars:** 0 | **Created:** June 21, 2026
**Status:** Early stage (1 commit)

---

## Category 3: Self-Evolving Agent Backups (4 repos)

### beer-sakthai/sakthai-skills — GEPA Self-Evolving Skills (⭐0)

Self-evolving Hermes skills for the sakthai agent using GEPA (Generate/Execute/Plan/Adapt) methodology. Active sync with co-authored commits (Claude Opus 4.8). Includes live config backup (secrets excluded), SOUL.md snapshots, and skill directory.

**Repo:** [beer-sakthai/sakthai-skills](https://github.com/beer-sakthai/sakthai-skills) | **Stars:** 0 | **Created:** June 21, 2026

Sister repos (same pattern for different GEPA agents):
- [beer-sakthai/saksit-skills](https://github.com/beer-sakthai/saksit-skills) — saksit agent
- [beer-sakthai/saksee-skills](https://github.com/beer-sakthai/saksee-skills) — saksee agent

---

### 963072676/hermes-researcher-backup — Self-Evolution Backup Pipeline (⭐0)

Public, version-controlled trace of a self-modifying AI researcher profile. SOUL drafts, skill proposals, memory snapshots, weekly digests, and cron outputs — all with a push strategy (real-time critical + daily 23:50 UTC aggregate). C-tier self-evolution upgrade documented.

**Repo:** [963072676/hermes-researcher-backup](https://github.com/963072676/hermes-researcher-backup) | **Stars:** 0 | **Created:** June 21, 2026

---

## Category 4: Domain & Personal Skills (4 repos)

### kuil09/tossinvest-openapi-agent-pack — Toss Securities API Pack (⭐0)

Agent-compatible instruction pack for Toss Securities Open API. Includes Hermes SKILL.md, agent-agnostic guide, system prompt block, and reference docs. Human approval gate before any live order execution.

**Repo:** [kuil09/tossinvest-openapi-agent-pack](https://github.com/kuil09/tossinvest-openapi-agent-pack) | **Stars:** 0 | **Created:** June 22, 2026

---

### ai-workflow-space/hermes-skills — Personal Skill Library (⭐0)

Curated personal skill library: systematic-debugging, spike, TDD, release-gate, opencode-driven-development, stock-toolkit, pr-workflow, code-review, price-alert-system, react-dropdown-race-fix. Well-structured with SKILL.md format compliance.

**Repo:** [ai-workflow-space/hermes-skills](https://github.com/ai-workflow-space/hermes-skills) | **Stars:** 0 | **Created:** June 22, 2026

---

### SouthpawIN/hermes-test-skill — Test Skill (⭐0)

Hermes Agent test skill repository. Utility/testing pattern.

**Repo:** [SouthpawIN/hermes-test-skill](https://github.com/SouthpawIN/hermes-test-skill) | **Stars:** 0 | **Created:** June 21, 2026

---

### MarcleWright/marcle_hermes_skill_plugin — Personal Hermes Plugin (⭐0)

Personal Hermes Agent skill plugin.

**Repo:** [MarcleWright/marcle_hermes_skill_plugin](https://github.com/MarcleWright/marcle_hermes_skill_plugin) | **Stars:** 0 | **Created:** June 22, 2026

---

## Setup Guides

Dedicated setup guides created for the 3 highest-impact new skills:

| Skill | Guide | Why |
|-------|-------|-----|
| **council-decision-layer** | [Setup →](/hermes/skills/catalog/council-decision-layer-setup/) | Decision infrastructure: 5 proven frameworks, 85 tests, zero deps |
| **hermes-skill-router-plugin** | [Setup →](/hermes/skills/catalog/hermes-skill-router-setup/) | Architectural innovation: 17ms semantic routing, self-improving |
| **hermes-openspec** | [Setup →](/hermes/skills/catalog/hermes-openspec-setup/) | Dashboard + agent tools for OpenSpec-driven development |

---

## Ecosystem Patterns

1. **Plugin architecture maturing** — `pre_llm_call` hooks, dashboard tabs, and semantic routing show Hermes plugin ecosystem accelerating
2. **Decision infrastructure emerging** — council-decision-layer fills the gap between "agent can do anything" and "agent should think before acting"
3. **Self-evolution going public** — GEPA agents and researcher backups show community codifying self-improvement loops
4. **Browser automation evolving** — event-layer agents challenge screenshot-based approaches with 100× speed claims
5. **API packs bridging ecosystems** — tossinvest pattern shows skills as bridge between Hermes and other agent frameworks

---

*← [Previous Discovery](/hermes/skills/marketplace/new-june21-2026/) | [Marketplace Home](/hermes/skills/marketplace/)*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*
