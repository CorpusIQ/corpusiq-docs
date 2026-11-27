---
title: "Serac Skills - ServiceNow MCP Agent Guides Setup"
description: "serac-labs/serac - 3.4K combined installs: a ServiceNow MCP server plus skill guides that teach an agent to use its 400+ snow_* tools."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/serac-labs-serac-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "servicenow", "mcp", "itsm"]
---

# Serac Skills - Setup Guide

**Source:** [serac-labs/serac](https://www.skills.sh/serac-labs/serac) via skills.sh - 3.4K combined installs across 73 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [serac-labs/serac](https://github.com/serac-labs/serac) - 77 stars, Apache-2.0 license, last pushed Oct 20, 2026, main branch; 70 skill guides under packages/skills/<name>/SKILL.md plus the @serac-labs/servicenow-mcp server package.
**Category:** ServiceNow MCP and Agent Skills (Serac Labs)
**Quality Tier:** 🟡 Yellow - 20 of 73 listings sampled: 0 Fail and 6 Warn cells (five Snyk Warns, one Gen Agent Trust Hub Warn), all other cells Pass.

serac-labs/serac is a ServiceNow MCP server plus the skill guides that teach an agent to use it. The server, published on npm as @serac-labs/servicenow-mcp, exposes 400+ snow_* tools over stdio or streamable HTTP and is the actual integration surface: it is what connects an MCP client to a ServiceNow instance. The skills, in the @serac-labs/skills package, are plain markdown guides an agent loads into its prompt so it uses those tools like a practitioner, knowing which update set to be in, why a Business Rule needs ES5, and what to check before renaming a field.

Install counts are flat and small: the top listings (vendor-management and document-management) sit at 101 installs each, and the 73 indexed listings total 3,412 combined installs, so this is a niche enterprise publisher rather than a high-volume one. Because the catalog is far larger than a context window, tools are deferred by default: tools/list returns two meta-tools and the model widens its own surface as it works, with blast-radius impact analysis for judging the scope of a change before making it.

## Installation

The server installs globally from npm:

```bash
npm install -g @serac-labs/servicenow-mcp
```

Point an MCP client at the servicenow-mcp-stdio binary with three environment variables: SNOW_INSTANCE (your instance URL), SNOW_CLIENT_ID, and SNOW_CLIENT_SECRET. Credentials come from an OAuth application registry entry on the instance (System OAuth > Application Registry); a free developer instance from developer.servicenow.com is enough to try everything.

```json
{
  "mcpServers": {
    "servicenow": {
      "command": "servicenow-mcp-stdio",
      "env": {
        "SNOW_INSTANCE": "https://dev12345.service-now.com",
        "SNOW_CLIENT_ID": "your-client-id",
        "SNOW_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

If nothing works, ask the server what is wrong before changing anything:

```bash
servicenow-mcp-stdio --doctor
```

The report names the credential source used, whether the URL is usable, whether the instance is awake, whether the OAuth exchange succeeds, and which roles the account holds. As a Claude Code plugin, the repository is a plugin marketplace, so the server and all skills arrive in one step:

```
/plugin marketplace add serac-labs/serac
/plugin install servicenow@serac
```

The server runs through npx, so nothing has to be installed first. Other clients copy the mcpServers block from the repo root .mcp.json into .cursor/mcp.json (Cursor), ~/.codeium/windsurf/mcp_config.json (Windsurf), or .vscode/mcp.json (VS Code, which names the block servers). The skills themselves are directories holding a SKILL.md; nothing loads them automatically, so copy the ones you want into your agent's skills directory or read them from the package via skillsRoot().

## What It Provides

skills.sh publishes per-skill install counts for all 73 indexed listings. The 17 listings at or above 60 installs are listed below; the rest are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| vendor-management | 101 | manage core_company vendors and ast_contract with renewal alerts and SLA tracking |
| document-management | 101 | move attachment bytes in and out and generate documents from templates |
| knowledge-management | 92 | create kb_knowledge articles, workflow, search, and feedback rating |
| email-notifications | 88 | build sysevent_email_action notifications with templates and mail scripts |
| approval-workflows | 85 | configure approval rules and sysapproval_approver records |
| reporting-dashboards | 83 | build sys_report reports and sys_dashboard layouts |
| asset-management | 77 | manage hardware, software licenses, and lifecycle on alm_hardware/alm_license |
| predictive-intelligence | 72 | use sn_ml predictors for classification, similarity, and clustering |
| change-management | 71 | create and transition change requests and change tasks |
| mcp-tool-discovery | 70 | find and call tools on this MCP server via its meta-tools |
| grc-compliance | 69 | build GRC policy lifecycle, controls, risk assessment, and audits |
| scheduled-jobs | 67 | create sysauto_script scheduled jobs with cron patterns and batch limits |
| import-export | 65 | move data in and out with import sets, transforms, and exports |
| field-service | 65 | build wm_order work orders, tasks, and technician dispatch |
| cmdb-patterns | 62 | create CIs and cmdb_rel_ci relationships and walk impact |
| event-management | 61 | push em_event events, rules, correlation, and rollups |
| hr-service-delivery | 60 | build sn_hr_core_case and lifecycle events for onboarding/offboarding |

The remaining 56 indexed listings range from 4 to 59 installs.

## Why This Matters for Hermes Agents

The value here is the integration surface, not the install volume. A Hermes agent that already drives MCP servers gains a full ServiceNow toolkit: 400+ snow_* tools covering incident, change, CMDB, GRC, HR, field service, and platform development, each matched to a skill guide that encodes the judgement needed to use it safely on a production instance. Because the catalog is far larger than a context window, the server defers tools by default and lets the model widen its own surface on demand, keeping the prompt small while the whole toolkit stays reachable. The blast-radius analysis tools are the standout for cautious builders: they map which apps, fields, update sets, and dependents a change will touch before it is made. The skill guides are plain markdown, so a host agent can load only the ones relevant to the current task. Both the server and the skills work with any MCP client, and neither requires the Serac product.

## Usage

| You say | What happens |
|---|---|
| Which snow_* tools handle incidents | Uses mcp-tool-discovery to find and enable the incident tools via the meta-tools |
| Create an incident with priority 1 | Uses the incident tools to create the record with impact/urgency priority calculation |
| What will this change break | Uses the blast-radius tools to map affected apps, fields, and update sets |
| Review this Business Rule for ES5 problems | Uses the es5-compliance guide to check the script against ES5 constraints |
| Which update set should I work in | Uses the update-set-workflow guide to place the change in the right update set |
| Notify me when an incident is created | Uses email-notifications to build a sysevent_email_action with a template |
| Rename this field safely | Uses the relevant guide to check references before renaming |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/serac-labs/serac/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/serac-labs/serac/main/packages/skills/es5-compliance/SKILL.md | head -40
```

Both URLs return 200. After installing, review each packages/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| vendor-management | Pass | Pass | Pass |
| document-management | Pass | Pass | Warn |
| knowledge-management | Pass | Pass | Warn |
| email-notifications | Pass | Pass | Pass |
| approval-workflows | Pass | Pass | Warn |
| reporting-dashboards | Pass | Pass | Pass |
| asset-management | Pass | Pass | Pass |
| predictive-intelligence | Pass | Pass | Pass |
| change-management | Pass | Pass | Warn |
| mcp-tool-discovery | Pass | Pass | Pass |
| grc-compliance | Pass | Pass | Pass |
| scheduled-jobs | Pass | Pass | Pass |
| import-export | Pass | Pass | Pass |
| field-service | Pass | Pass | Pass |
| cmdb-patterns | Pass | Pass | Pass |
| event-management | Pass | Pass | Warn |
| hr-service-delivery | Warn | Pass | Pass |
| rest-integration | Pass | Pass | Pass |
| incident-management | Pass | Pass | Pass |
| flow-designer | Pass | Pass | Pass |

Across the 20 sampled skills there are 54 Pass, 6 Warn, and 0 Fail cells. Five skills carry a single Snyk Warn each (document-management, knowledge-management, approval-workflows, change-management, event-management) and one carries a single Gen Agent Trust Hub Warn (hr-service-delivery).

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,412 combined installs across 73 indexed listings; 77 GitHub stars; Apache-2.0 license; last pushed Oct 20, 2026. Counts drift over time.
- The install band is flat: the top listings sit at 101 installs and the long tail bottoms out at 4, so this is a niche enterprise publisher rather than a high-volume skill suite.
- The install index outruns the tree: 73 listings are indexed but the current packages/skills/ tree carries 70 skill directories; snow-flow-commands, bun-file-io, and effect carry install counts with no matching directory.
- The README's package table says 57 skill guides while its plugin section says all 70 skills arrive; the current tree carries 70 directories.
- skills.sh sampled only 20 of the 73 indexed listings for security verdicts; the other 53 carry no published verdict.
- The @serac-labs/skills npm package has no trusted publisher yet, so no version has shipped to npm, per the README's releases section.

## Related

[Salesforce Skills Library (sf-skills) - 330+ Agent Skills Setup](/hermes/skills/catalog/salesforce-sf-skills-setup) | [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup) | [ECC Engineering Skills - Enterprise Engineering Suite Setup](/hermes/skills/catalog/ecc-engineering-skills-setup) | [SAP Skills - BTP, CAP and ABAP Agent Suite](/hermes/skills/catalog/sap-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run servicenow-mcp-stdio --doctor first whenever a call looks broken; it names the credential source and whether the instance is awake.
- Leave SNOW_LAZY_TOOLS at its default so the deferred catalog stays small, and widen the tool surface on demand.
- Load only the skill guides relevant to the current task; they are plain markdown and nothing loads them automatically.
- Start reading with the es5-compliance, update-set-workflow, and blast-radius guides, which the README recommends first.
- Use the blast-radius tools before a risky change to map the apps, fields, and update sets it will touch.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
