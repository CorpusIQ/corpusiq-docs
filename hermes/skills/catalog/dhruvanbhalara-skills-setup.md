---
title: "Flutter and Dart Skills - Architecture and Testing"
description: "dhruvanbhalara/skills: 43 Flutter, Dart and GitHub workflow skills for professional development - 6.6K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dhruvanbhalara-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "flutter", "dart", "mobile development"]
---

# Flutter and Dart Skills - Setup Guide

**Source:** [dhruvanbhalara/skills](https://www.skills.sh/dhruvanbhalara/skills) via skills.sh - 6.6K combined installs across 63 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** [dhruvanbhalara/skills](https://github.com/dhruvanbhalara/skills) - 30 stars, MIT licence, main branch, last pushed Aug 30, 2026. Skills live under `skills/<language>/<name>/SKILL.md` (43 directories: 14 Dart, 25 Flutter, 4 GitHub).
**Category:** Flutter / Dart Mobile Development
**Quality Tier:** 🟢 Green - all 16 sampled verdicts Pass; MIT licence.

This is a collection of 43 specialized coding-agent skills for professional Flutter and Dart development, with a published documentation site and project-level guidance files (`.github/copilot-instructions.md` and `AGENTS.md`) for agents such as Antigravity, Claude Code, Cursor and Copilot. The library spans three areas: Dart fundamentals and tooling, Flutter architecture and UI work, and GitHub workflows for commits, pull requests, changelogs and CI/CD.

The skills are structured as small, self-contained guides an agent can invoke by task, so the repository reads less like a monolith and more like a playbook: build flavors, state management with BLoC, Pigeon native bridges, test pyramids, and conventional commits each get their own file.

## Installation

Add all skills to your workspace:

```bash
npx skills add dhruvanbhalara/skills
```

Add a specific skill:

```bash
npx skills add dhruvanbhalara/skills --skill flutter-spm
```

For agents that support project-level guidance (GitHub Copilot or Codex), the repository also ships `.github/copilot-instructions.md` and `AGENTS.md` to copy into your project.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| flutter-ui | 454 | Design tokens, themes, reusable components and accessible widget layouts |
| flutter-dio | 378 | HTTP clients with Dio: interceptors, retry logic and response caching |
| flutter-security | 371 | AES-256-GCM encryption, secure storage and biometric auth gates |
| flutter-firebase | 358 | Firebase Authentication, Firestore, Messaging, Crashlytics and Analytics |
| flutter-debugging | 355 | Error boundaries, Crashlytics, logging and layout diagnosis |
| flutter-testing | 299 | Test pyramids, golden variants and state matrix testing |
| dart-optimization | 298 | CPU hot paths, allocation profiling and static typing performance |
| dart-memory | 283 | Memory leaks, GC overhead and stream/listener disposal |
| flutter-code-gen | 282 | build_runner codegen for immutable models, JSON serialization and DI |
| flutter-config | 276 | Build flavors, dart-define-from-file and stage-specific credentials |
| flutter-native | 275 | MethodChannel, EventChannel and Pigeon native bindings |
| dart-logic-patterns | 275 | Business logic, data structures and Dart 3 pattern matching |
| flutter-bloc | 262 | Sealed BLoC classes, injectable DI and GoRouter listeners |
| github-actions | 220 | CI/CD pipelines for testing, static analysis and releases |
| flutter-architecture | 153 | Clean Architecture with BLoC (indexed listing; no directory in the current tree) |
| flutter-isar | 152 | Isar NoSQL persistence with schemas and reactive queries |
| flutter-bloc-forms | 151 | Form state, input validation and asynchronous submission |
| git-commit | 134 | Conventional Commits and atomic commit hygiene |

The remaining 45 indexed listings range from 1 to 115 installs.

## Why This Matters for Hermes Agents

Flutter and Dart have a specific shape of quality problems: render-flex overflows, GC pressure, codegen drift, and CI pipelines that check nothing. This library encodes those fixes as discrete skills an agent can invoke by task, which fits an agent's tool-calling pattern better than a long prose style guide. The GitHub skills extend the same discipline to commits, pull requests, changelogs and Actions, closing the loop between writing code and shipping it. Each skill is a small self-contained guide, so an agent can load just the one it needs rather than a whole playbook, and the project ships AGENTS.md and Copilot instructions for frameworks that read project-level guidance. The skills target assistants that run inside a project, which is exactly where Flutter code actually gets written.

## Usage

| You say | What happens |
|---|---|
| Set up Firebase auth in my Flutter app | The flutter-firebase skill configures Auth, Firestore, Messaging and Analytics |
| My app overflows on small screens | The debugging and layout skills diagnose the RenderFlex overflow and fix the layout |
| Add end-to-end tests | The integration-test skill sets up device, web and Firebase Test Lab runs |
| Wire a native iOS API from Dart | The flutter-native skill builds a Pigeon or MethodChannel bridge |
| Encrypt local data at rest | The security skill applies AES-256-GCM and secure credential storage |
| Write a Conventional Commits message | The git-commit skill produces an atomic, spec-compliant commit |
| Build a CI pipeline that runs format checks and tests | The github-actions skill scaffolds the workflow file |

## Verification

```bash
# after install, confirm the skill files landed
ls .skills/dhruvanbhalara/skills/
# review one skill's instructions before relying on it
curl -sL https://raw.githubusercontent.com/dhruvanbhalara/skills/main/skills/dart/dart-add-unit-test/SKILL.md
```

The raw SKILL.md URL above was probed Nov 19, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| flutter-ui | Pass | Pass | Pass |
| flutter-dio | Pass | Pass | Pass |
| flutter-security | Pass | Pass | Pass |
| flutter-firebase | Pass | Pass | Pass |
| flutter-debugging | Pass | Pass | Pass |
| flutter-testing | Pass | Pass | Pass |
| dart-optimization | Pass | Pass | Pass |
| dart-memory | Pass | Pass | Pass |
| flutter-code-gen | Pass | Pass | Pass |
| flutter-config | Pass | Pass | Pass |
| flutter-native | Pass | Pass | Pass |
| dart-logic-patterns | Pass | Pass | Pass |
| flutter-bloc | Pass | Pass | Pass |
| github-actions | Pass | Pass | Pass |
| flutter-architecture | Pass | Pass | Pass |
| flutter-isar | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 19, 2026: 6,607 combined installs across 63 indexed listings; 30 GitHub stars; MIT licence; last pushed Aug 30, 2026. Counts drift over time.
- The install index outruns the tree: 63 listings are indexed but the repository ships 43 skill directories. Twenty indexed names (including flutter-architecture, flutter-localization, dart-testing and 17 category-style names such as testing, state-management and forms) have no matching directory in the current tree.
- flutter-architecture appears in the table above at 153 installs but has no directory in the tree; treat it as an index-only listing.
- The lower tail mixes concrete skills (dart-tooling, flutter-spm, changelog-writing) with generic category labels (security, localization, networking) that look like landing-page tags rather than shipped skills.
- Only 16 of 63 listings have skills.sh verdicts; the remaining 47 are unverified on that platform.

## Related

- [Flutter Agent Plugins - Official Flutter Skills Setup](/hermes/skills/catalog/flutter-agent-plugins-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Prefer the concrete skills (flutter-dio, flutter-isar, flutter-bloc) over the generic category labels in the tail; the concrete ones are the shipped guides.
- Copy `AGENTS.md` and `.github/copilot-instructions.md` into projects where the agent reads project-level guidance.
- Use `--skill` to pull one skill at a time so the whole 43-skill library does not sit in the workspace.
- Pair `flutter-native` with `flutter-security` when bridging native code that handles credentials, so the bridge does not weaken the encryption gate.
- Run the test-skills sequence (unit, widget, integration) together; they share the same pyramid and naming conventions.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
