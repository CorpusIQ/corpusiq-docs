---
title: "Terminal Skills - Open-Source Agent Skills Library"
description: "terminalskills/skills: 2.2K combined installs. Open-source SKILL.md agent skill library spanning creative tools, infrastructure and marketing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/terminalskills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "open-source", "creative tools", "infrastructure"]
---

# Terminal Skills - Setup Guide

**Source:** [terminalskills/skills](https://www.skills.sh/terminalskills/skills) via skills.sh - 2.2K combined installs across 35 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [TerminalSkills/skills](https://github.com/terminalskills/skills) - 218 stars, Apache-2.0 license, branch main, last pushed 2026-11-08; skills live under `skills/<name>/SKILL.md` with a generated `_scores.json` beside each and a `skills/index.json` at the root.

**Category:** Open-source agent skills library - creative tools, infrastructure and marketing skills for Claude Code, Codex, Gemini CLI and Cursor

**Quality Tier:** 🟡 Yellow - Apache-2.0 and 218 stars, but three of the 20 sampled listings carry a Warn cell (api-tester on Snyk; after-effects and claude-mem on the Gen Agent Trust Hub); no Fails across the sample.

Terminal Skills is an open-source library of AI agent skills that follows the Agent Skills open standard, published as a single repository and indexed on skills.sh. Each skill is a standalone SKILL.md file that works across Claude Code, OpenAI Codex, Gemini CLI, Cursor and other AI-powered development tools, with the full catalog browsable at terminalskills.io. The library spans creative tools (Blender, DaVinci Resolve, After Effects, FFmpeg), infrastructure (Coolify, Directus, Hono) and marketing (Instagram, Facebook), plus a long tail of framework and platform skills.

The skills.sh index lists 35 of these skills at 2,237 combined installs, but the repository tree carries 1,146 skill directories, each with its own SKILL.md and a generated _scores.json, so the index covers only a small slice of the full catalog. Two skills (the Terminal Skills router and SEOG) are also backed by hosted MCP servers, letting an agent call the catalog as live tools rather than reading instructions only.

## Installation

The README installs skills with the terminal-skills CLI, or by curling a SKILL.md straight into an agent's skills directory. Replace pdf-analyzer with the skill name you want:

```bash
npx terminal-skills install pdf-analyzer
```

Claude Code:

```bash
curl -sL https://raw.githubusercontent.com/terminalskills/skills/main/skills/pdf-analyzer/SKILL.md -o .claude/skills/pdf-analyzer.md
```

OpenAI Codex, Gemini CLI and Cursor use the same curl with a different target directory (.codex/skills, .gemini/skills and .cursor/skills). The two hosted MCP servers (Terminal Skills at https://api.terminalskills.io/api/mcp and SEOG at https://api.seog.ai/mcp) can be added as connectors in claude.ai or as http MCP servers with a bearer token.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| instagram-marketing | 387 | Create, optimize and automate Instagram content: Reels, Stories, carousels, the Graph API and growth tactics. |
| davinci-resolve | 329 | Automate DaVinci Resolve via the Python/Lua scripting API: color grading, batch renders and timeline management. |
| api-tester | 151 | Test REST and GraphQL endpoints with structured assertions, auth flows and response validation. |
| claude-hud | 133 | Build heads-up display dashboards that monitor context usage, tools and sub-agent progress in real time. |
| coolify | 106 | Deploy and manage apps, databases and services on Coolify through the CLI and REST API. |
| hono | 77 | Build a Hono web API with Zod validation, JWT auth, CORS and the type-safe RPC client across runtimes. |
| ui-ux-pro-max | 70 | Search a local design-intelligence library of UI styles, palettes and guidelines, or generate a design system. |
| blender-animation | 66 | Animate 3D objects in Blender with Python (bpy): keyframes, armatures, shape keys, F-Curves and drivers. |
| after-effects | 63 | Script After Effects with ExtendScript or CEP, batch renders and build render pipelines with aerender. |
| yt-dlp | 61 | Download video and audio from YouTube and other platforms: playlists, subtitles, metadata and automation. |
| agent-memory | 56 | Add persistent memory to coding agents: file-based, vector and semantic search that survives sessions. |
| directus | 54 | Build backends and APIs with the Directus headless CMS: data modeling, roles and auto-generated REST/GraphQL. |
| playwright-testing | 51 | Write end-to-end tests with Playwright: page objects, auth, API mocking and CI integration. |
| ffmpeg | 50 | Transcode, convert and edit audio and video with FFmpeg: format conversion, filters and media pipelines. |
| blender-scripting | 50 | Write Blender Python scripts for 3D automation and procedural modeling with the bpy API. |

The remaining 20 indexed listings range from 20 to 38 installs, spanning whisper (38), claude-mem (37), konva (33), security-audit (32) and svgo with blender-render-automation (31 each) down to renovate, pdf-merge-split and facebook-marketing at 20 each.

## Why This Matters for Hermes Agents

Terminal Skills is a useful reference for running a large, open catalog on the Agent Skills standard: every skill is one self-contained SKILL.md with frontmatter and instructions, a generated _scores.json beside it, and a scripts/generate-index.js that builds skills/index.json, so a Hermes builder can copy the layout for a catalog of its own. The distribution story is also worth studying: one CLI (npx terminal-skills install) plus a raw curl into .claude, .codex, .gemini or .cursor directories, which is the simplest possible multi-runtime install path. The creative-tool skills (Blender, DaVinci Resolve, After Effects, FFmpeg) show how a skill can wrap a desktop or command-line production tool, and the MCP pair shows how to graduate a catalog from static instructions to live, routed tools. The scale drift is a useful calibration: the index lists 35 skills while the tree holds 1,146 directories, so a low install count on skills.sh can badly understate a library's actual breadth.

## Usage

| You say | What happens |
|---|---|
| "Grow our Instagram account" | Uses instagram-marketing for Reels-first strategy, content formats and Graph API publishing. |
| "Automate my DaVinci Resolve render queue" | Uses davinci-resolve to script batch renders and timeline management. |
| "Transcribe this podcast to subtitles" | Uses whisper to transcribe audio and emit SRT or VTT subtitles. |
| "Download this YouTube playlist as audio" | Uses yt-dlp to fetch the playlist and extract audio. |
| "Shrink these SVG files" | Uses svgo to strip editor metadata and shorten paths. |
| "Convert this video to mp4" | Uses ffmpeg to transcode and re-encode the file. |
| "Stand up a Hono API with JWT auth" | Uses hono to scaffold a Web Standards API with Zod validation and middleware. |

## Verification

The skills live under `skills/<name>/SKILL.md` on branch main. Fetch one directly to review its frontmatter and instructions before installing:

```bash
curl -sL https://raw.githubusercontent.com/terminalskills/skills/main/skills/instagram-marketing/SKILL.md
```

After a clone, confirm the catalog and its generated index:

```bash
git clone --depth 1 https://github.com/terminalskills/skills.git /tmp/terminal-skills
ls /tmp/terminal-skills/skills/ | wc -l
cat /tmp/terminal-skills/skills/index.json
```

The skills directory holds 1,146 skill folders. Note the README's curl examples spell the org terminal-skills (hyphenated), which no longer resolves; the live repository is github.com/terminalskills/skills.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| instagram-marketing | Pass | Pass | Pass |
| davinci-resolve | Pass | Pass | Pass |
| api-tester | Pass | Pass | Warn |
| claude-hud | Pass | Pass | Pass |
| coolify | Pass | Pass | Pass |
| hono | Pass | Pass | Pass |
| ui-ux-pro-max | Pass | Pass | Pass |
| blender-animation | Pass | Pass | Pass |
| after-effects | Warn | Pass | Pass |
| yt-dlp | Pass | Pass | Pass |
| agent-memory | Pass | Pass | Pass |
| directus | Pass | Pass | Pass |
| playwright-testing | Pass | Pass | Pass |
| ffmpeg | Pass | Pass | Pass |
| blender-scripting | Pass | Pass | Pass |
| whisper | Pass | Pass | Pass |
| claude-mem | Warn | Pass | Pass |
| konva | Pass | Pass | Pass |
| security-audit | Pass | Pass | Pass |
| svgo | Pass | Pass | Pass |

This guide is Yellow because three of the 20 sampled listings carry a Warn cell and none carries a Fail: api-tester (Snyk) and after-effects and claude-mem (Gen Agent Trust Hub). 17 of the 20 sampled listings pass all three auditors, and 15 of the 35 indexed listings were not sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 2,237 combined installs across 35 indexed listings; 218 GitHub stars; Apache-2.0 license; last pushed 2026-11-08. Counts drift over time.
- The tree far outruns the skills.sh index: 1,146 skill directories in the repo versus 35 indexed listings (and the README's own Skills Catalog table highlights only 25), so the install counts above cover a small fraction of the library.
- The README's curl examples reference a hyphenated org (terminal-skills) that returns 404; the live repository is github.com/terminalskills/skills.
- Only 20 of the 35 indexed listings carry security verdicts; the other 15 were not sampled.
- Install counts are low across the board (the top listing has 387 installs), so treat this as a broad, early-stage catalog rather than a heavily adopted suite.

## Related

- [Awesome AI Agent Skills - 103-Skill Agent Library](/hermes/skills/catalog/awesome-ai-agent-skills-setup)
- [Skills Gallery Setup](/hermes/skills/catalog/skills-gallery-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a skill's SKILL.md before installing: it is a single file with frontmatter plus instructions, so the curl approach gives you the whole skill to review.
- Prefer npx terminal-skills install <name> for reproducibility; the raw-curl path pins you to whatever is on main at that moment.
- Use the generated skills/index.json to enumerate the catalog programmatically instead of parsing the README table.
- Because the index lists only 35 of 1,146 skill directories, browse the repo tree or terminalskills.io for the full catalog before concluding a topic is uncovered.
- The two MCP servers turn the catalog into live tools; add the Terminal Skills router (search_skills, get_skill, plan_task) if you want the agent to pick skills on its own.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
