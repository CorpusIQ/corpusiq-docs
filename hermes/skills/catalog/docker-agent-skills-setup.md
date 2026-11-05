---
title: "Docker Agent Skills - Container Workflow Suite"
description: "docker/skills on skills.sh: 12.7K combined installs across 12 listings; Compose patterns, Dockerfile builds, sandboxes and Docker Agent workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/docker-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "docker", "containers", "devops"]
---

# Docker Agent Skills - Setup Guide

**Source:** [docker/skills](https://www.skills.sh/docker/skills) via skills.sh - 12.7K combined installs across 12 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 615 stars, Apache-2.0 licence, last pushed 2026-11-04, 12 SKILL.md directories under skills/
**Category:** Container workflows for agents: project foundations, Dockerfile builds, Compose stacks, Docker Sandboxes microVMs and Docker Agent authoring
**Quality Tier:** 🟢 Production - every sampled audit Pass; Apache-2.0; 615 stars.

Docker authored twelve portable `SKILL.md` directories that cover the container work an agent actually gets asked to do: containerize a repository, shrink an image, wire a Compose stack, run an agent in an isolated sandbox, or ship a Docker Agent. Each skill triggers from its own description and there is no entry router, so a request lands on the skill that names it.

The README also publishes a load order for tasks that span several skills, which is rarer than it should be. Project foundations come before build strategies or Compose when there is no Docker setup yet; build strategies come before Compose when a Dockerfile and a compose.yaml both change; sandbox lifecycle comes before network credentials, and both before environments or kits; agent config comes before run, and run before deploy. Two skills, `docker-sandboxes-env` and `docker-sandboxes-kits`, are marked experimental because their schemas may still change.

## Installation

The README's quick start installs the collection through the skills CLI, which reads the repository's `skills.sh.json` index and groups the prompts by product:

```bash
npx skills add docker/skills
```

Non-interactive forms cover the common cases, starting with a read-only browse:

```bash
npx skills add docker/skills --list
```

```bash
npx skills add docker/skills --skill docker-compose-patterns --yes
```

```bash
npx skills add docker/skills --all
```

```bash
npx skills update
```

The README also documents plugin installs for Claude Code, Codex and GitHub Copilot CLI. Plugin installs register the remote Docker docs MCP server used by `docker-docs`, while the skills CLI installs skills only:

```text
/plugin marketplace add docker/skills
/plugin install docker-skills@docker
```

A pinned install is available by pointing the CLI at a release tag:

```bash
npx skills add https://github.com/docker/skills/tree/vX.Y.Z --skill docker-compose-patterns --yes
```

Each skill declares its own prerequisites in frontmatter. `docker-compose-patterns`, for example, states that it requires Docker Compose v2 and the compose.yaml format.

## What It Provides

Eleven of the 12 indexed listings meet the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| docker-compose-patterns | 1,814 | Wiring multi-container stacks, adding a database or cache, and building maintainable local development environments |
| docker-build-strategies | 1,599 | Multi-stage builds, layer caching, .dockerignore, non-root users and hardening images for production |
| docker-project-foundations | 1,319 | Containerizing a project from scratch, including the initial layout and local development foundations |
| docker-destructive-guardrails | 1,285 | Confirmation policy before any command that deletes, wipes, resets or force-removes state |
| docker-agent-deploy | 918 | Exposing an agent over MCP, HTTP, A2A or an OpenAI-compatible API, OCI distribution and eval runs |
| docker-agent-config | 911 | Authoring agent.yaml: agents, models and providers, built-in and MCP toolsets, sub_agents teams |
| docker-agent-run | 909 | Running an agent locally with approval modes, the sandbox flag, aliases and run troubleshooting |
| docker-sandboxes-lifecycle | 897 | Creating, reattaching to, listing, stopping and removing sbx microVM sandboxes |
| docker-sandboxes-network-credentials | 895 | Sandbox egress policy and credential injection through the proxy model |
| docker-sandboxes-kits | 891 | Authoring, verifying, publishing and composing sandbox kits, marked experimental |
| docker-sandboxes-env | 891 | Declarative sbxenv.yaml environments: plan, run, execute and remove, marked experimental |

The remaining 1 indexed listing is docker-docs at 337 installs, below the threshold.

## Why This Matters for Hermes Agents

Container work is where an agent can do expensive damage in one command. `docker-destructive-guardrails` is the answer worth copying: a confirmation policy for irreversible operations, written once as a skill that every other skill in the pack can rely on, rather than a warning repeated in each procedure.

The published load order is the second transferable idea. Most skill collections are a menu; this one states which skill's output feeds which, so an agent that loads three of them has a dependency graph instead of a pile of overlapping advice.

The suite also tracks products that moved recently. Docker Sandboxes and Docker Agent are new surfaces, and the skills cover the `sbx` lifecycle, kit authoring, agent.yaml, approval modes and serving, which is exactly the knowledge a model trained earlier does not have.

Portability is deliberate. Skills are authored as plain directories that any compliant agent discovers through standard paths, with no entry-point skill to load first, so the same files work in Claude Code, Codex, Cursor, Copilot, Gemini CLI and the rest.

The practical caution is that the sandbox skills target a specific runtime, the standalone `sbx` CLI with microVMs. Without it those four skills describe a workflow the host cannot run, while the Dockerfile, Compose and agent skills remain useful anywhere Docker is installed.

## Usage

| You say | What happens |
|---|---|
| "containerize this repo" | docker-project-foundations scaffolds the Dockerfile, .dockerignore and local development setup |
| "my image is two gigabytes" | docker-build-strategies rewrites the build as multi-stage with layer caching and a slim runtime |
| "add Postgres and Redis to my stack" | docker-compose-patterns wires the services, volumes and healthchecks into compose.yaml |
| "wipe the volumes and start fresh" | docker-destructive-guardrails stops for confirmation before the irreversible command |
| "run this agent in a sandbox" | docker-sandboxes-lifecycle creates an sbx microVM and reattaches to it later |
| "let the sandbox call our internal API" | docker-sandboxes-network-credentials sets the egress policy and injects the credential |
| "serve this agent over MCP" | docker-agent-deploy exposes the agent and runs an eval for regressions |

## Verification

Fetch a raw skill file to confirm the tree still matches what skills.sh indexed. This path is `skills/docker-compose-patterns/SKILL.md` on branch `main` and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/docker/skills/main/skills/docker-compose-patterns/SKILL.md | head -20
```

A response opening with `name: docker-compose-patterns` and its description confirms the content is live. Before installing, list the catalog without writing anything:

```bash
npx skills add docker/skills --list
```

That output is grouped by product and is the quickest way to see the 12 skills against the 11 rows above. After an install, confirm the skill directories in the agent skills directory the CLI reported, and check that Docker itself is present:

```bash
docker --version
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| docker-compose-patterns | Pass | Pass | Pass |
| docker-build-strategies | Pass | Pass | Pass |
| docker-project-foundations | Pass | Pass | Pass |
| docker-agent-run | Pass | Pass | Pass |

Every sampled skill passes all three auditors with no Warn and no Fail, which is what the green tier reflects. The repository also runs its own CI workflow and carries an OpenSSF Scorecard badge, and the destructive-operations policy is shipped as a skill rather than left to prose.

## Limitations

- Snapshot data, verified 2026-11-04: 12,666 combined installs across 12 indexed listings; 615 GitHub stars; Apache-2.0 licence; last pushed 2026-11-04. Counts drift over time.
- `docker-sandboxes-env` and `docker-sandboxes-kits` are marked experimental in the README, so their schemas may change between releases.
- The four sandbox skills target the standalone `sbx` CLI and microVMs. Treat them as dependent on that runtime rather than on a plain container engine.
- Plugin installs register the remote Docker docs MCP server and update through the agent marketplace; the skills CLI installs skills only and does not add the MCP server.
- One of the 12 indexed listings sits below the 500-install threshold, so the table above covers 11 of the 12.
- Each skill triggers from its own description with no router, so a request that spans build and Compose depends on the model choosing correctly. The README's load order is guidance, not enforcement.

## Related

- [CC DevOps Skills - Kubernetes and IaC Suite](/hermes/skills/catalog/cc-devops-skills-setup)
- [Pulumi Agent Skills - Infrastructure as Code Setup](/hermes/skills/catalog/pulumi-agent-skills-setup)
- [Next.js Agent Skills - Official Vercel Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `docker-destructive-guardrails` in any session that can run Docker. It is the cheapest insurance in the pack and it applies across products.
- Run `--list` first on an unfamiliar machine. It prints the catalog grouped by product without writing files, which is enough to plan an install.
- Follow the README's load order when a task spans skills. Foundations before build, build before Compose, lifecycle before credentials.
- Pin a release tag when a sandbox schema matters. Experimental skills are the ones most likely to move under you.
- Keep plugin and CLI installs separate. The plugin route brings the docs MCP server, the CLI route does not, and mixing them makes updates confusing.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
