---
title: "UX Writing Skill - Interface Copy Setup"
description: "Interface copy skill: 3.1K combined installs across 1 listing, four quality standards, error patterns and accessibility rules for microcopy"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ux-writing-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "ux writing", "microcopy", "content design", "accessibility"]
---

# UX Writing Skill - Setup Guide

**Source:** [content-designer/ux-writing-skill](https://www.skills.sh/content-designer/ux-writing-skill) via skills.sh - 3.1K combined installs across 1 indexed listing (3,063 exact); first seen Jan 20, 2026 (Nov 10, 2026 sweep)
**GitHub:** 262 stars, MIT license, `main` branch, last pushed 2026-05-26, one `SKILL.md` at the repository root among 32 tracked paths, with four `references/` documents, three `templates/`, one `examples/` file and `docs/figma-integration.md`
**Category:** Product copy: interface microcopy, error and empty states, design-system voice enforcement
**Quality Tier:** 🟢 Strong - 262 stars, MIT, three Pass verdicts and a reference set loaded on demand; the one caveat is that the standards are enforced by the agent reading them, not by a checker.

This is the UX writing skill that behaves like part of a design system rather than a list of writing tips. It was built by Christopher Greer, a Staff Content Designer at Stripe, and the README traces its principles to four published sources: Sarah Richards on content design, Torrey Podmajersky on strategic writing for UX, Kiefer Lee and Fenton on voice, and Google's Material writing guidelines. The README states version 1.6.0 and a March 2026 content update, which is a more disciplined release habit than most single-skill repositories manage.

The subject is every string a product puts in front of a user: titles, buttons and links, validation and system errors, blocking and permission errors, success messages, empty states, form labels and help text, and notifications. Each pattern in the skill gets a purpose, a format rule and a fill-in pattern, and the error section splits four ways because the timing and location differ: inline validation while a field is being completed, a modal or banner after a backend failure, a full-screen block when the product cannot continue, and a permission request that has to justify itself before the OS dialog appears.

What separates it from a style guide is the scoring apparatus. Four quality standards (purposeful, concise, conversational, clear) double as an edit sequence, and the file carries numeric targets for almost everything it asks for, so a review produces a number to argue with rather than an opinion.

## Installation

The README's route is the skills CLI, which it presents as the primary path with no manual copying:

```bash
npx skills add content-designer/ux-writing-skill
```

Restart the agent or IDE afterwards, then check that it took by asking for a payment failure message. The README documents a team variant that is the same command run from a project root, with the installed skill files committed so everyone who pulls the code gets the skill.

Two constraints come straight from the README. It works with Claude Desktop, Claude Code, Codex (CLI and IDE extensions) and Cursor, and it explicitly does not work with ChatGPT, which cannot install or use skills. If the CLI does not recognise your agent, copy the package by hand into the Hermes profile skills directory and keep the folder names intact, because the `SKILL.md` refers to its references, templates and examples by relative path:

```bash
git clone https://github.com/content-designer/ux-writing-skill
cp -R ux-writing-skill ~/.hermes/profiles/corpusiq/skills/ux-writing
```

That copy carries repository files the skill does not need. The project's own `build-skill.sh` produces `dist/ux-writing-skill.zip` holding only `SKILL.md`, `docs/`, `examples/`, `references/` and `templates/`, which is the cleaner package if you want the same subset the maintainer ships.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ux-writing | 3,063 | Writes and edits interface microcopy across buttons, errors, notifications, forms, onboarding, empty states and help text, scored against four quality standards with accessibility rules and numeric benchmarks. |

No indexed listings fall below the threshold.

One listing, one skill file, and a supporting package of references, templates and examples. The `SKILL.md` holds the framework and the pattern library, then points outward: `references/accessibility-guidelines.md` for screen reader and cognitive accessibility work, `references/content-usability-checklist.md` for scoring, `references/patterns-detailed.md` for the same patterns rendered in different product voices, `references/voice-chart-template.md` for establishing a voice, and three fillable templates for error messages, empty states and onboarding flows. The README calls the loading behaviour progressive disclosure: the agent pulls a reference only when the task needs it, which is what keeps a 15KB instruction file from costing you its full size on every unrelated turn.

## Why This Matters for Hermes Agents

Interface copy is the highest-volume text an agent writes for a software product, and the default output is recognisable from a mile away: "Submit" on the button, "An error occurred. Please try again later." in the banner, "No data" in the empty state. Each of those is a small dead end, and at product scale they accumulate into an interface that feels machine-made.

The skill's numbers are what make it usable as a gate rather than a preference. Buttons are 2 to 4 words with a 6 word maximum; titles are 3 to 6 words and 40 characters; error messages are 12 to 18 words including the fix; instructions cap at 20 words with 14 as the target; lines run 40 to 60 characters; button labels sit at 15 to 25 characters. The comprehension figures behind the sentence rules are stated plainly: 8 words or fewer reads at 100 percent, 14 words at 90 percent, and 25 words is where comprehension drops off. A reviewer can point at a string and a limit instead of saying it feels long.

The accessibility section is the part most copy advice omits. Its examples are concrete and testable: "Submit application" instead of "Submit" so a screen reader announces the action, "Read our privacy policy" instead of "Click here", errors paired with the field label so both are announced together, a 4.5:1 contrast floor for WCAG AA, and no meaning carried by colour alone. For an agent building a form or a settings screen, those are the strings that decide whether the result is usable with a screen reader.

It also encodes voice as two separable things, which is the distinction agents usually collapse. Voice is the constant personality, charted through three to five brand concepts with do and don't examples. Tone is the variable, and the skill maps five emotional states to five registers: frustrated gets empathy and a recovery path, confused gets patience and steps, confident gets one word, cautious gets consequences stated plainly, successful gets a short confirmation proportional to the action.

## Usage

| You say | What happens |
|---|---|
| "Write an error message for when a payment fails" | Applies the system error pattern, names what failed, gives the likely cause and a recovery step, and lands inside the 12 to 18 word target |
| "Review this button label: Submit your information for processing" | Scores it against the four standards and returns a shorter imperative label with the character count against the 15 to 25 character range |
| "Score this error message: An error occurred. Please try again later." | Runs the content usability checklist and returns a scored critique naming the missing cause and the missing recovery path |
| "Create empty state copy for a task list, professional but friendly" | Picks the first-use empty state pattern, writes explanation plus a call to action, and holds the stated voice across the string |
| "Audit every string in this settings page" | Works through labels, helper text, success and error states, flagging generic verbs, blame language and text that repeats the label |
| "Our tone is too chummy in billing errors" | Uses the tone adaptation framework to move the frustrated register toward serious and transparent while keeping the voice concepts intact |
| "Write onboarding for a bank connection flow" | Applies the onboarding pattern with benefit before the ask, then the permission pattern for the data access request |

## Verification

The `SKILL.md` sits at the repository root, so the path is short. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/content-designer/ux-writing-skill/main/SKILL.md | head -4
```

It should open with frontmatter holding `name: ux-writing` and a description beginning `Create user-centered, accessible interface copy (microcopy)`, followed by the delimiter and the instruction body. Confirm the references came with the install, since the skill cites them by relative path:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/content-designer/ux-writing-skill/main/references/content-usability-checklist.md
test -f ~/.hermes/profiles/corpusiq/skills/ux-writing/references/voice-chart-template.md && echo ok
```

If the CLI installed into an agent-specific directory instead of the profile one, list the skills directory and check for a `ux-writing` folder holding `SKILL.md` before assuming the install failed.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ux-writing | Pass | Pass | Pass |

All three scanners pass on the single listing, which is the reason the tier is green. A Pass here is worth reading precisely. The scanners inspect what the skill ships and what it asks the agent to do, and this one ships markdown: no scripts in the skill package, no network calls, no credentials, no file writes outside its own directory. The repository has a `build-skill.sh` used to zip the package, and that script is not part of the skill the agent loads.

What a Pass does not tell you is whether the copy is any good, and it does not audit the guidance for bias, tone or accuracy of the benchmarks. Those numbers are stated as targets in the file without per-figure citations, so treat them as a considered house standard rather than a literature review. The other thing to keep in view is that the skill writes user-facing text, which is a publishing surface: a scanner passing says the skill is safe to run, not that a string it produced is safe to ship without a human read, particularly for legal, medical or billing copy.

## Limitations

- Snapshot data, verified 2026-11-10: 3,063 combined installs across 1 indexed listing; 262 GitHub stars; MIT; last pushed 2026-05-26. Counts drift over time.
- Guidance, not enforcement. Nothing in the package measures a character count or fails a build; the standards hold only as long as the agent reads and applies them, and a model that ignores the reference load will produce generic copy with the skill installed.
- The benchmarks are stated as targets inside the skill, not attributed per figure. Use them as a consistent house standard, and cite your own research if the numbers need defending in a design review.
- Activation is model-invoked. Codex offers `$ux-writing` and Cursor offers `@ux-writing`, but on Hermes the skill triggers on its description matching the request, so a vague prompt such as "fix this page" may never load it. Name the element you want written.
- The examples and tone framework are English-language and Western product context. The four standards transfer; the reading level targets, idiom warnings and voice chart do not, and need localising.
- The Figma route is documentation, not a bundled integration. `docs/figma-integration.md` describes connecting the skill through your agent's Figma MCP setup, and the skill works on pasted strings without it.

## Related

- [Anti-Slop - AI Copywriting Quality Skill](/hermes/skills/catalog/anti-slop-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)
- [UX UI Agent Skills - Design Gates for Coding Agents](/hermes/skills/catalog/ux-ui-agent-skills-setup)

## Pro Tips

- Give it the surface and the audience, not just the string. "Error for a failed card payment, consumer app, customer already frustrated" produces a usable message; "write an error" produces the generic one you were trying to avoid.
- Run the scoring path on copy you already shipped. The checklist is most valuable as an audit, and the first pass usually finds buttons that name the mechanism instead of the outcome.
- Put your voice chart in the prompt or the project. The skill can build one from three to five brand concepts, but consistency only holds across sessions if the chart lives somewhere durable.
- Ask for the count with the string. Requesting the character count alongside each suggestion is what keeps button labels inside 15 to 25 characters instead of drifting to a sentence.
- Keep a human read on anything legal, financial or medical. The skill optimises clarity and tone, not compliance, and a well-written string can still be the wrong promise.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
