---
title: "New Hermes Skill Repo"
description: "12 newly discovered Hermes Agent skills from aawobdev/hermes-skills  --  a complete multi-agent blueprint orchestration system: Architect, Developer, Tester, Designer, DevOps, Security Auditor, End-User, Researcher, Orchestrator, Model Routing, Prompting Standards"
---

# New Skills: June 22, 2026 (Late Sweep)  --  aawobdev/hermes-skills

**Discovered:** June 22, 2026 via GitHub search + skills.sh
**New repo:** 1 | **Net-new skills:** 12
**Repo:** [aawobdev/hermes-skills](https://github.com/aawobdev/hermes-skills)

A complete multi-agent blueprint orchestration system that splits work across 9 specialized roles  --  an expensive thinking model produces a detailed blueprint, then cheap local models execute under human supervision.

---

## ⭐ aawobdev/hermes-skills  --  Blueprint Orchestration

**Stars:** 0 ⭐ | **License:** Not specified | **Created:** May 27, 2026
**Author:** [Alistair (aawobdev)](https://github.com/aawobdev)
**Languages:** Python 86.9%, Shell 13.1%
**Commits:** 83 | **Status:** Actively maintained (latest commit: June 22, 2026)

### Core Philosophy

> *"The expensive model thinks. The cheap models do. You supervise."*

A frontier thinking model acts as **Architect**  --  it interviews you, makes all design decisions, and produces a detailed blueprint. Cheap local models then execute the blueprint role-by-role. Roles never talk directly  --  you are the relay.

> *"If the blueprint is thorough enough, you don't need a frontier model for every task. A blueprint that specifies exact file names, function signatures, and verification commands turns a $0.001/task local model into a reliable executor."*

---

## Skills Included (12)

| # | Skill | Role | Description |
|---|-------|------|-------------|
| 1 | `blueprint-orchestration` | Entry Point | Full workflow: interview → blueprint → one-shot execution. **Start here.** |
| 2 | `role-architect` | Architect | System prompt: interviews, designs, produces blueprints, patches specs |
| 3 | `role-designer` | Designer | System prompt: visual decisions, UI layouts, interaction patterns |
| 4 | `role-developer` | Developer | System prompt: executes build tasks, writes code, never decides |
| 5 | `role-tester` | Tester | System prompt: adversarially verifies output against the spec |
| 6 | `role-devops` | DevOps | System prompt: CI/CD, environments, release, rollback, observability |
| 7 | `role-researcher` | Researcher | System prompt: gathers evidence, compares options, produces reports |
| 8 | `role-security-auditor` | Security | System prompt: vulnerability review, credentials, attack surface |
| 9 | `role-end-user` | End-User | System prompt: simulates real user to find UX gaps |
| 10 | `role-orchestrator` | Orchestrator | System prompt: sequences tasks, delegates via one-shot commands |
| 11 | `prompting-standards` | Standards | LLM/prompt best practices for authoring + executing blueprints |
| 12 | `model-routing` | Routing | Model roster, VRAM constraints, role-to-model assignments (Ollama + OpenRouter + Claude Code) |

---

## The Workflow

```
You → Architect (thinking model) → Blueprint
         ↑                              ↓
    Researcher                 ┌─────────────────────────┐
  (evidence reports)           │ Developer (cheap model)  │ ← executes tasks
                               │ Tester (mid model)       │ ← validates output
                               │ Security (thinking model)│ ← reviews for risks
                               │ End-User (any model)     │ ← simulates usage
                               └─────────────────────────┘
                                           ↓
                                   You sign off
```

**Phases:** 0: Interview → 1: Blueprint → 2: Design → 3: Build → 4: Test → 5: Deploy → 6: Security Audit → 7: End-User Review → 8: Closeout

Any escalation goes back to Architect. Human is the relay between all phases.

---

## Why This Matters for Hermes Operators

This is the **first community blueprint orchestration system** we've discovered for Hermes Agent. It addresses a core pain point: how to structure multi-agent projects without a single omnipotent prompt. Key innovations:

- **Model routing by tier**  --  TIER 0 (OpenRouter Orchestrator) → TIER 1 (local Ollama for routine dev) → TIER 2 (OpenRouter paid for complex tasks) → TIER 3 (OpenRouter free tier) → TIER 4 (Claude Code CLI). Role-appropriate model assignment based on task complexity.
- **Self-contained blueprints**  --  Each role receives only its task section + role card. Zero context leaking between roles.
- **STATUS.md tracking**  --  Every task starts as `⬜ Todo`, progresses through `🟦 In Progress` → `✅ Done` → `❌ Failed`. Live progress, not a static plan.
- **Escalation protocol**  --  Roles escalate to Architect (via human relay) when stuck, confused, or the spec is ambiguous. No silent drift.
- **Local-first, cloud-fallback**  --  Uses local Ollama models by default (free, private), falls back to OpenRouter only for reasoning-heavy tasks.

---

## Installation

### Option A  --  Hermes Tap (recommended)

```bash
hermes skills tap add aawobdev/hermes-skills
```

Skills are immediately available. Update anytime:

```bash
hermes skills tap update aawobdev/hermes-skills
```

### Option B  --  Manual Clone

```bash
git clone https://github.com/aawobdev/hermes-skills ~/hermes-skills
```

Then in `~/.hermes/config.yaml`:

```yaml
skills:
  external_dirs:
    - ~/hermes-skills/skills
```

### To Start a Project

```
/skill blueprint-orchestration

My project: I want to [one sentence description]
```

---

## Model Defaults

| Role | Primary Model | Runtime |
|------|---------------|---------|
| Architect | `qwen3.6-35b-a3b` | LM Studio |
| Designer | `qwen3.6-35b-a3b` (UX reasoning) + `gemma4:26b` (vision) + Claude Sonnet (creative) | Mixed |
| Developer | `qwen3-coder-30b` | LM Studio |
| Tester | `gemma4:26b` | Ollama |
| DevOps | `qwen3-coder-30b` | LM Studio |
| Researcher | `qwen3.6-35b-a3b` or Claude Sonnet | LM Studio / Claude |
| Security | `qwen3.6-35b-a3b` | LM Studio |
| End-User | `gemma4:26b` | Ollama |
| Orchestrator | `deepseek/deepseek-v4-flash` | OpenRouter |

Full model roster (24 models across Ollama + OpenRouter + Claude Code CLI) is documented in `model-routing`.

---

## Summary

| Metric | Value |
|--------|:-----:|
| New repos | 1 |
| New skills | 12 |
| Skill categories | Orchestration, Roles, Standards, Routing |
| First-of-kind | Multi-agent blueprint orchestration for Hermes |
| Setup guide | [blueprint-orchestration-setup.md](/hermes/skills/catalog/blueprint-orchestration-setup/) |

---

*← [Previous Discovery](/hermes/skills/marketplace/new-june20-22-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
