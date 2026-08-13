---
title: Mnemosyne Hermes Memory Providers — Local-First Agent Memory Setup Guide
description: Install and configure hermes-memory-providers from mnemosyne-oss/mnemosyne (2.3K stars) — replaces MEMORY.md/USER.md with SQLite vector + FTS5 hybrid search, 20 memory tools, and lifecycle hooks. 100% local.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mnemosyne-hermes-memory-providers-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Mnemosyne Hermes Memory Providers — Setup Guide

**Source:** [mnemosyne-oss/mnemosyne](https://skills.sh/mnemosyne-oss/mnemosyne/hermes-memory-providers)
**GitHub:** [github.com/mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) (2.3K⭐)
**Category:** Memory / Knowledge Infrastructure
**First Seen:** July 14, 2026
**Security:** Gen Agent Trust Hub Pass · Socket Pass · Snyk Pass

Mnemosyne is a local-first memory layer for AI agents. Deployed as a Hermes memory provider, it replaces the built-in MEMORY.md/USER.md flat-file system with SQLite-backed vector + FTS5 hybrid search, episodic consolidation, temporal knowledge graphs, and optional bidirectional sync.

**100% local. Zero cloud. Sub-millisecond recall.**

---

## Installation

```bash
npx skills add https://github.com/mnemosyne-oss/mnemosyne --skill hermes-memory-providers
```

The provider ships with its own SQLite storage engine; no external vector database or cloud account is required.

---

## What It Gives You

| Capability | Detail |
|---|---|
| System prompt injection | `# Mnemosyne Memory` context block in every prompt |
| Pre-turn prefetch | Relevant memories injected before each LLM call |
| Post-turn sync | Conversation turns auto-stored to episodic memory |
| 20 injected tools | remember, recall, sleep, triples, scratchpad, graph, sync, diagnostics, and more |
| 3 lifecycle hooks | `pre_llm_call`, `on_session_start`, `post_tool_call` |
| CLI | `hermes mnemosyne {stats|sleep|inspect|export|import|clear|version}` |

---

## CLI Reference

```bash
hermes mnemosyne stats     # memory counts, storage size, health
hermes mnemosyne inspect   # browse stored memories
hermes mnemosyne export    # portable JSON export
hermes mnemosyne import    # restore from export
hermes mnemosyne sleep     # consolidation cycle (vector re-index)
hermes mnemosyne clear     # wipe memory store
hermes mnemosyne version   # provider version
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| Hermes Agent | Current version with memory-provider support |
| Python 3.9+ | For the provider runtime |
| SQLite | Bundled with Python; no separate install |
| Disk space | Local-only storage; sized by memory volume |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Structured memory upgrade** | Replace flat MEMORY.md with queryable vector + FTS5 recall across agent sessions |
| **Episodic consolidation** | Auto-archive conversation turns; run `sleep` cycles to consolidate patterns |
| **Memory analytics** | `stats` and `graph` surface what the agent actually remembers and uses |
| **Portable backups** | `export`/`import` for agent migrations between machines |
| **Local-first compliance** | Zero-cloud memory for sensitive business data |

---

## Limitations / Verification

- Provider replaces MEMORY.md/USER.md — migrate existing memory files before enabling
- 4 installs on skills.sh; the repo (2.3K⭐) is established but the Hermes provider integration is new
- Verify: `hermes mnemosyne version` returns the provider version, and a fresh session shows the `# Mnemosyne Memory` context block

---

## Related

- [Discovery Page — Aug 12 OpenClaw Ecosystem Sweep](/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/)
- [Knowledge Architecture](/hermes/knowledge/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
