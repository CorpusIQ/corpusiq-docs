---
title: "Microsoft Power Platform Skills - Setup Guide"
description: "microsoft/power-platform-skills: Microsoft's Power Platform plugin marketplace for GitHub Copilot and Claude Code - 19.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/microsoft-power-platform-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "power platform", "microsoft", "copilot", "power apps"]
---

# Microsoft Power Platform Skills - Setup Guide

**Source:** [microsoft/power-platform-skills](https://www.skills.sh/microsoft/power-platform-skills) via skills.sh - 19.1K combined installs across 96 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) - 1,169 stars, MIT license, main branch, last pushed Nov 21, 2026; ten plugin directories under plugins/ (canvas-apps, code-apps, mcp-apps, mobile-apps, model-apps, pcf, power-apps-mobile-extension, power-automate, power-pages and process-intelligence) plus a scripts/install.js installer and plugin marketplace manifests at .claude-plugin/marketplace.json and .agents/plugins/marketplace.json.
**Category:** Low-Code App Development and Automation (Microsoft Power Platform)
**Quality Tier:** 🟢 Green - MIT license and 1,169 stars from Microsoft; the 20 sampled skills carry no Fail cells, with Snyk Warns on four skills (add-sharepoint, add-office365, genpage and add-mcscopilot).

Power Platform Skills is Microsoft's official plugin marketplace that teaches AI assistants such as GitHub Copilot and Claude Code to build on Power Platform. One marketplace adds ten plugins covering the platform's surfaces: canvas apps, code apps, model-driven apps, mobile apps, Power Pages sites, Power Automate cloud flows, PCF code components, MCP Apps widgets and Process Intelligence mining, with Dataverse maintained in a separate repository. Each plugin packages skills, agents and commands, and several wire up MCP servers so the assistant can talk directly to Power Platform services rather than only reading instructions.

The suite is broad but shallow in per-skill adoption: 96 indexed listings combine to 19.1K installs, and no single skill tops 400. That reflects a young marketplace shipping several plugins as preview rather than low quality. The repository is actively maintained by Microsoft, carries an MIT license and 1,169 stars, and ships one-command installers for both Claude Code and GitHub Copilot.

## Installation

The quick installer adds this plugin marketplace, installs every plugin except Dataverse, and turns on automatic updates:

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js | node
```

On Windows PowerShell:

```powershell
iwr https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js -OutFile install.js; node install.js; del install.js
```

The installer also installs the Power Platform CLI (pac) if it is missing and finds Claude Code and GitHub Copilot CLI on your computer. Pass --include-dataverse to also install the external Dataverse plugin. To install plugins manually from inside a Copilot CLI or Claude Code session, add the marketplace and install the plugins you want:

```bash
/plugin marketplace add microsoft/power-platform-skills
/plugin install power-pages@power-platform-skills
/plugin install model-apps@power-platform-skills
/plugin install canvas-apps@power-platform-skills
/plugin install code-apps-preview@power-platform-skills
/plugin install mobile-app@power-platform-skills
/plugin install power-apps-mobile-extension@power-platform-skills
/plugin install power-automate@power-platform-skills
/plugin install process-intelligence@power-platform-skills
/plugin install pcf@power-platform-skills
/plugin install mcp-apps@power-platform-skills
```

The repository ships plugin marketplace manifests at .claude-plugin/marketplace.json and .agents/plugins/marketplace.json, so these commands resolve against the repo directly. One-click install links on the plugin website add the same plugins through Claude Code and the GitHub Copilot app.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| add-sharepoint | 378 | add the SharePoint Online connector to a code app for lists, documents and SharePoint sites |
| create-code-app | 353 | scaffold a Power Apps code app with React and Vite |
| add-dataverse | 342 | add Dataverse tables to a code app with generated TypeScript models and services |
| configure-canvas-mcp | 335 | configure the Canvas Authoring MCP server before editing a canvas app |
| canvas-app | 332 | create or edit a canvas app through the Canvas Authoring MCP session |
| add-office365 | 322 | add the Office 365 Outlook connector for calendars, email and Outlook events |
| genpage | 296 | build, update or deploy generative pages for model-driven apps |
| add-excel | 294 | add the Excel Online (Business) connector for workbook data |
| add-mcscopilot | 284 | add the Microsoft Copilot Studio connector to invoke Copilot Studio agents |
| add-connector | 284 | add any Power Platform connector to a code app as a generic fallback |

The remaining 86 indexed listings range from 91 to 278 installs.

## Why This Matters for Hermes Agents

Power Platform Skills turns the low-code platform into something an agent can drive end to end, from scaffolding an app to publishing it to an environment. The value is the plugin architecture rather than any single skill: each plugin bundles skills, agents, commands and references, and the heavier surfaces wire up MCP servers so the assistant acts against Power Platform directly instead of guessing from docs. The connector skills (add-sharepoint, add-dataverse, add-excel and add-office365) absorb the fiddly Microsoft 365 and Dataverse wiring that makes up most of the platform's setup grunt work. Microsoft provenance with an MIT license and 1,169 stars matters for enterprise buyers, and the sampled security posture is clean: no Fail cells and no Gen Agent Trust Hub warnings across the 20 sampled skills. The real cost for a Hermes agent is the prerequisites, a Power Platform environment, Node.js and per-plugin extras such as the Azure CLI or the .NET SDK, plus the preview status of several plugins.

## Usage

| You say | What happens |
|---|---|
| Create a Power Pages site with React for a job board | Scaffolds a code site with React and deploys it to Power Pages |
| Build an app for tracking service requests | Builds a model-driven app with tables, forms, views, charts and a sitemap |
| Create a code app for tracking customer requests | Scaffolds a React and Vite code app connected to Power Platform |
| Add a SharePoint list to this code app | Adds the SharePoint Online connector and wires the list into the app |
| Create a flow that emails me when a SharePoint item is added | Builds a Power Automate cloud flow that triggers on the list change |
| Create a PCF star rating control for a model-driven form | Scaffolds and deploys a PCF code component with registration |
| Edit my Canvas App to add a new screen for reports | Connects the Canvas Authoring MCP server and edits the app's screens |

## Verification

Review a skill before installing it by fetching its SKILL.md directly from the repository:

```bash
curl -sL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/plugins/code-apps/skills/create-code-app/SKILL.md | head -40
```

Inspect the canvas authoring skill that backs canvas-app:

```bash
curl -sL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/plugins/canvas-apps/skills/canvas-app/SKILL.md | head -40
```

The installer reports which plugins it added, and the README documents `claude plugin update` and `copilot plugin update` for keeping them current.

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| add-sharepoint | Pass | Pass | Warn |
| create-code-app | Pass | Pass | Pass |
| add-dataverse | Pass | Pass | Pass |
| configure-canvas-mcp | Pass | Pass | Pass |
| canvas-app | Pass | Pass | Pass |
| add-office365 | Pass | Pass | Warn |
| genpage | Pass | Pass | Warn |
| add-excel | Pass | Pass | Pass |
| add-mcscopilot | Pass | Pass | Warn |
| add-connector | Pass | Pass | Pass |
| add-data-source | Pass | Pass | Pass |
| deploy | Pass | Pass | Pass |
| setup-datamodel | Pass | Pass | Pass |
| setup-auth | Pass | Pass | Pass |
| list-connections | Pass | Pass | Pass |
| add-teams | Pass | Pass | Pass |
| integrate-webapi | Pass | Pass | Pass |
| add-onedrive | Pass | Pass | Pass |
| add-azuredevops | Pass | Pass | Pass |
| add-datasource | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 22, 2026: 19.1K combined installs across 96 indexed listings; 1,169 GitHub stars; MIT license; last pushed Nov 21, 2026. Counts drift over time.
- Telemetry is on by default for several plugins (Power Pages, Model-driven apps, PCF, Mobile apps, Power Apps Mobile extensions and Power Automate); each plugin has a telemetry skill or an opt-out environment variable to turn it off.
- Only 20 of the 96 indexed listings have skills.sh security verdicts in this snapshot; the remaining 76 are unverified.
- Several plugins ship as preview or private preview (Code apps, Mobile apps, PCF and Power Apps Mobile extensions), so their interfaces may change.
- The Dataverse plugin is external and maintained in microsoft/Dataverse-skills, installed from that repository's default branch, and should not be installed twice.
- Plugins need a Power Platform environment with permission to create or change resources, Node.js, and per-plugin extras such as the Azure CLI or the .NET SDK.

## Related

- [Dataverse Skills - Microsoft CRM and ERP Agent Setup](/hermes/skills/catalog/dataverse-skills-setup)
- [Microsoft Fabric Skills - Power BI Agent Suite](/hermes/skills/catalog/microsoft-fabric-skills-setup)
- [Microsoft Azure AI Foundry Skills - Enterprise Agent](/hermes/skills/catalog/microsoft-azure-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start in a free developer environment rather than a tenant with live apps and data; the plugins ask before publishing, but a scratch environment keeps mistakes cheap.
- Install only the plugins you need; the quick installer adds everything except Dataverse, which pulls in tools you may not use.
- Read each permission request before approving; these plugins edit files, run shell commands and call MCP servers, and auto-approval gives the agent your own access.
- Turn telemetry off per plugin if you do not want usage data sent to Microsoft by default; run the plugin's telemetry skill or set its opt-out environment variable in scripts and CI.
- Use the report-issue skill bundled with most plugins to draft a bug report, or open an issue on the repository.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
