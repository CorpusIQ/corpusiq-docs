---
title: "ClawHub Skill Vetting - Security Scanner Setup"
description: "Skill security scanner for Clawhub — scan and vet skills before install. ~1,656 installs, 5⭐."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/clawhub-skill-vetting-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "security", "skill vetting"]
---

# ClawHub Skill Vetting - Setup Guide

**Source:** [hugomrtz/skill-vetting-clawhub](https://github.com/hugomrtz/skill-vetting-clawhub) (5⭐)
**Skill family:** `hugomrtz/skill-vetting-clawhub` (1 installable skill)
**Combined Installs:** ~1,656 across indexed listings (Sep 29, 2026 snapshot)
**Category:** DevOps
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

This single-skill family ships one installable skill, `clawhub-skill-vetting` — a skill security scanner for Clawhub, published by an individual maintainer (hugomrtz). The SKILL.md lives at the repo root rather than in a skills/ subdirectory. Skills.sh verified 1/1 SKILL.md with ~1,656 installs in the Sep 29, 2026 sweep.

---

## Installation

```bash
npx skills add hugomrtz/skill-vetting-clawhub
```

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Pre-install security gate | Reference the scanner's approach when building vetting gates for Hermes skill installs. |
| Supply-chain review | Track scanner adoption when auditing skill supply chains and Clawhub distribution. |
| Catalog due diligence | Pair with Trust Hub / Socket / Snyk checks when promoting skills past the Unverified tier. |

## Limitations / Verification

- Verified: skills.sh indexing (1/1 SKILL.md), ~1,656 installs, and 5 GitHub stars as of Sep 29, 2026.
- Not verified: no live install test was run. The README description ("Skill security scanner for Clawhub") is the only published summary; scanner mechanics were not independently inspected.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
