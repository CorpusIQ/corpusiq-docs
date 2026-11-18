---
title: "Flutter Skills - Reusable Flutter Engineering Skills"
description: "zakariaf/flutter-skills: 8.4K combined installs across 38 listings; reusable Flutter engineering skills for AI coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/flutter-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "flutter", "dart", "riverpod"]
---

# Flutter Skills - Setup Guide

**Source:** [zakariaf/flutter-skills](https://www.skills.sh/zakariaf/flutter-skills) via skills.sh - 8.4K combined installs across 38 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 69 stars, MIT license, `main` branch, last pushed 2026-09-23, 40 skills under `skills/<name>/SKILL.md`
**Category:** Flutter and Dart engineering skills
**Quality Tier:** 🟠 Orange - 57 Pass, 2 Warn and 1 Fail (Gen Agent Trust Hub) across the 20 sampled listings.

Flutter Agent Skills is a set of 40 reusable Flutter and Dart engineering playbooks for coding agents. Each skill is a short ruleset an agent loads only when a task matches its description: the rules, the anti-patterns, and a definition of done, applied the same way across sessions, projects, and agents. The set spans architecture, Riverpod 3.x state, testing, persistence, i18n/RTL, accessibility, navigation, performance, and shipping, plus the codegen, CI, and migration runbooks that keep those practices enforced.

The suite is built on the Agent Skills open standard, so the same files work in Claude Code, Cursor, Codex, Copilot, Gemini CLI, Windsurf, Cline, OpenCode, and 70+ other agents. The skills were distilled from the private libraries of more than ten production Flutter apps (about 120 skills), merged into one canonical stack of Riverpod 3.x, go_router, Drift, package:clock, and Material 3, with design-token and app-domain specifics left out.

## Installation

The universal installer uses the skills CLI and works across the agents the CLI detects:

```bash
npx skills add zakariaf/Flutter-Skills                 # all skills
npx skills add zakariaf/Flutter-Skills --list          # browse first
npx skills add zakariaf/Flutter-Skills --skill flutter-architecture
```

Claude Code can install it as a plugin from the marketplace:

```text
/plugin marketplace add zakariaf/Flutter-Skills
/plugin install flutter@flutter-skills
```

Or copy the skills into a single project:

```bash
git clone https://github.com/zakariaf/Flutter-Skills
mkdir -p .claude/skills && cp -R Flutter-Skills/skills/* .claude/skills/
```

For a personal-global install that every project sees, symlink each skill directory into `~/.claude/skills/`. Agents that read `AGENTS.md` can copy the repo's intent-to-skill map into a consuming project's own `AGENTS.md`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| flutter-performance | 280 | Runtime performance rules: const subtrees, minimal rebuild scope, lazy lists, sized image decode, and profile-mode measurement. |
| widget-composition | 262 | Widget structure: named const Widget classes, lean build methods, key policy, and controller disposal. |
| flutter-architecture | 253 | Feature-first layered MVVM with a downward-only dependency DAG and Riverpod 3.x as the one DI and state mechanism. |
| design-system-structure | 250 | Token-to-theme design system organization with ThemeExtension, no raw values, and reduced-motion handling. |
| state-management-riverpod | 247 | One Notifier/AsyncNotifier ViewModel per feature over immutable state with a single write path. |
| ui-states-and-feedback | 243 | Loading, empty, error, and content states in one switch, with typed failure messages and retry. |
| testing-strategy | 242 | Test doctrine where shape follows code: clock-injected pure cores, seeded fuzz tests, and fakes over mocks. |
| i18n-rtl-l10n | 240 | gen-l10n/ARB localization: key parity, ICU plurals, Directional-only geometry, and RTL/bidi isolation. |
| adaptive-layout | 240 | Layout by constraints and Material 3 window size classes, never device or platform checks. |
| accessibility-as-code | 239 | Accessibility as a correctness property: Semantics on every node, 44px targets, never color alone. |
| widget-golden-and-a11y-testing | 234 | A pumpApp test harness with a per-device overflow matrix and golden plus a11y lanes. |
| navigation-and-routing | 231 | One GoRouter with deep-linkable path identity, redirect guards, and StatefulShellRoute shells. |
| motion-and-haptics | 228 | Designed interaction feedback: same-frame acknowledgment, an interruptible animation, and one haptic per commit. |
| dependency-hygiene | 227 | pubspec and lock discipline: caret ranges, committed lock, SDK pinning, and a dependency gate. |
| custom-canvas-and-gestures | 226 | CustomPainter discipline: View/Painter/Scene split, one shared transform, and geometry hit-testing. |
| lint-and-style-config | 220 | A strict analysis_options.yaml on very_good_analysis with silent-failure lints promoted to errors. |
| forms-and-input | 220 | Form and TextFormField rules: sync and async validation, focus traversal, and controller disposal. |
| dart3-idioms-and-coding-standards | 220 | Which Dart 3 construct each declaration earns: sealed classes, records, and immutable value types. |

The remaining 20 indexed listings range from 195 to 219 installs.

## Why This Matters for Hermes Agents

Each skill is a short playbook that loads only when a task matches its description, so an agent pays the context cost only for the rules that apply. The rules are written as anti-patterns plus a definition of done, which means the same decision gets made the same way across sessions, projects, and agents.

The heavier skills ship progressive disclosure: a lean SKILL.md plus on-demand references/, complete examples/, and runnable scripts/. Many scripts are grep or analyze checks (check_architecture.sh, check-drift-confinement.sh, check-money-violations.sh) that turn a rule into a failing command an agent can run, so compliance is verified rather than asserted.

The one-canonical-stack design is the real value for an agent: feature-first layout, Riverpod 3.x, go_router, Drift, package:clock, and Material 3 are reconciled to a single vocabulary, so the 40 skills never contradict each other. For a Hermes agent maintaining a Flutter app, the suite gives it a consistent, reviewable standard to enforce instead of improvising per task.

## Usage

| You say | What happens |
|---|---|
| "Set up zakariaf/Flutter-Skills" | Installs all 40 skills into the agent the skills CLI detects. |
| "Review this screen for state leaks" | Loads state-management-riverpod and widget-composition to check the ViewModel, rebuild scope, and disposal. |
| "Add a settings form with async validation" | Loads forms-and-input: sync validator, async checks in a debounced Notifier, focus traversal, and controller disposal. |
| "Make this list jank-free" | Loads flutter-performance: const subtrees, select-scoped rebuilds, lazy builders, and sized image decode. |
| "Wire up a new route with auth redirects" | Loads navigation-and-routing: GoRouter, path-param identity, and redirect guards. |
| "Cut a release build" | Loads release-and-store-shipping: version source, archived symbols, merged-manifest permission audit, and store declarations. |

## Verification

Probe a skill before installing. The repo lives at zakariaf/Flutter-Skills on GitHub (capitalized) with skills under `skills/<name>/SKILL.md` on the `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/zakariaf/Flutter-Skills/main/skills/flutter-architecture/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zakariaf/Flutter-Skills/main/skills/state-management-riverpod/SKILL.md
```

Both return 200. Install with `npx skills add zakariaf/Flutter-Skills`, or for one skill `npx skills add zakariaf/Flutter-Skills --skill flutter-architecture`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| flutter-performance | Pass | Pass | Pass |
| widget-composition | Pass | Pass | Pass |
| flutter-architecture | Pass | Pass | Pass |
| design-system-structure | Pass | Pass | Pass |
| state-management-riverpod | Pass | Pass | Pass |
| ui-states-and-feedback | Pass | Pass | Pass |
| testing-strategy | Pass | Pass | Pass |
| i18n-rtl-l10n | Fail | Pass | Pass |
| adaptive-layout | Pass | Pass | Pass |
| accessibility-as-code | Pass | Pass | Pass |
| widget-golden-and-a11y-testing | Pass | Pass | Pass |
| navigation-and-routing | Pass | Pass | Warn |
| motion-and-haptics | Pass | Pass | Pass |
| dependency-hygiene | Pass | Pass | Warn |
| custom-canvas-and-gestures | Pass | Pass | Pass |
| lint-and-style-config | Pass | Pass | Pass |
| forms-and-input | Pass | Pass | Pass |
| dart3-idioms-and-coding-standards | Pass | Pass | Pass |
| persistence-drift | Pass | Pass | Pass |
| release-and-store-shipping | Pass | Pass | Pass |

The sample covers 20 of 38 indexed listings. One listing fails an auditor: i18n-rtl-l10n fails Gen Agent Trust Hub. navigation-and-routing and dependency-hygiene carry Snyk warnings. Review the i18n-rtl-l10n verdict page before relying on it in production.

## Limitations

- Snapshot data, verified 2026-11-17: 8,430 combined installs across 38 indexed listings; 69 GitHub stars; MIT; last pushed 2026-09-23. Counts drift over time.
- The install counts in the table sit within a 60-install spread (220 to 280); the suite installs as one unit, so flat counts are expected rather than a quality signal.
- The README counts 40 skills; skills.sh indexes 38. The two without a skills.sh listing are async-safety and design-review-workflow.
- i18n-rtl-l10n carries a Gen Agent Trust Hub Fail in the sampled verdicts, so give it more review than the rest of the suite before production use.
- Skills are guidance playbooks, not a code generator: each one ships rules, anti-patterns, and a definition of done that an agent must still apply correctly.

## Related

- [Flutter Agent Plugins - Official Flutter Skills Setup](/hermes/skills/catalog/flutter-agent-plugins-setup)
- [MAD Agents Skills - Dart and Flutter Suite Setup](/hermes/skills/catalog/mad-agents-skills-setup)
- [Apple Design Skill - HIG Review Across Frameworks](/hermes/skills/catalog/apple-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with `--list` first to browse the skills before pulling the whole set.
- Run the shipped scripts (check_architecture.sh, check-drift-confinement.sh, check-money-violations.sh) as gates, not just as documentation.
- Rich skills (references/, examples/, scripts/) auto-load only the lean SKILL.md; the deep dives load on demand.
- The flutter-conventions-index skill is the front door: it routes each task to the right deep-dive skill.
- For the manual-only runbooks (run-codegen, run-migration, run-goldens-rebaseline), trigger them explicitly rather than letting an agent fire them unprompted.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
