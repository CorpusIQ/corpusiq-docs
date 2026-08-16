---
title: "Deep Research Skill — Citation-Tracked Research Setup"
description: "199-biotechnologies/claude-deep-research-skill — 9.4K installs: structured research pipeline with evidence persistence, source identity management, and claim-level verification."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-deep-research-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "research", "citations"]
---

# Deep Research Skill — Setup Guide

**Source:** [199-biotechnologies/claude-deep-research-skill](https://skills.sh/199-biotechnologies/claude-deep-research-skill/deep-research)
**GitHub:** [199-biotechnologies/claude-deep-research-skill](https://github.com/199-biotechnologies/claude-deep-research-skill) (989 stars)
**Skills:** 1 skill · 9.4K installs
**Category:** Research
**First Seen:** Jan 21, 2026 · catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn)

A single-skill research engine: citation-tracked reports through a structured pipeline with evidence persistence, source identity management, claim-level verification, and progressive context management. The decision tree routes simple lookups to WebSearch and only complex analyses into the full pipeline — the right triage design for an autonomous agent.

---

## Installation

```bash
npx skills add https://github.com/199-biotechnologies/claude-deep-research-skill --skill deep-research
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Web search access** | For source gathering |
| **Markdown-friendly output target** | Reports are markdown-first |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| deep-research | 9.4K | Citation-tracked research reports with evidence persistence |

## Quick Start

1. Install: `npx skills add https://github.com/199-biotechnologies/claude-deep-research-skill --skill deep-research`
2. Ask: "research the MCP server landscape and produce a citation-tracked report"
3. Review the Introduction and Methodology sections — the skill surfaces high-materiality assumptions there explicitly

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Market research sweeps** | Citation-tracked output for competitive and market reports |
| **Funding research** | Structured, verifiable reports for investor diligence |
| **Docs content** | Evidence-backed drafts for the knowledge base |
| **Verification discipline** | Claim-level verification as a pattern for our own research quality |

## Limitations / Verification

- Security audits: Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn (named in audit; manual review recommended)
- Single-skill package — the pipeline is opinionated and may not fit ad-hoc research
- Verification command: `npx skills add https://github.com/199-biotechnologies/claude-deep-research-skill --skill deep-research`

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
