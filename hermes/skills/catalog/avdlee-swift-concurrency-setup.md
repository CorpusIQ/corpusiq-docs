---
title: "Swift Concurrency Agent Skill - Swift 6 Setup"
description: "avdlee/swift-concurrency-agent-skill on skills.sh: 17.4K combined installs from 1 listing; Swift 6 migration, actors and data-race triage for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/avdlee-swift-concurrency-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "swift", "swift 6", "concurrency"]
---

# Swift Concurrency Agent Skill - Setup Guide

**Source:** [avdlee/swift-concurrency-agent-skill](https://www.skills.sh/avdlee/swift-concurrency-agent-skill) via skills.sh - 17.4K combined installs across 1 indexed listing; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 1,702 stars, MIT licence, last pushed 2026-09-14, 1 SKILL.md directory at skills/swift-concurrency with a references/ folder of 15 topic files plus an index
**Category:** Swift concurrency guidance for coding agents: isolation, Sendable, actors, task cancellation, performance tuning and Swift 6 migration
**Quality Tier:** 🟢 Production - all three audits Pass; MIT; 1,702 stars.

This is one skill, not a suite. It packages the reasoning from Antoine van der Lee's Swift Concurrency Course into a triage playbook plus a set of topical references, and it is distributed as a portable Agent Plugin (spec 1.0.0) with a root `plugin.json` manifest and a `skills/` directory, alongside client manifests for Claude Code, Cursor, Codex and pi.

The install count is the interesting part of the record: 17,351 installs from a single indexed listing, which puts it in the same range as catalogues ten times its size. One well-scoped skill that answers a hard compiler error travels further than twenty that answer easy ones.

## Installation

The README's recommended path uses the skills CLI:

```bash
npx skills@latest add https://github.com/avdlee/swift-concurrency-agent-skill --skill swift-concurrency
```

If the skill was installed before the Agent Plugins migration, the README says to run `npx skills@latest update` with CLI 1.5.24 or newer, which moves the saved skill path instead of treating the skill as deleted.

Claude Code users can install it as a plugin instead. Personal use takes two commands:

```bash
/plugin marketplace add AvdLee/Swift-Concurrency-Agent-Skill
/plugin install swift-concurrency@swift-concurrency-agent-skill
```

For a shared repository, the README configures it through `.claude/settings.json` by enabling `swift-concurrency@swift-concurrency-agent-skill` and adding the GitHub repo as an extra known marketplace, so teammates get an install prompt when they open the project.

ChatGPT and Codex users install from the OpenAI Plugins Directory by searching for "Swift Concurrency" in the plugin browser. Cursor loads it from a local clone placed in `~/.cursor/plugins/local`, or from the Cursor Marketplace once listed. Other clients, including pi, Gemini CLI and Autohand Code, are covered in the repo's `INSTALLATION.md`.

## What It Provides

One listing, above the threshold on its own.

| Skill | Installs | Use For |
|---|---|---|
| swift-concurrency | 17,351 | Diagnosing isolation errors and data races, refactoring callbacks to async/await, choosing actors or @MainActor, Sendable conformance, performance tuning and Swift 6 migration |

All 1 indexed listings clear the threshold and appear in the table above.

## Why This Matters for Hermes Agents

Concurrency bugs are where a confident agent does the most damage. The compiler message names a symbol and an isolation boundary, the plausible-sounding fix is to wrap the call site in `@MainActor`, and that fix is wrong often enough to be a real cost.

This skill fights that pattern directly. Its Fast Path opens by requiring the agent to read `Package.swift` or the `.pbxproj` for language mode, strict concurrency level, default isolation and upcoming features before proposing anything, and it says to do that always, not only for migration work.

The guardrails are unusually explicit for a skill file: no blanket `@MainActor`, structured concurrency before unstructured tasks, `Task.detached` only with a stated reason, and any `@unchecked Sendable` or `nonisolated(unsafe)` needs a documented invariant and a removal plan. Those are the exact escape hatches an agent reaches for when it wants the error to go away.

Progressive disclosure is the other design worth copying. The SKILL.md carries the triage logic and a reference index, and the depth sits in 15 topic files covering actors, sendable, tasks, async sequences, migration, testing, core-data, memory management and linting, so context is spent on the topic the error actually belongs to.

For any team mid-migration to Swift 6, that combination is close to the highest-leverage skill you can install: the work is repetitive, the failure mode is silent until runtime, and the correct answer changes with the project's build settings.

## Usage

| You say | What happens |
|---|---|
| "Why is this actor-isolated property access an error?" | The skill reads the project settings, names the isolation boundary and walks to the matching reference file |
| "Refactor this completion-handler API to async/await" | It rewrites the callback path to async/await and keeps the smallest safe change rather than restructuring the module |
| "We are moving this target to Swift 6" | It reads the build settings, enables strict concurrency incrementally and produces a migration order |
| "This test is flaky when it touches the main actor" | It applies the testing reference, including the main serial executor pattern for deterministic runs |
| "Should this be a custom actor or @MainActor?" | It justifies the choice from whether the code is genuinely UI-bound, and refuses the blanket answer |
| "Core Data objects are crossing an isolation boundary" | It switches to `NSManagedObjectID` handoff and the data access object pattern in the core-data reference |
| "This loop is slow under load" | It moves to the performance reference for actor contention, suspension points and parallel versus serial execution |

## Verification

Fetch the skill file and confirm the frontmatter and the Fast Path section are present:

```bash
curl -fsSL https://raw.githubusercontent.com/avdlee/swift-concurrency-agent-skill/main/skills/swift-concurrency/SKILL.md | head -30
```

That URL returned 200 on 2026-11-04, and the reference index returns 200 at `skills/swift-concurrency/references/_index.md`. A local clone should show `SKILL.md` plus the `references/`, `agents/` and `assets/` directories.

Then confirm the skill is registered. On the skills CLI path, check the agent's skills directory for a `swift-concurrency` folder. On the Claude Code plugin path, `/plugin` lists the installed plugins and `swift-concurrency@swift-concurrency-agent-skill` should appear there.

The README's own acceptance test is behavioural: ask the agent to use the skill on a project and it should open the triage playbook and jump to the reference file that matches your error or task.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swift-concurrency | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 17,351 combined installs across 1 indexed listing; 1,702 GitHub stars; MIT licence; last pushed 2026-09-14. Counts drift over time.
- One indexed listing matches the single SKILL.md directory in the tree, so there is no breadth signal here. The install number reflects one skill's reach, not a catalogue's.
- Every claim in the skill is Swift and Apple-platform specific. The advice assumes Xcode or SwiftPM build settings and does not translate to other languages' concurrency models.
- The skill is distilled from a paid course and says so. Where the references stop, the course is the intended next step, which is a documentation trail rather than a support commitment.
- The SKILL.md itself warns that Xcode 26 project defaults should be treated as likely rather than confirmed. It asks the agent to verify settings instead of assuming them, so expect a question before migration advice.
- Installation is client-specific: skills CLI, Claude Code plugin, Cursor local clone and the OpenAI Plugins Directory each have their own path, and the slash commands in the README apply to Claude Code only.

## Related

- [Swift Concurrency Skill - Structured Concurrency Setup](/hermes/skills/catalog/swift-concurrency-skill-setup)
- [SwiftUI Agent Skill - Apple UI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let the skill read the build settings first. Guidance given without knowing the language mode and default isolation is the main source of bad concurrency advice.
- Ask for the diagnostic, not a description of the bug. The Fast Path keys off the exact compiler or linter message and the offending symbol.
- Keep migration changes small and separate. The skill's own guardrail is to avoid refactoring unrelated architecture mid-migration, and a large diff hides the isolation change that mattered.
- Use `npx skills@latest update` on skills CLI 1.5.24 or newer if an older install reports the skill as deleted. The migration renames the saved path rather than removing the skill.
- Send the agent to one reference file at a time. Fifteen topic files loaded at once costs more context than the error usually deserves.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
