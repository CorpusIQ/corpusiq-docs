---
title: Blueprint Orchestration Setup Guide
description: Install and configure aawobdev/hermes-skills — a 12-skill multi-agent blueprint orchestration system for Hermes Agent. Architect interviews, cheap models execute.
---

# Blueprint Orchestration — Setup Guide

**Source:** [aawobdev/hermes-skills](https://github.com/aawobdev/hermes-skills)
**Skills:** 12 | **Author:** [Alistair](https://github.com/aawobdev)
**Hermes Version:** Any (skills are standard SKILL.md format)
**Last Updated:** June 22, 2026

## Overview

A complete multi-agent project orchestration system for Hermes Agent. An expensive thinking model (Architect) interviews you, produces a detailed blueprint, then cheap local models execute role-by-role under your supervision.

**Core philosophy:** *"The expensive model thinks. The cheap models do. You supervise."*

## Prerequisites

- **Hermes Agent** installed and configured
- **Ollama** (for local models) or **OpenRouter** API key (for cloud models)
- Git (for cloning)
- At least 24GB VRAM recommended for running multiple local models (see [model-routing](#model-routing))

## Quick Install

### Method 1: Hermes Tap (Recommended)

```bash
hermes skills tap add aawobdev/hermes-skills
```

Skills are immediately available. Update anytime:

```bash
hermes skills tap update aawobdev/hermes-skills
```

### Method 2: Manual Clone

```bash
git clone https://github.com/aawobdev/hermes-skills ~/hermes-skills
```

Add to `~/.hermes/config.yaml`:

```yaml
skills:
  external_dirs:
    - ~/hermes-skills/skills
```

## Skills Included

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| `blueprint-orchestration` | Full workflow orchestrator | Start any new project |
| `role-architect` | System design, blueprint production | Phase 0-1: Interview + Planning |
| `role-designer` | UI/UX visual design | Phase 2: When UI is needed |
| `role-developer` | Code execution, file creation | Phase 3: Build |
| `role-tester` | Verification, drift detection | Phase 4: After each dev phase |
| `role-devops` | CI/CD, release, rollback | Phase 5: Deployment |
| `role-researcher` | Evidence gathering, option comparison | Any phase needing research |
| `role-security-auditor` | Vulnerability review | Phase 6: Before release |
| `role-end-user` | UX simulation | Phase 7: User-facing review |
| `role-orchestrator` | Task sequencing, one-shot delegation | Phase 3-7: Execution coordination |
| `prompting-standards` | LLM best practices | Reference for all role authors |
| `model-routing` | Model roster + assignments | Setup: pick models for your hardware |

## Starting a Project

### In Hermes

```
/skill blueprint-orchestration

My project: I want to build a monitoring dashboard for my homelab.
```

### Manual (Paste & Relay)

1. Open a session with a strong thinking model (e.g., `qwen3.6-35b-a3b` via LM Studio, or Claude Sonnet)
2. Paste the content of `role-architect/SKILL.md`
3. Provide your project in one sentence
4. Answer the 15 interview areas
5. Wait for the blueprint
6. Execute each phase using the assigned model

## The Workflow

```
PHASE 0: Interview (Architect determines scope + roles)
    ↓
PHASE 1: Blueprint (Architect produces the full plan)
    ↓
PHASE 2: Design (Designer, if activated)
    ↓
PHASE 3: Build (Developer executes tasks)
    ↕
PHASE 4: Test (Tester after each dev phase)
    ↓
PHASE 5: Deploy (DevOps)
    ↓
PHASE 6: Security Audit
    ↓
PHASE 7: End-User review (if activated)
    ↓
PHASE 8: Closeout (Architect reviews, you sign off)

Any escalation → back to Architect
Human is the relay between all phases
```

## Model Routing

### Default Role-to-Model Assignments

| Role | Primary Model | Runtime | tok/s |
|------|---------------|---------|-------|
| Architect | `qwen3.6-35b-a3b` (Q4_K_M) | LM Studio | ~104 |
| Designer | `qwen3.6-35b-a3b` + `gemma4:26b` | Mixed | varies |
| Developer | `qwen3-coder-30b` (Q4_K_M) | LM Studio | ~135 |
| Tester | `gemma4:26b` (Q4_K_M) | Ollama | ~113 |
| DevOps | `qwen3-coder-30b` | LM Studio | ~135 |
| Researcher | `qwen3.6-35b-a3b` or Claude Sonnet | Mixed | varies |
| Security | `qwen3.6-35b-a3b` | LM Studio | ~104 |
| End-User | `gemma4:26b` | Ollama | ~113 |
| Orchestrator | `deepseek/deepseek-v4-flash` | OpenRouter | cloud |

### Routing Tiers

```
TIER 0 — Orchestrator (OpenRouter)
  → Task decomposition, cheap reasoning

TIER 1 — Local Ollama (all routine dev, FREE)
  → Architect, Developer, Tester, End-User

TIER 2 — OpenRouter Paid
  → CC-class: complex logic, multi-file refactors

TIER 3 — OpenRouter Free (rate-limited)
  → Free cloud fallback

TIER 4 — Claude Code CLI (separate subscription)
  → CC-class via Claude: Sonnet/Haiku/Opus
```

## Per-Project Setup

Each project needs a minimal `HERMES.md`:

```markdown
# HERMES.md (in project root)

## Orchestration
Uses global Hermes skills. Run `/skill blueprint-orchestration` to start.
Blueprint is at: [path/to/blueprint.md]

## Project-specific model overrides
- Developer: qwen3-coder-30b (override from global)

## Project context for Hermes
- [One paragraph: what this project is, its stack, key constraints]
```

## Customization

- **Role skills:** Edit `role-*/SKILL.md` in place — changes take effect immediately
- **Model assignments:** Edit `model-routing/SKILL.md`
- **Adding new roles:** Add a new `role-<name>/SKILL.md` file
- **Prompt standards:** Follow `prompting-standards/SKILL.md` Part A for blueprints, Part B for execution

## Architect Interview Areas (15)

The Architect covers these during Phase 0:

1. Vision & outcome
2. Scope & boundaries
3. Platforms & targets
4. Technical environment
5. Stack & hosting selection
6. Execution context
7. Model inventory & routing
8. Risk & rollback
9. Quality & verification
10. Non-functional requirements
11. Design requirements
12. Security posture (shift-left)
13. User-facing surface
14. Deployment & operations
15. Patterns & preferences

## Verification

After installation, verify skills are available:

```bash
# List installed skills
hermes skills list --marketplace | grep -E "blueprint|role-|model-routing|prompting"

# Load the main orchestrator
hermes chat
/skill blueprint-orchestration
```

Expected: The blueprint-orchestration skill loads and begins the Architect interview.

## Troubleshooting

### Skills not found
- Verify `external_dirs` path in `~/.hermes/config.yaml` is correct
- Check directory permissions: `ls -la ~/hermes-skills/skills/`
- Try re-installing: `hermes skills tap update aawobdev/hermes-skills`

### Local models not loading
- Check Ollama is running: `ollama list`
- Verify model names match `model-routing/SKILL.md`
- Pull missing models: `ollama pull qwen3-coder:30b`

### VRAM exhaustion
- Reduce concurrent loaded models
- Use smaller quants (Q3_K_M instead of Q4_K_M)
- Offload to OpenRouter for memory-heavy roles

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Blueprint Orchestration Marketplace Entry](/hermes/skills/marketplace/new-june22-2026-late/) →*

*Powered by CorpusIQ*
