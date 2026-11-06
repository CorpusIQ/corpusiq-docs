---
title: "Obsidian Visual Skills - Canvas, Excalidraw and Mermaid"
description: "axtonliu/axton-obsidian-visual-skills on skills.sh: 6.7K combined installs across 3 listings; Excalidraw, Mermaid and Canvas files from plain text."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/axton-obsidian-visual-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "obsidian", "diagrams", "excalidraw"]
---

# Obsidian Visual Skills - Setup Guide

**Source:** [axtonliu/axton-obsidian-visual-skills](https://www.skills.sh/axtonliu/axton-obsidian-visual-skills) via skills.sh - 6.7K combined installs across 3 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 3,677 stars, MIT licence, last pushed 2026-02-11, three SKILL.md directories at the repository root plus a .claude-plugin marketplace manifest
**Category:** Obsidian vault visuals for agents: canvas boards, Excalidraw sketches and Mermaid diagrams generated from text
**Quality Tier:** 🟢 Production - all three sampled audits Pass; MIT; 3,677 stars.

Three skills, one for each visual format an Obsidian vault actually uses. `excalidraw-diagram` produces hand-drawn style diagrams in three output modes: an Obsidian `.md` file with embedded Excalidraw JSON, a standard `.excalidraw` file for excalidraw.com, and an animated `.excalidraw` file whose elements carry an animation order. `mermaid-visualizer` writes Mermaid source with syntax error prevention built into the reference set. `obsidian-canvas-creator` writes JSON Canvas files in MindMap or freeform layout.

The package is small on purpose. Each skill is a folder at the repository root holding a `SKILL.md` and a `references/` directory with the schema or syntax rules; the Canvas skill adds an `assets/` directory of template canvas files. The Excalidraw skill ships the element schema, the Canvas skill ships layout algorithms and the JSON Canvas spec, and the Mermaid skill ships the syntax rules that keep a generated diagram from failing to render. Nothing here is a script: the agent writes files.

The repository is public, MIT licensed, and describes itself as experimental. It has been installed more than six thousand times across the three listings, which is a strong signal for a pack that has not been updated since February 2026.

## Installation

Claude Code installs the whole pack through the plugin marketplace the repository ships. Run both lines, then restart the client so the skills load:

```text
/plugin marketplace add axtonliu/axton-obsidian-visual-skills
/plugin install obsidian-visual-skills
```

The manual route clones the repository and copies the skill folders into the skills directory. Copy only the ones you want if the vault does not use all three formats:

```bash
git clone https://github.com/axtonliu/axton-obsidian-visual-skills.git
mkdir -p ~/.claude/skills
cp -r axton-obsidian-visual-skills/excalidraw-diagram ~/.claude/skills/
cp -r axton-obsidian-visual-skills/mermaid-visualizer ~/.claude/skills/
cp -r axton-obsidian-visual-skills/obsidian-canvas-creator ~/.claude/skills/
```

For a project-scoped install, copy into `.claude/skills` inside the project instead of the home directory. The README lists two prerequisites: the Claude Code CLI, and Obsidian with the Excalidraw plugin for the Excalidraw skill. Mermaid rendering needs a Mermaid-capable renderer, which Obsidian has natively.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| excalidraw-diagram | 3,032 | Hand-drawn style diagrams from text, written as Obsidian markdown, a standard .excalidraw file or an animated file with a set element order |
| obsidian-canvas-creator | 2,001 | JSON Canvas boards in MindMap or freeform layout, with sized nodes, labeled edges and color-coded groups that open directly in Obsidian |
| mermaid-visualizer | 1,685 | Mermaid source for flowcharts, sequence diagrams, architecture views, comparisons and mindmaps, written against syntax rules that prevent render errors |

No indexed listings fall below the 500-install threshold; all three appear above.

## Why This Matters for Hermes Agents

An agent asked for a diagram usually returns Mermaid text or an ASCII sketch, because that is what fits in a chat reply. That answer is fine in a README and useless in a vault. The file formats here are the ones Obsidian actually opens: JSON Canvas for a board a person can drag around, Excalidraw JSON for a sketch they can edit by hand, Mermaid fenced blocks for anything that should re-render when the text changes.

The harder problem is validity. Excalidraw and JSON Canvas are both JSON schemas, and a model writing JSON from memory produces files that look right and fail to open: an element without the required id, an edge pointing at a node that does not exist, a group whose bounding box does not contain its children. Each skill carries the schema and the layout rules in `references/`, so the agent writes against a specification instead of a recollection.

Canvas work also needs geometry. Node sizing by text length, spacing that prevents overlap, and edge routing are layout decisions that a language model gets wrong by default and gets right when the skill states the algorithm. The Canvas skill's freeform mode is the case where this shows: without spacing rules, a generated board is a pile of overlapping cards.

The third piece is the output mode switch. The same request in the same session can need a vault-native markdown file, a file to share on excalidraw.com, or an animated one for a demo. A single sentence in the prompt selects the mode, and the skill documents the trigger words for each, including the Chinese phrases the author uses.

For a Hermes agent working in a knowledge base, this is the difference between describing a system and leaving an artifact in the vault next to the note that describes it.

## Usage

| You say | What happens |
|---|---|
| "Create an Excalidraw flowchart of the CI/CD pipeline" | Writes an Obsidian markdown file with embedded Excalidraw JSON, in hand-drawn style |
| "Make a standard Excalidraw file of this architecture" | Switches to standard mode and writes a `.excalidraw` file that opens on excalidraw.com |
| "Animate this diagram" | Writes an `.excalidraw` file with an animation order, ready for excalidraw-animate |
| "Visualize the auth flow as a Mermaid sequence diagram" | Writes Mermaid source with the participants and message order the flow implies |
| "Turn this article into an Obsidian Canvas" | Produces a `.canvas` board with card nodes and edges, in MindMap layout by default |
| "Make a freeform canvas of these services" | Switches to freeform layout with custom positions and labeled connections |
| "Make a mind map canvas for the project plan" | Produces a MindMap canvas with a central node and a radial hierarchy around it |

## Verification

Read the skill the installer will place before trusting it. The raw path is the repository root, and the branch is `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/axtonliu/axton-obsidian-visual-skills/main/excalidraw-diagram/SKILL.md | head -4
```

It should open with `name: excalidraw-diagram` and a description naming the three output modes. Then confirm the folders landed with their references, since a copy that takes only `SKILL.md` loses the schema:

```bash
ls ~/.claude/skills/excalidraw-diagram
ls ~/.claude/skills/obsidian-canvas-creator
```

The first should list `SKILL.md` and `references/`; the second should list `SKILL.md`, `assets/` and `references/`. Finally, open one generated file in Obsidian. A canvas that opens blank or an Excalidraw file that reports invalid JSON means the agent wrote from memory instead of reading the reference.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| excalidraw-diagram | Pass | Pass | Pass |
| obsidian-canvas-creator | Pass | Pass | Pass |
| mermaid-visualizer | Pass | Pass | Pass |

The install surface is markdown and JSON templates. There are no scripts, no hooks, no network calls and no credentials in any of the three skill folders, which is why the three audits agree. The risk that remains is at the destination rather than the source: the skills write files into your vault, so run them in a vault you can inspect, and check the path in the file the agent offers to write before accepting it.

## Limitations

- Snapshot data, verified 2026-11-05: 6,718 combined installs across 3 indexed listings; 3,677 GitHub stars; MIT; last pushed 2026-02-11. Counts drift over time.
- The README marks the project Experimental and says the author's focus is demonstrating how tools work together rather than maintaining the codebase. Expect edge cases in large inputs.
- The Excalidraw skill needs the Obsidian Excalidraw plugin installed and enabled. The `.md` mode targets that plugin, so choose standard mode when the file has to open somewhere else.
- Chinese text in Excalidraw output depends on a CJK handwriting font loaded from excalidraw.com at runtime. Offline or firewalled vaults fall back to a non-handwriting font unless the fonts are installed locally, which the README documents as a troubleshooting section.
- Three skills, three formats. There is no generic diagram skill: if the target is a PNG, a Graphviz file or a draw.io document, this pack does not cover it.
- The schemas are pinned to whatever Excalidraw and JSON Canvas accepted in February 2026. A breaking change in either format is not tracked by this repository until the author updates it.

## Related

- [Obsidian Agent Skills Setup Guide](/hermes/skills/catalog/obsidian-skills-setup)
- [excalidraw - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/excalidraw-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)

## Pro Tips

- Say the mode in the prompt. "Standard Excalidraw" and "animate" are documented triggers, and they are cheaper than generating the default and converting afterwards.
- Keep the vault path in the prompt. These skills write files, so naming the folder saves a round trip where the agent guesses between the vault root and a subfolder.
- Read `references/` once yourself. The Canvas layout rules explain why a generated board is spaced the way it is, which makes a bad layout diagnosable instead of mysterious.
- Prefer Mermaid when the diagram must survive edits. It re-renders from text; the other two formats are fixed JSON once written.
- For a long note, ask for the Canvas after the note is finished. The skill reads the content it is given, so converting a draft produces a board you will rebuild.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
