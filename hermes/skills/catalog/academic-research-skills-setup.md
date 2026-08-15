---
title: Academic Research Skills — Paper Pipeline for Agents Setup
description: "imbad0202/academic-research-skills — 4 skills at 26.4K installs: academic-paper, academic-paper-reviewer, deep-research, and academic-pipeline for literature review, paper drafting, review, and research workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/academic-research-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "research", "academic", "deep research"]
---

# Academic Research Skills — Setup Guide

**Source:** [imbad0202/academic-research-skills](https://skills.sh/imbad0202/academic-research-skills)
**GitHub:** [imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)
**Skills:** 4 skills · 26.4K total installs
**Category:** Research & Literature Review
**First Seen:** August 15, 2026 sweep
**Quality Tier:** 🟡 Trusted (community suite; verify per-skill before production use)

A four-skill academic research suite: academic-paper for paper drafting, academic-paper-reviewer for peer-review workflows, deep-research for multi-source investigation, and academic-pipeline for end-to-end research orchestration. Distinct from the separate `izillionways/academic-research-skills-hermes` repo already in our ecosystem tracking — this is the skills.sh marketplace cluster. Complements the research intelligence framework used across CorpusIQ research sweeps.

---

## Installation

```bash
npx skills add imbad0202/academic-research-skills
```

Individual skills:

```bash
npx skills add imbad0202/academic-research-skills --skill deep-research
npx skills add imbad0202/academic-research-skills --skill academic-paper-reviewer
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the installer |
| **Research sources** | Paper repositories, journals, or literature collections to work from |

## What It Provides

| Skill | Installs | Notes |
|---|---|---|
| academic-paper | 8.0K | Academic paper drafting |
| academic-paper-reviewer | 7.4K | Peer-review and critique workflows |
| deep-research | 5.7K | Multi-source deep research |
| academic-pipeline | 5.3K | End-to-end research orchestration |

## Quick Start

1. `npx skills add imbad0202/academic-research-skills`
2. "Run the deep-research workflow on this topic and produce a structured literature summary"
3. "Review this draft paper with the academic-paper-reviewer skill"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Market research sweeps** | deep-research workflow patterns for competitor and market investigations |
| **Research quality** | academic-paper-reviewer as a critique pass on research memos |
| **Investor materials** | Structured paper-style sourcing for diligence documents |
| **Pipeline reference** | academic-pipeline orchestration pattern for multi-stage research crons |

## Limitations / Verification

- Community suite — per-skill quality varies; verify outputs against primary sources
- Academic orientation; adapt prompts for business research contexts

```bash
npx skills add imbad0202/academic-research-skills --skill deep-research   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Grounded Citations](/hermes/skills/) — cited, verifiable sources
- [Awesome LLM Apps Skills Setup](/hermes/skills/catalog/awesome-llm-apps-skills-setup/) — role-based research skills

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
