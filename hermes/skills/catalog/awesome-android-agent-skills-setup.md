---
title: "Awesome Android Agent Skills - Compose and Kotlin Setup"
description: "new-silvermoon/awesome-android-agent-skills: 9.9K combined installs. Eighteen Android skills for Compose, coroutines, Gradle and testing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-android-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "android", "kotlin", "jetpack compose"]
---

# Awesome Android Agent Skills - Setup Guide

**Source:** [new-silvermoon/awesome-android-agent-skills](https://www.skills.sh/new-silvermoon/awesome-android-agent-skills) via skills.sh - 9.9K combined installs across 18 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) - 998 stars, Apache-2.0, branch main, last pushed 2026-07-27; 17 `SKILL.md` files laid out as `.github/skills/<category>/<skill>/SKILL.md` across seven category folders (architecture, build_and_tooling, concurrency_and_networking, migration, performance, testing_and_automation, ui), plus an `Agent.md` at the root that the README says every agent reads implicitly

**Category:** Android app development: Jetpack Compose UI, Kotlin coroutines, Gradle build logic, Clean Architecture, performance, testing and migration work

**Quality Tier:** 🟢 Green - every sampled verdict is a Pass on Gen Agent Trust Hub, Socket and Snyk, and the repository is Apache-2.0 with the licence file present

The README frames these as specialised "brains" for AI coding assistants, and the framing is accurate: each skill is a short, rule-shaped document rather than an essay. `compose-ui` states that a composable takes state down and sends events up, that a `modifier` parameter comes first and applies to the root, and that `derivedStateOf` belongs on fast-changing values whose UI only reacts to a threshold. `android-coroutines` opens with NEVER and ALWAYS rules on dispatcher injection, main-safety, `repeatOnLifecycle`, `GlobalScope` and `CancellationException`. An agent that loads these writes code that matches a house style on the first attempt.

The set covers the decisions that a Kotlin project actually turns on. Architecture skills pin the layer boundaries, Hilt annotation placement, the module map and the rule that the domain layer imports no Android framework classes. Build skills turn convention plugins and version catalogs into a concrete `build-logic` layout. Performance skills separate the two bottlenecks that are usually conflated, recomposition in Compose and configuration versus execution time in Gradle. Two migration skills handle the codebases most teams actually have, XML layouts moving to Compose and RxJava chains moving to Coroutines and Flow, with full mapping tables rather than advice.

There is also an `Agent.md` at the root, which the README treats as the foundation: every agent working in the project reads it for architecture, minimum SDK and testing philosophy before any skill activates. That file is part of the install, not an afterthought.

## Installation

The README documents a manual install rather than a CLI. The instructions are to copy the `.github/skills/` folder into the root of your project, copy `Agent.md` alongside it, then verify that the result is `.github/skills/<category>/<skill>/SKILL.md`. There is no `npx skills add` line and no plugin manifest, so the standard CLI form does not apply to this repository. The clone below is our addition to their copy steps:

```bash
git clone --depth 1 https://github.com/new-silvermoon/awesome-android-agent-skills.git /tmp/awesome-android-agent-skills
mkdir -p .github/skills
cp -r /tmp/awesome-android-agent-skills/.github/skills/. .github/skills/
cp /tmp/awesome-android-agent-skills/Agent.md .
```

The README calls `.github/skills/` the industry standard location and aims it at VS Code and GitHub Copilot, which is why the category folders matter: the same skill names would collide in a flat directory. For a Hermes profile the same files go into the profile skills directory, keeping the category level:

```bash
cp -r /tmp/awesome-android-agent-skills/.github/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Because the install is a copy and the README tracks nothing by version, there is no update path. Re-run the clone and copy when you want a newer tree.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| android-testing | 847 | Unit, Hilt integration and Roborazzi screenshot tests: the `libs.versions.toml` entries, a screenshot test example, and the Gradle commands to record and verify. |
| gradle-build-performance | 788 | Diagnosing slow builds by phase, reading build scans, and twelve named optimisations from configuration cache to kapt migration. |
| compose-ui | 740 | Composable design rules: state hoisting, modifier ordering, `remember` and `derivedStateOf`, theming from `MaterialTheme`, and previews for every public composable. |
| android-gradle-logic | 720 | Convention plugins and version catalogs in a `build-logic` composite build, so module build files stop repeating Compose, Kotlin and Hilt setup. |
| android-architecture | 680 | Clean Architecture layer boundaries, Hilt annotation and module rules, and the `:core:*` and `:feature:*` module map for a multi-module app. |
| kotlin-concurrency-expert | 666 | Reviewing coroutine code against symptoms: ANR, memory leak, race, wrong state, then applying the smallest safe fix. |
| compose-performance-audit | 574 | Recomposition storms, unstable lazy list keys, heavy work in composition, and the Layout Inspector and Perfetto workflow to prove it. |
| android-viewmodel | 556 | ViewModel state design with `StateFlow` for UI state and `SharedFlow` for one-off events, lifecycle-aware collection, and Kotlin explicit backing fields. |
| android-emulator-skill | 556 | Driving a device from scripts: screen mapping, semantic navigation by text or resource id, gestures, log monitoring, builds and AVD lifecycle. |
| android-coroutines | 548 | Authoritative coroutine rules: injected dispatchers, main-safe suspend functions, `repeatOnLifecycle`, no `GlobalScope`, rethrown cancellation. |
| android-accessibility | 530 | Auditing content descriptions, 48dp touch targets, 4.5:1 contrast, focus order, merged semantics and heading traversal. |
| android-data-layer | 514 | Repository as single source of truth, Room and Retrofit wiring, stale-while-revalidate reads and outbox-style writes. |
| android-retrofit | 479 | Retrofit service definitions, path and query handling, body and multipart forms, header control, and a Hilt network module. |
| coil-compose | 447 | Image loading in Compose: `AsyncImage` as the default, when `rememberAsyncImagePainter` is a trap, and avoiding `SubcomposeAsyncImage` in lists. |
| compose-navigation | 436 | Navigation 3 in Compose: serializable navigation keys, a state back stack, `NavDisplay`, argument passing and ViewModel scoping. |
| xml-to-compose-migration | 435 | Converting XML layouts to Compose with container, widget and attribute mapping tables, plus state and click listener migration. |
| rxjava-to-coroutines-migration | 333 | Converting RxJava types, subjects, schedulers and operators to coroutines and Flow, with the execution order for a migration. |
| navigation3 | 99 | Indexed listing with no directory in the current tree; the Navigation 3 guidance ships inside `compose-navigation`, whose `SKILL.md` declares `name: navigation3`. |

No indexed listings fall below the threshold; all 18 appear above.

## Why This Matters for Hermes Agents

An agent writing Kotlin without guidance produces code that compiles and still fights the project. It hoists state into the wrong place, hardcodes a dispatcher, collects a flow outside a lifecycle, exposes a mutable state holder, and puts a `SubcomposeAsyncImage` inside a lazy list. Each of those is a real defect that survives review because it runs, and each is answered by a single rule in this pack.

The rules are written in the imperative, which is what a model follows best. `android-coroutines` does not explain structured concurrency in general, it says never hardcode a dispatcher, always inject one, never expose `MutableStateFlow`, and rethrow `CancellationException` inside a generic catch. That brevity is the point: a skill that fits in a screen of context gets loaded and applied, while a long tutorial gets skimmed.

The build and performance skills are where the time savings are largest. `gradle-build-performance` insists on measuring a baseline, changing one thing and re-measuring in a build scan, which is the opposite of the batch of speculative edits an agent will otherwise make. `compose-performance-audit` refuses to guess from symptoms and asks for a Layout Inspector count or a Perfetto trace, which converts a vague complaint about jank into a specific defect.

The migration skills matter because most Android codebases are mixed. A team with XML screens and RxJava repositories cannot adopt a Pure Compose doctrine, and having explicit mapping tables for `RecyclerView` to `LazyColumn`, `switchMap` to `flatMapLatest` and `Schedulers.io()` to `Dispatchers.IO` makes an incremental change reviewable.

## Usage

| You say | What happens |
|---|---|
| "This screen recomposes on every scroll" | `compose-performance-audit` identifies unstable parameters, missing keys or a heavy computation in composition, and asks for a Layout Inspector count before recommending the fix. |
| "Our builds take nine minutes in CI" | `gradle-build-performance` separates configuration from execution time in a build scan and applies one optimisation at a time; if the cause is repeated module config, `android-gradle-logic` moves it into a convention plugin. |
| "Refactor this ViewModel" | `android-viewmodel` rewrites it around a single immutable UI state, a `SharedFlow` for events and an explicit backing field, with lifecycle-aware collection at the screen. |
| "Convert this RecyclerView screen to Compose" | `xml-to-compose-migration` maps the layout and widgets, migrates the state and listeners, then checks accessibility and configuration change behaviour. |
| "Our coroutine code leaks and I get ANRs" | `kotlin-concurrency-expert` triages the scope and dispatcher, replaces `GlobalScope` with a lifecycle scope, moves work with `withContext` and keeps the change minimal. |
| "Review this Composable for accessibility" | `android-accessibility` checks content descriptions, touch target size, contrast, focus order and headings, and returns a per-item finding list. |
| "Add an onboarding flow with three screens" | `compose-ui` and `compose-navigation` produce stateless composables with a state back stack, serializable keys and view model scoping per entry. |

## Verification

The raw path for the Compose UI skill returned HTTP 200 on branch main when this guide was written on 2026-11-01. Note the category folder in the path, which is what this repository uses instead of a flat `skills/` tree:

```bash
curl -sL -o /dev/null -w "%{http_code} compose-ui\n" \
  https://raw.githubusercontent.com/new-silvermoon/awesome-android-agent-skills/main/.github/skills/ui/compose-ui/SKILL.md
```

Expect `200`. After the clone, confirm the category structure and the skill count:

```bash
find /tmp/awesome-android-agent-skills/.github/skills -name SKILL.md | wc -l
ls /tmp/awesome-android-agent-skills/.github/skills | wc -l
head -4 /tmp/awesome-android-agent-skills/.github/skills/ui/compose-ui/SKILL.md
```

The first count should print 17 and the second 7, one per category folder. The header should show `name: compose-ui` with a `description:` line before the closing frontmatter. Confirm that `Agent.md` is present at the repository root as well, since the README treats it as the context every skill assumes.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| android-testing | Pass | Pass | Pass |
| gradle-build-performance | Pass | Pass | Pass |
| compose-ui | Pass | Pass | Pass |

All three sampled verdicts are clean and the repository is Apache-2.0 with the licence file in place, which is the most permissive position in this catalog's tier scale. Sixteen of the seventeen skill files are instructions only, with no scripts, no dependencies and no network calls, so the review question is code quality rather than execution risk.

The exception is `android-emulator-skill`, which is built around a set of Python and shell helpers (`emu_health_check.sh` or `.ps1`, `app_launcher.py`, `screen_mapper.py`, `navigator.py`, `gesture.py`, `keyboard.py`, `log_monitor.py`, `build_and_test.py`, `emulator_manage.py`) that drive adb, Gradle and the emulator. That is genuine execution surface with device control, so read the scripts before the first run and confirm the `scripts/` directory exists in your clone, because the tree listing records only `SKILL.md` paths per skill.

`Agent.md` is the other item to review, for a different reason. The README says every agent reads it implicitly before any skill activates, which gives one markdown file repo-wide authority over architecture, minimum SDK and testing rules. Treat it as a configuration file with the same review requirements as a build script, and keep it aligned with the project it sits in rather than copying it blindly between repositories.

## Limitations

- Snapshot data, verified 2026-11-01: 9,948 combined installs across 18 indexed listings; 998 GitHub stars; Apache-2.0; last pushed 2026-07-27. Counts drift over time.
- The index lists 18 skills while the tree holds 17 `SKILL.md` files. The extra listing is `navigation3` at 99 installs, which has no directory: the Navigation 3 content lives in `.github/skills/ui/compose-navigation/SKILL.md`, whose frontmatter declares `name: navigation3`, so the same guidance is indexed twice at 436 and 99 installs.
- There is no CLI or versioned install. The README documents copying two paths into a project, which means updates are manual re-copies and there is no lockfile to record which revision a project uses.
- Version details inside the skills will age. The navigation skill pins Navigation 3 at `1.0.0-alpha08` with a Kotlin 2.2.0 serialization plugin, and the ViewModel skill treats Kotlin 2.3 explicit backing fields as experimental with 2.4 as the stable target, so check current releases before following the snippets literally.
- The emulator skill depends on a local Android SDK, a running AVD, `adb` and Python 3, and it is the only skill that executes anything. The other sixteen are inert instructions.
- Last pushed 2026-07-27, about three months before this snapshot, and Android tooling moves quickly. Verify Android Gradle Plugin and Compose versions against your project before applying the Gradle advice.

## Related

- [Android Skills - Play Policy and App Quality Setup](/hermes/skills/catalog/android-skills-setup)
- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)
- [Harmony Next Skills - Setup Guide](/hermes/skills/catalog/harmony-next-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `Agent.md` with the skills or the pack is half-loaded. The README treats it as the context every skill assumes, and without it an agent applies local rules to a project whose conventions it never read.
- Keep the category folders. The install target is `.github/skills/`, and flattening `architecture` and `ui` into one directory puts similarly named skills side by side with no namespace.
- Load `kotlin-concurrency-expert` for bug reports and `android-coroutines` for new code. One is a remediation workflow for a symptom, the other is a rule set to write against, and swapping them wastes a step.
- Ask `compose-performance-audit` for evidence before it edits. It is written to demand a Layout Inspector count or Perfetto trace, and holding it to that stops a cosmetic refactor being sold as a performance fix.
- Pair `xml-to-compose-migration` with `android-testing`. A migration is only done when the screenshot tests still pass, and the Roborazzi setup in the testing skill is what makes that check cheap.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
