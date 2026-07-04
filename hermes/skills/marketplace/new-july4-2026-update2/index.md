---
title: "🆕 July 4, 2026 (Update 2) — Hermes Idea Workflow Suite + OpenClaw Tooling"
description: "6 new Hermes-relevant skills discovered in a July 4 late-evening sweep: akoliteza/hermes-agent-idea-workflow (4 skills, 235⭐), archieindian/openclaw-superpowers tool-description-optimizer, and heyvhuang/ship-faster tool-openclaw."
---

# 🆕 July 4, 2026 (Update 2) — 6 New Skills Across 3 Repos

Late-evening sweep of the skills.sh API (July 4, 2026) surfaced **6 new Hermes-relevant skills** across 3 repositories. The headline find is the complete **Hermes Agent Idea Workflow suite** by AkoliteZA — a 4-skill pipeline that turns rough ideas into design docs, UI briefs, and implementation plans.

## Summary

| # | Skill | Installs | Repo | Stars |
|---|-------|----------|------|-------|
| 1 | `idea-superpowers-suite` | 27 | `akoliteza/hermes-agent-idea-workflow` | 235 |
| 2 | `idea-to-implementation-doc` | 40 | `akoliteza/hermes-agent-idea-workflow` | 235 |
| 3 | `idea-to-design-doc` | 27 | `akoliteza/hermes-agent-idea-workflow` | 235 |
| 4 | `idea-to-ui-design-brief` | 28 | `akoliteza/hermes-agent-idea-workflow` | 235 |
| 5 | `tool-description-optimizer` | 24 | `archieindian/openclaw-superpowers` | 65 |
| 6 | `tool-openclaw` | 63 | `heyvhuang/ship-faster` | 337 |

---

## 🏆 Headline: Hermes Agent Idea Workflow Suite

**Repo:** [AkoliteZA/hermes-agent-idea-workflow](https://github.com/AkoliteZA/hermes-agent-idea-workflow)  
**Stars:** 235 · **Skills:** 4 · **Topics:** hermes-agent, skills, superpowers, workflow, ai-agents

A complete pre-build product/spec pipeline for Hermes Agent. These 4 skills form a sequential workflow that takes rough ideas all the way to build-ready implementation specs:

### Pipeline Flow

```
Rough Idea → idea-to-design-doc → idea-to-ui-design-brief → idea-to-implementation-doc
                  ↑                                                    ↑
                  └────── idea-superpowers-suite (orchestrator) ───────┘
```

### Individual Skills

| Skill | Description | Install |
|-------|-------------|---------|
| **idea-to-design-doc** | Turns rough ideas into focused product/design Markdown docs through guided questions — without jumping to implementation too early. Acts as the "idea filter" stage. | `npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-design-doc` |
| **idea-to-ui-design-brief** | Converts product/design docs into focused UI design briefs with optional AI image-generation concept prompts. Produces implementation-ready UI direction. | `npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-ui-design-brief` |
| **idea-to-implementation-doc** | Reviews design docs, researches similar products, and produces a separate technical implementation plan/roadmap. The final stage before coding. | `npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-implementation-doc` |
| **idea-superpowers-suite** | The orchestrator — runs the full workflow end-to-end: captures rough ideas, expands them into design/UI/implementation docs, researches competitors, and generates build-ready Markdown artifacts. | `npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-superpowers-suite` |

### Why This Matters

This is the first complete **idea-to-build pipeline** built specifically for Hermes Agent. The skills chain together: the orchestrator (`idea-superpowers-suite`) calls the individual stages in sequence. Each stage produces a structured Markdown artifact that feeds the next. For Hermes users building products, this turns the agent from a code assistant into a full product development partner.

**CorpusIQ Use Case:** Use `idea-superpowers-suite` to rapidly spec new features from user feedback and competitive research. The implementation doc output feeds directly into Hermes coding workflows.

---

## Tool Description Optimizer (OpenClaw)

**Repo:** [ArchieIndian/openclaw-superpowers](https://github.com/ArchieIndian/openclaw-superpowers)  
**Stars:** 65 · **New skill:** `tool-description-optimizer` (24 installs)

| Skill | Description |
|-------|-------------|
| **tool-description-optimizer** | Analyzes skill descriptions for trigger quality — scores clarity, keyword density, and specificity, then suggests rewrites that improve discovery accuracy. Useful for skill publishers who want their skills to surface correctly in agent searches. |

**Install:** `npx skills add archieindian/openclaw-superpowers --skill tool-description-optimizer`

**Note:** openclaw-superpowers contains 57 total skills. Most were catalogued in prior sweeps (June 18 batch, June 25, etc.). Only `tool-description-optimizer` is genuinely new to this sweep.

---

## Tool OpenClaw (Ship Faster / Voxyz AI)

**Repo:** [Heyvhuang/ship-faster](https://github.com/Heyvhuang/ship-faster)  
**Stars:** 337 · **New skill:** `tool-openclaw` (63 installs)

| Skill | Description |
|-------|-------------|
| **tool-openclaw** | A comprehensive OpenClaw knowledge base skill — bundles the full OpenClaw documentation (CLI reference, gateway config, providers, channels, plugins, security, deployment) as agent-accessible reference material. Lives in ship-faster's legacy skills directory. |

**Install:** `npx skills add heyvhuang/ship-faster --skill tool-openclaw`

**Note:** Ship Faster contains 36 agent packs by Voxyz AI across creator, developer, and growth categories. `tool-openclaw` is the only OpenClaw-specific skill in the collection. It's categorized as "legacy" in the repo but remains the most-installed OpenClaw skill on skills.sh (63 installs).

---

## Installation

```bash
# Full idea workflow suite (all 4 skills)
npx skills add akoliteza/hermes-agent-idea-workflow

# Or individual skills:
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-superpowers-suite
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-design-doc
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-implementation-doc
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-ui-design-brief

# OpenClaw tooling
npx skills add archieindian/openclaw-superpowers --skill tool-description-optimizer
npx skills add heyvhuang/ship-faster --skill tool-openclaw
```

---

*Discovered: July 4, 2026 · Source: skills.sh API (7 targeted queries) · Method: API sweep → cross-reference against 400+ existing pages*

*← [Previous Discovery](/hermes/skills/marketplace/new-july4-2026-update/) | [Marketplace Home](/hermes/skills/marketplace/) →*
