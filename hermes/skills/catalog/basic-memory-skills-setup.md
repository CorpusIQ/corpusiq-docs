---
title: "Basic Memory Skills Setup Guide for Hermes Agents"
description: "basicmachines-co/basic-memory - 9.7K installs across 38 skills, 3.8K stars: the YC-backed Basic Machines team's agent memory suite - knowledge-graph notes, capture, curate, reflect, defrag, and lifecycle workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/basic-memory-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "memory", "knowledge graph", "agent memory", "basic memory"]
---

# Basic Memory Skills - Setup Guide

**Source:** [basicmachines-co/basic-memory](https://skills.sh/basicmachines-co/basic-memory) (9.7K installs across 38 skills)
**GitHub:** [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) (3.8K stars)
**Skills:** 38 skills; top skills: `memory-notes` (621), `memory-continue` (617), `memory-capture` (614)
**Category:** Agent Operations / Memory & Knowledge Management
**First Seen:** skills.sh May 31, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟢 Production - publisher authority (Basic Machines, YC-backed builder of the Basic Memory MCP) and all three skills.sh security audits Pass (see Security Audit Status)

Basic Machines - the YC-backed company behind the Basic Memory MCP server - publishes a 38-skill suite that teaches agents how to build and maintain a **searchable knowledge graph** from markdown notes. Each note carries three sections: frontmatter, observations, and relations. The skills encode the full lifecycle: capturing notes, continuing interrupted work, curating the graph, defining schema, reflecting, managing tasks, metadata search, defragmenting the graph, ingesting external content, and onboarding a fresh project.

The suite also includes engineering-workflow skills (`code-review`, `fix-pr-issues`, `pr-create`, `adversarial-review`) and CLI-facing helpers (`bm-setup`, `bm-remember`, `bm-status`, `bm-share`) that drive the Basic Memory tooling directly. Originally published as `basicmachines-co/basic-memory-skills`, the skills now live in the main `basic-memory` repo.

---

## Installation

```bash
npx skills add basicmachines-co/basic-memory
```

Or per-skill:

```bash
npx skills add https://github.com/basicmachines-co/basic-memory --skill memory-notes
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Basic Memory (optional)** | The MCP server at [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) for live graph storage; the note-writing skills also work against plain markdown |
| **Node.js** | Recent LTS for the `npx skills` installer |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| memory-notes | 621 | Writing well-structured notes with frontmatter, observations, and relations that parse into the knowledge graph |
| memory-continue | 617 | Resuming interrupted work by querying prior notes before redoing anything |
| memory-capture | 614 | Capturing decisions, constraints, and context into the graph as work happens |
| memory-curate | 610 | Organizing and pruning the graph to keep signal high |
| memory-schema | 592 | Defining entity types, relations, and tags for a project |
| memory-reflect | 591 | Periodic reflection passes that consolidate notes into higher-level insights |
| memory-tasks | 587 | Task tracking tied to graph entities |
| memory-metadata-search | 582 | Finding notes by frontmatter, tags, and metadata |
| memory-defrag | 580 | Defragmenting the graph - merging duplicates, fixing orphans |
| memory-ingest | 580 | Importing external content (docs, transcripts, code) into the graph |

Plus `memory-lifecycle`, `memory-research`, `memory-ci-capture`, `memory-onboarding`, the `bm-*` CLI helpers, and engineering workflow skills (`code-review`, `fix-pr-issues`, `pr-create`, `adversarial-review`).

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| memory-notes | Pass | Pass | Pass |

All three audits Pass - the basis for the 🟢 Production tier.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent memory discipline** | The notes → observations → relations pattern is a portable model for how CorpusIQ-connected agents structure session context and project knowledge |
| **Research synthesis** | `memory-capture` + `memory-reflect` give research sweeps a structured place to land findings and consolidate them |
| **Knowledge graph backing** | Operators asking CorpusIQ for knowledge management get a reference implementation: graph-first notes with metadata search |
| **Code review loops** | `code-review`, `fix-pr-issues`, and `pr-create` support agent-driven PR workflows for the docs and MCP repos |

## Limitations / Verification

- Below the 20K-install drafting bar; drafted on **publisher authority plus domain relevance**: YC-backed vendor, 3.8K stars, cohesive 38-skill suite, and agent memory is a core CorpusIQ operating surface (suite-cohesion precedent: coreyhaines31/makerskills).
- The `memory-*` skills reference the Basic Memory toolchain for full graph features; using them against plain markdown captures the note discipline without the graph backend.
- The repository is actively consolidating (`basic-memory-skills` → `basic-memory`); install commands here follow the current canonical repo.

Verification after install:

```bash
npx skills add basicmachines-co/basic-memory --list    # 38 skills discovered
```

## Related

- [Skills Catalog](/hermes/skills/catalog) - full quality-tiered directory
- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
