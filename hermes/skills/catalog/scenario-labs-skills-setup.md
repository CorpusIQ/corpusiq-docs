---
title: "Scenario Labs Skills - Custom Model Training Setup"
description: "scenario-labs/skills: 53.3K combined installs. 174 skills for Scenario image, video, 3D and audio, plus Blender, Maya and game engine families."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/scenario-labs-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "game assets", "3d", "custom models", "image generation"]
---

# Scenario Labs Skills - Setup Guide

**Source:** [scenario-labs/skills](https://www.skills.sh/scenario-labs/skills) via skills.sh - 53.3K combined installs across 173 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [scenario-labs/skills](https://github.com/scenario-labs/skills) - 1,284 stars, MIT, branch main, last pushed 2026-10-31; 174 `SKILL.md` files in three trees, 7 internal ones under `.agents/skills/`, 35 DCC family skills under `skills/dcc/` (Blender, Maya, ZBrush) and 52 game engine skills under `skills/game-engines/` (Unreal, Unity, Godot, Roblox), with the rest as single-skill folders directly under `skills/`

**Category:** Generative asset production for games and creative work, with custom model training and DCC / engine expert families

**Quality Tier:** 🟡 Yellow - a clean MIT licence and Pass verdicts from Gen Agent Trust Hub and Socket on all five sampled skills, offset by a Snyk Warn on two of them and a Socket Warn on the skill-creator utility

Scenario is a generative platform for game and creative assets, and `scenario-labs/skills` is the vendor's own skill library for it: 174 `SKILL.md` files that teach an agent to drive Scenario through its MCP server. The suite covers the whole asset pipeline rather than one model. Images, video, audio, textures, skyboxes, 3D meshes and sprite animations each have a dedicated skill, and a set of production skills sits on top: consistency across shots, quality gates against a brand brief, asset analysis, and custom model training when references stop holding a look.

The bottom half of the library is different in kind. Seven expert families drive software installed on your machine instead of the Scenario API: Blender, Maya, ZBrush, Unreal Engine, Unity, Godot and Roblox Studio, 52 game engine skills and 35 DCC skills, distilled from conference talks, official documentation and expert tutorials. They need the application, not the MCP server, and each family installs as a set because the specialists import the lead skill's scripts. That split is why this is a suite to install selectively rather than wholesale.

## Installation

Every Scenario skill sits behind one installer, and the README documents a single-skill call, a menu and per-family sets. There is no npm package to add first:

```bash
# A single skill
npx skills add scenario-labs/skills --skill scenario

# Pick from the installer menu, grouped by topic
npx skills add scenario-labs/skills
```

The Scenario skills then need the MCP server connected, which is a separate step from the skill copy:

```bash
claude mcp add --transport http scenario https://mcp.scenario.com/mcp
```

Any other MCP client takes the same `https://mcp.scenario.com/mcp` endpoint and signs in with a Scenario account over OAuth, or with an API key from the Scenario settings page. The `scenario` skill carries the full setup and should be installed first, since the other Scenario skills route through it.

The expert families install as one command each. Blender, the largest, is fifteen skills:

```bash
npx skills add scenario-labs/skills --skill scenario-blender-expert scenario-blender-animation scenario-blender-blockout scenario-blender-export scenario-blender-geometry-nodes scenario-blender-grease-pencil scenario-blender-hair scenario-blender-hard-surface scenario-blender-lighting-rendering scenario-blender-previs-storyboard scenario-blender-retopology scenario-blender-rigging scenario-blender-sculpting scenario-blender-texturing-shading scenario-blender-uv-baking
```

To pin a reviewed state instead of tracking `main`, the README pins both the installer version and a release commit:

```bash
npx skills@1.7.4 add scenario-labs/skills#<commit> --skill <name>
```

The command line matches `--skill` against exact skill names only, so the menu's topic groups cannot be scripted; a role command from `INSTALL.md`, run with `-y`, is the CI-friendly route. The checkout was verified at 174 skill directories, and the role command that bundles model training with consistency and quality gating is one of the shorter ways in.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| scenario-blender-expert | 812 | Blender lead that routes any 3D task through Python or a live MCP bridge: modeling, sculpting, retopology, baking, rigging, lighting, engine handoff, plus the shared review and mesh-audit loop. |
| scenario | 754 | The connection skill: wires an agent to the Scenario MCP server, picks a model, runs a LoRA, refines a prompt, uploads references, waits on jobs and explains auth, quota or Forbidden errors. |
| scenario-game-assets | 658 | Sprites, sprite sheets, tilesets, autotile terrain, isometric buildings, pixel art, UI panels and parallax layers, with background removal and PNG export for Unity, Godot or Unreal. |
| scenario-consistency | 629 | Holds one look across generations: the same character in every scene, a turnaround, a product across angles, and the point where references stop scaling and a trained model is due. |
| scenario-sprite-animation | 602 | Walk, idle and attack cycles in 4 or 8 directions, isometric sheets, VFX loops, animated GIFs, and slicing a finished sheet into engine-ready frames. |
| scenario-3d | 598 | Text-to-3D and image-to-3D meshes as GLB, FBX, OBJ, STL or VOX, with auto-rigging, retargeting, remesh, UV unwrap and a viewer preview. |
| scenario-image | 587 | Text-to-image, instruction editing, inpaint and outpaint with a mask, aspect and resolution control, and model choice when a run fails on prompt length or a restricted model. |
| scenario-textures | 563 | Seamless tileable textures and PBR sets (albedo, metallic, roughness, normal) applied to meshes, plus upscaling that preserves tiling. |
| scenario-blender-rigging | 556 | Rigify metarigs, automatic weights and the fixes when weighting fails, IK/FK switching, foot roll, twist bones, drivers and face rigs. |
| scenario-blender-animation | 539 | Cycles, jumps, acting shots and lip sync in Blender, from stepped blocking to spline polish, with graph editor handles, slotted actions and NLA layers. |
| scenario-blender-texturing-shading | 530 | PBR materials from texture sets, procedural materials, wear and grime, triplanar mapping, stylized skin and eyes, and diagnosing a look that reads waxy or CG. |
| scenario-skyboxes | 527 | Skyboxes, 360 panoramas, equirectangular and cubemap layouts, HDRI-style backdrops and VR environments, including upscaling without breaking the seam wrap. |
| scenario-blender-sculpting | 527 | Head, bust and creature sculpting in Blender by script: primitives to planes and landmarks, stylized and realistic faces, remesh or multires planning. |
| scenario-refine-loop | 523 | The generate, review, revise loop: judging a batch against the brief, choosing between re-prompt, new reference, inpaint or another model, and wiring the loop into automation. |
| scenario-audio | 523 | Music, full songs from lyrics, score, SFX, foley, ambience, voiceover and voice cloning, with play and download for MP3 and WAV. |
| scenario-quality-gate | 515 | Pass, warn or fail scoring of a generated image against a brand brief, QA gating a batch, and pricing or refreshing a stored verdict. |
| scenario-image-editing | 515 | Tool-model edits to an existing image: upscale to 2x, 4K or 8K, LUT grade, grain and blur, uncrop and reframe, background removal, tile slicing. |
| scenario-video | 509 | Text-to-video, image-to-video, music videos, lipsync and talking avatars, dubbing, 4K upscale, trim, concat, extend and reframe. |
| scenario-moderation | 507 | What to do when a generation is blocked or refused: provider filters, likeness and IP flags, and why one model passes a prompt another rejects. |
| scenario-asset-analysis | 500 | Captions and alt text, reusable style descriptions, control maps for canny, depth, pose and segmentation, and finding an asset again by text or visual similarity. |

The remaining 153 indexed listings range from 1 to 494 installs.

## Why This Matters for Hermes Agents

Most skill libraries give an agent one thin capability. This one gives it a vocabulary for an entire production pipeline, and that is the useful part for a builder: the same agent can draft a concept image, hold a character consistent across twelve shots, generate the matching sprite sheet, then hand the asset to an engine family and check it before export. The connection between those steps is written down in the skills instead of living in someone's head.

The MCP layer is also where the routing value sits. Scenario exposes many models, and the skills encode which one to pick for a transparent sprite, a tileable texture, a mesh with a rig, or a clip that needs dubbing. An agent that has read `scenario` and `scenario-consistency` stops asking the user to choose a model by name and starts choosing by constraint, which is the difference between a useful generation turn and a demo.

The training path is the piece most profiles lack. `scenario-model-training` documents dataset curation, base model choice, epochs, sample prompts, cost estimation and the failure mode where a trained model loses its identity, and `scenario-consistency` tells the agent when to stop stacking references and train instead. For a brand, a game with a fixed art direction, or a character that recurs, that is a real capability rather than a prompt trick.

The expert families are a different bet. They encode procedures that were run live in specific versions: Blender 5.2 with twelve passing headless suites, Unity 6.3, Godot 4.7.2, Maya 2027, ZBrush 2026, Unreal 5.8. That makes them the most detailed part of the library and the most likely to drift, since an API change in the application breaks a procedure the skill states as fact.

## Usage

| You say | What happens |
|---|---|
| "Train a model on our 40 approved illustrations, then generate props in that style" | The agent curates the dataset, picks a base model, sets epochs and sample prompts, estimates cost, runs training through the Scenario MCP and checks the samples before using the result. |
| "Keep this heroine identical across twelve shots, poses and outfits included" | `scenario-consistency` decides between references and a trained model, pins the identity, and hands each shot to the image or video skill with the same control inputs. |
| "Give me a walk cycle in 8 directions for this sprite" | `scenario-sprite-animation` generates the directional sheet, checks the frames line up, and slices it into engine-ready files for Unity, Godot or Unreal. |
| "These walls look flat, make the texture tile properly" | `scenario-textures` regenerates a seamless set, verifies the tiling, and applies the PBR maps to the mesh instead of restyling the whole asset. |
| "Why was this render blocked when the last one worked?" | `scenario-moderation` reads the error, distinguishes a provider filter from a likeness or IP flag, and proposes a prompt or model change that keeps the intent. |
| "Score this batch against the brand brief before it ships" | `scenario-quality-gate` returns pass, warn or fail per image with the reason, and `scenario-refine-loop` decides whether to reprompt, inpaint or swap the model. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30, and it is the router every Blender specialist depends on:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/scenario-labs/skills/main/skills/dcc/blender/scenario-blender-expert/SKILL.md
```

Expect `200`. Read it before installing the family, because the first section names the execution channel and the sibling skills it hands work to; if a sibling is missing the router falls back to `skill_get` through Scenario MCP and tells the agent to flag the gap.

After the copy lands, confirm the skill directory and that the frontmatter survived the copy:

```bash
find . -path "*scenario-consistency/SKILL.md" -exec head -5 {} \;
```

A good copy shows `name: scenario-consistency` and a single long `description:` line naming the trigger situations, with `license: MIT` under it. The same three lines are what Hermes routes on, so a truncated description is the failure worth catching here. Where the installer put the folder depends on the client, so the search above is deliberately relative.

## Security

Verdicts sampled on skills.sh and verified 2026-10-30: two skills carry a Snyk Warn and one carries a Socket Warn, which is not a failure, because a Warn is a non-blocking finding the scanner raised on the skill folder, so those three need a read before production use rather than a rejection, and no sampled skill fails on any auditor. Re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| scenario-blender-expert | Pass | Pass | Warn |
| scenario | Pass | Pass | Warn |
| scenario-game-assets | Pass | Pass | Pass |
| scenario-consistency | Pass | Pass | Pass |
| skill-creator | Pass | Warn | Pass |

Two things follow from the table. The Warns cluster on the two largest skills, `scenario-blender-expert` and `scenario`, which are also the two that carry the most instructions and the widest tool surface, and they do not appear on the two content skills that were sampled alongside them. `skill-creator` is the odd one: it is an internal utility under `.agents/skills/` that writes new skills, not an asset skill, and it is the only sampled skill with a Socket Warn.

The wider surface is not the markdown at all. The expert families drive installed applications through Python, an MCP bridge or command ports, which means an agent that loads them can run scripts against Blender, Maya, ZBrush or an engine on your machine. Treat that as the real permission boundary: read the family README's provenance section, keep those skills out of profiles that touch client material, and install the Scenario MCP skills separately from the DCC families so the blast radius is a prompt and not a headless render queue. The repository also ships a `SECURITY.md` and runs CI plus an OpenSSF Scorecard.

## Limitations

- Snapshot data, verified 2026-10-30: 53,338 combined installs across 173 indexed listings; 1,284 GitHub stars; MIT; last pushed 2026-10-31. Counts drift over time.
- The last-push stamp reads 2026-10-31, one day after the 2026-10-30 snapshot date carried in this guide. It is copied verbatim from the pack rather than adjusted, so treat the pair as adjacent timestamps from a sweep that ran across a date boundary.
- The index does not map one to one onto the tree. skills.sh carries 173 listings and the checkout holds 174 skill directories, and the names diverge in `.agents/skills/`: the listings read `skills-pr-summary`, `skills-pr-handle` and `Skill Development` while the directories read `pr-summary`, `skills-pr-handle` and `skill-development`. Count the directories, not the listings, when auditing what is installed.
- The two halves have different prerequisites. The Scenario skills need a Scenario account and the MCP server connected; the expert families need the application installed at the version the family was validated against (Blender 5.2, Maya 2027, ZBrush 2026, Unreal 5.8, Unity 6.3, Godot 4.7, Roblox Studio), and the engine families were validated on macOS.
- A family is not divisible. The specialists import the lead skill's scripts, so installing `scenario-blender-sculpting` without `scenario-blender-expert` leaves the agent with instructions and no toolkit, and the router will report the gap rather than proceed.
- The counts are concentrated. One listing holds 812 of 53,338 installs and the tail runs down to 1, where the four `skills-*` utilities sit, so install counts describe the two big routing skills rather than the 174 files.

## Related

- [Motion Design Skills - After Effects and Remotion Setup](/hermes/skills/catalog/motion-design-skills-setup)
- [Remotion Framework Skills - Programmatic Video Suite Setup](/hermes/skills/catalog/remotion-framework-skills-setup)
- [Pexo Video Skills - AI Video Generation Suite Setup](/hermes/skills/catalog/pexo-video-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `scenario` first and alone, then add the one content skill you actually need. The other Scenario skills assume the connection skill is present, and a profile carrying eighty generative skills at once pays for all of them in context before it renders anything.
- Keep the DCC families out of the default profile. They are the largest files in the library and they only make sense on a machine that has Blender, Maya or ZBrush open, so load them where the application lives.
- Read the family README before trusting a procedure. Each one records how the family was built and how far it was verified, and the difference between "twelve test suites pass headless" and "the bridge was proven live, full tests pending" is the difference between a fact and a hypothesis.
- Prefer training over more references once consistency starts slipping. `scenario-model-training` documents the crossover, and a model trained on 40 approved images will hold a style that no stack of reference images holds past a dozen shots.
- Pin a release commit for anything you put in CI. The README's `npx skills@1.7.4 add scenario-labs/skills#<commit>` form is the only route that does not silently move with `main`, and this library changes often enough that an unpinned run is a different library each week.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
