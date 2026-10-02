---
title: "rlaope Oh My Hermes - 130-Skill All-in-One Plugin Setup"
description: "Setup guide for rlaope/oh-my-hermes - 130+ Hermes Agent workflow packages: coding intelligence, long-term memory, ops reviews, research, sales, finance, security."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rlaope-oh-my-hermes-setup/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes skill", "agent skill", "skill setup", "workflow", "agent orchestration", "memory"]
---

# rlaope Oh My Hermes - Setup Guide

**Source:** [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) (3,000⭐, pushed Sep 28, 2026)
**Skill:** `rlaope/oh-my-hermes` (130 installable skills, 1,515+ combined installs on skills.sh)
**Category:** Agent Workflow Packages / Hermes Operations
**Quality Tier:** 🔵 Community (new repo, no security verdicts published - verified Sep 28, 2026)

rlaope's Oh My Hermes is an all-in-one plugin for Hermes Agent: "the coding intelligence, a long-term memory system and model optimized workflow packages". Unlike the earlier-documented 9-skill `witt3rd/oh-my-hermes` suite, this is a much larger (130-skill) collection of Hermes-native workflow packages spanning operations, product, research, sales, finance, security, and the `ulw-*` work-loop family. Repo pushed the same day as this sweep - the author is actively shipping.

---

## Installation

```bash
# Individual skills
npx skills add rlaope/oh-my-hermes --skill omh-ops-review

# Or tap the repo as a Hermes skill tap
hermes skills tap add rlaope/oh-my-hermes
hermes skills install omh-ops-review omh-research-brief omh-security-safety-review
```

## Skill Families

| Family | Skills | Focus |
|---|---|---|
| omh-ops | 15+ | Ops reviews, observability cards, operating rhythm, run efficiency, workspace audit, morning brief |
| omh-research | 10+ | Research briefs, research department, web research, paper learning, source finder |
| omh-product | 10+ | Product briefs, product discovery/validation, CTO loop, idea-to-deploy, decision prototypes |
| omh-sales | 5+ | Sales development, sales pipeline review, meeting briefs, people ops |
| omh-security | 6+ | Security safety review, security event response, legal compliance, threat models |
| omh-memory | 5+ | Long-term memory system: memory-new, memory-sync, decision recall, instinct ledger |
| omh-code | 15+ | Code review, frontend/backend, refactor plans, build-failure triage, codebase onboarding |
| omh-runtime | 10+ | Toolbelt/connector/executor readiness, prompt import, model setup, routing, meta-router |
| ulw-* | 9 | Work-loop suite: ulw-context, ulw-interview, ulw-plan, ulw-loop, ulw-perf, ulw-qa, ulw-research, ulw-work, ulw-maestro |
| sweeps | 2 | triage-sweep, review-sweep (issue/review batch sweeps) |

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| triage-sweep | 19 | Batch triage sweep across an issue/work backlog |
| review-sweep | 19 | Batch review sweep (PRs, documents) |
| ulw-research | 16 | Work-loop research stage |
| omh-ops-review | 16 | Structured ops review of a system or team |
| omh-frontend | 16 | Frontend development workflow |
| omh-decide | 16 | Decision-making workflow with options scoring |
| omh-codegraph-refresh | 16 | Refresh the codebase knowledge graph |
| omh-capability-toggle | 16 | Capability toggle management |
| omh-agent-board | 16 | Agent task board and status tracking |
| omh-ai-slop-cleaner | 15 | Strip AI-slop patterns from writing |
| omh-security-safety-review | 15 | Pre-execution security/safety review gate (prompt injection, secrets, destructive actions) |
| omh-automation-blueprint | 15 | Recurring job blueprint: schedule, delivery, silence policy, context chain |
| omh-browser | 15 | Browser task policy overlay with auth/confirmation/observed-trace gates |
| omh-memory-sync | 15 | Long-term memory sync between sessions |

(130 skills total - 100 indexed on skills.sh at sweep time, installs concentrated at 15-19 each.)

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Cron discipline** | `omh-automation-blueprint` matches the CorpusIQ cron blueprint pattern: schedule + delivery + silence policy |
| **Pre-execution gates** | `omh-security-safety-review` aligns with the pre-flight gate doctrine for external actions |
| **Weekly self-optimization** | `omh-ops-review` + `omh-run-efficiency` feed the Monday performance audit |
| **Content quality** | `omh-ai-slop-cleaner` pairs with the content-slop-scoring gate for UGC drafts |
| **Memory operations** | `omh-memory-sync` / `omh-decision-recall` complement Honcho + GBrain session handoff |

## Limitations / Verification

- New and fast-moving repo (pushed Sep 28, 2026); skills change frequently - pin versions where possible
- Not the same publisher as the documented [witt3rd/oh-my-hermes suite](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup) (255⭐, 9 skills)
- Verify: `npx skills add rlaope/oh-my-hermes --list` shows the current skill count

## Security

No skills.sh security audits published (verified Sep 28, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Oh My Hermes (OMH) Suite Setup](/hermes/skills/catalog/oh-my-hermes-omh-suite-setup) (different publisher: witt3rd)
- [Oh My Hermes Workflow Setup](/hermes/skills/catalog/oh-my-hermes-workflow-setup) (different publisher: reason-machines)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
