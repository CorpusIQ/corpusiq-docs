---
title: "Wshaddix .NET Skills - Developer Suite Setup"
description: "wshaddix/dotnet-skills: Claude Code skills and sub-agents for .NET developers covering C#, ASP.NET Core, Blazor and EF Core - 13.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wshaddix-dotnet-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "dotnet", "csharp", "asp.net core", "blazor"]
---

# Wshaddix .NET Skills - Developer Suite Setup

**Source:** [wshaddix/dotnet-skills](https://www.skills.sh/wshaddix/dotnet-skills) via skills.sh - 13.5K combined installs across 96 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [wshaddix/dotnet-skills](https://github.com/wshaddix/dotnet-skills) - 92 stars, no LICENSE file (the README claims MIT but GitHub reports no license), master branch, last pushed Feb 27, 2026; 167 skill directories under `skills/<name>/SKILL.md`, 16 agents under `agents/` and 12 commands under `commands/`, plus a `.claude-plugin/plugin.json` manifest.
**Category:** .NET Development Skills and Sub-Agents
**Quality Tier:** 🟡 Yellow - no LICENSE file and stale (last pushed Feb 27, 2026), even though all 20 sampled skills carry clean Pass verdicts and the repository holds 92 stars.

wshaddix/dotnet-skills is an individual publisher's re-upload of Aaron Stannard's .NET Skills for Claude Code plugin. The README advertises 167 skills and 16 specialized agents across C#, ASP.NET Core, Blazor, MAUI, EF Core, Native AOT, testing, security, performance, CI/CD and cloud-native work, and the tree backs that up with 167 SKILL.md directories, 16 agent definitions and 12 slash commands.

The skills.sh index, however, carries only 96 listings combining to 13.5K installs, so 71 of the tree's skills are not indexed. The copy is also stale and unlicensed: the repository has no LICENSE file, has not been pushed since Feb 27, 2026, and the bundled README still points its install commands at the original Aaronontheweb/dotnet-skills repository, which is separately catalogued on this site.

## Installation

The README in this repository is copied from Aaronontheweb/dotnet-skills, so its install commands still point at that repository rather than this listing. The Claude Code plugin route is run inside the CLI:

```
/plugin marketplace add Aaronontheweb/dotnet-skills
/plugin install dotnet-skills
```

Update with `/plugin marketplace update`. These commands install the original suite, not this listing.

To install the wshaddix copy, substitute the owner in the clone routes. GitHub Copilot at project level:

```bash
git clone https://github.com/wshaddix/dotnet-skills.git /tmp/dotnet-skills
cp -r /tmp/dotnet-skills/skills/* .github/skills/
```

Or globally:

```bash
mkdir -p ~/.copilot/skills
cp -r /tmp/dotnet-skills/skills/* ~/.copilot/skills/
```

OpenCode copies each skill's SKILL.md and the agents:

```bash
git clone https://github.com/wshaddix/dotnet-skills.git /tmp/dotnet-skills
mkdir -p ~/.config/opencode/skills ~/.config/opencode/agents
for skill_file in /tmp/dotnet-skills/skills/*/SKILL.md; do
  skill_name=$(grep -m1 "^name:" "$skill_file" | sed 's/name: *//')
  mkdir -p ~/.config/opencode/skills/$skill_name
  cp "$skill_file" ~/.config/opencode/skills/$skill_name/SKILL.md
done
cp /tmp/dotnet-skills/agents/*.md ~/.config/opencode/agents/
```

There is no `npx skills add` line in the README. The nearest Hermes equivalent is the Copilot copy pattern with the destination pointed at a profile's skills directory:

```bash
git clone https://github.com/wshaddix/dotnet-skills.git /tmp/dotnet-skills
cp -r /tmp/dotnet-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The README also documents an AGENTS.md router snippet that maps task classes to skill names; copy it over for a suite this large.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| dotnet-xunit | 625 | Writing xUnit v3 tests: Fact/Theory, fixtures, parallelism, IAsyncLifetime, with v2 compatibility. |
| dotnet-testing-strategy | 624 | Deciding how to test .NET code: unit vs integration vs end-to-end via a decision tree, plus test doubles. |
| csharp-wolverinefx | 575 | Building .NET apps with WolverineFX for messaging, HTTP services, event sourcing with Marten, CQRS and outbox patterns. |
| testcontainers | 571 | Spinning up real dependencies (databases, message brokers) in .NET integration tests with Testcontainers and Docker. |
| microsoft-extensions-dependency-injection | 557 | Configuring Microsoft DI containers: service lifetimes, decorator patterns and service interception. |
| logging-observability | 551 | Production logging and observability for ASP.NET Core: Serilog structured logging, correlation IDs, health checks and OpenTelemetry tracing. |
| validation-patterns | 545 | Validation in ASP.NET Core: FluentValidation, DataAnnotations, IValidatableObject, IValidateOptions and MediatR pipeline behavior. |
| project-structure | 541 | Organizing .NET solutions: solution structure, .slnx format, Directory.Build.props, central package management and SourceLink. |
| dotnet-domain-modeling | 539 | Modeling business domains: aggregates, value objects, domain events, rich models and repositories. |
| dotnet-wpf-modern | 366 | Building WPF on .NET 8+: host builder, MVVM Toolkit, Fluent theme, performance and modern C# patterns. |
| dotnet-winforms-basics | 295 | Building WinForms on .NET 8+: high-DPI, dark mode (experimental), DI patterns and modernization tips. |
| dotnet-csharp-modern-patterns | 191 | Using modern C# 12-15: records, pattern matching, primary constructors and collection expressions. |
| dotnet-security-owasp | 183 | Securing .NET code and reviewing for vulnerabilities against the OWASP Top 10. |
| dotnet-csharp-code-smells | 180 | Reviewing C# for logic issues: anti-patterns, common pitfalls, async misuse and DI mistakes. |
| dotnet-api-security | 177 | Implementing API auth: Identity, OAuth/OIDC, JWT bearer, passkeys (WebAuthn), CORS and rate limiting. |

The remaining 81 indexed listings range from 74 to 137 installs.

## Why This Matters for Hermes Agents

.NET has sharp edges that compile clean and fail at runtime: an IQueryable that becomes an N+1 storm, a Task where a Channel was needed, a nullable annotation that lies about a return. The suite attacks these with reference documents rather than prompts, and its strongest entries settle a choice instead of describing an API. dotnet-testing-strategy picks unit versus integration, dotnet-domain-modeling shapes aggregates and value objects, and dotnet-api-security lays out the whole auth stack, so an agent that loads one of these before writing code answers a design question the user never asked, which is where generated .NET usually goes wrong.

The caveat is provenance. This listing is a copy of Aaron Stannard's Aaronontheweb/dotnet-skills, and the copy lags it: no LICENSE file, no push since Feb 27, 2026, and a README that still points its install commands at the original. A builder who wants the same skills with a current tree and an MIT license should prefer the original, which is separately catalogued. The 20 sampled security verdicts here are all clean Pass, so the content itself is not the risk; the risk is adopting a stale, unlicensed mirror when a maintained source exists.

## Usage

| You say | What happens |
|---|---|
| Write xUnit tests for this service | dotnet-xunit walks through v3 Fact/Theory, fixtures and the async lifecycle with v2 compatibility. |
| Should this be a unit or an integration test | dotnet-testing-strategy runs the unit vs integration vs end-to-end decision tree and picks test doubles. |
| Build a message handler with WolverineFX | csharp-wolverinefx sets up command handlers, message handlers, outbox patterns and Marten event sourcing. |
| Spin up a real Postgres for integration tests | testcontainers starts the database container and writes tests against the real dependency. |
| Wire up dependency injection for this API | microsoft-extensions-dependency-injection configures lifetimes, decorators and service interception. |
| Add structured logging and tracing to this API | logging-observability sets up Serilog, correlation IDs, health checks and OpenTelemetry. |
| Add FluentValidation to this form | validation-patterns wires FluentValidation, DataAnnotations and options validation. |

## Verification

Confirm the top skill and read its routing before installing:

```bash
curl -sL https://raw.githubusercontent.com/wshaddix/dotnet-skills/master/skills/dotnet-xunit/SKILL.md | head -40
```

Review the testing strategy and the WolverineFX skill:

```bash
curl -sL https://raw.githubusercontent.com/wshaddix/dotnet-skills/master/skills/dotnet-testing-strategy/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/wshaddix/dotnet-skills/master/skills/csharp-wolverinefx/SKILL.md | head -40
```

Inspect the Testcontainers skill before writing Docker-backed integration tests:

```bash
curl -sL https://raw.githubusercontent.com/wshaddix/dotnet-skills/master/skills/testcontainers/SKILL.md | head -40
```

After the copy lands, confirm the skill count matches the tree's 167 directories:

```bash
git clone https://github.com/wshaddix/dotnet-skills.git /tmp/dotnet-skills
ls /tmp/dotnet-skills/skills | wc -l
```

The raw URLs use the master branch, not main.

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dotnet-xunit | Pass | Pass | Pass |
| dotnet-testing-strategy | Pass | Pass | Pass |
| csharp-wolverinefx | Pass | Pass | Pass |
| testcontainers | Pass | Pass | Pass |
| microsoft-extensions-dependency-injection | Pass | Pass | Pass |
| logging-observability | Pass | Pass | Pass |
| validation-patterns | Pass | Pass | Pass |
| project-structure | Pass | Pass | Pass |
| dotnet-domain-modeling | Pass | Pass | Pass |
| dotnet-wpf-modern | Pass | Pass | Pass |
| dotnet-winforms-basics | Pass | Pass | Pass |
| dotnet-csharp-modern-patterns | Pass | Pass | Pass |
| dotnet-security-owasp | Pass | Pass | Pass |
| dotnet-csharp-code-smells | Pass | Pass | Pass |
| dotnet-api-security | Pass | Pass | Pass |
| dotnet-csharp-async-patterns | Pass | Pass | Pass |
| dotnet-csharp-dependency-injection | Pass | Pass | Pass |
| dotnet-architecture-patterns | Pass | Pass | Pass |
| dotnet-performance-patterns | Pass | Pass | Pass |
| dotnet-solid-principles | Pass | Pass | Pass |

Every one of the 20 sampled skills carries a clean Pass across Gen Agent Trust Hub, Socket and Snyk. Every skill in this repository is a markdown reference document: there is no package, build step, postinstall hook or bundled executable, and the commands that appear in the skills are ordinary dotnet CLI invocations the agent chooses to run, so the surface is small and the clean verdicts are unsurprising. The repository has no LICENSE file (GitHub reports no license even though the copied README claims MIT), so treat the redistribution terms as unclear.

## Limitations

- Snapshot data, verified Nov 22, 2026: 13.5K combined installs across 96 indexed listings; 92 GitHub stars; no LICENSE file; last pushed Feb 27, 2026. Counts drift over time.
- There is no LICENSE file at the repository root: GitHub reports no license even though the copied README claims MIT, so redistribution and modification rights are unclear.
- The skills.sh index carries 96 listings, far fewer than the 167 skills the README advertises and the 167 SKILL.md directories the tree ships; 71 skills are not indexed.
- The repository has not been pushed since Feb 27, 2026, so it is several months stale and behind the Aaronontheweb/dotnet-skills source it was copied from.
- This is a copy of Aaron Stannard's Aaronontheweb/dotnet-skills. The bundled README still points its install commands at that repository, so following the README verbatim installs the original, not this listing.
- The branch is master, not main; every raw URL above uses master and should not be rewritten to main.

## Related

- [Aaronontheweb Dotnet Skills - Akka.NET Suite](/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup)
- [Dotnet Skills - .NET AI Coding Setup](/hermes/skills/catalog/dotnet-skills-setup)
- [DotNet Claude Kit - .NET 10 Engineering Setup](/hermes/skills/catalog/codewithmukesh-dotnet-claude-kit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Prefer the original Aaronontheweb/dotnet-skills over this copy: it is MIT-licensed and actively maintained, while this listing lags it and has no LICENSE file.
- Substitute `wshaddix` for `Aaronontheweb` in the README's clone and plugin commands if you specifically want this listing; the README points at the original.
- Copy the AGENTS.md router snippet into your profile guidance file; with 167 skills, description matching alone will not surface the right skill for a task.
- Run dotnet-security-owasp and dotnet-api-security as pre-commit review steps, not afterthoughts.
- Re-check the skills.sh security pages before production use; the clean sample covers 20 of 96 listings and the other 76 are unverified.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
