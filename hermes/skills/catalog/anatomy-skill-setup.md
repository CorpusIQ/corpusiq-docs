---
title: "Anatomy Skill - Isometric SVG Explainer Setup"
description: "Anatomy: 19.4K combined installs. One skill that builds interactive isometric SVG figures that explain a technical idea as a working machine."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anatomy-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-23"
tags: ["hermes skill", "agent skill", "skill setup", "isometric", "svg", "technical illustration"]
---

# Anatomy Skill - Setup Guide

**Source:** [wheresryan22/anatomy](https://www.skills.sh/wheresryan22/anatomy) via skills.sh - 19.4K combined installs across 1 indexed listing; new to this catalog in the Oct 23, 2026 sweep

**GitHub:** [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) - 19,426 stars, MIT license, last pushed 2026-10-18, branch main, the skill is the repository root, with `kit/`, `references/`, `examples/`, `evals/` and `tests/` beside it

**Category:** Design / Technical Illustration

**Quality Tier:** 🟡 Beta - MIT, 19.4K installs and 19.4K stars with Socket and Snyk both passing, but Gen Agent Trust Hub returns a MEDIUM warning because a session script reads local agent conversation logs

Anatomy is a figure-building skill with an unusual premise: to explain a technical idea, build a physical object whose working is the idea. A cache key that skips work becomes a pin-tumbler lock that only turns when every pin matches. One GPU context serving many canvases becomes a gantry plotter whose single print head visits sixteen wells. The agent then draws that object isometrically, out of many small shaded parts, in a framed card with a title, a hint and a live readout.

The output is a self-contained page of SVG and HTML, optionally with WebGL shaders that live inside the same isometric plane, and every number the figure displays comes from the same small model that moves its parts. It is the rare agent skill whose result you can judge in one look: either the drawing reads as a real object or it does not.

## Installation

Anatomy is a standard Agent Skill, so the repository root is the skill folder:

```bash
# For your agents, choosing hosts interactively
npx skills add wheresryan22/anatomy -g

# Or pin the host
npx skills add wheresryan22/anatomy -g -a codex

# Or clone it straight into an agent skills directory
git clone https://github.com/wheresryan22/anatomy.git ~/.agents/skills/anatomy
```

For Hermes, put the folder wherever the agent loads its skills and confirm the `SKILL.md` sits at the top of that folder. The usual route is the skills CLI, which writes `~/.agents/skills/anatomy` for Codex and the equivalent directory for the other supported hosts.

There is nothing to install and no key to set. The kit uses only Node's built-in modules; the requirements are Node.js 20.10 or newer and Chrome or Chromium for the geometry and rendering checks.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| anatomy | 19,442 | Builds an interactive isometric figure that explains a technical idea as a physical object: many small precision parts, four-tone shading, correct painter's order, a framed card with title, hint and live readout, calm eased motion on pointer and keyboard, and a self-check that zooms into every joint. Works framework-free in TypeScript or JavaScript that emits SVG and HTML, or in React and Next.js, can add WebGL shaders for fire, exhaust, water, caustics and lamp light, prints a figure as an A4 PDF, and can publish it to the Anatomy community gallery. |

No indexed listings fall below the threshold; the single listing appears above.

## Why This Matters for Hermes Agents

Documentation diagrams fail in a predictable way: a box-and-arrow chart repeats the structure of the sentence next to it and adds no understanding. A figure that behaves like an object does something a diagram cannot. The reader recognises the machine, then recognises the idea inside it, and the explanation is carried by the drawing rather than by prose.

For a Hermes agent this is the difference between producing a PNG that needs a designer to fix and producing an artifact that ships. The skill carries a geometry kit, a set of reference documents for shading, motion, WebGL, print and verification, and nine example projects to open before starting, so the agent is composing inside a system rather than improvising from an empty file.

It is also a case where the verification loop matters more than the drawing. The examples ship an audit mode that proves, at rest and in every replayed frame of an animation, that no part passes through another, that every end sits on a real mount, and that overlaps are drawn in depth order. That is the kind of check an agent can run without a human looking at the picture.

## Usage

| You say | What happens |
|---|---|
| "Make an isometric figure for the docs page explaining our retry with backoff" | The skill invents a physical object whose working is the concept, builds it from the kit, and delivers a framed card with a live readout that moves. |
| "Illustrate how a cache key skips work when nothing changed" | The agent builds a mechanism that visibly only turns when the parts match, and the readout reports the state. |
| "I need a premium technical drawing for the landing page, Linear style" | The skill treats the style as a craft constraint: precise parts, four-tone shading, quiet motion, no clip art. |
| "Add fire and steam to the engine figure" | WebGL layers are registered to the isometric planes, so the shader sits inside the drawing instead of on top of it. |
| "Print this as an A4 poster" | The print reference and the print script produce a sheet from the same model the figure animates. |
| "Check the drawing before I publish it" | The audit pass reports clearances, mounts, bends and depth order per frame rather than leaving correctness to the eye. |

## Verification

The skill is the repository root, so a single fetch confirms the install target:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  "https://raw.githubusercontent.com/wheresryan22/anatomy/main/SKILL.md"
```

Read the skill and the two references that decide quality before the first real figure:

- https://raw.githubusercontent.com/wheresryan22/anatomy/main/SKILL.md
- https://raw.githubusercontent.com/wheresryan22/anatomy/main/references/craft.md
- https://raw.githubusercontent.com/wheresryan22/anatomy/main/references/verify.md

The repository also commits its built example pages, so the fastest acceptance test is to open one of them and then ask for the smallest example, `examples/dial-indicator`, which the skill describes as about 300 lines in total. If the agent cannot reproduce that scale, it is composing from imagination rather than from the kit.

## Security

skills.sh verdicts for the single skill (verified October 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| anatomy | Warn | Pass | Pass |

The Gen Agent Trust Hub report is specific and worth reading before install. It rates the skill MEDIUM and names four categories: data exfiltration, command execution, dynamic execution and indirect prompt injection. The evidence is `scripts/session.mjs`, which reads conversation logs from the local agent directory under `~/.claude/projects` to compute token and time metrics, plus the scripts that drive a headless Chrome and publish figures to a gallery. None of that is required to build a figure.

Two practical consequences. Run the skill with the smallest local agent-log history you can accept being read, or remove the session script from your copy if you do not want the metrics. And treat the gallery publish step as a separate decision from drawing: publishing uploads your figure, so it should be an explicit request rather than a step the agent takes on its own.

## Limitations

- Snapshot data, verified October 23, 2026: 19,442 combined installs across 1 indexed listing; 19,426 GitHub stars; license MIT; last pushed 2026-10-18. Counts drift over time.
- One auditor warns on this skill. The two Pass results do not cancel that out; read the report in Security and decide for your own data.
- The skill needs Chrome or Chromium locally for its capture and verification scripts. A headless environment without a browser can build but cannot check.
- The SKILL.md text describes eight complete examples while the current tree carries nine example directories. The extra one is not documented in the prose, so open the directory listing before assuming which are canonical.
- Quality is the whole product here. A small or vague request produces a drawing that reads as clip art, and the skill's own craft references are the only thing preventing that.
- Publishing to the gallery is a public action and is not part of the drawing loop.

## Related

- [Archify - Interactive Architecture Diagram Skill Setup](/hermes/skills/catalog/archify-setup)
- [System Atlas - Explorable Architecture Map Skill Setup](/hermes/skills/catalog/system-atlas-setup)
- [impeccable-design-polish - Post-Generation Design Polish Setup](/hermes/skills/catalog/impeccable-design-polish-setup)

## Pro Tips

- Ask for the physical object first, in words, before any drawing. The skill works best when the metaphor is decided by a human and the build is delegated.
- Open `examples/dial-indicator` before every new figure. It is the cheapest reminder of the part vocabulary and the file layout.
- Run the audit before you look at the picture. Geometry errors are invisible at normal zoom and obvious in the report.
- Keep the live readout honest. Every number it shows must come from the model that moves the parts, otherwise the figure teaches the wrong thing.
- Use the print path for anything that will be pasted into a deck. An A4 sheet from the same model beats a screenshot of an animated page.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
