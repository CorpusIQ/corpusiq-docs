---
title: Hermes Memory Stack — Memory OS Setup Guide
description: Install and configure Chukwuemeka001/hermes-memory-stack — a modular memory OS layer for Hermes Agent with semantic retrieval, auto-extraction, temporal versioning, and state.db remediation
---

# Hermes Memory Stack — Setup Guide

**Source:** [Chukwuemeka001/hermes-memory-stack](https://github.com/Chukwuemeka001/hermes-memory-stack)
**Stars:** 0 ⭐ | **License:** Apache-2.0
**Created:** June 24, 2026
**Category:** Agent Infrastructure / Memory Management
**Tests:** 228

---

## 1. What It Is

A modular memory OS layer for Hermes Agent that addresses the full memory lifecycle: semantic session retrieval, conservative auto-extraction, temporal versioning, and remediation for users with existing memory overload.

### Component Status

| Component | Status | Description |
|-----------|:------:|-------------|
| Semantic retrieval | ✅ Built + verified | Session search via semantic indexing |
| Auto-extraction | ✅ Built + verified | Conservative memory auto-extraction with intake gate |
| Temporal versioning | ✅ Built + verified | Version-tracked memory with migration support |
| Export installer | 🟡 Draft | One-command install via `install.sh` |
| Curator/dreaming maintenance | 🟡 Planned | Remediation plan only |
| **Remediation Area 1:** state.db | ✅ Built + tested | State database remediation (explicit-run only) |
| **Remediation Area 2:** MEMORY.md audit | ✅ Built + tested | Memory file audit (read-only) |
| **Remediation Area 3:** pointer rewrite | ✅ Built + tested | Memory pointer rewrite (dry-run/render only) |
| **Remediation Area 4:** temporal migration | ✅ Built + tested | Temporal memory migration (verify read-only; sync gated) |

---

## 2. Prerequisites

- Hermes Agent with existing memory (state.db, MEMORY.md)
- Python 3.8+

---

## 3. Installation

```bash
git clone https://github.com/Chukwuemeka001/hermes-memory-stack.git
cd hermes-memory-stack
bash install.sh
```

### Verify

```bash
# Check semantic index
python3 scripts/semantic_index.py --health

# Run memory audit (read-only, safe)
python3 scripts/memory_audit.py
```

---

## 4. Core Modules

### Semantic Retrieval (`scripts/semantic_index.py`)

Converts session history into searchable embeddings for natural-language recall. Run:

```bash
python3 scripts/semantic_query.py "what did we decide about the RAG architecture"
```

### Auto-Extraction (`scripts/memory_auto_extract*.py`)

Conservatively extracts durable facts from sessions and writes them to memory. Uses `hermes_memory_intake_gate.py` to prevent garbage extraction.

### Temporal Versioning (`scripts/temporal_memory.py`)

Tracks memory entries with timestamps and supports migration between versions:

```bash
python3 scripts/temporal_migrate.py --from v1 --to v2
```

### Remediation Tools

For users with existing memory that needs cleanup:

| Tool | Function | Safety |
|------|----------|:------:|
| `state_db_remediate.py` | Clean and optimize state.db | Explicit-run only |
| `memory_audit.py` | Audit MEMORY.md for issues | Read-only |
| `memory_rewrite.py` | Rewrite memory pointers | Dry-run/render only |
| `temporal_migrate_onboard.py` | Migrate to temporal memory | Verify read-only; sync gated |

---

## 5. CorpusIQ Use Cases

| Use Case | Application |
|----------|-------------|
| **Multi-agent memory sync** | Semantic retrieval across CorpusIQ's agent fleet |
| **Session knowledge extraction** | Auto-extract operator insights and bug reports from agent sessions |
| **Memory hygiene** | Audit and remediate bloated MEMORY.md files across agent profiles |
| **Temporal rollback** | Version-track agent memories for compliance and debugging |
| **Onboarding new agents** | Install memory stack on new agent profiles for consistent recall |

---

## 6. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Semantic index empty | Index not built | Run `scripts/semantic_reindex.sh` |
| Auto-extraction silent | Intake gate blocking | Check gate thresholds in `hermes_memory_intake_gate.py` |
| Migration fails | Schema version mismatch | Run `temporal_migrate.py` to align versions |
| Remediation tools won't run | Safety gates active | All remediation tools have explicit-run or dry-run safeties — review output before committing |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Evening Discovery](/hermes/skills/marketplace/new-june24-2026-evening/) →*
