---
title: "Baoyu Design - Local Artifact Editors for Agents"
description: "jimliu/baoyu-design: 16.2K combined installs across 10 listings for local slide decks, design systems, dashboards, motion films and whiteboards"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/baoyu-design-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "design", "slides", "dataviz", "motion"]
---

# Baoyu Design - Setup Guide

**Source:** [jimliu/baoyu-design](https://www.skills.sh/jimliu/baoyu-design) via skills.sh - 16.2K combined installs across 10 indexed listings; first seen Jun 7, 2026 (Nov 11, 2026 sweep)
**GitHub:** 6,382 stars, GitHub reports NOASSERTION with a LICENSE file at the repository root and separate licence files per plugin, `main` branch, last pushed 2026-11-12, 818 tracked files with 25 `SKILL.md` files across `skills/`, `chatgpt-plugins/`, `dsh-plugins/` and `archive/`
**Category:** Design artifacts: slide decks, design canvases, design systems, dashboards, data visualization, motion films, whiteboards
**Quality Tier:** 🟡 Established - 6,382 stars and an unusually complete local-editor stack, held back by a Socket Fail on the flagship listing and a licence GitHub cannot classify.

This repository brings the artifact types people know from claude.ai to a local machine, as files an agent edits and an editor renders. A deck is a `deck.json` plus one HTML file per slide. A design system is tokens, a brand book and component previews. A canvas, a dashboard, a motion film and a whiteboard each get the same treatment: structured data on disk, an editor that opens it locally, and a skill that writes it.

That last part is the interesting design decision. Each `SKILL.md` keeps the original artifact instructions close to verbatim and swaps only the tool calls, so an agent that has seen Claude artifacts already knows the vocabulary. Everything runs on Node with nothing to build: the scripts ship prebuilt, and the editors serve from your own machine, which is why the README warns that a sandbox blocking local network access will block the editor.

Alongside the six editors sits `dataviz`, a chart guide the agent reads before drawing any chart in any medium, and `motion-director`, which takes a film from the point of it to a finished cut. `release-skills` is unrelated to design and lives in `.claude/skills/`: it is a universal release workflow that detects version files and changelogs for Node, Python, Rust and Claude plugins.

## Installation

The README's recommended route is the Vercel Labs skills CLI, which reads the repository and drops the skills into whatever agent it detects:

```bash
npx skills add JimLiu/baoyu-design
npx skills add JimLiu/baoyu-design -g
npx skills add JimLiu/baoyu-design --agent claude-code
```

Node 20 or newer is required for the editors; the dashboard, Motion and the whiteboard want Node 22. Nothing needs compiling, and the README states there is nothing to install beyond Node.

Three other routes exist and matter if you live in a different host. The DeepSeek Harness app installs the same editors as npm plugins by name, such as `dsh-claude-design` and `dsh-claude-slides`. The ChatGPT desktop app and Codex add the repository as a marketplace with sparse checkouts:

```bash
codex plugin marketplace add JimLiu/baoyu-design --sparse .agents/plugins --sparse chatgpt-plugins
```

Opening an editor needs local network access, which the default sandbox blocks. Approve it when the app asks, or the artifact will be written and never displayed.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| baoyu-design | 6,972 | Create or edit visual design artifacts as self-contained HTML: UI mockups, prototypes, wireframes, landing pages and app screens. |
| release-skills | 3,004 | Universal release workflow that auto-detects version files and changelogs across Node, Python, Rust and plugin repositories. |
| claude-design | 1,200 | Works in the Design canvas artifact format, one `.dc.html` Design Component per artboard, opened in a local editor. |
| claude-design-system | 1,156 | Builds design systems as tokens, a README brand book and component previews that import from a component library. |
| claude-slides | 1,098 | Builds slide decks as `deck.json` plus one HTML file per slide, editable in a local slide editor. |
| claude-dashboard | 1,087 | Builds data dashboards in the Data artifact format, written through the same local store and script. |
| dataviz | 806 | The chart guide the agent reads before drawing any chart, graph or plot, in this pack or anywhere else. |
| claude-motion | 415 | Produces a short animated film, ten to thirty seconds by default, as a local Motion project. |
| motion-director | 390 | Directs a finished motion video with a point: an explainer, a product or feature film, a data story. |

The remaining 1 indexed listing is claude-whiteboard (39 installs), a shared space for laying out thinking as diagrams, flows or maps.

The pack has drifted from its index in two ways worth knowing. `baoyu-design` still carries installs but now lives in `archive/`, superseded by the per-artifact skills, and `claude-dashboard` maps to the current `skills/claude-data/` directory after the rename the README documents.

## Why This Matters for Hermes Agents

An agent that produces a design deliverable as a screenshot or a single HTML blob has produced something you cannot edit. This pack's artifacts are structured: change the theme of a deck and every slide follows, because the deck is data and the slides are views of it.

That structure is also what makes review possible. A design system in the pack is tokens plus component previews, so a reviewer can argue about a radius value instead of arguing about whether a screen looks right. For an agent working with a non-designer, that shift is the difference between a conversation about taste and one about a number.

The local-only execution is the other half. Nothing renders on a vendor's server, the artifacts stay on disk, and the editors are ordinary Node services on localhost. For teams that cannot send unreleased designs to a third party, that constraint is the whole value.

Two caveats belong up front rather than in the limitations. This is a large repository with per-plugin licences that GitHub cannot reduce to one identifier, so read the licence of the plugin you install. And the flagship listing carries a Socket Fail, which is the reason the tier is not higher.

## Usage

| You say | What happens |
|---|---|
| "Make me a five-slide deck on our Q3 numbers" | Writes `deck.json` and one HTML file per slide, then opens the local slide editor so you can edit rather than re-prompt. |
| "Design a settings screen for this app" | Produces a self-contained HTML mockup plus a canvas project you can keep iterating in. |
| "Build a design system from our brand colours" | Creates tokens, a README brand book and component previews, importable by decks and canvases. |
| "Chart this CSV" | Reads `dataviz` first, then produces a chart with the axis, colour and annotation rules already applied. |
| "Make a 20-second product film" | Routes through `motion-director` and produces a local Motion project with the cut assembled. |
| "Whiteboard how these three services talk to each other" | Writes a whiteboard artifact as a diagram with the boxes and arrows as editable objects. |
| "Cut a release for this plugin" | Uses `release-skills` to detect the version files and changelog, bump them consistently and draft the release notes. |

## Verification

The current tree keeps the skills under `skills/`, and the plugin copies mirror them. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/jimliu/baoyu-design/main/skills/claude-design/SKILL.md | head -6
```

The archived flagship still resolves if you want to compare the old and new instructions:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/jimliu/baoyu-design/main/archive/baoyu-design/SKILL.md
```

After installing, confirm the editor payload arrived: each skill folder should hold a `scripts/` directory with `artifact.mjs`, and the dashboard, Motion and whiteboard skills should point at Node 22. If `npx skills add` wrote into an agent-specific directory instead of your profile, list that directory before assuming the install failed.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| baoyu-design | Pass | Fail | Pass |
| claude-slides | not reported | not reported | not reported |

The flagship listing draws a Socket Fail, and the sampled slide skill carries no scanner verdicts at all. A Fail here is worth reading rather than treating as a blocker: this repository ships executable scripts, spawns local servers and writes files, which is exactly the behaviour a supply-chain scanner treats as risky. It is also exactly what makes the artifacts editable.

What the verdicts do not cover is the generated output. A deck or dashboard produced by these skills is HTML rendered in a local browser with content the agent wrote, so treat a published artifact the way you would treat any generated page before it goes public.

## Limitations

- Snapshot data, verified 2026-11-11: 16,167 combined installs across 10 indexed listings; 6,382 GitHub stars; NOASSERTION with per-plugin licence files; last pushed 2026-11-12. Counts drift over time.
- The last-push date is one day after this snapshot date, which is a timezone artifact of the repository activity feed rather than an error.
- GitHub cannot classify the repository licence because the licence files are per plugin. Read the licence of the specific plugin you install rather than the repository.
- The index carries 10 listings against a current `skills/` tree of eight artifact skills plus `release-skills`, and the flagship name now points at `archive/`. Expect the index to lag the tree.
- The editors need Node 20, or Node 22 for the dashboard, Motion and the whiteboard. A sandbox that blocks local network access will write artifacts you cannot open.
- Rendering quality depends on the brand assets you supply. The component-library import is powerful and assumes you have one.

## Related

- [Baoyu Skills - Content Generation & Publishing Suite Setup](/hermes/skills/catalog/baoyu-skills-setup)
- [UI Craft - Design Engineering System Setup](/hermes/skills/catalog/ui-craft-setup)
- [Designlang Skill - Extract Any Site's Design System](/hermes/skills/catalog/design-extract-skill-setup)

## Pro Tips

- Start from a design system artifact, then build decks and canvases off it. Every later artifact inherits the tokens instead of re-deciding them.
- Ask for the artefact format by name. "A deck" and "a slides artifact" produce different structures, and only the second one is editable in the editor.
- Keep the `db/` store inside the project. That folder is where dashboards, films and boards persist, and moving the project without it loses the state.
- Let `dataviz` be read before any chart request, including charts inside a deck. It is the one skill here that improves work done outside this pack.
- Check Node before the first run. A version mismatch surfaces as a silent failure to open rather than an error message.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
