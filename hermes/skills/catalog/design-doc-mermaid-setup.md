---
title: Design Doc Mermaid Skill — Diagram & Documentation Setup
description: "spillwavesolutions/design-doc-mermaid — design-doc-mermaid (34.2K installs): Mermaid Architect skill for hierarchical diagrams, decision trees, code-to-diagram workflows, high-contrast styling, and documentation systems."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/design-doc-mermaid-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "mermaid", "diagrams", "documentation"]
---

# Design Doc Mermaid Skill — Setup Guide

**Source:** [spillwavesolutions/design-doc-mermaid](https://skills.sh/spillwavesolutions/design-doc-mermaid)
**GitHub:** [spillwavesolutions/design-doc-mermaid](https://github.com/spillwavesolutions/design-doc-mermaid) (147 stars)
**Skills:** 1 skill (`design-doc-mermaid`) · 34.2K installs
**Category:** Diagrams & Technical Documentation
**First Seen:** February 6, 2026 (catalogued August 15, 2026 sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub and Socket pass; Snyk reports a warning)

The Mermaid Architect skill is a diagram and documentation system with specialized guides and code-to-diagram capabilities. It covers decision trees, usage patterns, a resilient workflow, unicode semantic symbols, Python utilities, high-contrast styling, file organization, and a learning path with a "when to use what" matrix. Well suited to agents that produce architecture docs, flowcharts, and design documents in Markdown-based repositories.

---

## Installation

```bash
npx skills add spillwavesolutions/design-doc-mermaid
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the installer |
| **Mermaid rendering** | GitHub, MkDocs with mermaid plugin, or a Mermaid CLI for rendered output |

## What It Provides

| Capability | Notes |
|---|---|
| Decision trees | Hierarchical decision-tree diagrams with examples |
| Code-to-diagram | Generate diagrams from code structure |
| Usage patterns | When to use which diagram type |
| Resilient workflow | Iterative diagram workflow that tolerates revisions |
| Unicode symbols | Semantic unicode symbol conventions |
| Python utilities | Helper scripts for diagram generation |
| High-contrast styling | Accessibility-focused color conventions |
| Learning path | Progressive guide from basic flowcharts to advanced layouts |

## Quick Start

1. `npx skills add spillwavesolutions/design-doc-mermaid`
2. Ask: "diagram this API flow as a sequence diagram with high-contrast styling"
3. Follow the decision tree to pick the right diagram type for the document

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Architecture docs** | Flowcharts and sequence diagrams for MCP server and connector docs |
| **Docs repo quality** | High-contrast, accessible diagrams in corpusiq-docs markdown |
| **Decision documentation** | Decision trees for governance and process pages |
| **Code-to-diagram** | Generate diagrams from repo structure for onboarding docs |

## Limitations / Verification

- Text-based Mermaid — rendering depends on the hosting platform's Mermaid support
- Snyk audit carries a warning — review before production use

```bash
npx skills add spillwavesolutions/design-doc-mermaid   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Markdown Viewer](/hermes/skills/) — diagram rendering in Hermes
- [SEO GEO Claude Skills Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup/) — docs optimization

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
