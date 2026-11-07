---
title: "CC Godot - Game Development Plugin for Agents"
description: "zate/cc-godot on skills.sh: 5.2K combined installs across 4 listings; Godot 4 UI, GDScript development, debugging and optimisation skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cc-godot-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "godot", "game development", "gdscript"]
---

# CC Godot - Setup Guide

**Source:** [zate/cc-godot](https://www.skills.sh/zate/cc-godot) via skills.sh - 5.2K combined installs across 4 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 19 stars, no LICENSE file in the repository root, branch `main`, last pushed 2025-11-09, 4 SKILL.md directories under `plugins/gd/skills/`
**Category:** Godot game development for agents: project setup, GDScript development, debugging and rendering optimisation
**Quality Tier:** 🟡 Yellow - all four sampled skills pass Gen Agent Trust Hub, Socket and Snyk, but the repository has no LICENSE file and has not been pushed since 2025-11-09.

This is a Claude Code plugin rather than a plain skill pack. The four skills sit under `plugins/gd/skills/` and ship alongside slash commands (`/gd:setup`, `/gd:init-game`, `/gd:run`, `/gd:stop`), a game-planning agent, a session-start hook that validates the environment, and shell helpers for environment setup. The README describes it as "a comprehensive Claude Code plugin for Godot game development with namespaced commands, intelligent agents, and automated environment setup".

The skill half is what transfers to other agents. `godot-ui` carries Control node and theme knowledge for menus, HUDs, inventories and dialogue boxes, `godot-development` covers scenes, nodes, GDScript and project structure, `godot-optimization` covers profiling and bottlenecks, and `godot-debugging` covers parser errors and crashes. Each is a long reference document in `SKILL.md` form, which is why they install well on their own.

## Installation

The README's own path is the Claude Code plugin route. It lists three prerequisites first: Godot Engine 4.5.1 or later, Node.js 18 or later for the MCP server, and a built Godot MCP server. The MCP build block is quoted verbatim from the README, including its placeholder clone URL:

```bash
git clone <godot-mcp-repo-url> ~/projects/godot-mcp
cd ~/projects/godot-mcp
npm install
npm run build
```

Then the marketplace and the plugin itself, again verbatim:

```
/plugin marketplace add https://github.com/your-username/godot-claude-plugin
/plugin install gd@godot-gamedev
```

Both of those carry template placeholders: `<godot-mcp-repo-url>` and `your-username`. They have to be replaced with the real Godot MCP server repository and the repository you cloned `zate/cc-godot` from. The README notes the plugin then answers to the `/gd:*` namespace.

For agent skills outside Claude Code, the install route the skills.sh listing page shows is the shorter path, and it skips the plugin machinery:

```bash
npx skills add zate/cc-godot
```

After either install, the README's quick start says to open the Godot project and run `/gd:setup`, which auto-detects the Godot installation, verifies the MCP server build, writes `.mcp.json` into the project and validates the result. The README is explicit that Claude Code must be restarted afterwards, because MCP configuration only loads at startup.

## What It Provides

Three listings clear the 500-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| godot-ui | 2,680 | Godot's UI system: Control node anchors and containers, themes and styling, responsive layouts, and menu, HUD, inventory and dialogue patterns |
| godot-development | 1,435 | Godot Engine development: scene creation, node management, GDScript programming and project structure for 2D and 3D projects |
| godot-optimization | 724 | Performance work: the built-in profiler, performance monitors, bottleneck identification, and optimisation for 2D and 3D games |

The remaining 1 indexed listing ranges from 378 to 378 installs: godot-debugging, parser and syntax errors, crash interpretation and troubleshooting.

Two naming details matter when you go looking for files. The install index calls the second skill `godot-development` while the directory is `plugins/gd/skills/godot-dev/`; the frontmatter inside that directory declares `name: godot-development`, so they are the same skill. The README's plugin structure section shows only `skills/godot-dev/` and does not mention the other three, so the index is the more complete view of what shipped.

Each skill's frontmatter scopes itself tightly. `godot-ui` triggers on "Godot UI/menu creation or styling", `godot-development` on "working with Godot projects, creating or modifying scenes, adding nodes, writing game scripts", `godot-optimization` on "improving game performance or analyzing performance issues", and `godot-debugging` on "helping fix Godot errors, crashes, or unexpected behavior".

## Why This Matters for Hermes Agents

Godot's API surface is wide and version-sensitive, and public code samples are split across the 3.x and 4.x lines. An agent writing GDScript from memory produces a plausible mix: `KinematicBody2D` instead of `CharacterBody2D`, `instance()` instead of `instantiate()`, signal connections in the 3.x style. The `godot-development` skill opens with a node taxonomy that is 4.x throughout, so the vocabulary it hands the agent is current.

UI is the highest-install skill in the set for a reason. Godot menus are built from Control nodes with anchors, offsets, size flags and containers, and getting a HUD to scale correctly is a layout problem that models tend to solve with absolute positions. `godot-ui` covers the anchor and container model directly, along with theme resources and the common game-UI patterns (inventory grids, dialogue boxes, HUDs).

Debugging is the place where a general model wastes the most turns. Godot parser output is terse, and the fixes are specific: consistent indentation, missing colons, child order for collision shapes. `godot-debugging` collects those error strings and their causes, which turns a guess-and-rerun loop into a lookup.

For a Hermes agent the practical value is a consistent 4.x vocabulary across scene edits, scripts and UI, plus a profiler workflow for the performance pass that follows. The MCP dependency is what makes the loop tight, because the agent can drive the editor rather than describing edits for a human.

## Usage

| You say | What happens |
|---|---|
| "Create a player scene with a sprite and a collision shape" | `godot-development` supplies the node tree (CharacterBody2D, Sprite2D, CollisionShape2D in the right order) and the MCP tools create it in the editor |
| "Build a main menu with a settings panel" | `godot-ui` drives containers, anchors and theme overrides instead of fixed positions |
| "My game stutters when enemies spawn" | `godot-optimization` walks the profiler and the performance monitors to find the bottleneck before suggesting changes |
| "Parse Error: Expected end of statement" | `godot-debugging` matches the message to its usual causes (indentation, missing colon) and points at the line |
| "Why is my inventory grid broken at other resolutions?" | The UI skill applies the container and size-flag model, plus the responsive layout patterns |
| "Start a new 2D platformer project" | `/gd:init-game` runs the planning agent, which asks about genre and mechanics and scaffolds `scenes/`, `scripts/`, `assets/` and `resources/` |
| "Run the game so I can test this" | `/gd:run` launches it through the plugin command, and `/gd:stop` closes it |

## Verification

Read a skill before installing it. These paths returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/zate/cc-godot/main/plugins/gd/skills/godot-ui/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/zate/cc-godot/main/plugins/gd/skills/godot-dev/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/zate/cc-godot/main/plugins/gd/skills/godot-optimization/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/zate/cc-godot/main/plugins/gd/skills/godot-debugging/SKILL.md | head -20
```

Each should open with `name:` and `description:` frontmatter, then a heading and the reference body. Note the `allowed_tools` key in the frontmatter and read it before you install: `godot-debugging` lists `mcp__godot__*`, Read, Write, Edit, Glob, Grep and Bash, so the skill is asking for shell access, not only Godot MCP tools.

After install, confirm all four skill directories arrived:

```bash
ls plugins/gd/skills
```

That should print `godot-debugging`, `godot-dev`, `godot-optimization` and `godot-ui`. If you installed through the skills route instead, list the directory your installer reported and expect the same four names.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| godot-ui | Pass | Pass | Pass |
| godot-development | Pass | Pass | Pass |
| godot-optimization | Pass | Pass | Pass |
| godot-debugging | Pass | Pass | Pass |

The skill payload is markdown, but the plugin around it is not inert. It ships hooks (`SessionStart` environment validation), slash commands, shell scripts (`validate-env.sh`, `setup-mcp.sh`, `init-project.sh`) referenced through `${CLAUDE_PLUGIN_ROOT}`, and a `.mcp.json.template`. Installing the plugin means installing all of that, and the session hook runs on every start. That is the reason to prefer the skills route if you only want the Godot knowledge.

The MCP dependency is the second consideration. The Godot MCP server is a separate Node process that receives tool calls and manipulates your project, and the README never names its source, only a placeholder URL. Vet whichever server you point `.mcp.json` at before giving an agent write access to a game project.

The licence question is unresolved in the repository itself. The README ends with a License section reading "MIT License - See LICENSE file for details", but there is no LICENSE file in the repository root, and the GitHub metadata records no licence. Treat it as source-available with an MIT intent rather than a licensed distribution until the file appears.

## Limitations

- Snapshot data, verified 2026-11-07: 5,217 combined installs across 4 indexed listings; 19 GitHub stars; no LICENSE file; last pushed 2025-11-09. Counts drift over time.
- The repository has not been pushed since 2025-11-09, so nothing here reflects Godot releases after that date. The README's own floor is Godot 4.5.1 and Node 18, and anything newer is untested.
- No LICENSE file in the repository root, while the README's License section claims MIT and points at a file that is not there. Reuse terms are therefore ambiguous.
- The README's install block is incomplete by design: the Godot MCP clone URL (`<godot-mcp-repo-url>`) and the marketplace URL (`https://github.com/your-username/godot-claude-plugin`) are placeholders, so both have to be resolved manually before the commands do anything useful.
- The plugin assumes Claude Code. The namespace commands, the game-planning agent and the session hook do not exist for other agents, which leaves only the four skills.
- The README documents one skill (`godot-dev`) while four are indexed and present in the tree, so the README is a poorer map than the directory listing.

## Related

- [GD Agentic Skills - Godot 4 Agent Setup](/hermes/skills/catalog/gd-agentic-skills-setup)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup)
- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Take the skills route if you only want knowledge. `npx skills add zate/cc-godot` avoids the hooks, the slash commands and the MCP configuration entirely.
- Pin the Godot version in the project before you start. The suite is written against 4.x, and a 3.x project will get advice that compiles nowhere.
- Ask for the node tree before the script. "Which nodes and which order" is where `godot-development` pays off, and it makes scene diffs reviewable.
- Run the profiling pass before the optimisation pass. `godot-optimization` is organised around the profiler and the performance monitors, and guesses without a measurement tend to move the bottleneck rather than remove it.
- Keep the MCP server out of the repository you ship. It belongs at `~/projects/godot-mcp` per the README, and `.mcp.json` should stay project-local rather than committed with absolute paths.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
