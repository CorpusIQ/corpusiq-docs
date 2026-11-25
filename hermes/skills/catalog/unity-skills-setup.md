---
title: "Unity Skills - Game Development Automation Setup"
description: "besty0728/unity-skills - 7.0K combined installs across 92 indexed listings: AI automation skills that drive Unity scenes through a REST server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/unity-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "unity", "game development"]
---

# Unity Skills - Setup Guide

**Source:** [besty0728/unity-skills](https://www.skills.sh/besty0728/unity-skills) via skills.sh - 7.0K combined installs across 92 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [besty0728/unity-skills](https://github.com/besty0728/unity-skills) - 1,974 stars, MIT license, last pushed Nov 24, 2026, main branch; the skills ship as one UnitySkills template at SkillsForUnity/unity-skills~/SKILL.md, with per-tool copies under .agents/skills/ and .claude/skills/.
**Category:** Game Development (Unity)
**Quality Tier:** 🟡 Yellow - unity-skills carries a Warn on all three checks (Gen Agent Trust Hub, Socket, Snyk), and unity-shader carries a Snyk Warn; the other 13 sampled skills pass all checks.

besty0728/unity-skills is a REST-API-based automation engine that lets an AI agent drive the Unity Editor directly through Skills. The README describes it as 873 REST skills across 55 categories, generated from 57 source files, plus 30 advisory design modules for architecture, script design, performance, and maintainability. Rather than shipping 873 separate SKILL.md files, the repo bundles everything into a single UnitySkills template at SkillsForUnity/unity-skills~/SKILL.md, installed through the Unity Package Manager and then wired into an AI tool with a one-click installer.

The skills.sh index lists 92 individual listings for this repo, but they ship as one set, which is why the install band is flat: dozens of listings sit between 88 and 99 installs, with only the umbrella unity-skills (198) and a few top modules such as unity-uitoolkit (121) and unity-ui (107) above that band.

## Installation

Install the Unity package via the Unity Package Manager using the git URL (stable, main branch):

```
https://github.com/Besty0728/Unity-Skills.git?path=/SkillsForUnity
```

Beta and pinned versions use #beta or a tag such as #v1.6.0. In Unity, open Window > UnitySkills and start the server with the toggle. Then use the one-click AI Config tab: pick your tool's icon and click Install, which copies the unity-skills~/ template into the tool's skill directory (plus the optional unity-skills-eval/ evaluation skill). For a manual install, copy the unity-skills~/ template into the tool's skills root as unity-skills/ and add an agent_config.json under scripts/.

## What It Provides

The indexed listings do not map one-to-one to separate SKILL.md files; they are the module names inside one shipped template. The table below covers the eight listings at or above the 95-install line, with module scopes from the README's category overview.

| Skill | Installs | Use For |
|---|---|---|
| unity-skills | 198 | main template skill that routes the agent to the REST skills and advisory modules |
| unity-uitoolkit | 121 | UI Toolkit: UXML and USS files, UIDocument, PanelSettings, and runtime data binding |
| unity-ui | 107 | UGUI: Canvas, Button, Text, InputField, Dropdown, ScrollView, and layout |
| unity-shader | 100 | shader creation, URP templates, compile checks, and keyword management |
| unity-editor | 100 | editor control: play mode capture, frame stepping, live state inspection, and undo-redo |
| unity-scriptableobject | 99 | ScriptableObject create, read-write, serialized-property paths, and JSON import-export |
| unity-architecture | 98 | advisory module for architecture design guidance |
| unity-scriptdesign | 96 | advisory module for C# script design guidance |

The remaining 84 indexed listings range from 1 to 94 installs.

## Why This Matters for Hermes Agents

For a Hermes agent working on a Unity project, this suite turns the Editor into a scriptable surface the agent can operate through typed REST calls rather than hand-edited scene files. The three-tier permission model (Approval, Auto, Bypass) and the JSONL audit trail matter for agents, because every write to a scene or prefab is gated by risk metadata and recorded, and a failed operation rolls back so a wrong change does not leave the project dirty. The 873 skills span the surface a game project actually touches: prefabs, materials, lights, cameras, animations, physics, navmesh, shaders, UI Toolkit, and the major asset packages. For a builder running Hermes agents, the practical win is that "set up a third-person camera rig" or "batch-create these prefabs" resolves to a concrete skill call with a dry-run rehearsal available before anything is written. The main caveat is setup: these are not plain Markdown files you copy in; they require installing the Unity package, starting a local REST server, and letting the one-click installer place the template into your AI tool.

## Usage

| You say | What happens |
|---|---|
| Create a ScriptableObject with these fields | Uses unity-scriptableobject to create and write the object |
| Add a button and text to this Canvas | Uses unity-ui to place and configure UGUI elements |
| Capture the play mode state to debug this frame | Uses unity-editor for live state inspection and frame stepping |
| Make a URP shader and check it compiles | Uses unity-shader for URP templates and compile checks |
| Build a UXML panel with data binding | Uses unity-uitoolkit for UXML/USS and runtime data binding |
| Preview a batch of prefab changes before writing | Uses the batch endpoint's dryRun and plan modes |

## Verification

Confirm the shipped template resolves on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/besty0728/unity-skills/main/SkillsForUnity/unity-skills~/SKILL.md | head -40
```

Returns 200. The template's SKILL.md is the single entry point; docs/SETUP_GUIDE.md and docs/OPERATING_MODES.md in the repo cover full setup and the permission model. After installing, review the template and its skills/ module docs before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| unity-skills | Warn | Warn | Warn |
| unity-uitoolkit | Pass | Pass | Pass |
| unity-ui | Pass | Pass | Pass |
| unity-shader | Pass | Pass | Warn |
| unity-editor | Pass | Pass | Pass |
| unity-scriptableobject | Pass | Pass | Pass |
| unity-architecture | Pass | Pass | Pass |
| unity-scriptdesign | Pass | Pass | Pass |
| unity-test | Pass | Pass | Pass |
| unity-terrain | Pass | Pass | Pass |
| unity-package | Pass | Pass | Pass |
| unity-skills-index | Pass | Pass | Pass |
| unity-optimization | Pass | Pass | Pass |
| unity-material | Pass | Pass | Pass |
| unity-light | Pass | Pass | Pass |

15 of 92 listings were sampled. 13 pass all three checks; unity-skills carries a Warn on all three, and unity-shader carries a Snyk Warn.

## Limitations

- Snapshot data, verified Nov 25, 2026: 6,981 combined installs across 92 indexed listings; 1,974 GitHub stars; MIT license; last pushed Nov 24, 2026. Counts drift over time.
- The 92 indexed listings ship as one set (a single UnitySkills template plus module docs), so the install counts are flat: dozens of listings sit at 88 to 99 installs and do not represent independent skill adoption.
- The indexed skill names (unity-ui, unity-shader, unity-editor, and so on) do not map one-to-one to SKILL.md files in the tree; the repo ships one template SKILL.md with 85 module docs (55 REST/module docs and 30 advisory design modules).
- Setup is heavier than copying Markdown files: it requires the Unity package, a running local REST server, and the one-click AI configuration.
- The maintenance baseline is Unity 2022.3+; some Unity 2021 compatibility logic may remain, but future work targets 2022.3+ and Unity 6.
- The editor window bundles a CJK font under the SIL Open Font License 1.1, separate from the MIT license on the code.

## Related

[Unity AI Skills - Official Unity 29-Skill Game Dev Suite Setup](/hermes/skills/catalog/unity-ai-skills-setup) | [Awesome GameDev Skills - 77 Game Engine Agent Suite](/hermes/skills/catalog/awesome-gamedev-agent-skills-setup) | [CC Godot - Game Development Plugin for Agents](/hermes/skills/catalog/cc-godot-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the Unity package via the Unity Package Manager git URL, then use the one-click AI Config installer to place the template into your tool.
- Start in Approval mode and use the dryRun and plan modes to rehearse calls before writing to a scene.
- Read docs/SETUP_GUIDE.md and docs/OPERATING_MODES.md for the full permission model and governance.
- Prefer batch skills for multi-object work; most modules support *_batch operations.
- Use the Evaluation set (41 tasks, /unity-skills-eval) to benchmark how well your agent drives the suite.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
