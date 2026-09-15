---
title: "Archify - Interactive Architecture Diagram Skill Setup"
description: "tt-a1i/archify - 1 skill, 32.5K installs, 39.2K GitHub stars. Generates self-contained interactive HTML architecture, workflow, sequence, dataflow, and lifecycle diagrams from typed JSON specs, with a built-in validation CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/archify-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "diagrams"]
---

# Archify - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/tt-a1i/archify) (32.5K installs)
**GitHub:** [tt-a1i/archify](https://github.com/tt-a1i/archify) (39,204⭐, MIT)
**Category:** Architecture & Diagrams
**First Seen:** May 11, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

Archify creates self-contained, interactive HTML diagrams - architecture, workflow, sequence, dataflow, and lifecycle - from a small typed JSON specification. Static output is the default; motion is opt-in for demos and presentations. The unusual part is the quality gate: a bundled CLI (`node bin/archify.mjs validate <type> <candidate.json> --quality showcase --json`) checks every artifact against 9 checks with 0 composition errors before handoff, and `deliver` is the final acceptance command. One of the highest-starred single-skill repos on skills.sh (39.2K⭐ vs 32.5K installs).

---

## Installation

```bash
npx skills add tt-a1i/archify --skill archify
```

## Workflow

1. Choose the diagram type (architecture, workflow, sequence, dataflow, lifecycle)
2. Read the matching schema + one example from the skill's `schemas/` and `examples/` directories
3. Write the candidate JSON artifact first (max ~12 primary nodes, one clear main path, sparse labels)
4. Validate: `node bin/archify.mjs validate <type> <candidate.json> --quality showcase --json` - showcase requires all 9 artifact checks, 0 composition errors, 0 warnings
5. Deliver: `deliver` is the final acceptance command for the rendered HTML
6. Brand marks: `node bin/archify.mjs brands "<name>" --json` for real product identity

Schema version 2 is the current authoring contract for workflows; version 1 is preserved only for fixed-geometry legacy diagrams.

## Prerequisites

- Node.js (for the bundled `bin/archify.mjs` validation CLI)
- No API keys or external services - output is a self-contained HTML file

## CorpusIQ Use Cases

- **Architecture docs** - CorpusIQ's data-connector and agent-orchestration architecture pages become interactive, verifiable diagrams instead of static images
- **Investor/operator decks** - motion-enabled workflow diagrams for demos and presentations
- **Verifiable diagram quality** - the validate-before-deliver gate is the diagram equivalent of CorpusIQ's pre-publish content gates

## Limitations / Verification

- JSON-spec authoring is a different muscle than Mermaid/D2 text syntax - budget a short learning pass on `schemas/`
- Static default keeps output light; motion must be explicitly requested per the SKILL.md
- Verify install: `npx skills list | grep archify`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/tt-a1i/archify/archify/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/tt-a1i/archify/archify/security/socket) · [Snyk: Pass](https://www.skills.sh/tt-a1i/archify/archify/security/snyk)

## Related

- [Design Doc Mermaid Setup](/docs/hermes/skills/catalog/design-doc-mermaid-setup)
- [Hallmark - Anti-AI-Slop Design Skill](/docs/hermes/skills/catalog/hallmark-setup)
