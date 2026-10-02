---
title: "CodeStable Skills - AI Coding Workflow Setup"
description: "Human-in-the-loop AI coding workflow: requirements, architecture, features, issues, and decisions stay controllable and traceable."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codestable-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "ai coding", "workflow"]
---

# CodeStable Skills - Setup Guide

**Source:** [codestable/codestable](https://github.com/codestable/codestable) (1114⭐)
**Skill family:** `codestable/codestable` (5 installable skills indexed)
**Combined Installs:** ~38,530 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

CodeStable is a human-in-the-loop AI coding workflow for serious software engineering: it organizes requirements, architecture, features, issues, and historical decisions so Codex- and Claude-driven development stays controllable, traceable, and sustainable. Skills live under plugins/codestable/skills/ and .claude/skills/; the sweep indexed five: cs, cs-refactor, cs-onboard, cs-feat, and cs-issue. Combined installs total ~38,530 across indexed listings (Sep 29, 2026 snapshot).

---

## Installation

```bash
npx skills add codestable/codestable
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| cs | 1488 | Core CodeStable workflow |
| cs-refactor | 1487 | Refactoring workflow |
| cs-onboard | 1486 | Codebase onboarding |
| cs-feat | 1469 | Feature delivery |
| cs-issue | 1465 | Issue handling |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Traceable features | Drive features and issues through cs-feat and cs-issue. |
| Agent onboarding | Prime agents with cs-onboard codebase context. |
| Controlled refactors | Run refactors under cs-refactor's human-in-the-loop gates. |

## Limitations / Verification

- Verified: skills.sh marketplace indexing captured Sep 29, 2026 (skill names, install counts, repo stars).
- The sweep verified 0/6 sampled SKILL.md paths because skills live under plugins/codestable/skills/ and .claude/skills/; install counts are from indexed listings. Repo README: https://raw.githubusercontent.com/codestable/codestable/main/README.md
- Not verified: no live `npx skills add` install test has been run for this family.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
