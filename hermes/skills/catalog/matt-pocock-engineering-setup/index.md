---
title: "Matt Pocock Engineering Skills — Setup Guide"
description: "Install and configure the 5-skill Matt Pocock engineering suite: architecture review, PRD generation, issue decomposition, repo setup, and adversarial plan grilling. 1.3M+ combined installs."
---

# Matt Pocock Engineering Skills — Hermes Setup Guide

**Skill Suite:** Matt Pocock Engineering Skills (5 skills, 1.3M+ combined installs)
**Source:** [mattpocock/skills](https://github.com/mattpocock/skills)
**Category:** Software Engineering, Product Management, Project Management

---

## 1. Overview

Matt Pocock's engineering skills turn Hermes agents into production-grade software engineers. The suite covers the full planning-to-implementation pipeline:

| Skill | Role | Installs |
|-------|------|:--------:|
| **improve-codebase-architecture** | Scan code for improvement opportunities, visual HTML report | 347K |
| **to-prd** | Convert conversations into structured PRDs | 308K |
| **to-issues** | Decompose plans into executable issues (tracer-bullet slices) | 296K |
| **setup-matt-pocock-skills** | One-time repo config: issue tracker, labels, domain docs | 288K |
| **grilling** | Adversarial plan review — stress-test before building | 71K |

**Typical workflow:** Setup repo → Grill the plan → Generate PRD → Break into issues → Improve architecture as you go.

---

## 2. Prerequisites

- Hermes Agent installed ([setup guide](/hermes/setup/))
- Node.js 18+ (for `npx skills add`)
- GitHub repo with Issues enabled (for to-issues and to-prd output)
- GitHub Personal Access Token with `repo` scope (for issue creation)

---

## 3. Installation

### Step 1: Install the setup skill first

```bash
npx skills add mattpocock/skills@setup-matt-pocock-skills
```

### Step 2: Configure your repo

Run the setup skill to configure your project's issue tracker, label vocabulary, and domain document layout:

```bash
# From your project directory
npx skills run setup-matt-pocock-skills
```

This creates:
- Issue labels: `bug`, `feature`, `tech-debt`, `docs`, `epic`
- Triage workflow: `triage` → `backlog` → `sprint`
- Domain doc directory: `docs/domain/`

### Step 3: Install the rest of the suite

```bash
npx skills add mattpocock/skills@grilling
npx skills add mattpocock/skills@to-prd
npx skills add mattpocock/skills@to-issues
npx skills add mattpocock/skills@improve-codebase-architecture
```

### Step 4: Verify installation

```bash
npx skills list | grep -E "grilling|to-prd|to-issues|improve-codebase|setup-matt"
```

All five should appear with their install counts.

---

## 4. Skill Capabilities

### 4.1 grilling — Adversarial Plan Review

**Trigger phrases:** "grill this plan", "stress-test my design", "poke holes in this", "what am I missing?"

The skill conducts a structured interview about your plan:
- Identifies unstated assumptions
- Surfaces edge cases and failure modes
- Tests resource and timeline estimates
- Flags missing stakeholders or dependencies

**Best used BEFORE writing code or committing to architecture decisions.**

### 4.2 to-prd — PRD Generation

**Trigger phrases:** "turn this into a PRD", "create a product spec", "write a requirements doc"

Synthesizes the conversation into a structured PRD:
- Problem statement
- Success metrics
- User stories with acceptance criteria
- Technical constraints
- Out-of-scope items
- Timeline estimates

Outputs to your GitHub issue tracker as a single PRD issue.

### 4.3 to-issues — Issue Decomposition

**Trigger phrases:** "break this into issues", "create tickets for this plan", "decompose the PRD"

Uses tracer-bullet vertical slices to create independently-grabbable issues:
- Each issue is a complete, shippable increment
- Issues are prioritized by dependency order
- Estimates are included where possible
- Labels and milestones are applied automatically

### 4.4 improve-codebase-architecture — Architecture Review

**Trigger phrases:** "review the architecture", "scan for improvements", "find deepening opportunities"

Analyzes the codebase and produces an interactive HTML report:
- Identifies coupling hotspots
- Surfaces dead code and duplication
- Suggests refactoring opportunities
- Ranks by impact and effort

---

## 5. CorpusIQ Use Cases

### PRD Pipeline for Feature Development
```
User describes feature → grilling (stress-test) → to-prd (generate spec) → to-issues (decompose) → Start building
```

### Architecture Health Check
```
Run improve-codebase-architecture weekly → review HTML report → create refactor issues via to-issues
```

### Sprint Planning
```
Accumulate feature requests in conversation → to-prd → to-issues with sprint labels → Ready for development
```

---

## 6. CLI Reference

| Command | Purpose |
|---------|---------|
| `npx skills run grilling` | Start adversarial plan interview |
| `npx skills run to-prd` | Generate PRD from conversation |
| `npx skills run to-issues` | Decompose plan into issues |
| `npx skills run improve-codebase-architecture` | Run architecture scan |
| `npx skills run setup-matt-pocock-skills` | Configure repo (first-time only) |

All skills operate on the current conversation context — no additional arguments needed.

---

## 7. Troubleshooting

| Issue | Solution |
|-------|----------|
| `to-issues` creates no issues | Verify `GH_TOKEN` is set and has `repo` scope |
| `improve-codebase-architecture` takes too long | Run on specific directories with `--path <dir>` |
| Skills not found after install | Run `npx skills list` to verify, re-install if missing |
| `to-prd` output is too brief | The skill synthesizes from conversation — provide detailed context before running |

---

*↑ [Skills Catalog](/hermes/skills/catalog/) | [Matt Pocock Skills Repo](https://github.com/mattpocock/skills) →*

---

*Part of the Hermes Skills Library. Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
