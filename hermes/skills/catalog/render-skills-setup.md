---
title: "Render Agent Skills - Official Render Collection Setup"
description: "render-oss/skills - 10.7K combined installs: 22 agent skills that teach AI tools to deploy, operate, and debug apps on Render."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/render-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "cloud deployment", "devops", "render"]
---

# Render Agent Skills - Setup Guide

**Source:** [render-oss/skills](https://www.skills.sh/render-oss/skills) via skills.sh - 10.7K combined installs across 22 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [render-oss/skills](https://github.com/render-oss/skills) - 107 stars, MIT license, last pushed Nov 20, 2026, main branch; 22 skill directories under skills/<name>/SKILL.md, most with a references/ folder, plus Claude Code auto-approval hooks and a Claude Code plugin manifest.
**Category:** Cloud Platform (Render)
**Quality Tier:** 🟠 Orange - render-workflows fails the Gen Agent Trust Hub check and render-debug fails Snyk; six of the fifteen sampled skills carry a Warn cell and the rest pass.

render-oss/skills is Render's open-source collection of agent skills that teach AI coding tools how to deploy, operate, and debug applications on Render. Each of the 22 skills is a self-contained SKILL.md plus references/ files that any compatible agent (Claude Code, Codex, OpenCode, Cursor) can read. Skills cover the full Render surface: web services, background workers, cron jobs, static sites, Blueprints (render.yaml), Docker, Postgres, Key Value, persistent disks, private networking, autoscaling, sandboxes, and Heroku migration.

The recommended install path is the Render CLI (render skills install), with a Skills CLI fallback (npx skills add render-oss/skills) and a Claude Code plugin route. A RENDER_API_KEY and either the Render MCP server or CLI are prerequisites. The repo also ships Claude Code auto-approval hooks that pre-approve a small set of read-only render commands while leaving anything that changes infrastructure behind an explicit approval.

## Installation

The recommended path is the Render CLI:

```bash
render skills install
```

Manage installed skills with:

```bash
render skills          # interactive management
render skills list     # show installed skills
render skills update   # update installed skills
```

Alternative installs: npx skills add render-oss/skills for the Skills CLI, or the Claude Code plugin route /plugin marketplace add render-oss/skills followed by /plugin install render@skills. You can also copy any directory from skills/ into your tool's skills path (~/.claude/skills/, ~/.codex/skills/, ~/.config/opencode/skills/, or ~/.cursor/skills/).

Prerequisites: a Render account with the Render MCP server or Render CLI configured, a RENDER_API_KEY environment variable, and a Git repository on GitHub, GitLab, or Bitbucket for any deploy-related skill.

## What It Provides

skills.sh publishes per-skill descriptions for 15 of the 22 indexed listings; the seven without an indexed description all sit below the smallest rows in the table. All 22 indexed listings have a matching skills/<name>/ directory in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| render-deploy | 671 | deploying apps to Render by analyzing the codebase and authoring Blueprints |
| render-debug | 644 | diagnosing failed deploys, startup issues, and runtime errors |
| render-cli | 608 | installing and using the Render CLI for deploys, logs, SSH, and automation |
| render-monitor | 606 | checking service health, metrics, logs, and resource usage |
| render-env-vars | 577 | managing environment variables, secrets, and env groups |
| render-mcp | 554 | connecting and configuring the Render MCP server for AI tools |
| render-cron-jobs | 528 | configuring scheduled jobs and cron expressions |
| render-web-services | 513 | configuring web services, health checks, TLS, and custom domains |
| render-blueprints | 508 | authoring and validating render.yaml Blueprints |
| render-docker | 489 | building and deploying Docker containers and multi-stage builds |
| render-postgres | 480 | operating Managed PostgreSQL, backups, replicas, and connections |
| render-workflows | 471 | building, validating, and deploying Render Workflows |

The remaining 10 indexed listings range from 83 to 457 installs.

## Why This Matters for Hermes Agents

render-oss/skills packages Render's operating knowledge as agent-readable skills, so an agent can plan and apply infrastructure changes instead of only reciting documentation. Each skill pairs a short SKILL.md with references/ files that carry the deep detail, covering deployment, Blueprints, service types, data services, networking, scaling, and migration. For a builder running Hermes agents against a Render account, the suite turns "deploy my app" into a sequence that analyzes the codebase, authors a render.yaml, reviews the plan, and applies it through the CLI or MCP server. The auto-approval hooks are the part worth studying: they whitelist a narrow set of read-only render commands for Claude Code while forcing anything that changes infrastructure through explicit approval, a governance pattern that transfers to other tools. Adoption costs are real but modest: skills need a Render account, a RENDER_API_KEY, and either the CLI or MCP server, and two sampled skills carry Fail cells in the skills.sh verdicts. Read it as both a deploy toolkit and a reference for hook-based approval.

## Usage

| You say | What happens |
|---|---|
| Deploy my application to Render | Uses render-deploy to analyze the codebase, author a Blueprint, and apply it |
| Debug why my Render service won't start | Uses render-debug to analyze logs, metrics, and error patterns |
| Is my Render service healthy? | Uses render-monitor to check health, metrics, and resource usage |
| Set up a private service for this internal API | Uses render-private-services over the private network |
| Add a cron job that runs every night | Uses render-cron-jobs to configure the schedule and cron expression |
| Configure custom domains for this web service | Uses render-web-services for TLS and custom domains |
| Migrate my Heroku app to Render | Uses render-migrate-from-heroku to map services and move data |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/render-oss/skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/render-oss/skills/main/skills/render-deploy/SKILL.md | head -40
```

Both URLs return 200. After installing, run render skills list to confirm the skills registered with your agent.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| render-deploy | Pass | Pass | Warn |
| render-debug | Pass | Pass | Fail |
| render-cli | Pass | Pass | Warn |
| render-monitor | Pass | Pass | Warn |
| render-env-vars | Pass | Pass | Pass |
| render-mcp | Pass | Pass | Warn |
| render-cron-jobs | Pass | Pass | Pass |
| render-web-services | Pass | Pass | Pass |
| render-blueprints | Pass | Pass | Warn |
| render-docker | Pass | Pass | Pass |
| render-postgres | Pass | Pass | Pass |
| render-workflows | Fail | Pass | Warn |
| render-static-sites | Pass | Pass | Pass |
| render-background-workers | Pass | Pass | Pass |
| render-networking | Pass | Pass | Pass |

Two sampled skills carry Fail cells: render-workflows on Gen Agent Trust Hub and render-debug on Snyk. 15 of the 22 indexed listings were sampled; the rest were not.

## Limitations

- Snapshot data, verified Nov 24, 2026: 10,700 combined installs across 22 indexed listings; 107 GitHub stars; MIT license; last pushed Nov 20, 2026. Counts drift over time.
- skills.sh publishes per-skill descriptions for 15 of the 22 listings; render-disks, render-domains, render-keyvalue, render-migrate-from-heroku, render-private-services, render-sandboxes, and render-scaling have no indexed description and appear below the cut-off of the table.
- The README's opening line says 21 skills, but its own catalog and the repo tree list 22, matching the 22 indexed listings.
- Two sampled skills carry Fail cells: render-workflows on Gen Agent Trust Hub and render-debug on Snyk.
- The auto-approval hooks pre-approve only read-only render commands made of plain words; commands with quotes, pipes, redirects, or shell syntax fall through to normal permission checks, and infrastructure changes still require approval.
- Skills assume a Render account, a RENDER_API_KEY, and the MCP server or CLI; deploy-related skills also need a Git repository.

## Related

[AWS Agent Plugins - Official AWS Plugin Suite Setup](/hermes/skills/catalog/aws-agent-plugins-setup) | [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup) | [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with render skills install, then run render skills update after any repo release to pull newer SKILL.md files.
- Set up RENDER_API_KEY and the MCP server (or CLI) first; every skill assumes at least one access path.
- Use render-cli for scripted CI/CD deploys and render-mcp for interactive agent tool use; they overlap but serve different loops.
- Review hooks/hooks.json before enabling auto-approve in Claude Code; it whitelists only read-only commands.
- Migrate Heroku apps with render-migrate-from-heroku and render-blueprints together rather than hand-editing render.yaml.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
