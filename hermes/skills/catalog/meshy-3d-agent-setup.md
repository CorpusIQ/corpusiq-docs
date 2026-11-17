---
title: "Meshy 3D Agent - Text-to-3D Generation and Print Setup"
description: "meshy-dev/meshy-3d-agent - 6.4K combined installs across 4 indexed listings: skills for generating digital 3D assets and 3D prints with the Meshy CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/meshy-3d-agent-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "3d generation", "3d printing"]
---

# Meshy 3D Agent - Setup Guide

**Source:** [meshy-dev/meshy-3d-agent](https://www.skills.sh/meshy-dev/meshy-3d-agent) via skills.sh - 6.4K combined installs across 4 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 111 stars, MIT license, `main` branch, last pushed 2026-11-12, skills under `skills/<name>/` with a `references/` folder each
**Category:** 3D generation - digital asset creation and print preparation
**Quality Tier:** 🟢 Green - all 4 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk.

Meshy ships two skills that drive the Meshy CLI for 3D work. `meshy-3d-generation` covers digital assets: text-to-3D and image-to-3D, texturing, remeshing and LODs, UV unwrapping, format conversion, rigging, animation, and motion clips. `meshy-3d-printing` covers physical output: white and multicolor prints, printability analysis and repair, splitting into parts, Creative Lab products, sizing, and slicer handoff.

The skills are instructions and references only; no bundled runtime scripts. They drive Meshy CLI 0.8 on Node.js 22.12+ and require a paid Meshy plan (Pro or above) because generation spends credits. Sign-in is OAuth in the browser, so no API key is pasted into chat. The repo also publishes an OpenClaw single-skill build on ClawHub.

## Installation

Let your agent install it: paste the install pointer and the agent follows `INSTALL.md` through the CLI, the skills, and one browser sign-in.

By hand:

```sh
npm install -g meshy-cli@0.8
meshy --version
meshy auth login
```

Then install the skills with your host's installer, for example:

```sh
npx skills add meshy-dev/meshy-3d-agent
```

Or for Hermes Agent:

```sh
hermes skills install meshy-dev/meshy-3d-agent/skills/meshy-3d-generation
```

Or copy each whole `skills/<name>/` directory into your agent's skills directory (`.claude/skills/`, `.cursor/skills/`, or `.agents/skills/`). Replace a prior managed directory rather than merging files.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| meshy-3d-generation | 2,849 | Digital 3D assets: text-to-3D and image-to-3D, texturing, remeshing, UV, conversion, rigging, animation. |
| meshy-3d-printing | 1,995 | Physical prints: white and multicolor models, analysis and repair, parts, Creative Lab, slicer handoff. |
| meshy-3d-agent | 908 | This repository's combined listing covering both the generation and printing workflows. |
| meshy-openclaw | 627 | The OpenClaw single-skill build published on ClawHub, carrying both workflows. |

All 4 indexed listings appear in the table above; none sits below 500 installs.

## Why This Matters for Hermes Agents

For a Hermes agent doing 3D work, this suite turns a cloud generation platform into a set of CLI calls the agent can drive end to end. The generation skill handles the full asset lifecycle, from text and image prompts through texturing, remeshing, LODs, UV unwrapping, rigging, animation, and format conversion, so one skill covers the conversion and delivery steps agents otherwise fumble. The printing skill is deliberately separate and installs independently, and it controls its generation parameters from the start, so a print request stays within a budget you approve before any paid task. The cost model is disciplined: estimates come from `meshy make --dry-run` or the published price list, never from your balance, and the real charge is the task's own consumed credits. Security is handled without secrets in chat: OAuth sign-in in the browser, credentials encrypted at rest under an OS key, and the skills never read, copy, or print a token. The workspace boundary is worth copying: every writing command names an output directory and refuses paths outside it, including through symlinks.

## Usage

| You say | What happens |
|---|---|
| "Turn this photo into a textured GLB in ./assets" | Sets up the CLI if needed, signs in once, then generates the asset to the named path. |
| "Make a 1500-face LOD of that model" | Generates the lower-poly LOD for the existing task. |
| "Now export it as FBX" | Converts the existing model to FBX. |
| "Prepare this model for a multicolor 3MF print" | meshy-3d-printing analyzes, repairs, and produces the multicolor 3MF. |
| "Split this model into printable parts" | Splits the model into parts sized for printing. |
| "Hand it off to Bambu Studio" | Writes the slicer files and launches the detected slicer. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/meshy-dev/meshy-3d-agent/main/skills/meshy-3d-generation/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/meshy-dev/meshy-3d-agent/main/skills/meshy-3d-printing/SKILL.md | head -20
npx skills add meshy-dev/meshy-3d-agent
```

Each skill is one `SKILL.md` under `skills/<name>/` with a `references/` folder; confirm the path exists before copying. The meshy-openclaw listing lives in its own repository, not this tree.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| meshy-3d-generation | Pass | Pass | Pass |
| meshy-3d-printing | Pass | Pass | Pass |
| meshy-3d-agent | Pass | Pass | Pass |
| meshy-openclaw | Pass | Pass | Pass |

All 4 sampled skills pass all three scanners.

## Limitations

- Snapshot data, verified Nov 16, 2026: 6,379 combined installs across 4 indexed listings; 111 GitHub stars; MIT; last pushed 2026-11-12. Counts drift over time.
- Generation spends Meshy credits and requires a paid plan (Pro or above); a Free account can sign in but task creation is refused.
- Requires Node.js 22.12+ and the Meshy CLI; the skills ship no runtime and install the CLI separately.
- Cursor's sandbox blocks most network access, so the first sign-in needs the Meshy domains allowlisted.
- The skills never read or print tokens, but a user-supplied MESHY_API_KEY overrides the browser session if left set.

## Related

- [Blender Skills](/hermes/skills/catalog/blender-skills-setup)
- [Three.js Skills](/hermes/skills/catalog/threejs-skills-setup)
- [Game Creator](/hermes/skills/catalog/game-creator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Point the agent at `INSTALL.md` first; it walks the CLI, the skills, and one browser sign-in.
- Quote estimates from `meshy make --dry-run` or the published price list, and approve a budget before any paid task.
- Approve in the browser during `meshy auth login`; in SSH or CI use `--device` and open the printed URL.
- Add `api.meshy.ai`, `www.meshy.ai`, and `assets.meshy.ai` to Cursor's sandbox allowlist (or the `.cn` equivalents on the China site).
- Copy each skill's whole directory and replace a prior managed directory rather than merging, so stale files are removed.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
