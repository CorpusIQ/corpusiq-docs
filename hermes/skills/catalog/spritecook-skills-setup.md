---
title: "SpriteCook Skills - Pixel Art and Game Assets"
description: "spritecook/skills on skills.sh: 7.4K combined installs across 10 listings; sprite, tileset, animation and UI kit generation through SpriteCook MCP."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/spritecook-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "spritecook", "game art", "pixel art"]
---

# SpriteCook Skills - Setup Guide

**Source:** [spritecook/skills](https://www.skills.sh/spritecook/skills) via skills.sh - 7.4K combined installs across 10 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 54 stars, MIT, last pushed 2026-10-20, ten SKILL.md directories, one per listing, all under `skills/`
**Category:** Game art for agents: sprite and tileset generation, animation, UI kits and Godot import through MCP tools
**Quality Tier:** 🟢 Production - MIT licensed, all five sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the suite ships one skill per stage of the asset pipeline.

SpriteCook is an AI game asset generator, and this repository is the instruction layer that teaches a coding agent to drive it: pixel art and detailed or HD art, autotile tilesets, animation, UI kits and a Godot export. The skills follow the open Agent Skills standard and the README lists Cursor, VS Code with Copilot, Claude Code, Claude Desktop, Antigravity, Codex, Grok Build and Windsurf among the editors they run in.

The structure is one skill per job rather than one manual. `spritecook-workflow-essentials` holds the shared rules every other skill assumes (credit checks, async polling, asset ID manifests, model defaults), and each generation, animation, polish, UI or import skill adds only its own decisions. That split matters here more than in most suites, because the work is paid: every step that re-runs a provider spends credits, and the skills are written to avoid that.

## Installation

The quick install is the Agent Skills CLI:

```bash
npx skills add spritecook/skills
```

The README's preferred path for SpriteCook itself also sets up the MCP connection, which is the part the skills cannot do for you:

```bash
npx spritecook-mcp setup
```

That command is the whole prerequisite. The skills tell an agent how to use SpriteCook; the MCP server provides the actual tools, and without it the agent has instructions and no way to act on them. Manual setup instructions live at spritecook.ai if you would rather wire the server yourself.

## What It Provides

Eight of the ten listings clear the 500-install threshold, and they cover the pipeline in the order a project needs it.

| Skill | Installs | Use For |
|---|---|---|
| spritecook-generate-sprites | 1,267 | Still images: pixel art or detailed and HD assets, model and crop choice, style consistency through `reference_asset_id` |
| spritecook-animate-assets | 1,136 | Animate uploaded or existing assets: grounded motion prompts, `edge_margin=6` framing default, `auto_enhance_prompt` for short prompts |
| spritecook-workflow-essentials | 1,112 | Shared rules: credit checks, async polling, canonical `sprite_url` outputs, `asset_id` manifests and the recommended model defaults |
| spritecook-generate-tilesets | 677 | Autotile tilesets through the MCP tools: tile sizes, reference, edit and style asset IDs, saving the generated tileset IDs |
| spritecook-use-dual-grid-tilesets | 659 | Dual-grid autotiling: mapping a 4x4 15-piece tileset image onto terrain with SpriteCook's mask system |
| spritecook-use-assets-in-godot | 656 | Godot 4.x export: SpriteFrames importer files, ready-to-test player scenes, AnimatedSprite2D for platformers and AnimatedSprite3D for top-down or isometric |
| spritecook-upload-assets | 627 | Import a user-selected image into the asset library through the MCP upload tools, for reference, editing, animation or reuse |
| spritecook-use-presets | 621 | Saved presets over MCP: reuse a preset's style and settings, or save a private preset so later assets match |

The remaining 2 indexed listings range from 204 to 442 installs: spritecook-build-ui-kits (442), which builds menus, HUDs, inventories and dialogs from a concept through component sheets and 9-slice metadata, and spritecook-polish-sprites (204), which cleans up broken outlines, halos and background debris after generation or background removal.

## Why This Matters for Hermes Agents

Game art is an unusually good fit for an agent and an unusually easy place to waste money. A sprite is small, the request is specific, and the correction loop is fast, which is exactly the shape of work an agent handles well. It is also metered: an agent that regenerates instead of editing, or re-runs a provider to change a transparency threshold, produces a bill rather than an asset.

The workflow skill is the answer to that. It puts the credit check before larger runs, requires the asynchronous polling contract to be followed, and insists the canonical `sprite_url` and `spritesheet_url` outputs are what the agent works from, with reusable `asset_id` values kept in a local manifest. Those rules exist because a model that loses an asset ID re-generates it, and the manifest is what makes a later edit cheap.

Model selection is documented rather than assumed, which is rarer than it should be. Nano Banana 2.1 (`gemini-nano-banana-2.1`) is the recommended default for new pixel-art sprites and characters, while Pixel Engine Image (`pixel-engine-image-v1`) is for single sprites at an exact size from 16 to 128 px with the background already removed, and it is text only, so it takes no reference or edit images. An agent that knows which one is which stops guessing at sizes.

The import half is where this suite earns its place in a real project. `spritecook-use-assets-in-godot` exports character animation runs into Godot 4.x, materialises the MCP `text_files` and `asset_downloads` manifests, writes SpriteFrames importer files and a ready-to-test player scene, and picks `AnimatedSprite2D` or `AnimatedSprite3D` by camera setup. That is the handoff where most AI art pipelines stop and a person starts doing it by hand.

`use-dual-grid-tilesets` is the same idea applied to the least obvious piece of 2D rendering: a 4x4 15-piece tileset mapped onto terrain through a dual-grid mask. It is a small skill that answers a question an agent would otherwise answer wrongly and confidently.

## Usage

| You say | What happens |
|---|---|
| "Make a 32x32 knight sprite with a sword" | generate-sprites picks the model and crop settings, keeps style consistent through reference asset IDs, and saves the returned asset ID |
| "Animate this character walking" | animate-assets uploads or takes the existing asset, writes a grounded motion prompt and uses `edge_margin=6` for safer framing |
| "Make me a tileset for a cave level" | generate-tilesets covers autotile generation, tile size choice and reference, edit and style asset IDs |
| "How do I render this tileset in my engine?" | use-dual-grid-tilesets maps the 4x4 15-piece sheet onto terrain with the dual-grid mask system |
| "Export the idle animation into my Godot project" | use-assets-in-godot writes the SpriteFrames importer, the player scene and the right AnimatedSprite node for the camera |
| "The sprite has a halo and broken edges" | polish-sprites inspects the alpha cutoff, compares thresholds locally, then saves the chosen cutoff without spending credits |
| "Build a HUD with health, ammo and a minimap" | build-ui-kits goes concept to component sheet to named controls and states, then finalises 9-slice metadata |
| "Use the same style as my last batch" | use-presets applies a saved preset, or saves a private one so the next run matches |

## Verification

Read the skills before installing; two of them are the ones an agent leans on first:

```bash
curl -fsSL https://raw.githubusercontent.com/spritecook/skills/main/skills/spritecook-generate-sprites/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/spritecook/skills/main/skills/spritecook-use-dual-grid-tilesets/SKILL.md | head -20
```

The first should open with `name: spritecook-generate-sprites` and the still-image description that pairs it with `spritecook-workflow-essentials`; the second with `name: spritecook-use-dual-grid-tilesets` and the 4x4 15-piece description. Both returned HTTP 200 on 2026-11-06.

Then confirm the tool half is connected, since the skills are inert without it:

```bash
npx spritecook-mcp setup
```

A completed setup run leaves the MCP server registered with your editor. `spritecook-workflow-essentials` also tells the agent to check plugin versions when a user asks about updates or compatibility, so a version mismatch usually surfaces as the agent asking rather than as a failed call.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| spritecook-generate-sprites | Pass | Pass | Pass |
| spritecook-workflow-essentials | Pass | Pass | Pass |
| spritecook-use-assets-in-godot | Pass | Pass | Pass |
| spritecook-use-presets | Pass | Pass | Pass |
| spritecook-polish-sprites | Pass | Pass | Pass |

Every sampled listing is clean, and the content justifies it: these are markdown instructions for calling a first-party MCP server, with no install scripts, no binaries and no credential handling in the skills themselves.

The exposure sits in the tools rather than the text. `spritecook-upload-assets` reads an image the user selected and pushes it into a hosted asset library, so an agent asked to "match this style" can send a file off the machine. That is the documented purpose of the skill, and it is still a data movement worth being deliberate about on a work machine.

Two more practical notes. SpriteCook is metered, so the credit check in `spritecook-workflow-essentials` is a spending control: skipped, an agent can run a large batch before anyone notices. And `spritecook-polish-sprites` deliberately saves the chosen alpha cutoff through MCP instead of re-running a provider, which is both cheaper and the reason its guidance never needs your image to leave local tooling for a threshold comparison.

The licence is MIT with a `LICENSE` file in the root, so the instructions are ordinary to reuse and redistribute.

## Limitations

- Snapshot data, verified 2026-11-06: 7,401 combined installs across 10 indexed listings; 54 GitHub stars; MIT; last pushed 2026-10-20. Counts drift over time.
- No tools without the SpriteCook MCP server. The skills are guides for a hosted generator, so an install with no MCP connection produces advice and no assets.
- The work is paid. Model runs consume credits, which is why the workflow skill front-loads a credit check and why polish work is designed to avoid a second provider call.
- Pixel Engine Image is text only and limited to single sprites at 16 to 128 px with the background already removed, so reference and edit images cannot be used with it. Requests that need either have to go through a different model.
- Model identifiers are provider-side facts (`gemini-nano-banana-2.1`, `pixel-engine-image-v1`) and will drift. The skills tell the agent to check plugin versions for compatibility rather than pinning a permanent default.
- Four listings are absent from the README's Available Skills section (generate-tilesets, use-dual-grid-tilesets, upload-assets, use-presets). Their descriptions here come from their own SKILL.md frontmatter, not from the README.

## Related

- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)
- [Game Creator - Playable Intelligence Game Skills](/hermes/skills/catalog/game-creator-setup)
- [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `spritecook-workflow-essentials` alongside whatever else you need. Every other skill in the suite assumes its credit checks, polling contract and manifest rules, and it is the shortest file that prevents duplicate spend.
- Ask for an edit, not a regeneration. `edit_asset_id` exists so a small change costs a small call, and a model that re-prompts from scratch pays full price for a new asset.
- Keep the manifest. Saving `asset_id` values locally is what lets a later session animate, slice or re-style an asset instead of regenerating it.
- Polish before you slice. Edge cleanup on the sheet is cheaper and better than cleanup on forty individual frames, and the skill says as much about animation frames and edge flicker.
- Name the target engine up front. The Godot skill picks `AnimatedSprite2D` or `AnimatedSprite3D` from the camera setup, so stating "top-down" or "platformer" at the start avoids an export you have to redo.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
