---
title: New Skills — June 19, 2026 Update (ECC-Hermes 36-pack, SkillSpector Vetting, AgentMint)
description: 6 newly discovered Hermes skill repos — 36-skill ECC pack, NVIDIA SkillSpector vetting pipeline, AgentMint subagent routing, devops/scraping skills, SEO/WordPress marketing pack, and Herman's execution playbook.
---

# New Skills — June 19, 2026 Update

**Sources:** GitHub discovery, skills.sh
**Date:** June 19, 2026 (afternoon sweep)
**Total new:** 6 repos, ~60+ skills

The ecosystem continues accelerating. This afternoon sweep found six new repos published in the last 24 hours — including a 36-skill pack adapted for Hermes from the ECC framework, NVIDIA's SkillSpector vetting pipeline for Hermes, and a subagent routing bridge to AgentMint.

---

## Hermes Agent Ecosystem (6 new repos)

| # | Repo | Skills | Stars | Description |
|---|------|:------:|:-----:|-------------|
| 1 | `JingWang-Star996/ecc-hermes` | 36 | 2 ⭐ | ECC skills adapted for Hermes Agent & OpenClaw — universal AI coding agent skills |
| 2 | `SoCalStreet/skill-vetting` | 1 | — | Auto-vet external AI agent skills with NVIDIA SkillSpector before installation |
| 3 | `mesutcelik/agentmint-skills` | 2 | — | Route Hermes `delegate_task(background=True)` to named, persistent AgentMint subagents |
| 4 | `Puchen-ai/hermes-skills` | 9 | — | User-authored Hermes skills: devops, scrapers, cron, guidelines, monitoring |
| 5 | `RobinBeraud/hermes-skills` | 5+ | — | Community skills for Hermes: SEO audits, WordPress, Marketing automation |
| 6 | `darraappen2/herman-skill-playbook` | 8 | — | Hermes Agent skill playbook — 8 execution skills by Herman |

---

## Spotlight: ECC-Hermes (36 skills)

**Source:** [JingWang-Star996/ecc-hermes](https://github.com/JingWang-Star996/ecc-hermes)
**Stars:** 2 ⭐ | **License:** MIT | **Created:** June 18, 2026

The most substantial Hermes skill pack drop this week. 36 universal skills adapted from the ECC (Engineering Coding Companion) framework for both Hermes Agent and OpenClaw. Includes `install.sh` and `uninstall.sh` for one-command setup.

### Skill Categories

| Category | Skills | Examples |
|----------|:------:|----------|
| Agent Engineering | 6 | `agent-architecture-audit`, `agent-eval`, `agent-harness-construction`, `agent-introspection-debugging`, `agent-self-evaluation`, `agentic-engineering` |
| API & Integration | 3 | `api-connector-builder`, `api-design`, `api-integration-patterns` |
| Code Quality | 4 | `code-review-patterns`, `refactoring-workflows`, `testing-strategies`, `error-handling` |
| DevOps & Deploy | 4 | `ci-cd-pipeline`, `docker-automation`, `kubernetes-ops`, `infra-as-code` |
| Data & Storage | 3 | `database-migrations`, `data-pipeline`, `cache-strategies` |
| Security | 3 | `security-audit`, `dependency-scan`, `secret-management` |
| Documentation | 2 | `doc-generation`, `api-documentation` |
| Frontend | 3 | `component-builder`, `ui-testing`, `accessibility-audit` |
| Workflow | 4 | `git-workflows`, `release-management`, `incident-response`, `onboarding` |
| General | 4 | `file-operations`, `search-patterns`, `code-generation`, `context-management` |

### Installation

```bash
git clone https://github.com/JingWang-Star996/ecc-hermes.git
cd ecc-hermes
./install.sh   # Installs all 36 skills to ~/.hermes/skills/
```

Or install individual skills:

```bash
npx skills add JingWang-Star996/ecc-hermes --skill agent-architecture-audit
npx skills add JingWang-Star996/ecc-hermes --skill agent-eval
```

---

## Spotlight: Skill Vetting Pipeline (NVIDIA SkillSpector)

**Source:** [SoCalStreet/skill-vetting](https://github.com/SoCalStreet/skill-vetting)
**Author:** @_markstreeter | **License:** MIT | **Created:** June 19, 2026

A security-first skill that gates every external skill installation through NVIDIA's [SkillSpector](https://github.com/NVIDIA/skillspector) vulnerability scanner. Never install an untrusted skill without a risk assessment.

### Core Rule

> **Never install an external skill (from GitHub, a marketplace, or any external source) without first scanning it with SkillSpector.** This is non-negotiable.

### Pipeline

```
External skill → SkillSpector scan → Risk score → Gate check → Install or reject
```

Risk levels: `low` (auto-approve), `medium` (show findings, ask), `high` (reject, log), `critical` (block permanently).

### Installation

```bash
git clone https://github.com/SoCalStreet/skill-vetting.git
mkdir -p ~/.hermes/skills/skill-vetting
cp skill-vetting/SKILL.md ~/.hermes/skills/skill-vetting/
cp skill-vetting/catalog.json ~/.hermes/skills/skill-vetting/
```

---

## Spotlight: AgentMint Subagent Bridge

**Source:** [mesutcelik/agentmint-skills](https://github.com/mesutcelik/agentmint-skills)
**Created:** June 19, 2026

Routes Hermes `delegate_task(background=True)` calls to named, persistent AgentMint subagents instead of ephemeral child processes. Subagents survive parent context resets, accumulate long-term memory, and can be shared across agents.

### Key Difference

| Standard delegate_task | AgentMint delegate |
|------------------------|-------------------|
| Subagent dies with parent context | Subagent persists independently |
| No cross-agent sharing | Shared AgentMint worker pool |
| Ephemeral state | Long-term memory accumulation |
| Single-agent only | Multi-agent reuse |

### Installation

```bash
npx skills add mesutcelik/agentmint-skills --skill hermes-delegate-task
```

Requires AgentMint running locally. Start with:

```bash
agentmint serve --port 11435
```

---

## Additional Finds

### Puchen-ai/hermes-skills (9 skills)

[Puchen-ai/hermes-skills](https://github.com/Puchen-ai/hermes-skills) — 9 user-authored production skills: devops automation, web scrapers, cron job management, agent guidelines, and monitoring. Created June 18.

```bash
git clone https://github.com/Puchen-ai/hermes-skills.git
```

### RobinBeraud/hermes-skills (5+ skills)

[RobinBeraud/hermes-skills](https://github.com/RobinBeraud/hermes-skills) — Community skills for SEO audits, WordPress management, and Marketing automation. Created June 19.

```bash
git clone https://github.com/RobinBeraud/hermes-skills.git
```

### Herman's Skill Playbook (8 skills)

[darraappen2/herman-skill-playbook](https://github.com/darraappen2/herman-skill-playbook) — 8 execution-focused skills by Herman. Created June 19.

```bash
git clone https://github.com/darraappen2/herman-skill-playbook.git
```

---

## Installation Summary

```bash
# ECC-Hermes (36 skills — the big one)
git clone https://github.com/JingWang-Star996/ecc-hermes.git && cd ecc-hermes && ./install.sh

# Skill Vetting (NVIDIA SkillSpector)
git clone https://github.com/SoCalStreet/skill-vetting.git

# AgentMint Bridge
npx skills add mesutcelik/agentmint-skills --skill hermes-delegate-task

# DevOps & Scraping
git clone https://github.com/Puchen-ai/hermes-skills.git

# SEO & WordPress
git clone https://github.com/RobinBeraud/hermes-skills.git

# Herman's Playbook
git clone https://github.com/darraappen2/herman-skill-playbook.git
```

---

## Why This Matters

1. **ECC-Hermes is the largest single Hermes skill drop this week** — 36 skills from a proven framework. The install.sh/uninstall.sh pattern makes it trivial to try and remove. This nearly doubles the documented native Hermes skill count.

2. **SkillSpector vetting is a security necessity** — As the Hermes skill ecosystem grows past 400+ skills, automated vulnerability scanning before installation becomes critical. This skill enforces that at the agent level.

3. **AgentMint enables persistent subagents** — The `delegate_task` primitive is powerful but ephemeral. AgentMint bridges it to durable, named workers that survive context resets — a meaningful upgrade for long-running multi-agent workflows.

4. **Specialized domains filling in** — SEO/WordPress (RobinBeraud), devops/scraping (Puchen-ai), execution playbooks (Herman) — the ecosystem is diversifying beyond general-purpose coding into domain-specific automation.

---

## Catalog Updates

- **Marketplace index:** Updated with this page
- **Total documented marketplace repos:** 340 + 6 = 346+
- **Estimated new skills:** 60+

---

*← [June 19 Morning Batch](/hermes/skills/marketplace/new-june19-2026/) | [Skills Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Catalog Home](/hermes/skills/catalog/)*
*Powered by CorpusIQ*
