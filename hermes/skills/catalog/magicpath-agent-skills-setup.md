---
title: "MagicPath Agent Skills - UI Component Workflow Setup"
description: "Setup guide for magicpathai/agent-skills - 6.3K combined installs. Search, preview, export, and edit MagicPath UI components from your agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/magicpath-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "ui components", "design tooling"]
---

# MagicPath Agent Skills - Setup Guide

**Source:** [magicpathai/agent-skills](https://www.skills.sh/magicpathai/agent-skills) via skills.sh - 6.3K combined installs across 1 indexed listing; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [magicpathai/agent-skills](https://github.com/magicpathai/agent-skills) (93 stars, no license file; pushed Jul 15, 2026; `skills/<name>/SKILL.md` layout)
**Category:** UI Components / Design Tooling
**Quality Tier:** 🟡 Beta - official MagicPathAI; NO LICENSE file; mixed sampled verdicts (Socket + Snyk Warn)

MagicPathAI publishes the official agent skill for MagicPath: a single `magicpath` skill that teaches the `magicpath-ai` CLI to search, preview, inspect, install, export, create, and edit MagicPath UI components. Beyond the tool surface, it carries the two details component workflows usually miss: how to preserve 1:1 fidelity when moving a MagicPath design into local code, and how to manage MagicPath-hosted skills through `magicpath-ai skills ...`. The repo is packaged for the open Agent Skills ecosystem and installs with Vercel's skills CLI or as a Claude Code, Codex, or Cursor plugin.

It is also the canonical source of truth for the skill: both `npx skills add` and `magicpath-ai setup-skills` install from this repository, so every install path converges on the same maintained payload. The skill activates when a request mentions MagicPath or asks to find, preview, export, add, adapt, create, or edit a component.

---

## Installation

Install in Cursor (from the Cursor marketplace or in-session):

```text
/add-plugin magicpath
```

Install in Claude Code:

```text
/plugin marketplace add MagicPathAI/agent-skills
/plugin install magicpath@magicpath
```

Install in Codex (CLI, app, or VS Code extension):

```text
codex plugin marketplace add MagicPathAI/agent-skills
codex plugin add magicpath@magicpath
```

Install via the Agent Skills CLI (works across harnesses):

```bash
npx skills add https://github.com/MagicPathAI/agent-skills

# Preview the skill payload without installing
npx skills add https://github.com/MagicPathAI/agent-skills --list
```

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| magicpath | 6,307 | Search, preview, inspect, install, export, create, and edit MagicPath UI components; 1:1 design-to-code fidelity |

Every indexed listing for this repo is in the table above; there is no tail.

## Why This Matters for Hermes Agents

Component workflows are where agent output degrades fastest: an agent can write a component, but finding the right existing one, previewing it, and porting it into a codebase without losing the design's fidelity is a chain of tool calls most agents improvise badly. MagicPath's official skill replaces that improvisation with documented operations - search, preview, inspect, install, export, create, edit - that the agent can invoke deliberately. The 1:1 fidelity guidance is the valuable part: moving a design into local code usually loses spacing, tokens, and behavior, and the skill teaches the agent to preserve them instead of eyeballing the result. Because the skill is canonical for both the skills CLI and `magicpath-ai setup-skills`, installs converge on one maintained payload rather than drifting forks. For teams that treat MagicPath as the design surface and their repo as the build surface, the skill is the glue between the two. It is also a compact example of tight skill design: one skill, one tool surface, explicit triggers. Coverage is a single skill, so review the vendor the same way you would any tool that edits local files.

## Usage

| You say | What happens |
|---|---|
| "Find a pricing card component in MagicPath" | The skill searches and previews matching components through the magicpath-ai CLI |
| "Export this component to the components folder" | The selected component is exported into your project tree |
| "Add this MagicPath design to my codebase" | The agent ports it in while following the skill's 1:1 fidelity guidance |
| "Create a canvas component for the hero section" | A new canvas component is created and edited in place |
| "Update the skill on my MagicPath workspace" | Hosted skills are created, retrieved, updated, or imported via magicpath-ai skills commands |
| "What did we use for the last landing page?" | The CLI surfaces component details before any local change is made |

## Verification

```bash
# Confirm the skill is installed for your agent
npx skills list | grep magicpath

# Review the layout-verified skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/magicpathai/agent-skills/main/skills/magicpath/SKILL.md | head -20
```

Plugin installs are visible in the hosting tool's plugin listing (Claude Code, Codex, or Cursor), and every install path lands the same skill content.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| magicpath | Pass | Warn | Warn |

The single sampled skill carries mixed verdicts (Pass on Gen Agent Trust Hub, Warn on Socket and Snyk), and the repo ships no license file, so pair a fresh security review with a licensing conversation before production use.

## Limitations

- No license file: without a LICENSE in the repo, redistribution and vendor terms are unclear; confirm with the publisher before bundling it into your own product.
- Single skill, 93 stars, last pushed Jul 15, 2026; this is a boutique integration, not a broad library.
- Mixed sampled verdicts: Socket and Snyk both return Warn on the one sampled skill.
- The workflow depends on the `magicpath-ai` CLI for its component operations.
- Snapshot data, verified Oct 10, 2026: 6,307 combined installs across 1 indexed listing; 93 GitHub stars; no license file; last pushed Jul 15, 2026. Counts drift over time.

## Related

- [Assistant UI Skills - AI Chat Interface Dev Suite Setup](/hermes/skills/catalog/assistant-ui-skills-setup) - chat interface components that can be sourced through the same workflow
- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup) - pairs with component work that needs token extraction
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup) - audit the result after porting components
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Mention MagicPath explicitly in the request; the skill is built to activate on that cue.
- Export to a folder first and adapt in local code second; that is the documented path to 1:1 fidelity.
- Use the `--list` flag to inspect the payload before adding it to your context.
- Manage hosted skills from the CLI with `magicpath-ai skills ...` instead of editing remote state by hand.
- Treat the mixed verdicts as a prompt to pin the repo revision you reviewed rather than tracking `main`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
