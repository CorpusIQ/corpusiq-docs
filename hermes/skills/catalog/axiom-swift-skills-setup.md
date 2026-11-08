---
title: "Axiom Swift Skills - Apple Platform Skill Suite Setup"
description: "charleswiltgen/axiom on skills.sh: 64.1K combined installs across 200 listings; Apple platform skills for Swift 6, SwiftUI, Xcode and data."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/axiom-swift-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "swift", "swiftui", "apple platform"]
---

# Axiom Swift Skills - Setup Guide

**Source:** [charleswiltgen/axiom](https://www.skills.sh/charleswiltgen/axiom) via skills.sh - 64.1K combined installs across 200 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 1,253 stars, MIT, last pushed 2026-11-07, 125 SKILL.md files at this commit: 71 under `axiom-codex/skills/`, 27 under `axiom-cursor/` and 27 under `.claude-plugin/`, plus six bundled command line tools in `tools/`
**Category:** Apple platform development: Swift 6, SwiftUI, Xcode build and crash debugging, persistence, performance, accessibility and App Store shipping
**Quality Tier:** 🟢 Green - all three sampled skills pass all three scanners, the licence is MIT with a LICENSE file, and the skills themselves are markdown routed by name.

Axiom is the most serious Apple platform skill set on skills.sh. The pitch is specific: knowledge that prevents a bad SwiftData migration from losing user data, catches retain cycles before a user reports the crash, and stops an agent from guessing at a compiler diagnostic when Apple's documentation says what it means. `axiom-apple-docs` exists for exactly that last case, and it is a telling skill to ship.

The design is a router plus deep specialists. `axiom-swiftui`, `axiom-data`, `axiom-concurrency` and `axiom-networking` cover the four surfaces where Apple work usually goes wrong, and each one is a full discipline rather than a tip sheet. The README adds three counts that describe the packaging rather than the skills: 44 agents that scan for problems, 18 commands such as `/axiom:audit memory` and `/axiom:health-check`, and six bundled tools that give the agent a build log, a console, a symbolication path, a simulator driver, a profiler and a project reader.

## Installation

The README gives a route per host. Claude Code uses the plugin marketplace, and you install from the `/plugin` menu:

```bash
/plugin marketplace add CharlesWiltgen/Axiom
```

Codex installs the skills with the skills CLI, and optionally the full plugin for the bundled helpers and hooks:

```bash
npx skills add CharlesWiltgen/Axiom -a codex -g
codex plugin marketplace add CharlesWiltgen/Axiom
codex plugin add axiom@axiom-marketplace
```

The Codex hooks stay off until you set `features.hooks = true` in `~/.codex/config.toml` and approve the trust prompt. Pi installs everything in one command:

```bash
pi install git:github.com/CharlesWiltgen/Axiom
```

Cursor, the Claude app and MCP clients each have their own guide on the project site. The Claude app route is Customize, then Plugins, then Add marketplace, then enter `CharlesWiltgen/Axiom` and add the `axiom` plugin.

The README documents no Hermes command, and the CLI line it does ship names Codex explicitly with `-a codex`. What the tree does give you is a clean copy source: `axiom-codex/skills/` holds 71 directories, each a plain `SKILL.md` folder, which is the shape an agent skills directory expects. Copying or linking that directory is the portable route; the marketplace and installer routes are the tested ones.

## What It Provides

Twenty two listings clear the 1,200-install threshold, which is the discipline layer of the set:

| Skill | Installs | Use For |
|---|---|---|
| axiom-vision | 1,840 | Computer vision: image analysis, pose detection, segmentation, subject lifting, text recognition, barcodes |
| axiom-swiftui | 1,631 | SwiftUI views, navigation, layout, animation, gestures and iOS 26 features |
| axiom-networking | 1,593 | URLSession and Network.framework connections, API calls, sockets, connection diagnostics |
| axiom-apple-docs | 1,586 | Apple's own documentation and Swift compiler diagnostics, explained rather than recalled |
| axiom-shipping | 1,509 | App Store submission, rejection appeals, App Store Connect, TestFlight crash triage |
| axiom-xcode-mcp | 1,495 | Driving Xcode over MCP: mcpbridge, the headless server, XcodeRead and BuildProject |
| axiom-macos | 1,485 | macOS apps: windows, menus, sandboxing, distribution, AppKit bridging and modernization |
| axiom-design | 1,452 | HIG patterns, Liquid Glass, SF Symbols, typography, app entry point and auth flow structure |
| axiom-media | 1,412 | Camera, photos, audio, haptics, ShazamKit, screen recording, casting and SharePlay |
| axiom-performance | 1,400 | Slow apps, memory growth, battery drain, leaks, profiling and Instruments workflows |
| axiom-data | 1,376 | SwiftData, Core Data, GRDB, SQLite, Realm, CloudKit sync, file storage and migrations |
| axiom-testing | 1,370 | Swift Testing versus XCTest, flaky tests, async tests, test architecture |
| axiom-integration | 1,363 | Siri and Shortcuts, widgets, Live Activities, in-app purchase, localization, alarms and timers |
| axiom-build | 1,363 | Build failures, crash logs, crashing test runs, Xcode misbehaviour, environment faults |
| axiom-concurrency | 1,319 | Swift 6 concurrency, actors, @MainActor, Sendable, data races, async patterns |
| axiom-swift | 1,315 | Swift and its toolchain: idioms, noncopyable types, drag and drop, debug deep links, tvOS |
| axiom-tools | 1,301 | Axiom's own tooling: axbuild, xclog, xcsym, xcui and xcprof |
| axiom-security | 1,278 | Keychain storage, encryption, passkeys, prompt injection, code signing and certificates |
| axiom-uikit | 1,265 | UIKit and SwiftUI bridging, scene lifecycle, Auto Layout, Combine, TextKit, PencilKit |
| axiom-accessibility | 1,257 | VoiceOver, Dynamic Type, colour contrast, touch targets, WCAG and App Store accessibility review |
| axiom-graphics | 1,255 | Metal, shaders, 3D content, RealityKit, AR, USD files and display performance |
| axiom-ai | 1,211 | Foundation Models, @Generable, LanguageModelSession, on-device AI and speech to text |

The remaining 178 indexed listings range from 34 to 1,147 installs.

The tail is not filler. It is where the reference and diagnostic variants live: `axiom-swiftui-26-ref` at 281, `axiom-hig-ref` at 207, `axiom-testflight-triage` at 179, `axiom-lldb` at 108. Those are the files an agent loads when a discipline skill needs the exact API surface, so a strict threshold cut leaves out the reference layer underneath the table.

## Why This Matters for Hermes Agents

Apple platform work punishes invented detail. A plausible looking SwiftData migration that skips a versioned schema step destroys user data, and a concurrency fix that compiles but violates actor isolation ships a race. The difference between a model answer and a correct answer here is usually a specific API contract, which is exactly what these skills carry.

The debugging skills encode a decision order. `axiom-build` starts from build failures, crash logs and environment faults before code is the suspect, which is the order a senior iOS engineer works in and the opposite of what an agent does when it sees a failing test. Told to check the environment first, an agent stops rewriting correct code.

The bundled tools matter more than they look. A build that fails inside an agent session usually fails with truncated output, so the agent sees the last lines rather than the first error. `axbuild` saves the full log and returns a summary of errors and failed tests. `xclog` does the same for simulator logs, and `xcsym` symbolicates `.ips`, MetricKit and `.crash` files. Without them, the agent is guessing from a partial view.

For a Hermes agent the constraint is the host. Almost all of this needs macOS, Xcode and a simulator, so it is a set you install on a Mac worker rather than a Linux server. The reference skills that explain APIs are still useful on any host, but the audit and build skills are not.

The routing design is worth copying even if you never build for Apple. One router per problem area, one skill per discipline, and reference files loaded only when needed is the progressive disclosure pattern that keeps a large skill library inside a context window.

## Usage

| You say | What happens |
|---|---|
| "Build failed and I cannot see why" | `axiom-build` takes the build path, and `axbuild` returns the first real error instead of the truncated tail |
| "My app leaks memory" | `axiom-performance` walks leak patterns and profiling, and `/axiom:audit memory` runs the scan |
| "How do I fix Swift 6 concurrency errors?" | `axiom-concurrency` works through actor isolation, Sendable and @MainActor against the actual diagnostic |
| "I need to add a database column safely" | `axiom-data` produces a versioned SwiftData migration plan rather than an in-place schema edit |
| "Symbolicate this crash file" | `axiom-tools` routes to `xcsym`, which handles `.ips`, MetricKit and legacy `.crash` with dSYM discovery |
| "Is this ready for App Store review?" | `axiom-shipping` runs the submission checklist, and `axiom-accessibility` covers the accessibility rejection cases |
| "What does this Swift compiler error mean?" | `axiom-apple-docs` explains the diagnostic from Apple's documentation instead of paraphrasing it |

## Verification

Read the top skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/CharlesWiltgen/Axiom/main/axiom-codex/skills/axiom-vision/SKILL.md | head -8
```

It should open with `name: axiom-vision`, a description about computer vision work, and `license: MIT` in the frontmatter.

After install, confirm the skill directories are where the agent will look. The `axiom-codex` tree holds 71:

```bash
ls axiom-codex/skills | wc -l
```

If you installed through the plugin instead, check the `/plugin` menu for `axiom` and run `/axiom:health-check`, which the README lists as the command that runs all relevant auditors. A working install answers that command with a list, not an error.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07). This is a snapshot, so re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| axiom-vision | Pass | Pass | Pass |
| axiom-swiftui | Pass | Pass | Pass |
| axiom-networking | Pass | Pass | Pass |

The skills are markdown, but the plugin is not. The bundled tools in `tools/` are command line binaries and the Codex plugin adds lifecycle hooks, which the README keeps disabled until you set `features.hooks = true` and approve the trust prompt. That default is the right one, and it is worth leaving alone until you have read what the hooks do.

The Claude Code plugin also adds 44 agents that scan your project and 18 commands that run on request. Agents that read a codebase and write reports are a lower risk than agents that edit, but an audit agent still sees source, keys in configuration files and any secrets committed by mistake. Point it at repositories you would let a contractor read.

Xcode MCP is a new surface. `axiom-xcode-mcp` covers `xcrun mcpbridge` and the headless server, which expose project read and build actions to the agent. Grant it on a project you can rebuild, and check what the MCP server exposes before pointing it at a shipping app.

The licence is MIT with a LICENSE file in the repository root, so reuse and modification are uncomplicated.

## Limitations

- Snapshot data, verified 2026-11-07: 64,084 combined installs across 200 indexed listings; 1,253 GitHub stars; MIT; last pushed 2026-11-07. Counts drift over time.
- The README advertises 289 skills, while the tree at this commit carries 125 SKILL.md files across `axiom-codex/skills` (71), `axiom-cursor` (27) and `.claude-plugin` (27). The larger number counts the published catalogue rather than installable directories, so confirm what your host actually loads.
- The set is macOS bound. Build, simulator, profiling and crash symbolication skills need Xcode and an Apple toolchain, so a Linux host can use the reference skills and little else.
- The README states that an OS 27 beta track is in progress and that guidance for OS 26 and earlier stays stable, which means the newest material is moving. Pin a revision if you need reproducible behaviour.
- The bundled tools (`axbuild`, `xclog`, `xcsym`, `xcui`, `xcprof`, `xcproject`) ship with the Claude Code plugin and the full Codex plugin, not with a plain skills install. A skills only install gets the knowledge without the tooling.
- The reference and diagnostic variants sit below the table threshold. Reading only the table rows leaves out `axiom-*-ref` and `axiom-*-diag` files that the discipline skills call on for exact API detail.

## Related

- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [Swift Concurrency Agent Skill - Swift 6 Setup](/hermes/skills/catalog/avdlee-swift-concurrency-setup)
- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `axiom-apple-docs` on a real compiler error. If the answer cites Apple's documentation rather than paraphrasing, the skill set is working as designed.
- Install the plugin rather than the bare skills if you debug builds. `axbuild` and `xclog` are the difference between seeing the first error and seeing the last line.
- Run `/axiom:health-check` once on a healthy project. The output is the baseline you compare against when something breaks.
- Keep the hooks off until you need them. `features.hooks = true` in the Codex config is a deliberate opt in, and the trust prompt is the point where you decide.
- Read the `-ref` skill for any API you are about to write against. The discipline skills give the method, and the reference files give the signatures that stop an agent from inventing one.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
