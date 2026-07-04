---
title: Hermes Agent Idea Workflow Suite — Setup Guide
description: Install and configure the complete idea-to-build pipeline for Hermes Agent. Turn rough ideas into design docs, UI briefs, and implementation plans with 4 chained skills from akoliteza/hermes-agent-idea-workflow (235⭐).
---

# Hermes Agent Idea Workflow Suite

**Repo:** [AkoliteZA/hermes-agent-idea-workflow](https://github.com/AkoliteZA/hermes-agent-idea-workflow)  
**Stars:** 235 · **Skills:** 4 · **Installs:** 27–40 each

The Idea Workflow Suite is a pre-build product/spec pipeline for Hermes Agent. Four skills chain together to turn rough ideas into design docs, UI briefs, and implementation plans — producing structured Markdown artifacts at each stage.

## Pipeline Overview

```
Rough Idea
    │
    ▼
┌─────────────────────┐
│ idea-to-design-doc  │  "What should we build?"
│ (27 installs)        │  Guided questions → product/design doc
└────────┬────────────┘
         │ design doc
         ▼
┌─────────────────────────┐
│ idea-to-ui-design-brief │  "How should it look?"
│ (28 installs)            │  Design doc → UI brief + AI image prompts
└────────┬────────────────┘
         │ UI brief
         ▼
┌──────────────────────────────┐
│ idea-to-implementation-doc   │  "How do we build it?"
│ (40 installs)                 │  Research + roadmap → implementation plan
└──────────────────────────────┘

         ▲
         │  (orchestrates all stages)
┌────────────────────────┐
│ idea-superpowers-suite │  "Just build the whole spec"
│ (27 installs)           │  Runs full pipeline end-to-end
└────────────────────────┘
```

## Prerequisites

- Hermes Agent v0.16.0 or later
- Node.js 18+ (for `npx skills`)
- An active project/idea to spec out

## Installation

### Option A: Full Suite (Recommended)

```bash
npx skills add akoliteza/hermes-agent-idea-workflow
```

This installs all 4 skills. The orchestrator (`idea-superpowers-suite`) calls the individual stages automatically.

### Option B: Individual Skills

```bash
# Just the design doc stage
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-design-doc

# Just the implementation planning stage
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-implementation-doc

# Just the UI design stage
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-to-ui-design-brief

# The full orchestrator (calls the others when needed)
npx skills add akoliteza/hermes-agent-idea-workflow --skill idea-superpowers-suite
```

## Usage

### Quick Start: Full Pipeline

```
"I have an idea for a tool that helps operators manage their business data.
Run the idea workflow on this."
```

The `idea-superpowers-suite` orchestrator will:
1. Ask clarifying questions to flesh out the idea
2. Produce a structured design document
3. Generate a UI design brief with layout guidance
4. Research competing products
5. Produce a technical implementation plan

### Stage-by-Stage Usage

**Stage 1 — Design Doc (`idea-to-design-doc`):**
```
"Turn this idea into a design doc: a dashboard that aggregates
Shopify, Stripe, and GA4 data into one view for operators."
```
Triggers when you mention "design doc," "product spec," or "flesh out this idea."

**Stage 2 — UI Brief (`idea-to-ui-design-brief`):**
```
"Take this design doc and create a UI brief. Include image-generation
prompts for the dashboard mockup."
```
Triggers on "UI brief," "design brief," "mockup," or when a design doc is ready.

**Stage 3 — Implementation Plan (`idea-to-implementation-doc`):**
```
"Review this design doc, research similar products, and create an
implementation roadmap with technical milestones."
```
Triggers on "implementation plan," "roadmap," "technical spec," or "how to build."

**Stage 4 — Orchestrator (`idea-superpowers-suite`):**
```
"Run the full idea workflow: I want to build a business intelligence
tool for e-commerce operators."
```
Triggers on "idea workflow," "full spec," "product pipeline," or "idea to build."

## Output Artifacts

Each stage produces structured Markdown files:

| Stage | Output File | Contents |
|-------|-------------|----------|
| Design Doc | `design-doc.md` | Problem statement, user stories, feature list, constraints |
| UI Brief | `ui-design-brief.md` | Layout wireframes (text), component list, image-gen prompts, color/styling guidance |
| Implementation Plan | `implementation-plan.md` | Tech stack, architecture decisions, milestone breakdown, risk register |
| Full Pipeline | All 3 files + `pipeline-summary.md` | Complete build-ready specification package |

## CorpusIQ Use Cases

1. **Feature Validation:** When user research surfaces a pain point, run `idea-to-design-doc` to turn the feedback into a structured feature spec before coding.

2. **Competitive Response:** When a competitor launches a new feature, use `idea-to-implementation-doc` to research and plan a differentiated response.

3. **Client Deliverables:** Generate professional design docs and implementation plans for client projects without spending hours in Figma or Notion.

4. **Internal Tooling:** Rapidly spec internal tools and automations before committing engineering resources.

## Capabilities

- **Guided Ideation:** Each stage asks clarifying questions before producing output — no vague one-shot generation
- **Competitive Research:** The implementation stage researches similar products as context
- **AI Image Prompts:** The UI brief stage generates image-generation prompts for mockups
- **Build-Ready Output:** Implementation plans include file structure, API contracts, and milestone timelines
- **Hermes-Native:** All skills use Hermes Agent's tool set (terminal, web_extract, write_file)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Skill not triggering | Verify with `hermes skills list --marketplace`. The skill activates on keywords like "design doc," "implementation plan," or "idea workflow." |
| Pipeline stops mid-way | Run individual stages manually. The orchestrator chains them but individual stages work standalone. |
| Missing tools | Requires `terminal`, `web_extract`, and `write_file`. Verify these are available in your Hermes config. |
| Output quality | The skills use guided questions — answer them thoroughly for best results. Vague inputs produce vague outputs. |

## Related Skills

- `writing-plans` — General-purpose plan writing (bundled with Hermes Agent)
- `superpowers:writing-plans` — Superpowers variant with enhanced structure
- `codex` — Delegate implementation to OpenAI Codex CLI after the spec is complete
- `blueprint-orchestration` — Multi-agent orchestration for larger projects

---

*Skill source: [AkoliteZA/hermes-agent-idea-workflow](https://github.com/AkoliteZA/hermes-agent-idea-workflow) · License: MIT · Curated by CorpusIQ*

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
