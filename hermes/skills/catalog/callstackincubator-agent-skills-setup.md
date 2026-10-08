---
title: "Callstack Agent Skills - React Native Skill Suite Setup"
description: "Setup guide for callstackincubator/agent-skills: official Callstack React Native skills - performance, upgrades, navigation, CI, migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/callstackincubator-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-07"
tags: ["hermes skill", "agent skill", "skill setup", "react native", "mobile development", "callstack"]
---

# Callstack Agent Skills - Setup Guide

**Source:** [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) (1,663⭐, MIT LICENSE; very active - pushed Oct 6, 2026)
**Skill family:** `callstackincubator/agent-skills` (13 SKILL.md files in-repo; 15 indexed listings)
**Combined Installs:** ~80,715 across indexed listings (Oct 7, 2026 snapshot)
**Category:** Mobile Development / React Native
**Quality Tier:** 🟡 Beta (official Callstack incubator org, active since 2018; MIT LICENSE in-repo; very active development; sampled security verdicts predominantly Pass - verified Oct 7, 2026)

Callstack Agent Skills give AI coding assistants practical React Native knowledge drawn from
Callstack's production work on real apps. The suite ships as three plugin bundles -
**Building React Native Apps**, **Testing React Native Apps**, and **Migrating to React Native** -
covering performance profiling and optimization, navigation (React Navigation 7), TV app
development, library authoring with `create-react-native-library`, framework upgrades, CI builds
(downloadable iOS simulator and Android emulator artifacts via GitHub Actions), device automation
and exploratory QA, migration readiness assessment, and incremental brownfield adoption via
`@callstack/react-native-brownfield`. Several skills derive from Callstack's published reference
material, including the "Ultimate Guide to React Native Optimization".

---

## Installation

```bash
# Full suite (all Callstack skills)
npx skills add callstackincubator/agent-skills --skill '*'

# Or pick a single skill
npx skills add callstackincubator/agent-skills --skill react-native-best-practices
```

Claude Code and Codex users can install the three bundles from their plugin marketplaces
(`plugins/building-react-native-apps`, `plugins/testing-react-native-apps`,
`plugins/migrating-to-react-native`). The skills are host-neutral Agent Skills
(`skills/<name>/SKILL.md`) and can be pointed at any host's skill installer.

## Roster - Indexed Skills

| Skill | Bundle | Installs | What It Does |
|---|---|---|---|
| react-native-best-practices | Building | 28,198 | Performance optimization: FPS and re-renders, bundle size, TTI, memory leaks, animations |
| upgrading-react-native | Building | 11,583 | Framework upgrades: Upgrade Helper template diffs, dependency alignment, Expo SDK steps, verification |
| github-actions | Testing | 9,834 | CI workflows producing downloadable iOS simulator and Android emulator build artifacts |
| validate-skills | Tooling | 6,845 | Skill-authoring validator for the repo (lives under `.claude/skills/`) |
| react-native-brownfield-migration | Migrating | 4,760 | Phased adoption of React Native inside existing native iOS and Android apps |
| react-navigation | Building | 3,841 | React Navigation 7 stacks, tabs, drawers, headers, sheets, safe-area behavior |
| create-react-native-library | Building | 3,424 | Standalone libraries and local native modules or views |
| react-native-tv-best-practices | Building | 1,838 | TV focus, remote input, playback, performance, packaging, accessibility |
| assess-react-native-migration | Migrating | 1,718 | Migration audits: path selection and checkpoint definition |
| writing-user-docs | Tooling | 471 | User documentation authoring for the repo |
| react-native-testing | Testing (vendored) | 42 | User-focused tests with React Native Testing Library |
| agent-device | Testing (vendored) | 30 | iOS and Android app flow automation, input, screenshots, logs, UI inspection |
| dogfood | Testing (vendored) | 28 | Exploratory QA, smoke checks, and structured app walkthroughs |

Additional indexed listings not in the current repo tree: `github` (8,096) and
`vercel-react-native-skills` (7) - older index entries kept for install-count continuity.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent-suite packaging pattern** | Three themed bundles built from one company's domain expertise, with verify-oriented pairs and vendored open-source skills - a strong reference for how product teams structure skill libraries |
| **Mobile teams working with AI assistants** | Teams shipping React Native apps get measurement-first performance work, guided upgrades, CI artifact builds, and migration planning from an assistant that knows current framework idioms |
| **Enterprise migration evaluations** | The migration pair (assess plus brownfield) turns "should we adopt React Native?" into an auditable, checkpoint-based plan - useful when operators evaluate mobile stack changes |

## Limitations / Verification

- Verified Oct 7, 2026: 13 `SKILL.md` files via the GitHub trees API on branch `main` (9 first-party under `skills/`, 1 tooling skill under `.claude/skills/`, 3 vendored under `plugins/vendored/`); 1,663 stars; MIT LICENSE in-repo; last pushed Oct 6, 2026; publisher is Callstack's incubator org (`callstackincubator`, created June 2018, 48 public repos, callstack.com).
- First seen in the July 27-28, 2026 sweeps and deferred then as below-floor and platform-specific; re-qualified Oct 7, 2026 at ~80,715 combined listed installs, roughly 4x its July size.
- React Native-specific: useful for RN and mobile teams, not a general-purpose suite. The three vendored skills mirror publications from `callstackincubator/agent-device` and `callstack/react-native-testing-library`.
- Skills operate on live development projects (upgrades, CI workflows, migration steps, device automation). Review commands before running them against production repos or CI secrets.
- No live install test was performed; install counts are the Oct 7, 2026 skills.sh sweep snapshot.

## Security

skills.sh per-skill verdicts (sampled 5 skills, verified Oct 7, 2026) - verdicts vary per skill; check the skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-native-best-practices | Pass | Pass | Pass |
| upgrading-react-native | Pass | Pass | Pass |
| react-navigation | Pass | Pass | Pass |
| react-native-brownfield-migration | Pass | Pass | Pass |
| github-actions | Pass | Warn | Pass |

## Related

- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
