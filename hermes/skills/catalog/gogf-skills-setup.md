---
title: "GoFrame Skills - Go Framework Development Setup"
description: "Setup guide for gogf/skills: 3.4K combined installs across 1 listing; the GoFrame v2 skill for AI-generated GoFrame code with runnable examples."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gogf-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "goframe", "golang", "web framework"]
---

# GoFrame Skills - Setup Guide

**Source:** [gogf/skills](https://www.skills.sh/gogf/skills) via skills.sh - 3.4K combined installs across 1 indexed listing; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** 83 stars, no LICENSE file, `main` branch, last pushed 2026-06-05. One skill at `skills/goframe-v2/SKILL.md` with a large `references/` documentation tree and an `examples/` tree of runnable Go projects across HTTP, gRPC, database, and observability topics.
**Category:** GoFrame v2 framework development (Go)
**Quality Tier:** 🟠 Orange - no LICENSE file; the single sampled verdict is Pass/Warn/Pass (Socket).

gogf/skills is the GoFrame team's skill for teaching AI agents to write accurate GoFrame code. GoFrame is a Go application framework, and the skill packs its conventions, component documentation, and practical examples so an agent produces production-ready code instead of approximating the framework's APIs.

The single goframe-v2 skill carries a references tree spanning CLI management, configuration, logging, error handling, the database ORM, web service development, microservices, and observability, plus an examples tree of runnable projects. It is designed to trigger only when the target project actually uses GoFrame, checked against go.mod and imports.

## Installation

```bash
npx skills add github.com/gogf/skills -g
```

Check for updates:

```bash
npx skills check
```

Install updates:

```bash
npx skills update
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| goframe-v2 | 3,376 | Write GoFrame v2 Go code: APIs, controllers, services, middleware, routing, config, ORM and database operations, gf CLI codegen, HTTP and gRPC services, and microservice conventions. |

All 1 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

GoFrame has a large surface area, and a generic Go agent will invent router, ORM, and config idioms that diverge from what the framework actually provides. This skill bundles the framework's own documentation and examples so a Hermes agent writes idiomatic GoFrame instead of guessing.

The trigger discipline matters as much as the content: the skill activates only when go.mod requires github.com/gogf/gf/v2 or the code imports it, and it declines generic Go, frontend, or infrastructure work. That keeps the skill from polluting unrelated sessions with framework context.

The examples tree is the practical payoff: runnable projects for HTTP servers, gRPC, databases, observability, and injection patterns give an agent a working reference to copy from rather than a prose description to paraphrase. The README recommends Claude Opus 4.6 or later for the best code generation.

## Usage

| You say | What happens |
|---|---|
| "Build a user service with GoFrame and RESTful CRUD" | goframe-v2 scaffolds the service using GoFrame's API, controller, service, and DAO conventions. |
| "Add JWT authentication to this GoFrame project" | The skill applies GoFrame middleware and config patterns for protected endpoints. |
| "Set up database access for this model" | The skill uses GoFrame's ORM, DAO, DO, and entity layers and the gf CLI codegen. |
| "Add an HTTP endpoint with request validation" | The skill applies GoFrame's routing, request input, and validation conventions. |
| "Convert this service to gRPC" | The skill uses GoFrame's gRPC and microservice scaffolding and conventions. |

## Verification

Confirm the skill landed in the agent skills directory after install, and probe the SKILL.md on the `main` branch before reviewing (returns 200):

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/gogf/skills/main/skills/goframe-v2/SKILL.md
```

```bash
npx skills check
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| goframe-v2 | Pass | Warn | Pass |

The sample covers the single indexed listing; it passes Gen Agent Trust Hub and Snyk with a Socket Warn.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,376 combined installs across 1 indexed listing; 83 GitHub stars; no LICENSE file; last pushed 2026-06-05. Counts drift over time.
- There is no LICENSE file, so treat the repo as all-rights-reserved rather than open source until terms are confirmed with GoFrame.
- The README marks the project as in beta, so expect the skill content to change between updates.
- Everything ships as one large skill (974 files in the tree), so the full references and examples trees come along with the single SKILL.md.
- The skill recommends Claude Opus 4.6 or later; other models may produce lower-quality GoFrame code.

## Related

- [CXUU Golang Skills - Go Engineering Suite](/hermes/skills/catalog/cxuu-golang-skills-setup)
- [Encore Skills - Backend Service Development Setup](/hermes/skills/catalog/encore-skills-setup)
- [Walden - Spec-Driven Development with Executable Proofs](/hermes/skills/catalog/walden-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Confirm the project actually imports github.com/gogf/gf/v2 before relying on the skill; it is designed not to trigger otherwise.
- Use the examples tree as a copy source: a runnable project beats a prose description for framework idioms.
- Run `npx skills check` and `npx skills update` periodically; the skill is in beta and changes between versions.
- Prefer the ORM, DAO, DO, and entity layers and gf CLI codegen over hand-written SQL for schema work.
- Pair the skill with a capable model; the README recommends Claude Opus 4.6 or later for the best output.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
