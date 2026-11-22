---
title: "NocoBase Skills - No-Code Platform Suite Setup"
description: "nocobase/skills: NocoBase's agent skills for no-code app building, data modeling, UI, ACLs, workflows and plugins - 4.0K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nocobase-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "nocobase", "no-code", "data modeling", "workflow"]
---

# NocoBase Skills - No-Code Platform Suite Setup

**Source:** [nocobase/skills](https://www.skills.sh/nocobase/skills) via skills.sh - 4.0K combined installs across 26 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [nocobase/skills](https://github.com/nocobase/skills) - 54 stars, no LICENSE file, main branch, last pushed Sep 4, 2026; 20 skill directories under `skills/<name>/SKILL.md`, with nocobase-ui-builder and nocobase-dsl-reconciler shipping the deepest trees (runtimes, reference libraries and template exports) alongside their SKILL.md.
**Category:** No-Code Platform Development (Data Modeling, UI, Workflows, ACLs and Plugins)
**Quality Tier:** 🟠 Orange - no LICENSE file and 54 stars; three of the 20 sampled skills carry a Snyk Fail (nocobase-ui-builder, nocobase-mcp-setup and nocobase-env-bootstrap), with Socket and Gen Agent Trust Hub Warns on a few more.

NocoBase publishes a set of domain-knowledge skills so AI agent CLIs (Claude Code, Codex, Cursor, OpenCode and similar) can build inside a NocoBase instance without hand-writing API calls. The skills span the platform's full surface: data modeling, UI authoring, workflow orchestration, ACL and role governance, plugin management and development, backup and migration, and environment bootstrap. Every skill description is pinned to "NocoBase 2 only; never use in a NocoBase 3 project", so the whole set targets the v2 line. The README carries an explicit publisher warning that the set is still a draft: "NocoBase Skills is still in draft status. The content is for reference and may change at any time."

The install story is automatic: `nb init` installs the skills during NocoBase CLI initialization, so no manual install is needed for agents working in an initialized directory. The install index outruns the tree: 20 of the 26 indexed listings have a SKILL.md directory in the repository, while six (nocobase-install-start, nocobase-mcp-setup, nocobase-env-bootstrap, nocobase-swagger-fetch, nocobase-api-call and nocobase-ai-employee-manager) carry install counts but no matching directory, and all six sit below 200 installs.

## Installation

The NocoBase CLI installs the skills automatically during initialization, so the install path is the NocoBase setup path itself:

```bash
npm install -g @nocobase/cli
mkdir my-nocobase && cd my-nocobase
nb init --ui
```

`nb init --ui` opens a browser configuration page to install a new NocoBase application or connect to an existing one, and installs the skills during that process. Then start the agent session in the initialized directory:

```bash
cd my-nocobase && claude   # or codex, cursor, etc.
```

A graphical AI tool (Claude Code Desktop, Cursor, Codex App) needs the initialized directory set as its working directory. To pull the skills directly instead, use the skills CLI:

```bash
npx skills add nocobase/skills
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nocobase-data-modeling | 384 | creating and changing collections, fields, relations and view-backed schemas |
| nocobase-workflow-manage | 351 | inspecting, creating, editing and diagnosing workflows, nodes and approvals through nb |
| nocobase-acl-manage | 348 | role lifecycle, permission policy, Portal entry access and risk assessment via nb CLI |
| nocobase-ui-builder | 338 | authoring Modern UI pages, blocks, fields and actions after portal-manage resolves a no-code Portal |
| nocobase-data-analysis | 303 | querying counts, groupings and distributions across collections via MCP |
| nocobase-utils | 297 | filter conditions, evaluator engines, expression syntax and UID generation references |
| nocobase-dsl-reconciler | 251 | opt-in YAML and DSL app building from spec files committed to git |
| nocobase-plugin-manage | 249 | inspecting, enabling and disabling plugins with nb plugin commands |
| nocobase-plugin-development | 241 | the step-by-step playbook for scaffolding and building a NocoBase plugin |
| nocobase-publish-manage | 226 | backup, restore and migration publish through nb api |

The remaining 16 indexed listings range from 4 to 180 installs.

## Why This Matters for Hermes Agents

NocoBase's set encodes a whole platform in skills, so an agent can drive collections, pages, workflows and roles from CLI calls instead of memorizing a web UI. The routing discipline is the part worth copying: nocobase-portal-manage is the single dispatcher for every UI request, resolving exactly one enabled Portal from structured output before it hands off to nocobase-ui-builder, and it refuses to guess when multiple Portals match. That two-stage handoff keeps the authoring skill from acting on an ambiguous target. The DSL reconciler is explicitly opt-in and warns agents to prefer the live-UI path for ordinary edits, a guardrail against using a heavyweight tool where a light one fits. The per-skill "NocoBase 2 only" pin is the kind of version fence that prevents silent breakage when the platform ships a v3. For Hermes operators the caveats are the missing license file and the three Snyk Fail cells in the sampled verdicts, plus a publisher warning that the set is still a draft and may change.

## Usage

| You say | What happens |
|---|---|
| Create a contacts collection with an owner field | nocobase-data-modeling inspects or creates the collection, fields and relations through the data-modeling surface |
| Add an approval step to this workflow | nocobase-workflow-manage edits the workflow nodes and approval surfaces with version-safe nb commands |
| Only let the sales role open this Portal | nocobase-acl-manage adjusts the role permission policy and Portal entry access through nb CLI |
| Add a dashboard page to this app | nocobase-portal-manage resolves the Portal, then nocobase-ui-builder authors the page and blocks |
| Export this app as YAML I can commit | nocobase-dsl-reconciler runs the opt-in DSL path and pushes spec files to the workspaces project |
| Check which plugins are enabled | nocobase-plugin-manage lists the plugins and can enable or disable them with nb plugin commands |
| Back up this app before migrating | nocobase-publish-manage runs the backup, restore or migration publish via nb api |

## Verification

Confirm the top skill landed and read its routing before use:

```bash
curl -sL https://raw.githubusercontent.com/nocobase/skills/main/skills/nocobase-data-modeling/SKILL.md | head -40
```

Review the dispatcher that every UI request routes through:

```bash
curl -sL https://raw.githubusercontent.com/nocobase/skills/main/skills/nocobase-portal-manage/SKILL.md | head -40
```

Inspect the workflow skill's node and trigger coverage before driving workflows:

```bash
curl -sL https://raw.githubusercontent.com/nocobase/skills/main/skills/nocobase-workflow-manage/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nocobase-data-modeling | Pass | Pass | Pass |
| nocobase-workflow-manage | Warn | Warn | Pass |
| nocobase-acl-manage | Pass | Pass | Pass |
| nocobase-ui-builder | Pass | Warn | Fail |
| nocobase-data-analysis | Pass | Pass | Warn |
| nocobase-utils | Pass | Pass | Pass |
| nocobase-dsl-reconciler | Warn | Warn | Pass |
| nocobase-plugin-manage | Pass | Pass | Pass |
| nocobase-plugin-development | Pass | Pass | Warn |
| nocobase-publish-manage | Pass | Pass | Pass |
| nocobase-env-manage | Pass | Pass | Warn |
| nocobase-ai-employee | Pass | Pass | Pass |
| nocobase-install-start | Pass | Pass | Pass |
| nocobase-mcp-setup | Pass | Pass | Fail |
| nocobase-revision | Pass | Pass | Pass |
| nocobase-prototype-repro | Pass | Warn | Pass |
| nocobase-notification-manage | Pass | Pass | Pass |
| nocobase-env-bootstrap | Pass | Pass | Fail |
| nocobase-portal-manage | Pass | Pass | Pass |
| nocobase-ai-manager | Pass | Pass | Pass |

The repository has no LICENSE file at the root, so redistribution and modification rights are unresolved.

## Limitations

- Snapshot data, verified Nov 22, 2026: 3,991 combined installs across 26 indexed listings; 54 GitHub stars; no LICENSE file; last pushed Sep 4, 2026. Counts drift over time.
- The README warns that the set is still a draft: "NocoBase Skills is still in draft status. The content is for reference and may change at any time."
- Every skill is pinned to NocoBase 2 and must not be used in a NocoBase 3 project.
- Six indexed listings (nocobase-install-start, nocobase-mcp-setup, nocobase-env-bootstrap, nocobase-swagger-fetch, nocobase-api-call and nocobase-ai-employee-manager) have install counts but no directory in the current tree.
- There is no LICENSE file at the repository root, so redistribution and modification rights are unclear.
- The 20 sampled skills are a subset of the 26 indexed listings; the remaining six carry no skills.sh security verdict in this snapshot.

## Related

- [Customware Skills - Low-Code App Builder Suite Setup](/hermes/skills/catalog/customware-ai-skills-setup)
- [Base44 Skills - AI App Builder Platform Suite Setup](/hermes/skills/catalog/base44-skills-setup)
- [n8n Skills - Workflow Automation for Business](/hermes/skills/catalog/n8n-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Route every UI request through nocobase-portal-manage first; it resolves the Portal and picks the builder, and bypassing it for nocobase-ui-builder skips the required resolution check.
- Reach for nocobase-dsl-reconciler only when the user explicitly asks for YAML, DSL or git-committed spec files; for ordinary page and block edits the live-UI path is the default.
- Keep in mind the set is NocoBase 2 only; confirm the instance version before letting any skill touch a project.
- Read each SKILL.md before first use; the set is still in draft status and the publisher warns the content may change.
- The repository has no LICENSE file, so treat redistribution and modification rights as unresolved before relying on these skills for production work.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
