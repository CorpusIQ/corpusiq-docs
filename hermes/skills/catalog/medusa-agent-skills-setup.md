---
title: "Medusa Agent Skills - Official Ecommerce Platform Setup"
description: "Setup guide for medusajs/medusa-agent-skills: 39.4K combined installs. Official Medusa skills for building, deploying, and learning the ecommerce platform."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/medusa-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-09"
tags: ["hermes skill", "agent skill", "skill setup", "ecommerce", "medusa", "storefront"]
---

# Medusa Agent Skills - Setup Guide

**Source:** [medusajs/medusa-agent-skills](https://www.skills.sh/medusajs/medusa-agent-skills) via skills.sh - 39.4K combined installs across 19 indexed listings; first seen Oct 9, 2026 (evening sweep)
**GitHub:** [medusajs/medusa-agent-skills](https://github.com/medusajs/medusa-agent-skills) (228 stars; no LICENSE file in the repository - review terms before production use; very active - pushed Oct 5, 2026; 18 skills across 4 Claude Code plugins under `plugins/`: medusa-dev, learn-medusa, ecommerce-storefront, and medusa-cloud)
**Category:** Ecommerce Development / Medusa Platform / Agent Skills
**Quality Tier:** 🟢 Production - official Medusa org (open-source ecommerce platform), very active (pushed Oct 5, 2026); 39.4K combined installs across 19 indexed listings; all sampled verdicts Pass/Pass/Pass; note: no LICENSE file in the repository

Medusa is an open-source ecommerce platform, and medusa-agent-skills is the Medusa team's official agent-skills repository. It ships 18 skills as four Claude Code plugins: medusa-dev (comprehensive skills for building Medusa applications across backend, admin UI, and storefronts), learn-medusa (an interactive tutorial that teaches Medusa concepts by building a brands feature), ecommerce-storefront (building high-converting storefronts), and medusa-cloud (managing Medusa Cloud resources through the Cloud CLI, mcloud). The README notes that the skills can be used with any agent, not just Claude Code.

The four most-installed skills all cover building: building-with-medusa (4.3K installs), storefront-best-practices (4.3K), building-admin-dashboard-customizations (4.2K), and building-storefronts (3.9K), followed by the database and onboarding skills (db-migrate, learning-medusa, db-generate, new-user) at 2.8K to 3.2K. The medusa-cloud plugin covers the Cloud lifecycle as single-purpose skills - auth, projects, environments, variables, deployments, logs, and organizations - most in the 1.2K range.

---

## Installation

```bash
# Claude Code: add the Medusa marketplace, then install a plugin
/plugin marketplace add medusajs/medusa-agent-skills
/plugin install medusa-dev@medusa

# Verify the plugin loaded (README)
/plugin
```

Repeat the install step with `learn-medusa`, `ecommerce-storefront`, or `medusa-cloud` to add the other plugins. For other agents, the README documents two paths:

```bash
# Copy skills into the skills directory for your agent
yarn skills add medusajs/medusa-agent-skills
```

The `skills add` path copies skills only - it cannot copy MCP server configuration. Manual installation covers both: copy the plugin's skill directories into the agent's skills folder and place the MCP server configuration in the agent's config file (the README's example uses `.cursor/skills/` and `.cursor/mcp.json`).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| building-with-medusa | 4,339 | Core skill for building Medusa applications - backend, admin UI, and storefronts |
| storefront-best-practices | 4,313 | High-converting ecommerce storefront practices |
| building-admin-dashboard-customizations | 4,183 | Customizing the Medusa admin dashboard |
| building-storefronts | 3,947 | Storefront development |
| db-migrate | 3,210 | Running database migrations |
| learning-medusa | 3,187 | Interactive tutorial - learn Medusa concepts by building a brands feature |
| db-generate | 3,160 | Generating database migrations |
| new-user | 2,828 | First-run onboarding |
| using-medusa-cloud | 1,273 | Medusa Cloud orientation via the mcloud CLI |
| mcloud-deployments | 1,222 | Managing deployments in Medusa Cloud |
| mcloud-environments | 1,210 | Managing environments in Medusa Cloud |
| mcloud-variables | 1,209 | Managing environment variables in Medusa Cloud |
| mcloud-projects | 1,207 | Managing projects in Medusa Cloud |
| mcloud-logs | 1,206 | Reading logs in Medusa Cloud |
| mcloud-organizations | 1,205 | Managing organizations in Medusa Cloud |
| creating-agents-in-medusa | 898 | Creating agents in Medusa |
| mcloud-local | 698 | Local Medusa Cloud development |

The remaining two listings are creating-internal-agents (46 installs) and mcloud-auth (36). Note: `creating-agents-in-medusa` (898) has no counterpart in the current `plugins/` tree; the shipped medusa-dev skill is `creating-internal-agents`.

## Why This Matters for Hermes Agents

Agent-written ecommerce code drifts from platform conventions quickly - ad-hoc data models and hand-rolled patterns in places where the platform already has an answer. These skills are the platform vendor's own counterweight, encoding Medusa's module, workflow, and migration patterns as instructions an agent executes. They ship as plain Markdown skills and commands, so a Hermes agent uses them like any other skill: copy the directories in, or install the plugin where the harness supports plugins. Coverage lands in the places ecommerce builds usually need help: db-generate and db-migrate keep schema changes tied to migrations, building-admin-dashboard-customizations keeps admin extensions on Medusa's component conventions, and storefront-best-practices applies conversion-oriented storefront patterns. The medusa-cloud family extends the same agent to deployments, environments, and logs through the mcloud CLI. The README's privacy note - skills are local files, and MCP servers query only public Medusa documentation - keeps the integration surface small for teams with strict data policies.

## Usage

| You say | What happens |
|---|---|
| "Teach me Medusa by building something real" | learning-medusa runs an interactive tutorial that builds a brands feature step by step |
| "Start a new Medusa project" | building-with-medusa guides the scaffold and conventions, with new-user for first-run setup |
| "Build a storefront for my Medusa backend" | building-storefronts handles the integration; storefront-best-practices layers on conversion patterns |
| "Customize the admin dashboard" | building-admin-dashboard-customizations applies Medusa's admin extension patterns |
| "My model change needs a migration" | db-generate generates the migration; db-migrate applies it |
| "Deploy this project to Medusa Cloud" | mcloud-deployments drives the deployment, with mcloud-environments and mcloud-logs for follow-up |
| "Find out what happened to my Medusa Cloud project" | mcloud-logs reads the project's logs |

## Verification

```bash
# Claude Code: confirm the plugin is loaded (README)
/plugin

# Other agents: confirm copied skills landed in the agent's skills directory
ls .cursor/skills/ | grep -iE "building-|storefront-best-practices|learning-medusa|mcloud-|new-user|db-"

# Review a skill's SKILL.md directly before installing (no rate limits)
curl -s https://raw.githubusercontent.com/medusajs/medusa-agent-skills/main/plugins/medusa-dev/skills/building-storefronts/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 9, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| building-storefronts | Pass | Pass | Pass |
| building-admin-dashboard-customizations | Pass | Pass | Pass |
| storefront-best-practices | Pass | Pass | Pass |

All three sampled skills pass all three scanners. The README states that the plugins do not collect, store, or transmit any user data or conversation information, and that MCP servers query only public Medusa documentation. Note that the repository carries no LICENSE file (see Limitations).

## Limitations

- The repository carries no LICENSE file - confirm licensing terms with the Medusa team before production or redistribution use.
- Claude Code is the first-class install path; other agents copy skill directories manually or run `yarn skills add`, which cannot copy MCP server configuration.
- The mcloud skills target Medusa Cloud through the mcloud CLI, so a Medusa Cloud account and the CLI are prerequisites for that family.
- `creating-agents-in-medusa` (898 installs) has no counterpart in the current `plugins/` tree; the shipped medusa-dev skill is `creating-internal-agents` (46 installs).
- Snapshot data, verified Oct 9, 2026: 39,377 combined installs across 19 indexed listings; 228 GitHub stars; no LICENSE file; last pushed Oct 5, 2026. Counts drift over time.

## Related

- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup) - component-layer workflows for React admin and storefront UI
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup) - framework guidance for storefront frontends
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup) - browser platform best practices for storefront UX
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Add the marketplace and install plugins one at a time, verifying with `/plugin` between installs.
- New to Medusa? Start with learning-medusa - it teaches core concepts by building a brands feature, so the team ramps while the tutorial runs.
- On non-Claude agents, remember `skills add` copies skills only; add MCP server configuration by hand (README).
- Keep db-generate and db-migrate in the loop for every model change instead of editing the database by hand.
- For Cloud work, follow the lifecycle order: mcloud-auth, then projects and environments, then deployments, variables, and logs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
