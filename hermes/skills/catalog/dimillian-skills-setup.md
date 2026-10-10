---
title: "Dimillian Skills - Apple Platform Engineering Suite Setup"
description: "Setup guide for dimillian/skills - 33.8K combined installs. SwiftUI, iOS, and Apple platform engineering skills from Thomas Ricouard."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dimillian-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "swiftui", "apple platforms", "ios development"]
---

# Dimillian Skills - Setup Guide

**Source:** [dimillian/skills](https://www.skills.sh/dimillian/skills) via skills.sh - 33.8K combined installs across 18 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [dimillian/skills](https://github.com/dimillian/skills) (3,989 stars, MIT; pushed 2026-03-29; skill dirs at the repo root, `swiftui-performance-audit/SKILL.md` style)
**Category:** Apple Platform / SwiftUI / iOS
**Quality Tier:** 🟡 Beta - Dimillian (Thomas Ricouard), 3,989 stars, MIT; last pushed Mar 2026; all sampled verdicts Pass

Dimillian Skills is the public skill collection from Thomas Ricouard (dimillian): sixteen self-contained skills for Apple platform engineering, plus supporting workflow skills for GitHub operations, diff review swarms, bug investigation swarms, refactoring, and skill curation. Its strongest entries target SwiftUI: runtime performance auditing, iOS 26 Liquid Glass adoption, UI patterns, view refactoring, and Swift 6.2 concurrency.

Each skill is a self-contained folder at the repo root with its own `SKILL.md` carrying triggers, workflow guidance, examples, and references. The README's install method places the skill folders under `$CODEX_HOME/skills`; skills.sh also indexes the same folders for registry-based installs. A practical starting point: pair swiftui-performance-audit with swiftui-ui-patterns on an existing app, then run the review and bug swarms before merging changes.

---

## Installation

```bash
# Browse the collection
npx skills add dimillian/skills --list

# Install the full collection globally
npx skills add dimillian/skills -g --all

# Or install individual skills
npx skills add dimillian/skills -g --skill swiftui-performance-audit
```

The README's manual method for Codex: copy the skill folders you want from the repo into `$CODEX_HOME/skills`. Every skill is self-contained, so folders can be copied individually with no cross-skill dependencies.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swiftui-performance-audit | 9,505 | Auditing SwiftUI runtime performance: invalidation storms, identity churn, layout thrash, heavy render work |
| swiftui-liquid-glass | 5,060 | Implementing and reviewing iOS 26+ Liquid Glass APIs with correct modifier ordering, grouping, and fallbacks |
| swiftui-ui-patterns | 3,439 | Best-practice SwiftUI screens and components: navigation, sheets, app wiring, async state |
| ios-debugger-agent | 2,705 | Building, launching, and debugging iOS apps on a booted simulator with UI inspection, screenshots, and log capture |
| swiftui-view-refactor | 2,226 | Refactoring SwiftUI views toward smaller subviews and stable view trees with explicit dependency injection |
| swift-concurrency-expert | 1,897 | Fixing Swift 6.2+ concurrency issues: actor isolation, Sendable violations, main-actor annotations |
| macos-spm-app-packaging | 1,339 | Scaffolding, building, signing, and notarizing SwiftPM-based macOS apps without an Xcode project |
| app-store-changelog | 1,308 | Turning git history into user-facing App Store release notes |
| react-component-performance | 1,029 | Diagnosing slow React components: re-render churn, unstable props, list bottlenecks |
| github | 846 | Operating on GitHub through the gh CLI: issues, PRs, workflow runs, run logs, advanced queries |
| project-skill-audit | 755 | Auditing a project to recommend the highest-value new skills or skill updates |
| review-and-simplify-changes | 751 | Reviewing diffs for reuse, quality, efficiency, and clarity, then applying safe fixes |
| review-swarm | 718 | Running a read-only four-agent diff review for regressions, security, and coverage gaps |
| bug-hunt-swarm | 684 | Running a read-only four-agent bug investigation that ranks root-cause paths |
| orchestrate-batch-refactor | 660 | Planning and executing dependency-aware parallel refactors with scoped work packets |
| macos-menubar-tuist-app | 650 | Building, refactoring, or reviewing Tuist + SwiftUI menubar apps with reliable local launch scripts |

The remaining 2 indexed listings range from 68 to 194 installs.

## Why This Matters for Hermes Agents

Agents doing Apple platform work hit a specific failure profile: SwiftUI code that looks correct but thrashes at runtime, concurrency that compiles under Swift 6 but races under load, and release chores that are easy to get subtly wrong. These skills give an agent auditable procedures for each: performance audits that trace invalidation storms and identity churn, a Liquid Glass skill that encodes correct modifier ordering for iOS 26 APIs, and a concurrency expert for actor isolation and Sendable violations. The two swarm skills take a different approach to review: instead of one pass, they run four read-only agents over a diff or a bug report and return a ranked path, which suits agents that can delegate. The macOS packaging skills take Xcode out of the loop for SwiftPM apps, and the GitHub skill wraps the gh CLI so an agent can read CI results and run logs directly. Everything is plain SKILL.md content with no runtime dependencies, so only the skills relevant to a task need to be present.

## Usage

| You say | What happens |
|---|---|
| Our SwiftUI list scrolls badly on older iPhones | swiftui-performance-audit traces invalidation storms, identity churn, and layout thrash, then prescribes targeted fixes |
| Adopt Liquid Glass in this iOS 26 settings screen | swiftui-liquid-glass applies correct modifier ordering, grouping, interactivity, and fallbacks |
| This screen crashes in the simulator, find out why | ios-debugger-agent builds and launches the app on a booted simulator, then captures logs and screenshots |
| Review this branch before we merge | review-swarm runs a read-only four-agent diff review and returns a prioritized fix path |
| Migrate this feature to Swift 6.2 strict concurrency | swift-concurrency-expert fixes actor isolation, Sendable violations, and main-actor annotations |
| Write the release notes for our next App Store submission | app-store-changelog collects changes since the last tag and rewrites them as What's New bullets |
| Package this SwiftPM app for macOS without opening Xcode | macos-spm-app-packaging scaffolds, builds, signs, and optionally notarizes the app |

## Verification

Confirm the install and review a skill before trusting it:

```bash
# List installed skills
npx skills list | grep dimillian

# Codex manual installs: confirm the folders landed
ls "$CODEX_HOME/skills" | grep swiftui
```

Each skill lives at a predictable path in the repo, so you can review the exact instructions the agent will read before installing. For example, fetch the SwiftUI performance audit skill at `https://raw.githubusercontent.com/dimillian/skills/main/swiftui-performance-audit/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swiftui-performance-audit | Pass | Pass | Pass |
| swiftui-liquid-glass | Pass | Pass | Pass |
| swiftui-ui-patterns | Pass | Pass | Pass |

## Limitations

- Verdicts cover three sampled skills only; the rest of the suite is unaudited here, so re-check each skill's security page on skills.sh before production use.
- Last pushed Mar 2026: the SwiftUI and Liquid Glass guidance tracks fast-moving Apple SDKs, so re-check it against your current Xcode and iOS versions before applying it.
- The README documents sixteen skills while eighteen listings are indexed on skills.sh; gh-issue-fix-flow and simplify-code appear in the listings but not in the README skill table.
- ios-debugger-agent needs XcodeBuildMCP and a booted simulator, and the github skill needs an authenticated gh CLI; install those prerequisites first.
- The README's documented install path targets Codex ($CODEX_HOME/skills); other agents need the skills.sh CLI or a manual copy into their skills directory.
- MIT license per the repo; pin a revision when vendoring.

- Snapshot data, verified Oct 10, 2026: 33,834 combined installs across 18 indexed listings; 3,989 GitHub stars; MIT; last pushed 2026-03-29. Counts drift over time.

## Related

- [Macos Computer Use Setup](/hermes/skills/catalog/macos-computer-use-setup) - pairs with the macOS packaging and menubar skills for full desktop workflows
- [Hermes Agent Core - Official Skill Setup Guide](/hermes/skills/catalog/hermes-agent-setup) - how the Hermes skills system loads and routes installed skills
- [Hermex iPhone App - Setup Guide for Hermes Agent](/hermes/skills/catalog/hermex-iphone-app-setup) - mobile counterpart that pairs with the iOS debugging workflows
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the SwiftUI trio: swiftui-performance-audit (9,505 installs) and swiftui-ui-patterns cover most day-to-day app work.
- Set up prerequisites before first use: XcodeBuildMCP plus a booted simulator for ios-debugger-agent, and an authenticated gh CLI for github.
- Use review-swarm and bug-hunt-swarm as read-only gates: they return prioritized findings and paths, not patches, so run them before changes land.
- Copy only the folders you need under $CODEX_HOME/skills; every skill is self-contained with no cross-skill dependencies.
- The repo ships a GitHub Pages site (linked from the README) for browsing skill descriptions before installing.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
