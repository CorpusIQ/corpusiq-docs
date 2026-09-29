---
title: "CopilotKit Skills - Dev Lifecycle Setup"
description: "Six CopilotKit agent skills for setup, development, integration, debugging, and v1-to-v2 migration; ~5,519 indexed installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/copilotkit-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "copilotkit", "generative ui"]
---

# CopilotKit Skills - Setup Guide

**Source:** [copilotkit/skills](https://github.com/copilotkit/skills) (38⭐)
**Skill family:** `copilotkit/skills` (6 installable skills)
**Combined Installs:** ~5,519 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

Published by the CopilotKit organization, this companion repository bundles six AI agent skills covering the CopilotKit lifecycle: quickstart (`copilotkit`), the AG-UI protocol, debugging, integrations, v2 development, and v1-to-v2 migration (`copilotkit-upgrade`). All six skills have indexed SKILL.md entries on skills.sh (6/6 as of the Sep 29, 2026 snapshot). It is a smaller, more focused alternative to the skill family in the main CopilotKit monorepo.

---

## Installation

```bash
npx skills add copilotkit/skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| copilotkit | 979 | Quickstart for CopilotKit |
| copilotkit-agui | 573 | AG-UI Protocol Skill |
| copilotkit-debug | 571 | CopilotKit Debugging Skill |
| copilotkit-integrations | 569 | CopilotKit Integrations |
| copilotkit-develop | 568 | CopilotKit v2 Development Skill |

The sixth skill, `copilotkit-upgrade` (CopilotKit v1 to v2 Migration Skill), has no published install count in the snapshot.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| New CopilotKit project | Start with the copilotkit quickstart skill |
| Legacy v1 app migration | Run copilotkit-upgrade for v1-to-v2 migration guidance |
| Troubleshooting agent UI | Use copilotkit-debug for structured debugging steps |

## Limitations / Verification

- All 6 skill SKILL.md entries were verified on skills.sh as of Sep 29, 2026; verification reflects indexed content, not an independent security audit.
- No live install test has been run from Hermes yet.

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
