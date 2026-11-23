---
title: Hermes Ershov Memory Engine Setup
description: Install and configure Ershov - a staged nightly memory engine for Hermes operators with reviewable proposals, artifact-first workflow, and 4 LLM backends
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-ershov-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes Ershov Memory Engine Setup

**Plugin:** self-ershov-memory (formerly hermes-ershov)
**Source:** [ersh123/self-ershov-memory](https://github.com/ersh123/self-ershov-memory)
**Stars:** 3 ⭐ | **License:** MIT | **Created:** June 19, 2026
**CI:** ✅ GitHub Actions (Python 3.11-3.13) | **Security:** ✅ CodeQL + OpenSSF Scorecard

## 1. What It Is

A self-audit memory engine. It reads Hermes dialogue history from `~/.hermes/state.db`, extracts durable operator corrections, snapshots memory files, and updates `USER.md` / `MEMORY.md` only through explicit, reviewable runs. Nothing is silently rewritten.

**Key design principles:**
- **Grounded:** durable memory comes from dialogue evidence, not fabricated assumptions
- **Idempotent:** repeat runs skip corrections already known
- **Safe by default:** `--dry-run` is the default mode; `--execute` is explicit
- **Auditable:** a snapshot before every write, plus an Error Bank for repeated failures

**How it works:**

```
~/.hermes/state.db dialogs
  -> correction / rule extraction
  -> Error Bank extraction for fixed compiler/runtime/test failures
  -> controlled context checkpoint / rebuild sidecar
  -> topic classification + dedup
  -> snapshot before write
  -> USER.md / MEMORY.md / error-bank / context / skill updates
```

The project was renamed from `hermes-ershov` to `self-ershov-memory`, and the maintainer removed the legacy staged-memory command surface (`review`, `inspect`, `approve`, `apply`, `revert`) from the public package. What ships now is one CLI with a dry-run / execute loop.

## 2. Prerequisites

- Hermes Agent installed (plugin system supported)
- Python 3.11, 3.12, or 3.13 - the versions the project's CI gates on
- DeepSeek reachable as the LLM fallback path (direct `deepseek` is the provider policy)
- Git (for install)
- Disk space: small - the plugin, the `USER.md` / `MEMORY.md` snapshots, and the `~/.hermes/context` store

## 3. Installation

### Plugin Install (Recommended)

```bash
hermes plugins install ersh123/self-ershov-memory --enable
```

### Local Development Install

Clone into the profile's plugins directory, then register that checkout so updates are tracked:

```bash
git clone https://github.com/ersh123/self-ershov-memory.git "$HERMES_HOME/plugins/self-ershov-memory"
hermes plugins adopt self-ershov-memory
```

### Verify Installation

```bash
hermes plugins list | grep -i ershov
self-ershov-memory --help
```

### Configure the LLM Backend

The provider policy is direct DeepSeek. Set the key in the environment Hermes runs in:

```bash
export DEEPSEEK_API_KEY="your-key"
```

## 4. Capabilities

| Feature | Description |
|---------|-------------|
| Audit pass | Extract corrections from recent dialogues; `--dry-run` shows the delta, `--execute` applies it |
| Error Bank | File-backed entries keyed `error_bank/<language>/<code>`, so repeat failures consolidate instead of flooding memory |
| checkpoints | MiMo-style `checkpoint.md` plus budgeted rebuild packets under `~/.hermes/context` |
| rebuild | Rebuild a session's context packet inside a token budget |
| fts-index / fts-search | Local Markdown FTS5 index over the context store |
| Snapshots | Memory files are copied before any write |
| Validation | Size checks on memory files; no secret values in logs or doctor output |

## 5. CLI Reference

```bash
# Inspect proposed changes (nothing is written)
self-ershov-memory --dry-run --quick

# Full 30-day pass - still dry-run unless --execute is present
self-ershov-memory --dry-run --full

# Apply after review
self-ershov-memory --execute --full

# Controlled context rebuild sidecar
self-ershov-memory checkpoint --session <session-id>
self-ershov-memory rebuild --session <session-id> --budget 48000

# Local context index
self-ershov-memory fts-index
self-ershov-memory fts-search "checkpoint"
```

## 6. CorpusIQ Use Cases

**For the CorpusIQ growth agent profile.** The profile flag is `-p` (`hermes -p <profile> <command>`); `--profile` is not a flag.

```bash
# Install for the corpusiq profile
hermes -p corpusiq plugins install ersh123/self-ershov-memory --enable

# Nightly dry-run audit against CorpusIQ sessions
self-ershov-memory --dry-run --full

# Apply the reviewed corrections
self-ershov-memory --execute --full
```

**CorpusIQ-specific config:**

```bash
# In the environment of the profile's process
export DEEPSEEK_API_KEY="your-key"
```

**Integration with CorpusIQ's existing memory stack:**
- Ershov complements (doesn't replace) the Hermes `memory` tool and the Sibyl provider
- Use Ershov for: cross-session correction extraction, cleanup of stale memories, quality audits
- Keep Hermes `memory` for: session-level facts, user preferences, quick saves
- Ershov's snapshots act as a changelog for the memory layer - pairs well with Honcho's peer context

**Cron job for nightly review:**

```bash
# Add to crontab: run at 3 AM Arizona daily. Dry-run by default; review before adding --execute.
0 3 * * * self-ershov-memory --dry-run --full >> ~/.hermes/logs/ershov-audit.log 2>&1
```

## 7. Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `hermes plugins install` fails | Git not installed | `apt-get install git` / `brew install git` |
| No changes proposed | `--execute` missing, or nothing new in the window | Run `--dry-run --full` and read the delta; widen the window |
| LLM provider error | DeepSeek key missing or rejected | Check `DEEPSEEK_API_KEY` in the process environment |
| Memory file rejected | Size validation failed | Trim the file; the previous run's snapshot is still in place |
| `review` / `apply` commands missing | Staged command surface removed upstream | Use the `--dry-run` / `--execute` loop above |
| High token costs | Expensive model in the fallback path | Keep direct `deepseek`; use `--quick` for routine passes |

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
