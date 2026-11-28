---
title: "Fireworks Tech Graph - Technical Diagram Generation Skill"
description: "yizhiyanhua-ai/fireworks-tech-graph: 18.6K combined installs. Natural-language SVG, PNG and GIF technical diagrams, 12 styles and 14 types."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fireworks-tech-graph-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "diagrams", "svg", "png", "gif"]
---

# Fireworks Tech Graph - Setup Guide

**Source:** [yizhiyanhua-ai/fireworks-tech-graph](https://www.skills.sh/yizhiyanhua-ai/fireworks-tech-graph) via skills.sh - 18.6K combined installs across 1 indexed listing; first documented 2026-11-27 (evening sweep)

**GitHub:** [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) - 12,086 stars, MIT, branch main, last pushed 2026-11-26; the complete skill lives under `skills/fireworks-tech-graph/` (SKILL.md, references, scripts, schemas, fixtures, templates and tests), mirrored by a root `SKILL.md`.

**Category:** Technical diagram generation (SVG, PNG, animated GIF) for agent runtimes

**Quality Tier:** 🟡 Yellow - the single sampled skill passes Gen Agent Trust Hub and Socket but warns Snyk.

fireworks-tech-graph is one Agent Skill that works unchanged in Codex and Claude Code, published as both a Codex Skill and a Claude Code Skill. It turns natural-language descriptions, in English or Chinese, into geometry-checked SVG diagrams, high-resolution PNGs, validated SVG-to-GIF motion and offline interactive HTML. The generator ships 12 visual styles (11 generator-backed plus one AI-authored Dark Luxury style) and all 14 UML diagram types, alongside built-in AI/Agent domain patterns for RAG, Agentic Search, Mem0, Multi-Agent and Tool Call flows.

The README positions the skill against Mermaid and draw.io: natural-language input, AI/Agent patterns, 12 built-in styles, automatic 1920px PNG export and semantic arrow colors, with no online tool required. It also imports and exports Draw.io and Excalidraw, so an existing diagram library can be converted through the Fireworks JSON format rather than redrawn.

## Installation

The recommended install uses the nested skill path, which is required because a bare repository install can select only the root `SKILL.md` in current versions of the skills CLI:

```bash
npx -y skills@1.5.17 add \
  yizhiyanhua-ai/fireworks-tech-graph/skills/fireworks-tech-graph \
  --agent codex claude-code -g -y --copy
```

This creates complete copies at `~/.agents/skills/fireworks-tech-graph` for Codex and `~/.claude/skills/fireworks-tech-graph` for Claude Code, including scripts, schemas, fixtures, templates, tests and references. For an editable checkout instead, clone into either discovery path:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.claude/skills/fireworks-tech-graph
```

Python 3.9+ is required. The bundled SVG/PNG scripts need `cairosvg` (recommended, `python3 -m pip install cairosvg`) or `rsvg-convert`; optional GIF export needs FFmpeg/FFprobe, Chrome/Chromium and `puppeteer` or `puppeteer-core` installed beside the copied skill. The npm package is a separate distribution channel and may lag GitHub Releases, so use the nested GitHub path for the current version.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| fireworks-tech-graph | 18,556 | Create geometry-safe SVG technical diagrams, export PNG or offline interactive HTML, and animate supported semantic SVGs to GIF for architecture, UML, agent, cloud and workflow diagrams. |

The single indexed listing appears above.

## Why This Matters for Hermes Agents

The loop engineering is the transferable lesson here: a first render is a candidate, not a final result. The skill runs a bounded validation loop that checks deterministic structure first (XML, marker integrity, path geometry), then reads the exported PNG back to inspect clipping, label collisions and routing that syntax checks cannot see, then applies at most two targeted correction passes. Completion is reported as `validation: passed` and `visual_review: passed`, and it explicitly says `visual_review: skipped` when no image reader is available instead of claiming visual verification without evidence.

The style system is executable rather than documented: style guides are encoded into the generator, and a shared composition-quality contract enforces zero crossings, zero bridge jumps, at most two bends per edge, spacing budgets and label clearance across every style. Input goes through a versioned diagram IR with JSON schema validation, so duplicate IDs, dangling references and non-finite geometry fail before rendering instead of producing a broken SVG.

For a builder wiring this into a router, the single-file offline HTML export matters: it sanitizes the SVG, adds pan/zoom, light and dark themes and SVG/PNG/JPEG/WebP downloads, so a generated diagram can be delivered without any online dependency. The dual Codex/Claude Code packaging is also a clean pattern: one SKILL.md plus runtime-specific metadata, not two divergent forks.

## Usage

| You say | What happens |
|---|---|
| "Draw a RAG pipeline flowchart" | Renders a flowchart from the built-in RAG domain pattern with labeled arrows. |
| "Generate a Mem0 memory architecture diagram, dark style" | Classifies the task as a memory architecture diagram in Style 2 (Dark Terminal), renders the SVG and exports a 1920px PNG. |
| "Generate an Agentic Search architecture diagram" | Uses the Agentic Search pattern with planner, search and synthesis nodes. |
| "Animate this diagram as a GIF" | Validates the semantic SVG against one of 12 motion contracts and writes a 960px GIF plus a motion.json verification report. |
| "Draw an OAuth2 authorization code flow sequence diagram" | Renders a UML sequence diagram with vertical lifelines and activation boxes. |
| "Export this as an offline interactive HTML file" | Writes a single HTML file with pan/zoom, themes and SVG/PNG/JPEG/WebP downloads. |

## Verification

The raw skill path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/yizhiyanhua-ai/fireworks-tech-graph/main/skills/fireworks-tech-graph/SKILL.md
```

After a clone, confirm the bundle and the CLI:

```bash
git clone --depth 1 https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git /tmp/fireworks-tech-graph
python3 /tmp/fireworks-tech-graph/scripts/fireworks.py version
python3 /tmp/fireworks-tech-graph/scripts/fireworks.py doctor
ls /tmp/fireworks-tech-graph/skills/fireworks-tech-graph/
```

`version` reports the package, the actual skill root and git state when available; `doctor` distinguishes SVG/HTML support from the optional PNG and GIF dependencies.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fireworks-tech-graph | Pass | Pass | Warn |

The single indexed skill passes Gen Agent Trust Hub and Socket and warns Snyk. The verdict covers the skill package only; the repository also ships Python and Node scripts under `scripts/` whose dependencies the skill-level scan does not assess. Re-check the security page on skills.sh before production use.

## Limitations

- Snapshot data, verified 2026-11-27: 18,556 combined installs across 1 indexed listing; 12,086 GitHub stars; MIT; last pushed 2026-11-26. Counts drift over time.
- The skills.sh listing description mentions 7 styles while the README documents 12 visual styles and 14 diagram types; the README is the current source.
- The 12 styles, 14 diagram types, geometry-safe routing and semantic-motion guarantees are the README's own claims; verify them against your own inputs before relying on them.
- GIF motion export is optional and depends on FFmpeg/FFprobe, Chrome/Chromium and puppeteer installed beside every copied skill; PNG export needs cairosvg or rsvg-convert.
- The sampled verdict covers one skill package only: Gen Agent Trust Hub and Socket pass, Snyk warns. The bundled Python and Node scripts are outside that scan.
- The npm package is a separate distribution channel and may lag GitHub Releases, so the nested GitHub path is the authoritative install for the current version.

## Related

- [Architecture Diagram - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/architecture-diagram-setup)
- [excalidraw - Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/excalidraw-setup)
- [Design Doc Mermaid Skill - Diagram & Documentation Setup](/hermes/skills/catalog/design-doc-mermaid-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install through the nested path (`skills/fireworks-tech-graph`) so the skills CLI copies the full bundle, not just the root SKILL.md.
- Run `doctor` before requesting exports so the agent knows which optional PNG and GIF dependencies are already present.
- Add `--strict-text` to renders to reject truncated or suppressed labels before output is written.
- Remember Style 8 (Dark Luxury) is the one AI-authored style, and styles 9-12 enforce engineering semantic contracts that fail closed before rendering.
- Pin an output path in the prompt (`--output /tmp/diagrams/`) so the generated SVG and PNG land where you can inspect them.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
