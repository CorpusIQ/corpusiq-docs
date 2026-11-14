---
title: "EventCatalog Skills - Architecture Docs for Agents"
description: "event-catalog/skills: 4.0K combined installs across 6 listings, six skills that turn architectures and codebases into EventCatalog documentation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/event-catalog-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "eventcatalog", "architecture", "documentation"]
---

# EventCatalog Skills - Setup Guide

**Source:** [event-catalog/skills](https://www.skills.sh/event-catalog/skills) via skills.sh - 4.0K combined installs across 6 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 16 stars, MIT licence, `main` branch, last pushed 2026-10-26, 6 `SKILL.md` files in `skills/<name>/` folders, 39 files in total
**Category:** Architecture documentation workflows for EventCatalog
**Quality Tier:** 🟢 Green - six in-tree skills, all four sampled verdicts Pass, MIT licence, and a README that documents four install paths.

EventCatalog keeps architecture documentation as structured files in the repository: services, agents, events, commands, queries, domains, flows, channels and containers, all browsable as a catalog. This pack ships six skills that write and maintain those files.

Two skills form the backbone. `code-to-catalog` scans a codebase, proposes an architectural model, and interviews you on the structural decisions before writing a reviewable plan file. `catalog-documentation-creator` turns that plan into catalog files with the correct frontmatter and folder structure. `c4-to-eventcatalog` feeds the same pipeline from C4 models in Structurizr DSL, C4-PlantUML or Mermaid C4. The remaining three cover business flows, custom pages and API routes, and fitness functions that fail CI when the architecture drifts.

## Installation

```bash
# Install all six skills
npx skills add event-catalog/skills

# Install a single skill, for example the documentation generator
npx skills add event-catalog/skills --skill catalog-documentation-creator
```

The README also documents a clone-and-copy path and a git submodule path, plus a fork-and-customise option for teams that want the skills to match their own conventions.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| catalog-documentation-creator | 1,270 | Generates EventCatalog files (systems, services, agents, events, commands, queries, domains, flows, channels, containers, ADRs, data products, entities, diagrams) with correct frontmatter and folder structure. |
| code-to-catalog | 1,047 | Scans a codebase, proposes an architectural model, interviews you on the structural decisions, and writes a reviewable plan before handing off to catalog-documentation-creator. |
| flow-wizard | 597 | Walks you step-by-step through documenting a business or agent flow, cross-referencing the existing catalog resources. |
| c4-to-eventcatalog | 485 | Converts C4 models (Structurizr DSL, C4-PlantUML, Mermaid C4) into an EventCatalog documentation plan and hands off to catalog-documentation-creator. |
| custom-pages-and-apis | 471 | Builds custom Astro pages and TypeScript API endpoints in the catalog's pages/ folder using the @catalog/layouts and @catalog/utils toolkit. |

The remaining 1 indexed listing is fitness-functions, at 85 installs.

## Why This Matters for Hermes Agents

Most architecture documentation drifts. Diagrams are redrawn once and never again, and wiki pages describe the system as it was last quarter. EventCatalog's model is different: the architecture lives as structured files in the repository, so the documentation and the code change together, and drift can be caught by a CI check.

These skills make that model reachable by an agent. `code-to-catalog` does not ask you to describe your system from memory; it reads the code first and then grills you on the structural decisions, so the catalog is grounded in what actually exists. `catalog-documentation-creator` emits the files with the frontmatter and folder structure EventCatalog expects, removing the fiddly formatting work that makes hand-writing these files error-prone.

`fitness-functions` closes the loop. It encodes an architecture rule as a TypeScript check that fails CI when the rule is broken, so the catalog is not just documentation but an enforced contract.

The set is small and single-purpose. There is no generic content or SEO skill here, just six skills that cover the EventCatalog lifecycle: discover the architecture, model it, write the files, extend the pages, and keep it honest.

## Usage

| You say | What happens |
|---|---|
| "Document my OrderService that receives OrderCreated and sends OrderConfirmed" | Runs `catalog-documentation-creator` and writes the service and event files with the correct frontmatter. |
| "Look at my src/ directory and generate EventCatalog docs for the services and events you find" | Runs `code-to-catalog`, scans the code, interviews you on the model, and writes a reviewable plan file. |
| "Map this Structurizr DSL file into my existing EventCatalog" | Runs `c4-to-eventcatalog` and converts the C4 model into a documentation plan. |
| "Document the checkout flow from cart through payment to confirmation" | Runs `flow-wizard` and walks the flow step-by-step against the existing catalog. |
| "Add a team page to my catalog" | Runs `custom-pages-and-apis` and creates an Astro page wired into the navigation. |
| "Write a fitness function that fails CI when a service writes to another domain's database" | Runs `fitness-functions` and emits a `*.fitness.ts` rule wired into CI. |

## Verification

Probe two skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/event-catalog/skills/main/skills/catalog-documentation-creator/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/event-catalog/skills/main/skills/code-to-catalog/SKILL.md
```

Read the first one in full before installing it. The layout is flat: every skill lives at `skills/<name>/SKILL.md`, so a verification script pointed at a different path pattern will report a false failure.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| catalog-documentation-creator | Pass | Pass | Pass |
| code-to-catalog | Pass | Pass | Pass |
| flow-wizard | Pass | Pass | Pass |
| c4-to-eventcatalog | Pass | Pass | Pass |

All four sampled skills pass all three auditors, a clean signal for a pack this small. The other two skills (custom-pages-and-apis and fitness-functions) publish no verdict, which is unverified rather than clean. The main risk to review is the output: these skills write Markdown files and TypeScript rules into your repository, so read any SKILL.md before you let it write into a tree with secrets.

## Limitations

- Snapshot data, verified 2026-11-13: 3,955 combined installs across 6 indexed listings; 16 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- The install index and the tree agree here: all six indexed listings resolve to a `skills/<name>/SKILL.md` path in the current tree.
- The repo is young. 16 stars and a modest install base mean fewer people have exercised the generated output than a large, widely-audited suite would carry.
- `fitness-functions` is the only skill below the threshold at 85 installs, so its CI-failing behaviour is the least battle-tested of the set.
- Two of the six skills publish no security verdict on skills.sh; treat them as unverified, not clean.
- The output is EventCatalog-specific. These skills only pay off if EventCatalog is your catalog of record, and they do not replace a general architecture tool.

## Related

- [Architecture Diagram - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/architecture-diagram-setup)
- [Agent Architect - Agent System Design Setup](/hermes/skills/catalog/agent-architect-setup)
- [Terraform Skill - IaC Testing and Modules Setup](/hermes/skills/catalog/terraform-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `code-to-catalog`, not `catalog-documentation-creator`. The interview forces you to state the architectural model explicitly, and the plan file it writes is your review surface before any catalog file changes.
- Keep the catalog in the same repository as the code. That is the whole point of EventCatalog, and it is what lets `fitness-functions` fail CI against real drift.
- Wire `fitness-functions` in early. A rule that passes from day one is cheap; retrofitting rules onto an already-drifted catalog is its own project.
- Use `c4-to-eventcatalog` when you already have C4 models in Structurizr or PlantUML, so you do not re-derive the architecture from source.
- Add `custom-pages-and-apis` only after the core catalog files exist, so the custom pages have resources to link against.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
