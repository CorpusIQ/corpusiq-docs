---
title: "Zeabur Agent Skills - CLI Operations and Deployment Setup"
description: "zeabur/agent-skills - 5.4K combined installs: a Claude Code and Codex plugin for Zeabur CLI operations, deployment, and troubleshooting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zeabur-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "zeabur", "deployment", "cli"]
---

# Zeabur Agent Skills - Setup Guide

**Source:** [zeabur/agent-skills](https://www.skills.sh/zeabur/agent-skills) via skills.sh - 5.4K combined installs across 36 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [zeabur/agent-skills](https://github.com/zeabur/agent-skills) - 38 stars, no LICENSE file (the README states MIT), main branch, last pushed Sep 6, 2026; 32 skill directories mirrored under both plugins/zeabur/skills/ and skills/, with Claude Code, Codex, and .agents plugin marketplace manifests.
**Category:** Cloud Platform (Zeabur)
**Quality Tier:** 🟡 Yellow - zeabur-template carries Warn cells on Socket and Snyk; zeabur-deployment-logs, zeabur-deploy, zeabur-domain-register, and zeabur-server-rent carry a Snyk Warn; the other 10 sampled skills pass.

zeabur/agent-skills is a plugin for Claude Code and OpenAI Codex that packages 36 skills for operating the Zeabur cloud platform from the command line: deploying projects, managing services and environment variables, renting dedicated servers, registering domains, and troubleshooting common failure modes. It ships marketplace manifests for Claude Code, Codex, and the .agents plugin directory, and each skill exists in both plugins/zeabur/skills/ and a top-level skills/ tree.

Four of the 36 indexed listings have no counterpart in the current tree: zeabur-ai-hub was removed when the Zeabur AI Hub shut down in Sep 2026, zeabur-context was folded into direct --project-id use, and zeabur-service-expose and zeabur-domain-registrant are absent despite the latter still appearing in the README skills table.

## Installation

Claude Code:

```
claude plugin marketplace add zeabur/agent-skills && claude plugin install zeabur@zeabur
```

Update to the latest version:

```
claude plugin marketplace update zeabur && claude plugin update zeabur@zeabur
```

OpenAI Codex: in the Codex app, search for "Zeabur" in the plugin directory and click Add to Codex. In the Codex CLI, run /plugins and select "Install plugin" to browse and install.

Local testing:

```bash
# Claude Code
claude --plugin-dir /path/to/agent-skills

# Codex
codex --plugin-dir /path/to/agent-skills
```

## What It Provides

All 13 listings in the table have an indexed description and a matching skill directory in the current tree. Four of the 36 indexed listings have no tree counterpart (zeabur-ai-hub, zeabur-context, zeabur-service-expose, and zeabur-domain-registrant) and are covered in Limitations.

| Skill | Installs | Use For |
|---|---|---|
| zeabur-restart | 206 | restarting a Zeabur service that is stuck or frozen |
| zeabur-deployment-logs | 202 | viewing service runtime and build logs when a deploy fails or an error needs debugging |
| zeabur-domain-url | 193 | setting up public URLs and fixing CORS and trailing-slash redirect problems for a service |
| zeabur-template | 192 | creating, editing, validating, and troubleshooting Zeabur template YAML, including docker-compose conversion |
| zeabur-service-list | 192 | listing services and getting the service IDs other commands need |
| zeabur-variables | 189 | managing all Zeabur environment variables: create, list, update, delete, and troubleshoot |
| zeabur-update-service | 185 | modifying service config and env vars without a full redeploy |
| zeabur-deploy | 183 | deploying a local project or codebase to Zeabur, directly or from GitHub |
| zeabur-project-create | 182 | creating a new Zeabur project or deploying a template into a new environment |
| zeabur-server-list | 179 | listing dedicated servers and checking status, IP, or provider info |
| zeabur-startup-order | 178 | fixing connection-refused failures when a service starts before its database or Redis is ready |
| zeabur-migration | 177 | resolving services stuck waiting for database migrations to complete |
| zeabur-domain-register | 177 | searching, purchasing, renewing, and managing registered domains |

The remaining 23 indexed listings range from 1 to 176 installs.

## Why This Matters for Hermes Agents

zeabur/agent-skills is a vendor-maintained reference for turning a cloud PaaS's CLI into narrow, single-purpose skills, each with explicit triggers, so an agent can resolve which skill to invoke from the user's phrasing instead of reverse-engineering the CLI. The troubleshooting skills encode hard-won failure modes, port mismatches, startup ordering, stuck migrations, as lookup tables, the kind of operational knowledge that usually lives in support tickets. For a builder, the repository shows how to ship one skill set with marketplace manifests for multiple agents while keeping a top-level skills/ tree synced with a plugin copy. The changelog is a maintenance discipline worth copying: skills are removed when their endpoints retire and rewritten when the CLI changes. Adoption costs are low but real: the README's version line lags the changelog, the license is stated but not filed, and four indexed listings no longer ship.

## Usage

| You say | What happens |
|---|---|
| Deploy this project | Uses zeabur-deploy to upload a local project or deploy from GitHub |
| Restart my service | Uses zeabur-restart to restart the stuck service |
| Show the logs for this deploy | Uses zeabur-deployment-logs to pull runtime and build logs |
| Set an environment variable | Uses zeabur-variables to create or update the variable |
| Fix the CORS error | Uses zeabur-domain-url to correct the public URL and trailing-slash config |
| Create a new project | Uses zeabur-project-create to set up the project and its deploy target |
| The service keeps failing on connection refused | Uses zeabur-startup-order to reorder startup so the database is ready first |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/zeabur/agent-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/zeabur/agent-skills/main/plugins/zeabur/skills/zeabur-deploy/SKILL.md | head -30
```

Both URLs return 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| zeabur-restart | Pass | Pass | Pass |
| zeabur-deployment-logs | Pass | Pass | Warn |
| zeabur-domain-url | Pass | Pass | Pass |
| zeabur-template | Pass | Warn | Warn |
| zeabur-service-list | Pass | Pass | Pass |
| zeabur-variables | Pass | Pass | Pass |
| zeabur-update-service | Pass | Pass | Pass |
| zeabur-deploy | Pass | Pass | Warn |
| zeabur-project-create | Pass | Pass | Pass |
| zeabur-server-list | Pass | Pass | Pass |
| zeabur-startup-order | Pass | Pass | Pass |
| zeabur-migration | Pass | Pass | Pass |
| zeabur-domain-register | Pass | Pass | Warn |
| zeabur-server-rent | Pass | Pass | Warn |
| zeabur-port-mismatch | Pass | Pass | Pass |

All 15 sampled skills pass the Gen Agent Trust Hub check; five carry a Snyk Warn and zeabur-template also carries a Socket Warn. 15 of the 36 indexed listings were sampled; the rest were not.

## Limitations

- Snapshot data, verified Nov 24, 2026: 5,373 combined installs across 36 indexed listings; 38 GitHub stars; no LICENSE file (README states MIT); last pushed Sep 6, 2026. Counts drift over time.
- The install index outruns the tree: zeabur-ai-hub (removed in 1.22.0 when the AI Hub shut down) and zeabur-context (removed in 1.3.0) carry install counts but have no skill directory; zeabur-service-expose and zeabur-domain-registrant likewise have no tree counterpart, and zeabur-domain-registrant is still listed in the README skills table.
- The README's version line (1.21.3) lags its own changelog (1.22.0), and zeabur-template-deploy uses lowercase skill.md in the tree.
- No LICENSE file in the repository although the README states MIT; treat the license as claimed but not filed and confirm before redistribution.
- The repository is not archived, but the last push was Sep 6, 2026.

## Related

[Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup) | [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup) | [AWS Agent Plugins - Official AWS Plugin Suite Setup](/hermes/skills/catalog/aws-agent-plugins-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install through the plugin marketplace (claude plugin install zeabur@zeabur) so updates arrive via the marketplace rather than a manual copy.
- Use the top-level skills/ tree with --plugin-dir for local testing before committing to a marketplace install.
- Run zeabur-project-create before zeabur-deploy on a new project; the deploy skill defers project creation to it.
- Fetch service IDs with zeabur-service-list instead of guessing them from logs.
- Treat zeabur-ai-hub, zeabur-context, zeabur-service-expose, and zeabur-domain-registrant as retired listings; do not assume they still ship.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
