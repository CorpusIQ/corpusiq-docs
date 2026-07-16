---
title: "June 30, 2026 (Update) — Matt Pocock Engineering Skills"
description: "7 additional Hermes skills discovered June 30, 2026 late sweep: 5 Matt Pocock engineering skills (1.3M+ combined installs), ChromaDB integration, OpenClaw skill loader."
---

# 🆕 June 30, 2026 — Update: 7 Additional Skills

**Date:** June 30, 2026 (Update to [main June 30 sweep](/hermes/skills/marketplace/new-june30-2026/))
**New Repos:** 3 | **New Skills:** 7 | **Combined Installs:** 1,312,684

A second-pass sweep across skills.sh surfaced 7 additional skills missed in the morning sweep. Five Matt Pocock engineering skills — totalling 1.3M+ installs — bring production-grade software engineering workflows to Hermes agents: architecture review, PRD synthesis, issue decomposition, and adversarial plan grilling.

---

## New Skills at a Glance

| # | Skill | Installs | Category | Source |
|---|-------|:--------:|----------|--------|
| 1 | **improve-codebase-architecture** | 347,772 | Software Engineering | mattpocock/skills |
| 2 | **to-prd** | 308,668 | Product Management | mattpocock/skills |
| 3 | **to-issues** | 296,216 | Project Management | mattpocock/skills |
| 4 | **setup-matt-pocock-skills** | 288,420 | Infrastructure | mattpocock/skills |
| 5 | **grilling** | 71,235 | Planning & Critique | mattpocock/skills |
| 6 | **cli-anything-chromadb** | 331 | Vector Database | hkuds/cli-anything |
| 7 | **voltagent-openclaw-skill-loader** | 40 | OpenClaw Ecosystem | aradotso/hermes-skills |

---

## Category Breakdown

### Software Engineering (1 skill)

#### improve-codebase-architecture (347,772 installs)
**Repo:** [mattpocock/skills](https://github.com/mattpocock/skills)

Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. Architecture review and improvement recommendations built for agent-driven refactoring.

```bash
npx skills add mattpocock/skills@improve-codebase-architecture
```

### Product Management (1 skill)

#### to-prd (308,668 installs)
**Repo:** [mattpocock/skills](https://github.com/mattpocock/skills)

Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed. Converts natural-language discussions into structured product requirement documents.

```bash
npx skills add mattpocock/skills@to-prd
```

### Project Management (1 skill)

#### to-issues (296,216 installs)
**Repo:** [mattpocock/skills](https://github.com/mattpocock/skills)

Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Transforms high-level plans into executable, prioritized issue lists.

```bash
npx skills add mattpocock/skills@to-issues
```

### Infrastructure (1 skill)

#### setup-matt-pocock-skills (288,420 installs)
**Repo:** [mattpocock/skills](https://github.com/mattpocock/skills)

Configure the repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the Matt Pocock engineering skill suite.

```bash
npx skills add mattpocock/skills@setup-matt-pocock-skills
```

### Planning & Critique (1 skill)

#### grilling (71,235 installs)
**Repo:** [mattpocock/skills](https://github.com/mattpocock/skills)

Interview the user relentlessly about a plan or design. Use when you want to stress-test a plan before building, or with any "grill" trigger phrases. Adversarial plan review that catches blind spots before implementation.

```bash
npx skills add mattpocock/skills@grilling
```

### Vector Database (1 skill)

#### cli-anything-chromadb (331 installs)
**Repo:** [hkuds/cli-anything](https://github.com/hkuds/cli-anything)

ChromaDB integration for CLI-Anything. Brings vector search and embedding storage to Hermes agents via the CLI-Anything framework — persistent, disk-backed semantic memory for any CLI tool.

```bash
npx skills add hkuds/cli-anything@cli-anything-chromadb
```

### OpenClaw Ecosystem (1 skill)

#### voltagent-openclaw-skill-loader (40 installs)
**Repo:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills)

Fully automatic OpenClaw skill manager that installs, updates, and launches 5,200+ community skills from ClawHub with zero manual configuration. Bulk skill management for OpenClaw agents — discover, install, and update community skills programmatically.

```bash
npx skills add aradotso/hermes-skills@voltagent-openclaw-skill-loader
```

---

## Why These Matter

**Matt Pocock's engineering skills are the most-installed skills.sh suite** — 1.3M+ combined installs across 5 skills. They give Hermes agents production-grade software engineering workflows: architecture review → PRD generation → issue decomposition → adversarial critique. Any Hermes agent doing code work benefits from this pipeline.

**The gap between "assistant" and "engineer" is closing.** These skills replace human-driven code review, spec writing, and project management with agent-driven equivalents. The install counts (300K+ per skill) show real adoption, not experimental toy projects.

**OpenClaw skill management is becoming automated.** voltagent-openclaw-skill-loader (5,200+ skills from ClawHub) signals that OpenClaw's skill ecosystem is large enough to need programmatic management — not manual `npx skills add` one at a time.

---

*← [June 30 Main Sweep](/hermes/skills/marketplace/new-june30-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*

---

*Part of the Hermes Skills Library. Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
