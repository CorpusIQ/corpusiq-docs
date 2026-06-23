---
title: New Hermes Skills  --  June 20-22, 2026
description: 15 newly discovered Hermes Agent repos  --  Hermes Bible (169-page community KB), Steroids Image Gen, Ershov Memory Engine, Obsidian integration bundles, P2P Agent Agency, and 9 new plugin stubs from jligato
---

# New Skills: June 20-22, 2026

**Discovered:** June 22, 2026 via GitHub API search
**New repos:** 15 | **Net-new (uncatalogued):** 6 substantive repos + 9 plugin stubs
**Date range:** June 19-22, 2026

The Hermes ecosystem continues its explosive growth. This sweep covers the weekend through Monday  --  15 new repos, including a 169-page community knowledge base, a production image generation provider, a staged memory engine with proper CI/CD, and the first Obsidian-integrated Hermes bundles.

---

## ⭐ Substantive Repos (6)

| # | Repo | Stars | Skills | Description |
|---|------|:-----:|:------:|-------------|
| 1 | `DeployFaith/hermes-bible-skill` | 4 ⭐ | 1 (+ bundles) | 169-page community knowledge base  --  25+ real-world flows, SOUL.md patterns, hidden features, intent-based routing |
| 2 | `eve-ai-dev/steroids-openai-image-gen` | 3 ⭐ | 1 plugin | Hermes image generation provider  --  OpenAI-compatible + Codex Auth paths, overrides `image_generate` tool schema |
| 3 | `ersh123/hermes-ershov` | 2 ⭐ | 1 plugin | Staged nightly memory engine  --  reviewable proposals, artifact-first workflow, 4 LLM backends, CI/CodeQL/Scorecard |
| 4 | `david-internal/hermes-obsidian-always-on-setup` | 9 ⭐ | 2 (+ scripts) | VPS + systemd + Obsidian Sync setup bundle from companion video |
| 5 | `david-internal/hermes-obsidian-self-organizing-vault` | 9 ⭐ | 1 | Obsidian vault curator skill + starter templates |
| 6 | `david-internal/hermes-obsidian-capture-and-proof` | 7 ⭐ | 2 | Telegram capture + sync doctor bundle |
| 7 | `david-internal/hermes-obsidian-giveaway-pack` | 11 ⭐ | 4 | All giveaway bundles from companion video |
| 8 | `DeployFaith/Hermes_Agency` | 0 ⭐ | 1 | P2P agent collaboration via AgentAnycast SDK  --  NAT-traversing, encrypted, decentralized |

---

## 🔬 Plugin Stubs  --  jligato Ecosystem (9 repos)

**Author:** jligato (@jligato)  --  created 9 Hermes Agent plugin repos on June 19, 2026. All 0 stars, no READMEs  --  consistent with early-stage scaffolding.

| # | Repo | Purpose |
|---|------|---------|
| 1 | `jligato/hermes-chronicle` | Chronicle plugin |
| 2 | `jligato/hermes-reminisce` | Reminisce plugin |
| 3 | `jligato/hermes-temporal-memory` | Temporal memory plugin |
| 4 | `jligato/hermes-core-patches` | Core patches plugin |
| 5 | `jligato/hermes-introspect` | Introspection plugin |
| 6 | `jligato/hermes-dyad-core` | Dyad core plugin |
| 7 | `jligato/hermes-prompt-refinement` | Prompt refinement plugin |
| 8 | `jligato/hermes-agent-memory` | Agent memory plugin |
| 9 | `jligato/hermes-working-memory` | Working memory plugin |

**Status:** ⚠️ All stubs  --  no READMEs, no SKILL.md files confirmed. Watch for future development. Not catalogued in setup guides until content materializes.

---

## Spotlight: Hermes Bible Skill

**Source:** [DeployFaith/hermes-bible-skill](https://github.com/DeployFaith/hermes-bible-skill)
**Stars:** 4 ⭐ | **License:** MIT | **Created:** June 21, 2026
**Author:** iamlukethedev (source: [hermesbible.com](https://www.hermesbible.com))

The largest community-built Hermes knowledge base outside official docs. 169 pages distilled into a single loadable skill with embedded routing tables, flows catalog, and reference files.

### What's Inside

| File | Content |
|------|---------|
| `SKILL.md` (11KB) | Main router  --  embedded knowledge, flows catalog, intent mappings, trigger keywords |
| `references/patterns.md` | SOUL.md templates, delegation patterns, kanban concepts, cron patterns |
| `references/flows-catalog.md` | 26 real-world flows with intent-based routing |
| `references/hidden-features.md` | 8 community-sourced hidden Hermes features |
| `references/index.md` | Full 169-page documentation index |
| `references/llms-full.md` | Sanitized full-corpus markdown export for offline/audit |
| `bundles/hermes-complete.yaml` | `/hermes-complete` slash-command loading both `hermes-agent` + `hermes-bible` |

### Installation

```bash
git clone https://github.com/DeployFaith/hermes-bible-skill.git
cd hermes-bible-skill
mkdir -p ~/.hermes/skills/hermes-bible
cp -r SKILL.md references ~/.hermes/skills/hermes-bible/
```

**Light install (SKILL.md only):**
```bash
hermes skills install https://raw.githubusercontent.com/DeployFaith/hermes-bible-skill/main/SKILL.md
```

**Setup Guide:** [hermes-bible-skill-setup.md](/hermes/skills/catalog/hermes-bible-skill-setup/)

---

## Spotlight: Steroids OpenAI Image Gen

**Source:** [eve-ai-dev/steroids-openai-image-gen](https://github.com/eve-ai-dev/steroids-openai-image-gen)
**Stars:** 3 ⭐ | **License:** MIT | **Created:** June 20, 2026

A proper Hermes **plugin** (not just a skill) that overrides Hermes' built-in `image_generate` tool to support two production paths:

1. **OpenAI-compatible**  --  any `/v1/images/generations` endpoint (OpenAI, reverse proxy, etc.)
2. **Codex Auth**  --  reuse Hermes' existing Codex/OpenAI OAuth token

Also exposes `image_generate_background` for slow/batch generations via Hermes' async delegation queue.

### Installation

```bash
cd "${HERMES_HOME:-$HOME/.hermes}/plugins"
git clone https://github.com/eve-ai-dev/steroids-openai-image-gen.git
hermes plugins enable steroids-openai-image-gen
```

**Setup Guide:** [steroids-openai-image-gen-setup.md](/hermes/skills/catalog/steroids-openai-image-gen-setup/)

---

## Spotlight: Hermes Ershov  --  Memory Engine

**Source:** [ersh123/hermes-ershov](https://github.com/ersh123/hermes-ershov)
**Stars:** 2 ⭐ | **License:** MIT | **Created:** June 19, 2026
**CI:** ✅ GitHub Actions | **Security:** ✅ CodeQL + Scorecard

A staged nightly memory engine that turns recent sessions into reviewable memory proposals  --  no silent live-memory mutation. Ships as a proper Hermes plugin with install via `hermes plugins install`.

### Key Features

- **Staged review loop:** inspect → diff → validate → approve/reject → apply → revert
- **Artifact-first:** JSONL proposals with full diffs before any memory write
- **Offline mode:** deterministic replays for demos and tests
- **4 LLM backends:** DeepSeek, OpenRouter, OpenAI-compatible, Ollama
- **Audit trail:** local run ledger + `ERSHOV.md` diary

### Installation

```bash
hermes plugins install ersh123/hermes-ershov --enable
hermes ershov review --help
```

**Setup Guide:** [hermes-ershov-setup.md](/hermes/skills/catalog/hermes-ershov-setup/)

---

## Hermes + Obsidian Bundles (4 repos)

**Author:** david-internal  --  companion bundles for the "Hermes + Obsidian" video series
**Total stars:** 36 across 4 repos

| Repo | Stars | What it does |
|------|:-----:|-------------|
| `hermes-obsidian-giveaway-pack` | 11 ⭐ | All giveaway bundles from the companion video |
| `hermes-obsidian-always-on-setup` | 9 ⭐ | VPS + systemd + Obsidian Sync setup  --  includes prerequisite checker, install script, troubleshooting |
| `hermes-obsidian-self-organizing-vault` | 9 ⭐ | Vault curator skill + starter templates for self-organizing vaults |
| `hermes-obsidian-capture-and-proof` | 7 ⭐ | Telegram capture workflow + sync doctor diagnostics |

These bundles solve the "always-on Hermes writing into the same Obsidian vault" problem  --  a common pain point for operators wanting persistent cross-device agent output.

---

## P2P Agent Agency

**Source:** [DeployFaith/Hermes_Agency](https://github.com/DeployFaith/Hermes_Agency)
**Stars:** 0 ⭐ | **Created:** June 22, 2026

Wraps the [AgentAnycast Python SDK](https://github.com/AgentAnycast/agentanycast-python) (Apache 2.0, PyPI: `agentanycast`)  --  P2P agent discovery and communication with encryption, NAT traversal, and decentralized routing. Created today (June 22)  --  early stage, worth watching for multi-agent CorpusIQ architectures.

---

## Summary

| Category | Count |
|----------|:-----:|
| Knowledge & Documentation | 1 (Hermes Bible) |
| Image Generation | 1 (Steroids) |
| Memory & Persistence | 1 (Ershov) |
| Integration Bundles | 4 (Obsidian) |
| Multi-Agent | 1 (Hermes Agency) |
| Plugin Stubs (watch) | 9 (jligato) |
| **Total repos** | **17** |
| **Substantive (catalogued)** | **6** |
| **New setup guides** | **3** |

---

*← [Previous Discovery](/hermes/skills/marketplace/new-june19-20-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
