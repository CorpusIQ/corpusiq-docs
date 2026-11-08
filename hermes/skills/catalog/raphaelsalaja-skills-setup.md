---
title: "Interface Skills - Animation and UI Craft for Agents"
description: "raphaelsalaja/skills on skills.sh: 6,201 combined installs across 42 indexed listings; interface craft rules for motion, layout, colour and UI audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/raphaelsalaja-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "interface design", "motion", "ui audit"]
---

# Interface Skills - Setup Guide

**Source:** [raphaelsalaja/skills](https://www.skills.sh/raphaelsalaja/skills) via skills.sh - 6,201 combined installs across 42 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep, first documentation)
**GitHub:** 62 stars, MIT, last pushed 2026-11-04, 25 SKILL.md directories under skills/ with a shared interface kit at kit/
**Category:** Interface craft for agents: animation principles, motion tokens, layout, colour, icons and UI audit playbooks
**Quality Tier:** 🟡 Use With Care - MIT licence and a well-structured collection, but 62 stars, 17 of the 42 indexed listings have no skill directory in the snapshot, and one sampled listing carries a Snyk warning.

Twenty-five skills that argue about interface quality in the only way an agent can act on: exact values and a broken line beside the line that replaces it. The house rule is called the pair. Every rule has an id, an example of the mistake and an example of the fix, and a finding is reported as `file:line - [rule-id]`. A rule with no pair is, by the repository's own standard, not finished.

The collection splits in two. Eight principle skills hold a standard that applies while any work is happening: `scope`, `reuse`, `restraint`, `copy`, `prose`, `defaults`, `motion`, `color`. Seventeen procedure skills run a job in order: `verify`, `gather`, `match`, `rule`, `viewports`, `icons`, `ship`, `prototype`, `lab`, `deconstruct`, `alignment`, `keyboard`, `frames`, `avatar`, `bots`, `sketchbook`, `audit`. Eleven of the procedures are user-invoked only and set `disable-model-invocation: true`, so they cannot be triggered by inference.

The quality of the writing is the reason to read this collection even if you install nothing. `skills/motion/SKILL.md` is 208 lines of specific claims: app chrome fades and does not slide, entrances do not replay on route change, `transition: all` is a finding, nothing enters from `scale(0)`, and any motion the user started that runs past 300ms is a finding in any style. `skills/verify/SKILL.md` opens with the sentence that most agents need: a typecheck, a lint pass or a green build does not show that a visual change works.

## Installation

The README's install is one command:

```bash
npx skills add raphaelsalaja/skills
```

Claude Code users can take the plugin instead, which registers every skill under a `userinterface` namespace:

```text
/plugin marketplace add raphaelsalaja/skills
/plugin install userinterface@userinterface
```

The two routes differ in invocation only. Skills-CLI users call `/verify`; plugin users call `/userinterface:verify`. The plugin is at version 3.28.0 in `.claude-plugin/plugin.json`, and that number is the only signal plugin users update on.

Principle skills and the six non-user-invoked procedures load on their own when the work calls for them. The rest are called by name:

```text
/audit the uncommitted diff
/alignment the settings page
/frames opening the command palette
/viewports the pricing page
```

There is one maintenance command for anyone working inside a clone rather than consuming the skills. `kit/` holds the shared interface shipped pages and overlays use, and it is copied into marked regions of each skill rather than imported:

```bash
node kit/sync.mjs           # push kit changes into every skill
node kit/sync.mjs --check   # exits 1 when any region has drifted
```

## What It Provides

Twelve of the 42 indexed listings clear the 100-install threshold. All twelve appear below with their exact counts:

| Skill | Installs | Use For |
|---|---|---|
| 12-principles-of-animation | 2,247 | The canonical animation principles, applied as checks rather than as theory |
| morphing-icons | 362 | Icon transitions that morph between states without a redraw |
| mastering-animate-presence | 325 | Enter and exit animation with the presence primitive handled correctly |
| to-spring-or-not-to-spring | 271 | Choosing between a spring and a curve, with the reasoning made explicit |
| pseudo-elements | 247 | Decorations and overlays built from pseudo-elements instead of extra markup |
| sounds-on-the-web | 212 | Interface sound done sparingly, with the browser constraints named |
| generating-sounds-with-ai | 196 | Producing the sound assets themselves rather than sourcing them |
| motion | 149 | House motion policy: what animates, easing, durations, springs, gestures, exits, motion blur, reduced motion |
| gather | 107 | Collecting references from the user's own library onto one linked board before building |
| deconstruct | 103 | Breaking an animation into a state machine and a timeline you can scrub and edit |
| alignment | 101 | Measuring a running page for edges, gaps, centring and radii that miss by a pixel or two |
| viewports | 100 | Rendering every width, breakpoint edge, landscape phone and 200% text, then reporting what breaks |

30 rows fall below the threshold, from 2 to 99 installs. The tail is long and flat: `reuse` at 99, `match` at 99, `defaults` at 98, then a block of skills at 94 to 97, down to `container-bounds`, `interface-sound`, `predictive-prefetch`, `synthesize-sound`, `exit-animations` and `interface-typography` at 2 to 4 installs. Those numbers are what a young collection looks like, not a quality ranking, since several of the strongest files in the repository are principle skills sitting in the tail.

The substance is in the rule ids. `motion-opacity-for-chrome`, `motion-origin-from-trigger`, `motion-no-scale-from-zero`, `verify-build-is-not-proof`, `verify-say-where`, `scope-smallest-reading`, `alignment-measure-the-render`, `audit-project-rules-first`. Each id appears once in the prose and once in that skill's pair table, and the naming scheme means a finding is traceable to a rule that has a written replacement for the exact thing it flags.

`audit` is the consolidator and owns no rule of its own. It states the scope, reads `AGENTS.md`, `CLAUDE.md` and the editor rule folders first because a written project rule outranks a default here, then checks the scope against every skill and merges the findings into one ranked, numbered report. The report closes with `Block` if any high-severity finding remains and `Approve` if not.

## Why This Matters for Hermes Agents

Agents produce interface work that passes every automated gate and still looks wrong. The tells are small and consistent: a dropdown that scales from its own centre instead of its trigger, a page that replays every entrance on navigation, a card that enters from `scale(0)`, a `transition: all` that animates layout, a form built from a `div` with `space-y-*`. None of that fails a build.

This collection attacks that with values. Motion past 300ms is a finding. A 1 to 4 pixel misalignment is a finding, because it reads as a mistake while a 16 pixel indent reads as intent. An entrance below `scale(0.95)` is a finding. Numbers are checkable by an agent in a way that "polish the motion" is not, and checkable rules are the only kind that survive a long session.

The second fit is `verify`, which is the discipline most agent workflows lack. Its rules are blunt: reproduce the symptom before editing, look where the user will look, click every control you added once, check the whole surface not just the edited row, and say where the user can see the result. A reply that says "it should work now" is `verify-say-where`. Declaring done with an unchecked item is `verify-name-the-gap`. Those map directly onto a subagent that reports back to a parent.

Third, the collection is honest about scope. Principle skills hand off to each other by name instead of restating: whether an animation should exist belongs to `restraint`, taking one apart belongs to `deconstruct`, frame rate belongs to `frames`. An agent loading one skill gets a pointer, not a duplicated body, which keeps the context cost of a loaded skill low.

## Usage

| You say | What happens |
|---|---|
| "Audit the uncommitted diff" | Runs every skill against the diff, cites rule ids from the owning skills, returns one ranked report with a Block or Approve verdict |
| "Check the alignment of this page" | Measures rendered ink at a 2x scale factor, drops findings the pixels do not show, returns a numbered report with crops |
| "Verify this change" | Opens the running result, clicks the new controls, then states the route or menu path where the user can see it |
| "Break down this button animation" | Returns a state machine plus a timeline of every animated property on a page you can scrub and edit |
| "Sweep the breakpoints" | Renders every width and the breakpoint edges, a short landscape phone and 200% text, then reports overflow and clipping |
| "Trace why this feels janky" | Records a performance trace on a throttled CPU, names what drops frames, then proves the fix with a second trace |
| "Build me three variants of this filter bar" | Builds labelled variants on one page, collects your pick, then deletes the rest |

The user-invoked procedures matter here. `ship`, `prototype`, `lab`, `deconstruct`, `alignment`, `keyboard`, `frames`, `avatar`, `bots`, `sketchbook` and `audit` set both `disable-model-invocation: true` in frontmatter and `allow_implicit_invocation: false` in `agents/openai.yaml`. The repository's own rule is to set both or neither, so a half-configured skill is a bug rather than a preference.

## Verification

Read one principle and one procedure before installing. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/raphaelsalaja/skills/main/skills/motion/SKILL.md | head -40
```

It should open with frontmatter naming `motion` and a one-sentence description covering what animates, easing, durations, springs, gestures, exits, motion blur and reduced motion. The first body heading is `# Motion`, followed by the hand-off paragraph that names `restraint`, `deconstruct`, `frames` and `defaults` as the owning skills for adjacent questions.

The audit skill verifies the same way and is the better sanity check on the pair format:

```bash
curl -fsSL https://raw.githubusercontent.com/raphaelsalaja/skills/main/skills/audit/SKILL.md | head -35
```

It should open with `disable-model-invocation: true` in the frontmatter and the sentence that the skill owns no interface rule, only scope, order, consolidation and the verdict.

After install, confirm the collection landed as directories rather than as a single file:

```bash
ls ~/.claude/skills | grep -E "motion|verify|audit"
```

You should see three separate entries. Each skill directory ships on its own, by design, so a relative link to a sibling would break; that is why hand-offs are written in backticks as names rather than as links.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08). Re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 12-principles-of-animation | Pass | Pass | Pass |
| alignment | Pass | Pass | Warn |
| copy | Pass | Pass | Pass |
| sketchbook | Pass | Pass | Pass |
| container-bounds | Pass | Pass | Pass |

The one non-Pass cell is Snyk's Warn on `alignment`, and it is not structural in the way a failed scan usually is. `alignment` ships and runs `measure.js` through the browser's evaluate call, passing a spacing scale as `window.__alignmentOptions`, then crops candidates from a 2x screenshot. That is a script injected into the page under test, which is the shape a static analyser flags: dynamic code, a browser evaluate path, and a file whose behaviour depends on the page it runs against. The Gen Agent Trust Hub and Socket verdicts both pass, so the warning reads as a scanner's judgement about page-injection capability rather than a discovered defect. Treat it as a reason to run the skill against pages you control.

Two related considerations from the same reading. `avatar` draws objects as animated characters and `bots` turns Grok Bots into a shareable pile, and the repository states that private details are stripped; that is a claim to check before publishing output, not a guarantee. `sketchbook` generates experiments in the project's own stack and keeps the ones you keep, so it writes code into a working tree.

Licence status is clean: MIT, with a LICENSE file in the repository root and `license: MIT` in the plugin manifest. The repository is not archived. Nothing in the install path executes beyond copying markdown, with the exception of `kit/sync.mjs` and the per-skill scripts, which only run if you work inside a clone.

## Limitations

- Snapshot data, verified 2026-11-08: 6,201 combined installs across 42 indexed listings, 62 GitHub stars, MIT, last pushed 2026-11-04. Counts drift.
- The 42 indexed listings and the 25 SKILL.md directories do not agree. 17 listing names have no directory in the snapshot: `12-principles-of-animation`, `morphing-icons`, `mastering-animate-presence`, `to-spring-or-not-to-spring`, `pseudo-elements`, `sounds-on-the-web`, `generating-sounds-with-ai`, `animation-principles`, `timing-functions`, `visual-design`, `laws-of-ux`, `interface-typography`, `exit-animations`, `synthesize-sound`, `predictive-prefetch`, `interface-sound` and `container-bounds`. Several of those are the collection's higher-install entries, so the most-installed skill in the index has no file in the repository tree.
- The security sample includes `container-bounds`, which is also absent from the directory list, so a verdict exists for a skill I could not read here.
- 62 stars is a thin signal for a collection whose output quality is high. Adoption is clustered on a handful of animation skills, and the install counts say more about topic demand than about the rest of the set.
- The collection is written for Claude Code and opencode first. Invocation syntax differs per harness: `/name` for Claude Code skills, `/userinterface:name` for the plugin, `$name` in Codex. Hermes users should expect to load these by file path or by skill name rather than by slash command.
- Some procedures assume a browser or computer-use tool. `alignment`, `viewports`, `keyboard`, `frames` and `verify` all open or measure a running page, and degrade to advice if the harness cannot drive one.
- `kit/` regions and `node kit/sync.mjs` only matter if you maintain the collection. Consumers never need Node.
- I read the README, AGENTS.md and five of the 25 SKILL.md files. The per-skill claims for the other twenty rest on the README one-liners.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)

## Pro Tips

- Start with `defaults`, `motion` and `restraint`, not with the animation skills. The principle files are what change output on every task; the procedures are what you call when something needs measuring.
- Quote rule ids in your own reviews. A finding that reads `PricingCard.svelte:41 - [motion-no-scale-from-zero]` is actionable and greppable, while a finding that reads "the entrance is too dramatic" is neither.
- Run `audit` on a diff, not on a codebase, for the first pass. The report ranks findings across every skill, and a whole-codebase run floods the ranking with legacy issues you were not going to fix today.
- Use `verify` before `audit` on any single change. `audit` assumes each changed surface was already opened in the running app, and skipping that leaves every visual rule unverifiable.
- Expect the user-invoked procedures to stay quiet. If `/alignment` fires on its own, the frontmatter or `agents/openai.yaml` is half-configured, and the repository treats that as a defect.
- Copy the pair table format into your own project rules. Broken line plus replacement line, one row per rule id, is the cheapest interface standard an agent can actually follow.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
