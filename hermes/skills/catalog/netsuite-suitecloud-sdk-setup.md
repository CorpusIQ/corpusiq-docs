---
title: "NetSuite SuiteCloud - ERP Development Skills"
description: "oracle/netsuite-suitecloud-sdk: 8.2K combined installs across 11 listings, SuiteCloud SDK skills for NetSuite ERP and CRM customization."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/netsuite-suitecloud-sdk-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "netsuite", "erp", "suitecloud"]
---

# NetSuite SuiteCloud - Setup Guide

**Source:** [oracle/netsuite-suitecloud-sdk](https://www.skills.sh/oracle/netsuite-suitecloud-sdk) via skills.sh - 8.2K combined installs across 11 indexed listings; first seen Nov 14, 2026
**GitHub:** 383 stars, UPL-1.0 license, `master` branch, last pushed 2026-11-12, 16 `SKILL.md` files across `packages/agent-skills/` and `packages/ai-plugins/`
**Category:** ERP and CRM development skills for NetSuite SuiteCloud
**Quality Tier:** 🟠 Orange - one sampled skill fails the Gen Agent Trust Hub, and the repo is a full SDK under the UPL-1.0 license.

NetSuite SuiteCloud SDK is Oracle's set of tools for customizing NetSuite accounts and building SuiteApps through the SuiteCloud Development Framework (SDF). It is a full SDK rather than a prompt-only pack: the repo tracks 2,284 files spanning a Node.js CLI, a VS Code extension, unit testing, UIF types, AI agent plug-ins and the SuiteCloud Agent Skills, of which the index serves 11 listings with 8,165 combined installs.

The agent skills live under `packages/agent-skills/` and cover SuiteScript records and fields, SDF roles and permissions, project documentation, SuiteScript 1.0/2.0/2.x-to-2.1 migration, UIF SPA components, OWASP secure coding and SDF best practices. The license is Oracle's Universal Permissive License (UPL) Version 1.0, an uncommon permissive license rather than a standard MIT or Apache grant.

## Installation

The repo README documents the SuiteCloud SDK packages (CLI, VS Code extension, unit testing, UIF types) but no agent-skill install command. Install the skills with the standard skills.sh CLI:

```bash
npx skills add oracle/netsuite-suitecloud-sdk --skill 'netsuite-suitescript-records-reference' -g
```

Confirm the skill exists in the current tree first; see Limitations for the layout.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| netsuite-suitescript-records-reference | 1,120 | SuiteScript records and fields reference: field IDs, types, required status and search capabilities. |
| netsuite-sdf-roles-and-permissions | 961 | Generate or review SDF permission configs such as customrole XML and script deployments. |
| netsuite-sdf-project-documentation | 909 | Generate enterprise-grade documentation for SDF projects: scripts and object XML files. |
| netsuite-suitescript-upgrade | 889 | SuiteScript 1.0, 2.0 and 2.x to 2.1 migration: analyze, convert, explain and validate scripts. |
| netsuite-uif-spa-reference | 870 | Build, modify or debug NetSuite UIF SPA components with API and type lookup. |
| netsuite-owasp-secure-coding | 855 | OWASP secure coding with JavaScript/Node.js patterns and NetSuite SuiteScript guidance. |
| netsuite-ai-connector-instructions | 844 | NetSuite Intelligence skill teaching AI tool-selection order, output formatting and domain knowledge. |
| netsuite-sdf-safe-guide | 703 | NetSuite SDF best practices from the SAFE Guide (12 principles plus appendices). |

The remaining 3 indexed listings range from 3 to 531 installs.

## Why This Matters for Hermes Agents

SuiteCloud SDK gives a Hermes agent the reference material it needs to write NetSuite customizations correctly. The records-reference skill maps field IDs, types and search capabilities, while the upgrade skill turns SuiteScript 1.0/2.0 code into 2.1 and validates the result - the kind of mechanical migration an agent can perform at scale, but only if it has the field and API truth in front of it.

The SDF skills matter for traceability. sdf-roles-and-permissions and sdf-project-documentation turn agent output into reviewable artifacts - permission XML and project docs - which is what an ERP customization workflow needs before anything deploys to a production account.

The security skill is the important caveat. netsuite-owasp-secure-coding carries platform-agnostic OWASP patterns, but it is also the one sampled skill that fails the Gen Agent Trust Hub. An agent that emits SuiteScript should lean on the OWASP patterns while a human reviews the verdict before trusting generated code.

Finally, the repo is a full SDK, not a prompt pack: the skills sit beside a CLI, a VS Code extension and unit-testing tooling, so an agent can generate a customization while a human builds and deploys it with tooling from the same repository.

## Usage

| You say | What happens |
|---|---|
| "Look up the field IDs for a sales order record" | Runs netsuite-suitescript-records-reference for field IDs, types and search capabilities. |
| "Migrate this SuiteScript 1.0 file to 2.1" | Runs netsuite-suitescript-upgrade to analyze, convert and validate the script. |
| "Generate docs for this SDF project" | Runs netsuite-sdf-project-documentation over scripts and object XML. |
| "Review these customrole XML permissions" | Runs netsuite-sdf-roles-and-permissions against the permission config. |
| "Check this SuiteScript for OWASP issues" | Runs netsuite-owasp-secure-coding for injection, input validation and secure patterns. |
| "Help me build a UIF SPA component" | Runs netsuite-uif-spa-reference for API and type lookup. |

## Verification

Probe skills on the `master` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/oracle/netsuite-suitecloud-sdk/master/packages/agent-skills/netsuite-suitescript-records-reference/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/oracle/netsuite-suitecloud-sdk/master/packages/agent-skills/netsuite-sdf-roles-and-permissions/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/oracle/netsuite-suitecloud-sdk/master/packages/agent-skills/netsuite-owasp-secure-coding/SKILL.md
```

Skills live at `packages/agent-skills/<name>/SKILL.md` on the `master` branch.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| netsuite-suitescript-records-reference | Pass | Pass | Pass |
| netsuite-sdf-roles-and-permissions | Pass | Pass | Pass |
| netsuite-sdf-project-documentation | Pass | Pass | Pass |
| netsuite-suitescript-upgrade | Pass | Pass | Pass |
| netsuite-uif-spa-reference | Pass | Pass | Pass |
| netsuite-owasp-secure-coding | Fail | Pass | Pass |

Five of the six sampled skills pass all three auditors; netsuite-owasp-secure-coding fails the Gen Agent Trust Hub. The sample covers only 6 of the 11 indexed listings, so it says little about the remaining 5.

## Limitations

- Snapshot data, verified 2026-11-14: 8,165 combined installs across 11 indexed listings; 383 GitHub stars; UPL-1.0; last pushed 2026-11-12. Counts drift over time.
- The repo README documents the SuiteCloud SDK packages but no agent-skill install command; the npx skills command above is the standard fallback, not a documented one.
- The license is Oracle's Universal Permissive License (UPL) Version 1.0, an uncommon permissive license; review its terms before redistributing.
- This is a full SDK, not a prompt-only pack: 2,284 tracked files spanning a CLI, a VS Code extension, unit testing and UIF types, which the skill-level verdicts do not cover.
- One of six sampled skills fails the Gen Agent Trust Hub; the sample covers only 6 of 11 listings.

## Related

- [Oracle Skills - Database, OCI and APEX Guidance](/hermes/skills/catalog/oracle-skills-setup)
- [SAP Skills - BTP, CAP and ABAP Agent Suite](/hermes/skills/catalog/sap-skills-setup)
- [Open Mercato Skills - Enterprise ERP Engineering Setup](/hermes/skills/catalog/open-mercato-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with netsuite-suitescript-records-reference to ground field IDs and types before writing any SuiteScript.
- Pair netsuite-owasp-secure-coding with a human security review, since it is the sampled skill that fails the Gen Agent Trust Hub.
- Keep the `master` branch in every raw URL; the repo does not use `main`.
- Use the bundled SuiteCloud CLI and VS Code extension from the same repo to build and deploy what the skills generate.
- Treat the SDF skills (roles, permissions, docs, SAFE guide) as reviewable-artifact generators, not deployment shortcuts.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
