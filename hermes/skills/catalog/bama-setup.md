---
title: "BAMA - Build Any Mac App - Setup Guide"
description: "daveebbelaar/bama: 21 agent skills to research, clone, design, build and test native macOS apps with Swift and SwiftUI - 20.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bama-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "macos", "swiftui", "app development"]
---

# BAMA - Build Any Mac App - Setup Guide

**Source:** [daveebbelaar/bama](https://www.skills.sh/daveebbelaar/bama) via skills.sh - 20.9K combined installs across 21 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [daveebbelaar/bama](https://github.com/daveebbelaar/bama) - 1,917 stars, MIT license, main branch, last pushed Nov 5, 2026. Skills live under skills/<stage>/<name>/SKILL.md across five stages (start, plan, code, design, ship), 128 files in the tree.
**Category:** Native macOS App Development
**Quality Tier:** 🟡 Yellow - 2 Warn among 20 sampled verdicts (Snyk: clone; Socket: improve-loop); MIT license.

BAMA (Build Any Mac App) is a suite of 21 agent skills that take a native macOS app from idea to the Dock, using Swift and SwiftUI with local data and no Xcode GUI. The skills span five stages: start (the bama router, app-brief and new-mac-app), plan (research, clone, user-stories), code (swift-swiftui, os-integrations, performance, improve-architecture, agent-cli), design (seven skills from mac-design to app-icon) and ship (build-and-verify, test-mac-app, improve-loop). The repository also ships 12 build plans in specs/ for small Mac apps, such as a window snapper and clipboard history.

The pitch is "see an app you like, rebuild it as your own native Mac app": an agent screenshots every screen of a reference app, turns the screens into a prioritized backlog with checkable acceptance criteria, then builds one story per commit while snapshotting every page in light and dark mode before calling a change done. The suite installs through skills.sh, as a Claude Code or Codex plugin, or by hand.

## Installation

The fastest route for any skills-protocol agent (Hermes, Cursor, Gemini CLI, Copilot and more) is skills.sh:

```bash
npx skills@latest add daveebbelaar/bama
```

Install a single skill instead of the whole suite:

```bash
npx skills@latest add daveebbelaar/bama --skill=clone
```

Claude Code plugin:

```text
/plugin marketplace add daveebbelaar/bama
/plugin install bama@bama
```

Codex plugin:

```bash
codex plugin marketplace add daveebbelaar/bama
codex plugin add bama@bama
```

By hand:

```bash
git clone https://github.com/daveebbelaar/bama.git
bama/scripts/link-skills.sh
```

link-skills.sh links every skill into ~/.claude/skills and ~/.agents/skills. Requirements: macOS 26 or later, Xcode 26 or later (for the Swift 6.2 toolchain), an agent that supports skills, and computer use (Claude Pro or Max) for the clone skill on native apps.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| app-icon | 1,008 | Liquid Glass macOS app icon as an Icon Composer file, compiled with actool and reviewed in every look |
| mac-design | 1,006 | Design rules for a native Mac look on macOS 26+: Apple's eight principles, Liquid Glass, toolbars, menus, type, color, dark mode |
| clone | 1,002 | Screenshot every screen of an existing app with computer use or a browser, then write a screen index |
| ux-design | 1,001 | UX pass for one feature: names, flow, where it opens, states, words, hover help, accessibility, AI features |
| bama | 1,000 | Router: finds where you are in the build and calls the right skill |
| test-mac-app | 1,000 | Swift Testing unit tests, an in-app self-test, and a debug bridge an agent can drive |
| new-mac-app | 998 | A working app from a template: Swift package, SwiftData, build script, snapshot mode, git |
| user-stories | 996 | Prioritized backlog with checkable acceptance criteria, in milestones |
| swift-swiftui | 996 | Swift 6 concurrency, state, SwiftData, AppKit bridges, and common compiler errors |
| design-kit | 996 | Your own parts, not Apple's: token layers, type, icon set, parts gallery, custom window chrome |
| design-system | 995 | Accent color and design tokens in Settings and code, plus a DESIGN-SYSTEM.md rules page |
| layout-grid | 994 | 4 pt grid with alignment checks: a code lint, a layout probe, a grid overlay |
| improve-architecture | 994 | Finds hot spots and refactors one step per commit with behavior proven unchanged |
| os-integrations | 993 | Global hotkeys, menu bar, floating panels, window control, screen capture, Shortcuts, URL schemes, CLI, permissions |
| performance | 992 | Measure hangs, CPU, memory, energy, then move work off the main thread and onto the GPU |
| design-from-app | 992 | Rebuild the look of an app you like by measuring its screenshots and comparing pixel by pixel |
| app-brief | 992 | One-page brief (docs/BRIEF.md) for a new macOS app before any code |
| build-and-verify | 990 | Build, install, and snapshot every page in light and dark before calling a change done |
| agent-cli | 990 | Optional CLI and MCP server so Claude Code, Codex, and scripts can drive the running app |
| improve-loop | 988 | Autonomous loop through docs/STORIES.md, one story per commit until a milestone is done |
| research | 987 | Parallel researcher agents: market, users, features, design, macOS APIs |

No indexed listings fall below the 700-install threshold; all 21 appear above.

## Why This Matters for Hermes Agents

Building a native Mac app with an agent usually breaks down because the agent does not know Swift and SwiftUI conventions, cannot verify what it just built, and has no discipline for design. BAMA closes those gaps: swift-swiftui supplies the Swift 6 rules, build-and-verify compiles and snapshots every page before a change counts as done, and mac-design plus the six other design skills enforce a native look instead of a generic one. The staged layout means an agent loads only the stage it needs: start with the bama router, then pull research, clone and user-stories when planning, and the code, design and ship skills as the build proceeds. Because every skill ships as a SKILL.md file, the suite works with any agent that supports the skills protocol, not just Claude Code. The autonomous improve-loop is the standout: an agent can work through the backlog one story at a time, building, snapshotting, comparing against reference screenshots and committing, so a long build can run with light supervision.

## Usage

| You say | What happens |
|---|---|
| Clone my to-do app as a native Mac app | The clone skill screenshots every screen and writes a screen index, then user-stories turns it into a backlog |
| Screenshot every screen, write the user stories, and build milestone 1 | The agent walks clone, user-stories, then build-and-verify one story per commit |
| Make it look like Spotify | design-from-app measures the reference screenshots and builds a matching SwiftUI design kit |
| Build the app in window-snapper.md with BAMA | The agent reads the spec and drives the start and build stages from it |
| Keep going through the backlog | improve-loop works through docs/STORIES.md, snapshotting and committing each story until the milestone is done |
| Make it feel more native | mac-design applies Apple's design principles, Liquid Glass, toolbars and menus to the current screen |

## Verification

```bash
# after a by-hand install, confirm the skills linked into place
ls ~/.claude/skills
ls ~/.agents/skills
# review the router skill before relying on the suite
curl -sL https://raw.githubusercontent.com/daveebbelaar/bama/main/skills/start/bama/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| app-icon | Pass | Pass | Pass |
| mac-design | Pass | Pass | Pass |
| clone | Pass | Pass | Warn |
| ux-design | Pass | Pass | Pass |
| bama | Pass | Pass | Pass |
| test-mac-app | Pass | Pass | Pass |
| new-mac-app | Pass | Pass | Pass |
| user-stories | Pass | Pass | Pass |
| swift-swiftui | Pass | Pass | Pass |
| design-kit | Pass | Pass | Pass |
| design-system | Pass | Pass | Pass |
| layout-grid | Pass | Pass | Pass |
| improve-architecture | Pass | Pass | Pass |
| os-integrations | Pass | Pass | Pass |
| performance | Pass | Pass | Pass |
| design-from-app | Pass | Pass | Pass |
| app-brief | Pass | Pass | Pass |
| build-and-verify | Pass | Pass | Pass |
| agent-cli | Pass | Pass | Pass |
| improve-loop | Pass | Warn | Pass |

20 of 21 listings are sampled; the research listing carries no skills.sh verdict.

## Limitations

- Snapshot data, verified Nov 20, 2026: 20,910 combined installs across 21 indexed listings; 1,917 GitHub stars; MIT license; last pushed Nov 5, 2026. Counts drift over time.
- The install figures are a skills.sh point-in-time snapshot and drift as the marketplace keeps indexing; treat them as a floor, not a ceiling.
- Only 20 of 21 listings carry skills.sh security verdicts; the research listing has none in the sample.
- The suite requires macOS 26 and Xcode 26, and the clone skill on native apps needs computer use (Claude Pro or Max).
- It is Mac-only: the README points Windows users to BAWA (Build Any Windows App) instead.

## Related

- [REA - Reverse Engineer Anything Skill Setup](/hermes/skills/catalog/rea-setup)
- [SwiftUI Pro - Apple UI Development Skill](/hermes/skills/catalog/twostraws-swiftui-pro-setup)
- [Swift iOS Skills - iOS 26 and SwiftUI Suite Setup](/hermes/skills/catalog/dpearson-swift-ios-skills-setup)
- [Dimillian Skills - Apple Platform Engineering Suite Setup](/hermes/skills/catalog/dimillian-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start every new build with the bama router: it reads the project state and picks the next skill, so you never need to memorize the 21-skill graph.
- Type /bama in Claude Code for the same routing.
- Use the specs/ directory when you have no idea in mind: copy one of the 12 build plans into an empty folder and tell the agent to build it.
- Pick one install route per agent; installing two routes installs every skill twice.
- Run build-and-verify after any UI change so light and dark snapshots catch regressions before you call a change done.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
