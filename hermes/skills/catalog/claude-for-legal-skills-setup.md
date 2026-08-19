---
title: "Claude for Legal Skills — Anthropic Legal Workflow Suite Setup"
description: "anthropics/claude-for-legal — 118 skills, 54.4K installs: Anthropic's official legal-workflow suite covering contract review, matter management, regulatory research, and lawyer-facing drafting pipelines."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-for-legal-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "legal", "contract review", "anthropic", "claude"]
---

# Claude for Legal Skills — Setup Guide

**Source:** [anthropics/claude-for-legal](https://skills.sh/anthropics/claude-for-legal)
**GitHub:** [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal)
**Skills:** 118 skills · 54.4K total installs
**Category:** Legal Operations
**First Seen:** May 13, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, and Snyk Pass on the flagship legal-writing skill; official Anthropic publisher; 9.2K GitHub stars

Claude for Legal is Anthropic's official skill suite for legal workflows. It covers the full matter lifecycle: intake, drafting, review (NDA, MSA, DPA, vendor agreements, IP clauses), regulatory research, compliance tracking, and client communication. The flagship legal-writing skill encodes a strict no-rewriting rule for law-student feedback (structural critique only, with labeled example phrasings), and the suite ships with its own skill-manager and skill-installer for governing the pack inside Claude environments.

---

## Installation

```bash
npx skills add anthropics/claude-for-legal
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/anthropics/claude-for-legal --skill legal-writing
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Claude environment** | Skills reference `~/.claude/plugins/config/claude-for-legal/` for per-user state (student profiles, feedback trackers, matter workspaces) |
| **Matter data** | Local files or client-provided documents; the suite does not ship cloud connectors |

## What It Provides

| Skill Group | Examples | Purpose |
|---|---|---|
| Core drafting | legal-writing, draft, memo, client-letter, plain-language-letters | Lawyer-facing drafting with strict no-rewrite feedback rules |
| Contract review | saas-msa-review, nda-review, dpa-review, vendor-agreement-review, ip-clause-review, termination-review | Structured agreement review with issue extraction |
| Matter management | matter-intake, matter-briefing, matter-workspace, matter-update, matter-close, deadlines, closing-checklist | Full matter lifecycle tracking |
| Regulatory | reg-gap-analysis, reg-feed-watcher, entity-compliance, dsar-response, pia-generation, aia-generation | Compliance gap analysis and privacy assessments |
| Litigation support | claim-chart, case-brief, chronology, demand-draft, cease-desist, subpoena-triage, deposition-prep | Litigation and dispute workflow |
| Suite governance | skill-manager, skill-installer, skills-qa, customize, disable, uninstall | The pack governs itself inside the agent |

Top skills by installs: legal-writing (962), draft (669), flashcards (574), saas-msa-review (549), policy-monitor (538).

## Quick Start

1. Install: `npx skills add anthropics/claude-for-legal`
2. Ask the agent to review a contract: the nda-review, saas-msa-review, or dpa-review skills structure the analysis
3. For tracking work, use matter-intake to open a matter and matter-close to file it

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Business operator contract review** | NDA and MSA review skills give operators structured red-flag analysis without counsel on retainer |
| **Privacy compliance** | dsar-response and pia-generation map to GDPR/CCPA workflows business operators routinely face |
| **Multi-connector diligence** | diligence-issue-extraction and material-contract-schedule pair well with CorpusIQ document connectors |
| **Agent governance reference** | The suite's skill-manager pattern is a working model for self-governing skill packs |

## Limitations / Verification

- Security audits on the legal-writing flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass
- Publisher-page total verified (54.4K across 118 skills); 9.2K GitHub stars as of the sweep
- Official Anthropic publisher; skills assume a Claude-style plugin directory layout (`~/.claude/plugins/config/claude-for-legal/`)
- Legal guidance is not legal advice — outputs should be reviewed by qualified counsel for binding matters

```bash
npx skills add anthropics/claude-for-legal   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
