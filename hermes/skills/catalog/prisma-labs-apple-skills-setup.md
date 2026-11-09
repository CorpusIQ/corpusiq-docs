---
title: "Prisma Labs Apple Skills - iOS 26 and SwiftUI Setup"
description: "prisma-labs-dev/apple-skills on skills.sh: 13.4K combined installs; 34 Apple skills for SwiftUI, Liquid Glass, SwiftData and HIG lookups."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/prisma-labs-apple-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "apple", "ios", "swiftui", "liquid glass"]
---

# Prisma Labs Apple Skills - Setup Guide

**Source:** [prisma-labs-dev/apple-skills](https://www.skills.sh/prisma-labs-dev/apple-skills) via skills.sh - 13.4K combined installs across 20 indexed listings; snapshot 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 357 stars, MIT via LICENSE, `main` branch, last pushed 2026-09-26, 34 SKILL.md files in a 412-file tree, split across `skills/` (29 directories) and `disabled-skills/` (5 directories)
**Category:** Apple platform engineering: iOS 26 APIs, SwiftUI, UIKit, Liquid Glass, HealthKit, StoreKit, XCTest and App Store metadata
**Quality Tier:** 🟡 Yellow - derived from sampled scanner warnings: one Gen Agent Trust Hub Warn and four Snyk Warns across 20 sampled skills, with an MIT license and no Fail verdict.

Prisma Labs publishes apple-skills as a suite rather than a single skill: 29 skill directories under `skills/`, five more parked in `disabled-skills/`, and a README that sorts them into framework reference docs, a coordinator, design and guideline skills, six workflow guides, and two utilities. The split matters more than the count. The reference docs (`swiftui`, `uikit`, `healthkit`, `storekit`, `widgetkit` and the rest) document what APIs exist and are meant to be queried for a symbol or modifier. The workflow guides teach how to approach a task, and all six are vendored from other authors' repositories, named in the README's Origin column: three from `twostraws`, one from `AvdLee`, two from `Dimillian`.

The suite targets iOS 26 and Swift 6 and says so in the README: `@Observable` rather than `ObservableObject`, `NavigationStack` rather than `NavigationView`, async/await rather than completion handlers, Swift Testing where applicable. No legacy patterns ship. The stated reason is that models already carry old Apple APIs in training data, so the skills spend their budget on the APIs a model is most likely to get wrong.

Adoption looks like suite-level installs rather than per-skill discovery. 13,416 installs spread over 20 listings, with the top skill at 983 and the bottom at 536, is a flat distribution, and the README's Codex and Cursor commands install with `--skill '*'`. Against 357 stars, the install count is the skills CLI and the Claude Code marketplace doing the work, not GitHub traffic.

## Installation

The README gives one block per agent. Claude Code goes through the plugin marketplace:

```bash
claude plugin marketplace add Prisma-Labs-Dev/apple-skills
claude plugin install apple-skills@apple-skills
```

Codex and Cursor go through the skills CLI, with the whole suite selected:

```bash
npx skills add Prisma-Labs-Dev/apple-skills --agent codex --skill '*' -g -y
npx skills add Prisma-Labs-Dev/apple-skills --agent cursor --skill '*' -g -y
```

For a single skill through the skills CLI, the indexed install line names the skill:

```bash
npx skills add https://github.com/prisma-labs-dev/apple-skills --skill hig
```

Updates follow the install route. Marketplace installs update through the plugin command, and the CLI route is a re-run of the install command:

```bash
claude plugin update apple-skills@apple-skills
```

Removal is symmetric:

```bash
claude plugin uninstall apple-skills@apple-skills
npx skills remove -g
```

Two details are worth knowing before choosing a route. The marketplace entry in `.claude-plugin/marketplace.json` declares `source: "./"` and version `1.0.20`, so the plugin resolves to the repository root and ships the working tree as it stands, including `scripts/` and `tests/`. And the repository's own tooling needs Node 25.2.0 or newer (`"engines": {"node": ">=25.2.0"}` in `package.json`), which matters only if you intend to run the doc refresh scripts, not the skills.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear:

| Skill | Installs | Use For |
|---|---|---|
| hig | 983 | Fact lookup from a local, greppable Human Interface Guidelines corpus: hit-target sizes, Dynamic Type behaviour, contrast, platform terminology, component capabilities and the conventions App Review checks. Not design direction |
| ios-liquid-glass | 885 | Liquid Glass API reference for iOS 26 and later: glass effects, GlassEffect modifiers, navigation patterns and the design principles behind them |
| apple-docs-index | 849 | Index of Apple developer documentation for iOS and macOS: what APIs exist in a framework, which doc page to fetch, covering SwiftUI, UIKit, QuartzCore, XCTest, HealthKit, Combine and SwiftData |
| healthkit | 785 | HealthKit API reference: HKHealthStore, HKQuantitySample, workouts, and health data read and write |
| ios-dev | 779 | Coordinator to start with on any iOS or SwiftUI task: routes to the best-practice guides, correctness checks and API references used for building, reviewing, refactoring and debugging an app |
| xcuitest | 759 | XCUITest API reference: element queries, waiting patterns, Swift 6 @MainActor, assertions, screenshots and launch arguments |
| swiftui | 755 | SwiftUI API reference: views, layouts, navigation, @State and @Binding, @Observable, view modifiers, NavigationStack and iOS 26 additions |
| swift-concurrency | 721 | Swift Concurrency API reference: async and await, Task, TaskGroup, actors, AsyncSequence, AsyncStream and continuations |
| swift-testing | 715 | Swift Testing API reference: @Test, @Suite, #expect, #require, traits, parameterized tests and migration from XCTest |
| combine | 690 | Combine API reference: publishers, subscribers, operators and async data streams |
| corehaptics | 578 | Core Haptics API reference: CHHapticEngine, haptic patterns and tactile feedback |
| storekit | 568 | StoreKit 2 API reference: Product, Transaction, subscriptions, StoreView and SubscriptionStoreView |
| usernotifications | 552 | UserNotifications API reference: local and remote notifications, triggers and notification content |
| guide-swiftui-performance-audit | 550 | Audit and fix SwiftUI runtime performance from code review and architecture: slow rendering, janky scrolling, high CPU or memory use, excessive view updates and layout thrash, plus what to profile in Instruments when reading the code is not enough |
| apple-aso | 546 | App Store Optimization for the metadata in store.config.json: keywords, titles, subtitles, descriptions and localized variants |
| backgroundtasks | 544 | BackgroundTasks API reference: BGTaskScheduler, app refresh and background processing |
| photosui | 543 | PhotosUI API reference: PhotosPicker, PHLivePhotoView and photo selection |
| swiftdata | 541 | SwiftData API reference: @Model, ModelContext, @Query and schema migrations |
| guide-macos-spm-packaging | 537 | Scaffold, build and package a SwiftPM macOS app without an Xcode project: target and resource layout, a custom .app bundle assembly script, signing, notarization and appcast steps |
| widgetkit | 536 | WidgetKit API reference: widget timelines, entries, providers, and home and lock screen widgets |

No indexed listings fall below the threshold, so all 20 appear above.

The depth is uneven by design. `skills/hig/` holds 51 files: `SKILL.md` plus a greppable copy of the guidelines, one markdown file per topic and `.videos.md` companions that point at WWDC sessions. `skills/swiftui/` holds 51 files, one per view or modifier such as `alert.md`, `asyncimage.md` and `binding.md`. `skills/ios-dev/` is a single file, because it is a router and nothing else.

The five disabled directories are the most interesting part of the repository. `ios-ui-craft`, `ios-design-consultant`, `guide-swiftui-view-refactor`, `guide-swiftui-animations` and `guide-swiftui-ui-patterns` are kept but not loaded, and the README explains why: they impose a taste or architecture (aesthetic manifestos, an MV-over-MVVM mandate, "Apple-approved" design framing) and the maintainer's position is that the model should form its own design judgment from the reference docs. Re-enabling one is a directory move back into `skills/`. The README's disabled table names only three of the five; the two animation and UI-pattern guides are undocumented there.

The `hig` skill is also the clearest example of how these files are meant to be read. Its frontmatter carries `context: fork`, `agent: Explore` and `user-invocable: true`, so it runs in a forked explore subagent against local markdown rather than in the main thread, and its body opens by stating that visual design is the designing model's own taste and the HIG is a source for facts only.

## Why This Matters for Hermes Agents

Apple platform work is where a general model is most confidently wrong, because the API surface moves every year and the training data does not. The failure is specific: an agent writes `NavigationView` and `.onAppear` in a new SwiftUI screen, uses `ObservableObject`, or invents a Liquid Glass modifier that does not exist. Every one of those is a plausible completion, and none of them compiles against the iOS 26 SDK in the way the skill describes.

The second fit is retrieval shape. A 51-file reference tree per framework is not something to load whole. The coordinator pattern solves that: `ios-dev` decides which reference applies, `apple-docs-index` locates the page, and the specific skill answers the symbol question. That is the same route an agent takes through Hermes' own skill index, so the behaviour composes.

The third is that the HIG skill is deliberately narrow. Accessibility minimums, Dynamic Type behaviour, terminology and App Review conventions are facts with a right answer, and they are the part of Apple guidance that an agent cannot reason its way to. Design taste is left to the model, which is a defensible line and an unusual one for a published skill suite.

One caveat on fit: these skills were written for Claude Code and Codex, and the `context: fork` and `agent: Explore` fields in the HIG frontmatter are client-specific. A Hermes agent will read the same markdown and ignore those fields, so the fork isolation is lost and the 51-file corpus is only as scoped as the agent's own tooling makes it.

## Usage

| You say | What happens |
|---|---|
| "Build a settings screen with a glass toolbar in this iOS app" | Routes through `ios-dev`, pulls `ios-liquid-glass` for the GlassEffect modifiers and navigation patterns, and `swiftui` for the view and modifier surface, on the iOS 26 baseline |
| "What is the minimum hit target for a toolbar button" | Answers from the local HIG corpus: 44pt, with the Dynamic Type and contrast rules that sit beside it, and cites the guideline file it read |
| "This list scrolls at 30fps and the profiler shows view churn" | Runs `guide-swiftui-performance-audit`: reads the view structure for identity and state problems, then names the Instruments template and trace to capture if the code review is inconclusive |
| "Which framework do I use for a lock screen widget" | Uses `apple-docs-index` to place WidgetKit, then `widgetkit` for timelines, entries and the supported widget families |
| "Write tests for this view model with the new testing library" | Uses `swift-testing` for `@Test`, `@Suite`, `#expect` and parameterized cases, and `guide-swift-testing` for the patterns that replace XCTest habits |
| "Set up a macOS app without opening Xcode" | Runs `guide-macos-spm-packaging`: package layout, resources, the bundle assembly script, then signing, notarization and appcast steps |
| "Our App Store subtitle is not converting" | Uses `apple-aso` against `store.config.json`: keyword and subtitle edits, with the localization pass kept to the same file |
| "Why is the HIG telling me to use a specific font" | Answers that it does not: the `hig` skill is a fact lookup, and the disabled design skills that mandated fonts stay disabled |

## Verification

Every skill lives at `skills/<name>/SKILL.md` on `main`, and the disabled ones at `disabled-skills/<name>/SKILL.md`. Both shapes return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/prisma-labs-dev/apple-skills/main/skills/hig/SKILL.md | head -10
curl -fsSL https://raw.githubusercontent.com/prisma-labs-dev/apple-skills/main/skills/ios-dev/SKILL.md | head -6
```

The HIG file should open with frontmatter holding `name: hig`, `user-invocable: true`, a `description` that starts `Fact lookup: Apple Human Interface Guidelines corpus`, plus `context: fork` and `agent: Explore`. Below the closing delimiter the first heading is `# Human Interface Guidelines Reference`. The coordinator file should open with `name: ios-dev` and a body that opens by telling the reader to start there for any iOS or SwiftUI task.

The skill count is checkable against the tree, and it is the fastest way to spot a restructure:

```bash
curl -fsSL "https://api.github.com/repos/prisma-labs-dev/apple-skills/git/trees/main?recursive=1" | grep -c 'SKILL.md'
```

That prints 34, of which 29 sit under `skills/` and five under `disabled-skills/`. If the number moves, the suite has gained or lost a skill and the install index will lag behind it.

Promoting a disabled skill is a two step check, because the file exists in the repository whether or not the agent loads it:

```bash
curl -fsSL https://raw.githubusercontent.com/prisma-labs-dev/apple-skills/main/disabled-skills/ios-ui-craft/SKILL.md | head -4
```

A disabled file returns 200 and still carries a valid `name` and `description`; the only thing that distinguishes it is its directory. After a plugin install, confirm the client is reading the enabled set and not the parked one, by checking that a name under `disabled-skills/` does not appear in the agent's skill list.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hig | Pass | Pass | Pass |
| ios-liquid-glass | Pass | Pass | Pass |
| apple-docs-index | Pass | Pass | Pass |
| healthkit | Pass | Pass | Pass |
| ios-dev | Pass | Pass | Pass |
| xcuitest | Pass | Pass | Warn |
| swiftui | Pass | Pass | Warn |
| swift-concurrency | Warn | Pass | Warn |
| swift-testing | Pass | Pass | Pass |
| combine | Pass | Pass | Pass |
| corehaptics | Pass | Pass | Pass |
| storekit | Pass | Pass | Warn |
| usernotifications | Pass | Pass | Pass |
| guide-swiftui-performance-audit | Pass | Pass | Pass |
| apple-aso | Pass | Pass | Pass |
| backgroundtasks | Pass | Pass | Pass |
| photosui | Pass | Pass | Pass |
| swiftdata | Pass | Pass | Pass |
| guide-macos-spm-packaging | Pass | Pass | Pass |
| widgetkit | Pass | Pass | Pass |

No skill in the sample carries a Fail. The five Warn cells are Snyk flags on `xcuitest`, `swiftui`, `swift-concurrency` and `storekit`, and a Gen Agent Trust Hub Warn on `swift-concurrency` alone. In practice that means one scanner reported something it wanted a human to look at on four of the twenty skills, and nothing in the sample was blocked. Read the individual skills.sh page for `swift-concurrency` before installing that one, since it is the only skill flagged by two scanners.

What the skills themselves execute is nothing. Each `SKILL.md` is markdown plus sibling markdown reference files; there is no installer hook, no shell script invoked on load, and no network call from the skill body. The HIG and framework references are committed markdown, fetched by the maintainer's tooling, not by your agent.

The repository around them is not inert, and the plugin route pulls the whole thing. `package.json` declares Node 25.2.0 or newer, a `scripts/apple-docs.ts` fetcher, Biome and vitest as dev dependencies, and a set of `pnpm` scripts for refreshing docs, typechecking, linting and testing. There is no `postinstall` entry, so nothing runs on install, but `source: "./"` in the marketplace manifest means those files land on disk and are available to anything that later decides to run a package script.

The content risk is the one that matters for an agent. These skills feed Apple documentation into context as authoritative reference, and a doc refresh pulls new markdown from Apple into `skills/`. If you pin the suite by commit, you pin the docs with it; if you track `main`, the reference text changes underneath your agent without a version bump.

## Limitations

- Snapshot data, verified 2026-11-09: 13,416 combined installs across 20 indexed listings; 357 GitHub stars; MIT license; last pushed 2026-09-26. Counts drift over time.
- 20 is also the skills.sh source page cap, so the index cannot show more listings than that even if the repository grows. Treat 20 as the visible ceiling, not as the suite's size.
- The index is behind the tree: the repository holds 34 SKILL.md files, and nine enabled skills carry no listing at all (`uikit`, `mapkit`, `tipkit`, `eventkit`, `core-animation`, `guide-swift-concurrency`, `guide-swift-testing`, `guide-swiftdata`, `guide-swiftui-charts`). Their absence from the install table says nothing about their quality.
- The disabled set is documented in one place and enforced in another: five directories sit in `disabled-skills/`, while the README's table explains only three of them. `guide-swiftui-animations` and `guide-swiftui-ui-patterns` are undocumented there.
- All six workflow guides are vendored from other repositories (`twostraws` for concurrency, testing and SwiftData, `AvdLee` for charts, `Dimillian` for the performance audit and SPM packaging). Upstream fixes arrive only when the maintainer re-copies them, and the copies can drift.
- The suite deliberately targets iOS 26 and Swift 6 with no legacy patterns, which makes it a poor fit for a project that must build against an older deployment target. The README's answer is that the agent can add backward compatibility itself, which is a reasonable position and still your code review's problem.
- The HIG skill's `context: fork` and `agent: Explore` frontmatter is Claude Code specific. Clients that ignore those fields get the same facts without the isolated subagent.

## Related

- [Dimillian Skills - Apple Platform Engineering Suite Setup](/hermes/skills/catalog/dimillian-skills-setup)
- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [SwiftUI Agent Skill - Apple UI Development Setup](/hermes/skills/catalog/avdlee-swiftui-agent-skill-setup)
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start at `ios-dev` and let it route. Jumping straight to `swiftui` on a task that is really about data or testing is how you get a view layer written against the wrong model.
- Load `hig` for the numbers, not for the look. It answers 44pt targets, Dynamic Type and App Review conventions, and it explicitly refuses to be a design authority; the five parked design skills are parked for that reason.
- When a framework question is vague ("what can I use for X"), go through `apple-docs-index` first. It exists to tell you which doc page to fetch, and fetching a top-level page instead of a symbol page is the usual cause of sparse answers.
- For a performance complaint, take `guide-swiftui-performance-audit` before touching the code. It separates view identity and update problems from layout thrash, and it names the Instruments run to capture, so a code review alone does not become guesswork.
- If you install the plugin rather than a single skill, you get all 29 enabled skills and the repository tooling. If you only need reference lookups, the single-skill CLI line keeps the surface small and keeps the Node 25 toolchain off your machine.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
