---
title: "Willem4130 Claude Code Skills - PowerPoint Designer"
description: "willem4130/claude-code-skills on skills.sh: 5.4K combined installs; one elite PowerPoint designer skill with brand styles and slide templates."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/willem4130-claude-code-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "powerpoint", "presentations", "slides"]
---

# Willem4130 Claude Code Skills - Setup Guide

**Source:** [willem4130/claude-code-skills](https://www.skills.sh/willem4130/claude-code-skills) via skills.sh - 5.4K combined installs across 1 indexed listing; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 9 stars, no licence file in the repository root (the README's License section says MIT), last pushed 2025-11-11, one SKILL.md at `skills/elite-powerpoint-designer/SKILL.md` with `scripts/`, `templates/` and `examples/` beside it
**Category:** Slide design for agents: one elite PowerPoint designer skill covering layout, typography and template rules
**Quality Tier:** 🟡 Usable with review - there is no LICENSE file in the repository root even though the README's License section says MIT, so the grant is asserted in prose only; the sampled audit passes on all three engines.

The repository calls itself a playground, and that framing is accurate: it is a development workspace for custom Claude Code skills with one skill promoted to production, `elite-powerpoint-designer`. That single skill accounts for all 5,382 indexed installs.

What it contains is a design system rather than a converter. The SKILL.md defines five brand styles with concrete palettes and type scales (Tech Keynote, Corporate Professional, Creative Bold, Financial Elite, Startup Pitch), a markdown to slide type mapping, a spacing and typography table, animation timings per brand, and a six step workflow that starts with a content analyzer and ends with a consistency check. The intent is a deck that looks like it came from a design team rather than from a template gallery.

Two dependencies are worth knowing before you install. Deck generation runs against the Office-PowerPoint-MCP-Server, which supplies the 25 plus slide templates the skill maps onto, and the Python side needs `python-pptx`, `pillow` and `pyyaml`. Neither is bundled here.

## Installation

The README's recommended route is a clone and a copy into the global skills directory, which makes the skill available in every project:

```bash
# Clone this repository
git clone https://github.com/willem4130/claude-code-skills.git
cd claude-code-skills

# Install globally (works in all projects)
cp -r skills/elite-powerpoint-designer ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/elite-powerpoint-designer/
```

For a single project, copy it into the project instead and commit it so the team gets it:

```bash
mkdir -p .claude/skills
cp -r /path/to/claude-code-skills/skills/elite-powerpoint-designer .claude/skills/
git add .claude/skills/elite-powerpoint-designer
git commit -m "Add elite PowerPoint designer skill"
```

The deck generation dependencies come from the skill's own README:

```bash
pip install python-pptx pillow pyyaml
```

There is no skills CLI command and no plugin marketplace entry for this repository. Updates are manual: pull the repository and copy the directory again.

## What It Provides

One listing, far above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| elite-powerpoint-designer | 5,382 | Building PowerPoint decks from markdown: five brand styles, slide type detection, a 25 plus template map, animation timing rules and a consistency checklist |

No indexed listings fall below the 500-install threshold; the single listing appears above.

## Why This Matters for Hermes Agents

Presentation output is where an agent's defaults are most visible. Left alone, a model produces slides with too much text, inconsistent margins, one font size for titles and body, and bullet lists where a comparison table belonged. The damage is not technical, it is reputational: a deck is usually the artifact a client or an investor actually sees.

This skill attacks that with constraints. The typography table fixes a range per level (hero titles 72 to 96 point, body 24 to 28 point, captions 18 to 20), the spacing system fixes gutters and margins, and the animation rules cap transitions at one or two types per deck and animated elements at three per slide. Constraints of that shape are exactly what a language model needs, because they convert "make it look good" into numbers.

The brand style table does similar work for tone. Choosing Financial Elite rather than Tech Keynote changes the palette, the typeface family and even the transition durations, so an agent asked for an investor deck has a defensible starting point instead of an average of every deck in its training data.

The content analyzer is the part that makes the workflow repeatable: point it at a markdown file and it scores the content type and audience, then recommends a style, which gives the agent a rationale to show you before generating anything.

## Usage

| You say | What happens |
|---|---|
| "Turn this markdown into an investor deck" | Runs the analyzer, selects a style, maps headings and metrics to slide types, then applies the matching type scale |
| "Make a product launch keynote" | Picks Tech Keynote: black and white with an accent blue, single focal point per slide, push and fade transitions |
| "This deck feels cluttered" | Applies the minimalism rules, one idea per slide, capped bullet counts, gutters from the spacing table |
| "Keep the animations subtle" | Uses the animation guidelines: one or two transition types, 0.3 to 0.8 second durations by brand, three animated elements maximum |
| "Which slide type is this section?" | Maps content to the template table: process to process flow, comparison to before and after, quote to testimonial, data to chart |
| "Our fonts and colors are drifting across slides" | Walks the consistency checklist: two font families maximum, palette from the design tokens, spacing from the system |

## Verification

Read the skill before installing, since it carries the whole design system:

```bash
curl -fsSL https://raw.githubusercontent.com/willem4130/claude-code-skills/main/skills/elite-powerpoint-designer/SKILL.md | head -5
```

It should open with `name: elite-powerpoint-designer` and a description about creating world class PowerPoint presentations. Then confirm what actually shipped with the skill, because the asset list matters more here than in a markdown-only skill:

```bash
ls -R ~/.claude/skills/elite-powerpoint-designer
```

Expected at the top level: `SKILL.md`, `README.md`, `scripts/`, `templates/` and `examples/`. `scripts/` should contain `analyze_content.py`, and `templates/` should contain `ANIMATION_GUIDE.md` and `brand-styles.json`. Then confirm the Python dependencies import before generating a deck:

```bash
python3 -c "import pptx, PIL, yaml; print('deps ok')"
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| elite-powerpoint-designer | Pass | Pass | Pass |

This skill is not markdown only. It ships `scripts/analyze_content.py`, which reads a markdown file and prints a style recommendation; the file imports `sys`, `json`, `re` and `typing` only, so it runs on the standard library and makes no network calls. Deck generation is a different matter, since it depends on `python-pptx`, `pillow`, `pyyaml` and the external Office-PowerPoint-MCP-Server, and those are outside this repository's audit surface.

The licensing position needs care. The README's License section states MIT, but there is no LICENSE file in the repository root, so the repository does not actually carry the grant it claims. Treat reuse as unresolved until a license file exists.

## Limitations

- Snapshot data, verified 2026-11-05: 5,382 combined installs across 1 indexed listing; 9 GitHub stars; no license file; last pushed 2025-11-11. Counts drift over time.
- The README says MIT and the repository has no LICENSE file. GitHub therefore reports no license, and the MIT claim is unverifiable in the tree.
- Step 6 of the workflow calls `python scripts/validate_consistency.py`, but `scripts/` contains only `analyze_content.py`. The consistency check cannot run as written, so the checklist has to be applied by the agent reading the tables.
- The 25 plus slide templates come from Office-PowerPoint-MCP-Server, not from this repository. Without that server installed and configured, the template mapping has nothing to map onto.
- The repository is a personal playground with one production skill. Last push is 2025-11-11 and the star count is 9, so expect stale paths and no upstream fixes.
- Installation is copy based, with no skills CLI or plugin marketplace entry. Updating means pulling the repository and overwriting the directory, which is easy to forget.

## Related

- [powerpoint - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/powerpoint-setup)
- [Claude Office Skills - XLSX, DOCX and PPTX Setup](/hermes/skills/catalog/tfriedel-claude-office-skills-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)

## Pro Tips

- Run the analyzer first and disagree with it out loud. It scores keywords, so a dry financial report with the word "growth" in it can be read as a pitch, and an explicit style override in the frontmatter settles it.
- Put the style and accent color in the markdown frontmatter. The skill reads `style`, `accent-color` and `animations`, which is more reliable than describing the look in prose.
- Replace the missing consistency script with a checklist pass. Ask the agent to list every font family and hex color used in the deck, then compare that against the brand style table.
- Cap the outline before generating slides. Ten to fifteen slides with one idea each beats thirty slides where the agent has to invent content to fill them.
- If you need PPTX output without the MCP server, use the design tables as a spec and let your own tooling build the file. The palette and type scale are the valuable part; the template binding is the fragile part.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
