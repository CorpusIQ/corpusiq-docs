---
title: "Text to CAD Skills - 3D Model and URDF Setup"
description: "earthtojake/text-to-cad: 124.1K combined installs. MIT skills for STEP, STL and 3MF models, DFM checks, and URDF, SRDF and SDF robot files."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/text-to-cad-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "cad", "3d printing", "robotics"]
---

# Text to CAD - Setup Guide

**Source:** [earthtojake/text-to-cad](https://www.skills.sh/earthtojake/text-to-cad) via skills.sh - 124.1K combined installs across 18 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) - 24,377 stars, MIT License, branch main, last pushed 2026-10-30; 12 `SKILL.md` files, one per directory under `skills/`, beside `packages/`, `apps/`, `models/`, `scripts/`, `plugin.json` (version 0.8.4), `mcp.json`, `skills.sh.json` and per-agent manifests in `.claude-plugin/`, `.codex-plugin/` and `.cursor-plugin/`

**Category:** Local CAD, fabrication and robot-description workflows for coding agents

**Quality Tier:** 🟡 Yellow - all five sampled skills Pass Gen Agent Trust Hub and Socket, but `step-parts` and `urdf` carry a Snyk Warn, on an MIT licence with 24,377 stars

text-to-cad is published by earthtojake, with the repository LICENSE naming Thompson Labs LLC, and it ships as a plugin plus a library of twelve agent skills backed by `cadgen` on PyPI. The pitch is concrete rather than aspirational: the agent writes each model as a Python script with build123d on Open CASCADE, running the script builds it through cadgen's warm engine into an `.xbf` document plus whatever STEP, GLB, STL or 3MF files the script declares, and the CAD viewer follows every rebuild.

What earns it a catalog page is the breadth past modelling. The same `skills/` tree covers 2D DXF cut layouts and PDF engineering drawings, design-for-manufacturing reviews for sheet metal, CNC and injection moulding, printability measurement per additive process, slicing through OrcaSlicer, print handoff to Bambu Lab machines, SendCutSend preflight, and the ROS side of the house in URDF structure, MoveIt SRDF planning semantics and Gazebo SDF worlds. skills.sh groups the twelve into CAD and Robotics, the plugin manifest declares skills plus an MCP server, and at 24,377 stars this is the most-starred 3D modelling entry the catalog indexes.

## Installation

The README leads with one command that finds every agent app on the machine and installs the plugin, or the skills alone for agents without one:

```bash
curl -fsSL https://texttocad.dev/install.sh | sh
```

On Windows it is a PowerShell one-liner, and the docs explain that `www.texttocad.dev` is named because the bare domain redirects with a 308 that PowerShell 5.1 will not follow:

```powershell
irm https://www.texttocad.dev/install.ps1 | iex
```

It asks nothing on the way, so read the plan before it changes anything. The docs show the read-it-first route, which also avoids piping an unreviewed script into a shell:

```bash
curl -fsSL https://texttocad.dev/install.sh -o install.sh
sh install.sh --dry-run
```

Hermes Agent is one of the sixteen agents the installer knows through the Skills CLI, under the id `hermes-agent`, and for it the skills land in `$HERMES_HOME/skills`, which for this profile is the profile's own `skills` directory. The install command treats it as an agent without a plugin, so it copies the skills and there is no CAD server: models open in the CAD Viewer in a browser instead of an in-conversation card. The equivalent manual call names the branch and the agent explicitly:

```bash
npx -y skills@latest add earthtojake/text-to-cad#latest -g -a hermes-agent -s '*' -y --copy
```

Pin `#latest`, not `main`. The docs state that `latest` carries the released plugin while `main` is where development happens and can hold unreleased changes. Twelve `SKILL.md` files exist in the current checkout, and `npx skills add` again is the documented update path because it re-fetches and overwrites, whereas `npx skills update` only touches skills already in the lockfile and silently misses newly added ones.

Two of the eighteen listings are retired upstream and worth skipping. `cad-viewer` is covered now by the CAD, DXF and robot-description skills, and `cad-mcp-setup` by the install command and the install page, so the docs tell you to clear old standalone copies with `npx skills remove cad-viewer cad-mcp-setup`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cad | 14,539 | Creating and editing parametric parts and assemblies as Python build123d models that cadgen builds into live XBF documents, then exporting STEP, STL, 3MF or GLB on request and reviewing existing CAD files in the viewer. |
| step-parts | 11,415 | Finding a real purchasable part before falling back to placeholder geometry: fuzzy search of the hosted step.parts catalog for screws, bearings, motors and connectors, then a canonical `.step` fetch with checksum verification. |
| sdf | 10,966 | Authoring and validating SDFormat models and worlds for Gazebo: links, joints, poses, frames, inertials, visual and collision geometry, mesh URIs, sensors, lights, physics and plugins. |
| urdf | 10,921 | Writing and debugging robot structure files: links, joints, limits, inertials, mesh references and frame conventions, treated as constrained kinematic modelling rather than XML typing. |
| srdf | 10,820 | Adding MoveIt2 planning semantics on top of a valid URDF: planning groups, end effectors, group states, virtual and passive joints, and a safe disabled-collision matrix derived from URDF topology. |
| sendcutsend | 10,632 | Preflighting DXF and STEP uploads for SendCutSend orders against that vendor's ordering guide, catalog and specs: upload readiness, material and thickness availability, and per-service checks. |
| gcode | 9,924 | Slicing a model into printer-ready G-code with OrcaSlicer, headless through its CLI or by opening the file in the app, using your own printer profiles and never contacting a printer. |
| bambu-labs | 9,628 | Handing a sliced job to a Bambu Lab printer by opening it in Bambu Connect or Bambu Studio, where you pick the machine and start the print. |
| dxf | 9,612 | Generating and validating 2D DXF drawings from build123d models: profiles, outlines, templates, gaskets, panels, flat patterns and laser, plasma or waterjet cut layouts. |
| cad-viewer | 8,994 | Opening existing or freshly generated CAD, DXF and robot-description files in CAD Viewer and handing back live review links. Retired upstream in favour of the CAD, DXF and robot-description skills. |
| implicit-cad | 5,523 | Building experimental implicit CAD models as `.implicit.js` or `.implicit.mjs` browser ES modules that run directly in CAD Viewer, for cases where STEP-first modelling is not wanted. |
| dfam-check | 4,541 | Measuring a mesh against design-for-additive-manufacturing rules per process: wall thickness, overhangs, support volume and build orientation, as facts rather than pass or fail verdicts. |
| engineering-drawing | 2,617 | Producing a dimensioned engineering drawing as one PDF: orthographic views, hidden lines, centre marks, hole callouts, notes and an ISO title block, all projected from the part geometry. |
| dfm | 2,450 | Reviewing a part for sheet metal, CNC machining or injection moulding, with measured evidence such as mould draft, undercuts and projected area, and the cited rule behind each finding. |
| render | 1,347 | Rendering generated or modified CAD and robot-description files in CAD Explorer and returning a viewer URL per file, including snapshots or parameter-animation GIFs for review. |
| cad-mcp-setup | 148 | Wiring CAD's MCP server into an agent by hand. Superseded by the install command and the install documentation, so treat it as historical. |
| cad-explorer | 13 | Opening CAD and robot-description files in a local CAD Explorer instance started with `dev:ensure` and returning the printed URL, the early single-purpose ancestor of the render skill. |
| robot-motion | 6 | Generating local motion behaviour from an existing URDF: IK, path planning, MoveIt configuration, websocket motion-server debugging and ROS dependency setup. |

No indexed listings fall below the threshold.

The index has outrun the tree. Six listings have no directory in the current checkout: `cad-viewer` and `cad-mcp-setup` are retired by their own documentation, and `implicit-cad`, `render`, `cad-explorer` and `robot-motion` still have skills.sh pages with readable `SKILL.md` content but no folder under `skills/` on `main`. The `robot-motion` page refers to an internal `.agents/skills/` tree that this checkout does not carry, so if a workflow of yours depends on it, read the page before assuming the file ships.

## Why This Matters for Hermes Agents

Most agent output is text or code, and a Hermes profile is already good at both. Physical geometry is the gap: an agent that can write a Python script but cannot rebuild it, measure it, check it for manufacturability or export the format a shop accepts leaves the last mile to a human. These skills close that loop locally, with a warm engine so an edit rebuilds only what changed instead of re-running a cold kernel.

The structure is what keeps it honest. Each script declares its own exports, so a STEP or 3MF file exists because a model asked for it rather than because a tool guessed, and the DFM and DfAM skills are written to report measurements and cite the rule behind each finding instead of issuing a readiness verdict. For an agent that tends to hand over confident summaries, that is the more useful contract: numbers you can check, and a clear statement when a check was unavailable.

The robotics half is the part with the fewest good alternatives on skills.sh. URDF, SRDF and SDF are three different documents with three different failure modes, frame placement and joint-axis semantics in one, planning-group topology and collision matrices in another, and simulator metadata in the third, and this suite separates them, tells the agent to derive SRDF from the URDF's own link and joint table rather than from memory, and keeps the CAD viewer available for a visual sanity check.

It is also a cheap thing to try. The markdown is MIT licensed, the engine runs as your own user on loopback, and a profile can install three skills, ask for one bracket, and decide from the result whether to keep the rest.

## Usage

| You say | What happens |
|---|---|
| "Make me a 60 mm mounting bracket with four M4 clearance holes" | The cad skill writes a build123d script, runs it against cadgen's engine, shows the part in the viewer and exports STEP or STL when you ask for a file. |
| "Find a real 608 bearing and put it in this assembly" | step-parts searches the hosted catalog, retries aliases and family facets, fetches the canonical `.step`, verifies the checksum and positions it in the model. |
| "Will this bracket print without supports, and can it be bent from 2 mm steel?" | dfam-check measures wall thickness, overhangs, support volume and orientation per process on the mesh, and dfm runs the sheet metal review with bends, reliefs and flat patterns cited against the rule. |
| "Draw this part up so a shop can quote it" | engineering-drawing generates one PDF with ISO views, hidden lines, real dimensions, hole callouts and a title block, projected from the geometry so a model change moves the sheet with it. |
| "Export a DXF for laser cutting and check it against SendCutSend" | dxf builds the 2D outline from the model, and sendcutsend reviews it against the live vendor guide and catalog, naming the material and thickness combinations that work. |
| "Slice it for my printer and send it to the Bambu" | gcode slices headless with OrcaSlicer into `.gcode.3mf` or `.gcode` using your presets, then bambu-labs opens the job in Bambu Connect or Bambu Studio for you to start. |
| "Here is a robot arm URDF, get it planning in MoveIt" | urdf checks structure, frames and inertials, srdf derives planning groups, end effectors and disabled collisions from the link and joint table, and sdf covers the Gazebo world if you need one. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} cad\n" \
  https://raw.githubusercontent.com/earthtojake/text-to-cad/main/skills/cad/SKILL.md
```

Expect `200`. Then confirm what actually landed in the profile, since the install writes into `$HERMES_HOME/skills` rather than a fixed global path:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E '^(cad|dxf|urdf|srdf|sdf|step-parts|gcode|dfm)$'
head -4 ~/.hermes/profiles/corpusiq/skills/cad/SKILL.md
cadgen doctor
```

Each installed skill directory is one self-contained `SKILL.md` with a `references/` folder beside it, and a good copy shows `name: cad` with a description that mentions build123d, cadgen and the exports. `cadgen doctor` is the repository's own diagnosis tool: the README asks for its output in a bug report, which makes it the fastest way to confirm the engine is reachable before blaming the markdown.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30): two of the five carry a Snyk Warn, in `step-parts` and `urdf`, and none carry a Fail, so re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cad | Pass | Pass | Pass |
| step-parts | Pass | Pass | Warn |
| sdf | Pass | Pass | Pass |
| urdf | Pass | Pass | Warn |
| robot-motion | Pass | Pass | Pass |

A Snyk Warn is not a Fail, but it is not a clearance either: it means the scanner surfaced something it could not resolve, and only three skills were audited by Snyk at all, so the table describes five files out of eighteen. Read the two Snyk pages before these run unattended. Both warned skills are ordinary markdown that shells out to local tools, `step-parts` to a hosted HTTP catalog and `urdf` to cadgen, so the interesting surface is the runtime they drive rather than the instructions themselves.

That runtime is worth understanding before you point the CAD viewer at client work. One warm `cadgen` engine per installation serves the viewer and the MCP endpoint over HTTP on `127.0.0.1`, port 3245 unless another program holds it, and SECURITY.md is explicit that the credentials are the boundary: whoever holds the token, a link inside its 24 hour life, or the session cookie can read any CAD file on the machine by path, list folders and export. Links are therefore private by definition, and `--host` should stay on loopback.

Two more behaviours matter operationally. text-to-cad sends usage statistics and crash reports by default, tagged with a random ID and, per the README, never including your files, paths or prompts, and the installer's `--no-telemetry` flag turns it off. Files written by someone else, STEP, GLB, STL, 3MF, DXF, URDF, SDF or SRDF, are treated as untrusted input and read in separate processes with bounded work, which is the right default when a downloaded part lands in a model.

## Limitations

- Snapshot data, verified 2026-10-30: 124,096 combined installs across 18 indexed listings; 24,377 GitHub stars; MIT License; last pushed 2026-10-30. Counts drift over time.
- The index outruns the tree. Eighteen listings are indexed, but the checkout holds twelve skill directories, and six entries, `cad-viewer`, `cad-mcp-setup`, `implicit-cad`, `render`, `cad-explorer` and `robot-motion`, have no folder under `skills/` on `main` today.
- The counts are not a ranking. `cad` alone holds 14,539 of the 124,096 installs and the smallest entry sits at 6, so a low number can mean a retired skill, a niche one, or a file the index still lists after upstream moved on.
- The engine is a hard dependency. Install needs `uv`, the runtime wants Python 3.11 or newer, and the first run downloads a pinned `cadgen` release plus a managed Python 3.13, so an air-gapped or offline profile gets markdown that cannot build anything.
- The fabrication skills need local software and live vendor data. `gcode` wants OrcaSlicer installed, `bambu-labs` wants Bambu Connect signed in to a Bambu Lab account, and `sendcutsend` fetches its guide and catalog every review, so its verdicts are only as current as that vendor's pages.
- The checks measure, they do not certify. `dfm` and `dfam-check` report findings with cited rules and explicitly refuse to issue readiness statuses, so a clean report is evidence for a decision, not a manufacturing sign-off.

## Related

- [K2F - Document Generation Skills Setup](/hermes/skills/catalog/k2f-setup)
- [Kami - PDF, PNG and Editable PPTX Layout Skill Setup](/hermes/skills/catalog/kami-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Add `--dry-run` to the install command the first time. It prints the per-app plan, add, update, remove a duplicate or leave alone, and changes nothing, which is the cheapest way to see how many copies already exist.
- Keep one copy per app, not two. The docs are blunt that the plugin and the standalone skills should not both be installed in the same agent, because every skill then appears twice in the catalog the model reads.
- Pin `#latest` rather than `main` in any scripted install. `latest` carries released versions, `main` can carry unreleased changes, and the difference only shows up as a model script that fails on a pin it did not expect.
- Ask for the check before the export. Running `dfm` or `dfam-check` on the geometry and iterating there is faster than exporting, uploading to a fabricator and learning about an undercut from a quote.
- For robot work, treat the URDF as the source of truth and generate SRDF from its extracted link and joint table. The SRDF skill says plainly that plausible-looking XML with the wrong planning group or the wrong tool link is the common failure, and that no link or joint name should ever be typed from memory.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
