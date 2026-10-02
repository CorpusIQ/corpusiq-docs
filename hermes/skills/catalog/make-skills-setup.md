---
title: "Make Skills - Automation Platform Suite Setup"
description: "Setup guide for integromat/make-skills - 5 official Make.com agent skills: scenario building, MCP reference, module configuring, E2B code execution."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/make-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "make", "automation", "integromat", "mcp"]
---

# Make Skills - Setup Guide

**Source:** [integromat/make-skills](https://github.com/integromat/make-skills) (121⭐, pushed Sep 25, 2026)
**Skill:** `integromat/make-skills` (5 installable skills)
**Installs:** ~330 per top skill, ~1.6K combined (Sep 27, 2026 snapshot)
**Category:** Automation / iPaaS
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

Make (formerly Integromat), one of the largest automation platforms, ships five official agent skills. Agents can build and configure Make scenarios (`make-scenario-building`, `make-module-configuring`), look up modules through an MCP reference (`make-mcp-reference`), wire custom API connections (`make-api-shell-connection-workflow`), and execute code inside scenarios via E2B (`make-e2b-code-execution`). This gives agents a governed path to build and modify client automations on Make's visual canvas.

---

## Installation

```bash
# Full suite
npx skills add integromat/make-skills

# Scenario building only
npx skills add integromat/make-skills --skill make-scenario-building
```

## Roster - 5 Skills

| Skill | Installs | Does |
|---|---|---|
| make-scenario-building | 373 | Design and assemble complete Make scenarios |
| make-mcp-reference | 361 | Query the Make module catalog via MCP |
| make-module-configuring | 356 | Configure module fields, filters, and mappings |
| make-api-shell-connection-workflow | 327 | Build custom API-shell connections |
| make-e2b-code-execution | 230 | Execute sandboxed code (E2B) inside scenarios |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Client automation delivery** | Agents can build Make scenarios for operators end to end |
| **CorpusIQ internal automations** | Prototype integrations before building native connectors |
| **MCP reference pattern** | `make-mcp-reference` is a working example of a module catalog exposed via MCP |
| **Code-in-automation** | `make-e2b-code-execution` covers the sandboxed-code gap in iPaaS flows |

## Limitations / Verification

- Requires a Make account and scenario permissions (org-level, not free-tier only)
- Skills orchestrate Make's APIs; complex scenarios still benefit from human review
- Verify: `npx skills add integromat/make-skills --list` shows 5 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [n8n Skills Setup](/hermes/skills/catalog/n8n-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
