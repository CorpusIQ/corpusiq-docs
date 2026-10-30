---
title: "Swift Concurrency Skill - Structured Concurrency Setup"
description: "twostraws/swift-concurrency-agent-skill: 12.2K combined installs. Swift 6.2 concurrency review skill: async/await, actors, Sendable, task groups."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/swift-concurrency-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "swift", "concurrency", "ios", "code review"]
---

# Swift Concurrency Pro - Setup Guide

**Source:** [twostraws/swift-concurrency-agent-skill](https://www.skills.sh/twostraws/swift-concurrency-agent-skill) via skills.sh - 12.2K combined installs across 1 indexed listing; first seen 2026-10-30 (morning sweep)

**GitHub:** [twostraws/swift-concurrency-agent-skill](https://github.com/twostraws/swift-concurrency-agent-skill) - 578 stars, MIT License, branch main, last pushed 2026-05-17; 2 `SKILL.md` files in the tree, a plugin-root copy at `swift-concurrency-pro/SKILL.md` and a nested copy at `swift-concurrency-pro/skills/swift-concurrency-pro/SKILL.md`, beside 12 topic references in `swift-concurrency-pro/references/`, `agents/openai.yaml`, `.claude-plugin/plugin.json` and shared assets

**Category:** Swift concurrency: tasks, actors, isolation and migration

**Quality Tier:** 🟢 Verified - all sampled skills Pass on all three auditors; MIT, one skill covering Swift 6.2 concurrency review across tasks, actors, isolation and GCD migration

This is Paul Hudson's Swift concurrency skill, published from the Hacking with Swift side of the Swift ecosystem under the `twostraws` account and packaged as a single-plugin Claude Code marketplace. The repository holds one skill, `swift-concurrency-pro`, aimed at AI coding assistants that already know `async`/`await` well enough to write it and not well enough to write it safely. The targets are Swift 6.2 and iOS 26 or later, and the README states the design thesis plainly: this is not a dumping ground for all Swift concurrency advice, because skills that reteach fundamentals the model already knows burn tokens for nothing.

The structure is a thin `SKILL.md` plus twelve reference files, and the split is what makes it usable at review time. The skill body is a review process: scan for dangerous patterns, then check Swift 6.2 behaviour changes, actor isolation, structured versus unstructured tasks, cancellation, async streams and continuations, sync-to-async bridging, legacy migration, common bug patterns, strict-concurrency diagnostics, and async tests. Each step names the reference file that carries the detail, and a partial review is told to load only the relevant ones. The references cover hotspots, new features, actors, structured concurrency, unstructured tasks, cancellation, async streams, bridging, interop, bug patterns, diagnostics and testing.

The output contract is also fixed rather than left to the model. Findings are grouped by file, each one states the line, names the rule being violated and shows a before and after fix, files with no issues are skipped, and the review ends with a prioritized summary of the most impactful changes. The bundled example walks exactly that shape, an actor reentrancy bug with a force unwrap after `await` and a `Task {}` in a loop that should have been a task group.

## Installation

The README documents two routes. Claude Code installs the plugin from the repository's own marketplace:

```text
/plugin marketplace add twostraws/Swift-Concurrency-Agent-Skill
/plugin install swift-concurrency-pro@swift-concurrency-agent-skill
```

Codex, Gemini, Cursor and other hosts use the skills CLI, and the README names the skill explicitly:

```bash
npx skills add https://github.com/twostraws/swift-concurrency-agent-skill --skill swift-concurrency-pro
```

The README notes that `npx` requires Node, and gives the Homebrew fallback if it is missing:

```bash
brew install node
```

Neither `SKILL.md` carries an install block of its own, so the README is the only install source in the repository. The README also says you can clone the whole repository and install it however you want, which is the durable route for this Hermes profile: copy `swift-concurrency-pro/skills/swift-concurrency-pro/` from a clone into `~/.hermes/profiles/corpusiq/skills/swift-concurrency-pro/`. Copy the directory and not the markdown alone, because `references/` holds the twelve topic files that the skill body tells the agent to read, and a lone `SKILL.md` leaves the agent naming references it cannot open.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swift-concurrency-pro | 12,209 | Reviewing Swift concurrency code against Swift 6.2 rules: hotspot scan, actor reentrancy and isolation, structured versus unstructured tasks, cancellation, async streams and continuations, sync-to-async bridging, GCD migration, strict-concurrency diagnostics and async tests, with twelve reference files loaded on demand and findings reported per file with before and after fixes. |

No indexed listings fall below the threshold; all 1 appear above.

## Why This Matters for Hermes Agents

Concurrency is the part of Swift that agents get wrong in ways that compile. A missing `await`, an actor method that reads state, suspends and writes it back, or a `Task {}` inside a loop all pass a build and then fail under load, and a generic reviewer will not catch them because nothing looks unusual. This skill encodes the specific patterns that are dangerous, which is the only kind of concurrency review that pays for its tokens.

The reference split is the practical win. A full review loads twelve files, a partial review loads the one that matters, and the `argument-hint: "[focus area]"` in the skill frontmatter gives a caller a documented way to ask for the narrow pass. For a Hermes subagent reviewing a large package, that is the difference between spending context on actors and spending it on a testing chapter nobody asked for.

The output contract is what makes the results usable downstream. Findings arrive as file, line, rule and a before and after diff, which is close enough to a patch shape that a follow-up agent can act on it without re-deriving intent, and the prioritized summary gives a human the order to work in. The instruction to report only genuine problems and skip clean files keeps a review from turning into a wall of nitpicks.

Two rules in the skill are worth copying into any Swift prompt you write yourself. It refuses to suggest `@unchecked Sendable` as a way to silence a compiler error, on the grounds that it hides the race rather than fixing it, and it prefers structured concurrency over `Task {}` while still allowing GCD in low-level, interop and performance-critical synchronous code instead of flagging it mechanically. That second rule is the difference between a reviewer that is strict and one that is merely loud.

## Usage

| You say | What happens |
|---|---|
| "Review this Swift package for concurrency bugs" | The skill scans for the hotspot patterns first: `DispatchQueue`, `Task.detached`, `Task {}` in a loop, checked continuations, closure-based `AsyncStream`, `@unchecked Sendable`, `MainActor.run`, then walks the topic references and reports per file with line, rule and a before and after fix. |
| "The build fails with `Sending 'x' risks causing data races`" | The diagnostics reference maps that strict-concurrency error to fixes in order: check whether region-based isolation already covers it, mark the parameter `sending`, make the type `Sendable`, try `nonisolated(nonsending)`, and treat `@unchecked Sendable` as a last resort only for manually synchronized types. |
| "This actor crashes after an await" | The actor and bug-pattern references look for reentrancy, where a method reads state, suspends and writes it back, and for force unwraps on actor state after an `await`, where another caller may have set the value to nil during the suspension. |
| "Should we turn on default main-actor isolation for this app target?" | The new-features reference explains the Swift 6.2 module setting, the warning that networking still runs off the main actor because it is an external module, and the neighbouring features that change review advice: isolated conformances, `@concurrent`, `Task.immediate`, task naming and priority escalation. |
| "Help me migrate this project off GCD" | The interop reference covers the migration paths it knows: `DispatchQueue` to Swift concurrency, `Mutex` and locks, completion handlers to `async`, delegates and Combine, and it compares concurrency build settings across targets before assuming behaviour should match. |
| "Our cancellation is being ignored" | The cancellation reference traces propagation and cooperative checks through the call graph, then names the broken patterns where a child task outlives its parent or a loop never tests for cancellation. |
| "Review the async tests in this target" | The testing reference checks Swift Testing async patterns, race detection and timing-based tests that pass locally and flake in CI, and reports them against the same file and line format as production code. |

## Verification

All three raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} nested\n" \
  https://raw.githubusercontent.com/twostraws/swift-concurrency-agent-skill/main/swift-concurrency-pro/skills/swift-concurrency-pro/SKILL.md
curl -sL -o /dev/null -w "%{http_code} root\n" \
  https://raw.githubusercontent.com/twostraws/swift-concurrency-agent-skill/main/swift-concurrency-pro/SKILL.md
curl -sL -o /dev/null -w "%{http_code} hotspots\n" \
  https://raw.githubusercontent.com/twostraws/swift-concurrency-agent-skill/main/swift-concurrency-pro/references/hotspots.md
```

Expect `200` three times. Read one `SKILL.md` before installing, because the frontmatter description is the whole routing contract: it names the trigger, reviewing Swift concurrency code, and the review scope the model should expect.

After a copy lands in the profile, confirm the skill file and the reference directory both arrived:

```bash
head -8 ~/.hermes/profiles/corpusiq/skills/swift-concurrency-pro/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/swift-concurrency-pro/references/
```

A good copy shows `name`, `description`, `license: MIT` and the author metadata in the frontmatter, and the listing shows twelve markdown files from `actors.md` through `unstructured.md`. If `references/` is missing or short, the copy took a single `SKILL.md` instead of the full skill directory.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swift-concurrency-pro | Pass | Pass | Pass |

No FAIL or Warn verdict appears in the sampled set. The surface here is small and static: the repository ships markdown, an SVG and PNG icon pair, `agents/openai.yaml`, a plugin manifest and marketplace manifest, and no bundled scripts, no hooks, no MCP server and no credential handling. Nothing in the skill reaches the network or executes code on its own, and the only install-time action is a directory copy or a plugin install.

The real risk is the review itself rather than the package. The skill instructs the agent to rewrite Swift code, and some of its advice changes program structure: moving a loop to a task group, replacing `Task.detached`, removing a `@unchecked Sendable` conformance, marking a parameter `sending`. Read the diff before you accept it, and keep the repository under version control while an agent works through a concurrency migration, because a compile-clean concurrency rewrite can still change scheduling behaviour in ways tests only reveal later.

## Limitations

- Snapshot data, verified 2026-10-30: 12,209 combined installs across 1 indexed listing; 578 GitHub stars; MIT License; last pushed 2026-05-17. Counts drift over time.
- The index and the tree count differently. skills.sh indexes one listing, `swift-concurrency-pro`, while the checkout holds two `SKILL.md` files for that same skill: a plugin-root copy at `swift-concurrency-pro/SKILL.md` and a nested copy at `swift-concurrency-pro/skills/swift-concurrency-pro/SKILL.md`. They are not byte identical: the nested copy carries an `argument-hint` frontmatter field and prefixes reference paths with `${CLAUDE_SKILL_DIR}`, the root copy does not and uses repository-relative paths.
- The advice is pinned to Swift 6.2 and iOS 26 or later, and the skill body tells the reviewer to target Swift 6.2 with strict concurrency checking. On an older toolchain, parts of the new-features reference describe features the compiler does not have, and default main-actor isolation is a build setting that has to be enabled before that guidance applies to a target.
- `${CLAUDE_SKILL_DIR}` is substituted by Claude Code. A host that does not implement it will show the agent a literal variable in every reference path, so either resolve those paths yourself or take the root `SKILL.md`, whose paths are relative to the repository.
- Nothing in this repository compiles, runs or tests Swift. The skill is review guidance with a fixed output shape, so a clean report is not proof of correctness: the claim still needs a real build with strict concurrency checking and a test run that exercises the concurrent paths.
- Installation lives only in the README. No `SKILL.md` carries an install block, the `npx skills add` route needs Node, and the fallback instructions are Homebrew commands that assume macOS.

## Related

- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [SwiftUI Agent Skill - Apple UI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the whole `swift-concurrency-pro` directory. The twelve files in `references/` are the substance of the skill, and the body only points at them; without them the agent invents the rules it was told to look up.
- Ask for the partial review with a focus area. The frontmatter `argument-hint` accepts one, and a narrow scope such as actors or cancellation loads one reference instead of twelve.
- Paste compiler diagnostics verbatim. The diagnostics reference is keyed on the real error strings such as "Sending value risks causing data races", so a paraphrased error misses the mapping it was written for.
- Keep the "report only genuine problems" instruction when you wrap this in a subagent prompt. Dropping it is the fastest way to get a review full of style opinions that the skill exists to avoid.
- Pair it with a testing pass before a migration. The review reads code, the testing reference tells you what to check, and neither replaces a build plus a test run under strict concurrency.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
