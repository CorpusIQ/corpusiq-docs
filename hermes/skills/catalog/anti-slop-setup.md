---
title: "Anti-Slop - AI Copywriting Quality Skill"
description: "miqdadbadjuber/anti-slop: 41.3K combined installs. Six skills that strip generic AI tells from UI, copy, mobile layout and code comments."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anti-slop-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "copywriting", "design quality", "code comments"]
---

# Anti-Slop - Setup Guide

**Source:** [miqdadbadjuber/anti-slop](https://www.skills.sh/miqdadbadjuber/anti-slop) via skills.sh - 41.3K combined installs across 6 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) - 7,670 stars, MIT, branch main, last pushed 2026-10-28; 6 `SKILL.md` directories under `skills/`, one per concern, with a 745-line standalone `antislop.md` at the root, a `rules/` copy for editors, a Node installer under `cli/` and before-and-after images under `assets/`

**Category:** Copywriting quality control: stripping the tells that make AI-written prose read as generic

**Quality Tier:** 🟡 Yellow - five of six sampled skills Pass all three auditors, but the core `antislop` skill carries a Trust Hub Warn

This is a filter, not a style guide, and that distinction decides whether you want it. Anti-slop does not prescribe a font, a colour or a hero layout. It removes the patterns that make generated output read as generated: the invented statistic, the em-dash rhythm, the sparkle icon, the "NEXT-GEN AI 2.0" pill, the comment that restates the line below it. Direction stays with you, which is why the README is blunt that the filter alone leaves a page with the slop gone and nothing in its place, and that UI work you intend to ship needs a `DESIGN.md` beside it.

The six skills split along the surfaces an agent touches. `antislop` is the core rulebook at 750 lines, meant to be loaded always. `antislop-ui` covers colour, layout, components, decoration, structure and motion. `antislop-copywriting` covers headlines, CTAs, tone and value propositions. `antislop-human` covers contrast, keyboard, focus states and the mobile details that exclude people. `antislop-layoutmobile` covers reflow from phone to desktop. `antislop-code` covers comment hygiene and explicitly does not touch the code. Each satellite names the core, references its rules by number and never renumbers them.

## Installation

The recommended route on a Hermes host is the installer, because it is the only one that knows Hermes exists. It asks which skills you want, whether the install is project-scoped or everywhere, and which agents you use, then copies the folders and writes the pointer that reloads the rules each session:

```bash
npx antislop-ai
```

The skills CLI is the second route, and it lands the same six folders with no pointer, so the rules are found by description alone:

```bash
npx skills add miqdadbadjuber/anti-slop
```

If you already have a Claude Code plugin marketplace in play, the plugin door installs all six:

```text
/plugin marketplace add https://github.com/miqdadbadjuber/anti-slop
/plugin install antislop@anti-slop
```

Updating is a separate command, since the rules do not update themselves:

```bash
npx antislop-ai --update
```

Two traps in that list. The npm package is `antislop-ai`; the README says the name `antislop` belongs to a different package, so `npx antislop` installs the wrong thing. And the installer's Hermes target is `.hermes/skills` in the current project, or `~/.hermes/skills` for a global install, which on this host is the default profile's skill directory rather than `~/.hermes/profiles/corpusiq/skills`. For the corpusiq profile, copy the six folders directly, and keep the core beside its satellites because every satellite references it:

```bash
git clone --depth 1 https://github.com/miqdadbadjuber/anti-slop.git /tmp/antislop
cp -r /tmp/antislop/skills/. ~/.hermes/profiles/corpusiq/skills/
```

A project-scoped installer run needs one extra step that the CLI prints as a warning: `hermes skills trust` inside the project, because Hermes gates project skills behind a one-time trust decision per repository.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| antislop | 8,144 | The core filter, loaded always: the numbered rules that stop generic UI, text and AI-shaped code, plus the two usage modes that decide when the rules are applied. |
| antislop-ui | 7,078 | Interface work: colour, layout, components, decoration, structural flow, motion and page performance, with each rule tied back to a core rule number. |
| antislop-copywriting | 6,801 | Prose: headlines, CTAs, tone, value propositions and the specific patterns that make AI-written marketing copy easy to spot. |
| antislop-human | 6,538 | Keeping an interface usable by people with different eyes, hands and setups: contrast, keyboard paths, focus and states, plus the contrast checker with its formula, reference table and script. |
| antislop-code | 6,417 | Comment hygiene only: removing decorative, obvious, stiff or loud AI-style comments while keeping the ones that carry real information, and never editing the code around them. |
| antislop-layoutmobile | 6,329 | Layouts that reflow from phone to desktop: breakpoints, scale, grids, overflow, tap targets and navigation. |

All six indexed listings clear the threshold and appear in the table.

## Why This Matters for Hermes Agents

An agent writing copy drifts toward a register that is recognisable from the first sentence: the tricolon, the "it is not just X, it is Y" turn, the em-dash aside, the invented percentage. Naming those patterns in a skill the agent loads is the only mechanism that reliably suppresses them, because a style preference stated once in a session prompt fades by the third document. `antislop-copywriting` does the naming, rule by rule, which is more useful to an agent than an instruction to "write naturally".

The accessibility half is the part people skip and the part that pays. `antislop-human` refuses to assert that a colour pairing passes; it requires running the contrast checker, or applying the formula, or falling back to the reference table, and it says outright that claiming a pair passes without checking is the most common accessibility hallucination in agent output. That is a concrete, testable rule rather than an aspiration, and the skill ships `contrast-check.py` to make it executable.

`antislop-code` is the smallest skill at 128 lines and the one with the clearest boundary: it filters comments, and it does not touch code. An agent given a general instruction to "clean up this file" will reformat working code; an agent given this skill rewrites the banner comments and leaves the logic alone.

The rules are prose, so they are advisory. Nothing enforces them. What they buy is a vocabulary the agent can be held to: when a rule is numbered and cited, a reviewer can point at R-25 and say the contrast was never tested.

## Usage

| You say | What happens |
|---|---|
| "Write the landing page copy for this launch" | The agent loads `antislop` and `antislop-copywriting`, then works the headline, the value proposition and the CTA against the named anti-patterns rather than a tone adjective. |
| "This hero section looks like every other AI landing page" | `antislop-ui` goes through the visible tells: sparkle iconography, badge pills, invented metrics, gradient text, decorative structure, and says what to remove before anything is added. |
| "Check this colour pair is readable" | `antislop-human` runs the bundled checker on the two hex values or applies the formula, instead of asserting that the pair passes. |
| "Does this layout hold up on a phone" | `antislop-layoutmobile` walks breakpoints, grids, overflow and tap targets, and covers the cases where a grid survives a narrow screen but the navigation does not. |
| "Clean up the comments in this module" | `antislop-code` removes the decorative banner and the comment restating the constant below it, keeps the one explaining why, and does not touch the code. |
| "Set the mode so it does not ask every time" | Saved as `npx antislop-ai --mode during`, and the skill announces `antislop active: during (global preference).` once per session instead of prompting. |
| "Is this page ready to ship" | The agent checks for a `DESIGN.md` first, because the README treats the filter alone as a draft without direction. |

## Verification

The raw path for the core skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} antislop\n" \
  https://raw.githubusercontent.com/miqdadbadjuber/anti-slop/main/skills/antislop/SKILL.md
```

Expect `200`. After the copy lands, confirm all six directories arrived and that the contrast checker came with its skill:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/antislop* | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/antislop/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/antislop-human
```

The count should print 6, the header should show `name: antislop` and a `description:` reading "Anti Slop: Rules for AI Coding Agents. The core filter.", and the `antislop-human` listing should contain `SKILL.md`, `contrast-check.py` and `contrast-mcp.py`. A count of 5 means the glob caught the core plus four satellites and one skill was left in the clone.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31). The core `antislop` skill carries a Gen Agent Trust Hub Warn while every other sampled skill Passes all three auditors, and the Warn is on the skill you are told to load always - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| antislop | Warn | Pass | Pass |
| antislop-ui | Pass | Pass | Pass |
| antislop-human | Pass | Pass | Pass |
| antislop-code | Pass | Pass | Pass |
| antislop-layoutmobile | Pass | Pass | Pass |

Most of the repository is markdown, and the skills themselves are instructions the model may follow or ignore. Two exceptions are worth knowing before you install. `antislop-human` declares `Bash(python *)` and `Bash(python3 *)` in its allowed tools and ships two Python files, `contrast-check.py` for the contrast maths and `contrast-mcp.py` for an MCP wrapper, so that skill can execute code where the others cannot. The repository root also carries a Node installer under `cli/` with a `package.json`, which is what runs when you type `npx antislop-ai`; read `cli/lib/install.mjs` if you want to see exactly which paths it writes, including the `AGENTS.md` pointer at project scope.

The installer touches more of the filesystem than a skills copy does. It writes into one skills folder per selected agent, adds a pointer line to that agent's entry file, and requires `hermes skills trust` before a project install is visible to Hermes. If you want a Hermes install with no writes outside the profile, use the `cp -r` route above and skip the installer entirely.

## Limitations

- Snapshot data, verified 2026-10-31: 41,307 combined installs across 6 indexed listings; 7,670 GitHub stars; MIT; last pushed 2026-10-28. Counts drift over time.
- Six listings is a small sample, and every one of them sits between 6,329 and 8,144 installs. The six skills are designed to be installed together, so the near-identical counts say nothing about which one is best.
- The top skill is the one with the Warn. `antislop` is the rulebook the other five reference by number, so skipping it is not an option, and the audit flag lands on the mandatory piece rather than an optional one.
- The filter does not add direction. The README states that anti-slop alone leaves a page with the slop removed and no visual idea behind it, that `DESIGN.md` is mandatory for UI work you ship, and that the filtered result is labelled a draft without one.
- The rules are numbering-dependent. Satellites cite core rule numbers, so a partial install leaves dangling references, and an upstream renumber would silently point every satellite at the wrong rule.
- Licensing is mixed at the file level. The repository is MIT, but `antislop-human` carries a second license file for the web-quality contrast material with a different copyright holder, so the checker's terms are not the repository's terms.
- The install surface differs by route. `npx antislop-ai` writes skills folders plus a pointer and supports twelve agents, `npx skills add` writes only the folders, and the plugin doors install from the repository directly, so "installed" means something different depending on the command you used.

## Related

- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup)
- [Humanizer Setup](/hermes/skills/catalog/humanizer-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all six or none. The satellites reference core rules by number and the core expects them to be loaded with it, so a two-skill install produces citations to rules that were never read.
- Pair it with `humanizer` rather than choosing between them. Anti-slop removes mechanical tells from UI and code as well as prose, while a prose-focused rewrite pass handles voice; the two overlap least where anti-slop is strongest.
- Save the mode once. `npx antislop-ai --mode during` stops the per-session question and makes the skill announce `antislop active: during (global preference).` instead, which keeps the transcript honest about whether the filter is on.
- For anything you intend to ship, write the `DESIGN.md` first. Without it the rules leave a plain page with no direction, and the README treats that as a draft rather than a result.
- Take the `cp -r` route on this host. The installer's global Hermes target is `~/.hermes/skills`, which belongs to the default profile here, not to `corpusiq`; copying into the profile keeps the two separate and needs no `hermes skills trust` step.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
