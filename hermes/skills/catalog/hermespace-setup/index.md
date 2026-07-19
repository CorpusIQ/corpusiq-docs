---
title: "Hermespace — Persistent Agent World Setup"
description: "Install and configure hermespace (PabloTheThinker/hermespace) for Hermes Agent — a persistent world model with limited working-memory desk, dual decode channels, skill fabric, and append-only archive."
---

# Hermespace Setup Guide

**Repo:** [PabloTheThinker/hermespace](https://github.com/PabloTheThinker/hermespace)
**Version:** v0.18.3
**Stars:** 46
**License:** MIT
**Skill:** `npx skills add PabloTheThinker/hermespace --skill hermespace -g -y`

## What It Is

Hermespace is a persistent, append-only world model that adds a limited working-memory desk beside Hermes Agent. It provides:

- **Workbench** — Focused attention of ≤4 items, park stack for deferred goals, monotropic goal focus
- **Dual Decode** — Separate channels: short human `report` vs dense model `context` (never dumps model context into chat)
- **Fabric** — Ranks `$HERMES_HOME/skills` and injects MEMORY/USER excerpts relevant to current goal
- **Plugin** — `on_session_start`, `pre_llm_call`, `on_session_end` hook broadcasts
- **Study DB** — Turn history stored under `~/.hermespace` (separate from Hermes session DB)
- **Desktop Plugin** — Right-rail pane for Hermes desktop app
- **World Model** — Append-only archive that never prunes, never decays, never caps

It does **not** replace Hermes tools, skills, memory, gateway, or the agent loop. It augments them.

## Prerequisites

- Python 3.10+
- Hermes Agent v0.17+ (v0.18+ recommended)
- Git
- pip or uv for Python package management

## Installation

### Method 1: npx skills (recommended)

```bash
npx skills add PabloTheThinker/hermespace --skill hermespace -g -y
```

This places the skill at `$HERMES_HOME/skills/hermespace/`.

### Method 2: Manual clone + install

```bash
git clone https://github.com/PabloTheThinker/hermespace.git
cd hermespace
./scripts/install_hermes.sh
```

The install script:
1. Installs the Python package (`pip install -e .`)
2. Symlinks `hermes_plugin/` → `$HERMES_HOME/plugins/hermespace`
3. Symlinks `skills/hermespace/` → `$HERMES_HOME/skills/hermespace`
4. Creates `~/.hermespace/` state directory

### Verify Installation

```bash
cd hermespace
./scripts/smoke_test.sh    # expect 9/9
```

```bash
# Python import check
python3 -c "from hermespace import Workbench; print('OK')"
```

## Configuration

### State directory

Default: `~/.hermespace/`

Override with environment variable:
```bash
export HERMESPACE_HOME=/custom/path
export ILO_HOME=/custom/path     # alternative name
```

### Plugin activation

If installed via `install_hermes.sh`, the plugin is symlinked. Verify:
```bash
ls -la $HERMES_HOME/plugins/hermespace/
```

The plugin broadcasts on three hooks:
- `on_session_start` — Desk initialization, fabric scan
- `pre_llm_call` — Inject ranked skills + memory
- `on_session_end` — Seal turn, update archive

### Skill loading

The skill (`hermespace`) should be loaded when:
- User says "hermespace", "pocket", "workbench", "FOA desk", "pulse", "viewport"
- Multi-step job needs monotropic focus + dual channel
- Ranking Hermes skills or injecting MEMORY for current goal
- Desktop Hermespace missing or right-rail only
- Access approve/deny, autonomy toggles, ops boot

## Usage

### Quick start — Workbench

```python
from hermespace import Workbench

wb = Workbench(agent_id="hermes", session_id="main")
wb.enter()
r = wb.receive_order("Audit the deployment pipeline", goal="Find bottlenecks", say="Starting audit...", force=True)

# r["user_reply"] → what the user sees
# r["model_context"] → dense context for the model (NOT shown to user)
```

### CLI turn interface

```bash
./scripts/hs turn -m "Analyze our current social posting cadence" --goal "Find gaps in our schedule" --say "On it"
```

### World Model (persistent archive)

```python
from hermespace import WorldModel

wm = WorldModel(agent_id="corpusiq-growth")
wm.enter()
wm.add_belief("Help-first content outperforms promotional", 0.85, source="six-month-data")
wm.add_landmark("Hit 5,000 monthly reach across platforms")
wm.set_trait("operations-minded")
wm.set_goal("Grow to 15% MoM", decision="A — increase Reddit presence", plan=["audit", "deploy", "measure"])
wm.evolve()  # consolidate, detect patterns
print(wm.render_markdown())
```

The archive lives at `~/.hermespace/worlds/corpusiq-growth_archive.jsonl` — an append-only JSONL file that grows forever.

### Focus of Attention (FOA)

The workbench enforces a bounded FOA:

| Limit | Default | Meaning |
|-------|---------|---------|
| FOA capacity | 4 | Active items in focus |
| Desk capacity | 12 | Items on desk (parked + active) |
| Monotropic goal | 1 | One active goal at a time |

When the desk is full, items are parked and can be recalled.

### Fabric — Skill ranking

The fabric scans `$HERMES_HOME/skills/` and ranks them by relevance to the current goal. It injects the top matches into the model context (not the user report):

```python
wb = Workbench()
wb.enter()
# Fabric auto-ranks on receive_order
r = wb.receive_order("Debug the gateway crash loop", goal="Fix gateway")
# The model sees ranked skills + relevant MEMORY excerpts
# The user only sees the report
```

## Architecture Decisions

### Dual Decode Pattern

This is the critical design insight: **never dump model context into the chat**. Hermespace provides two separate channels:

| Channel | Audience | Contents |
|---------|----------|----------|
| `report` | Human user | Concise summary, decision, next step |
| `context` | Model only | Ranked skills, memory, full plan, fabric output |

This prevents the context pollution where model-internal reasoning overwhelms the conversation.

### Append-Only Archive

The world model is an append-only JSONL — no pruning, no decay, no deletion. Every entry type (`enter`, `leave`, `landmark`, `belief`, `trait`, `evolution`, `focus`, `epoch_transition`, `resolve`, `relationship`) appends to the file.

Evolution is triggered explicitly (`wm.evolve()`) and handled by the library — consolidation, pattern detection, epoch checks.

## Pitfalls

1. **Not a replacement for Hermes memory** — Hermespace's archive is a companion, not a replacement for Hermes MEMORY, Sibyl, or GBrain. Use both.

2. **Not a second agent runtime** — Hermespace provides bounded working memory, not a second LLM. It does not make API calls or run tools.

3. **Desktop plugin requires Hermes desktop app** — The right-rail pane only works with the Hermes desktop app (Electron). On headless/SSH systems, use the Python API.

4. **Archive grows unbounded** — The JSONL file never prunes. For long-running agents (months/years), disk usage may become significant. Monitor `~/.hermespace/worlds/` size periodically.

5. **Python 3.10+ required** — Some type annotations and features require Python 3.10+. On older systems, upgrade Python first.

## Verification Checklist

- [ ] `pip install -e .` succeeds (or `npx skills add` succeeds)
- [ ] `./scripts/smoke_test.sh` returns 9/9
- [ ] `python3 -c "from hermespace import Workbench"` succeeds
- [ ] `~/.hermespace/` directory exists
- [ ] Plugin appears in `$HERMES_HOME/plugins/hermespace/`
- [ ] Skill appears in `$HERMES_HOME/skills/hermespace/`
- [ ] `wb = Workbench(agent_id="test"); wb.enter()` completes without error

## See Also

- [Official Repo](https://github.com/PabloTheThinker/hermespace)
- [FOR_HERMES.md](https://github.com/PabloTheThinker/hermespace/blob/main/FOR_HERMES.md) — maintainer notes
- [WORKFLOW.md](https://github.com/PabloTheThinker/hermespace/blob/main/WORKFLOW.md) — agent workflow design
- [Design docs](https://github.com/PabloTheThinker/hermespace/tree/main/docs) — concept research, workbench design

---

*Discovered July 19, 2026 · [Marketplace →](/hermes/skills/marketplace/new-july19-2026/)*
