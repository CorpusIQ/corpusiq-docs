---
title: RigorPilot Skills — AI Research & Paper Reproduction Setup Guide for Hermes Agents
description: Install llllllllama/rigorpilot-skills (2.6M combined installs) — 12 skills for AI research exploration, paper reproduction, code exploration, safe debugging, and ML training runs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rigorpilot-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# RigorPilot Skills — Setup Guide

**Source:** [lllllllama/rigorpilot-skills](https://www.skills.sh/lllllllama/rigorpilot-skills) (2.6M combined installs)
**GitHub:** [github.com/lllllllama/rigorpilot-skills](https://github.com/lllllllama/rigorpilot-skills)
**Category:** Research / ML Engineering
**First Seen:** August 12, 2026
**Quality Tier:** 🟡 Beta (high install volume, young publisher)

RigorPilot packages the full AI-research loop as twelve agent skills: explore a research area, resolve paper context, reproduce experiments, run training, and audit the result — all with safety-first debugging. Every skill carries ~234K installs, making this one of the highest-volume research clusters on skills.sh.

---

## Installation

```bash
# Install the full repo
npx skills add llllllllama/rigorpilot-skills

# Or install individually
npx skills add llllllllama/rigorpilot-skills --skill ai-research-explore
npx skills add llllllllama/rigorpilot-skills --skill paper-context-resolver
npx skills add llllllllama/rigorpilot-skills --skill safe-debug
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `ai-research-explore` | 235.2K | Systematic exploration of a research area |
| `analyze-project` | 234.8K | Project structure and goals analysis |
| `ai-research-reproduction` | 234.6K | Reproducing published AI research |
| `explore-code` | 234.5K | Codebase exploration for research repos |
| `paper-context-resolver` | 234.5K | Resolving paper references and context |
| `safe-debug` | 234.5K | Debugging without breaking experiments |
| `repo-intake-and-plan` | 234.5K | Intake a repo and produce an execution plan |
| `minimal-run-and-audit` | 234.4K | Minimal run + result audit loop |
| `run-train` | 234.4K | Training run execution |
| `env-and-assets-bootstrap` | 234.4K | Environment and dataset/asset setup |
| `explore-run` | 234.4K | Exploratory run management |
| `ai-paper-reproduction` | 0 | End-to-end paper reproduction (newest) |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| Python ML stack | PyTorch/HF ecosystem for the training-oriented skills |
| GPU access | For `run-train` and reproduction workloads (local or cloud) |
| Git | Repos under study are cloned locally |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Model evaluation research** | `ai-research-explore` + `paper-context-resolver` for surveying techniques before evals |
| **Agent skill upgrades** | `repo-intake-and-plan` + `explore-code` when assessing new tooling repos for the stack |
| **Safe experimentation** | `minimal-run-and-audit` + `safe-debug` pattern for local AI infrastructure work |

---

## Limitations / Verification

- Newest skill (`ai-paper-reproduction`) has zero installs — treat as alpha
- Verify install: `npx skills list | grep -E "research|rigor"` shows installed entries
- Training skills assume a working GPU environment; they orchestrate, they don't provision hardware

---

## Related

- [Research Paper Writing Pipeline Setup](/hermes/skills/catalog/research-paper-writing-setup/)
- [Grounded Citations Setup](/hermes/skills/catalog/grounded-citations-setup/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
