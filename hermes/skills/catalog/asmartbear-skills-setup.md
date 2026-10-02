---
title: "A Smart Bear Skills - Positioning & PMF Suite Setup"
description: "Setup guide for asmartbear/asb-skills - 21 agent skills from A Smart Bear (Jason Cohen) on positioning, problem discovery, and product-market fit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/asmartbear-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "positioning", "product-market fit", "strategy"]
---

# A Smart Bear Skills - Setup Guide

**Source:** [asmartbear/asb-skills](https://github.com/asmartbear/asb-skills) (46⭐, pushed Aug 29, 2026)
**Skill:** `asmartbear/asb-skills` (21 installable skills)
**Installs:** ~540 per top skill, ~11K combined (Sep 27, 2026 snapshot)
**Category:** Product Strategy / Positioning
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

Jason Cohen's A Smart Bear blog is one of the most-cited sources in B2B startup strategy (positioning, pricing, bootstrapping, "the problem"). This skill suite encodes his frameworks and the book _Hidden Multipliers_ into 21 runnable agent skills: positioning exercises, problem-discovery workflows, needs-stack analysis, buyer/voter mapping, and the Carol framework (define, observations, keystones, inciting events, dealbreakers, strengths) for customer discovery. Agents get Cohen's exact questioning discipline as executable workflows.

---

## Installation

```bash
# Full suite
npx skills add asmartbear/asb-skills

# Positioning subset
npx skills add asmartbear/asb-skills --skill asb-positioning
```

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| asb-positioning | 555 | Positioning statements and differentiation |
| asb-problem | 546 | Problem discovery and validation |
| asb-rude-qa | 545 | The "rude Q&A" test for claims |
| asb-who-me | 544 | Who-has-this-problem discovery |
| asb-needs-stack | 542 | Needs-stack analysis (JTBD-style) |
| asb-voters | 541 | Buyer/voter identification |
| asb-carol-define | 538 | Carol framework: define the customer |
| asb-carol-observations | 537 | Carol framework: gather observations |
| asb-carol-keystones | 537 | Carol framework: find keystone beliefs |
| asb-carol-inciting-events | 536 | Carol framework: inciting events |
| asb-carol-dealbreakers | 535 | Carol framework: dealbreakers |
| asb-carol-strengths | 534 | Carol framework: strengths inventory |
| asb-interview-debrief | 540 | Interview debrief: turn one customer conversation into a question-mapped debrief file (verbatim phrases, addenda) |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **CorpusIQ positioning** | `asb-positioning` and `asb-rude-qa` pressure-test our own messaging |
| **User research** | The Carol framework skills structure customer-discovery interviews |
| **Feature validation** | `asb-problem` and `asb-needs-stack` frame feature requests as validated problems |
| **Help-first content** | Cohen's frameworks convert directly into operator-help content angles |

## Limitations / Verification

- Skills encode frameworks, not data - they guide the agent's reasoning rather than calling APIs
- Repo is new and small (46⭐); skills.sh lists no security verdicts yet
- Verify: `npx skills add asmartbear/asb-skills --list` shows 21 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Marketing Mindset Setup](/hermes/skills/catalog/marketing-mindset-setup)
- [Revenue-Centric Design Setup](/hermes/skills/catalog/revenue-centric-design-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
