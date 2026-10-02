---
title: "Ziniao Skills - ERP and Store Automation Setup"
description: "Ziniao browser AI agent skills covering ERP management (staff/roles/devices) and store automation via ziniao-cli."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ziniao-open-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "e-commerce", "automation"]
---

# Ziniao Skills - Setup Guide

**Source:** [ziniao-open/skills](https://github.com/ziniao-open/skills)
**Skill family:** `ziniao-open/skills` (5 installable skills)
**Combined Installs:** ~65,073 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Automation
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

The Ziniao browser AI-agent skill pack, published under the ziniao-open organization, covers ERP management (staff, roles, devices, tags, departments) and store automation, adapted for the ziniao-cli and ZClaw local interface. The README (fetched Sep 29, 2026; Chinese, translated here) notes skills are now installed via `ziniao-cli skills install`. The sweep surfaced five skills: ziniao-page (5,270), ziniao-shared (5,268), ziniao-store (5,267), ziniao-staff (4,956), and ziniao-openapi-explorer (4,951).

---

## Installation

```bash
npx skills add ziniao-open/skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| ziniao-page | 5,270 | Ziniao page capabilities |
| ziniao-shared | 5,268 | ziniao-cli shared rules |
| ziniao-store | 5,267 | Store automation operations |
| ziniao-staff | 4,956 | Staff management operations |
| ziniao-openapi-explorer | 4,951 | OpenAPI endpoint exploration |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| ERP automation | Manage staff, roles, and departments through ziniao-staff and ziniao-page skills. |
| Store operations | Automate store workflows with ziniao-store. |
| API integration work | Explore Ziniao's API surface with ziniao-openapi-explorer before building integrations. |

## Limitations / Verification

- Verified: skills.sh indexing of Sep 29, 2026 (install counts as reported).
- Not verified: no live install test performed. Star count not captured in the sweep. The publisher's README recommends `ziniao-cli skills install` (after `npm install -g @ziniao-open/cli`) over the npx path.

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
