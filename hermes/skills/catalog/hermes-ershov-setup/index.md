---
title: Hermes Ershov Memory Engine Setup
description: Install and configure Ershov  --  a staged nightly memory engine for Hermes operators with reviewable proposals, artifact-first workflow, and 4 LLM backends
---

# Hermes Ershov Memory Engine Setup

**Plugin:** hermes-ershov
**Source:** [ersh123/hermes-ershov](https://github.com/ersh123/hermes-ershov)
**Stars:** 2 ⭐ | **License:** MIT | **Created:** June 19, 2026
**CI:** ✅ GitHub Actions | **Security:** ✅ CodeQL + OpenSSF Scorecard

## 1. What It Is

A staged nightly memory engine that turns recent Hermes sessions into **reviewable memory proposals**  --  no silent live-memory mutation. Think of it as "Git for agent memory": inspect, diff, approve, apply, revert.

**Key design principles:**
- **Artifact-first:** Every proposal is a JSONL file with full diffs before any memory write
- **Human-in-the-loop:** No automated mutation of live memory  --  every change goes through review
- **Auditable:** Local run ledger + `ERSHOV.md` diary tracks every decision
- **Offline-capable:** Deterministic replays for demos and tests

**How it works (nightly loop):**

```
Recent Sessions → Analyze → Generate Proposals (JSONL)
                              ↓
                    Inspect → Diff → Validate
                              ↓
                   Approve → Apply → Verify
                   Reject  → Archive with reason
                              ↓
                   Write to ERSHOV.md diary
```

## 2. Prerequisites

- Hermes Agent installed (plugin system supported)
- At least one LLM backend configured (DeepSeek, OpenRouter, OpenAI-compatible, or Ollama)
- Git (for install)
- Disk space: ~50KB for plugin + ledger files

## 3. Installation

### Plugin Install (Recommended)

```bash
hermes plugins install ersh123/hermes-ershov --enable
```

### Local Development Install

```bash
hermes plugins install file:///path/to/hermes-ershov --enable
```

### Verify Installation

```bash
hermes plugins list | grep ershov
hermes ershov review --help
```

### Configure LLM Backend

Ershov supports 4 backends. Configure in `~/.hermes/config.yaml`:

```yaml
ershov:
  backend: deepseek           # deepseek | openrouter | openai-compatible | ollama
  model: deepseek-chat        # Model name for your chosen backend
  
  # Backend-specific configs (only one needed):
  deepseek:
    api_key_env: DEEPSEEK_API_KEY
    base_url: "https://api.deepseek.com/v1"
  
  openrouter:
    api_key_env: OPENROUTER_API_KEY
    base_url: "https://openrouter.ai/api/v1"
  
  openai_compatible:
    api_key_env: OPENAI_API_KEY
    base_url: "${OPENAI_BASE_URL}"
  
  ollama:
    base_url: "http://localhost:11434"
```

## 4. Capabilities

| Feature | Description |
|---------|-------------|
| `review` | Generate memory proposals from recent sessions |
| `inspect` | View a proposal's full diff |
| `validate` | Validate proposals against memory constraints |
| `approve` | Approve a proposal for application |
| `reject` | Reject with reason, archived for audit |
| `apply` | Apply an approved proposal to live memory |
| `revert` | Roll back an applied proposal |
| `ledger` | View local run history |
| `diary` | Read/write ERSHOV.md audit trail |
| `offline` | Run with `--offline` for deterministic replay |

## 5. CLI Reference

```bash
# Nightly review cycle
hermes ershov review                    # Generate proposals
hermes ershov review --list             # List pending proposals
hermes ershov inspect <proposal-id>     # View full diff
hermes ershov validate <proposal-id>    # Validate against constraints
hermes ershov approve <proposal-id>     # Approve for application
hermes ershov reject <proposal-id> --reason "factually incorrect"
hermes ershov apply <proposal-id>       # Write to live memory

# Rollback
hermes ershov revert <proposal-id>      # Undo an applied proposal

# Audit
hermes ershov ledger                    # View run history
hermes ershov ledger --since 7d         # Last 7 days
hermes ershov diary                     # Read ERSHOV.md

# Offline mode
hermes ershov review --offline          # Deterministic replay
```

## 6. CorpusIQ Use Cases

**For the CorpusIQ growth agent profile:**

```bash
# Install for corpusiq profile
hermes --profile corpusiq plugins install ersh123/hermes-ershov --enable

# Run nightly review on CorpusIQ sessions
hermes --profile corpusiq ershov review --since 24h

# Inspect proposals about growth strategy
hermes --profile corpusiq ershov inspect <id>

# Approve high-quality memory proposals
hermes --profile corpusiq ershov approve <id>
hermes --profile corpusiq ershov apply <id>
```

**CorpusIQ-specific config:**

```yaml
# In ~/.hermes/profiles/corpusiq/config.yaml
ershov:
  backend: deepseek
  model: deepseek-chat
  deepseek:
    api_key_env: DEEPSEEK_API_KEY
    base_url: "https://api.deepseek.com/v1"
```

**Integration with CorpusIQ's existing memory stack:**
- Ershov complements (doesn't replace) Hermes' built-in `memory` tool
- Use Ershov for: cross-session pattern detection, cleanup of stale memories, quality audits
- Keep Hermes `memory` for: session-level facts, user preferences, quick saves
- Ershov diary serves as a changelog for the memory layer  --  pairs well with Honcho's peer context

**Cron job for nightly review:**

```bash
# Add to crontab: run at 3 AM Arizona daily
0 3 * * * hermes --profile corpusiq ershov review --since 24h >> ~/.hermes/profiles/corpusiq/logs/ershov.log 2>&1
```

## 7. Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `hermes plugins install` fails | Git not installed | `apt-get install git` / `brew install git` |
| `review` produces 0 proposals | No sessions in window | Check `--since` window; run a session first |
| LLM backend connection refused | Wrong base URL or API key | Verify env vars; test with `curl $base_url/models` |
| `apply` fails silently | Proposal conflicts with live memory | Inspect diff first; resolve conflict manually |
| High token costs | Using expensive model for proposal gen | Switch backend to DeepSeek or Ollama |
| Offline mode produces different results | Non-deterministic backend configured | Use `--model` override with a deterministic temp |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
