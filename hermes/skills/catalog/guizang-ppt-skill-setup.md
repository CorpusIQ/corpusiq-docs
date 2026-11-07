---
title: "Guizang PPT Skill - Editorial HTML Slide Decks"
description: "op7418/guizang-ppt-skill on skills.sh: 28.4K combined installs; single-file HTML decks in editorial magazine or Swiss style, with a presenter runtime."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/guizang-ppt-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "html slides", "presentation", "design system"]
---

# Guizang PPT Skill - Setup Guide

**Source:** [op7418/guizang-ppt-skill](https://www.skills.sh/op7418/guizang-ppt-skill) via skills.sh - 28.4K combined installs across 1 indexed listing; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 29,395 stars, AGPL-3.0 licence file in the repo root, last pushed 2026-10-30, a single SKILL.md at the root with assets/, references/ and scripts/ beside it
**Category:** HTML decks for agents: magazine and Swiss layouts, image prompts, social covers and a low-power presentation runtime
**Quality Tier:** 🟢 Recommended - clean verdicts from all three scanners, 29.4K stars, a licence file at the root and a repository still taking commits; the one caveat is that the licence is copyleft AGPL-3.0, which matters if you redistribute the templates.

This is one skill that does one thing at a high standard: it turns an outline into a single-file HTML slide deck with horizontal page turns, and then helps you rehearse it. The repository is a single `SKILL.md` of 636 lines backed by two HTML templates, twelve reference files and three Node validators, with no package manifest and no build step anywhere.

Two visual systems ship with it, and choosing between them is the first decision the skill forces. Style A is editorial magazine crossed with electronic ink: serif headlines, WebGL fluid and contour backgrounds, warm colour, ten layouts. Style B is Swiss International Typographic Style: an all-sans typographic grid, one high-saturation anchor colour from International Klein Blue, lemon yellow, lemon green or safety orange, 22 locked layouts, hairline rules and no shadows or gradients. The documentation is blunt about which to use: magazine for narrative and personal voice, Swiss for facts, products and analysis.

The part that separates this from a template dump is the validation. `scripts/validate-swiss-deck.mjs` rejects centred body titles, layouts outside S01 to S22, visible SVG text and images placed outside their declared slots. `scripts/validate-presenter-mode.mjs` checks the speaker notes contract and the runtime, optionally against a target duration. The skill's own workflow gates on a P0 checklist before you ever open the deck.

## Installation

The README's one-line route, quoted verbatim:

```bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
```

The manual route is a clone into the Claude Code skills directory:

```bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill
```

The repository is also indexed on skills.sh, which publishes the short form of the same command:

```bash
npx skills add op7418/guizang-ppt-skill
```

The README also offers a third path, aimed at agents rather than people: paste an install instruction into any agent with shell access and let it create the directory, clone the repository and verify that `SKILL.md`, `assets/` and `references/` are present. That is a reasonable pattern, and it is the one most likely to leave you with a correct install on a machine you are not sitting at.

Once installed, the skill is triggered by what you ask for rather than by a slash command. The README lists the phrases that work: make me a magazine-style deck, make me a Swiss-style deck, generate a horizontal swipe deck, editorial magazine style presentation, electronic ink slides for my talk.

## What It Provides

One listing, one skill, and it clears the threshold on its own:

| Skill | Installs | Use For |
|---|---|---|
| guizang-ppt-skill | 28,412 | Single-file HTML decks in editorial magazine or Swiss style: layouts, image prompts, social covers and a presenter and rehearsal runtime |

The single indexed listing clears the 500-install threshold and appears in the table above.

What the one listing actually contains is the story. The `references/` tree holds `layouts.md` with ten paste-ready Style A skeletons, `layouts-swiss.md` with 22 locked Swiss layouts, `swiss-layout-lock.md` for the fidelity rules, `themes.md` with five electronic-ink presets, `themes-swiss.md` with four anchor-colour themes, `components.md` for the component catalogue, `image-prompts.md` for the image types and base prompts, `screenshot-framing.md` for CleanShot-style screenshot handling, `presenter-mode.md` for the notes contract, and `checklist.md`, which is 635 lines of tiered quality checks. `assets/` carries both templates plus nine WebP screenshot backgrounds.

The workflow is ten explicit steps, from choosing the style and answering a seven-question intent checklist, through copying the template and filling content, to generating speaker notes, running the self-check, previewing, rehearsing and iterating. Step 0 is not about the deck at all: it tells the agent to `git fetch` the skill directory, count the commits behind upstream, and ask before pulling.

## Why This Matters for Hermes Agents

Markdown is a poor format for a talk and a bad format for a design system. HTML gives an agent something it can read, edit and validate as text, which is why the README's "why HTML decks" section reads like a list of agent advantages: precise layout, real motion, and a format where a validator can catch drift. The Swiss validator is the clearest example, because it enforces the grid rather than describing it.

The constraint structure is the transferable idea. Style B does not say "use a grid, be tasteful". It names 22 layouts, forbids inventing new ones, fixes the anchor colour to four options, and then runs a script that fails the deck if a body title is centred or an image escapes its slot. That is a design system expressed as a machine-checkable contract, and it is what stops an agent from drifting back to the generic look after the first few slides.

The presenter runtime is the other unusual piece. All of it runs inside the local HTML file: current and next 16:9 previews, an audience window on a second display, structured notes with purpose, talking points and transitions, per-slide timing, rehearsal records, black and white screen, freeze, laser and circle annotation, and a visible disconnected state when the audience window loses its heartbeat. No cloud relay, no phone remote, no AI coaching service. Add the low-power mode, which freezes WebGL to a still frame on slow machines, and you have a presentation tool that will work on a borrowed laptop.

The output rules are strict in a way worth copying. Generated images are assets, not slides: no footer, no page number, no title inside the image, no decorative border, and the language of the labels must match the deck. Slide titles stay in HTML where they belong.

## Usage

| You say | What happens |
|---|---|
| "Turn this article into a 7-slide Swiss deck with 2-3 visuals" | The agent answers the intent checklist, copies template-swiss.html, assigns S-layouts and runs the Swiss validator |
| "Make a magazine-style deck from this Markdown" | Style A: editorial layouts, serif headlines, WebGL background, speaker notes per slide |
| "Create a 21:9 cover and a paired 1:1 share card from this deck" | Cover mode produces the WeChat main cover and the visually matched share card |
| "Redesign these screenshots as 16:10 slide visuals" | Screenshot framing keeps the raw capture and rebuilds the canvas around it at the slot ratio |
| "Add speaker notes and timing to every slide" | Notes gain purpose, talking points, transition and planned duration, then the presenter validator runs |
| "Help me rehearse this in presenter mode" | Press `P`: audience window, 16:9 previews, timers and rehearsal records, all local to the file |
| "Validate this deck before I present it" | The Swiss and presenter validators run and report layout drift, slot violations and notes gaps |

## Verification

Read the skill before installing it. This path returned 200 on `main` when checked on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/op7418/guizang-ppt-skill/main/SKILL.md | head -30
```

It should open with frontmatter naming `guizang-ppt-skill`, a Chinese description listing the two styles and their trigger phrases, and a body that begins with the source-identification block before the "what this skill does" section.

After a clone, the structure is the check, because a partial copy is the usual failure. The skill's own directory is `guizang-ppt-skill`:

```bash
ls ~/.claude/skills/guizang-ppt-skill
ls ~/.claude/skills/guizang-ppt-skill/references | wc -l
```

You should see `SKILL.md`, `assets`, `references` and `scripts`, and twelve files in `references`. If `assets/template-swiss.html` is missing, Style B will not work at all.

The validators are the functional test once you have a deck. They need Node and nothing else, since there is no package manifest and every import is a Node builtin:

```bash
node scripts/validate-swiss-deck.mjs path/to/index.html
node scripts/validate-presenter-mode.mjs path/to/index.html --target-minutes 30
node scripts/check-presenter-runtime-sync.mjs
```

A clean run prints no findings. A failure names the slide and the rule it broke, which is exactly what you want to hand back to the agent.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| guizang-ppt-skill | Pass | Pass | Pass |

The install surface is small and readable. Markdown, two HTML templates, twelve reference files and three Node scripts that import only `node:fs`, `node:path`, `node:url`, `node:module` and `node:vm`. There is no `package.json`, so there is no dependency tree to audit and nothing is fetched at install time beyond the repository itself.

The licence needs a moment of attention. The root LICENSE file carries the full GNU Affero General Public License v3 text, which is copyleft and considerably stronger than the Apache-2.0 or MIT terms most skill repositories use; skills.sh lists the licence as a custom file rather than a recognised identifier, so the label and the text disagree. Reading the file is the only reliable check. If you are embedding the templates or the presenter runtime inside a product, AGPL section 13 obligations are a question for your lawyer, not for this page.

Two behavioural notes are worth recording. The `SKILL.md` contains a provenance block naming the author and the project's sponsors, with an explicit instruction to keep that information out of generated decks and covers; that is a reasonable guard against an agent pasting sponsorship text onto a slide. And the skill instructs the agent to check for upstream updates with `git fetch` at the start of every run, which means it will offer to pull new code into your skills directory. Approve that deliberately.

Everything else runs locally. The deck is one HTML file, the presenter runtime is inside it, and the generated preview opens in your own browser.

## Limitations

- Snapshot data, verified 2026-11-06: 28,412 combined installs across 1 indexed listing; 29,395 GitHub stars; AGPL-3.0 licence file; last pushed 2026-10-30. Counts drift over time.
- One maintainer, one language. The skill body and most references are written in Chinese, with an English README as the entry point; trigger phrases work in English but the internal instructions do not.
- The style system is opinionated by design. Style B permits 22 layouts and rejects new ones, so a deck that needs a structure outside that set will fight the validator rather than extend it.
- No table or chart support worth having. The README says data-heavy tables and chart stacking belong in conventional presentation software, and the layouts reflect that.
- Static output, single author. A deck is one HTML file, which is excellent for delivery and poor for collaborative editing.
- The image flow assumes Codex. Generated visuals are described in terms of GPT-Image 2.0 and GPT-M 2.0 image types and ratios, so other harnesses get the prompts without the generation.

## Related

- [Codex PPT Skill - Image-Based Slide Decks](/hermes/skills/catalog/codex-ppt-skill-setup)
- [HTML PPT Skill - Slide Decks From an Outline](/hermes/skills/catalog/html-ppt-skill-setup)
- [html-ppt-hermes-cyber-terminal - Setup Guide](/hermes/skills/catalog/html-ppt-hermes-cyber-terminal-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Decide the style before you write a word. Style A and Style B have different layout vocabularies, and switching after the outline is built means rebuilding the rhythm rather than re-skinning it.
- Run the validator before you look at the deck. It catches centred body titles, images outside their slots and invented layouts faster than your eye will, and the fix is cheaper while the file is still being written.
- Ask for the seven-question checklist. Style, audience, duration, source material, images, theme and hard constraints: an agent that answers those first produces a deck that needs fewer passes.
- Say the ratio when you ask for a visual. Swiss hero slots are often 21:9, main visuals 16:9 or 16:10, UI scenes 16:10; a generated image at the wrong ratio gets cropped or breaks the grid.
- Keep the raw screenshot. Screenshot framing exists to rebuild the canvas around an untouched capture, and asking the model to redraw the UI is how you lose the detail you were trying to show.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
