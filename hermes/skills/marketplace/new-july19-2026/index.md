---
title: "July 19, 2026 — Hermespace Pocket Workbench, Cursor Dispatcher, Plutus Billing, Daidala Workshop"
description: "4 new Hermes-relevant repos discovered: hermespace (46★, persistent agent world), cursor-dispatcher (1★, Cursor CLI delegation), plutus (2★, LLM billing), daidala (0★, craft workshop)."
---

# 🆕 July 19, 2026 — 4 New Hermes-Agent Repos

**Date:** July 19, 2026
**New Repos:** 4 | **New Skills:** ~12+ | **Combined Stars:** 49

Morning discovery sweep across `topic:hermes-agent` and `topic:agent-skills` repos pushed since July 18, 2026. Cross-referenced against all prior marketplace pages (June 9 — July 18, 2026). The headline find: **hermespace** (46★) — a persistent agent world that grows forever, adding a limited working-memory desk beside Hermes with dual decode, fabric for skill ranking, and an append-only archive.

---

## New Repos at a Glance

| # | Repo | Stars | Skills | Category | Hermes-Ready |
|---|------|:-----:|:------:|----------|:------------:|
| 1 | **hermespace** | 46 | 1+ | Agent Memory / Workbench | ✅ SKILL.md |
| 2 | **plutus** | 2 | — | Billing / Spend Monitor | ✅ Tagged |
| 3 | **hermes-cursor-dispatcher** | 1 | 1 | Coding / Delegation | ✅ SKILL.md |
| 4 | **daidala** | 0 | — | Workflow / Craft | ✅ Plugin |

---

## Category Breakdown

### Agent Memory & Workbench — hermespace (46★, v0.18.3) ⭐ Setup Guide Available

**Repo:** [PabloTheThinker/hermespace](https://github.com/PabloTheThinker/hermespace)
**Install:** `npx skills add PabloTheThinker/hermespace --skill hermespace -g -y`
**Language:** Python 3.10+ · **License:** MIT · **Smoke Tests:** 9/9

The most significant Hermes companion project discovered this month. Hermespace adds a **persistent, append-only world model** beside Hermes Agent — an archive that never prunes, never decays, never caps. Every session, belief, landmark, and evolution is recorded. The agent builds a deepening model of itself across sessions.

**Core capabilities:**

| Capability | What It Does |
|-----------|-------------|
| **Workbench** | Limited FOA (≤4), park stack, load-aware receive_order, monotropic goal focus |
| **Dual Decode** | Short human `report` vs dense model `context` — never dump inject to chat |
| **Fabric** | Ranks `$HERMES_HOME/skills` + injects MEMORY/USER excerpts for current goal |
| **Plugin** | `on_session_start` / `pre_llm_call` / `on_session_end` broadcast when desk ready |
| **Study DB** | Turns stored under `~/.hermespace` — local, not Hermes session DB |
| **Desktop Plugin** | Right-rail pane for the Hermes desktop app |

**Design honesty (from the author):**
- "Like Claude J-space" — **Role only** — limited workspace *outside* weights. No activation access.
- "Consciousness / brain scan" — **No.** Harness cognition + optional local embeddings.
- "Replaces Hermes skills/memory" — **No.** Ranks and injects them.
- "Official Nous module" — **No.** Community companion; feedback welcome.

**Integration surface:**
- **Plugin:** `hermes_plugin/` → `$HERMES_HOME/plugins/hermespace`
- **Skill:** `skills/hermespace/` → `$HERMES_HOME/skills/hermespace`
- **Python:** `hermespace.agent_api`, `hermespace.Workbench`
- **CLI:** `scripts/hs` for turn-based interaction
- **Smoke:** `scripts/smoke_test.sh` (expect 9/9)

**Why it matters for Hermes:** As agents accumulate context across sessions, they lose focus — too many goals, dumping model context into chat, wrong skill for the job. Hermespace provides the bounded working memory that lets an agent focus on one goal while preserving everything else. The dual decode pattern (separate channels for human vs model) prevents the context pollution that degrades agent performance over long sessions. For CorpusIQ's multi-session growth operations, hermespace could reduce the "what was I working on?" amnesia that costs hours per session.

**Setup Guide:** [Hermespace — Full Setup Guide](/hermes/skills/catalog/hermespace-setup/)

```bash
# Clone and install
git clone https://github.com/PabloTheThinker/hermespace.git
cd hermespace
./scripts/install_hermes.sh
./scripts/smoke_test.sh    # expect 9/9

# Or via npx
npx skills add PabloTheThinker/hermespace --skill hermespace -g -y
```

---

### Billing & Spend — plutus (2★)

**Repo:** [Perseus-Computing-LLC/plutus](https://github.com/Perseus-Computing-LLC/plutus)
**Install:** `pip install plutus-agent`
**Language:** Python · **License:** MIT · **Tags:** `hermes-agent`, `cost-tracking`, `credit-monitoring`

Named for the Greek god of wealth. Plutus is a self-hosted, Stripe-integrated usage metering and prepaid-credit billing layer for LLM/agent spend. Drop it into your agent, see every call's cost live, and bill against prepaid credit.

**Four things in one (no OSS tool does all four together):**
- **Live balance monitoring** — real per-provider balances fused with your ledger
- **Ledger spend** — append-only, integer-micro-dollar credit ledger
- **Self-calibrating budgets** — back-solve a budget from real balance vs. spend
- **Runway routing** — shift your flagship model to the provider with the most days left

```bash
pip install plutus-agent
plutus demo    # zero-setup tour → http://localhost:8420
```

**Why it matters for Hermes:** With multi-model routing (DeepSeek, Anthropic, OpenAI, Grok) becoming standard for Hermes agents, tracking per-provider spend and routing by runway becomes critical. Plutus meters without proxying — it complements existing gateways rather than replacing them.

---

### Coding Delegation — hermes-cursor-dispatcher (1★) ⭐ Setup Guide Available

**Repo:** [matdev83/hermes-cursor-dispatcher](https://github.com/matdev83/hermes-cursor-dispatcher)
**Install:** `npx skills add matdev83/hermes-cursor-dispatcher --skill cursor-delegate -g -y`
**Created:** July 19, 2026 · **Language:** Python · **License:** MIT

**Brand new — created today.** A skill for Hermes Agent that safely delegates repository-level coding, debugging, refactoring, or implementation work to Cursor CLI. Uses isolated Git worktrees, validates independently before acceptance, and integrates natively with Grok models.

**Safety design:**
- **Stdin transport** — Exact UTF-8 prompts through a Python wrapper, no shell interpretation
- **Isolated worktrees** — Implementation in detached Git worktrees, never on dirty repos
- **Structured capture** — Bounded log tails, timeout, isolated process group
- **Hermes owns acceptance** — Diff review, independent tests, corrective iterations

**Workflow:** Inspect → Workspace selection → Prompt file → Invoke wrapper → Result capture → Diff review → Independent tests → Accept/Reject

**Why it matters for Hermes:** As the agent skills ecosystem grows, delegating heavy coding work to specialized CLI agents (Cursor, Codex, Claude Code) becomes essential. This skill provides the safety layer — isolated worktrees, output bounds, and explicit Hermes-owns-acceptance — that prevents autonomous coding agents from making unsupervised changes.

**Setup Guide:** [Cursor Delegate — Full Setup Guide](/hermes/skills/catalog/hermes-cursor-dispatcher-setup/)

```bash
npx skills add matdev83/hermes-cursor-dispatcher --skill cursor-delegate -g -y
```

---

### Craft Workshop — daidala (0★)

**Repo:** [forgegod/daidala](https://github.com/forgegod/daidala)
**Install:** Manual (Hermes plugin — `plugin.yaml`)
**Language:** Python · **License:** MIT · **Tags:** `hermes-agent`

A Hermes-native AI workshop that moves skill-backed work through interchangeable workflow packs and one explicit human approval gate — without introducing a second orchestration server. Named for the Ancient Greek word for skillfully crafted works.

**Core design:**
- **Workflow packs** — Map skills onto define → plan → implement → verify → review → deliver
- **Provenance** — Pins external skill sources, revisions, and directory digests
- **Approval integrity** — Human authorization bound to SHA-256 digest of plan revision
- **Git safety** — Rejects dirty targets, implements in Daidala-owned detached worktree
- **Plugin-based** — Loads in-process as a Hermes plugin, no MCP/HTTP server needed

**Why it matters for Hermes:** For operators who want structured, human-approved workflows around their agent work — especially in production environments where unsupervised changes are unacceptable. Complements hermespace's focus management with governance guardrails.

---

## Discovery Method

GitHub API search for repos tagged `hermes-agent` pushed since July 18, 2026. 165 repos surfaced across the `topic:hermes-agent` query. Cross-referenced against all 55+ prior marketplace discovery pages (June 9 — July 18, 2026) via `grep -rl` across the full `hermes/skills/` directory. 4 new repos confirmed absent from prior sweeps.

Additional repos found (deployment/configuration tools or tangential mentions — excluded from skill coverage):
- JasperKallfelz/hermes-x-jasper (starter kit, not a skill repo)
- jdvann/hermes-desktop-linux (prebuilt Electron app, not a skill)
- VantaSoft/vantasoft-hermes-plugins (empty beyond README)
- AxioRank/hermes-plugin (security gateway, early stage)
- Various VPS/deployment templates

---

*← [July 18](/hermes/skills/marketplace/new-july18-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
