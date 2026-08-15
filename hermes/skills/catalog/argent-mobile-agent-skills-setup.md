---
title: Argent Skills — Mobile Dev Agent Toolkit Setup
description: "software-mansion/argent — 20 skills, 154.0K installs: Android emulator and iOS simulator setup, React Native workflows, device interaction, profilers, screenshot diffing, and QA flows from the creators of react-native-reanimated."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/argent-mobile-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "react-native", "mobile development", "emulator", "simulator", "qa"]
---

# Argent Skills — Setup Guide

**Source:** [software-mansion/argent](https://skills.sh/software-mansion/argent)
**GitHub:** [software-mansion/argent](https://github.com/software-mansion/argent)
**Skills:** 20 skills · 154.0K total installs
**Category:** Mobile Development & QA
**First Seen:** catalogued August 15, 2026 midday sweep
**Quality Tier:** 🟢 Production (established vendor — Software Mansion, creators of react-native-reanimated, react-native-gesture-handler, and react-native-screens)

Argent is Software Mansion's agent toolkit for mobile development: it teaches agents how to stand up Android emulators and iOS simulators, drive device interaction, run React Native workflows and profilers, debug Metro, and diff screenshots. When queued in the morning sweep it was estimated at 11.9K installs from API sums; the publisher page shows 154.0K — the largest queue underestimate of the day, which is why it leads this batch.

---

## Installation

```bash
npx skills add software-mansion/argent
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Android SDK / emulator** | For `argent-android-emulator-setup` and device-interact skills |
| **Xcode + iOS simulator** | For iOS simulator, profiler, and screen-recording skills |
| **React Native project** | For workflow, optimization, and Metro debugging skills |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| argent-android-emulator-setup | 12.0K | Stand up an Android emulator for testing |
| argent-ios-simulator-setup | 11.9K | Stand up an iOS simulator |
| argent-react-native-app-workflow | 11.9K | Canonical RN app dev workflow |
| argent-react-native-optimization | 11.9K | RN performance optimization guidance |
| argent-device-interact | 11.8K | Tap, type, and navigate on devices |
| argent-test-ui-flow | 11.8K | End-to-end UI flow testing |
| argent-react-native-profiler | 11.8K | Profile RN performance |
| argent-metro-debugger | 11.8K | Debug Metro bundler issues |
| argent-create-flow | 11.8K | Scaffold new app flows |
| argent-native-profiler | 11.8K | Native-side profiling |
| argent-screenshot-diff | 10.5K | Visual regression via screenshot diffing |
| argent-lens | 8.1K | Visual element inspection |
| argent-tv-interact | 6.6K | TV platform interaction |
| argent-settings-permissions | 4.8K | Manage device settings and permissions |
| argent-screen-recording | 3.5K | Record device screens |
| argent-qa-flows / argent-vega | 952 / 902 | QA workflow support and Vega automation |

## Quick Start

1. Install: `npx skills add software-mansion/argent`
2. Start with the emulator or simulator setup skill for your target platform
3. Ask: "set up an Android emulator and run my React Native app through the canonical workflow"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Mobile QA automation** | Emulator/simulator setup plus screenshot diffing replaces manual device checks |
| **RN performance work** | Profiler skills for client mobile projects |
| **Agent-driven device testing** | device-interact and test-ui-flow as a mobile testing surface |
| **Reference architecture** | Vendor-quality skill packaging from a top React Native shop |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- iOS simulator skills require macOS with Xcode; Android skills require the SDK
- Three simulator skills (argent-ios-profiler, argent-simulator-setup, argent-simulator-interact) show single-digit installs and should be treated as new

```bash
npx skills add software-mansion/argent   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
