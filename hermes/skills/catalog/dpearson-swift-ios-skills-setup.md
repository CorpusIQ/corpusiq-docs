---
title: "Swift iOS Skills - iOS 26 and SwiftUI Suite Setup"
description: "dpearson2699/swift-ios-skills: 305.9K combined installs. 86 iOS 26 and SwiftUI skills covering Apple frameworks, concurrency and App Review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dpearson-swift-ios-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "swift", "ios"]
---

# Swift iOS Skills - Setup Guide

**Source:** [dpearson2699/swift-ios-skills](https://www.skills.sh/dpearson2699/swift-ios-skills) via skills.sh - 305.9K combined installs across 100 indexed listings, the largest source in this sweep; first seen Mar 3, 2026
**GitHub:** [dpearson2699/swift-ios-skills](https://github.com/dpearson2699/swift-ios-skills) (1,237 stars; GitHub reports the license as NOASSERTION while the LICENSE file holds the full PolyForm Perimeter 1.0.0 text, a source-available license with a noncompete clause; pushed 2026-07-31; 86 `skills/<name>/SKILL.md` directories, all 86 with an `evals/` folder and 85 with a `references/` folder, plus 259 eval scenario folders, `.claude-plugin/marketplace.json` and a 3.9.1 CHANGELOG)
**Category:** Mobile / Apple Platform Development
**Quality Tier:** 🟡 Trusted - deep, evaluated content at 305.9K installs with clean Trust Hub and Socket verdicts, held below Production by the PolyForm Perimeter noncompete license, one Snyk Warn on app-store-review, and a last push three months before this snapshot

Apple's annual release cycle is the hardest knowledge problem in mobile work. iOS 26 replaced the visual layer with Liquid Glass, added the Foundation Models framework for on-device inference, and shipped a new batch of Kit frameworks (PaperKit, AlarmKit, PermissionKit, EnergyKit, RelevanceKit, DockKit, SensorKit). Most models still answer with UIKit-era or iOS 17 patterns. This repository is 86 self-contained skills aimed squarely at iOS 26 and iPadOS 26 with Swift 6.3, and it is the most installed third-party skill source in this catalog sweep at 305.9K combined installs.

The publisher is the `dpearson2699` handle, called Derek Pearson in the repo's Claude Code marketplace metadata. The name reads like a personal account and it is one: this is an individual maintainer's suite rather than an org-backed one, versioned at 3.9.1 with a public CHANGELOG that records each skill rewrite. Every skill is independent, so an agent can load only the surface it needs; the repo's own guidance is to install per skill rather than everything.

## Installation

```bash
# Interactive picker: choose skills and target agents
npx skills add dpearson2699/swift-ios-skills

# Install all 86 skills for any supported agent
npx skills add dpearson2699/swift-ios-skills --all

# Install only what the task needs
npx skills add dpearson2699/swift-ios-skills --skill swiftui-animation --skill swiftdata
```

```bash
# Refresh later
npx skills check
npx skills update
```

```bash
# Claude Code marketplace route: one bundle or a themed subset
/plugin marketplace add dpearson2699/swift-ios-skills
/plugin install all-ios-skills@swift-ios-skills
/plugin install swiftui-skills@swift-ios-skills
```

```bash
# Codex route, one skill folder at a time
$skill-installer install https://github.com/dpearson2699/swift-ios-skills/tree/main/skills/swiftui-animation
```

Node.js is required for `npx`. The skills themselves are reference content and install anywhere, but following them means a macOS host with Xcode and the iOS 26 SDK, since the code they generate targets Swift 6.3 and iOS 26 APIs. No API key or account is needed, and the Claude bundle route caps how many skills load at once by theme (swiftui-skills carries 10, ios-gaming-skills 4, apple-kit-skills 39).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| swiftui-animation | 5,422 | Spring animations, PhaseAnimator, KeyframeAnimator, matchedGeometryEffect and SF Symbols motion, reviewed against iOS 26 APIs |
| ios-accessibility | 4,965 | VoiceOver, Dynamic Type, custom rotors, accessibility focus and assistive-technology support across SwiftUI, UIKit and AppKit |
| swiftui-performance | 4,619 | Rendering performance, view update optimization, layout thrash and Instruments profiling |
| swiftui-patterns | 4,543 | @Observable, state ownership, environment wiring, view composition, async loading and MV-pattern architecture |
| app-store-review | 4,530 | App Review guideline checks before submission: rejection prevention, privacy manifests, ATT and HIG compliance |
| ios-networking | 4,394 | URLSession async/await, REST APIs, downloads and uploads, WebSockets, pagination, retry and caching |
| swiftui-navigation | 4,363 | NavigationStack, NavigationSplitView, programmatic navigation and deep linking |
| swift-testing | 4,319 | Swift Testing framework: @Test, @Suite, #expect, parameterized tests and mocking |
| ios-localization | 4,292 | String Catalogs, pluralization, FormatStyle and right-to-left layout |
| swift-concurrency | 4,285 | Swift 6.2 concurrency: Sendable, actors, structured concurrency and data-race safety |
| swiftui-layout-components | 4,233 | Grid, LazyVGrid, the Layout protocol, ViewThatFits and custom layouts |
| push-notifications | 4,178 | UNUserNotificationCenter, APNs, rich and silent push, service extensions |
| swiftdata | 4,136 | @Model, @Query, #Predicate, ModelContainer, migrations, CloudKit sync and @ModelActor |
| swiftui-liquid-glass | 4,127 | iOS 26 Liquid Glass: glassEffect, GlassEffectContainer and morphing transitions |
| debugging-instruments | 4,068 | Xcode debugger, Instruments, os_signpost, MetricKit and crash symbolication |
| swiftui-uikit-interop | 4,059 | UIViewRepresentable, UIHostingController, Coordinator and incremental UIKit to SwiftUI migration |
| storekit | 4,035 | StoreKit 2 purchases, subscriptions, SubscriptionStoreView and transaction verification |
| apple-on-device-ai | 4,020 | Foundation Models framework, Core ML, MLX Swift and on-device LLM inference |
| swiftui-gestures | 4,019 | Tap, drag, magnify, rotate and long press gestures, including simultaneous and sequential composition |
| widgetkit | 4,011 | Home Screen, Lock Screen and StandBy widgets, Control Center controls and timeline providers |

The remaining 80 indexed listings range from 252 to 3,979 installs and fall into four groups. Core Swift and tooling sits just under the table, from swift-charts (3,979) and swift-language (3,965) through swift-codable 3,586, cryptokit 3,169, metrickit 3,153, swift-architecture 3,083, swift-security 2,983, swift-api-design-guidelines 2,821, swiftlint 2,718, swift-formatstyle 2,679 and core-data 2,666 down to focus-engine 2,641, with app-intents 3,961, authentication 3,884 and background-processing 3,872 alongside. Then comes one skill per Apple framework, a band from HealthKit (3,853) to SensorKit (3,020) that includes Vision, Core ML, Core Bluetooth, Core Motion, Speech, Natural Language, PhotoKit, AVKit, MusicKit, PDFKit, PencilKit, PaperKit, Core NFC, DeviceCheck and App Attest, Contacts, CryptoTokenKit, AccessorySetupKit, CallKit, AlarmKit, TipKit, App Clips, ActivityKit, SharePlay, WeatherKit, CloudKit, CarPlay, HomeKit, DockKit, BrowserEngineKit, AppMigrationKit, RelevanceKit, AudioAccessoryKit, AdAttributionKit, WebKit, MapKit, EventKit and PassKit, with ios-simulator at 3,052 and the graphics and games set (RealityKit, SpriteKit, SceneKit, GameKit, TabletopKit at 2,944) just below. Below that sit three analysis and security skills at 1,237 to 1,106 (ios-memgraph-analysis, ios-ettrace-performance, ios-security), and 13 listings under 500: twelve are the v2.x names that v3.0 renamed to Apple Kit names (live-activities 465 down to passkit-wallet 401), plus codable-patterns at 252.

## Why This Matters for Hermes Agents

SwiftUI is the worst case for retrieval-free code generation. A view modifier that exists in iOS 18 but was renamed in iOS 26 compiles into a deprecation warning at best and a rejected App Store build at worst, and a model trained before June cannot know which of the 40-odd Kit frameworks landed this cycle. An iOS 26 skill that states the current API is worth more than a general Swift skill that states the 2023 one.

The suite is unusually well distributed across the framework surface. Rather than one monolith, each framework gets its own SKILL.md with a `references/` folder for deeper material and an `evals/` folder of scenario checks, which means a session working on WidgetKit loads WidgetKit plus ActivityKit only where they connect, and nothing else. The widgetkit skill explicitly scopes adjacent frameworks and hands lifecycle and entity work to sibling skills, which is the behaviour that keeps context predictable.

Quality control is visible in the repo rather than claimed. The CHANGELOG records editorial passes over all 86 skills, 259 eval scenario folders exist under `evals/`, and the maintainer's own AGENTS.md instructs contributors to load the Agent Skills specification and best-practice documents before touching content. For an operator deciding whether to trust generated code, that is a stronger signal than install count alone.

For App Store work specifically, this collection covers the parts agents usually get wrong: privacy manifests and ATT in app-store-review, StoreKit 2 transaction verification in storekit, Sign in with Apple and passkeys in authentication, and ASO copy and Custom Product Pages in app-store-optimization. Each is a discrete skill, so a review pass can load the submission-facing ones without dragging in UI guidance.

## Usage

| You say | What happens |
|---|---|
| "Build a settings screen with Liquid Glass grouped sections" | Loads swiftui-liquid-glass for glassEffect and GlassEffectContainer, plus swiftui-patterns for @Observable state ownership, then writes against iOS 26 APIs |
| "This list stutters while scrolling images" | Uses swiftui-performance for view update and layout thrash guidance, and points at the Instruments and os_signpost workflow in debugging-instruments |
| "Add StoreKit 2 subscriptions with a paywall" | Loads storekit for product loading, SubscriptionStoreView and transaction verification, and hands entitlement storage to swiftdata |
| "Our build was rejected for missing privacy manifests" | Works through app-store-review for privacy manifest, ATT and SDK signature requirements, then produces the checklist for resubmission |
| "Convert this callback-based fetch to async/await" | Loads ios-networking for URLSession async patterns and swift-concurrency for Sendable and actor isolation on the result types |
| "VoiceOver reads this card as one blob" | Uses ios-accessibility to split accessibility elements, add labels and traits, and verify with the rotor |
| "We need a widget showing today's forecast" | Loads widgetkit for the timeline provider and Lock Screen families, and weatherkit for the WeatherService query behind it |

## Verification

Confirm the install and list what landed:

```bash
npx skills list | grep -Ei "swift|ios"
ls ~/.claude/skills | head -30
```

Read a skill before trusting it in a build. All six URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/dpearson2699/swift-ios-skills/main/README.md
curl -sL https://raw.githubusercontent.com/dpearson2699/swift-ios-skills/main/LICENSE
curl -sL https://raw.githubusercontent.com/dpearson2699/swift-ios-skills/main/skills/swiftui-animation/SKILL.md
curl -sL https://raw.githubusercontent.com/dpearson2699/swift-ios-skills/main/skills/ios-accessibility/SKILL.md
curl -sL https://raw.githubusercontent.com/dpearson2699/swift-ios-skills/main/skills/app-store-review/SKILL.md
curl -sL https://raw.githubusercontent.com/dpearson2699/swift-ios-skills/main/skills/widgetkit/SKILL.md
```

Check the version boundary a skill claims before applying it, since the suite targets iOS 26 only:

```bash
grep -m3 -i "iOS 26\|Swift 6.3\|availability" \
  ~/.claude/skills/swiftui-liquid-glass/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| swiftui-animation | Pass | Pass | Pass |
| ios-accessibility | Pass | Pass | Pass |
| app-store-review | Pass | Pass | Warn |
| widgetkit | Pass | Pass | Pass |

The Snyk Warn on app-store-review is the only non-Pass verdict across the four sampled skills, and it is worth reading before letting an agent act on that skill's submission guidance. None of the sampled skills carry an `allowed-tools` frontmatter block, so installing them does not widen an agent's tool surface by itself. The behaviour lives in the instructions and in four bundled Python scripts: `skills/ios-memgraph-analysis/scripts/capture_sim_memgraph.py` shells out to `xcrun simctl` against a booted simulator and writes a memgraph capture plus a JSON summary, and `skills/ios-ettrace-performance/scripts/` does the same for ETTrace runs and dSYM collection. Both use only local subprocess calls with no network code. The ios-simulator skill teaches `xcrun simctl` device management, including destructive commands such as erase, so an agent following it can wipe simulator state. The framework skills discuss credentials in the normal course of their subject matter (Keychain and Secure Enclave in swift-security, Apple Pay in passkit, App Attest in device-integrity, CloudKit in cloudkit, APNs in push-notifications), but they document app-side usage rather than handling secrets, and nothing in the repository phones home.

## Limitations

- The license is PolyForm Perimeter 1.0.0, not an OSI-approved open source license. It permits commercial and closed-source use, changes and redistribution, but forbids providing any product that competes with the software, and it requires the `Required Notice` line to travel with every copy. GitHub's license field reports NOASSERTION because the detector does not recognise the text, so the API metadata and the LICENSE file disagree; read the file, not the badge.
- The last push is 2026-07-31, roughly three months before this snapshot. The README flags six skills as beta-framework guidance (permissionkit, energykit, paperkit, relevancekit, appmigrationkit, audioaccessorykit) that are subject to API change before GM, and those are exactly the skills most likely to have drifted since the push.
- Coverage is iOS 26 and Swift 6.3 only, by design. There is no iOS 17 or 18 fallback guidance and no deprecated-pattern reference, so a project that must support older deployment targets needs a second source.
- The install index outruns the tree: 100 indexed listings against 86 directories. Twelve of the extra listings are v2.x names that v3.0 renamed to Apple Kit names (the rename table is in the README), and installing an old name no longer resolves. ios-security (1,106 installs) and codable-patterns (252 installs) have no directory at `main` and do not appear in that rename table.
- The Claude Code bundles split the suite by theme, and the README warns that context cost scales with bundle count: install `all-ios-skills` if you want everything rather than stacking bundles.
- Snapshot data, verified Oct 26, 2026: 305,876 combined installs across 100 indexed listings; 1,237 GitHub stars; NOASSERTION on GitHub with PolyForm Perimeter 1.0.0 in the LICENSE file; last pushed 2026-07-31. Counts drift over time.

## Related

- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup) - a narrower Swift Testing suite that pairs with the swift-testing skill here.
- [Xcode Build Optimization - iOS Build Performance Setup](/hermes/skills/catalog/xcode-build-optimization-setup) - build-time work that complements swiftui-performance and debugging-instruments.
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup) - the release pipeline side, after app-store-review has cleared the submission.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Do not install all 86 by reflex. `--skill` with three or four names keeps discovery cost low, and the skills are independent by design, so there is no dependency to satisfy.
- Pin the age of the guidance. Every skill targets iOS 26, so note the Xcode and SDK version in the task and have the agent state availability checks rather than assuming an API is present.
- Use the themed bundles when working in Claude Code: `swiftui-skills` for interface work, `ios-engineering-skills` for review and release work, `apple-kit-skills` for framework lookups.
- Read the CHANGELOG before upgrading. The v3.0 rename moved 12 skills to Kit names and old paths stopped resolving, which is the same failure you will hit if a session has stale skill directories.
- Run the skill's own eval scenarios as a smoke test after editing anything locally. Each skill ships an `evals/` folder, so you can check that a rewritten instruction still produces the intended behaviour.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
