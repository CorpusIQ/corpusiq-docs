---
title: "CXUU Golang Skills - Go Engineering Suite"
description: "cxuu/golang-skills: 24.9K combined installs. Twenty Go skills covering review, concurrency, errors, testing and style, each under 225 lines."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cxuu-golang-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "golang", "code review", "go style"]
---

# CXUU Golang Skills - Setup Guide

**Source:** [cxuu/golang-skills](https://www.skills.sh/cxuu/golang-skills) via skills.sh - 24.9K combined installs across 20 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [cxuu/golang-skills](https://github.com/cxuu/golang-skills) - 188 stars, Apache-2.0, branch main, last pushed 2026-06-20; 20 `SKILL.md` files, one per `skills/go-*/` directory, each under 225 lines, with 48 reference files, 8 shell scripts and 4 asset template folders alongside them

**Category:** Go engineering for coding agents: concurrency, error handling, testing and project layout

**Quality Tier:** 🟡 Yellow - every Socket and Snyk verdict is a Pass, but the sampled `go-interfaces` skill carries a Gen Agent Trust Hub warn, which is enough to hold the pack at Yellow

Twenty skills, each covering one decision area of Go, and the README is explicit about where the content comes from: the Google Go Style Guide, Effective Go, the Uber Go Style Guide and the Go Wiki CodeReviewComments. The skills are not summaries of those documents. They are decision trees for the moments an agent gets Go wrong: which error wrapping verb to use, when a goroutine needs a lifecycle, whether an interface should exist at all, whether a slice should be preallocated.

The packaging is the interesting part. Every `SKILL.md` stays under 225 lines so the core rules load cheaply, and 48 reference files sit behind them for on-demand loading, which is progressive disclosure done rather than described. Eight shell scripts cover the checks a review usually starts with, and four asset folders hold output templates. The suite also tracks rule ownership in `docs/RULE_OWNERSHIP.md` so the same guidance is not duplicated across skills, and Go-version-sensitive advice is supposed to name a minimum version and an older fallback.

## Installation

The README's recommended route installs all twenty through the skills CLI, which it documents for Cursor, Codex, OpenCode, Cline, GitHub Copilot, Windsurf, Roo Code and the other agents that support the format:

```bash
npx skills add cxuu/golang-skills --all
```

Claude Code gets a plugin route with the marketplace added once:

```bash
/plugin marketplace add cxuu/golang-skills
/plugin install golang-skills@cxuu-golang-skills
```

Cursor has a third route through Settings, Rules, Add Rule, Remote Rule (Github), pointing at `https://github.com/cxuu/golang-skills`. None of these three knows about Hermes, so the durable install is a directory copy that keeps each skill's `references/`, `scripts/` and `assets/` folders beside its `SKILL.md`:

```bash
git clone --depth 1 https://github.com/cxuu/golang-skills.git /tmp/cxuu-golang-skills
cp -r /tmp/cxuu-golang-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Copy the `skills/` directory and not the repository root, because the SKILL.md files live one level down under `skills/go-*/`. All eight bundled scripts expect a Go toolchain on `PATH`, and `setup-lint.sh` additionally expects `golangci-lint` to be installed already: it writes a `.golangci.yml`, runs the first lint and exits with an error when the binary is missing, so install the linter before using it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| go-code-review | 1,708 | A systematic checklist for reviewing Go code and PR submissions, with `scripts/pre-review.sh` running gofmt, go vet and golangci-lint first. |
| go-testing | 1,381 | Table-driven tests, subtests, test helpers, assertions and test organisation, with `scripts/gen-table-test.sh` scaffolding the test file. |
| go-linting | 1,305 | Linters, `golangci-lint` setup, nolint directives and CI integration, with `scripts/setup-lint.sh` doing the configuration. |
| go-error-handling | 1,299 | Error strategy decisions, wrapping with `%v` versus `%w`, sentinel errors and logging patterns, checked by `scripts/check-errors.sh`. |
| go-concurrency | 1,293 | Goroutine lifecycle, channels, mutexes, parallelisation and thread-safety rules. |
| go-interfaces | 1,286 | Interface design, abstractions, embedding and the accept interfaces, return structs rule, with `scripts/check-interface-compliance.sh`. |
| go-documentation | 1,286 | Doc comments, package docs, godoc formatting and runnable examples, with `scripts/check-docs.sh` finding exported symbols that lack them. |
| go-performance | 1,268 | String optimisation, capacity hints, benchmarking and `strconv` over `fmt`, with `scripts/bench-compare.sh` for before and after runs. |
| go-style-core | 1,266 | Formatting, nesting reduction, style principles and the fallback style guide when no other skill owns the case. |
| go-context | 1,258 | `context.Context` placement, cancellation, deadlines and request-scoped data. |
| go-naming | 1,255 | A naming decision flow for packages, types, functions, variables and receivers, with `scripts/check-naming.sh` catching SCREAMING_SNAKE and Get-prefixed getters. |
| go-defensive | 1,243 | API boundary hardening, defer cleanup, Must functions and time handling. |
| go-packages | 1,232 | Package organisation, imports, package size and CLI and flag patterns. |
| go-functional-options | 1,225 | The functional options pattern for constructors with optional configuration. |
| go-data-structures | 1,225 | Slices, maps and arrays: allocation with new versus make, append behaviour and copying. |
| go-control-flow | 1,223 | Idiomatic conditionals, loops, switch and break behaviour, and guard clauses. |
| go-logging | 1,060 | Structured logging with `slog`, log levels, request-scoped context and migration off older loggers. |
| go-functions | 1,038 | Function ordering, signature formatting, Printf verbs and the Stringer interface. |
| go-generics | 1,036 | When generics are worth it, constraint design, common pitfalls and type aliases. |
| go-declarations | 1,030 | Variable, const and type declarations, `var` versus `:=`, iota enums and shadowing. |

All 20 indexed listings appear in the table above; none of them falls below the threshold.

## Why This Matters for Hermes Agents

Go is the language where a confident wrong answer compiles. An agent that returns `%v` where `%w` was needed breaks the error chain silently, an agent that starts a goroutine without an owner leaks it, and an agent that reaches for an interface because it looks clean produces the opposite of the advice every Go style guide gives. Twenty small skills mapped to those decision points give the agent a place to look instead of a general instruction to write idiomatic code.

The structure is what makes it usable at runtime. Because every `SKILL.md` stays under 225 lines, loading one is cheap, and the 48 reference files only arrive when a specific situation needs them. That is the difference between a skills directory that fits in a context window and one that does not.

The eight scripts turn advice into evidence. `pre-review.sh` runs gofmt, go vet and `golangci-lint` before the review starts, `check-errors.sh` looks for bare returns and string comparison on errors, `check-docs.sh` lists exported symbols without doc comments. Each supports `--help`, `--json` for structured output, and exit codes of 0 for clean, 1 for issues and 2 for error, so an agent can branch on the result rather than parse prose.

The provenance is unusually clean for a community pack. The upstream style guides are snapshotted under `source/` with inline provenance headers, `THIRD_PARTY_NOTICES.md` records the path, project, URL, licence and copyright at repository level, and the skills are explicitly built to the agentskills.io best practices. For a profile that has to explain where its guidance came from, that trail is worth having.

## Usage

| You say | What happens |
|---|---|
| "Review this Go PR before I push" | `go-code-review` runs `scripts/pre-review.sh`, then works the checklist against the diff and reports findings in priority order. |
| "Why is this goroutine leaking" | `go-concurrency` walks the goroutine lifecycle rules, checks for a missing cancellation path, and proposes the owner and the defer. |
| "Should this be `%w` or `%v`" | `go-error-handling` applies the wrapping decision rules and points at the reference file for sentinel and logging patterns. |
| "Write table tests for this parser" | `go-testing` scaffolds the table-driven file with `scripts/gen-table-test.sh`, then fills the cases and subtests. |
| "This function is too clever, clean it up" | `go-style-core` and `go-functions` apply the nesting and signature rules, rewriting for guard clauses and readable ordering. |
| "Add a constructor with optional config" | `go-functional-options` writes the option type and the constructor signature the pattern expects. |
| "Set up golangci-lint for this repo" | `go-linting` runs `scripts/setup-lint.sh` and adds the CI step, then explains each enabled linter. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} go-code-review\n" \
  https://raw.githubusercontent.com/cxuu/golang-skills/main/skills/go-code-review/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and that the support files came along, since the reference folder is where most of the depth lives:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/go-*/ | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/go-code-review/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/go-code-review/references | wc -l
```

The count should print 20, the header should show `name: go-code-review` with its description, and the reference listing should be non-zero. If the reference folders are empty, the copy took the `SKILL.md` files without their directories.

## Security

One of the five sampled skills carries a warn: `go-interfaces` is flagged by Gen Agent Trust Hub while Socket and Snyk both pass it. The other four sampled skills are clean across all three scanners.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| go-code-review | Pass | Pass | Pass |
| go-interfaces | Warn | Pass | Pass |
| go-naming | Pass | Pass | Pass |
| go-control-flow | Pass | Pass | Pass |
| go-declarations | Pass | Pass | Pass |

The surface is markdown plus eight shell scripts. Nothing installs a package, nothing runs a postinstall hook, and nothing reaches the network: the scripts shell out to `gofmt`, `go vet`, `golangci-lint`, `strconv` benchmarks and `go test` against the local working copy. `setup-lint.sh` does write configuration and may install a linter binary, which is the one script that changes the environment rather than reading it, and the README states that destructive scripts require `--force` before overwriting an existing file.

Licensing is clear, which is not always the case in this catalogue. The repository is Apache-2.0 with a `LICENSE` file at the root, and `THIRD_PARTY_NOTICES.md` carries the upstream style guide provenance, so redistributing the skill text inside a profile is covered by the licence as long as the notices travel with it. No credentials are involved anywhere in this pack, because none of the skills talks to a hosted service.

## Limitations

- Snapshot data, verified 2026-10-31: 24,917 combined installs across 20 indexed listings; 188 GitHub stars; Apache-2.0; last pushed 2026-06-20. Counts drift over time.
- The install counts sit in a narrow band, 1,030 to 1,708, so the ordering in the table is not a quality signal. `go-code-review` leads because review is the entry point most people install first, not because it is the most useful skill.
- Seven of the eight scripts need a Go toolchain on `PATH`, and `setup-lint.sh` needs `golangci-lint` installed before it will run, so the automation is only as useful as the local Go environment. On a profile without Go installed, the skills degrade to markdown guidance.
- The README documents three install routes, for the skills CLI, Claude Code and Cursor, and none of them targets Hermes. The directory copy above is the documented layout applied by hand, not a route the repository describes.
- Go-version-sensitive guidance depends on each skill naming a minimum version and an older fallback, which the README describes as an expectation rather than a guarantee. Check the relevant SKILL.md before trusting advice about a recent standard library addition.
- The suite is versioned 1.8.0 in its plugin manifest and its changelog is the place to look for behaviour changes, since the skills are tuned over time and the install counts are a snapshot from one date.

## Related

- [Samber Go Skills - Golang Engineering Standards](/hermes/skills/catalog/samber-golang-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all twenty. The skills cross-reference each other with conditions, so a partial install leaves dangling links and the agent has to improvise the missing step.
- Run `pre-review.sh` before reading the diff yourself. It surfaces the mechanical failures first, which means the review conversation starts at design instead of formatting.
- Prefer `--json` on every script when the agent is the consumer. Structured output lets it branch on findings instead of parsing prose, and the exit codes make a clean run unambiguous.
- Read `docs/RULE_OWNERSHIP.md` before editing a skill. It records which skill owns which rule, and adding a rule to a non-owner skill is how these packs drift into contradiction.
- Keep the `references/` folders when copying. The `SKILL.md` files are deliberately thin and the depth lives one level down, so a copy that takes only the entry files halves the value of the install.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
