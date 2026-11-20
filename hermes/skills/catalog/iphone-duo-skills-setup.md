---
title: "iPhone Duo Skills - Foldable iOS Dev Setup Guide"
description: "mirzaaghazadeh/iphone-duo-skills: 11 skills for building iOS apps on iPhone Duo, Apple's first foldable iPhone - 9.0K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iphone-duo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "ios", "foldable", "mobile development"]
---

# iPhone Duo Skills - Setup Guide

**Source:** [mirzaaghazadeh/iphone-duo-skills](https://www.skills.sh/mirzaaghazadeh/iphone-duo-skills) via skills.sh - 9.0K combined installs across 11 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** [mirzaaghazadeh/iphone-duo-skills](https://github.com/mirzaaghazadeh/iphone-duo-skills) - 331 stars, MIT licence (the repo ships an MIT LICENSE file; GitHub metadata reports NOASSERTION), main branch, last pushed Nov 17, 2026. Skills live under `skills/<name>/SKILL.md` (11 directories).
**Category:** iOS / Foldable iPhone Development
**Quality Tier:** 🟡 Yellow - 1 Warn among 11 sampled verdicts (Snyk flags iphone-duo-capacitor); NOASSERTION licence field though the repo ships an MIT LICENSE.

Apple announced iPhone Duo, its first foldable iPhone, on September 9, 2026, and the developer material that followed (Tech Talk sessions, a Human Interface Guidelines page, a Prepare checklist, and an API reference) carries several corrections against the early claims. This repository distills all of it into eleven structured skills an agent can act on, plus reference sheets for device facts and the full iOS 27.1 API surface. Every technical claim traces to Apple's own material, and the repository ran five verification passes against the API reference between September and November 2026.

The suite is built around one insight: iPhone Duo is not a new idiom but a wider continuum of sizes, and every foldable port defect comes from an app asserting something fixed (an idiom, an orientation, a screen width, a symmetric inset). The skills replace those assertions with questions about the space available right now.

## Installation

```bash
npx skills add mirzaaghazadeh/iphone-duo-skills
```

Installs all eleven. The CLI detects the agent (Claude Code, Cursor, Copilot, Gemini and others) and places the skills where that agent looks.

```bash
# just one skill
npx skills add mirzaaghazadeh/iphone-duo-skills --skill iphone-duo-readiness

# user-level instead of project-level
npx skills add mirzaaghazadeh/iphone-duo-skills --global

# see what is inside without installing
npx skills add mirzaaghazadeh/iphone-duo-skills --list
```

To try a skill without installing it:

```bash
npx skills use mirzaaghazadeh/iphone-duo-skills@iphone-duo-readiness
```

Manual install:

```bash
git clone https://github.com/mirzaaghazadeh/iphone-duo-skills.git
cp -r iphone-duo-skills/skills/* ~/.claude/skills/
```

Each skill is a self-contained SKILL.md with YAML frontmatter, so it also works anywhere that reads plain Markdown instructions.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| iphone-duo-readiness | 1,040 | Entry point: audit and port an existing iOS app to iPhone Duo, routing to the rest |
| iphone-duo-adaptive-layout | 1,001 | Layouts that avoid the fold via reserved regions, division vs occlusion and ArrangementView |
| iphone-duo-design-review | 966 | Design critique for the closed, open, book-folded, tabletop and tent poses |
| iphone-duo-vertical-bars | 935 | Toolbars, navigation bars and tab bars on the vertical outer-display axis |
| iphone-duo-hinge-and-scenes | 907 | Hinge-driven effects, Split View and multi-scene dual-display UI |
| iphone-duo-camera | 797 | Dual front-camera capture with the direction and rotation coordinators |
| iphone-duo-dual-pane-patterns | 755 | Two-pane layouts, exact hinge callback types and pose-to-pattern mapping |
| iphone-duo-react-native | 725 | React Native / Expo support via a native module bridge to the iOS 27.1 APIs |
| iphone-duo-games | 680 | Game adaptation across poses with touch controls kept clear of the fold |
| iphone-duo-flutter | 677 | Flutter support via platform channels to the iOS 27.1 APIs |
| iphone-duo-capacitor | 565 | Capacitor / Ionic web-view apps getting fold state from the native side |

All 11 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Apple's first foldable iPhone breaks the assumptions most iOS code carries: a single screen, symmetric safe areas, one front camera, fixed orientation. An agent porting an existing app to iPhone Duo hits these as silent defects rather than compiler errors. This suite turns that work into checkable guidance: reserved regions and hinge callbacks instead of guessing, real iOS 27.1 API names instead of placeholders, and a readiness entry point that routes to the specific skill for each gap. The cross-platform skills are explicit about what does not work yet (Flutter's `MediaQuery.displayFeatures` is populated only on Android, and React Native has no fold API), so an agent does not lose a session hunting for an API that is not there. A weekly docs watcher diffs 33 Apple pages, which matters because Apple corrected several early claims after the announcement.

## Usage

| You say | What happens |
|---|---|
| Port my SwiftUI app to iPhone Duo | The readiness skill audits the app for fixed assumptions and routes to the layout, bar, hinge and camera skills |
| This toolbar overflows on the outer display | The vertical-bars skill reworks item ordering, axis behavior, overflow menus and visibility priority |
| Add a two-pane layout that reacts to the hinge | The dual-pane-patterns skill maps the pose to a pattern and wires the hinge callback |
| My camera app flips when the device folds | The camera skill applies the direction coordinator and rotation handling across camera switches |
| My Flutter app needs fold support | The Flutter skill bridges the reserved-region and hinge APIs through platform channels |
| Review this screen for the tent pose | The design-review skill critiques fold avoidance, side-mounted controls and asymmetry |

## Verification

```bash
# after install, confirm the skills landed in the agent skills directory
ls ~/.claude/skills/
# review one skill's instructions before relying on it
curl -sL https://raw.githubusercontent.com/mirzaaghazadeh/iphone-duo-skills/main/skills/iphone-duo-readiness/SKILL.md
```

The raw SKILL.md URL above was probed Nov 19, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| iphone-duo-readiness | Pass | Pass | Pass |
| iphone-duo-adaptive-layout | Pass | Pass | Pass |
| iphone-duo-design-review | Pass | Pass | Pass |
| iphone-duo-vertical-bars | Pass | Pass | Pass |
| iphone-duo-hinge-and-scenes | Pass | Pass | Pass |
| iphone-duo-camera | Pass | Pass | Pass |
| iphone-duo-dual-pane-patterns | Pass | Pass | Pass |
| iphone-duo-react-native | Pass | Pass | Pass |
| iphone-duo-games | Pass | Pass | Pass |
| iphone-duo-flutter | Pass | Pass | Pass |
| iphone-duo-capacitor | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 19, 2026: 9,048 combined installs across 11 indexed listings; 331 GitHub stars; MIT licence file (GitHub metadata reports NOASSERTION); last pushed Nov 17, 2026. Counts drift over time.
- The GitHub metadata licence field reads NOASSERTION, but the repository ships a full MIT LICENSE file and its README states MIT; treat the MIT text in the repo as the operative licence.
- All eleven indexed listings map to directories in the current tree, so there is no index-vs-tree drift to reconcile.
- The skills target a device that was announced in September 2026 and whose APIs are still being corrected by Apple; verify against the current Apple docs before shipping a port.

## Related

- [Mosif16 Codex Skills - iOS Design Setup](/hermes/skills/catalog/mosif16-codex-skills-setup)
- [Swift Testing Pro Skill - Swift Testing Suite Setup](/hermes/skills/catalog/swift-testing-pro-skill-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [Hermex iPhone App - Setup Guide for Hermes Agent](/hermes/skills/catalog/hermex-iphone-app-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Build against the iOS 27.1 SDK: it is the gate for edge-to-edge content, vertical bars, reserved regions and arrangements.
- Branch on size class, never on orientation or idiom, because the inner display ignores your supported interface orientations.
- `UIScreen.main` is ambiguous on this device and slated for deprecation; use the environment, the trait collection, or the scene's bounds.
- Safe areas are asymmetric, so any math shaped like `width - safeAreaInsets.left * 2` is a defect to flag in review.
- Start any stack with `iphone-duo-readiness`; it routes to the specific skill for each gap instead of requiring you to read all eleven.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
