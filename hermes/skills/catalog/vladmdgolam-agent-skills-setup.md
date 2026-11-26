---
title: "vladmdgolam Agent Skills - Blender and Cinema 4D Setup"
description: "vladmdgolam/agent-skills - 3.4K combined installs: Blender and Cinema 4D MCP skills plus PDF, JS deobfuscation and Figma guides for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vladmdgolam-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "blender", "cinema 4d", "mcp"]
---

# vladmdgolam Agent Skills - Setup Guide

**Source:** [vladmdgolam/agent-skills](https://www.skills.sh/vladmdgolam/agent-skills) via skills.sh - 3.4K combined installs across 12 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [vladmdgolam/agent-skills](https://github.com/vladmdgolam/agent-skills) - 9 stars, MIT license, last pushed Oct 14, 2026, main branch; skills live under skills/<name>/SKILL.md with optional references/ and scripts/ directories.
**Category:** 3D & Design (MCP tooling)
**Quality Tier:** 🟡 Yellow - 2 of 12 listings sampled: blender-mcp carries a Socket Warn, cinema4d-mcp passes all three checks.

vladmdgolam/agent-skills is a collection of skills for AI coding agents, packaged in the Agent Skills format. The install mass is concentrated on one skill: blender-mcp holds 2,782 of the 3,367 combined installs, a Blender MCP expert for scene inspection, Python scripting, GLTF export, and material and animation extraction. cinema4d-mcp is the same idea for Cinema 4D at 110 installs, and a tail of design, document, and session tooling follows.

The README documents the full roster of twelve skills; each lives in skills/<name>/SKILL.md with optional references/ and scripts/ directories.

## Installation

The README documents the skills CLI:

```bash
npx skills add vladmdgolam/agent-skills
```

Or a single skill:

```bash
npx skills add vladmdgolam/agent-skills --skill cinema4d-mcp
```

Skills are packaged instructions that extend agent capabilities with domain-specific knowledge, following the Agent Skills format.

## What It Provides

skills.sh publishes per-skill install counts for all 12 indexed listings. The 7 most-installed skills are listed below; the remaining 5 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| blender-mcp | 2,782 | Blender MCP expert: scene inspection, Python scripting, GLTF export, and material/animation extraction |
| cinema4d-mcp | 110 | Cinema 4D MCP expert: extracting scene data, writing C4D Python scripts, and controlling Cinema 4D through MCP |
| visual-feedback-loop | 64 | capture and inspect rendered output from any web app during iterative development |
| pdf-look-scanned | 58 | make PDF documents look physically scanned, with optional signature replacement |
| reverse-engineer-js | 55 | LLM-assisted deobfuscation of minified or obfuscated JavaScript bundles via humanifyjs |
| time-lens | 54 | analyze and visualize time spent on projects from WakaTime, git, Claude Code, Codex, and Cursor data |
| figma-context-mcp | 50 | use the Figma Context MCP (Framelink) efficiently while avoiding 429 rate-limit errors |

The remaining 5 indexed listings range from 19 to 47 installs.

## Why This Matters for Hermes Agents

The standout is blender-mcp, which turns a live Blender session into something an agent can drive: scene inspection, Python scripting, GLTF export for the web, and the material and animation extraction patterns that otherwise take hours to relearn. Its critical gotchas (export timeouts, modifier handling, Draco pitfalls, texture optimization) are the difference between a working asset pipeline and a broken one. The supporting skills fill adjacent gaps: cinema4d-mcp for the other major DCC, visual-feedback-loop for seeing rendered output during UI and 3D iteration, figma-context-mcp and figma-bridge for design-to-code, and reverse-engineer-js for reading minified bundles. time-lens and agent-sessions are about the agent's own memory and work history rather than a task domain. The caveat is trust: only two of twelve skills carry a skills.sh verdict, and blender-mcp holds a Socket Warn.

## Usage

| You say | What happens |
|---|---|
| Inspect this Blender scene | Uses blender-mcp to read scene info and write Blender Python scripts |
| Export this scene for the web | Uses blender-mcp for GLTF/GLB export and gltf-transform optimization |
| Extract scene data from Cinema 4D | Uses cinema4d-mcp to write C4D Python scripts and read scene data |
| Make this PDF look scanned | Uses pdf-look-scanned for grayscale, noise, and signature replacement |
| Deobfuscate this bundle.js | Uses reverse-engineer-js to run humanifyjs with the right defaults |
| Show me the rendered result | Uses visual-feedback-loop to capture and inspect rendered web output |

## Verification

Confirm the two sampled skills resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/vladmdgolam/agent-skills/main/skills/blender-mcp/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/vladmdgolam/agent-skills/main/skills/cinema4d-mcp/SKILL.md | head -40
```

Both URLs return 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| blender-mcp | Pass | Pass | Warn |
| cinema4d-mcp | Pass | Pass | Pass |

Across the 2 sampled skills there are 5 Pass, 1 Warn, and 0 Fail cells. skills.sh sampled only 2 of the 12 listings, so the other 10 carry no published verdict.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,367 combined installs across 12 indexed listings; 9 GitHub stars; MIT license; last pushed Oct 14, 2026. Counts drift over time.
- blender-mcp carries a Socket Warn verdict and is also the skill with the overwhelming share of installs; read its security page before relying on it.
- skills.sh sampled only 2 of the 12 listings; the other 10 carry no published security verdict.
- The repository is small (9 stars, last pushed Oct 14, 2026), so treat it as a personal collection rather than a maintained product.
- Install counts are top-heavy: blender-mcp holds 2,782 of the 3,367 combined installs.

## Related

[Blender Skills - MCP Production Pipeline](/hermes/skills/catalog/blender-skills-setup) | [Blender Agent Skills - 3D Production Workflows](/hermes/skills/catalog/blender-agent-skills-setup) | [CC Blender Skill - 3D Production for Agents](/hermes/skills/catalog/cc-blender-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install blender-mcp alone if you only need the 3D pipeline: `npx skills add vladmdgolam/agent-skills --skill blender-mcp`.
- For GLTF export, use the headless CLI export pattern to bypass MCP timeouts.
- pdf-look-scanned is for a printed-and-scanned appearance; verify it fits your intended use before relying on it.
- figma-context-mcp and figma-bridge are complementary: one is the Framelink MCP, the other a fork that reads live Figma through the plugin without API limits.
- Only two skills carry verdicts; re-check skills.sh before trusting the unsampled ten.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
