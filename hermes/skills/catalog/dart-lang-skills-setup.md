---
title: "Dart Language Skills Setup Guide for Hermes Agents"
description: "dart-lang/skills - 144.0K installs across 30 skills, official Dart org: the Dart team's first-party agent skills for testing, static analysis, package conflicts, FFI, CLI apps, and idiomatic Dart and Flutter development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dart-lang-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "dart", "flutter", "testing", "static analysis", "ffi"]
---

# Dart Language Skills - Setup Guide

**Source:** [dart-lang/skills](https://skills.sh/dart-lang/skills) (144.0K installs across 30 skills)
**GitHub:** [dart-lang/skills](https://github.com/dart-lang/skills) (463 stars)
**Skills:** 30 skills; top skills: `dart-add-unit-test` (14.0K), `dart-run-static-analysis` (13.9K), `dart-fix-runtime-errors` (13.8K)
**Category:** Development / Dart & Flutter
**First Seen:** skills.sh Apr 24, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟢 Production - first-party publisher (official `dart-lang` org, the Dart/Flutter team at Google) and all three skills.sh security audits Pass (see Security Audit Status)

The official Dart language team publishes a 30-skill agent suite covering the full Dart and Flutter development lifecycle: unit and integration testing, static analysis, runtime error fixing, package conflict resolution, pattern matching, code coverage, test mocks, the `checks` package migration, CLI app scaffolding, and native FFI interop. Each skill is a focused procedural guide an agent loads for one task class - the same pattern Hermes skills use.

The suite splits into a heavily installed workflow core (`dart-add-unit-test`, `dart-run-static-analysis`, `dart-fix-runtime-errors`, `dart-resolve-package-conflicts`, `dart-use-pattern-matching`, `dart-collect-coverage`) and a longer reference tail (effective style, language syntax, async programming, isolates, web development, compilation and deployment) that covers idiomatic Dart end to end.

---

## Installation

```bash
npx skills add dart-lang/skills
```

Or per-skill from the repo:

```bash
npx skills add https://github.com/dart-lang/skills --skill dart-add-unit-test
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Dart SDK** | `dart` 3.x on PATH for analysis, test, and pub commands |
| **Flutter SDK** | Optional; required for Flutter-specific workflows |
| **Node.js** | Recent LTS for the `npx skills` installer |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| dart-add-unit-test | 14.0K | Structuring and writing tests with `package:test`; mirrors `lib` structure in `test/` |
| dart-run-static-analysis | 13.9K | Running `dart analyze`, interpreting lints, and fixing analyzer findings |
| dart-fix-runtime-errors | 13.8K | Diagnosing and fixing crashes, exceptions, and runtime failures |
| dart-resolve-package-conflicts | 13.7K | Dependency resolution failures, version conflicts in `pubspec.yaml` |
| dart-use-pattern-matching | 13.6K | Applying Dart 3 pattern matching, switch expressions, and destructuring |
| dart-collect-coverage | 13.5K | `dart test --coverage` collection and coverage report workflows |
| dart-generate-test-mocks | 13.4K | Test doubles and mocking for Dart tests |
| dart-migrate-to-checks-package | 13.2K | Migrating assertions to the `checks` testing package |
| dart-build-cli-app | 13.1K | Scaffolding and structuring Dart command-line applications |
| dart-use-ffigen | 7.4K | Generating Dart FFI bindings from C headers with `ffigen` |

Plus `dart-setup-ffi-assets`, `dart-use-primary-constructors`, `dart-write-documentation`, and a reference tail covering effective style, language syntax, code generation, async programming, API design, native interop, isolates, web development, and deployment.

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| dart-add-unit-test | Pass | Pass | Pass |

All three audits Pass - the basis for the 🟢 Production tier.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent-built Dart tooling** | CorpusIQ agents that scaffold Dart CLIs or Flutter tooling load the workflow-core skills instead of guessing at `pub` and `analyze` commands |
| **MCP server maintenance** | Dart-based MCP servers get correct test structuring, coverage, and static-analysis fixes from first-party guidance |
| **FFI interop work** | `dart-use-ffigen` + `dart-setup-ffi-assets` cover binding generation for native integrations |
| **Idiomatic review reference** | The reference tail (effective style, API design, idiomatic usage) is the Dart team's own standard - useful for reviewing agent-written Dart |

## Limitations / Verification

- The suite is Dart/Flutter-specific; it does not cover other languages. For low-level C/C++/Rust/Zig work see the [Low-Level Dev Skills](/hermes/skills/catalog/low-level-dev-skills-setup) guide.
- The long reference tail has small per-skill install counts (60-1.1K); the workflow core above 13K is where most adoption sits.
- 463 GitHub stars is modest for an official org repo; first-party status and clean audits carry the tier rather than star count.

Verification after install:

```bash
dart --version                                  # Dart SDK present
npx skills add dart-lang/skills --list          # 30 skills discovered
```

## Related

- [Low-Level Dev Skills Setup](/hermes/skills/catalog/low-level-dev-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
