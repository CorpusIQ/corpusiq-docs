---
title: Hermes Skill Router Plugin — Setup Guide
description: Zero-VRAM semantic skill router for Hermes Agent. Auto-loads the correct SKILL.md before every LLM turn using Semantic Router (Ollama + Qdrant). 66 routes, ~17ms, self-improving.
category: skills
subcategory: setup
skill_name: hermes-skill-router-plugin
author: freyandere
last_updated: 2026-06-21
hermes_version: any (plugin system)
---

# Hermes Skill Router Plugin — Setup Guide

**Plugin:** [freyandere/hermes-skill-router-plugin](https://github.com/freyandere/hermes-skill-router-plugin)
**What it does:** A zero-VRAM semantic skill router that auto-loads the correct SKILL.md before every LLM turn. Uses Semantic Router (Ollama + Qdrant) for 17ms routing across 66 routes. Bilingual (RU+EN), self-improving, fail-safe.

> Why have the LLM figure out which skill to load when a 17ms vector search can do it perfectly?

---

## Quick Install

### 1. Install the Python dependency

```bash
pip install "semantic-router[qdrant,ollama]"
```

### 2. Verify services are running

```bash
docker ps | grep qdrant          # Qdrant on :16333
ollama list | grep nomic-embed   # Ollama on :11435
```

If either is missing:

```bash
# Start Qdrant
docker run -d -p 16333:6333 qdrant/qdrant

# Pull embedding model
ollama pull nomic-embed-text
```

### 3. Install the Hermes plugin

```bash
hermes plugins install freyandere/hermes-skill-router-plugin/plugin/semantic-router-preloader
```

### 4. Sync skills to Qdrant

```bash
cd E:/1.Environment/semantic-router   # Or wherever the repo lives
python sync-routes.py --force
```

### 5. Enable and restart

```bash
hermes plugins enable semantic-router-preloader
# Restart Hermes for the plugin hook to activate
```

## Prerequisites

| Requirement | Minimum | Notes |
|-------------|---------|-------|
| Python | 3.9+ | For semantic-router package |
| Docker | any | For Qdrant (or use native Qdrant) |
| Ollama | any | With `nomic-embed-text` model pulled |
| RAM | ~500 MB | Qdrant + Ollama overhead |
| VRAM | Zero | All calls via HTTP — no GPU needed |
| Hermes | Plugin support | `hermes plugins install` must work |

## What You Get

### 17ms Routing Pipeline

```
User Query
  │
  ▼
OllamaEncoder(nomic-embed-text)  ─── 15ms, 384-dim embedding
  │
  ▼
QdrantIndex(collection="hermes-skill-router")  ─── 2ms, top_k=5
  │
  ▼
Threshold check (≥0.80)
  │
  ├── Hit  → RouteChoice(name="github") → load SKILL.md → inject into context
  │
  └── Miss → .route-misses.jsonl → improve-routes.py (cron daily 5:00)
```

### Integration Points

| Layer | Method | Description |
|-------|--------|-------------|
| Plugin | `pre_llm_call` hook | Auto-injects matching SKILL.md before every LLM turn |
| Script | `sync-routes.py` | Scans all SKILL.md → generates utterances → syncs to Qdrant |
| Cron | Every 6h | `sync-skill-routes` — incremental sync |
| Self-learn | Daily 5:00 | `improve-routes --apply --prune` — learns from misses |

### Core Scripts

#### sync-routes.py — Skill → Route Sync

Generates 8-15 utterances per skill from frontmatter descriptions and syncs to Qdrant.

```bash
python sync-routes.py                    # Incremental (only changed)
python sync-routes.py --force            # Full rebuild
python sync-routes.py --dry-run          # Preview only
python sync-routes.py --name github      # Single skill
```

**Utterance generation order:**
1. Domain-specific queries
2. Skill name + action variants (`use X`, `run X`)
3. Description rephrased as requests
4. Tag-derived phrases
5. Generic patterns

#### improve-routes.py — Self-Improvement

Analyses missed queries and suggests new utterances.

```bash
python improve-routes.py                  # Dry-run preview
python improve-routes.py --apply          # Apply + rebuild Qdrant
python improve-routes.py --prune          # Trim dead auto-generated utterances
python improve-routes.py --watch          # Continuous mode (every 5min)
```

**Safety limits:**
- Max 20 utterances per route
- Min score 0.50 to suggest, 0.65 to auto-apply
- `--force` restores canonical state

## Verification

Test the router after installation:

```python
from semantic_router import SemanticRouter, RouterConfig
from semantic_router.encoders import OllamaEncoder
from semantic_router.index.qdrant import QdrantIndex

encoder = OllamaEncoder(name="nomic-embed-text:latest", base_url="http://127.0.0.1:11435")
index = QdrantIndex(location="http://127.0.0.1:16333", index_name="hermes-skill-router")
config = RouterConfig.from_index(index, encoder_type="ollama", encoder_name="nomic-embed-text:latest")
router = SemanticRouter(encoder=encoder, routes=config.routes, index=index, top_k=5)
router.set_threshold(0.80)

for q in ["push changes to git", "show kanban board", "bring me coffee"]:
    r = router(q)
    print(f"{q:30s} → {str(r.name or 'None'):20s} (score: {r.similarity_score:.2f})")
```

Expected output: First two route to appropriate skills, third returns `None` (below threshold).

## Fail-Safe Behavior

The plugin is designed to degrade gracefully:

- **Qdrant down:** Plugin silently no-ops. Hermes continues without routing.
- **Ollama down:** Plugin silently no-ops. Hermes continues without routing.
- **Threshold miss:** No skill injected. LLM proceeds without context injection.
- **Route conflict:** Highest-scoring route wins (deterministic).

**Hermes never fails because the router is unavailable.** The plugin is a performance optimization, not a critical path.

## Error Recovery

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Plugin not injecting skills | Plugin not enabled | `hermes plugins enable semantic-router-preloader` |
| `ModuleNotFoundError` | Missing pip dep | `pip install "semantic-router[qdrant,ollama]"` |
| Qdrant connection refused | Docker not running | `docker start qdrant` |
| Ollama connection refused | Ollama not running | `ollama serve` |
| All routes score below threshold | Skills not synced | `python sync-routes.py --force` |
| Empty route-misses.jsonl | Self-learning not needed yet | Wait. The plugin needs ~100 queries to build a meaningful miss log. |

## When NOT to Use

- You have fewer than 10 skills installed (manual skill loading is fine)
- Your Hermes instance runs on extremely constrained hardware (Qdrant + Ollama need ~500MB RAM)
- You always explicitly specify which skill to use (the router adds no value)

## Why This Matters

As your Hermes skill library grows beyond 20-30 skills, the LLM's ability to correctly identify which skill to load degrades. Every token spent on "should I load this skill?" is a token not spent on the actual task. This plugin:

1. **Cuts routing time** from LLM thinking (seconds) to vector search (17ms)
2. **Improves accuracy** — 13/13 correct on calibrated test set vs LLM hit-or-miss
3. **Self-improves** — missed routes automatically generate better triggers
4. **Zero VRAM** — no GPU competition with your LLM
5. **Bilingual** — `nomic-embed-text` handles Russian and English naturally

---

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — community-curated agent skills. Discover more at [skills.sh](https://skills.sh).*
