---
title: "Samber DevRel Skills - Open Source Growth Suite Setup"
description: "Setup guide for samber/developer-relations-skills - 50 agent skills for open source strategy, community programs, and developer GTM from Samber."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/samber-devrel-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "devrel", "open source", "developer marketing"]
---

# Samber DevRel Skills - Setup Guide

**Source:** [samber/developer-relations-skills](https://github.com/samber/developer-relations-skills) (pushed Sep 27, 2026)
**Skill:** `samber/developer-relations-skills` (50 installable skills)
**Installs:** ~1,020 per top skill; ~50K combined across the suite (Sep 27, 2026 snapshot)
**Category:** Developer Relations / Open Source Growth
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

Samber (author of widely-used Go libraries such as `lo` and `slog-multi`) ships a 50-skill suite encoding the full developer-relations playbook: open source launch, distribution strategy, contributor onboarding, sponsors and brand strategy, license strategy, governance, engineering blog posts, issue triage, and budget allocation. Each skill is a focused workflow an agent can run, which makes the suite a ready-made operator's manual for running an OSS project's growth motion.

---

## Installation

```bash
# Full suite
npx skills add samber/developer-relations-skills

# Or single skills as needed
npx skills add samber/developer-relations-skills --skill oss-launch
```

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| oss-launch | 1,020 | Launch checklist and sequencing for a new open source project |
| oss-distribution-strategy | 1,019 | Channel and distribution planning (HN, Reddit, directories) |
| github-profile-optimization | 1,019 | Optimize the GitHub org/profile as a conversion surface |
| oss-sponsors-brand-strategy | 1,016 | Sponsor tiers and brand positioning |
| oss-license-strategy | 1,012 | License selection and dual-licensing decisions |
| oss-contributor-onboarding | 1,011 | Contributor welcome flows and first-issue design |
| oss-governance | 1,010 | Maintainer governance and decision frameworks |
| engineering-blog-post | 1,008 | Technical blog post drafting and distribution |
| oss-issue-triage | 989 | Issue triage workflows and response SLAs |
| devrel-budget-allocation | 984 | DevRel budget planning and channel mix |
| developer-champions | 1,012 | Unpaid perks-only champions/ambassador program design: readiness check, selection criteria, perk ladder, fixed terms, alumni |

The suite also covers open-standards strategy, open-source-company strategy, and developer community programs - 50 skills total.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **corpusiq-docs and open tooling growth** | Run `oss-launch` and `oss-distribution-strategy` for CorpusIQ's public repos |
| **Sponsor/brand work** | `oss-sponsors-brand-strategy` informs GitHub Sponsors positioning |
| **Contributor funnel** | `oss-contributor-onboarding` designs first-issue flows for the docs repo |
| **Content pipeline** | `engineering-blog-post` templates technical content for the blog |
| **Help-first doctrine** | `oss-issue-triage` aligns with CorpusIQ's help-first engagement rules |

## Limitations / Verification

- Suite targets OSS DevRel specifically; not a general marketing stack
- Individual install counts are modest (~1K); adoption is spread across 50 skills
- Verify: `npx skills add samber/developer-relations-skills --list` shows 50 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Reddit Automation Setup](/docs/hermes/skills/catalog/reddit-automation-setup)
- [Apify Growth Skills Setup](/docs/hermes/skills/catalog/apify-growth-skills-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
