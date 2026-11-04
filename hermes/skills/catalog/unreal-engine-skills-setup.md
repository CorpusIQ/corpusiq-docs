---
title: "Unreal Engine Skills - Game Dev Suite for Agents"
description: "quodsoler/unreal-engine-skills on skills.sh: 35.6K combined installs across 31 listings; UE 5.8 checked Blueprints, C++ gameplay and rendering skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/unreal-engine-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "game development", "unreal engine", "cpp"]
---

# Unreal Engine Skills - Setup Guide

**Source:** [quodsoler/unreal-engine-skills](https://www.skills.sh/quodsoler/unreal-engine-skills) via skills.sh - 35.6K combined installs across 31 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 436 stars, MIT, last pushed 2026-09-28, 31 SKILL.md directories
**Category:** Unreal Engine for agents: Blueprints, C++ gameplay, materials, animation and packaging guidance
**Quality Tier:** 🟢 Green: MIT licence present, all five sampled skills pass every security scanner, and every API was checked against UE 5.8

This is a 31-skill pack for Unreal Engine 5.8 C++ work, built for agents rather than for humans reading docs. The author states that every API in every skill was checked against the 5.8 headers and source, and that every C++ example compiles against 5.8. Where an API changed, each skill carries a "Deprecated - do not use" table mapping the old form to the 5.8 form.

The pack is unusual in that it has an explicit hub skill. ue-project-context writes .agents/ue-project-context.md with your modules, target platforms and conventions, and every other skill reads it, so advice is tailored to the project instead of generic. The listings and the repo tree line up one to one: 31 indexed listings against 31 SKILL.md directories.

## Installation

No installer script is documented in the pack; these are markdown skills that you place in your agent's skills directory. Clone the repo next to your Unreal project:

```bash
git clone https://github.com/quodsoler/unreal-engine-skills
```

Then copy the directories you want into the skills folder your agent reads, for example:

```bash
mkdir -p .claude/skills
cp -r unreal-engine-skills/skills/ue-cpp-foundations .claude/skills/
cp -r unreal-engine-skills/skills/ue-project-context .claude/skills/
```

Add ue-project-context first. The README treats it as the foundation skill, and the rest reference the context file it writes:

```bash
cat unreal-engine-skills/skills/ue-project-context/SKILL.md
```

The skills are written to the Agent Skills spec, so the same directories work in any agent that reads SKILL.md files.

## What It Provides

Twenty of the 31 indexed listings clear 1,209 installs.

| Skill | Installs | Use For |
|---|---|---|
| ue-cpp-foundations | 1,487 | UCLASS, UPROPERTY, UFUNCTION, containers, delegates, GC and TObjectPtr |
| ue-ui-umg-slate | 1,457 | UMG and Slate widget work from the README UI/Input group |
| ue-editor-tools | 1,388 | Editor tooling and commandlets from the README Tools group |
| ue-project-context | 1,375 | Writing the shared project context file other skills read |
| ue-testing-debugging | 1,371 | Automation tests, logging and debugger work in the Tools group |
| ue-module-build-system | 1,352 | Module, target and build file setup in the Core C++ group |
| ue-materials-rendering | 1,349 | Materials and rendering work in the Render/VFX group |
| ue-niagara-effects | 1,313 | Niagara particle and VFX work |
| ue-gameplay-framework | 1,309 | GameMode, GameState and core gameplay classes |
| ue-actor-component-architecture | 1,301 | Actor and component lifecycle, spawning, attachment and ticking |
| ue-animation-system | 1,299 | AnimInstance, montages, notifies, blend spaces and root motion |
| ue-input-system | 1,286 | Input mapping and enhanced input in the README UI/Input group |
| ue-data-assets-tables | 1,276 | Data assets and data tables in the World group |
| ue-character-movement | 1,255 | CharacterMovementComponent modes, floor detection and network prediction |
| ue-procedural-generation | 1,251 | Procedural world generation in the README World group |
| ue-physics-collision | 1,247 | Collision channels, traces and physics bodies |
| ue-gameplay-abilities | 1,235 | Gameplay Ability System work in the Gameplay group |
| ue-networking-replication | 1,234 | Replication, RPCs and network authority |
| ue-ai-navigation | 1,220 | AI controllers, behavior trees, blackboards, EQS and NavMesh |
| ue-world-level-streaming | 1,209 | Level streaming and world partition in the World group |

The remaining 11 indexed listings range from 272 to 1,192 installs.

## Why This Matters for Hermes Agents

Game engine code is the hardest place to let a coding agent improvise. Unreal APIs churn between releases, signatures are verbose, and a plausible-looking call often fails to compile, so an agent that works from generic C++ knowledge burns a build cycle on every guess.

This pack solves that by shipping the engine knowledge as lookup documents: the correct class, the correct macro, and a table of the deprecated form it should not emit. That is the format a Hermes agent handles best, because it can be loaded on demand and cited.

The context-file pattern is the other transferable idea. One skill writes project facts once, and every later skill reads them, which removes the usual guessing about target platforms, module names and conventions. The same pattern works for any Hermes deployment with more than one specialist skill.

Coverage is deliberately uneven in a useful way: foundations, gameplay and animation skills carry the most installs, while narrower areas like cameras, tags and the Mover plugin sit at the bottom with a few hundred each.

Because the pack targets 5.8 specifically, it is a good example of pinning an agent knowledge base to one engine version and re-checking it at each upgrade.

## Usage

| You say | What happens |
|---|---|
| "Set up the project context for this UE project" | ue-project-context writes .agents/ue-project-context.md that later skills read |
| "Write a new actor component with replication" | actor-component-architecture and networking-replication supply the lifecycle and replication patterns |
| "Why does my UPROPERTY fail to register in the editor?" | ue-cpp-foundations checks the macro and reflection rules that govern registration |
| "Add a Niagara effect on hit" | ue-niagara-effects gives the spawn and parameter binding pattern |
| "Expose this C++ function to Blueprint" | ue-blueprint-cpp-interop covers UFUNCTION meta keys and latent actions |
| "Package this build for Windows" | the packaging guidance in the pack covers target and build configuration |
| "Check this animation montage setup" | ue-animation-system checks AnimInstance, notifies and blend space usage |

## Verification

Confirm the clone landed with all 31 directories:

```bash
ls unreal-engine-skills/skills | wc -l
```

Then fetch one raw skill file to confirm the tree matches what skills.sh indexed. This URL is built from the skills/ue-cpp-foundations/SKILL.md path in the repo tree, on branch main:

```bash
curl -fsSL https://raw.githubusercontent.com/quodsoler/unreal-engine-skills/main/skills/ue-cpp-foundations/SKILL.md | head -30
```

Frontmatter with a name and description plus a body that names UE 5.8 confirms the skill is the version this guide describes.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ue-cpp-foundations | Pass | Pass | Pass |
| ue-niagara-effects | Pass | Pass | Pass |
| ue-physics-collision | Pass | Pass | Pass |
| ue-state-trees | Pass | Pass | Pass |
| ue-mover | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified November 3, 2026: 35,564 combined installs across 31 indexed listings; 436 GitHub stars; MIT; last pushed 2026-09-28. Counts drift over time.
- The pack pins Unreal Engine 5.8. On 5.9 or later, read the deprecated tables first and expect some examples to need edits.
- No installer, CLI or marketplace command is documented. Setup is a clone plus a copy of directories.
- Skills are C++ first. Blueprint-only workflows get one interop skill, not full coverage.
- Install counts drop sharply after the first 27 listings, so the four lowest skills have thin usage evidence.
- The repo has been quiet since September 28, 2026, so new engine releases may outrun the content.

## Related

- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)
- [Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install ue-project-context before anything else; the other skills assume its output file exists.
- Keep .agents/ue-project-context.md in version control so a fresh agent session starts with the same project facts.
- Load two skills at most per task. Foundations plus the domain skill is usually enough, and more context dilutes the engine-specific detail.
- When a call fails to compile, check the skill's deprecated table before asking the agent to try a variation.
- Re-pull the repo at each engine upgrade instead of editing the skills in place, so the deprecated mappings stay authoritative.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
