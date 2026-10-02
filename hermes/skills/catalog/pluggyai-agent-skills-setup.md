---
title: "PluggyAI Agent Skills - Open Finance Setup"
description: "Skills for building with Pluggy open finance APIs: integration guidance, payments, and connector health diagnostics (~1.5K installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pluggyai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "open finance", "fintech"]
---

# PluggyAI Agent Skills - Setup Guide

**Source:** [pluggyai/agent-skills](https://github.com/pluggyai/agent-skills) (6⭐)
**Skill family:** `pluggyai/agent-skills` (4 installable skills)
**Combined Installs:** ~1,484 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Finance
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

PluggyAI publishes this vendor skill family for agents working with Pluggy, an open finance data platform. The four skills cover open finance data access (pluggy-open-finance), integration guidance (pluggy-integration), payments (pluggy-payments), and connector health diagnostics (pluggy-doctor). All four SKILL.md files were verified during the Sep 29, 2026 sweep.

---

## Installation

```bash
npx skills add pluggyai/agent-skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| pluggy-open-finance | 434 | Pluggy Open Finance data access |
| pluggy-integration | 407 | Pluggy integration guidance |
| pluggy-payments | 322 | Pluggy payments support |
| pluggy-doctor | 321 | Pluggy connector diagnostics |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Open finance data access | Use pluggy-open-finance to connect agents to Pluggy financial data APIs |
| Integration planning | Follow pluggy-integration for wiring Pluggy into an application |
| Connector troubleshooting | Run pluggy-doctor to diagnose Pluggy connector health |

## Limitations / Verification

- skills.sh indexing verified Sep 29, 2026: 4 of 4 SKILL.md paths verified; all install counts are from the Sep 29, 2026 snapshot.
- No live install test performed.
- Pluggy API credentials are not bundled; agents must supply their own Pluggy authentication.

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
