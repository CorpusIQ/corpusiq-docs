---
title: "MAD Agents Skills - Dart and Flutter Suite Setup"
description: "madteacher/mad-agents-skills: 24.5K combined installs. Eleven MIT skills for Flutter architecture, animation, navigation, Drift and AGENTS.md."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mad-agents-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "flutter", "dart", "mobile"]
---

# MAD Agents Skills - Setup Guide

**Source:** [madteacher/mad-agents-skills](https://www.skills.sh/madteacher/mad-agents-skills) via skills.sh - 24.5K combined installs across 11 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [madteacher/mad-agents-skills](https://github.com/madteacher/mad-agents-skills) - 111 stars, MIT (`LICENSE`, copyright 2026 Stanislav Chernyshev), branch main, last pushed 2026-05-01; 11 skill directories at the repository root, each with a `SKILL.md`, a `references/` folder of 2 to 7 topic files, and `assets/` holding Dart examples and templates, one of them with a `scripts/` folder, 95 files in all with an English and a Russian README

**Category:** Dart and Flutter engineering knowledge for agents: architecture, animation, adaptive layout, navigation, persistence, networking, localization and testing

**Quality Tier:** 🟢 Green - all nine sampled verdicts across three listings pass on Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT licence file

MAD Agents Skills is maintained by Stanislav Chernyshev, who publishes as MADTeacher, and it packages Dart and Flutter expertise in the Agent Skills format. The eleven skills sit at the repository root rather than under a `skills/` folder, which is the first practical detail: a manual install has to name each directory. Every skill follows the same shape, a `SKILL.md` with a trigger-heavy description, a `references/` folder of topic documents, and `assets/` with Dart code examples that can be pasted into a project.

The suite is not only about widgets. `flutter-architecture` covers MVVM, layered UI and data boundaries, dependency injection and the Result and Command patterns; `flutter-testing` covers unit, widget and integration tests plus golden and accessibility checks; `flutter-drift` and `dart-drift` split database work between Flutter and plain Dart; and `agents-md-generator` is stack-agnostic, producing a root AGENTS.md of 60 lines or fewer with nested module files of 40 or fewer. Usage is heavily concentrated: `flutter-animations` alone accounts for 15,490 of the 24,479 total installs.

## Installation

The README documents compatibility rather than a command: it states that the skills work in any assistant that reads the Agent Skills format, and names Claude and Cursor as examples. The install routes below use the skills CLI and a plain clone:

```bash
# the whole suite
npx skills add madteacher/mad-agents-skills

# a single skill
npx skills add madteacher/mad-agents-skills --skill flutter-animations
```

```bash
git clone --depth 1 https://github.com/madteacher/mad-agents-skills.git /tmp/mad-agents
cp -r /tmp/mad-agents/flutter-architecture ~/.hermes/profiles/corpusiq/skills/
```

Copy the whole directory. The references are the substance: `flutter-testing` ships six topic files covering unit, widget, integration, plugin and mock testing plus common errors, and `flutter-drift` ships seven covering setup, tables, queries, writes, streams, migrations and the Flutter UI layer. A copy of `SKILL.md` alone leaves the agent with headings and no detail.

Because the directories are at the root, there is no parent `skills/` folder to copy wholesale without pulling in the README, the licence and the Russian translation. Name the skills you want.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| flutter-animations | 15,490 | Implicit and explicit animations, Hero transitions, staggered motion, springs, reduced motion and lifecycle bugs. |
| flutter-adaptive-ui | 2,011 | Breakpoint-driven layouts for tablet, desktop, web, foldables and mixed input, with Capability and Policy patterns. |
| flutter-architecture | 1,725 | MVVM, layer boundaries, feature-first structure, repositories, DI and offline-first flows. |
| flutter-testing | 1,511 | Unit, widget and integration tests, mocks, goldens, CI commands and pump or finder failures. |
| flutter-networking | 726 | HTTP and WebSocket clients, token refresh, retries, JSON parsing, caching and background isolates. |
| flutter-drift | 679 | Drift persistence in Flutter: generated tables, typed queries, streams, migrations and web assets. |
| flutter-navigation | 595 | Navigator and Router API, go_router, guards, shell routes, deep links and web URL strategy. |
| flutter-internationalization | 541 | gen-l10n, ARB files, plurals, RTL, locale formatting and localization build errors. |
| dart-drift | 471 | Drift in Dart CLI, server and desktop apps, including PostgreSQL with drift_postgres. |
| agents-md-generator | 384 | Creating or repairing minimal AGENTS.md files at the repo root and in nested modules. |
| flutter-duit-bdui | 346 | Duit and flutter_duit backend-driven UI: registries, transports, custom widgets and capability delegates. |

No indexed listings fall below the threshold; all 11 appear above.

The skill texts are written as operating procedures rather than documentation summaries. `flutter-animations` opens with a Principle 0 that forbids motion becoming hidden state or unverified demo code, and requires the agent to inspect the target widget, lifecycle and route structure before editing, then to verify analyzer-clean Dart afterwards and call out anything it could not run or see. `flutter-testing` goes further and ships `scripts/verify-examples.sh`, which checks the skill's own frontmatter, local links and fenced blocks so the examples do not rot.

## Why This Matters for Hermes Agents

Flutter output is easy to fake and hard to verify. An agent can produce a widget tree that reads well and fails on the first `flutter analyze`, and the skills push in the opposite direction: inspect first, edit narrowly, then prove the analyzer is clean and say what was not run. That single instruction is worth more than another page of API reference.

The suite covers the failures that actually block a build. Drift code generation breaks on `build_runner` after a schema change, `go_router` redirects fight with nested navigators, and localization fails at `l10n.yaml` before it fails at runtime. Each of those has a dedicated skill with the error strings written down, which is what lets an agent resolve them without a human reading the stack trace.

`agents-md-generator` is the sleeper. It is not Flutter-specific: it discovers the repository shape, detects module boundaries, and writes a short root AGENTS.md plus nested files for independent packages, which is useful in any monorepo and pairs with the Dart skills when a Flutter app grows a server package.

Concentration is the caveat. One skill holds 63 percent of the installs, and the suite was last pushed in May 2026, so treat it as strong knowledge about Flutter as it stood then, not as a live mirror of the current SDK.

## Usage

| You say | What happens |
|---|---|
| "Add a staggered entry animation to this card list" | `flutter-animations` inspects the widget and route, picks implicit or explicit animation, then requires analyzer-clean output and an explicit note on what was not visually checked. |
| "This screen breaks on tablets" | `flutter-adaptive-ui` converts it to breakpoint-driven layout with responsive navigation and input-aware behaviour. |
| "Where should this feature live?" | `flutter-architecture` places it by feature and layer, moves cross-feature imports, and wires repositories and DI. |
| "My drift build_runner step fails after the schema change" | `flutter-drift` fixes the table and migration, regenerates, and updates the stream-based UI. |
| "The deep link opens the wrong screen" | `flutter-navigation` traces guards, redirects and shell routes, and corrects the App Links or Universal Links setup. |
| "Add Russian plural forms" | `flutter-internationalization` edits the ARB files, plural and select messages and `l10n.yaml`. |
| "Write an AGENTS.md for this monorepo" | `agents-md-generator` maps modules and writes a short root file plus per-module files. |

## Verification

The raw paths below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/madteacher/mad-agents-skills/main/flutter-animations/SKILL.md

curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/madteacher/mad-agents-skills/main/agents-md-generator/SKILL.md
```

Then confirm the layout after a clone:

```bash
git clone --depth 1 https://github.com/madteacher/mad-agents-skills.git /tmp/mad-agents
ls -d /tmp/mad-agents/*/ | wc -l
ls /tmp/mad-agents/flutter-animations/references | wc -l
head -12 /tmp/mad-agents/flutter-animations/SKILL.md
```

The counts print 11 and 6, and `head` shows `name: flutter-animations`, the description listing the animation types it covers, and `metadata` naming Stanislav [MADTeacher] Chernyshev with `version: "2.0"`. If a skill directory has `SKILL.md` but no `references/`, the checkout is partial.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| flutter-animations | Pass | Pass | Pass |
| flutter-adaptive-ui | Pass | Pass | Pass |
| flutter-architecture | Pass | Pass | Pass |

The repository is small and mostly inert: 95 files, of which 69 are Markdown and 19 are Dart. The Dart files are illustrative assets rather than a package, and nothing is compiled or published from this repo. There is no install hook and no network client.

One script ships, `flutter-testing/scripts/verify-examples.sh`, and it is a linter for the skill itself. It requires ruby with YAML and ripgrep, validates the `SKILL.md` frontmatter and every local Markdown link, fails on unbalanced code fences, and rejects a list of stale test patterns such as `tester.trace(` and `--no-sound-null-safety`. It reads only files inside the skill directory, never a target project.

The real execution risk sits downstream of the skills, not inside them: they instruct the agent to run `flutter pub get`, `build_runner`, `flutter test` and analyzer commands in your project. Those are ordinary build steps, and they should run under the same review you would apply to any generated code.

## Limitations

- Snapshot data, verified 2026-11-03: 24,479 combined installs across 11 indexed listings; 111 GitHub stars; MIT via `LICENSE`; last pushed 2026-05-01. Counts drift over time.
- Last push was six months before this snapshot, so Flutter SDK changes after May 2026 are not reflected. Check `go_router`, Material and Drift APIs against your pinned versions.
- Install counts are lopsided: `flutter-animations` holds 15,490 of 24,479, and the other ten average just under 900 each, so popularity is a poor guide to which of the smaller skills are mature.
- The README documents no install command and no versioning story, only compatibility with tools that read the Agent Skills format, so the CLI routes above are the ecosystem default rather than a publisher instruction.
- The skills assume a working Flutter or Dart toolchain. None of them install the SDK, and the Drift and testing skills assume code generation and a CI runner already exist.
- `flutter-duit-bdui` covers a third-party backend-driven UI library whose API moves independently; pin the library version before relying on its examples.

## Related

- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)
- [Flutter Agent Plugins - Official Flutter Skills Setup](/hermes/skills/catalog/flutter-agent-plugins-setup)
- [Argent Skills - Mobile Dev Agent Toolkit Setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup)
- [React Native Update Skill - OTA Update Integration Setup](/hermes/skills/catalog/react-native-update-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Always install `flutter-architecture` alongside any other Flutter skill. It decides where code goes, and the others assume an answer.
- Ask for the analyzer result explicitly. The animation skill's Principle 0 treats unverified motion as a defect, and the same standard applies to every other skill in the suite.
- Run `flutter-testing/scripts/verify-examples.sh` after editing a skill, so your local copy stays internally consistent before the agent reads it.
- Keep AGENTS.md short. The generator caps the root file at 60 lines and module files at 40, which is the point: a long one gets skimmed.
- Reach for `dart-drift` rather than `flutter-drift` in server or CLI code, because the imports and PostgreSQL path differ.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
