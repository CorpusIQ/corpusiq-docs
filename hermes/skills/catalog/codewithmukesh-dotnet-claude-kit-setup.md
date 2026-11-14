---
title: "DotNet Claude Kit - .NET 10 Engineering Setup"
description: "codewithmukesh/dotnet-claude-kit: 176.3K combined installs across 65 listings, a 52-skill .NET 10 engineering kit with a Roslyn MCP server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codewithmukesh-dotnet-claude-kit-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "dotnet", "csharp", "claude code"]
---

# DotNet Claude Kit - Setup Guide

**Source:** [codewithmukesh/dotnet-claude-kit](https://www.skills.sh/codewithmukesh/dotnet-claude-kit) via skills.sh - 176.3K combined installs across 65 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 833 stars, MIT license, `main` branch, last pushed 2026-11-04, 52 `SKILL.md` files in `skills/<name>/` folders, plus 272 `.cs`, 9 `.csproj`, 8 shell and 6 Python files
**Category:** .NET 10 engineering, architecture and C# workflows for Claude Code
**Quality Tier:** 🟢 Green - 52 in-tree skills, a detailed README, and all four sampled verdicts pass.

dotnet-claude-kit is a Claude Code plugin by Mukesh Murugan that turns the agent into an opinionated .NET 10 and C# 14 developer. The README counts 52 skills, 11 specialist agents, 17 slash-command workflows, 10 rules, 7 project templates and 26 MCP tools, all activated by one plugin install plus a single `/dotnet-init` in the project root.

The install index outruns the tree: 65 indexed listings against 52 resolved `SKILL.md` files, a drift named in the Limitations. The repo is not prompt-only either - it ships 272 `.cs` files, 9 `.csproj` files, 8 shell scripts and 6 Python files, mostly the Roslyn MCP server and its hook scripts. The README reports its Roslyn navigator answered 55 benchmark questions 32 percent faster, with under half the tool calls and a 92-vs-61 accuracy score, against the default grep-and-read workflow.

## Installation

Install the Roslyn MCP server first, then add the plugin inside a Claude Code session:

```bash
dotnet tool install -g CWM.RoslynNavigator
```

Inside Claude Code, add the marketplace and install the plugin:

```text
/plugin marketplace add codewithmukesh/dotnet-claude-kit
/plugin install dotnet-claude-kit
```

Then run `/dotnet-init` once in your project directory, existing or greenfield. It detects your solution, scans `.csproj` SDKs, asks architecture questions, and generates a customized `CLAUDE.md`. It never overwrites an existing `CLAUDE.md` without asking to Merge, Overwrite, or Keep.

APM users can install the repo as-is:

```bash
apm install codewithmukesh/dotnet-claude-kit --target claude
```

For local development, load directly from disk:

```bash
claude --plugin-dir /path/to/dotnet-claude-kit
```

The 10 rules ship in the repo for you to copy into your project's `.claude/rules/` to make them always-loaded.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| clean-architecture | 3,858 | Clean Architecture: the 4-project layout (Domain, Application, Infrastructure, Api), dependency inversion, use case handlers, domain entities with behavior. |
| modern-csharp | 3,775 | Modern C# 14 and .NET 10 features: primary constructors, collection expressions, records, pattern matching, spans, raw string literals. |
| ddd | 3,769 | Domain-Driven Design tactical patterns: aggregates, value objects, domain events, strongly-typed IDs, repository patterns. |
| vertical-slice | 3,750 | Vertical Slice Architecture: feature folders, endpoint grouping, and handler patterns for Mediator, Wolverine, or raw handlers. |
| security-scan | 3,746 | Six-layer security scan: vulnerable packages, secrets, OWASP patterns, auth config, CORS, and data protection with severity-rated findings. |
| serilog | 3,731 | Structured logging with Serilog: two-stage bootstrap, enrichers, sinks, request logging, destructuring. |
| error-handling | 3,728 | Error handling: the Result pattern, ProblemDetails (RFC 9457), global exception handling, FluentValidation. |
| docker | 3,724 | Docker containerization: multi-stage builds, .NET container images, non-root user, health checks, .dockerignore. |
| testing | 3,719 | Testing strategy: xUnit v3, WebApplicationFactory, Testcontainers, Verify snapshots, the AAA pattern. |
| architecture-advisor | 3,718 | Architecture selection: asks structured questions, then recommends VSA, Clean Architecture, DDD plus Clean, or Modular Monolith. |
| ef-core | 3,714 | EF Core patterns: DbContext config, migrations, interceptors, compiled queries, ExecuteUpdateAsync, value converters. |
| minimal-api | 3,713 | Minimal APIs: MapGroup, endpoint filters, TypedResults, OpenAPI metadata, parameter binding. |
| logging | 3,708 | Observability glue: /health endpoints, correlation IDs, log-level strategy, with routing into serilog and opentelemetry. |
| resilience | 3,705 | Polly v8 resilience: retry, circuit breaker, timeout, fallback, rate limiter, hedging, composed pipelines. |
| httpclient-factory | 3,704 | IHttpClientFactory: named, typed and keyed clients, DelegatingHandlers, resilience, testing patterns. |
| project-structure | 3,703 | Solution structure: .slnx format, Directory.Build.props, central package management, global usings. |
| messaging | 3,701 | Async messaging: Wolverine and MassTransit, the outbox pattern, sagas, RabbitMQ and Azure Service Bus. |

The remaining 48 indexed listings range from 31 to 3,699 installs.

## Why This Matters for Hermes Agents

The kit's core bet is that an agent should query a codebase semantically instead of reading whole files. Its Roslyn MCP server answers navigation questions in 30 to 150 tokens where a grep-and-read pass costs 500 to 2,000 plus. Every list-returning tool reports a Truncated flag, so no single call can blow the context window.

The second property is opinionated defaults. The kit commits to Result over exceptions, TimeProvider over DateTime.Now, direct DbContext over repository wrappers, and WebApplicationFactory plus Testcontainers over in-memory fakes. Each default is documented in an ADR, which gives an agent a defensible reason for every choice it makes in your repo.

The workflow layer matters too. Slash commands like `/spec`, `/plan` and `/scaffold` chain the skills into a pipeline that ends in a diff, not a checklist. A vague feature becomes a persisted spec with acceptance criteria, then a plan, then generated feature slices with tests.

## Usage

| You say | What happens |
|---|---|
| "Set up this repo for .NET 10" | Runs `/dotnet-init`, scans the solution, asks architecture questions, and generates `CLAUDE.md`. |
| "Which architecture fits this project?" | Runs `architecture-advisor` and recommends VSA, Clean Architecture, DDD or Modular Monolith. |
| "Scaffold a new feature for orders" | Runs `/scaffold` and generates the full feature slice for the detected architecture. |
| "Where does this stack trace point in our code?" | The Roslyn `resolve_stack_trace` MCP tool maps frames to file and line. |
| "Is this codebase healthy?" | Runs `/health-check` and returns an A-to-F report card across eight dimensions. |
| "Clean up the dead code and TODOs" | Runs `/de-sloppify` through its seven ordered cleanup steps. |
| "Are our NuGet packages up to date?" | Runs `/outdated` and reports stale, vulnerable and license-trap packages. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/codewithmukesh/dotnet-claude-kit/main/skills/clean-architecture/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/codewithmukesh/dotnet-claude-kit/main/skills/architecture-advisor/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/codewithmukesh/dotnet-claude-kit/main/skills/security-scan/SKILL.md
```

Skills live at `skills/<name>/SKILL.md`, not in a category subfolder, so a verification script pointed at a nested layout will report a false failure.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| clean-architecture | Pass | Pass | Pass |
| modern-csharp | Pass | Pass | Pass |
| ddd | Pass | Pass | Pass |
| vertical-slice | Pass | Pass | Pass |

All four sampled skills pass all three auditors, which is the cleanest sample possible. The sample covers only 4 of the 65 indexed listings; the remaining listings publish no verdict, which is not the same as a pass. The verdicts also do not cover the repo's executable artifacts: the Roslyn MCP server, the hook shell scripts, and the Python utilities are code, not prompts, and need their own review before production use.

## Limitations

- Snapshot data, verified 2026-11-13: 176,295 combined installs across 65 indexed listings; 833 GitHub stars; MIT; last pushed 2026-11-04. Counts drift over time.
- The install index outruns the tree: 65 indexed listings against 52 resolved `SKILL.md` files. Thirteen listings, mostly workflow-variant names such as self-correction-loop and code-review-workflow, carry install counts but have no matching directory in the current tree.
- All four sampled verdicts pass, but that sample covers only 4 of 65 listings; the rest publish no verdict on skills.sh.
- This is not a prompt-only pack. The repo ships 272 `.cs` files, 9 `.csproj` files, 8 shell scripts and 6 Python files, and the skill-level verdicts do not cover any of them.
- Multi-harness layouts appear in the tree (`.claude/`, `.codex/`, `.cursor/`), and the skills.sh index reflects the `.claude` layout primarily; the Cursor and Codex compatibility files are not counted as skills.
- The README's benchmark numbers are the author's own measurements on five open-source solutions, not an independent audit.

## Related

- [Dotnet Skills - .NET AI Coding Setup](/hermes/skills/catalog/dotnet-skills-setup)
- [Aaronontheweb Dotnet Skills - Akka.NET Suite](/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `/dotnet-init` on a greenfield repo. It scaffolds the solution and generates `CLAUDE.md` without manual template copying, and it is the safest first move.
- Install the Roslyn MCP server (`dotnet tool install -g CWM.RoslynNavigator`) before judging the token-efficiency claims; the skills that rely on it assume it is present.
- Read `architecture-advisor` before trusting `/scaffold`. The advisor's recommendation decides which feature-folder layout scaffolding generates.
- Copy the 10 rules into `.claude/rules/` so they are always-loaded rather than only available on demand.
- Pin a tag or commit SHA (`codewithmukesh/dotnet-claude-kit#<tag-or-sha>`) to keep installs reproducible across machines.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
