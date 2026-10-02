---
title: "AE-CLI Skills - AgenticEngine Platform Suite Setup"
description: "Setup guide for thinkingaiagenticengine/ae-cli - 34 agent skills for the ThinkingAI AgenticEngine platform: analysis, engagement, dataops, community."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ae-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "agentic platform", "cli", "engagement"]
---

# AE-CLI Skills - Setup Guide

**Source:** [thinkingaiagenticengine/ae-cli](https://github.com/thinkingaiagenticengine/ae-cli) (18⭐, pushed Sep 23, 2026)
**Skill:** `thinkingaiagenticengine/ae-cli` (34 installable skills)
**Installs:** ~650 per top skill, ~22K combined (Sep 27, 2026 snapshot)
**Category:** Agent Platform / Engagement & Analysis
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

AE-CLI is the CLI and skill suite for ThinkingAI's AgenticEngine (AE) platform, designed for both AI agents and humans. The 34 skills cover platform operations end to end: analysis (`ae-analysis`, `ae-analysis-global`), engagement (`ae-engage`), community management (`ae-community`), data ops (`ae-dataops`), knowledge base (`ae-kb`), team coordination (`ae-team`), metadata, tracking-plan generation, and CLI self-checks. The platform-first design means the skills are less about general capability and more about running a social/engagement operation through AE.

---

## Installation

```bash
# Full suite
npx skills add thinkingaiagenticengine/ae-cli

# Engagement-only subset
npx skills add thinkingaiagenticengine/ae-cli --skill ae-engage
```

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| ae-analysis | 675 | Platform analysis: posts, accounts, topics |
| ae-engage | 670 | Engagement workflows (reply, like, follow decisions) |
| ae-dataops | 670 | Data export, cleanup, and pipeline ops |
| ae-community | 666 | Community member tracking and outreach |
| ae-kb | 653 | Knowledge base ingest and query |
| ae-agent | 653 | Agent identity and configuration |
| cli-self-check | 651 | CLI health and version checks |
| ae-team | 647 | Team workspace coordination |
| ae-analysis-global | 645 | Cross-account/global analysis |
| ae-metadata | 618 | Entity metadata management |
| ae-data-integration-helper | 598 | Data source integration |
| ae-generate-tracking-plan | 596 | Tracking-plan generation for accounts/topics |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Engagement research** | Compare AE's engagement-analysis patterns with CorpusIQ's own social mining |
| **Tracking-plan ideas** | `ae-generate-tracking-plan` informs monitoring-plan design |
| **CLI design reference** | The self-check and metadata patterns are reusable CLI-health references |

## Limitations / Verification

- Deeply tied to the AE platform; limited value without an AE account
- Small publisher (18⭐); treat workflows as reference patterns rather than production tooling
- Verify: `npx skills add thinkingaiagenticengine/ae-cli --list` shows 34 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Reddit Automation Setup](/hermes/skills/catalog/reddit-automation-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
