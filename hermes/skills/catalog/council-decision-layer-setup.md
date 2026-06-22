---
title: Council Decision Layer — Hermes Skill Setup Guide
description: Install and configure the Council Decision Layer — structured decision-making for Hermes Agent with 5 proven frameworks. Stop ad-hoc architecture decisions. Curl-installable, zero dependencies.
category: skills
subcategory: setup
skill_name: council-decision-layer
author: varbees / Antharmaya Labs
last_updated: 2026-06-21
hermes_version: "0.16.0+"
---

# Council Decision Layer — Setup Guide

**Skill:** [varbees/council-decision-layer](https://github.com/varbees/council-decision-layer)
**What it does:** Replaces ad-hoc architecture and strategy decisions with 5 proven frameworks. A deterministic Python question engine logs every decision with rationale to SQLite so you can see WHY decisions were made, not just that they happened.

> "Stop making ad-hoc architecture and strategy decisions. Use proven frameworks — all through a curl-installable Hermes skill."

---

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/varbees/council-decision-layer/main/install.sh | bash
```

Then enable in Hermes:

```bash
hermes skills config          # Enable council-decision-layer
hermes tools enable council   # Enable the council toolset
```

Restart your Hermes session for changes to take effect.

## Prerequisites

| Requirement | Minimum | Notes |
|-------------|---------|-------|
| Hermes Agent | v0.16.0+ | Plugin support required |
| Python | 3.11+ | Stdlib only — no pip installs needed |
| Disk space | ~2 MB | Skill files + SQLite decision log |
| API keys | None | Fully deterministic, local-only |

**Zero external dependencies.** The question engine uses only Python stdlib. No API keys, no network calls, no telemetry. Everything runs locally.

## What You Get

### 5 Decision Patterns

| Pattern | When to Use | Source |
|---------|-------------|--------|
| `tradeoff_matrix` | Architecture choices (cloud vs self-host, monolith vs microservice) | DDIA Ch.1 |
| `failure_modes` | Pre-deployment risk assessment | DDIA Ch.9 |
| `end_to_end` | Data pipeline correctness verification | DDIA Ch.13 |
| `ethics_triage` | Before collecting/storing user data | DDIA Ch.14 + SAIF |
| `agentops_trajectory` | Multi-step agent task planning | Google Agent Guide §3 |

### Question Engine

The core is a ~600 LOC Python tool (stdlib-only) that:

1. Presents structured questions for each pattern
2. Logs every answer to a local SQLite database
3. Produces a decision summary with rationale
4. 85 component tests verify correctness with DB isolation
5. SQL injection hardened (LIKE escape)

### Decision Log

Every decision is recorded with:
- Pattern used
- Questions asked and answers given
- Rationale for the final choice
- Timestamp and session context
- Outcome tracking for later verification

## Verification

After installation, run the test suite to confirm everything works:

```bash
python3 -m pytest ~/.hermes/skills/council-decision-layer/tools/tests/ -v
```

Expected output: 85 tests passing, all green.

## File Structure

```
~/.hermes/skills/council-decision-layer/
├── SKILL.md                    # Hermes skill manifest
├── patterns/                   # 5 decision framework references
│   ├── tradeoff_matrix.md
│   ├── failure_modes.md
│   ├── end_to_end.md
│   ├── ethics_triage.md
│   └── agentops_trajectory.md
├── tools/
│   ├── question_engine.py      # Core engine (stdlib, ~600 LOC)
│   └── tests/
│       └── test_question_engine.py  # 85 tests
├── references/
│   └── source_mapping.md       # Book → pattern mapping
├── companion-skills/
│   └── privacy-ethics-checklist/  # Module D
├── install.sh
└── docs/
    └── decision-log-schema.md
```

## Usage Patterns

### Basic: Prompt Hermes to use a pattern

After installation, invoke any pattern by name:

```
"Use the tradeoff_matrix pattern to evaluate whether we should use
PostgreSQL or MongoDB for our new analytics service."
```

Hermes will:
1. Load the council-decision-layer skill
2. Run the question engine with the tradeoff_matrix pattern
3. Present structured questions about your specific context
4. Record your answers and generate a decision summary

### Intermediate: Pre-deployment risk check

```
"Before we deploy the new auth service, run the failure_modes
pattern to identify what could go wrong."
```

### Advanced: Ethics gate for new features

```
"We're adding user behavior tracking. Run ethics_triage before
we write any code."
```

## Error Recovery

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Skill not loading | Not enabled | `hermes skills config` → enable |
| `ModuleNotFoundError` | Wrong Python version | Requires Python 3.11+ |
| Tests fail on DB operations | Permission issue | Check `~/.hermes/skills/council-decision-layer/` is writable |
| Question engine hangs | Invalid pattern name | Verify pattern exists in `patterns/` directory |

## When NOT to Use

- Simple yes/no decisions (overkill — the patterns are for consequential choices)
- Decisions under extreme time pressure (the questions take thought)
- Purely personal preferences ("what should I eat for lunch")

## Why This Matters

Most AI agent users make architecture and strategy decisions ad-hoc. When things go wrong, there's no record of WHY the decision was made. The Council Decision Layer fixes this:

1. **Structured questioning** → forces systematic thinking
2. **Proven frameworks** → defaults to patterns from DDIA, not intuition
3. **Logged rationale** → traceable decisions for post-mortems
4. **Outcome verification** → learn which patterns produce better results

Built for solo founders running multi-agent councils. Powers the [Antharmaya Labs agent ecosystem](https://antharmaya.com/).

---

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — community-curated agent skills. Discover more at [skills.sh](https://skills.sh).*
