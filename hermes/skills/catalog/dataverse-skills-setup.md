---
title: "Dataverse Skills - Microsoft CRM and ERP Agent Setup"
description: "microsoft/Dataverse-skills: 3.1K combined installs across 11 listings that drive the Dataverse MCP server, CLI, SDK and PAC CLI"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dataverse-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "dataverse", "microsoft", "crm", "dynamics 365"]
---

# Dataverse Skills - Setup Guide

**Source:** [microsoft/dataverse-skills](https://www.skills.sh/microsoft/dataverse-skills) via skills.sh - 3.1K combined installs across 11 indexed listings; first seen Mar 23, 2026 (Nov 12, 2026 sweep)
**GitHub:** 257 stars, MIT license, `main` branch, last pushed 2026-11-11, 10 `SKILL.md` files under `.github/plugins/dataverse/skills/` plus plugin manifests for Claude Code and Cursor
**Category:** Microsoft data platform: Dataverse schema, queries, records, solutions and administration, plus Dynamics 365 Finance and Operations X++ and SQL access
**Quality Tier:** 🟡 Established - a first-party Microsoft pack with a permissive license, active development and specialist routing, held back by a Snyk Warn on the connect skill and a small skill count.

Dataverse is the data platform under Power Apps and Dynamics 365, and the skills in this pack exist to make an agent drive the tools Microsoft already ships: the Dataverse MCP server, the Dataverse CLI, the Python SDK and the PAC CLI. That framing matters. The agent is not reimplementing the platform, it is being taught which tool handles which request and what the constraints are.

The routing is the design. `dv-overview` loads first and directs each request to a specialist, and the specialists divide along the platform's own seams: metadata for the data model, query for reads, data for record operations, solution for lifecycle, security for roles and access, admin for environment settings. Two further skills leave Dataverse entirely and cover Dynamics 365 Finance and Operations: `erp-xpp` for the X++ build and deploy lifecycle, and `erp-sql` for explicitly approved read-only SQL access to a development environment.

The install distribution splits exactly along that line. The eight core Dataverse skills sit between 336 and 363 installs, tight enough to show a set install. `erp-xpp` draws 262, and `erp-sql` and `dv-python-sdk` draw 22 and 5, which is what a specialist finance-and-operations lane looks like next to the main platform.

One gap is worth knowing before you install: the tree carries 10 `SKILL.md` files, and `dv-python-sdk` is indexed but has no matching folder, so its documentation lives somewhere other than the skill tree.

## Installation

The quick install is a single command that takes all skills and asks which agent to install into:

```bash
npx skills add microsoft/Dataverse-skills -s "*"
```

Add `-g` to install globally so the skills are available in every project:

```bash
npx skills add microsoft/Dataverse-skills -s "*" -g
```

The repository also carries plugin manifests, so an agent that reads plugins can load it directly from the clone, and JetBrains IDEs have a native listing. After installing, the intended first step is to ask the agent to "Connect to Dataverse": the `dv-connect` skill fetches the helper scripts, walks through authentication and registers the MCP server.

You need a Dataverse environment. That comes through Power Apps, Dynamics 365 or a Power Platform plan, and the README points at the free Power Apps Developer Plan for a trial environment.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| dv-connect | 363 | One-time setup: installs the CLIs, authenticates, registers the MCP server and verifies the connection. |
| dv-metadata | 361 | Schema authoring and inspection: tables, columns, relationships, forms and views. |
| dv-overview | 359 | The routing layer: scope, skill map, tool capability reference and safety rules. |
| dv-solution | 356 | Solution lifecycle: create, export, import, promote across environments and validate. |
| dv-query | 349 | Reads, filters, pagination, aggregation and DataFrame loading over Dataverse records. |
| dv-data | 344 | Record CRUD, CSV import, multi-table loads with foreign keys and upsert by alternate key. |
| dv-security | 343 | Security roles, user access, application users, business units and admin elevation. |
| dv-admin | 336 | Environment administration: bulk delete, retention, org settings, recycle bin and audit. |

The remaining 3 indexed listings are erp-xpp (262 installs, the Finance and Operations X++ lifecycle), erp-sql (22, approved read-only SQL against a development environment) and dv-python-sdk (5, the Python SDK surface, which has no matching folder in the skills tree).

The tight band across the top eight is the intended usage: this is a pack you install as a set and let the overview route. The three tail skills are deliberately specialist and are worth installing only if the work involves Finance and Operations or direct SDK calls.

## Why This Matters for Hermes Agents

Business platforms are where agents most often produce confident nonsense, because the vocabulary is familiar and the constraints are not. A model asked to "add a field to the customer table" will write something plausible for a SQL database. Dataverse is not a SQL database. It has tables with logical names, columns with publisher prefixes, relationships with behaviours, and a solution layer that decides whether a change can be moved between environments.

The specialist split is how this pack addresses that. `dv-metadata` knows the model authoring rules, `dv-solution` knows that a change made outside a solution will not travel, and `dv-overview` knows which of them to call. An agent that starts from the overview asks for the publisher prefix and the target environment before it writes anything, which is exactly the question a DBA would ask first.

The read path has its own value. `dv-query` handles pagination, aggregation and DataFrame loading, which turns "how many open deals closed last quarter by region" from a session of trial and error into one request. For an operator, that is the difference between an agent that can answer a question about the CRM and one that can only describe how to answer it.

The administration skills deserve a warning rather than praise. `dv-admin` and `dv-security` can bulk delete, change retention and assign roles. That is real power over a production system, and it belongs behind an approval step that the pack does not provide.

## Usage

| You say | What happens |
|---|---|
| "Connect to our Dataverse environment" | Runs `dv-connect`: installs the CLIs, authenticates, registers the MCP server and verifies access. |
| "Show me the open opportunities over 50k in EMEA" | Queries records through `dv-query` with filtering, pagination and an aggregated result. |
| "Add a field for renewal date to the account table" | Uses `dv-metadata` with the correct logical naming, then packages the change in a solution. |
| "Import this CSV into the contact table" | Runs `dv-data` with foreign-key ordering and upsert rules rather than a raw insert loop. |
| "Promote this solution to the test environment" | Uses `dv-solution` for export, import and validation in the target environment. |
| "Give this team read access to the sales tables" | Assigns roles through `dv-security` and reports the effective access. |
| "Clean up the records flagged for deletion" | Uses `dv-admin` bulk delete, which is destructive and should be confirmed first. |

## Verification

The skills live under `.github/plugins/dataverse/skills/`, which is an unusual path and worth confirming before you script anything against it. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/Dataverse-skills/main/.github/plugins/dataverse/skills/dv-overview/SKILL.md | head -6
```

Check the connect skill as well, since it is the one that writes configuration:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/microsoft/Dataverse-skills/main/.github/plugins/dataverse/skills/dv-connect/SKILL.md
```

After installing, ask the agent which skills it sees. The overview should be loaded first and the eight specialists should be present; a partial install that skips the overview leaves skills that answer without routing.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dv-connect | Pass | Pass | Warn |
| dv-metadata | Pass | Pass | Pass |
| dv-overview | Pass | Pass | Pass |
| dv-solution | Pass | Pass | Pass |

The Warn is on `dv-connect`, and it is the expected one: that skill installs binaries, authenticates against a tenant and registers an MCP server. Every one of those actions is legitimate for a setup skill and every one is a capability a scanner should flag.

The wider risk is the administration surface. `dv-admin` can bulk delete and purge, `dv-security` can assign roles and elevate, `dv-solution` can promote code between environments. None of that is malicious, and all of it is irreversible in the wrong environment. Point the pack at a development environment first, and keep production behind an explicit confirmation step.

## Limitations

- Snapshot data, verified 2026-11-12: 3,100 combined installs across 11 indexed listings; 257 GitHub stars; MIT license; last pushed 2026-11-11. Counts drift over time.
- `dv-python-sdk` is indexed with 5 installs but has no matching folder in the skills tree, which carries 10 `SKILL.md` files for 11 listings.
- The pack assumes a Dataverse environment and the required licenses. Only the free Power Apps Developer Plan path is documented for a trial.
- The skills drive Microsoft tooling (MCP server, Dataverse CLI, Python SDK, PAC CLI) whose versions are not pinned. A CLI change moves the commands under the skills.
- The Finance and Operations lane is thin: two skills, one of which asks for explicitly approved temporary SQL access to a development environment and is installed by 22 people.
- Administration skills can delete, purge and reassign access. Nothing in the pack adds an approval gate, so the gate has to be in the agent or in the environment's own controls.

## Related

- [Microsoft Aspire Skills - .NET AppHost Agent Setup](/hermes/skills/catalog/aspire-skills-setup)
- [Microsoft Learn Agent Skills - Azure and .NET Docs](/hermes/skills/catalog/microsoftdocs-agent-skills-setup)
- [HVE Core - Microsoft Agentic SDLC Framework](/hermes/skills/catalog/hve-core-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let `dv-overview` start every session. It is the router, and the specialists are written to be called from it rather than directly.
- Ask for the publisher prefix before any schema change. Dataverse columns carry it, and a change with the wrong prefix is expensive to undo later.
- Do model edits inside a solution from the first change. Anything created outside a solution will not travel to the next environment, and retrofitting it is manual work.
- Use a development environment for the first admin task. Bulk delete and retention settings are the two operations where a mistaken target is unrecoverable.
- Ask the agent to quote the query it ran for a read. The pagination and aggregation behaviour is invisible in the result, and the query is what you would check.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
