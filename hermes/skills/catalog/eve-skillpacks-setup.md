---
title: "Eve Skillpacks - Eve Horizon Platform Skills Setup"
description: "incept5/eve-skillpacks - 7.9K combined installs: public skill packs for the Eve Horizon agent platform (work, SE and design packs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/eve-skillpacks-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "eve horizon", "agent platform", "orchestration"]
---

# Eve Skillpacks - Setup Guide

**Source:** [incept5/eve-skillpacks](https://www.skills.sh/incept5/eve-skillpacks) via skills.sh - 7.9K combined installs across 27 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [incept5/eve-skillpacks](https://github.com/incept5/eve-skillpacks) - 0 stars, MIT license, main branch, last pushed Jul 3, 2026; three packs (eve-work/, eve-se/, eve-design/) plus a private-skills/ directory, each skill in <pack>/<name>/SKILL.md with references/.
**Category:** Eve Horizon Platform Skills
**Quality Tier:** 🟡 Yellow - eve-web-ui-testing-agent-browser carries Warn on all three checks and eve-auth-and-secrets carries a Warn on Gen Agent Trust Hub; the other 13 sampled skills pass all three checks.

incept5/eve-skillpacks publishes the public skill packs for Eve Horizon, an agent platform with jobs, pipelines, manifests and a CLI. The repository is organized into three packs: eve-work (productive work patterns and orchestration), eve-se (platform-specific skills for deploys, manifests, pipelines and the agent runtime) and eve-design (architecture and design thinking).

The index lists 27 skills at 7.9K combined installs, led by eve-web-ui-testing-agent-browser (437) and eve-auth-and-secrets (332). Activity is low: the repository has 0 GitHub stars and was last pushed Jul 3, 2026. The README's install URLs point at github.com/eve-horizon/eve-skillpacks, while the skills.sh listing is incept5/eve-skillpacks.

## Installation

Add the repo to skills.txt for on-clone installs:

```
https://github.com/eve-horizon/eve-skillpacks
```

For a local install, run:

```bash
skills add https://github.com/eve-horizon/eve-skillpacks -a claude-code -y --all
```

Alternatively add the repo to skills.txt and run ./bin/eh skills install inside an Eve repo.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| eve-web-ui-testing-agent-browser | 437 | web UI testing and browser automation via Vercel agent-browser or the repo-pinned Playwright wrapper |
| eve-auth-and-secrets | 332 | authenticating with Eve, managing project secrets and adding SSO login |
| eve-skill-distillation | 327 | distilling repeated work into Eve skillpacks |
| eve-orchestration | 319 | orchestrating jobs via depth propagation, parallel decomposition, relations and control signals |
| eve-new-project-setup | 316 | configuring a new Eve Horizon project after eve init |
| eve-repo-upkeep | 315 | keeping Eve-compatible repos aligned with platform best practices |
| eve-local-dev-loop | 313 | local Docker Compose development loop with handoff to staging deploys |
| eve-job-debugging | 312 | monitoring and debugging Eve jobs with CLI follow, logs, wait and diagnose |
| eve-troubleshooting | 310 | troubleshooting Eve deploy and job failures with CLI-first diagnostics |
| eve-job-lifecycle | 310 | creating, managing and reviewing Eve jobs, phases and dependencies |
| eve-pipelines-workflows | 309 | defining and running Eve pipelines and workflows via manifest and CLI |
| eve-deploy-debugging | 307 | deploying and debugging Eve-compatible apps via the CLI, staging focus |
| eve-agent-memory | 307 | combining Eve storage primitives for persistent agent memory |
| eve-plan-implementation | 306 | executing engineering plan documents via Eve jobs and review gating |
| eve-read-eve-docs | 305 | load-first state-today index of Eve Horizon docs with task-based routing |
| eve-se-index | 304 | the eve-se pack index (name-level; no published description) |
| eve-cli-primitives | 302 | Eve CLI primitives (name-level; no published description) |
| eve-manifest-authoring | 300 | authoring Eve manifests (name-level; no published description) |
| eve-bootstrap | 300 | the Eve bootstrap step (name-level; no published description) |

The remaining 8 indexed listings range from 100 to 294 installs.

## Why This Matters for Hermes Agents

Eve Skillpacks is a clean example of packaging an agent platform's operational knowledge as skills: separate packs for work patterns, platform mechanics and design thinking, each with a load-first index skill (eve-read-eve-docs, eve-se-index) that routes the agent to the right reference. The memory and orchestration skills show how a platform exposes its storage primitives and job graph to an agent as reusable procedures rather than leaving it to guess. For a Hermes builder, the interesting parts are eve-skill-distillation (turning repeated work into skills) and eve-verification-plans (test-plan templates and conformance checks), which are the meta-skills for running an agent fleet. The tradeoffs are real: the repository is quiet, a handful of skills ship no description, and the top skill carries Warn on all three security checks.

## Usage

| You say | What happens |
|---|---|
| Test this web app's login flow | Uses eve-web-ui-testing-agent-browser to drive the browser and validate the flow |
| Set up a new Eve project | Uses eve-new-project-setup to configure profile, auth and manifest |
| This job is stuck, find out why | Uses eve-job-debugging to follow logs and diagnose |
| Deploy this app to staging | Uses eve-deploy-debugging via the CLI |
| Define a build and release pipeline | Uses eve-pipelines-workflows via manifest and CLI |
| Give this agent persistent memory | Uses eve-agent-memory to combine Eve storage primitives |
| Turn this repeated workflow into a skill | Uses eve-skill-distillation |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/incept5/eve-skillpacks/main/README.md | head -40
```

Confirm the highest-install skill body is present before installing:

```bash
curl -sL https://raw.githubusercontent.com/incept5/eve-skillpacks/main/eve-se/eve-web-ui-testing-agent-browser/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| eve-web-ui-testing-agent-browser | Warn | Warn | Warn |
| eve-auth-and-secrets | Warn | Pass | Pass |
| eve-skill-distillation | Pass | Pass | Pass |
| eve-orchestration | Pass | Pass | Pass |
| eve-new-project-setup | Pass | Pass | Pass |
| eve-repo-upkeep | Pass | Pass | Pass |
| eve-local-dev-loop | Pass | Pass | Pass |
| eve-job-debugging | Pass | Pass | Pass |
| eve-troubleshooting | Pass | Pass | Pass |
| eve-job-lifecycle | Pass | Pass | Pass |
| eve-pipelines-workflows | Pass | Pass | Pass |
| eve-deploy-debugging | Pass | Pass | Pass |
| eve-agent-memory | Pass | Pass | Pass |
| eve-plan-implementation | Pass | Pass | Pass |
| eve-read-eve-docs | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 7,878 combined installs across 27 indexed listings; 0 GitHub stars; MIT license; last pushed Jul 3, 2026. Counts drift over time.
- Low activity: the repository has 0 stars and has not been pushed since Jul 3, 2026.
- The README's install URLs point at github.com/eve-horizon/eve-skillpacks, while the skills.sh listing is incept5/eve-skillpacks.
- The top listing (eve-web-ui-testing-agent-browser) carries Warn on all three security checks, and eve-auth-and-secrets carries a Warn on Gen Agent Trust Hub.
- Four in-table listings ship no published per-skill description (eve-se-index, eve-cli-primitives, eve-manifest-authoring, eve-bootstrap), so those Use For cells are name-level.
- The repository carries sync map and state files (.sync-map.json, .sync-state.json) plus a private-skills/ directory, suggesting the public repo is mirrored from an internal Eve source.

## Related

- [Deep Agents - Batteries-Included Agent Harness Setup](/hermes/skills/catalog/deepagents-setup)
- [Wyatt Walsh Agents - Skill Governance and Orchestration](/hermes/skills/catalog/wyattowalsh-agents-setup)
- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [Skill Repo Manager - Hermes Repository Setup Guide](/hermes/skills/catalog/skill-repo-manager-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load eve-read-eve-docs first; it is the state-today index that routes to the right reference for any Eve task.
- Install the whole pack via skills.txt for on-clone installs, or the skills add command for a local agent.
- Treat eve-skill-distillation as the meta-skill if you maintain a skill library, since it encodes the turn-repeated-work-into-a-skillpack loop.
- Review the web UI testing skill's browser wrapper choice (Vercel agent-browser versus the repo-pinned Playwright wrapper) before relying on it in CI.
- Given the low activity, pin a known-good revision rather than tracking main.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
