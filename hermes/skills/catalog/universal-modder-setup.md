---
title: "Universal Modder - AI Game Modding Skills Setup"
description: "rehan-remade/universal-modder on skills.sh: 20.8K combined installs across 13 listings; skills that take an agent from game recon to a published mod."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/universal-modder-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "game modding", "reverse engineering"]
---

# Universal Modder - Setup Guide

**Source:** [rehan-remade/universal-modder](https://www.skills.sh/rehan-remade/universal-modder) via skills.sh - 20.8K combined installs across 13 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 9,510 stars, MIT, last pushed 2026-11-06, 39 SKILL.md files in the tree: 13 skills in `skills/`, mirrored into `.agents/skills` and `.claude/skills`, alongside `agents/` role briefs, a `knowledge/` field-note base and the `um` Python CLI
**Category:** Game modding and reverse engineering: engine recon, decompilation, asset generation, in-game testing and mod publishing
**Quality Tier:** 🟡 Yellow - MIT with a LICENSE file, but two of the three sampled skills carry a Snyk Warn, and the toolchain decompiles binaries, reads live memory and drives a running game.

Universal Modder is the most ambitious skill set in this wave, and the least like a prompt library. It targets a specific claim: point an AI coding agent at a PC game you own, and it will work out the engine, read the real code, build a mod, generate the art and sound, test it in the running game, cut a showcase clip and write down what it learned for the next agent.

The 13 skills follow that sequence almost exactly. `game-recon` establishes what you are dealing with and writes a `MODDING_PLAN.md`. `game-research-websearch` digs through dead forums and archive snapshots for prior art. `reverse-engineering` reads the binary formats and live memory. `mod-any-game` carries the engine playbooks and the safety rules. `fal-assets` and `asset-pipeline` produce art in the exact frame sizes the engine loads. `game-automation` launches and drives the game so the agent can verify its own work. `publish-mod` and `share-field-notes` close the loop.

With 9,510 GitHub stars this is the most-watched repository in this batch, and the README has the tone of a project that has actually shipped mods rather than one that speculates about them: it links specific field notes for Portal 2 with Minecraft inside it, Halo 3 weapons in Minecraft, Bloons TD 6 and a Counter-Strike style conversion of Elden Ring.

## Installation

Every agent gets the same skills, the fal MCP server and the `um` CLI. For Claude Code, the plugin route is two commands:

```text
/plugin marketplace add rehan-remade/universal-modder
/plugin install universal-modder@universal-modder
```

Codex, Gemini CLI and Copilot each have their own entry point:

```bash
codex plugin marketplace add rehan-remade/universal-modder
codex plugin add universal-modder@universal-modder
```

```bash
gemini extensions install https://github.com/rehan-remade/universal-modder
```

For any agent that reads Agent Skills format, the skills-only install is the shortest path:

```bash
npx skills add https://github.com/rehan-remade/universal-modder
```

For anything else, clone and start the agent inside the repository:

```bash
git clone https://github.com/rehan-remade/universal-modder
```

The `um` CLI is separate from the plugin on some harnesses. The Claude Code plugin puts it on PATH through a SessionStart hook, and a clone opened in Claude Code does the same; for other agents install it once:

```bash
uv tool install git+https://github.com/rehan-remade/universal-modder
```

Inside a clone, each agent finds the skills where it looks for them: `.agents/skills` for Codex, Gemini CLI, Copilot, Cursor and OpenCode, and `.claude/skills` for Claude Code. Both are copies of `skills/`, and instructions live in `AGENTS.md`, which `CLAUDE.md` and `GEMINI.md` point to. For a Hermes agent, copying or linking `skills/<name>` into the agent skills directory is a complete install, and keeping `.mcp.json` gives you the fal server alongside it.

Asset generation needs a fal API key. The README's preferred storage is the CLI, not a shell profile:

```bash
um fal key set
```

On Linux that goes into the desktop keyring through libsecret, elsewhere into an owner-only `~/.secrets/fal-key`. `um fal key status` reports which source is in use, and `FAL_KEY` in the environment still wins when set.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| reverse-engineering | 1,955 | Reading how a game works: ILSpy and Cpp2IL for .NET and IL2CPP, Vineflower for Java, Ghidra and IDA over MCP, live memory through Cheat Engine and Frida, RenderDoc for render passes |
| mod-any-game | 1,937 | The whole loop plus engine playbooks: new items, weapons, enemies, units, mechanics, art, sound, VR and cross-game mashups |
| game-recon | 1,907 | Engine, version, managed versus native code, anti-cheat, installed loaders, save folders and the community route, written to MODDING_PLAN.md |
| game-automation | 1,840 | Launching a real game, taking GPU-safe screenshots, clicking and typing through menus, and an in-game bridge so the agent can observe and act |
| mashup-mods | 1,816 | Cross-game mashups and total conversions, from content ports to passthrough mods that run two games at once and exchange state |
| asset-pipeline | 1,807 | Turning generated art into engine-exact frames: cutout, trim, pixelation, sprite sheets, team-colour masks and 3D to isometric sprites |
| share-field-notes | 1,770 | Searching and contributing the shared knowledge base of how specific games were modded, then opening the pull request |
| publish-mod | 1,755 | Packaging and releasing a mod: pre-release lint, README, credits, AI disclosure, versioning and where to upload |
| fal-assets | 1,739 | Generating sprites, textures, PBR maps, 3D models, rigs, sound effects, music, voice lines and trailer video through fal |
| showcase-video | 1,728 | Recording the game window with only its own audio, picking moments from contact sheets and cutting a titled video from an EDL |
| game-research-websearch | 1,324 | Archive-aware research through Wayback and archive.today, GitHub code search, Nexus and Workshop APIs, Reddit and YouTube transcripts |
| port-a-mod | 914 | Porting an existing mod to a newer game version or loader while keeping behaviour, with a pinned source and unit-by-unit tests |
| blitz3d-decomp | 268 | Decompiling a Blitz3D game to readable source with B3DDecomp, including animated .b3d models for engines such as Roblox |

No indexed listings fall below the threshold; all 13 appear above.

The spread is unusually flat for a 13-skill set, with 12 of the 13 between 914 and 1,955 installs. That shape suggests people install the whole workflow rather than a single favourite, which is consistent with the README's framing: recon, reverse engineering, assets, testing and publishing are steps in one loop, not alternatives.

## Why This Matters for Hermes Agents

The interesting part is not that an agent can write a mod. It is that the set closes the verification loop. `game-automation` launches the game, drives the menus, captures the window and reads an in-game JSON bridge, so the agent can observe the result of its own change instead of asserting that the code compiles. For modding, where a build can succeed and the game still crash on load, that is the whole game.

The second contribution is the safety framing. `mod-any-game` covers anti-cheat during recon, `publish-mod` runs a pre-release lint for game files, decompiled code and leaked keys, and the contributing rules rule out game files, decompiled dumps and cheating other players. An agent working on binaries with no stated boundaries will produce something unpublishable; these skills state the boundaries up front.

Third, the knowledge base is a real mechanism rather than a docs folder. `share-field-notes` searches prior art before work starts and writes a note at the end, with exact versions, the route and the gotchas. `um kb search "grand theft auto"` works outside the repository too, so it is usable as a research call before you commit to an approach.

For a Hermes agent, this is also a useful model of a long-horizon task: plan, research, act, verify in the target environment, package, and record what happened. The modding domain is incidental to that structure.

## Usage

| You say | What happens |
|---|---|
| "Can I mod this game" | `game-recon` fingerprints the install, engine, loaders and anti-cheat, then writes MODDING_PLAN.md with a recommended route |
| "Add a nuke to Terraria" | `mod-any-game` picks the engine playbook, `reverse-engineering` finds the damage and item code, and the loop runs to a working build |
| "How does the boss AI decide to attack" | `reverse-engineering` decompiles the relevant assembly or reads live memory, then traces the decision path |
| "Generate sprites for a new unit" | `fal-assets` generates the art, `asset-pipeline` cuts it to the engine's frame size and heading count |
| "Does the mod actually work" | `game-automation` launches the game, drives to the test scene, screenshots and reads the in-game bridge |
| "Make a trailer for this mod" | `showcase-video` records the window, picks moments from contact sheets and cuts a titled video from an EDL |
| "Port my 1.12 Forge mod to Fabric" | `port-a-mod` pins the source version, builds an adaptation matrix and ports unit by unit with drift tests |

## Verification

Read the recon skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/rehan-remade/universal-modder/main/skills/game-recon/SKILL.md | head -20
```

It should open with a description about working out whether a specific installed game can be modded, covering install location, engine version, anti-cheat and loaders, and producing `MODDING_PLAN.md`.

After install, confirm the skill count and that the CLI is reachable:

```bash
ls .agents/skills | wc -l
um --help
```

The count should be 13, matching the three copies of the skill set, and every `um` subcommand ships its own `--help` with examples. If `um` is missing, the plugin hook did not run and the `uv tool install` line above is the fix.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| reverse-engineering | Pass | Pass | Pass |
| mod-any-game | Pass | Pass | Warn |
| game-recon | Pass | Pass | Warn |

The skills are instructions, but they instruct an agent to run Ghidra, IDA, Frida, Cheat Engine, RenderDoc, Blender and PowerShell with embedded C#. That is a legitimate toolkit for the job and also a broad set of capabilities to hand an autonomous agent. Run modding work in a sandbox or a dedicated VM, keep the game and SDK files out of any repository, and do not point the memory tooling at processes you do not own.

The fal key is the main credential. Store it with `um fal key set` rather than exporting it from a shell profile, and check `um fal key status` to confirm the source. The two optional paid services, Sprixen and Voidless, each take their own key through `um sprixen key set` and `um voidless key set`, so scope and rotate them separately.

There is also a legal dimension the README states plainly: no game files, no decompiled dumps, no cheating other players. Anti-cheat protected games are out of bounds in practice as well as by policy, and `publish-mod` will block a release that ships game assets.

## Limitations

- Snapshot data, verified 2026-11-07: 20,760 combined installs across 13 indexed listings; 9,510 GitHub stars; MIT; last pushed 2026-11-06. Counts drift over time.
- The 39 SKILL.md files are 13 skills mirrored three times. `skills/` is the source, and `.agents/skills` plus `.claude/skills` are copies, so an edit to a mirror is lost on the next sync.
- `game-automation` is Windows-first, with notes for Linux and macOS. Agents on a headless server cannot run the verification loop, which is the part that makes the set work.
- Asset generation costs money. `fal-assets` needs a fal key and bills per generation, and `um sprixen` and `um voidless` are separate paid services. Only `um comfy` runs locally without a key.
- You need to own and install the game. `game-recon` fingerprints an installed copy, so nothing here works as a paper exercise.
- The three-agent team in `agents/` uses several times the tokens of one agent. The README recommends it only for long mods, and it is optional.

## Related

- [Reverse Engineering Skills - Frida and IDA Setup](/hermes/skills/catalog/p4nda0s-reverse-skills-setup)
- [Yaklang Hack Skills - Offensive Security Toolkit Setup](/hermes/skills/catalog/hack-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `um kb search` before `game-recon`. Prior art on the same engine saves more time than any amount of decompilation, and the command works outside a clone.
- Start with a vertical slice rather than a feature list. One working item that the game loads and the agent can see is worth more than a plan covering twenty.
- Keep `MODDING_PLAN.md` and the field note in the repository from day one. They are the only artifacts that survive a context reset mid-mod.
- Point `asset-pipeline` at the engine's real frame size before generating anything. Regenerating art that is one pixel off the sprite grid is the most common wasted pass.
- Never install a mod on a save you care about. The README's own loop assumes a lab copy of the game, and `um backup` exists for the save folders.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
