---
title: "HTML PPT Skill - Slide Decks From an Outline"
description: "lewislulu/html-ppt-skill: 21.2K installs on 1 listing; one skill for 36-theme static HTML decks with presenter mode and speaker notes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/html-ppt-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "presentations", "html", "slides"]
---

# HTML PPT Skill - Setup Guide

**Source:** [lewislulu/html-ppt-skill](https://www.skills.sh/lewislulu/html-ppt-skill) via skills.sh - 21.2K combined installs across 1 indexed listing; first documented November 4, 2026 (morning sweep)
**GitHub:** 8,974 stars, MIT, last pushed 2026-09-14, a single SKILL.md at the repository root (no skills/ directory)
**Category:** Presentations for agents: single-file HTML decks, layouts, typography and speaker notes generated from an outline
**Quality Tier:** 🟡 Yellow: html-ppt draws a Socket Warn, and every one of the 21.2K installs rides on that single listing

HTML PPT Studio is one skill that produces presentational HTML: static files, no build step, no framework. A deck is assembled from a theme token file, a page layout, and optional animation classes, all sharing the design system in `assets/base.css`. The README describes it as 36 themes, 15 full-deck templates, 36 single-page layouts and 47 animations (27 CSS plus 20 canvas FX).

A handful of engineering choices make it more than a template dump. The keyboard runtime handles navigation, theme switching and presenter mode in one file. Five layouts take real images, selected by how many images a page must carry. And the presenter window is a set of draggable, resizable cards whose previews are iframes loading the same deck with a preview query parameter, so the preview shares the exact CSS and fonts of the audience view.

## Installation

The README leads with one command, given as a full URL rather than an owner/repo pair:

```bash
npx skills add https://github.com/lewislulu/html-ppt-skill
```

Without network on the target machine, the README offers a local copy first:

```bash
git clone https://github.com/lewislulu/html-ppt-skill
npx skills add ./html-ppt-skill
```

And a hand copy, for an agent that scans a directory rather than using the CLI:

```bash
mkdir -p ~/.claude/skills
cp -R html-ppt-skill ~/.claude/skills/html-ppt
ls ~/.claude/skills/html-ppt/SKILL.md
```

The README's manual install table maps the same folder into other runtimes: `.agents/skills/html-ppt/` for Codex, Cursor, OpenCode and Gemini CLI, `~/.windsurf/skills/html-ppt/` for Windsurf. Only `SKILL.md`, `assets/`, `templates/`, `references/` and `scripts/` are needed at runtime; `docs/` is README artwork and can be dropped from an offline copy.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| html-ppt | 21,226 | Themes, layouts, animations and presenter mode for static HTML decks |

No indexed listings fall below the threshold; the single indexed listing appears above.

## Why This Matters for Hermes Agents

Presentation output is one of the few deliverables a team still judges visually, and it is where generated HTML usually looks generated. This skill bounds the problem: a fixed theme set, a fixed layout set and a shared token system mean the agent composes pages instead of inventing CSS, which is the difference between a deck that looks designed and one that looks like a bootstrap page.

The presenter mode is the feature worth studying. Speaker notes are not an afterthought bolted onto a slide body; the README's authoring rules are specific, at 150 to 300 words per slide, prompt signals rather than sentences to read, and written the way the speaker talks. An agent that follows those three rules produces notes a human can actually present from.

The offline story is also honest, which matters for agent fleets on restricted networks. Everything is local static files except one webfont `@import`, and the fallback stack is already declared, so a deck still renders without Google Fonts, just in different typefaces.

The cost is breadth: one skill, one structure. You get choices, not guidance on which theme suits a board update versus a launch keynote, and that judgment stays with the caller.

## Usage

| You say | What happens |
|---|---|
| "turn this outline into a pitch deck" | Scaffolds the pitch-deck full-deck template and fills slides from the outline |
| "an 8-page technical sharing deck in a cyberpunk theme" | Applies the cyberpunk-neon theme tokens and builds pages from single-page layouts |
| "add speaker notes to every slide" | Uses presenter-mode-reveal and writes 150 to 300 words into each slide's notes block |
| "open the presenter view" | Press S for current, next, script and timer cards in a synced popup window |
| "export the slides as PNG" | render.sh drives headless Chrome over the deck file and writes images |
| "make a 3:4 Xiaohongshu picture set" | Combines the xhs-post full-deck template with a white editorial theme |
| "switch theme while presenting" | Press T to cycle theme CSS without leaving the deck |

## Verification

Fetch the raw skill file to confirm the repository still ships SKILL.md at the root rather than under a skills directory. This URL returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/lewislulu/html-ppt-skill/main/SKILL.md | head -30
```

A response with `name: html-ppt` in the frontmatter confirms the layout the pack recorded. After a manual copy, confirm the entry file landed where the agent scans:

```bash
ls ~/.claude/skills/html-ppt/SKILL.md
```

Then scaffold one deck to check that the templates and scripts travelled with it:

```bash
cd ~/.claude/skills/html-ppt && ./scripts/new-deck.sh smoke-test
```

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| html-ppt | Pass | Warn | Pass |

## Limitations

- Snapshot data, verified November 4, 2026: 21,226 combined installs across 1 indexed listing; 8,974 GitHub stars; MIT; last pushed 2026-09-14. Counts drift over time.
- One indexed listing carries the whole install count, so there is no second data point to confirm the number or the skill's scope.
- The GitHub repo description is behind the README: it says 24 themes, 31 layouts and 20+ animations, while the README's box table and SKILL.md say 36 themes, 36 layouts and 47 animations.
- The README is also internally inconsistent on layouts: the box table says 36 single-page layouts while its own project tree still lists 31 layout files. Treat the layout count as approximate.
- `assets/fonts.css` imports Google Fonts, the only remote dependency. On an air-gapped machine decks fall back to the system stack unless you replace the imports.
- The Socket Warn means the skill's assets and scripts should be read before they are pointed at a shared or production machine.

## Related

- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)
- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup)
- [claude-design - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/claude-design-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Browse before authoring. `templates/theme-showcase.html`, `layout-showcase.html` and `full-decks-index.html` render every option, which is faster than reading the CSS.
- Start from a full-deck template when the deck has a genre (pitch, launch, tech talk, weekly report) and from single-page layouts when it does not.
- Keep the 150 to 300 word speaker note rule. Shorter notes read as bullet lists in the presenter window, longer ones stop being prompts.
- Drop `docs/` from an offline copy. It is several megabytes of README artwork with no runtime role.
- Render to PNG and look at it. The README ships a render script, and visual defects are cheaper to catch in a screenshot than in a live presentation.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
