---
title: "CC Blender Skill - 3D Production for Agents"
description: "roble3/cc-blender-skill: 36.7K combined installs across 30 listings; chain-loaded Blender skills for modeling, UV, lighting, rendering and export."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cc-blender-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "blender", "3d"]
---

# CC Blender Skill - Setup Guide

**Source:** [roble3/cc-blender-skill](https://www.skills.sh/roble3/cc-blender-skill) via skills.sh - 36.7K combined installs across 30 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 141 stars, MIT, last pushed 2026-10-12, 32 SKILL.md directories
**Category:** Blender for agents: modeling, UV, materials, lighting, cameras, animation and export handled like a senior 3D artist
**Quality Tier:** 🟢 Production - all five sampled listings are Pass on all three auditors, the licence is MIT, and what ships is Markdown plus a Blender Python bridge

The pack turns a request like "model a sword and render a hero shot with three-point lighting" into Blender Python that runs through an MCP server. `text-to-blender` is the orchestrator: it detects the intent, then chain-loads the sub-skills for modeling, materials, lighting, cameras, rendering, animation, export, wireframe-to-3d, pro-workflow and the reference fitting and validation family, and the generated Python is sent through `mcp__blender__execute_blender_code` to Blender and back as output.

Version 1.4.0 splits the backend question in two. The official Blender Lab MCP is preferred for shared capabilities, while existing ahujasid Blender MCP installations keep working, and tasks that need asset-download or generation tools start on ahujasid. The chosen backend stays fixed for the whole task, which matters because the two servers expose different tools for the same subject.

## Installation

skills.sh lists this source at https://www.skills.sh/roble3/cc-blender-skill, so the CLI route starts there:

```bash
npx skills add roble3/cc-blender-skill
```

The installable artifact in the repository is the plugin directory, not the repository root, so a manual install copies from `plugin/skills/` and leaves the `docs/` and `knowledge/` trees behind:

```bash
git clone --depth 1 https://github.com/roble3/cc-blender-skill.git /tmp/cc-blender-skill
mkdir -p ~/.hermes/profiles/corpusiq/skills
for skill in /tmp/cc-blender-skill/plugin/skills/*; do
  [ -f "$skill/SKILL.md" ] || continue
  destination="$HOME/.hermes/profiles/corpusiq/skills/$(basename "$skill")"
  [ -e "$destination" ] || cp -R "$skill" "$destination"
done
```

The README's Quick Install section is behind an anchor this pack's excerpt does not include, so the two routes above are the skills.sh one-liner and the copy loop that the tree guarantees, not quoted README instructions.

The second half of setup is the MCP backend, and the README is specific about it. The official MCP needs Blender 5.1 or newer, its add-on installed and a separate MCP process running; an existing ahujasid setup needs no change. Confirm the server answers before trusting a modeling run, because the skill content is agent-agnostic and the configuration is host-specific.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| blender-modeling | 2,782 | Mesh work in Blender, the first half of the README's sword example: primitives, joins, bevels and cleanup. |
| blender-materials | 2,043 | Shading and material setup, including the node graph behind a surface. |
| blender-export | 1,707 | Export routes, including the Unreal collision preflight and the Multires cage baking that version 1.4.0 adds. |
| blender-rendering | 1,670 | Render settings and the render check; 1.4.0 says validation reads the returned file path instead of an assumed destination. |
| blender-animation | 1,638 | Keyframes, timing and curves for a moving object. |
| blender-pro-workflow | 1,592 | A production working order for a multi-step job; the README lists it in the chain-loaded set beside export and wireframe-to-3d. |
| blender-lighting | 1,570 | Scene and three-point lighting, the second half of the README's example request. |
| reference-to-3d | 1,539 | Building a model from reference images, the front door to the fitting and calibration skills. |
| blender-uv-texturing | 1,393 | UV unwrapping and texture work, with atlas fitting and closed-surface coverage skills sitting under it. |
| blender-cameras | 1,391 | Camera placement, framing and lens choice for a hero shot. |
| text-to-blender | 1,374 | The orchestrator: reading a plain-language request and chain-loading modeling, materials, lighting, cameras, rendering, animation, export and the reference skills. |
| animation-quality-gate | 1,052 | A pass or fail check on animation before delivery; the repository description says the stack is validated on six scene classes. |
| blender-skill-harmonizer | 1,021 | Keeping chain-loaded skills consistent with each other when several load in one task. |
| reference-analysis-validator | 1,011 | Checking that a reference analysis is complete enough to model from before geometry starts. |
| reference-look-calibration | 996 | Calibrating materials and lighting against the reference so the render matches the source. |
| wireframe-to-3d | 976 | Turning a wireframe drawing into geometry; also shipped as `docs/WIREFRAME` and a standalone `skill/wireframe-to-3d` folder. |
| contour-to-mesh | 973 | Building a mesh from the contour lines in a reference. |
| orthographic-registration | 971 | Lining up orthographic views so front, side and top agree with each other. |
| multiview-fit-loop | 967 | Iterating a model against several reference views until they match. |
| quality-refinement-autoloop | 960 | A refinement loop that keeps polishing until the quality gate passes. |

The remaining 10 indexed listings range from 884 to 942 installs.

Everything in the table has a directory in the tree, which is unusual for this catalog: 20 rows against 32 `SKILL.md` directories, and each of the 20 appears at `plugin/skills/<name>/SKILL.md`.

## Why This Matters for Hermes Agents

3D work is where an agent's failure is the most expensive, because a wrong mesh is not a wrong sentence you edit, it is a rebuild. This pack addresses that with a chain rather than a single prompt: modeling loads materials and lighting, the reference skills load the fitting and calibration passes, and the quality gates decide whether the result leaves the run at all.

The reference-fitting family is the interesting half, with `reference-to-3d`, `orthographic-registration`, `multiview-fit-loop`, `contour-to-mesh` and `fit-repair-optimizer` describing a loop where a source drawing is measured, a mesh is fitted to it and the fit is repaired until it holds. That is a different posture from one-shot generation, and it is the posture an agent needs when the deliverable has to match something that already exists.

Keeping the backend fixed for the task, as version 1.4.0 requires, also prevents a run from silently changing subject when one of two MCP servers exposes an unequal tool set, and routing generated Python through the single `mcp__blender__execute_blender_code` call keeps the boundary between what the model wrote and what Blender executed visible and reviewable. For an unattended run, that boundary is the audit trail.

Version 1.4.0 adds checkable preflights rather than new claims: collider names, evaluated geometry, closedness, winding, convexity and same-file selection are verified before the static FBX route. The README also says plainly that not every Blender version or Unreal import has been validated, which is worth remembering when a gate reports success.

## Usage

| You say | What happens |
|---|---|
| "Model a sword and render a hero shot with three-point lighting" | text-to-blender loads modeling for the mesh, materials for the surface, lighting for the three-point setup and cameras for the shot, then rendering writes the file. |
| "Turn this wireframe into a 3D model" | wireframe-to-3d with orthographic-registration reads the drawing, contour-to-mesh builds geometry and multiview-fit-loop iterates until the views line up. |
| "Match this reference photo of a can" | reference-to-3d runs reference-analysis-validator first, then reference-look-calibration tunes materials and lighting against the source. |
| "Set up UVs for this character" | blender-uv-texturing unwraps the model, with atlas-uv-fitting and closed-surface-uv-coverage for the harder cases. |
| "Animate this turntable and export it" | blender-animation keys the motion, animation-quality-gate checks it and blender-export writes the file. |
| "Export this for Unreal with collision" | blender-export runs the collision preflight on names, geometry, closedness, winding and convexity before the static FBX route. |
| "Make a procedural motion graphic for a HUD" | orbital-hud-motion with texture-state-animation builds the motion, and the render path produces the clip. |

## Verification

The raw path below was built from the repository layout on branch main. Probe it before installing, and expect an HTTP 200:

```bash
curl -sL -o /dev/null -w "%{http_code} blender-modeling\n" \
  "https://raw.githubusercontent.com/roble3/cc-blender-skill/main/plugin/skills/blender-modeling/SKILL.md"
```

After the clone, count the skills in the plugin rather than in the docs, and read one frontmatter block, which is what the orchestrator routes on:

```bash
git clone --depth 1 https://github.com/roble3/cc-blender-skill.git /tmp/cc-blender-skill
find /tmp/cc-blender-skill/plugin/skills -name SKILL.md | wc -l
head -4 /tmp/cc-blender-skill/plugin/skills/text-to-blender/SKILL.md
```

The count should be 30, which is the same 30 the index lists. Anything lower means the copy is incomplete. Then confirm the MCP side independently: ask the agent to list its `mcp__blender__` tools, and if none appear, fix the server configuration before any modeling run.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| blender-modeling | Pass | Pass | Pass |
| reference-to-3d | Pass | Pass | Pass |
| wireframe-to-3d | Pass | Pass | Pass |
| mascot-logo-reconstruction | Pass | Pass | Pass |
| orbital-hud-motion | Pass | Pass | Pass |

All five sampled listings are Pass on all three auditors, and the sample covers modeling, reference fitting, wireframe reconstruction, logo reconstruction and HUD motion rather than only the orchestrator. The sample does not include every skill in the tree, so re-check the ones you plan to run.

The real trust boundary is elsewhere. The skills contain instructions, and the code that executes is Python the model writes, sent to a local Blender process through MCP with full access to that Blender session. Blender Python can read files and run commands, so treat a modeling run as code execution on your machine, sandbox the Blender process if the inputs are untrusted, and keep generated scripts reviewable rather than fire-and-forget.

## Limitations

- Snapshot data, verified November 3, 2026: 36,728 combined installs across 30 indexed listings; 141 GitHub stars; MIT; last pushed 2026-10-12. Counts drift over time.
- The README describes thirty chain-loadable skills and skills.sh indexes 30 listings, which matches the 30 folders in `plugin/skills`; the tree's 32 `SKILL.md` directories also include `docs/WIREFRAME` and a second copy of `wireframe-to-3d` at `skill/wireframe-to-3d`, so a raw file count is not a skill count.
- Blender 5.x is the target. The official Blender Lab MCP needs Blender 5.1 or newer plus its add-on and a separate MCP process, and the README keeps its legacy Blender 4.x caveats rather than retracting them.
- The README says outright that v1.4.0 is additive and not a claim that every Blender version or Unreal import has been validated, so a green gate is evidence about the tested path only.
- Export targets are Unreal and the standard FBX and glTF routes; nothing in the pack promises other engine importers.
- The skills are agent-agnostic but the installation and MCP configuration are host-specific, and nothing in the repository mentions Hermes, so the profile layout is yours to get right.

## Related

- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)
- [Hyperframes Setup](/hermes/skills/catalog/hyperframes-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start every job at `text-to-blender` and let it chain-load. Naming a sub-skill directly skips the orchestrator's ordering and loses the validation steps that come with it.
- Feed references as images, not adjectives. The fitting family works by measuring a drawing, and "a bit more like the photo" gives it nothing to register against.
- Fix the MCP backend at the start of the task. Switching between the official Lab server and ahujasid mid-run changes which tools exist, and 1.4.0 explicitly keeps the choice fixed.
- Read the generated Python before it runs when the scene is not disposable. The skills are instructions, and the code is the model's, with full access to the Blender process.
- Trust the collision preflight over a successful export. Names, closedness, winding and convexity are what break an Unreal import, and version 1.4.0 checks them before the FBX route rather than after.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
