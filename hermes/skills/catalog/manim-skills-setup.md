---
title: "Manim Skills - Math Animation for Agents"
description: "adithya-s-k/manim_skill: 7.0K combined installs across 2 listings, best-practice skills for Manim Community Edition and 3Blue1Brown's ManimGL."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/manim-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "manim", "animation", "python"]
---

# Manim Skills - Setup Guide

**Source:** [adithya-s-k/manim_skill](https://www.skills.sh/adithya-s-k/manim_skill) via skills.sh - 7.0K combined installs across 2 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 1,317 stars, MIT license, `main` branch, last pushed 2026-01-23, three `SKILL.md` files under `skills/`
**Category:** Mathematical animation and programmatic video
**Quality Tier:** 🟢 Green - both sampled skills pass all three auditors.

Manim is the framework behind 3Blue1Brown's explainer videos, and it has two incompatible editions: Manim Community Edition, which is the maintained production choice, and ManimGL, Grant Sanderson's original OpenGL implementation. This repository ships a best-practices skill for each, plus a composer skill that sits above them.

The distinction matters more than it sounds. Code written for one edition will not run on the other, the import lines differ (`from manim import *` against `from manimlib import *`), and the CLI is a different command. An agent that mixes them produces a script that fails at import, so the skills exist mainly to keep a model inside the correct dialect.

## Installation

Install both skills with the skills CLI:

```bash
npx skills add adithya-s-k/manim_skill
```

The documented prerequisites are shared by both editions: Python 3.7 or later, FFmpeg for video encoding, and a LaTeX distribution (TeX Live, MiKTeX or MacTeX) because Manim renders mathematical notation through LaTeX. Install the matching Python package for the edition you intend to use before asking an agent to write scenes.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| manimce-best-practices | 4,532 | Manim Community Edition scenes: working code examples, patterns and rendering guidance for the `manim` CLI. |
| manimgl-best-practices | 2,475 | ManimGL scenes: interactive OpenGL workflow, 3D scenes and rapid prototyping with the `manimgl` CLI. |

Both indexed listings appear in the table above. The repository also carries a `manim-composer` skill in the tree that has no install count on skills.sh.

## Why This Matters for Hermes Agents

Mathematical animation is a task where an agent can produce code that looks right and renders wrong: a transform between objects that do not share a family, an updater that fights the renderer, a camera move that only exists in one edition. The best-practices skills are largely a catalogue of those traps, with code examples rather than descriptions.

The edition split is the practical value. A user asking to "animate a Fourier series" may have ManimGL installed because that is what the original videos use; an agent that assumes Community Edition writes code the user cannot run. The skills make the edition an explicit choice with different patterns, and the repository says plainly that the two are not interchangeable without modification.

For agents in a content pipeline, this is the animation counterpart to a rendering skill. It produces a video file from a script, which means an agent can iterate against an actual artifact rather than a description of one.

## Usage

| You say | What happens |
|---|---|
| "Animate the Pythagorean theorem proof" | Writes a Community Edition scene with the shapes, transforms and LaTeX labels the skill documents. |
| "Build this 3D surface plot" | Uses the ManimGL patterns for OpenGL rendering and camera control. |
| "Why does my scene fail at import?" | Checks the import line and CLI against the edition the user actually has installed. |
| "Add captions to this animation" | Applies text and positioning patterns from the matching best-practices skill. |
| "Render it at 1080p 60fps" | Uses the documented CLI flags for the edition rather than generic FFmpeg advice. |
| "Make a 20 second explainer from this script" | Uses the composer skill to break the script into scenes before writing code. |

## Verification

Read both skill files, then confirm your installed edition:

```bash
curl -fsSL https://raw.githubusercontent.com/adithya-s-k/manim_skill/main/skills/manimce-best-practices/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/adithya-s-k/manim_skill/main/skills/manimgl-best-practices/SKILL.md | head -20
python3 -c "import manim, sys; print(manim.__version__)"
```

If the import fails, neither edition is installed and the agent should be told which one to target rather than guessing.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| manimce-best-practices | Pass | Pass | Pass |
| manimgl-best-practices | Pass | Pass | Pass |

The repository holds Markdown skills and example code only. Manim itself executes Python and shells out to LaTeX and FFmpeg, so treat rendered scenes as code execution.

## Limitations

- Snapshot data, verified 2026-11-14: 7,007 combined installs across 2 indexed listings; 1,317 GitHub stars; MIT; last pushed 2026-01-23. Counts drift over time.
- The last push predates this snapshot by ten months, so the patterns track the editions as of that date.
- The two editions are incompatible. Nothing in the repository makes ManimGL code run on Community Edition or the reverse.
- LaTeX is a hard prerequisite for mathematical typesetting, and its absence is a common first failure.
- The `manim-composer` skill exists in the tree but carries no install count on skills.sh.
- Rendering is CPU and time expensive. A long scene at high resolution can take minutes per attempt, which matters for agent loops.

## Related

- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [GSAP Skills - GreenSock Animation Platform Setup](/hermes/skills/catalog/greensock-gsap-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- State the edition in the first line of the prompt, then the topic: it prevents the most common failure before any code is written.
- Ask for a low-resolution render first and a final one at the target quality; iteration is much faster at draft settings.
- Keep LaTeX packages minimal in the scene, since a missing package fails the render rather than the text.
- For multi-scene explainers, use the composer skill to plan scenes before any Manim code exists.
- Ask the agent to print the Manim version it is coding against when a script fails twice; a version mismatch explains most repeat failures.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
