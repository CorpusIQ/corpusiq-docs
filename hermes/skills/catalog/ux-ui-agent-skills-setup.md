---
title: "UX UI Agent Skills - Design Gates for Coding Agents"
description: "plugin87/ux-ui-agent-skills on skills.sh: 10.4K combined installs across 20 listings; 26 design skills and 52 gates for any framework."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ux-ui-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "design systems", "accessibility", "design tokens", "wcag"]
---

# UX UI Agent Skills - Setup Guide

**Source:** [plugin87/ux-ui-agent-skills](https://www.skills.sh/plugin87/ux-ui-agent-skills) via skills.sh - 10,384 installs across 20 indexed listings (10.4K combined); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 3,145 stars, MIT via LICENSE, `main` branch, last pushed 2026-10-27, 26 skill directories under `.claude/skills/` with one `SKILL.md` each, plus a fixture skill at `tests/fixtures/bad/bare-paths/.claude/skills/leaky/`
**Category:** Design systems and UI quality: token architecture, component specs, accessibility audits and design QA gates for coding agents across 16 framework adapters
**Quality Tier:** 🟡 Adequate - MIT license, 26 skills and a real gate harness, but one Trust Hub Fail on a11y-audit and one Trust Hub Warn on design-component keep it below the top tier.

XIAS, which is what the repository calls itself, is a design-system doctrine layer for coding agents: 26 runnable skills, 14 DTCG token files, 52 component specs, 16 framework adapters and a library of 2,144 named design systems, 2,087 of them measured from the live site. Release v3.0.0. It ships no build tools, no dependencies and no runtime of its own, which is accurate: the skills are Markdown instruction files, and the work they describe is done by the agent reading them.

The part worth understanding before installing anything is the gate harness. 52 checks run against rendered HTML, and 34 of them open a real browser to do it: contrast measured per text element in every state, axe roles and landmarks, keyboard reachability, 24x24 target size, reduced motion, horizontal overflow down to 280px, token-by-intent resolution, a no-emoji rule and a hardcoded-value lint. The README's comparison runs that harness against a fixture page written the way a model writes when nothing stops it: ten gates reject it, including a Save button measured at 1.00:1, a 15x16 icon button against a 24x24 minimum, 820px of overflow at 280px and 63 hardcoded values. The reference screen beside it passes all 52.

The install index reflects breadth rather than depth. 20 indexed listings between 178 and 768 installs each means the suite is being taken one skill at a time rather than as a kit, and the per-skill route is exactly the one that leaves the kit's files behind.

One count is inconsistent in the repository itself: the README states 52 gates and badges 52, while the GitHub description says 50. Nothing in the tree resolves which is current, so treat 52 as the README's number.

## Installation

The README's recommended route is the Claude Code plugin, two lines and no files copied into the project:

```text
/plugin marketplace add plugin87/ux-ui-agent-skills
/plugin install ux-ui-agent-skills@ux-ui-agent-skills
```

That installs 26 skills and the `design-critic` agent. Fourteen of the skills the model can reach for on its own when the work calls for them, including `design-tokens`, `design-code`, `design-review`, `a11y-audit` and `design-doctrine`. Twelve are deliberately user-invoked, among them `/image-to-code`, `/redesign`, `/prototype`, `/gate`, `/critique` and `/grill-me`, because each one takes an action or sets a direction that should be your call.

The npx route installs the kit into the current folder:

```bash
npx ux-ui-agent-skills init                    # full kit
npx ux-ui-agent-skills init --agent codex      # AGENTS.md surface for Codex, Cursor, Copilot, Aider
npx ux-ui-agent-skills list                    # every area, before you choose
npx ux-ui-agent-skills demo                    # rendered examples, installs nothing
```

Homebrew wraps the same npm tarball:

```bash
brew install plugin87/tap/ux-ui-agent-skills
```

An MCP server ships in the same package as `ux-ui-mcp` and runs through `npx -y --package=ux-ui-agent-skills ux-ui-mcp`; register it with the client's `mcp add` command, which takes the server name followed by the command to run.

A single skill can be taken through the skills CLI, which is what the skills.sh listings wrap:

```bash
npx skills add https://github.com/plugin87/ux-ui-agent-skills --skill image-to-code
```

That route needs a warning the README does not put next to the command. Every `SKILL.md` in the kit opens with a Step 0 that runs `ls ${CLAUDE_SKILL_DIR}/../../../tokens` and, on a miss, prints KIT_MISSING, tells the agent that only the skill folders were installed, and stops. `npx skills add` installs only the skill folders. So a per-skill install gives you the instructions and none of the token files, accessibility checklists or gate scripts they read, and the skill will say so and refuse to guess rather than produce an audit from nothing.

The gates need a browser. 34 of them use the Chrome installed on the machine, or the one that `npx playwright install chrome` fetches. Neither install route installs it for you.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear below:

| Skill | Installs | Use For |
|---|---|---|
| image-to-code | 768 | Turning a reference image, screenshot or mockup into token-driven accessible code: infer the palette, type scale, spacing and layout archetype, map it to the three token tiers, rebuild, then verify with the gates |
| design-review | 644 | Reviewing a design across six weighted dimensions with Nielsen's ten heuristics and a prioritized findings table, before or after a build |
| a11y-audit | 598 | Auditing a UI against WCAG 2.2 AA and AAA and the ARIA patterns, returning criterion-referenced findings with severity and specific fixes |
| design-tokens | 585 | Generating, extending or auditing DTCG tokens in the primitive, semantic and component tiers, including multi-brand theming and token validation |
| redesign | 580 | Upgrading an existing site or app without breaking it: audit what is there, name the generic tells, then apply the system rules surgically |
| apply-aesthetic | 577 | Applying a visual direction, an archetype or one of 2,144 named design systems by resolving it into the token system |
| design-code | 569 | Generating production component code for a named stack, from React and Tailwind through SwiftUI, Flutter, Jetpack Compose and Web Components |
| design-component | 565 | Specifying a component at the design level: anatomy, variants, sizes, the eight states, token mapping and accessibility, before or beside the code |
| ux-writing | 564 | Writing or reviewing interface copy (buttons, errors, empty states, labels) against the voice and tone system and the what, why, how error formula |
| design-qa | 560 | Standing up design QA gates: token and hardcoded-value lint, axe accessibility, contrast, visual regression across states and themes, plus the manual checklist |
| brandkit | 558 | Generating a brand design system from a brief as DTCG tokens in light and dark, plus a single theme.css, verified for WCAG |
| migrate-design-system | 531 | Mapping the token system to or from an external design system (Material 3, Apple HIG, Fluent, Carbon, Ant, shadcn/ui, Radix) for interop or migration |
| prototype | 528 | Moving an idea up the fidelity ladder from content-first to code with a validation plan at each level, plus journey maps and usability-test scripts |
| performance | 528 | Optimizing UI against Core Web Vitals (LCP, INP, CLS), with code-split strategy, layout-shift prevention and animation performance rules |
| token-build | 522 | Running the token build pipeline that turns DTCG JSON into CSS variables, a Tailwind theme, JS or TS, an iOS Asset Catalog and Compose output |
| figma-integration | 520 | Keeping Figma and code in sync: map tokens to Figma Variables with collections and modes, sync either direction, verify component parity |
| governance | 516 | Governing how the system evolves: SemVer for tokens and components, the contribution workflow, deprecation policy and change communication |
| design-doctrine | 309 | The house rules the other skills defer to: run the gate and never claim a number, the no-emoji rule, token by intent, one shared theme, the eight states |
| critique | 184 | Adversarial critique of finished work: render it, look at it, argue for rejection. Run after the gates are green, never instead of them |
| grill-me | 178 | Interrogating the brief before anything is built, asking only the questions whose answers change the work and recording the rest as stated assumptions |

No indexed listings fall below the threshold; all 20 appear above.

Six more skill directories carry no listing at all: `data-dashboard`, `design-screen`, `gate`, `observe`, `scaffold-project` and `ship`. They are in the tree and install with the plugin, and the README names them as part of the 26, so the index is behind the suite rather than the suite being smaller than it looks.

`design-doctrine` is the one to read first regardless of which skill you came for. It carries the verification protocol that the rest assume: never state a number you did not measure, verify every state rather than only the resting one, report the real N/N line from `accuracy_report.mjs` rather than an interim claim, and treat a SKIPPED render gate as a failure rather than a pass. That last rule exists because a render gate with no browser installed prints SKIPPED and exits 0, which reads as success in any CI log.

## Why This Matters for Hermes Agents

The default output of a coding agent asked for a dashboard is a known shape: an indigo-to-purple gradient, four equal stat cards with no focal point, emoji as icons, one radius and one shadow everywhere, grey-on-white body text and a blue Delete button. Every item in that list is a measurable property, and this kit's premise is that measurable properties should be measured rather than reviewed by taste. For an agent that ships UI unattended, a gate that fails the build is worth more than a style guide it was asked to remember.

The second fit is the token architecture. Primitive, semantic and component tiers with intent names mean an agent can be told to use `color.text.danger` and be checked mechanically, instead of being told to use red and being trusted. `token-build` turns the same source into CSS, Tailwind, iOS and Compose output, so one extraction or one brandkit run can serve several targets without a second set of decisions.

The third is that the suite is written as procedures with stopping conditions. `design-doctrine` says to run the gate and report the real number, `critique` says to argue for rejection after the gates are green, `grill-me` says to interrogate the brief before a line is built. Those are the three places an agent most often substitutes confidence for work, and each has a skill that names the substitution.

The honest counterweight: these are instructions, not an enforcement layer. Nothing stops an agent from claiming a pass it did not run, and `critique` in particular is a prompt for an adversarial review rather than a scored test. The gates are the objective half; the taste half is still a model reading its own output.

## Usage

| You say | What happens |
|---|---|
| "Build this screenshot as a React component" | `image-to-code` infers the palette, type scale, spacing and layout archetype from the reference, maps them to the three token tiers, rebuilds and runs the gates |
| "Audit our settings page for accessibility" | `a11y-audit` checks the P0 set per component against WCAG 2.2, measures contrast with the render gates instead of eyeballing it, and returns criterion, severity, failure and fix |
| "Design a notification component with every state" | `design-component` writes the spec (anatomy, variants, sizes, the eight states, token mapping, accessibility) and `design-code` generates it for the named framework |
| "Make this landing page feel less generic" | `redesign` audits what is there, names the AI tells, then applies the aesthetic and system rules without changing behaviour |
| "Give us a brand system with light and dark" | `brandkit` emits primitive, semantic and component tokens for both modes plus a single theme.css, checked for WCAG contrast |
| "Our buttons look wrong in dark mode" | `design-qa` runs the state-aware contrast gate across default, hover and focus, which is where a button that passes at rest fails |
| "Set up CI so design cannot regress" | `design-qa` wires token lint, hardcoded-value lint, axe and visual regression into a pipeline, and `gate` runs all 52 checks and reports the real N/N |
| "Before we build, what are we actually making" | `grill-me` asks only the questions whose answers change the work and records every unasked decision as a stated assumption |

## Verification

Each skill is a plain `SKILL.md` under `.claude/skills/`, and this URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/plugin87/ux-ui-agent-skills/main/.claude/skills/image-to-code/SKILL.md | head -6
```

It should open with YAML frontmatter holding `name: image-to-code` and a `description` that names the three token tiers and the gate check, then `# Skill: Image to Code` below the closing delimiter.

The a11y-audit file is worth fetching separately, because it shows the kit dependency that the per-skill install route breaks:

```bash
curl -fsSL https://raw.githubusercontent.com/plugin87/ux-ui-agent-skills/main/.claude/skills/a11y-audit/SKILL.md | sed -n '1,12p'
```

The first lines after the frontmatter are the Step 0 kit check and the paths it reads: `accessibility/wcag-checklist.md`, `accessibility/aria-patterns.md` and three scripts under `scripts/`. If those relative paths change, every skill in the kit breaks at once rather than one at a time.

After a plugin install, confirm the inventory and the version rather than trusting the session:

```bash
claude plugin details ux-ui-agent-skills
```

That prints the loaded skills with their token cost, which is the practical way to see whether the fourteen auto-invocable skills are the fourteen you expect. For the npx route, `npx ux-ui-agent-skills list` enumerates the areas before you commit to a copy.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| image-to-code | Pass | Pass | Pass |
| design-review | Pass | Pass | Pass |
| a11y-audit | Fail | Pass | Pass |
| design-tokens | Pass | Pass | Pass |
| redesign | Pass | Pass | Pass |
| apply-aesthetic | Pass | Pass | Pass |
| design-code | Pass | Pass | Pass |
| design-component | Warn | Pass | Pass |
| ux-writing | Pass | Pass | Pass |
| design-qa | Pass | Pass | Pass |
| brandkit | Pass | Pass | Pass |
| migrate-design-system | Pass | Pass | Pass |
| prototype | Pass | Pass | Pass |
| performance | Pass | Pass | Pass |
| token-build | Pass | Pass | Pass |
| figma-integration | Pass | Pass | Pass |
| governance | Pass | Pass | Pass |
| design-doctrine | Pass | Pass | Pass |
| critique | Pass | Pass | Pass |
| grill-me | Pass | Pass | Pass |

One Fail sits on a11y-audit. Of the three scanners, Gen Agent Trust Hub returns Fail while Socket and Snyk both return Pass on the same files, so the disagreement is between scanners rather than between scanners and the code. The plain consequence: any pipeline or review process that treats a Trust Hub Fail as a block will reject a11y-audit, and it would have to be excluded from that gate deliberately, with a written exception, rather than waved through.

It is worth being concrete about what that skill actually instructs, because the verdict is only meaningful next to it. `a11y-audit` is 25 lines of Markdown with no code of its own. It tells the agent to read two reference files and to execute three repository scripts: `gate.mjs measure_render.mjs` for per-element contrast on rendered HTML, `gate.mjs verify_states.mjs` for default, hover and focus states, and `contrast.py` for a loose colour pair. Those reads and executions sit three directory levels above the skill's own folder, which is precisely the pattern a static scanner flags. Design-qa does the same thing and returns Pass on all three, so the verdicts here are an inconsistent signal rather than a risk score, and re-checking the live pages before a production install is not a formality.

The Warn on design-component is milder in kind: it is a specification skill, and the flagged behaviour is instruction shape rather than execution.

Beyond the verdicts, the security surface of the whole suite is close to zero at rest and considerable in effect. There is no package to compromise, no install hook and no network call in any skill file. What the kit changes is what the agent is willing to claim: the doctrine forces measured numbers, and the gates run real browsers against real pages. The risk that remains is the usual one for a design agent given Bash, since 34 of the gates execute Node scripts and a Chrome instance against the project's own files.

## Limitations

- Snapshot data, verified 2026-11-09: 10,384 combined installs across 20 indexed listings; 3,145 GitHub stars; MIT license; last pushed 2026-10-27. Counts drift over time.
- The skills.sh source page caps at 20 listings and this repository lands exactly on the cap, so a 21st indexed skill would not appear here and the combined figure would be understated. The tree already holds 26 skills against 20 listings.
- Index and tree disagree in both directions: `data-dashboard`, `design-screen`, `gate`, `observe`, `scaffold-project` and `ship` are installed with the kit but carry no install count, and the install counts are therefore not a complete measure of what the suite contains.
- The per-skill route is self-defeating for anything past a narrow task. `npx skills add ... --skill a11y-audit` copies one folder and the skill stops with KIT_MISSING because the token files, checklists and gate scripts it reads were never installed. Use the plugin or `init` for the kit.
- The 52-gate figure in the README and the 50 in the GitHub description are both live and un reconciled in the tree, so quote the README's number and expect a reader who checked the repo description to see a different one.
- 34 gates need a browser, and without one a render gate prints SKIPPED and exits 0. A green CI log is not evidence the gates ran; run single render gates behind `DS_REQUIRE_BROWSER=1` so a missing browser becomes a failure.
- Trust Hub returns Fail on a11y-audit and Warn on design-component while Socket and Snyk return Pass on both. The verdicts are a snapshot and they do not agree with each other.

## Related

- [UI/UX Pro Max - Design System Skill Pack Setup](/hermes/skills/catalog/ui-ux-pro-max-setup)
- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)
- [Layers Skills - Design System Agent Pack](/hermes/skills/catalog/layers-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `design-doctrine` before any other skill in the kit. It carries the verification protocol the rest assume, and an agent that skipped it will report an interim N/N as if it were a result.
- Set `DS_REQUIRE_BROWSER=1` in CI. A render gate with no browser prints SKIPPED and exits 0, which is indistinguishable from a pass in a log that only greps for failure.
- Missing the point badly? Run `/grill-me` before the build, not `/critique` after it. Every unasked decision that is not on the record as an assumption becomes a rewrite.
- Run `/gate` and read the raw N/N line yourself rather than accepting a summary. The doctrine is explicit that a claimed number and a measured number are different objects.
- Install the plugin (or run `init`) if you intend to use anything beyond one skill. The token files, accessibility checklists and gate scripts live outside the skill folders, and the per-skill route does not copy them.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
