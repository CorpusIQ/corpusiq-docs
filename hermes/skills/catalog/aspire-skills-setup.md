---
title: "Microsoft Aspire Skills - .NET AppHost Agent Setup"
description: "Microsoft Aspire agent skills: 8.5K combined installs across 8 listings for AppHost orchestration, monitoring, deployment and Project v2 migration"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aspire-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "dotnet", "aspire", "orchestration", "deployment"]
---

# Microsoft Aspire Skills - Setup Guide

**Source:** [microsoft/aspire-skills](https://www.skills.sh/microsoft/aspire-skills) via skills.sh - 8.5K combined installs across 8 indexed listings; first seen May 27, 2026 (Nov 11, 2026 sweep)
**GitHub:** 94 stars, MIT license, `main` branch, last pushed 2026-11-11, 443 tracked files with eight `SKILL.md` files under `skills/`, a second copy under `.github/plugins/aspire-skills/skills/` and an `opencode/v1/` mirror of the same eight
**Category:** .NET distributed applications: AppHost wiring, local orchestration, telemetry, publishing and version migration
**Quality Tier:** 🟡 Established - Microsoft first-party and MIT licensed, with three Pass verdicts on the router skill, but 94 stars and Warn verdicts on the deployment skill keep it out of the top band.

Aspire is Microsoft's opinionated stack for building distributed .NET applications: an AppHost declares the services, databases, containers and front ends a system is made of, and one command starts the whole graph locally with a dashboard for logs, traces and endpoints. The vocabulary is specific enough that a general-purpose agent will reach for `dotnet run`, `docker compose` and `curl` instead, which is the problem this repository solves.

The pack is eight skills under a router. `aspire` is the entry point: it detects an AppHost in the workspace, applies guardrails and dispatches to a focused skill. The others cover creating or adopting a project (`aspire-init`, `aspireify`), lifecycle (`aspire-orchestration`), observation (`aspire-monitoring`), publishing (`aspire-deployment`), terminal automation (`aspire-terminals`) and one deliberately narrow migration path (`aspire-project-v2-migration`). The repository also ships three canvas extensions, `aspire-doctor`, `aspireify` and `aspire-apphosts`, which are visual surfaces for environments that support them.

The release cadence is what stands out. The repository was pushed the same day as this snapshot, and the README documents the mechanism: changes here have to be re-embedded in the Aspire CLI's own `aspire-skills` archive before an installed CLI picks them up. The `opencode/v1/` tree exists because one host loads skills from an HTTP catalog rather than a checkout.

## Installation

Every route in the README targets a different host. For a Hermes agent, install through the skills CLI from your profile or a project root, then restart the session:

```bash
npx skills add microsoft/aspire-skills
```

Claude Code and GitHub Copilot CLI take the plugin marketplace instead of a checkout:

```text
/plugin marketplace add microsoft/aspire-skills
/plugin install aspire@aspire-skills
/plugin update aspire@aspire-skills
```

If you already build with Aspire, the CLI can install agent guidance itself, which is the route Microsoft prefers because the files come embedded in the tool you already have:

```bash
aspire new
aspire init
aspire agent init
```

`aspire new` and `aspire init` preselect the recommended repository-local skills when they see an agent environment. `aspire agent init` adds, updates or reconfigures guidance in an existing workspace, and it keeps the MCP server option off unless you pass `--mcp` (Aspire 13.6 and later; on 13.5 the flag does not exist and the choice is interactive). One caveat is stated in the README itself: editing this repository does not change the copy embedded in an installed CLI.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| aspire | 1,707 | Router. Detects AppHosts, enforces guardrails and selects the right sub-skill for a request. |
| aspire-orchestration | 1,622 | Starts, stops, waits for and manages resources, through the CLI or the VS Code integration. |
| aspire-monitoring | 1,607 | Reads logs, traces, metrics and resource state, and covers telemetry export and the standalone dashboard. |
| aspireify | 1,156 | Wires a new AppHost or repairs an existing TypeScript AppHost toolchain, proposing a resource graph before editing. |
| aspire-init | 1,153 | First-run flow that picks `aspire new` for a greenfield repo or `aspire init` for an existing one. |
| aspire-deployment | 1,141 | Publishes and deploys to Docker Compose, Kubernetes, Azure, AWS or preview Radius, and tears deployments down. |

The remaining 2 indexed listings range from 16 to 72 installs: aspire-project-v2-migration (72) and aspire-terminals (16). No indexed listing falls below that floor.

One listing has no same-named directory in the current `skills/` tree only because the repository names the folder after the task rather than the listing, and the `.github/plugins` copy mirrors the same eight folders. The extensions (`aspire-doctor`, `aspireify`, `aspire-apphosts`) are canvas surfaces, not skills, so they carry no install counts.

## Why This Matters for Hermes Agents

A distributed application is a graph, and most agent failures on one are graph failures: the agent edits a service without knowing what depends on it, starts a container the AppHost was supposed to manage, or reports a deployment healthy because one container is up.

The router design addresses that directly. `aspire` runs before anything else and decides which focused skill applies, so the agent does not have to hold the whole vocabulary at once. `aspireify` goes further and requires an approved resource plan before it edits an AppHost, which is the difference between an agent that proposes a change and one that makes it silently.

The deployment skill is the one to read before running. It covers Docker Compose, Kubernetes, Azure, AWS and preview Radius, which means a single ambiguous instruction such as "deploy this" has five valid outcomes. Naming the target in the prompt is what keeps the result predictable.

For Hermes users running .NET services alongside other systems, this is also a clean separation of concerns: Aspire owns the application graph and its local runtime, and the agent calls into it rather than reconstructing orchestration from shell commands.

## Usage

| You say | What happens |
|---|---|
| "What does this AppHost start?" | Detects the AppHost, enumerates declared resources and reports the dependency graph before anything runs. |
| "Add a Redis cache to the app" | Routes through aspireify, proposes the resource addition and the code changes, and waits for approval before editing. |
| "Start the app and tell me when it is ready" | Uses aspire-orchestration to launch the graph, waits for resource readiness and reports which resources came up. |
| "Why is the API failing locally?" | Reads logs and traces through aspire-monitoring and points at the failing resource rather than the whole graph. |
| "Publish this to Kubernetes" | Takes the explicit target through aspire-deployment and reports the artifacts it produced. |
| "Migrate our project resources to Project v2" | Uses aspire-project-v2-migration to assess eligibility on 13.6 and later, then requests explicit approval before editing. |
| "Automate the terminal that the worker opens" | Uses aspire-terminals to author terminals and replay VHS-subset tapes. |

## Verification

The skills live under `skills/` and the README documents that path. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/aspire-skills/main/skills/aspire/SKILL.md | head -6
```

It should open with YAML frontmatter naming the skill and describing it as the Aspire workflow router. The plugin copy is a second valid path if you install through Claude Code or Copilot CLI:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/microsoft/aspire-skills/main/.github/plugins/aspire-skills/skills/aspire/SKILL.md
```

After installation, list your agent's skills directory and confirm eight folders exist before assuming the pack took. If `aspire agent init` was the route, the skills may sit in a repository-local directory rather than your profile, because that command writes into the workspace it is run from.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| aspire | Pass | Pass | Pass |
| aspire-deployment | Pass | Warn | Warn |

The router passes all three scanners. The deployment skill draws Warns from Socket and Snyk, which is worth reading rather than dismissing: a skill that publishes applications to cloud targets asks the agent to run infrastructure commands, and a scanner treating that as elevated action is reasonable. The verdicts say nothing about whether a deploy is correct, only that the instructions were inspected.

Two other things belong here. The skills are markdown, but the workflow they describe executes `docker`, `kubectl`, `az` and `aspire` against real environments, so the safety of the result is the safety of your credentials and your target. And the Aspire CLI route installs files into your repository, which means an agent that follows the guidance can also change tracked code as part of a normal request.

## Limitations

- Snapshot data, verified 2026-11-11: 8,474 combined installs across 8 indexed listings; 94 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- The install index carries eight listings, and all eight have a directory in the current tree, but the skills also exist in three copies (`.github/plugins`, `skills/`, `opencode/v1`), so a version skew between an installed CLI and this repository is possible by design.
- The README states that repository changes do not update an installed CLI's embedded skills. If you use `aspire agent init`, the bundle version and the CLI version have to be refreshed together.
- The extensions are canvas surfaces. In a text-only client they do nothing, and the guide stays useful only through the skills.
- `.NET` and Aspire 13.x are assumed. The migration skill explicitly targets Aspire 13.6 and later, and older installations will not have the flag or the APIs it discusses.
- 94 stars is a thin community signal for a first-party pack. Support comes from the Aspire team, not from a large user base reading each other's issues.

## Related

- [Aaronontheweb Dotnet Skills - Akka.NET Suite](/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup)
- [Microsoft Learn Agent Skills - Azure and .NET Docs](/hermes/skills/catalog/microsoftdocs-agent-skills-setup)
- [Nx AI Agents Config - Monorepo Agent Skills Setup](/hermes/skills/catalog/nx-ai-agents-config-skills-setup)

## Pro Tips

- Ask for the graph before the change. "List the resources in this AppHost" costs one turn and makes every later request safer.
- Name the deployment target every time. Five supported targets plus a preview one is exactly the ambiguity an agent resolves wrongly by guessing.
- Keep `aspire agent init` for repos you own. It writes agent guidance into the workspace, which then travels with the code to everyone who clones it.
- Read `aspire-deployment` before the first deploy rather than after a failed one. The Warn verdicts are about scope, and the skill's own guardrails are the thing that constrains it.
- Pin the CLI version in CI. The embedded bundle moves with the CLI, so an unpinned runner can change which skills the agent sees between builds.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
