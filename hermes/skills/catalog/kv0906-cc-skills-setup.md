---
title: "KV0906 CC Skills - Design and Diagram Agent Suite Setup"
description: "kv0906/cc-skills: a Claude Code skill collection for premium frontend design, SVG art, diagrams, planning and brainstorming - 2.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/kv0906-cc-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "frontend design", "svg", "diagrams"]
---

# KV0906 CC Skills - Design and Diagram Agent Suite Setup

**Source:** [kv0906/cc-skills](https://www.skills.sh/kv0906/cc-skills) via skills.sh - 2.3K combined installs across 32 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [kv0906/cc-skills](https://github.com/kv0906/cc-skills) - 52 stars, no LICENSE file, main branch, last pushed Nov 7, 2026; skills live under `skills/<name>/SKILL.md` with `references/`, `templates/` and `scripts/` kept inside each skill folder, plus a `bundles/` directory for the explanation bundle.
**Category:** Frontend Design and Visual Explanation
**Quality Tier:** 🟠 Orange - 1 Snyk Fail (debate-brainstorm) and 6 Warn cells in the 20-skill sample, plus no LICENSE file at the repository root.

Kv0906's cc-skills is a single author's distribution catalog of skills for writing, design, video and coding with AI, usable with Amp, Claude Code, Codex or any agent that supports the skills protocol. The README describes 34 standalone skills grouped by task, with 23 imported from the author's Amp setup plus a separately supplied interactive-diagram skill, each laid out under `skills/<name>/SKILL.md` with supporting references, templates and scripts kept inside the skill folder.

The skills.sh index concentrates installs at the top: premium-frontend-design (1,412) leads for cinematic WebGL and shader work, followed by svg-art (558) for programmatic vector graphics. The rest of the catalog spreads across small diagram, planning, explanation and brainstorming skills that mostly sit in the single digits, with a `bundles/explanation-skills/` directory preserving an alternative explain-to-me and its companions without replacing the standalone versions.

## Installation

The README installs skills by copying folders rather than running a package command. Download the repository, pick a skill from `skills/`, and copy its whole folder into the agent's skills directory, keeping the supporting files:

```bash
cp -r cc-skills/skills/explain-to-me ~/.claude/skills/
```

The destination depends on the agent: `.claude/skills/` for Claude Code and `.agents/skills/` for Amp or Codex. Restart the agent or ask it to reload skills afterwards. For an agent that supports the skills CLI, the whole collection installs with:

```bash
npx skills add kv0906/cc-skills
```

That form installs the repository as a whole rather than a single skill folder, so prefer the folder copy when you only need one or two skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| premium-frontend-design | 1,412 | Award-winning cinematic frontend interfaces with WebGL, custom shaders and premium animations |
| svg-art | 558 | SVG icons, logos, illustrations, charts and generative art via Python scripts |
| excalidraw | 54 | Excalidraw diagrams as JSON for flowcharts, user journeys, architecture and wireframes |
| ralph | 45 | The Ralph Wiggum loop for autonomous AI coding with clean-slate iterations and PRD features |
| planning-with-files | 39 | Manus-style persistent markdown files for planning, progress tracking and knowledge storage |
| gws | 24 | Google Workspace CLI setup to manage Gmail, Drive, Calendar and more from the terminal |
| animated-diagram | 18 | Animated technical diagrams as Remotion and React videos built from Mermaid |
| excalidraw-diagram | 15 | Excalidraw diagram JSON files that make visual arguments for workflows and concepts |
| explaining-with-ascii | 11 | Technical systems and tradeoffs explained with plain language and ASCII diagrams |
| debate-brainstorm | 10 | Two independent agents run through a structured debate with cross-critique and a synthesized answer |
| pick-ui-library | 5 | Pick the right frontend library from a curated list for charts, inputs, toasts and styling |
| no-ai-slop | 5 | Edit drafts into sharper, more human writing while preserving voice, or detect AI-slop patterns |
| explain-to-me | 5 | Explain unfamiliar concepts or code at the requested depth and language |

The remaining 19 indexed listings range from 1 to 4 installs.

## Why This Matters for Hermes Agents

The head of this catalog is a design quality argument: premium-frontend-design packages a decade of creative frontend experience into WebGL, shader and animation guidance so an agent ships interfaces that do not read as generic output, and no-ai-slop applies the same bar to prose. The explanation cluster is the second theme: explain-to-me, explaining-with-ascii, show-me and the Excalidraw skills give an agent multiple ways to turn a difficult concept into a diagram or a plain-language walkthrough instead of a wall of text. Planning-with-files and ralph add structure for long-running work, keeping progress in persistent markdown files or running clean-slate coding iterations behind PRD and CI gates. For business operators, the value is breadth at a low install footprint: most of these skills are small, single-purpose instructions that can be copied into a project one at a time. The counterweight is licensing and security: the repository has no LICENSE file, and the 20-skill security sample carries one Snyk Fail and six Warn cells, so review each skill before trusting it in a shared or production workflow.

## Usage

| You say | What happens |
|---|---|
| Design a landing page that feels alive | premium-frontend-design guides WebGL, shader and animation choices for a cinematic interface |
| Generate an SVG logo and icon set | svg-art runs Python scripts to produce icons, logos and generative vector art |
| Draw a diagram of this system | excalidraw or excalidraw-diagram emits Excalidraw JSON for the flow or architecture |
| Explain how this code works, simply | explain-to-me or explaining-with-ascii walks through it with plain language or an ASCII diagram |
| Plan a multi-step task with tracked progress | planning-with-files sets up persistent markdown files for planning and progress |
| Edit this draft to sound less robotic | no-ai-slop sharpens the writing while keeping the author's voice |
| Debate two approaches to this design | debate-brainstorm runs two independent agents and synthesizes a unified answer |

## Verification

Confirm a copied skill folder landed in the target directory:

```bash
ls ~/.claude/skills/explain-to-me
```

Review the premium frontend design skill's instructions before use:

```bash
curl -sL https://raw.githubusercontent.com/kv0906/cc-skills/main/skills/premium-frontend-design/SKILL.md | head -40
```

Check the svg-art skill's generator scripts:

```bash
curl -sL https://raw.githubusercontent.com/kv0906/cc-skills/main/skills/svg-art/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| premium-frontend-design | Pass | Pass | Pass |
| svg-art | Pass | Pass | Pass |
| excalidraw | Pass | Pass | Pass |
| ralph | Pass | Pass | Pass |
| planning-with-files | Pass | Pass | Pass |
| gws | Pass | Pass | Warn |
| animated-diagram | Pass | Warn | Pass |
| excalidraw-diagram | Pass | Pass | Warn |
| explaining-with-ascii | Pass | Pass | Pass |
| debate-brainstorm | Pass | Pass | Fail |
| pick-ui-library | Pass | Pass | Pass |
| no-ai-slop | Pass | Pass | Pass |
| explain-to-me | Pass | Pass | Pass |
| video-use | Pass | Pass | Pass |
| show-me | Pass | Pass | Pass |
| review-animations | Pass | Pass | Pass |
| proving-changes | Pass | Pass | Pass |
| prototype | Pass | Pass | Pass |
| improve-animations | Pass | Pass | Pass |
| huashu-design | Warn | Warn | Warn |

The sample is mostly clean at the head but not uniform: one Snyk Fail on debate-brainstorm, and Warns on gws, animated-diagram, excalidraw-diagram and all three auditors for huashu-design.

## Limitations

- Snapshot data, verified Nov 21, 2026: 2,271 combined installs across 32 indexed listings; 52 GitHub stars; no LICENSE file; last pushed Nov 7, 2026. Counts drift over time.
- The install index undercounts the catalog: the README lists 34 standalone skills while skills.sh indexes 32 listings, and video-use bundles a manim-video sub-skill that also appears as its own listing.
- No LICENSE file at the repository root; the README states licenses vary and some imported skills have no bundled license, so confirm permission before redistributing.
- The security sample carries 1 Snyk Fail (debate-brainstorm) and 6 Warn cells, including huashu-design flagged Warn on all three auditors.
- Amp-only workflows that need Amp's special tools, portals or cloud environment are excluded from this distribution; other agents may still need adjustments.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [Planning With Files - Agent Planning Methodology Setup](/hermes/skills/catalog/planning-with-files-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with one skill that fits the task instead of installing the whole 34-skill catalog; the folder copy path makes single-skill installs cheap.
- Pair premium-frontend-design with no-ai-slop so the interface and its copy both clear the same quality bar.
- Use the Excalidraw and ascii skills for explanation first: a diagram or ASCII walkthrough often lands faster than a long prose answer.
- Keep each skill's supporting files together when copying; references, templates and scripts are required for several skills to run.
- Check the security pages on skills.sh for debate-brainstorm and huashu-design before using them in shared or production workflows.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
