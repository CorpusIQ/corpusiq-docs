---
title: "UI Craft - Design Engineering System Setup"
description: "educlopez/ui-craft on skills.sh: 23.2K combined installs across 32 listings; anti-slop UI rules, design review and a design memory for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ui-craft-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "frontend", "design systems", "accessibility"]
---

# UI Craft - Setup Guide

**Source:** [educlopez/ui-craft](https://www.skills.sh/educlopez/ui-craft) via skills.sh - 23.2K combined installs across 32 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 441 stars, MIT, last pushed 2026-11-06, 217 SKILL.md files across the tree because every skill is mirrored into `.agents/skills`, `.opencode/skills`, `.codex/skills`, `.gemini/skills` and the CLI's embedded copy, with the four published skills in `skills/`
**Category:** Frontend design engineering: anti-slop UI rules, design critique, motion, typography, accessibility and design tokens
**Quality Tier:** 🟢 Green - all three sampled skills pass all three scanners, the license is MIT, and the repo ships a real LICENSE file at the root.

UI Craft is a design system for coding agents rather than a component library. The README's claim is narrow and testable: ask for a dashboard and you get something you would put in production, not "gradient cards and bounce animations". Every surface is judged against one question, whether a designer would believe AI made it, and if the answer is yes the work is not done.

The system is organised as a ladder with four rungs. Rung 0 is simply installing it and asking for UI the way you always do. Rung 1 is naming a single pass: `/craft`, `/critique`, `/polish`, `/animate`, `/typeset`. Rung 2 is persisting taste in files under `.ui-craft/` so later sessions inherit it: `/brief`, `/tokens`, `/remember`. Rung 3 is enforcement: `/finalize` as a pre-ship gate, two read-only review agents, and MCP quality gates that can run in CI. `sddesign` is the express lane that walks rungs 1 to 3 in one guided run for a single large surface.

What separates it from the other design skills in this catalog is the scoring. The `/heuristic` command produces a critique from Nielsen's ten usability heuristics, six classic design laws and five persona walkthroughs, with every finding tagged by business impact, and the repo also ships a deterministic 0 to 100 `ui-craft-detect` score. That gives you a number to defend in a review instead of an opinion.

## Installation

The README recommends the CLI, a static Go binary that detects your harness and wires the skill, commands, MCP gates, review agents and design memory into its native config. It needs no Node at install time.

macOS and Linux:

```bash
curl -fsSL https://ui-craft.smoothui.dev/install | bash
```

Windows:

```powershell
irm https://ui-craft.smoothui.dev/install.ps1 | iex
```

Then wire it into the harnesses you use. The README notes the writes are idempotent, backed up before they happen and rolled back on failure:

```bash
ui-craft install
```

Claude Code users can skip the CLI and use the plugin, which auto-wires the MCP gates:

```text
/plugin marketplace add educlopez/ui-craft
/plugin install ui-craft
```

Cursor users clone into the local plugin folder and reload the window:

```bash
git clone https://github.com/educlopez/ui-craft.git ~/.cursor/plugins/local/ui-craft
```

The README's other two routes are a clone and a submodule:

```bash
git clone https://github.com/educlopez/ui-craft.git ~/.skills/ui-craft
git submodule add https://github.com/educlopez/ui-craft.git .skills/ui-craft
```

For a Hermes agent, the skill directories are plain Agent Skills folders, so copying or linking a skill into the agent's skills directory works without the CLI. The README documents the symlink pattern for exactly this case, because a global `npx skills add -g` writes to `~/.agents/skills` while Claude Code reads `~/.claude/skills`:

```bash
ln -s ~/.agents/skills/ui-craft ~/.claude/skills/ui-craft
```

Point that link at whichever skills directory your Hermes agent reads. The base skill is self-contained under `skills/ui-craft/`, including its `references/` folder, and the three style variants in `skills/ui-craft-minimal`, `skills/ui-craft-editorial` and `skills/ui-craft-dense-dashboard` defer to it.

## What It Provides

Twenty-four listings clear the 600-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| ui-craft | 1,563 | The base skill: discovery before coding, anti-slop rules, layout, typography, colour, motion, accessibility and polish |
| ui-craft-dense-dashboard | 1,297 | Data-heavy admin and analytics surfaces, with CRAFT 7, MOTION 3 and DENSITY 9 locked and IBM Plex plus tabular numerals |
| audit | 1,010 | Technical UI audit of accessibility, performance and responsive behaviour, returned as a prioritised findings table |
| ui-craft-minimal | 984 | Minimal whitespace-heavy surfaces, with CRAFT 8, MOTION 3 and DENSITY 2 locked and a monochrome plus one accent palette |
| ui-craft-editorial | 979 | Long-form editorial and magazine layouts, with CRAFT 9, MOTION 4 and DENSITY 3 locked and serif display type |
| colorize | 968 | Colour strategy: one accent in three to five intentional placements, or pulling an over-coloured UI back to neutral |
| heuristic | 957 | Scored critique from Nielsen's ten heuristics, six design laws and optional persona walkthroughs, with a 0 to 100 usability score |
| shape | 941 | Wireframe-first pass that writes an ASCII layout, state list, content inventory and open questions before any code |
| tokens | 932 | Auditing or establishing the three-layer token spine from primitive to semantic to component |
| finalize | 928 | Pre-ship gate that runs the detector, checks brief and tokens, applies the ten-pass finish bar and returns a verdict |
| brief | 926 | Writing or updating the durable design brief at `.ui-craft/brief.md` |
| remember | 798 | Recording a correction from the user as a lasting design constraint in the project brief |
| start | 797 | Front door: reads the project, reports which rung you are on and names the next command, with no code changes |
| sddesign | 788 | Spec-driven pipeline that walks brief, tokens, shape, craft, converge and ship in one run and writes `.ui-craft/spec.md` |
| critique | 656 | Design review of hierarchy, clarity and anti-slop patterns, as findings, with no code edits unless asked |
| animate | 639 | Motion pass: adding purposeful animation or removing motion that distracts, within the MOTION_INTENSITY setting |
| adapt | 639 | Responsive pass covering breakpoints, touch targets, safe areas and fluid type |
| typeset | 628 | Typography pass covering font choice, modular scale, tracking, leading and micro-typography |
| clarify | 626 | UX copy review of buttons, errors, empty states and form hints, with edits only on request |
| harden | 619 | Production readiness across loading, empty, error, partial data, internationalisation, offline and permissions |
| delight | 618 | One or two memorable micro-interactions, copy first and animation last, with no confetti |
| extract | 617 | Refactoring pass that pulls repeated class combinations into components and magic values into tokens |
| distill | 612 | Reduction pass that cuts content, structure and dead code that does not earn its space |
| unhappy | 611 | State-first design that covers loading, empty, error, partial, conflict and offline before the happy path |

The remaining 8 indexed listings range from 1 to 543 installs.

The ones just under the line are the ones you will reach for daily: `redesign` (543), `polish` (539), `craft` (535), `quieter` (526) and `bolder` (520). `craft` is the one-shot surface build and `polish` is the final detail pass, so a threshold based on install counts understates them. The other three tail entries are `friction-log` (370) and the two style presets, `ui-craft-playful` and `ui-craft-brutalist` at 1 install each.

## Why This Matters for Hermes Agents

Agents default to a recognisable visual vocabulary: centred gradient hero, three cards, generic Inter, uniform rounded corners, and one hover lift applied everywhere. This set attacks that with explicit rules and a named anti-slop detection pass, which is a different mechanism from a style guide. A rule like "hairline borders over shadows" or "tabular numerals for all data" is checkable, and `audit` and `finalize` check it.

The persistence layer is the part most design skills skip. `brief` writes five required sections to a file, `tokens` establishes a three-layer spine, and `remember` turns a correction into a constraint that survives the session. On a multi-session build that is the difference between a coherent interface and five screens that each look like a different product.

The scoring is what makes design review usable in a team. `heuristic` tags every finding with a business impact label, so a review produces a ranked list rather than a wall of taste. That maps directly onto an issue tracker, and the deterministic `ui-craft-detect` score gives CI something to gate on.

Finally, the coverage is broader than aesthetics. `adapt`, `harden`, `unhappy` and `clarify` cover responsive behaviour, non-happy states, internationalisation and microcopy, which are the parts of frontend work that agents most often declare done without checking.

## Usage

| You say | What happens |
|---|---|
| "Build me an analytics dashboard" | The base skill runs discovery, asks up to four questions, picks the dense dashboard composition and builds against the ten-item acceptance bar |
| "Why does this page look AI-generated" | `critique` returns a findings table on hierarchy, clarity and anti-slop patterns, with no code changes |
| "Make this feel more premium" | `polish` applies the compound detail pass, and `delight` adds one or two micro-interactions if the surface needs personality |
| "It breaks when the list is empty" | `unhappy` inventories every non-happy state and implements them, with `harden` following for the production matrix |
| "Set up the design tokens properly" | `tokens` audits or establishes the primitive, semantic and component layers, with light and dark both crafted |
| "Run a proper design review on this diff" | `heuristic` produces the scored scorecard, and the two read-only agents can run in parallel for an independent pass |
| "Is this ready to ship" | `finalize` runs the detector plus the brief and token checks and returns READY, NOT READY or BLOCKED |

## Verification

Read the base skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/educlopez/ui-craft/main/skills/ui-craft/SKILL.md | head -20
```

It should open with a description about avoiding generic AI-looking interfaces, with a required discovery phase before coding. The runner skills live in the harness mirrors, so this second path is the one to check if you installed through the CLI:

```bash
curl -fsSL https://raw.githubusercontent.com/educlopez/ui-craft/main/.opencode/skills/audit/SKILL.md | head -20
```

After install, check that the harness wiring is coherent rather than counting files by hand:

```bash
ui-craft doctor
```

The README describes `doctor` as a health check that verifies each harness install is coherent. If you installed through the skills CLI instead, `ls .agents/skills | wc -l` should report 29 skill directories.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ui-craft | Pass | Pass | Pass |
| ui-craft-dense-dashboard | Pass | Pass | Pass |
| audit | Pass | Pass | Pass |

The risk here is not the skills, which are markdown and reference files. It is the installer and the MCP server. The install script pipes a remote shell script into bash and then downloads a release binary, verifies its checksum and writes into your harness configuration directories; the Claude Code plugin pulls `ui-craft-mcp@0.9.0` through npx on first use. Read the script before running it, and prefer the plugin or a clone if you do not want a binary writing to config directories.

The broader consideration is that this system edits your application code. `craft`, `redesign`, `adapt` and the rest change components and styles, and the acceptance bar is the guarantee, not a diff review. Work on a branch, and keep `finalize` in front of your merge.

## Limitations

- Snapshot data, verified 2026-11-07: 23,168 combined installs across 32 indexed listings; 441 GitHub stars; MIT; last pushed 2026-11-06. Counts drift over time.
- The 217 SKILL.md files are mirrors, not 217 skills. Four published skills sit in `skills/` and the rest are the same directory copied into `.agents/`, `.opencode/`, `.codex/`, `.gemini/` and the CLI's embedded tree, so count skills by the 29 directories in one mirror.
- Two listings are presets rather than skills. `ui-craft-playful` and `ui-craft-brutalist` (1 install each) map to `examples/presets/playful.md` and `examples/presets/brutalist.md`, and `friction-log` (370) has no directory in the current tree.
- The CLI is the best-supported path. The README's own platform table shows the six release binaries are not equally exercised, with macOS Apple Silicon the only one tested end to end on every release.
- The Claude Code plugin and the MCP gates pull Node packages at runtime. The install itself needs no Node, but the quality gates do.
- The knobs are opinionated defaults. CRAFT_LEVEL 7, MOTION_INTENSITY 5 and VISUAL_DENSITY 5 suit product UI, and editorial or playful work needs the variant skills or explicit knob changes rather than the base defaults.

## Related

- [Superdesign Skill - Canvas Design & Inspiration Setup](/hermes/skills/catalog/superdesign-skill-setup)
- [UI/UX Pro Max - 19-Skill Design System Pack Setup](/hermes/skills/catalog/ui-ux-pro-max-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `start` on an existing project before anything else. It reports which rung the project is on and names one command, which is cheaper than guessing between twenty-five of them.
- Write the brief before the first screen. `brief` takes one pass and every later session reads it, while a missing brief means each new surface re-litigates the same decisions.
- Use `heuristic` when you need to convince someone, and `critique` when you need to fix something. The first produces a scored scorecard, the second produces a shorter list of what is wrong.
- Keep `.ui-craft/` in version control. The brief, tokens and spec are the only durable output of the system, and they are what makes the next session consistent.
- Pair `unhappy` with `harden` rather than choosing one. The first designs the states, the second proves the surface survives them in production.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
