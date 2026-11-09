---
title: "Samber Go Skills - Golang Engineering Standards"
description: "samber/cc-skills-golang on skills.sh: 1.8M combined installs; 46 Go skills covering style, concurrency, testing, security and project layout."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/samber-golang-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "golang", "go", "code review"]
---

# Samber Go Skills - Setup Guide

**Source:** [samber/cc-skills-golang](https://www.skills.sh/samber/cc-skills-golang) via skills.sh - 1,804,037 combined installs across 46 indexed listings; first documented September 29, 2026, refreshed in the Nov 8, 2026 evening sweep
**GitHub:** 3,816 stars, MIT via LICENSE, main branch, last pushed 2026-11-08, 46 SKILL.md directories under skills/
**Category:** Development
**Quality Tier:** 🟡 Beta - 46 directory-matched SKILL.md files, an evaluation log with assertion counts per skill and 3,816 stars, held at Beta because scan verdicts exist for only 5 of the 46 skills and one of those warns.

This is the Go standards library rather than a single skill. Forty-six instruction files cover language style, error handling, concurrency, testing, performance, security, observability, project layout and the framework or library clusters around them. The repository is deliberately scoped: the README states that it covers Go-specific skills only and points to the sibling samber/cc-skills repository for workflow skills such as git conventions, CI/CD and PR review. Anyone expecting one plugin to cover the whole Go delivery pipeline will need both.

The provenance is the part worth reading before the install. The README says the skills were bootstrapped with Claude Code by distilling the author's Go project commits, and then states plainly that they are edited, tested, reviewed and reworked by a human, with the line "No AI slop here." That claim is backed by EVALUATIONS.md, which publishes an assertion count and a with-skill against without-skill score for 41 of the 46 skills. The README summary reads 3348 of 3439 assertions with the skills loaded (97 percent) against 1957 of 3439 without them (57 percent), a 40 point gap. The same tables publish the weak results: golang-spf13-viper scores 98 percent with the skill against 100 percent without, golang-uber-fx gains 5 points and golang-uber-dig 10. Publishing the near-zero deltas is what makes the rest of the table credible.

Adoption sits at 1804.0K combined installs across the 46 indexed listings, and the distribution is unusual. The general engineering skills are tightly packed between 40K and 46K, the framework and library skills cluster around 38K, and three listings sit far below at 12K to 13K. A flat curve like that usually means the repository is installed as a bundle rather than picked apart per skill, which matches the README's own advice in the next section.

## Installation

The README documents the skills CLI first, described there as universal for any Agent Skills compatible tool. The full set is one command, and a single skill is the same command with a filter:

```bash
npx skills add https://github.com/samber/cc-skills-golang --all
npx skills add https://github.com/samber/cc-skills-golang --skill golang-performance
```

Test the second form before committing to the first. One skill is enough to confirm that the CLI resolves the repository and writes where the agent can find it, and it keeps the context cost low while you decide whether the library fits.

Claude Code has its own plugin route, which pins the marketplace to the samber/cc repository:

```bash
/plugin marketplace add samber/cc
/plugin install cc-skills-golang@samber
```

Two other clients get their own plugin route. Gemini CLI installs the repository as an extension and updates with gemini extensions update. Codex installs a plugin from github:samber/cc-skills. Cursor, Copilot, OpenCode, Antigravity and Openclaw are handled by cloning the repository into each client's discovery directory, and the README gives the exact path per client, for example ~/.cursor/skills/cc-skills-golang or ~/.openclaw/skills/cc-skills-golang. The clone route is also the honest fallback when a client has no plugin system.

The repository ships one extra routing file outside the skills tree. rules/golang-always.mdc sets alwaysApply to true for **/*.go, **/go.mod, **/go.sum and **/go.work, and embeds the same table that maps a task intent to a primary and a set of secondary skills. That is the file to copy if the client reads Cursor style rule files instead of skill directories.

## What It Provides

The 24 listings at or above 40,928 installs are in the table below, with the remaining 22 described after it.

| Skill | Installs | Use For |
|---|---|---|
| golang-code-style | 45,979 | Line breaking, declarations, composite literals and control flow clarity, the judgment calls gofmt cannot make |
| golang-testing | 45,265 | Table-driven tests, parallel tests, fuzzing, goleak leak detection and coverage for new or flaky suites |
| golang-error-handling | 45,246 | Wrapping with %w, errors.Is and errors.As, sentinel errors, custom types and panic recovery |
| golang-security | 44,079 | SQL and command injection, crypto, path traversal, SSRF, secrets handling, gosec and threat modeling |
| golang-design-patterns | 43,710 | Functional options, constructor APIs, graceful shutdown, timeouts and retries, architecture styles |
| golang-performance | 43,560 | Allocation reduction, GC tuning, pooling and hot-path fixes once a profile has named the bottleneck |
| golang-concurrency | 43,495 | Goroutine leaks, channels against mutexes, errgroup, singleflight, worker pools and pipelines |
| golang-context | 42,649 | Cancellation, deadlines, context.WithoutCancel for background work, request-scoped values |
| golang-database | 42,446 | Parameterized queries, transactions, isolation levels, connection pools, migrations |
| golang-naming | 42,443 | Package, receiver, acronym, error and subtest naming, including New against NewTypeName |
| golang-safety | 42,157 | Nil panics, typed-nil interfaces, append aliasing, float comparison, integer truncation |
| golang-project-layout | 42,016 | cmd, internal and pkg conventions, go.work workspaces, module and package naming |
| golang-documentation | 41,902 | godoc comments, README and CHANGELOG structure, Example tests, llms.txt |
| golang-modernize | 41,874 | Recent language features, deprecation cleanups and Go version upgrades |
| golang-lint | 41,831 | golangci-lint configuration, linter selection, nolint suppressions, reading lint output |
| golang-data-structures | 41,775 | Slice and map internals, preallocation, container packages, generic collections, copy semantics |
| golang-troubleshooting | 41,478 | Crashes, deadlocks, races, pprof capture, Delve, GODEBUG tracing, production debugging |
| golang-observability | 41,464 | slog logging, Prometheus metrics, OpenTelemetry tracing, continuous profiling, alerting |
| golang-dependency-management | 41,326 | go.mod and go.sum, minimal version selection, replace and exclude, govulncheck, vendoring |
| golang-structs-interfaces | 41,268 | Embedding, type assertions and switches, interface segregation, field tags, receiver choice |
| golang-cli | 41,015 | Command structure, flag handling, exit codes, signals, shell completion, CLI unit tests |
| golang-benchmark | 40,979 | Writing and comparing benchmarks, benchstat, CI regression detection, runtime metrics |
| golang-dependency-injection | 40,942 | Manual constructor injection and choosing between wire, dig, fx and samber/do |
| golang-popular-libraries | 40,928 | Vetted libraries by category, new stdlib packages, standard-library-first tradeoffs |

The remaining 22 indexed listings range from 12,406 to 40,840 installs. That tail is not filler. It holds the whole samber family (lo, mo, ro, do, hot, oops, slog), the spf13, uber and Google wiring libraries, gRPC, GraphQL, Swagger and testify, plus three outliers at the bottom: golang-pkg-go-dev at 13,265, golang-refactoring at 12,799 and golang-gopls at 12,406. It also holds golang-how-to at 37,867, which is the orchestrator every other skill leans on and still sits below the table threshold.

The internal structure is one of five groups the README draws: code quality, architecture and design, QA and performance, project setup, and the framework or library skills. Within those, every skill declares its own version in frontmatter, and several declare tool permissions. golang-gopls and golang-how-to want gopls on PATH and offer it through gopls's MCP server, Claude Code's LSP tool or the CLI. golang-pkg-go-dev wraps godig, a pkg.go.dev API client that ships as both CLI and MCP server. The rest are markdown instruction files with no runtime.

The README makes one structural claim that changes how you install it: the skills are atomic, cross-referencing units, and installing a subset gives a partial and potentially inconsistent view. Error handling rules that affect logging live in golang-error-handling rather than golang-observability, and golang-code-style explicitly defers naming, lint and doc comments to their own skills. Partial installs therefore work, but they work the way a partial standard works.

## Why This Matters for Hermes Agents

Hermes writes Go in short bursts, often inside a repository it did not author, and the failures are predictable. An agent asked for a handler returns one that wraps errors with the wrong verb, logs the error twice, starts a goroutine with no exit path and treats a nil slice as an empty one. None of that is caught by gofmt, and most of it is invisible in review until production. The skills convert each failure into a written rule with a replacement, which is the only instruction form that survives a long context.

The second fit is routing. Forty-six skills cannot all be loaded, and picking the wrong one wastes a context window on the wrong domain. golang-how-to exists for exactly that: it maps intent to a primary skill plus secondary skills and loads them together, so a request to build a gRPC service pulls golang-grpc with golang-testing and golang-error-handling rather than golang-grpc alone. It also disambiguates the clusters that look alike, which for an agent is the practical failure mode: performance against benchmark against troubleshooting, and lo against mo against ro.

The third is that the repository is honest about the division of labour. golang-code-style opens by saying linters handle formatting and the skill handles clarity, so an agent that already runs golangci-lint does not get a second conflicting formatting opinion. In a Hermes workspace where CI already enforces gofmt and golangci-lint, that boundary is the difference between a standards file that helps and one that fights the toolchain.

The counterweight is scope. This is a Go library and nothing else. It will not tell an agent how to structure a commit, review a pull request or shape a release, and the README says so by pointing at the sibling repository. It also cannot enforce any of its own rules. Every guarantee here comes from the agent reading the file, or from a linter you already run.

## Usage

| You say | What happens |
|---|---|
| "Write tests for this HTTP handler" | Loads golang-testing, defaults to table-driven subtests, adds goleak where goroutines are involved |
| "This worker never shuts down cleanly" | Pairs golang-concurrency with golang-context, traces the missing cancellation path and adds errgroup |
| "Review this query builder for injection" | Runs golang-security over parameter binding, then golang-safety for nil and aliasing issues |
| "Why is this endpoint slow?" | golang-benchmark measures first with pprof and benchstat, then golang-performance applies the matching pattern |
| "Start a new service, what layout?" | golang-project-layout applies cmd, internal and pkg conventions and decides whether go.work is warranted |
| "Set up metrics and tracing" | golang-observability wires slog, Prometheus and OpenTelemetry, with alerting left explicit |
| "Bump this module to a newer Go" | golang-modernize rewrites old patterns, then golang-lint and golang-continuous-integration follow the toolchain |

The orchestrator has a second mode that matters more than any single skill. golang-how-to configure writes an always-load directive into the project's agent config file, which the skill names as CLAUDE.md, AGENTS.md, GEMINI.md, Cursor rules or Copilot instructions, plus an optional Required Go skills block. In Hermes that means AGENTS.md, so the routing layer can be committed with the repository instead of depending on the agent choosing to load it.

## Verification

The default branch is main, and the raw path follows the repository layout, so skills/<name>/SKILL.md is the file to fetch. This one returned 200:

```bash
curl -fsSL https://raw.githubusercontent.com/samber/cc-skills-golang/main/skills/golang-code-style/SKILL.md | head -20
```

It should open with YAML frontmatter naming golang-code-style, a description scoped to style conventions with explicit handoffs to golang-naming, golang-lint and golang-documentation, then license: MIT, author samber and version 1.3.0 under metadata. Under that you should see the orchestration note and the Go Proverbs line about clear being better than clever.

Confirm the shape of the repository rather than trusting the star count. A shallow clone and a count should both read 46:

```bash
git clone --depth 1 https://github.com/samber/cc-skills-golang /tmp/cc-skills-golang
find /tmp/cc-skills-golang/skills -name SKILL.md | wc -l
```

After installing, the CLI's own listing is the cheapest check that the agent can see what you installed:

```bash
npx skills list | grep golang-
```

That should show one line per installed skill. If it is empty, the install went to a different scope, and the fix is either -g for user level or a rerun from the project root. If npx skills use is available in your version, it will generate a prompt for a single skill without installing it, which is the fastest way to inspect one file before adopting the set.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08), re-read the verdict pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| golang-code-style | Pass | Pass | Pass |
| golang-project-layout | Warn | Pass | Pass |
| golang-popular-libraries | Pass | Pass | Pass |
| golang-samber-ro | Pass | Pass | Pass |
| golang-gopls | Pass | Pass | Pass |

One sampled skill warns. golang-project-layout carries a Warn from Gen Agent Trust Hub while Socket and Snyk both pass it, and the other four samples are clean on all three scanners. Four clean samples and one warn across 46 listings is not a clean bill of health, it is a sample, so treat the verdict as provisional and read the skills.sh page for any skill you plan to run in a production repository.

The content itself is markdown, which is why the scanners mostly pass. The real surface is what the skills instruct an agent to run and install. Frontmatter blocks declare allowed-tools with Bash(go:*) and Bash(git:*), and 13 of the 46 skills declare Go tool installs in frontmatter, naming the binaries the instructions assume: gopls through golang.org/x/tools/gopls@latest, gotests through github.com/cweill/gotests/gotests@latest, govulncheck through golang.org/x/vuln/cmd/govulncheck@latest and benchstat through golang.org/x/perf/cmd/benchstat@latest. Every one of those resolves @latest rather than a pinned version, so install and pin the binaries yourself if the pipeline needs reproducibility.

The largest permission decision is optional and lives outside the skills tree. GOLANG-AI-DRIVEN-REVIEW.md documents adding an AI reviewer to CI, and its example workflow requests pull-requests: write plus actions: read. The file itself flags the risk: those permissions apply to the entire repository, not just the current pull request, so an agent holding them can comment on any PR and read any run's logs. Scope it to trusted branches or skip that workflow entirely if the repository is public.

## Limitations

- Snapshot data, verified 2026-11-08: 1,804,037 combined installs across 46 indexed listings; 3,816 GitHub stars; MIT license; last pushed 2026-11-08. Counts drift over time.
- This page replaces the September 29 snapshot, which listed 35K+ installs against eight skills. The repository has since grown to 46 indexed listings, so the earlier install figure understated the set and the earlier Production tier overstated how much of it had been reviewed.
- The repository covers Go only. Git workflow, CI/CD and PR review skills live in the sibling samber/cc-skills repository, and installing this one alone leaves those uncovered.
- Only 24 of the 46 listings clear the 40,928 install threshold used here. The other 22 include the orchestrator golang-how-to and the entire samber library family, so the table understates what a full install actually contains.
- The evaluation log is not uniformly positive. golang-spf13-viper scores 98 percent with the skill against 100 percent without, and golang-spf13-cobra gains only 2 points, so those two files add little over a competent model.
- The skills version independently. golang-code-style is at 1.3.0, golang-how-to and golang-pkg-go-dev at 1.4.2, golang-modernize at 1.5.1, and there is no repository level release tag, so a pin means pinning a commit.
- Scan verdicts cover 5 of 46 skills, and one of the five warns. There is no full coverage claim to inherit.

## Related

- [Samber Developer Platform Skills - API & DX Setup](/hermes/skills/catalog/samber-developer-platform-skills-setup)
- [CXUU Golang Skills - Go Engineering Suite](/hermes/skills/catalog/cxuu-golang-skills-setup)
- [Angular Framework Skills - Official Repo Agent Guides](/hermes/skills/catalog/angular-framework-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the general purpose skills as a set. The README warns that a subset gives a partial and inconsistent view, and the cross-references between error handling, safety and observability are the reason.
- Run golang-how-to configure once per project. It writes the always-load directive into AGENTS.md, which is the only way the routing survives a session that starts with no memory of the previous one.
- Measure before optimising, in the order the repository intends: golang-benchmark first, golang-performance second. Reversing it produces pattern application with no bottleneck behind it.
- Read the error rate column in the README table before trusting a skill. The values are published per skill, and the single digit deltas are cheap to skip.
- Check the eval assertions for any skill you plan to cite. golang-security runs 110 assertions and golang-performance runs 272, while golang-data-structures runs 36, and the assertion count is a fair proxy for how specific the guidance is.
- Prefer the raw probe to the star count when anything looks off. A repository whose directory count no longer matches 46 has been reorganised, which is a reason to read the tree before trusting the install path.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
