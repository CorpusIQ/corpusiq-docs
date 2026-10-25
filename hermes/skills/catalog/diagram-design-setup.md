---
title: "Diagram Design - Editorial HTML and SVG Diagrams"
description: "Diagram Design: 18.8K combined installs. Forty-five diagram types as one self-contained HTML plus SVG file, matched to your brand palette."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/diagram-design-setup/"
robots: "index,follow"
last_updated: "2026-10-25"
tags: ["hermes skill", "agent skill", "skill setup", "diagrams", "svg", "design"]
---

# Diagram Design - Setup Guide

**Source:** [cathrynlavery/diagram-design](https://www.skills.sh/cathrynlavery/diagram-design) via skills.sh - 18.8K combined installs across 1 indexed listing; new to this catalog in the Oct 25, 2026 morning sweep

**GitHub:** [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) - 60,868 stars, MIT, last pushed 2026-10-24, branch main, a single skill directory `skills/diagram-design/` carrying `references/`, `assets/` and `scripts/`, plus `commands/` and `prompts/` for the host slash commands

**Category:** Design / Diagrams and Data Visualisation

**Quality Tier:** 🟢 Production - one focused skill with a written style contract, CI geometry checks, accessible SVG output and clean auditor verdicts on its only indexed listing

Most agent diagram skills produce the same artefact: a rounded box diagram in the renderer's default theme, which reads as machine output the moment it sits next to a designed page. Diagram Design attacks that specific failure. It writes one self-contained HTML file with inline SVG, using an opinionated editorial style and your own palette, and it refuses to ship the default skin into a branded project without asking first.

The style contract is what makes the output consistent. One accent colour reserved for the one or two things the reader should look at first, 1px hairlines, no shadows, every coordinate on a 4px grid, and a target density of four out of ten. Those rules are stated as taste rather than as options, which is why two diagrams drawn on different days still look like they belong to the same document.

The type coverage is the other half. Forty-five diagram types, from architecture and sequence through Sankey, Wardley map, service blueprint, exploded axonometric and architecture delta, each in a minimal light, minimal dark and full-editorial variant. Output has no build step, no JavaScript dependency and no external images, so the file opens by double click and survives being emailed.

## Installation

Any host that reads Agent Skills can install it through the cross-agent CLI:

```bash
npx skills add cathrynlavery/diagram-design
```

In Claude Code, the plugin marketplace adds the slash commands and an update path:

```text
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```

Claude Code disables auto-update for third-party marketplaces by default. After installing, run `/plugin`, open Marketplaces, select diagram-design and enable auto-update if you want merged changes to arrive on their own.

Codex, GitHub Copilot, Factory Droid and Pi have their own registration commands in the README, and the standalone CLI install does not follow marketplace updates, so pick one path rather than both. On hosts with several skills directories, the CLI offers a Symlink install: one canonical copy linked into each root, so an update reaches all of them at once.

The standalone skill install does not carry the `/export-diagram`, `/import-mermaid`, `/profile` and `/doctor` command surfaces. Those come with the native plugin packages.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| diagram-design | 18,846 | Drawing architecture, sequence, flowchart, ER, timeline, swimlane, quadrant, radar, Sankey, Wardley, Gantt, user journey, service blueprint and UML class diagrams as one self-contained HTML file, plus redrawing existing draw.io, Mermaid and Excalidraw sources in the same style. |

No indexed listings fall below the threshold; the single listing appears above.

The skill is one artefact with three surfaces. Generation covers the 45 types and their named variants. Onboarding maps a website's palette and fonts onto semantic tokens (`paper`, `ink`, `muted`, `accent`, `link`) with WCAG AA checks before writing them. Import parses `.drawio`, `.mmd`, fenced Mermaid blocks and `.excalidraw` scenes, then redraws them at a chosen size and detail level rather than converting them mechanically.

## Why This Matters for Hermes Agents

Diagrams are where an agent's output most often leaves the document it was written for. A model asked for an architecture diagram reaches for Mermaid because Mermaid is text, and the result renders in GitHub's theme rather than in the brand of the report it sits inside. For anything a client or an executive will see, that reads as a draft.

This skill changes the artefact rather than the reasoning. The agent still picks the diagram type and decides the content, but the file it produces is a finished page object: brand colours, editorial spacing, one accent that marks the point, and an accessible SVG with a title and description that survives being inlined next to others.

The accessibility detail is worth calling out because it is usually skipped. Every template gives the inline SVG `role="img"` with a resolving `aria-labelledby` and first-child title and description slots, and IDs are prefixed per diagram so several can be inlined on one page. For a Hermes agent producing documentation, that is the difference between an image a screen reader announces and an image it skips.

The honest limit is that the output is not a source format. There is nothing to diff in a pull request and no canvas to drag. For a diagram that changes every sprint, Mermaid remains the better tool. For the diagram you publish, this is the one that looks like it belongs.

## Usage

| You say | What happens |
|---|---|
| "Make me an architecture diagram of my app with frontend, backend, database and a Redis cache" | The skill picks the architecture type, states its plan, then writes one HTML file with inline SVG on the 4px grid with one accent marking the primary path. |
| "Onboard diagram-design to https://mysite.com" | The skill fetches the homepage, extracts the dominant palette and font stack, maps them onto semantic tokens, shows a proposed diff and writes the result once you approve it. |
| "I need a quadrant of Q2 projects by impact against effort" | A quadrant diagram with the axes labelled, the accent reserved for the two items that matter and the remaining items kept at reading weight. |
| "Give me a sequence diagram of a bearer call with token refresh on 401" | A sequence diagram with the combined-fragment grammar for the retry branch, drawn in the editorial variant. |
| "Redraw this drawio file for my deck" | Import parses the source, maps its pastel fills onto one accent and its hand-placed coordinates onto the grid, then exports at the requested size. |
| "Make this Mermaid block editorial" | The Mermaid source is redrawn in the style system at a chosen detail level rather than converted as-is. |
| "This diagram is too busy" | The skill cuts nodes and detail against the density target instead of shrinking the type. |

## Verification

Confirm the layout on main before installing:

```bash
curl -sL -o /dev/null -w "%{http_code} skills/diagram-design/SKILL.md\n" \
  "https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/skills/diagram-design/SKILL.md"
```

Read the style contract and the onboarding contract, which are the two files that decide whether your output looks branded or generic:

- https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/skills/diagram-design/references/style-guide.md
- https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/skills/diagram-design/references/onboarding.md

After install, the skill appears as one directory named diagram-design in your agent's skills directory. A cloned checkout also ships a local gallery at `skills/diagram-design/assets/index.html`, which is the fastest way to see all 45 types before committing to an install.

## Security

skills.sh verdicts for sampled skills (verified October 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| diagram-design | Pass | Pass | Pass |

The single indexed listing passes all three auditors. The risk model matches the code: the skill writes a file, it holds no credential and it calls no service of its own. The only network request a default diagram makes is the Google Fonts load for Instrument Serif, Geist and Geist Mono, and setting the font source to `system` removes even that.

Two things still deserve a look before production use. Onboarding fetches your website to sample colours and fonts, so it reaches the network and writes extracted values into the skill's style guide. And motion output, when you ask for it, uses a pinned controller from the repository's own template while arbitrary inline scripts and remote assets are rejected. Neither is a red flag; both are places where the skill does more than draw.

The repository's own policy files are worth knowing about: it ships `PRIVACY.md` listing what leaves the machine, and it warns that listings published under any name other than the author's company are unofficial copies.

## Limitations

- Snapshot data, verified October 25, 2026: 18,846 combined installs across 1 indexed listing; 60,868 GitHub stars; MIT; last pushed 2026-10-24. Counts drift over time.
- The board row that surfaced this source read 465 installs. A publisher query returned 18,846 for the same listing, a 40x difference, which is why single rows are not used as a size signal.
- Output is a rendered artefact, not an editable source. There is no text to diff in review and no canvas to adjust by hand; changing the diagram means asking again or editing the SVG.
- Quality tracks the model you run it with, and the same prompt can lay out differently on two runs.
- The brand onboarding writes to `references/style-guide.md`, which a package update can replace. Saved profiles in `~/.diagram-design/profiles/` survive updates, and a `.diagram-design` marker file keeps per-client brands apart.
- The standalone CLI install has no slash commands and does not follow marketplace updates.

## Related

- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)
- [System Atlas - Explorable Architecture Map Skill Setup](/hermes/skills/catalog/system-atlas-setup)
- [Anatomy Skill - Isometric SVG Explainer Setup](/hermes/skills/catalog/anatomy-skill-setup)

## Pro Tips

- Run onboarding once, before the first real diagram. The first-run gate will otherwise stop and ask, and the answer you want is a branded palette rather than the default.
- Save each client's brand as a named profile and drop a `.diagram-design` marker in that project. Parallel workspaces then use different brands without a shared style guide being overwritten.
- Set the font source to `system` for anything that has to work offline. The output then makes no network requests at all.
- Ask for the diagram type when you know it and leave it out when you do not. The skill routes intent to type and will often choose a better form than the obvious one.
- Keep Mermaid for diagrams that live in Git and change weekly. Use this for the version that goes in front of a reader.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
