---
title: "SAP Skills - BTP, CAP and ABAP Agent Suite"
description: "secondsky/sap-skills: 31.8K combined installs. Forty-five SAP skills covering BTP, CAP, ABAP, HANA, Fiori, SAPUI5 and AI Core development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sap-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "sap", "abap", "btp"]
---

# SAP Skills - Setup Guide

**Source:** [secondsky/sap-skills](https://www.skills.sh/secondsky/sap-skills) via skills.sh - 31.8K combined installs across 45 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [secondsky/sap-skills](https://github.com/secondsky/sap-skills) - 482 stars, GPL-3.0, branch main, last pushed 2026-10-31; 45 `SKILL.md` directories, 40 of them inside `plugins/<name>/skills/<name>/` and 5 more under `.agents/skills/`, each plugin carrying its own commands, agents and marketplace manifest beside the skill

**Category:** SAP enterprise development: BTP services, CAP applications, ABAP and integration patterns

**Quality Tier:** 🟡 Yellow - sap-btp-service-manager draws a Gen Agent Trust Hub Warn and web-perf draws a Snyk Warn, so the sample is not clean despite three skills passing every auditor

This is one of the largest SAP skill libraries on skills.sh, and it is packaged the way SAP teams actually work: one plugin per product area, marketed through the Claude and Codex marketplaces, with shared `SKILL.md` content that is meant to stay portable to OpenCode, Cursor, Gemini CLI and anything else that reads Agent Skills. The 40 plugins break down cleanly: three at the ABAP language level (ABAP, ABAP CDS and SQLScript), five for applications and frontends (CAP, Fiori tools, and `sapui5`, `sapui5-cli` and `sapui5-linter`), fifteen for BTP services from Connectivity and Destination through Integration Suite, Identity Services, Job Scheduling, Transport Management and Work Zone, three for HANA, four for SAC, two for API style and policy, and the rest covering Datasphere, AI Core, the Cloud SDK for AI and a browser automation helper.

The distinguishing habit is evidence tracking. The README states that public-source and package-registry verification is recorded per plugin in `docs/project/source-verification-ledger.json`, and individual skill frontmatter carries `last_verified` dates plus, where applicable, a blunt `production_tested` field. `sap-ai-core`, for instance, records "No; documentation-audited only, no live tenant/runtime evidence". That honesty is rare in this catalog and it changes how you should read the rest of the pack: treat the skills as well-sourced documentation rather than as proof that a given BTP flow works on your tenant.

## Installation

The README's portable route is the skills CLI, which installs the skill content without the Claude-specific extras:

```bash
npx skills add secondsky/sap-skills
```

The repository is also a native marketplace for both Claude Code and Codex, which is how most of its users take it:

```bash
/plugin marketplace add secondsky/sap-skills
/plugin install sap-cap-capire@sap-skills
/plugin install sap-cap-capire@sap-skills sap-fiori-tools@sap-skills
```

```bash
codex plugin marketplace add .
codex plugin add sap-abap@sap-skills
```

For CI or a shared checkout, the README documents a sparse Codex route that pulls only the registry and the plugin payloads:

```bash
codex plugin marketplace add https://github.com/secondsky/sap-skills.git --sparse .agents/plugins --sparse plugins
```

None of those routes knows about Hermes, so the durable install for this profile is a directory copy. The tree is two levels deep, so flatten it while copying, and do not forget the five generic skills that live outside `plugins/`:

```bash
git clone --depth 1 https://github.com/secondsky/sap-skills.git /tmp/sap-skills
cp -r /tmp/sap-skills/plugins/*/skills/*/. ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/sap-skills/.agents/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all 45. For a narrower install, name the plugin folders, for example `sap-abap`, `sap-abap-cds`, `sap-cap-capire`, `sap-fiori-tools` and `sap-btp-cloud-platform`, which is the loop for an ABAP Cloud or CAP project on BTP.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sap-abap | 1,296 | ABAP development across classic and cloud dialects: internal tables, ABAP SQL, RAP, EML, field symbols and ABAP Unit tests. |
| sap-fiori-tools | 1,193 | Fiori Elements and freestyle SAPUI5 apps through the Fiori tools extensions: Page Editor, annotations, Service Modeler and deployment to ABAP or Cloud Foundry. |
| sap-cap-capire | 1,174 | Building CAP applications: CDS models, service implementations, event handlers, OData services and deployment to Cloud Foundry or Kyma. |
| sap-btp-developer-guide | 1,092 | End to end BTP application development in CAP or ABAP Cloud, from runtime choice through HANA Cloud, Fiori, remote systems, CI/CD and observability. |
| sap-btp-best-practices | 1,060 | BTP architecture and account design: global accounts, directories, subaccounts, authentication, governance and failover. |
| sap-btp-connectivity | 969 | Destination and Connectivity services, Cloud Connector and Connectivity Proxy, including OAuth, principal propagation and the 405, 407 and 503 errors those flows produce. |
| sap-abap-cds | 969 | ABAP CDS view modelling: annotations, associations and cardinality, input parameters, DCL access control and the CURR and QUAN types. |
| sap-btp-cloud-logging | 879 | SAP Cloud Logging setup and operation: instance creation, ingestion from Cloud Foundry or Kyma, OpenTelemetry, and OpenSearch Dashboards analysis. |
| sapui5-cli | 842 | The UI5 Tooling CLI: project init, `ui5.yaml` configuration, builds, dev servers, custom tasks and middleware, and workspace layouts. |
| sap-api-style | 816 | Documenting SAP APIs to the SAP API Style Guide: naming, doc comments, OpenAPI specifications and the deprecation policy. |
| sap-ai-core | 752 | SAP AI Core and AI Launchpad: model deployment, orchestration workflows, RAG with vector stores, training pipelines and the Prompt Registry. |
| sap-hana-cli | 742 | The hana-cli developer tool for HANA: connecting, inspecting objects, managing HDI containers and converting metadata to CDS, EDMX or OpenAPI. |
| sap-sqlscript | 736 | SQLScript development: HANA procedures, AMDP methods, table functions, exception handling and performance work. |
| sapui5 | 726 | SAPUI5 application work: freestyle apps, XML views and controllers, JSON and OData models, routing, QUnit and OPA5 tests, accessibility. |
| sapui5-linter | 713 | Static analysis with the UI5 Linter: deprecated API detection, CSP and manifest checks, autofix and UI5 2.x migration preparation. |
| sap-btp-business-application-studio | 706 | Business Application Studio setup and use: subscriptions, dev spaces, external system connections, MTA deployment and runtime versions. |
| sap-cloud-sdk-ai | 702 | The SAP Cloud SDK for AI in JavaScript, TypeScript and Java: chat completion, embeddings, streaming, function calling and LangChain or Spring AI integration. |
| sap-btp-build-work-zone-advanced | 701 | Build Work Zone advanced edition: workspaces, UI Integration Cards, content packages, SCIM provisioning and Microsoft 365 or Teams integration. |
| sap-datasphere | 698 | SAP Datasphere data warehousing: analytic models, data and replication flows, spaces, connections, access controls and the datasphere CLI. |
| sap-btp-job-scheduling | 689 | The Job Scheduling Service on BTP: service setup, the REST API, schedule formats, OAuth 2.0, CF tasks and monitoring. |

The remaining 25 indexed listings range from 311 to 683 installs.

The tail is where the specialised platform services live: Cloud Transport Management, Master Data Integration, Service Manager, Integration Suite, Identity Services and Intelligent Situation Automation all sit just under the cutoff, along with the SAC trio (`sap-sac-scripting`, `sap-sac-planning`, `sap-sac-custom-widget`) and the five generic skills that ship in the same repository (`claude-automation-recommender`, `claude-md-improver`, `dependency-upgrade`, `grill-me`, `web-perf`).

## Why This Matters for Hermes Agents

SAP documentation is genuinely hard to use from an agent: the official help portal moved most of its content behind JavaScript-heavy pages, the useful details are spread across service-specific guides, and the same concept has different names in BTP, ABAP and CAP contexts. These skills carry the distilled version, with per-service reference folders, so an agent answering a Destination Service question does not have to reconstruct the API surface from a search result.

The plugins also encode sequencing that general knowledge gets wrong. `sap-btp-best-practices` owns account hierarchy and governance before anything is deployed, `sap-btp-connectivity` owns the Cloud Connector path that on-premise calls depend on, `sap-btp-job-scheduling` owns the OAuth 2.0 client and schedule formats, and `sap-datasphere` and `sap-sqlscript` own the data layer on either side of HANA. An agent working a BTP task in the wrong order produces advice that reads correctly and fails at the first subscription or entitlement.

For a general profile the cost is mostly tokens rather than risk: 40 plugins is a lot of markdown, so install the four or five that match the tenant in front of you. The five generic skills are worth knowing about for the opposite reason, since `web-perf`, `dependency-upgrade` and `claude-md-improver` have nothing to do with SAP and arrive with the same clone.

## Usage

| You say | What happens |
|---|---|
| "Create a CAP service over our existing HANA tables" | `sap-cap-capire` leads: CDS model, service definition, event handlers and the deployment target, with `sap-hana-cli` if the objects need inspecting first. |
| "Write an ABAP CDS view with a DCL restricting by company code" | `sap-abap-cds` supplies the view entity, annotations, association cardinality and the access control definition. |
| "Our on-premise RFC call returns 503 from BTP" | `sap-btp-connectivity` walks the destination, Cloud Connector and Connectivity Proxy chain, with the documented error triage. |
| "Set up a Fiori Elements list report on this OData service" | `sap-fiori-tools` handles Page Editor, annotations and Service Modeler, and `sapui5` picks up any freestyle controller work. |
| "Deploy this MTA to Cloud Foundry" | `sap-btp-cloud-platform` or `sap-btp-business-application-studio` takes it, depending on whether the project is built in BAS. |
| "Why is our scheduled job firing twice" | `sap-btp-job-scheduling` reads the schedule format and OAuth client setup, then checks run logs and the CF task path. |
| "Design the subaccount and role collection layout before we build" | `sap-btp-best-practices` works the account hierarchy, authentication and governance pattern first. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} sap-abap\n" \
  https://raw.githubusercontent.com/secondsky/sap-skills/main/plugins/sap-abap/skills/sap-abap/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and read one header:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/sap-* \
      ~/.hermes/profiles/corpusiq/skills/sapui5* \
      ~/.hermes/profiles/corpusiq/skills/claude-* \
      ~/.hermes/profiles/corpusiq/skills/dependency-upgrade \
      ~/.hermes/profiles/corpusiq/skills/grill-me \
      ~/.hermes/profiles/corpusiq/skills/web-perf | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/sap-abap/SKILL.md
```

The count should print 45, and the header should show `name: sap-abap`, a block `description:` opened with `|`, and `license: GPL-3.0`. Check that the reference folders survived the flatten as well, since the service skills keep most of their value there:

```bash
find ~/.hermes/profiles/corpusiq/skills/sap-btp-connectivity -type f -name "*.md" | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sap-abap | Pass | Pass | Pass |
| sap-hana-cli | Pass | Pass | Pass |
| sap-btp-service-manager | Warn | Pass | Pass |
| claude-automation-recommender | Pass | Pass | Pass |
| web-perf | Pass | Pass | Warn |

Two of the five sampled skills carry a warning, which is why this guide is tiered Yellow: `sap-btp-service-manager` is Warned by Gen Agent Trust Hub and `web-perf` by Snyk. Neither is a Fail, and the three SAP development skills sampled, including the largest plugin, are clean on all three auditors.

The install surface is larger than a markdown pack usually has. Forty plugins ship Claude-specific commands, agents, hooks, LSP configuration and MCP recipes beside the skills, and the README is explicit that in other clients those pieces should be treated as role guidance, prompt templates and connection recipes rather than as working automation. It also points at `docs/contributor-guide/mcp-manual-connections.md` before any server is configured, which is the right instinct: an MCP recipe that an agent follows unaided will try to reach a tenant with whatever credentials are in the environment.

Two skills reach outside the file system in ways worth reading before you enable them. `sap-sqlscript` and `sap-datasphere` both document inspecting a browser-based SAP editor through the Microsoft Edge DevTools protocol, and `sap-browser-automation` is a dedicated browser automation plugin; that means a live session with an authenticated SAP UI attached to a debugging port. Decide deliberately whether an agent should have that, and scope the session rather than leaving Edge listening.

The license is the other constraint. GPL-3.0 is copyleft, so redistributing a modified skill carries obligations that MIT-licensed packs do not, and the repository keeps a `THIRD-PARTY-NOTICES.md` for the material it vendored.

## Limitations

- Snapshot data, verified 2026-10-31: 31,778 combined installs across 45 indexed listings; 482 GitHub stars; GPL-3.0; last pushed 2026-10-31. Counts drift over time.
- The README calls this 40 plugins while the checkout holds 45 skills: 40 plugin directories plus five generic skills under `.agents/skills/`. Only 40 of the 45 have anything to do with SAP, and the other five (`claude-automation-recommender`, `claude-md-improver`, `dependency-upgrade`, `grill-me`, `web-perf`) arrive whether you want them or not, carrying 311 to 589 installs each.
- The index and the tree agree at 45, so there is no drift to work around here, but the counts are not a ranking. `sap-btp-job-scheduling` sits exactly at the 689 cutoff and `sap-btp-service-manager` just below it at 674, and popularity tracks which product area a reader searched for rather than which skill is best written.
- Verification is per plugin and uneven. Some frontmatter carries a `last_verified` date, `sap-ai-core` states plainly that it is documentation-audited with no live tenant evidence, and the README limits the claim to public-source and package-registry verification. Treat every flow as needing a tenant test.
- The Claude and Codex layers are not portable. Commands, agents, hooks, LSP configuration and MCP recipes degrade to prose in other clients, so a Hermes install gets the skills and none of the automation the README demonstrates.
- The BTP skills overlap by design. `sap-btp-developer-guide`, `sap-cap-capire` and `sap-btp-best-practices` all answer deployment and account questions from different angles, and `sapui5`, `sapui5-cli` and `sapui5-linter` split one framework three ways, so the routing decision is yours as often as the agent's.

## Related

- [Salesforce Skills Library (sf-skills) - 330+ Agent Skills Setup](/hermes/skills/catalog/salesforce-sf-skills-setup)
- [Celigo AI Skills - Celigo Integrations Setup](/hermes/skills/catalog/celigo-ai-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by product area, not in bulk. `sap-abap`, `sap-abap-cds` and `sap-sqlscript` cover the language tier, `sap-cap-capire` and `sap-fiori-tools` cover the application tier, and `sap-btp-cloud-platform` plus `sap-btp-connectivity` cover the platform tier; four or five folders is a working set, 45 is a token bill.
- Read the `production_tested` field before trusting a skill with a tenant change. It appears in the frontmatter of the newer plugins and it is the fastest way to tell a documented flow from a verified one.
- Skip the five generic skills when you copy the tree. They are unrelated to SAP, and `web-perf` is one of the two skills in this pack the auditors warn about.
- Keep the `references/` folders. The service skills are thin without them: the install documents the command surface, and the reference material holds the error codes and the exact payloads.
- Do not enable the browser inspection skills casually. `sap-browser-automation`, `sap-datasphere` and `sap-sqlscript` can drive an authenticated Edge session over CDP, which is a live SAP UI with your entitlements attached.
- Ask for the tenant version before an upgrade question. These skills track specific releases (`ui5-cli` 4.0.55, `ui5-linter` 1.22.0, framework 1.148.1 in `sapui5`), and an answer pitched at the wrong version is worse than no answer.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
