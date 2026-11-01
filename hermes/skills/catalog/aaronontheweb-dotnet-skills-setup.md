---
title: "Aaronontheweb Dotnet Skills - Akka.NET Suite"
description: "aaronontheweb/dotnet-skills: 22.0K combined installs. A .NET pack for Akka.NET, Aspire, EF Core and C# standards, distinct from dotnet/skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "dotnet", "csharp", "akka.net", "aspire"]
---

# Aaronontheweb Dotnet Skills - Setup Guide

**Source:** [aaronontheweb/dotnet-skills](https://www.skills.sh/aaronontheweb/dotnet-skills) via skills.sh - 22.0K combined installs across 40 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [aaronontheweb/dotnet-skills](https://github.com/aaronontheweb/dotnet-skills) - 1,244 stars, MIT, branch master, last pushed 2026-10-28; 39 directories under `skills/`, one `SKILL.md` each, with `agents/` holding six agent definitions, `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` as the two plugin manifests

**Category:** .NET engineering beyond the official pack: Akka.NET actors, testing, packaging and API design

**Quality Tier:** 🟡 Yellow - one Snyk Warn on opentelemetry-net-instrumentation holds the pack at Yellow, even though every other sampled Gen Agent Trust Hub and Socket verdict is a Pass and the repository is MIT

This is the .NET skill pack by Aaron Stannard, the Akka.NET maintainer, and it is not the same collection as the official `dotnet/skills` suite already documented on this site as Dotnet Skills - .NET AI Coding Setup. The distinction matters before installing either: the official suite tracks the .NET platform, while this one is opinionated production code from Akka.NET, Petabridge and Sdkbin, and it says so in the README, which describes the pack as battle-tested patterns covering C#, Akka.NET, Aspire, EF Core, testing and performance optimisation. Where the two overlap on C# and EF Core, the house style here is explicit: immutability by default, nullable reference types, composition over inheritance with sealed classes, and no AutoMapper and no reflection-heavy frameworks.

The counts are worth reading carefully because they are the first place a reader can get confused. The README's own summary says 30 skills and 5 specialized agents, `skills/` holds 39 directories, `.claude-plugin/plugin.json` lists 39 skills and six agents, and skills.sh indexes 40 listings. The extra listing is `transactional-emails` at 4 installs, which has no directory in the current tree. None of that changes what an installer gets, but it does mean the skill count quoted in the README, the plugin manifest and the install index disagree, and the index is the source that matters for this catalogue.

The pack divides into five rough groups. C# language and code quality carries the top of the table, with `modern-csharp-coding-standards` at 2,264 installs and `csharp-concurrency-patterns` at 1,593 above everything else. Data access is `efcore-patterns` and `database-performance`. Aspire gets its own cluster of five skills covering configuration, service defaults, integration testing, Mailpit email testing and Akka.NET wiring. Testing covers TestContainers, Playwright for Blazor, Verify snapshots, CsCheck property tests and CRAP analysis. The rest is tooling: ILSpy decompilation, local tool manifests, package management, serialization, dev certificate trust and container publishing.

## Installation

The Claude Code CLI route is the one the README leads with, and it is run inside the CLI rather than the editor extension:

```
/plugin marketplace add https://github.com/Aaronontheweb/dotnet-skills
/plugin install dotnet-skills
```

Codex has its own marketplace and plugin commands, and the README notes that the specialized agents are Claude Code-specific and are not included in the Codex plugin:

```bash
codex plugin marketplace add Aaronontheweb/dotnet-skills
codex plugin add dotnet-skills@dotnet-skills
codex plugin list
```

GitHub Copilot uses the same slash-command shape with a different update command, `/plugin update dotnet-skills@dotnet-skills`, and the README also documents a copy route for Copilot at project level into `.github/skills/` and globally into `~/.copilot/skills/`. OpenCode gets a `for` loop that reads each `SKILL.md` frontmatter `name` and copies the file into `~/.config/opencode/skills/$skill_name`, which is a reminder that directory names and skill names are not the same thing in this repo.

There is no `npx skills add` command in this README. The newest route is the GitHub Copilot or OpenCode copy pattern, and it maps onto a Hermes profile by changing the destination:

```bash
git clone https://github.com/Aaronontheweb/dotnet-skills.git /tmp/dotnet-skills
cp -r /tmp/dotnet-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

If the agents are wanted as well, copy them separately, since they are Claude Code sub-agent definitions rather than skills:

```bash
cp /tmp/dotnet-skills/agents/*.md ~/.hermes/profiles/corpusiq/agents/
```

The README's other install advice is a router snippet for `AGENTS.md` or `CLAUDE.md` that names which skills to consult for which task class, plus a generated compressed index block that can be refreshed with `./scripts/generate-skill-index-snippets.sh --update-readme`. Both are worth carrying over to a Hermes profile's own guidance file, because the pack is large enough that the model will not reliably pick the right skill by description alone.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| modern-csharp-coding-standards | 2,264 | Writing modern, high-performance C#: records, pattern matching, value objects, async/await, `Span<T>` and `Memory<T>`, plus the pack's ban on AutoMapper and reflection-heavy frameworks. |
| csharp-concurrency-patterns | 1,593 | Choosing the right concurrency abstraction, from async/await for I/O to Channels for producer/consumer work to Akka.NET actors for stateful entities. |
| efcore-patterns | 1,578 | Entity Framework Core practice: NoTracking by default, query splitting for navigation collections, migration management and dedicated mapping configurations. |
| dependency-injection-patterns | 684 | Organising DI registrations as composable `Add*` extension methods on `IServiceCollection`, with scope management and keyed services. |
| database-performance | 679 | Database access patterns that scale: separated read and write models, N+1 avoidance, `AsNoTracking`, row limits and no application-side joins. |
| api-design | 673 | Designing stable public APIs with extend-only design: API compatibility, wire compatibility and versioning for NuGet packages. |
| dotnet-project-structure | 672 | Solution layout with the `.slnx` format, `Directory.Build.props`, central package management, SourceLink and version management. |
| type-design-performance | 668 | Designing .NET types for performance: sealed classes, readonly structs, static pure functions, avoiding premature enumeration and picking the right collection. |
| ilspy-decompile | 621 | Decompiling assemblies with ILSpy to see how a .NET API works internally or inspect what a NuGet package actually ships. |
| package-management | 596 | Managing NuGet with Central Package Management and the `dotnet` CLI, never editing package XML by hand. |
| microsoft-extensions-configuration | 591 | Microsoft.Extensions.Options patterns: `IValidateOptions`, strongly typed settings, validation on startup and clean injection of configuration. |
| serialization | 581 | Choosing a serialization format: schema-based Protobuf and MessagePack over reflection-based options, System.Text.Json source generators and AOT implications. |
| crap-analysis | 568 | Scoring coverage and CRAP (Change Risk Anti-Patterns) risk, with OpenCover output and ReportGenerator wiring for risk hotspots. |
| dotnet-slopwatch | 565 | Catching LLM reward hacking after a code change: disabled tests, suppressed warnings, empty catch blocks and similar shortcuts, via the Slopwatch tool. |
| testcontainers-integration-tests | 558 | Writing integration tests against real infrastructure with the TestContainers 3.0+ module builders for PostgreSQL, Redis, RabbitMQ and networks. |
| playwright-blazor-testing | 549 | End-to-end testing Blazor Server and WebAssembly apps with Playwright: navigation, interaction, authentication, selectors, page objects and async assertions. |
| dotnet-local-tools | 538 | Pinning team tooling with `dotnet-tools.json` manifests for consistent tools across development machines and CI. |
| aspire-integration-testing | 511 | Writing distributed application integration tests with `DistributedApplicationTestingBuilder` and `Aspire.Hosting.Testing` under xUnit. |
| mjml-email-templates | 502 | Building responsive transactional email with MJML, compiled to cross-client HTML that renders in Outlook, Gmail and Apple Mail. |
| aspire-service-defaults | 486 | Creating a shared ServiceDefaults project that centralises OpenTelemetry, health checks, resilience and service discovery for Aspire apps. |

The remaining 20 indexed listings range from 4 to 476 installs.

## Why This Matters for Hermes Agents

.NET is a platform where plausible code compiles and then misbehaves: a `Task` where a `Channel` was needed, an `IQueryable` that turns into an N+1 storm, a nullable annotation that lies about a return. This pack attacks that with reference documents rather than prompts. The README asks contributors for skills that are comprehensive reference material of 10 to 40 KB with concrete examples and anti-patterns, and the resulting files carry the rules an experienced .NET developer applies without thinking.

The strongest entries are the ones that settle a choice rather than describe an API. `csharp-concurrency-patterns` exists to pick between async/await, Channels and actors. `serialization` exists to pick a format. `api-design` exists to enforce extend-only evolution of a public surface. An agent that loads one of these before writing code is answering a design question the user did not ask explicitly, which is usually where generated .NET goes wrong.

The pack also carries two quality gates that act after generation. `dotnet-slopwatch` is explicitly aimed at LLM-authored code, looking for disabled tests, suppressed warnings and other reward-hacking shapes, and the README's router snippet says to run it after any substantial new or refactored code. `crap-analysis` scores change risk against coverage. Together they turn "the tests pass" into "the change is not hiding something", which is the check most agent workflows skip.

Finally, the pack is opinionated enough to be useful as a style contract. No AutoMapper, no reflection-heavy frameworks, sealed by default, records and readonly structs for value types, DI everywhere. Whether or not a team agrees, having that written down means an agent's output matches the rest of the codebase instead of importing a generic average of the internet.

## Usage

| You say | What happens |
|---|---|
| "Review this service class against our C# standards" | `modern-csharp-coding-standards` checks for records and value objects, nullable correctness, `Span<T>` opportunities and the AutoMapper ban. |
| "Should this be a Channel or an actor" | `csharp-concurrency-patterns` picks between async/await, Channels and Akka.NET based on the statefulness and throughput described. |
| "This EF Core query is slow in production" | `efcore-patterns` and `database-performance` look for missing `AsNoTracking`, N+1 patterns, query splitting needs and application-side joins. |
| "Add integration tests against a real Postgres" | `testcontainers-integration-tests` writes xUnit tests using the current TestContainers module builder API. |
| "I changed a public API surface, is it compatible" | `api-design` checks extend-only rules and both API and wire compatibility, with `snapshot-testing` able to approve the surface as a baseline. |
| "Run the quality gates on this refactor" | `dotnet-slopwatch` scans for disabled tests and suppressed warnings, then `crap-analysis` scores the changed code's risk against coverage. |
| "Wire OpenTelemetry and health checks into this Aspire app" | `aspire-service-defaults` builds the shared ServiceDefaults project, with `opentelemetry-net-instrumentation` available for the spans and metrics detail. |

## Verification

The raw path for the top skill returned HTTP 200 on branch master when this guide was written on 2026-10-31. Note that the URL uses the directory name, not the skill name:

```bash
curl -sL -o /dev/null -w "%{http_code} csharp-coding-standards\n" \
  https://raw.githubusercontent.com/aaronontheweb/dotnet-skills/master/skills/csharp-coding-standards/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and the directory-to-name mapping, which is the thing most likely to confuse an agent looking a skill up by name later:

```bash
ls /tmp/dotnet-skills/skills | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/csharp-coding-standards/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills | grep -c aspire
```

The count should print 39, the header should show `name: modern-csharp-coding-standards` inside a directory called `csharp-coding-standards`, and the aspire filter should match five directories.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| modern-csharp-coding-standards | Pass | Pass | Pass |
| microsoft-extensions-configuration | Pass | Pass | Pass |
| aspire-configuration | Pass | Pass | Pass |
| opentelemetry-net-instrumentation | Pass | Pass | Warn |
| transactional-emails | Pass | Pass | Pass |

Every skill in this repo is a markdown reference document. There is no package, no build step, no postinstall hook and no bundled script: the commands that appear in the skills are ordinary `dotnet` CLI invocations that the agent chooses to run. That is a much smaller surface than a pack that ships validators, and it is consistent with the clean Gen Agent Trust Hub and Socket results across the sample.

The single Snyk Warn lands on `opentelemetry-net-instrumentation`, which is also the heaviest of the sampled documents, covering traces, metrics, logs, naming conventions and exporters. There is no finding to read in the pack, so treat it as a heuristic flag on a configuration-dense skill rather than a defect, and read that skill before installing it into a profile that runs against production telemetry endpoints.

The one credential-shaped area is `dotnet-devcert-trust`, which documents HTTPS development certificate trust on Linux including system CA bundle inclusion. That means a `sudo` step and a change outside the repository, so review it before letting an agent run it unattended.

## Limitations

- Snapshot data, verified 2026-10-31: 21,954 combined installs across 40 indexed listings; 1,244 GitHub stars; MIT; last pushed 2026-10-28. Counts drift over time.
- The install index outruns the tree: `transactional-emails` carries 4 installs but has no matching directory under `skills/` in the current tree, so the README, plugin manifest and index disagree on the skill count (30, 39 and 40 respectively).
- Directory names are not skill names. Roughly a third of the directories differ from the skill's own frontmatter `name` (for example `csharp-coding-standards` holds `modern-csharp-coding-standards`, and `microsoft-extensions-dependency-injection` holds `dependency-injection-patterns`), so raw URLs and `grep` lookups must use the directory name.
- One directory name is misspelled in the tree, `skills/opentelementry-dotnet-instrumentation/`, while the skill and the listing are both `opentelemetry-net-instrumentation`.
- This is not the official `dotnet/skills` suite, and it is not a general .NET catalogue: a single maintainer's production opinions, weighted toward Akka.NET, Aspire and Petabridge house style.
- The six agent definitions in `agents/` are Claude Code sub-agents and are not part of the Codex plugin, so a Hermes profile gains skills only unless the agent files are copied separately.

## Related

- [Dotnet Skills - .NET AI Coding Setup](/hermes/skills/catalog/dotnet-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Asyraf Hussin Skills - Clean Code Suite](/hermes/skills/catalog/asyrafhussin-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install this and the official `dotnet/skills` suite into different profiles, or at least read both indexes first. They overlap on C# and EF Core and they do not agree on style.
- Copy in the router snippet from the README. With 39 skills, description matching alone will not reliably surface `csharp-concurrency-patterns` for a concurrency question.
- Use `dotnet-slopwatch` as a step after generation, not as a review aid. Its whole design is to catch LLM shortcuts such as disabled tests and suppressed warnings the moment they land.
- Reach for `ilspy-decompile` before guessing at a NuGet package's internals. It is the cheapest way to stop an agent inventing an API that does not exist.
- Keep the `AGENTS.md` snippet generator in mind if the skill set drifts: `./scripts/generate-skill-index-snippets.sh --update-readme` regenerates the compressed index block the README uses.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
