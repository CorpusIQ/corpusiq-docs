---
title: "Flutter AI Rules - Dart and Firebase Setup"
description: "evanca/flutter-ai-rules: 8.1K combined installs across 37 listings, 36 Flutter and Dart skills for architecture, state, tests and Firebase"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/flutter-ai-rules-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "flutter", "dart", "firebase", "mobile"]
---

# Flutter AI Rules - Setup Guide

**Source:** [evanca/flutter-ai-rules](https://www.skills.sh/evanca/flutter-ai-rules) via skills.sh - 8.1K combined installs across 37 indexed listings (8,083 exact); first seen Mar 11, 2026 (Nov 10, 2026 sweep)
**GitHub:** 670 stars, MIT license, `main` branch, last pushed 2026-11-05, 36 `SKILL.md` files among 168 blobs, one directory per skill under `skills/<name>/SKILL.md`, with plugin manifests in `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/` and `.agents/plugins/` alongside a root `plugin.json`
**Category:** Flutter development: state management, architecture, testing, accessibility and Firebase services
**Quality Tier:** 🟢 Production ready - all 25 sampled listings pass Agent Trust Hub, Socket and Snyk, the repository is MIT licensed and was pushed 2026-11-05.

This is a documentation-derived collection rather than a vendor kit. Every skill is built from official Flutter, Dart, Firebase and package documentation, and the README is explicit that it carries no personal preferences and no invented conventions. It started publishing in 2025 and the skills.sh listings first appeared Mar 11, 2026. 36 skills, 670 stars, 8,083 combined installs across 37 indexed listings.

The coverage is wider than the name suggests. `rules` in the title is legacy: the repository now ships `skills/` as the primary distribution, plus `rules/` (six foundation files) and `combined/` (seven topic bundles in full and `__under_6K` variants) for tools that cannot read a `SKILL.md` at all. GitHub Copilot is the named case. It does not read `SKILL.md`, so it takes a `combined/` bundle in `.github/copilot-instructions.md` or `rules/` files in `.github/instructions/` with `applyTo: "**/*.dart"` frontmatter.

The skill set splits into foundations (best practices, Effective Dart, Dart 3 language features, app architecture, feature-first folders, layout errors, pre-caching), state management (Bloc, Riverpod, Provider, ChangeNotifier), testing and review (unit, widget and golden tests, Mockito, Mocktail, Patrol end-to-end, code review), Firebase (16 listings, one per product) and shipping concerns (accessibility, inclusive design, RevenueCat testing, store listing assets).

That structure is the point. The state-management skills are deliberately plural and the README's own note says skills can contradict each other because their sources do, which is what you want from a documentation mirror and what you have to manage when an agent loads two of them at once.

## Installation

The README's primary route is the Skills CLI, which discovers the packages under `skills/` and installs them for supported agents:

```bash
npx skills add evanca/flutter-ai-rules

# browse the set, or install one skill
npx skills add evanca/flutter-ai-rules --list
npx skills add evanca/flutter-ai-rules --skill flutter-best-practices
```

This route needs Node 22.20 or newer. On older versions it exits with a `SyntaxError` about the missing `styleText` export before it does anything, which reads like a repository problem rather than a Node version problem. The plugin and manual routes below work on any Node version or none.

The repository is also a plugin marketplace. Claude Code:

```
/plugin marketplace add evanca/flutter-ai-rules
/plugin install flutter-ai-skills@flutter-ai-rules
```

Codex:

```bash
codex plugin marketplace add evanca/flutter-ai-rules
codex plugin add flutter-ai-skills@flutter-ai-rules
```

Cursor takes `/add-plugin` inside the editor, or the repository URL as a team marketplace under Dashboard, Settings, Plugins, Import from Repo. Antigravity installs from a clone: `git clone --depth 1 https://github.com/evanca/flutter-ai-rules.git`, then `agy plugin install ./flutter-ai-rules`. For any other agent, including Hermes, copy or symlink a skill folder into the directory that agent scans (`.claude/skills/`, `.cursor/skills/`, `.codex/skills/`, `.agents/skills/`, `.windsurf/skills/`), or vendor the whole set into the project:

```bash
git clone --depth 1 https://github.com/evanca/flutter-ai-rules.git temp_repo && mkdir -p .skills && cp -r temp_repo/skills/* .skills && rm -rf temp_repo
```

With a vendored `.skills/` folder a skill can also be named explicitly: "Read `@.skills/bloc/SKILL.md` and create test coverage for the new methods." The plugin install namespaces the skills instead, so Claude Code loads them as `flutter-ai-skills:bloc`, `flutter-ai-skills:riverpod` and so on.

## What It Provides

Twenty-five of the 37 indexed listings clear the 200-install threshold and appear below with their exact counts:

| Skill | Installs | Use For |
|---|---|---|
| riverpod | 312 | Riverpod providers, combining requests, state disposal, arguments, side effects and provider tests. |
| flutter-errors | 289 | Layout and runtime errors: RenderFlex overflow, unbounded constraints, RenderBox not laid out, setState during build. |
| effective-dart | 287 | Dart style, naming, doc comments, import order and type annotations. |
| flutter-best-practices | 264 | General Flutter and Dart work: screens, features, project structure, state, widgets, repositories and tests. |
| code-review | 263 | Reviewing a PR, MR, branch or diff, auditing changed files and checking code quality. |
| flutter-app-architecture | 261 | Layered scaffolding, view models and repositories, dependency injection, unidirectional data flow in MVVM. |
| architecture-feature-first | 258 | Feature folder structure, repositories and services per feature, and which layer owns logic. |
| bloc | 255 | Cubit and Bloc authoring, sealed state classes and status enums, BlocBuilder, BlocListener, BlocProvider, bloc tests. |
| dart-3-updates | 252 | Switch expressions, records versus classes, patterns, destructuring and modernising pre-Dart-3 code. |
| testing | 251 | Unit, widget and golden tests, flaky test fixes, coverage and choosing a test type. |
| firebase-messaging | 235 | Cloud Messaging setup, permissions and tokens, foreground and background notification taps, HTTP v1 dispatch. |
| patrol-e2e-testing | 231 | End-to-end tests that touch native permissions and system dialogs, with UI regression capture (Patrol 4.x). |
| accessibility | 228 | WCAG, screen readers, keyboard navigation, focus order, contrast, alt text, captions and target sizes. |
| provider | 226 | Provider consumption, rebuild optimisation, ProxyProvider and migration off deprecated providers. |
| flutterfire-configure | 224 | Adding Firebase to a Flutter project, running `flutterfire configure`, initialising Firebase in `main.dart`, multiple flavors. |
| flutter-pre-caching | 223 | Preloading fonts, asset and network images, Lottie and Rive animations, local JSON and config, Flutter Web startup. |
| mocktail | 222 | Mocks without code generation, stubbing, interaction verification, fallback values, mocks versus fakes. |
| flutter-change-notifier | 221 | ChangeNotifier models, providing them to the tree, consuming state with Consumer or `Provider.of`, rebuilds. |
| mockito | 219 | Generated mocks, stubbing, verification, argument capture, mocks versus fakes. |
| inclusive-design | 216 | Localisation, global name and address forms, low-end devices, slow or metered networks, first-time users. |
| firebase-crashlytics | 213 | Fatal and non-fatal crash reporting, isolate and async exceptions, custom reports, obfuscated symbol upload. |
| firebase-auth | 213 | Auth setup, auth state, email and password or social sign-in, auth errors, user management. |
| firebase-cloud-firestore | 211 | Firestore schema design, CRUD, listeners, pagination, indexes, offline persistence and security rules. |
| firebase-analytics | 206 | Event logging, user properties, default event parameters, funnels and screen-view tracking. |
| flutter-use-column-row-first | 203 | Choosing Row, Column, Expanded, Flexible and Spacer for responsive layouts before fixed sizes or coordinates. |

The remaining 12 indexed listings range from 120 to 199 installs: firebase-cloud-functions (199) and firebase-app-check (195) at the top, through firebase-remote-config, firebase-storage, firebase-database, firebase-in-app-messaging, firebase-ai, firebase-data-connect, developing-genkit-dart and revenuecat-testing, down to generate-images-with-firebase-ai (124) and store-listing-assets (120).

Read the table as career paths rather than a flat list. Four state-management skills compete for the same trigger, two mocking skills solve the same problem with and without code generation, and `accessibility` explicitly defers language, culture and device concerns to `inclusive-design`. The Firebase block is the deepest part of the set: 16 listings cover everything from `flutterfire configure` through Auth, Firestore, Realtime Database, Storage, Functions, Remote Config, App Check, Analytics, Crashlytics, FCM, in-app messaging, Data Connect, Gemini text and image generation, and Genkit agents.

## Why This Matters for Hermes Agents

Flutter advice ages badly. Null safety, records and patterns, sealed classes and `switch` expressions each changed how idiomatic Dart looks, and most blog content an agent has seen predates them. A skill file that tracks the official docs is the cheapest way to stop an agent writing Dart 2 patterns into a Dart 3 codebase, and the README states the content is re-fetched from upstream on a schedule rather than frozen at authoring time.

The descriptions are written as triggers, not summaries. Every one of the sampled descriptions begins "Use when", which is what a skill router matches against, so Firebase Auth guidance arrives when the task mentions auth rather than when someone remembers to mention the rules file. That is the difference between a rules folder nobody loads and guidance that shows up in context.

The breadth is what makes a single install worth it. A session that adds social sign-in, moves a screen to Riverpod and then asks for widget tests stays inside one collection that shares vocabulary about layers, view models and repositories, instead of mixing three publishers with three opinions about where business logic lives.

## Usage

| You say | What happens |
|---|---|
| "Add Google sign-in to the profile screen" | firebase-auth loads with flutter-app-architecture and wires auth state, error handling and the sign-in call to the layer that should own it. |
| "Move this screen to Riverpod" | riverpod covers providers, disposal and passing arguments; provider stays out of the way unless the project already uses it. |
| "Why does this Row overflow?" | flutter-errors names the RenderFlex overflow and unbounded constraint cases and the fixes; flutter-use-column-row-first supplies the responsive layout order. |
| "Review this PR" | code-review audits the diff, and effective-dart plus flutter-best-practices supply the rules it applies. |
| "Write tests for the new cubit" | bloc writes the bloc test, testing picks between unit and widget coverage, mocktail or mockito supplies the dependencies. |
| "Set up push notifications" | flutterfire-configure runs first, then firebase-messaging handles permissions, tokens and notification taps. |
| "Our low-end Android users churn" | inclusive-design covers low-end devices and metered networks, while accessibility handles WCAG, focus order and target sizes. |

## Verification

Every listing resolves to a raw `SKILL.md` one directory below `skills/` on `main`. This request returns 200 and is the file to read before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/evanca/flutter-ai-rules/main/skills/riverpod/SKILL.md | head -6
```

The frontmatter opens with `name: riverpod` and the description `Use when setting up providers, combining requests, managing state disposal, passing arguments, performing side effects, or testing providers (Riverpod).`, followed by `license: MIT` and the instruction body. The same pattern holds across the set, for example `skills/bloc/SKILL.md` and `skills/firebase-auth/SKILL.md`.

For a vendored install, confirm a skill landed with its `SKILL.md` intact:

```bash
test -f .skills/bloc/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| riverpod | Pass | Pass | Pass |
| flutter-errors | Pass | Pass | Pass |
| effective-dart | Pass | Pass | Pass |
| flutter-best-practices | Pass | Pass | Pass |
| code-review | Pass | Pass | Pass |
| flutter-app-architecture | Pass | Pass | Pass |
| architecture-feature-first | Pass | Pass | Pass |
| bloc | Pass | Pass | Pass |
| dart-3-updates | Pass | Pass | Pass |
| testing | Pass | Pass | Pass |
| firebase-messaging | Pass | Pass | Pass |
| patrol-e2e-testing | Pass | Pass | Pass |
| accessibility | Pass | Pass | Pass |
| provider | Pass | Pass | Pass |
| flutterfire-configure | Pass | Pass | Pass |
| flutter-pre-caching | Pass | Pass | Pass |
| mocktail | Pass | Pass | Pass |
| flutter-change-notifier | Pass | Pass | Pass |
| mockito | Pass | Pass | Pass |
| inclusive-design | Pass | Pass | Pass |
| firebase-crashlytics | Pass | Pass | Pass |
| firebase-auth | Pass | Pass | Pass |
| firebase-cloud-firestore | Pass | Pass | Pass |
| firebase-analytics | Pass | Pass | Pass |
| flutter-use-column-row-first | Pass | Pass | Pass |

All 25 sampled listings pass all three scanners with no warn and no fail. Verdicts were sampled for the 25 listings in the table above, so the 12 below the threshold were not scored here; check their individual pages if you install one of them.

A clean scan means the skill text is not doing anything unexpected. It does not review the app code an agent writes from it, and it does not cover a Firebase service you then wire up. The security decisions that matter in this stack are elsewhere: Firestore rules, App Check enforcement, API key restrictions and the scopes you grant the CLI, none of which a skill scanner evaluates.

## Limitations

- Snapshot data, verified 2026-11-10: 8,083 combined installs across 37 indexed listings; 670 GitHub stars; MIT license; last pushed 2026-11-05. Counts drift over time.
- The index outruns the tree: 37 indexed listings against 36 skill directories. store-listing-assets carries 120 installs but has no directory at `main`; its `skills/store-listing-assets/SKILL.md` path returns 404, so only the other 36 can be installed from `skills/`.
- The `npx skills add` route needs Node 22.20 or newer. Older versions fail with a `styleText` export error before installing anything, which is easy to misread as a repository fault.
- The skills contradict each other by design. The README says so directly: if one package recommends a folder layout and another recommends a different one, both appear. An agent loading bloc and riverpod together will blend them unless the project has chosen.
- GitHub Copilot cannot use any of this. It has no repo-level `SKILL.md` support, so it needs a `combined/` bundle in `.github/copilot-instructions.md`, `rules/` files in `.github/instructions/`, or a root `AGENTS.md`.
- Guidance only: nothing here runs `flutter analyze`, the test suite or a build, so a skill can describe the right pattern while the code it produced fails to compile.

## Related

- [Flutter Agent Plugins - Official Flutter Skills Setup](/hermes/skills/catalog/flutter-agent-plugins-setup)
- [Dart Language Skills - Official Dart Team Suite Setup](/hermes/skills/catalog/dart-lang-skills-setup)
- [firebase Skills](/hermes/skills/catalog/firebase)

## Pro Tips

- Run `--list` before installing. 36 skills is a lot of trigger surface, and the descriptions are specific enough that the list doubles as an index of what the agent can be asked to do.
- Install only the state-management skill the project uses. Bloc, Riverpod, Provider and ChangeNotifier all claim the same territory, and four competing sets of guidance produce a diff that mixes patterns.
- Pair `firebase-auth` with `flutter-app-architecture` on a new feature. Auth state is where an agent most often puts logic in the widget instead of the view model, and the architecture skill is what stops it.
- Vendor `.skills/` into the repository when the team is mixed. Everyone then reads the same text at the same version, and CI can reference `@.skills/testing/SKILL.md` explicitly.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
