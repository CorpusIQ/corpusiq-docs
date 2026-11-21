---
title: "Canva Skills - Design Workflows for Agents"
description: "canva-sdks/canva-skills: 15 Canva design skills for editing, resizing, brand checks and bulk templates - 2.8K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/canva-sdks-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "canva", "design", "mcp"]
---

# Canva Skills - Design Workflows for Agents

**Source:** [canva-sdks/canva-skills](https://www.skills.sh/canva-sdks/canva-skills) via skills.sh - 2.8K combined installs across 15 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [canva-sdks/canva-skills](https://github.com/canva-sdks/canva-skills) - 168 stars, Apache-2.0 license, main branch, last pushed Nov 20, 2026; a marketplace-style package where root host entrypoints point at one shared plugin under `plugins/canva/`, which holds the active skills in `plugins/canva/skills/<name>/SKILL.md`.
**Category:** Design and Creative Automation
**Quality Tier:** 🟡 Yellow - every sampled skill passes Gen Agent Trust Hub and Socket, with Snyk Warn cells on 6 of the 15 sampled skills.

Canva's own SDK team publishes this skills package for agents that drive Canva through its MCP server. It is a marketplace-style repository: root-level manifests for Antigravity, Claude, Cursor and Codex all point at one shared plugin package at `plugins/canva/`, and that package carries the active skill set plus the MCP registration. The split matters in practice, because the plugin is the installable unit and the skills travel with it.

The package covers the work a business agent actually does with Canva: resizing one campaign across channels, editing an existing design, implementing reviewer feedback, checking a design against a brand kit, bulk-producing designs from a spreadsheet, and translating or time-fitting a presentation. Several skills are read-only by design (design feedback, brand check), which makes them safe first steps on someone else's campaign. First seen in the Nov 21, 2026 morning sweep.

## Installation

Every host uses the Canva MCP server at `https://mcp.canva.com/mcp`. Connect the `canva` server and sign in to Canva when prompted.

Claude Code and Antigravity install from the repository as a plugin marketplace:

```bash
/plugin marketplace add canva-sdks/canva-skills
/plugin install canva@canva-skills
```

Codex has its own plugin commands:

```bash
codex plugin marketplace add canva-sdks/canva-skills
codex plugin add canva@canva-skills
codex mcp login canva
```

In Cursor, open the repository (its `.cursor/mcp.json` and `.cursor/skills/` load automatically) or open `plugins/canva/` directly, then connect the `canva` server under Settings, MCP Tools.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| canva-resize-for-social-media | 410 | channel-ready variants of one campaign: TikTok, Instagram, LinkedIn, Facebook, YouTube, Pinterest and custom sizes |
| canva-edit-design | 398 | the safe edit engine: text changes, image swaps, reformatting, repositioning, resize and retitle |
| canva-bulk-create | 357 | one design per row from a CSV, spreadsheet, pasted table or JSON through a brand template |
| canva-design-feedback | 347 | read-only critique of hierarchy, copy, spacing, consistency, readability and accessibility |
| canva-implement-feedback | 333 | reads comment threads, applies the clear-cut changes and flags decisions for a human |
| canva-branded-presentation | 324 | branded deck creation and rebuild in the brand kit |
| canva-brand-check | 307 | read-only brand audit: off-palette colours, non-brand fonts, logo misuse, off-tone copy |

The remaining 8 indexed listings range from 4 to 86 installs: canva-cli (86), canva-translate-design (84), canva-classroom-helper (53), canva-presentation-time-fitting (47), canva-resize-for-all-social-media (13), canva-agent-guide (11), canva-autofill (10) and canva-instagram-post (4).

## Why This Matters for Hermes Agents

Design work is where agents fail quietly: a generated asset looks plausible, ships off-brand, and nobody notices until a customer sees it. This package splits the job so the risky part is checkable. The brand-check and design-feedback skills are read-only, so an agent can audit a campaign before touching it and report what diverges instead of silently rewriting the design. The edit engine is deliberately narrow and the other skills build on it, which means an agent has one path for changes rather than six improvised ones.

The bulk path is the operationally interesting one for operators: a brand template plus a spreadsheet becomes one design per row, which is exactly the manual production work that eats a marketing team's week. Autofill reads the template's field schema first, uploads media before mapping, and leaves missing fields unfilled rather than inventing content, so a half-complete data set produces a partial design instead of a wrong one. The resize skill returns an edit link per channel rather than pretending a crop is a design, and the implement-feedback skill reads real review comments so a human decision stays a human decision. Because every skill is scoped by the Canva MCP tool surface, an agent cannot wander outside the account it is connected to.

## Usage

| You say | What happens |
|---|---|
| Check this Canva design against our brand kit | Runs the read-only brand check and lists off-palette colours, wrong fonts and logo misuse |
| Give me feedback on this deck before I send it | Returns structured critique on hierarchy, copy, spacing and accessibility |
| Make one version of this campaign for every social channel | Produces resized copies per platform and hands back the edit links |
| Change the headline on slide 3 and swap the hero image | Edits the existing design in place and retitles it |
| Fill in our event template for each of the 40 speakers | Reads the template schema, maps the table, creates one design per row |
| Implement the comments the client left on the pitch deck | Applies the clear changes and flags anything that needs a decision |
| Translate this presentation and fit every slide's copy | Produces the translated variant with text fitted per slide |

## Verification

Confirm the plugin landed and the skills are visible to your agent:

```bash
ls ~/.claude/plugins/canva/skills 2>/dev/null || ls plugins/canva/skills
```

Review the router skill's instructions before installing, since it decides which tool each Canva request routes to:

```bash
curl -sL https://raw.githubusercontent.com/canva-sdks/canva-skills/main/plugins/canva/skills/canva-agent-guide/SKILL.md | head -40
```

Check that the Canva MCP connection is authenticated in the host before running any write skill, then run the read-only brand check on one known design as a first test.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| canva-resize-for-social-media | Pass | Pass | Pass |
| canva-edit-design | Pass | Pass | Pass |
| canva-bulk-create | Pass | Pass | Warn |
| canva-design-feedback | Pass | Pass | Pass |
| canva-implement-feedback | Pass | Pass | Warn |
| canva-branded-presentation | Pass | Pass | Warn |
| canva-brand-check | Pass | Pass | Warn |
| canva-cli | Pass | Pass | Pass |
| canva-translate-design | Pass | Pass | Pass |
| canva-classroom-helper | Pass | Pass | Warn |
| canva-presentation-time-fitting | Pass | Pass | Pass |
| canva-agent-guide | Pass | Pass | Warn |
| canva-autofill | Pass | Pass | Pass |
| canva-instagram-post | Pass | Pass | Pass |

The write skills operate on live designs in a real Canva account, so scope the connected account to the team workspace you intend to change and start with the read-only skills.

## Limitations

- Snapshot data, verified Nov 21, 2026: 2,784 combined installs across 15 indexed listings; 168 GitHub stars; Apache-2.0 license; last pushed Nov 20, 2026. Counts drift over time.
- The install index outruns the active plugin: canva-branded-presentation, canva-translate-design, canva-classroom-helper and canva-presentation-time-fitting carry install counts but live under `plugins/canva/inactive-skills/`, which the hosts do not register.
- Autofill and bulk create depend on brand templates that have data fields, and Canva's README states autofill requires a paid Canva plan.
- Skill behaviour depends on the Canva MCP server's tool surface, so the exact calls an agent can make change with the server, not with the skill files.
- Six of the 15 sampled skills carry Snyk Warn cells; read the skill instructions before granting write access to a shared brand account.

## Related

- [Sumi - UX/UI Design Intelligence Skills](/hermes/skills/catalog/phazurlabs-sumi-setup)
- [Cuellar Design Skills - UX and Design Skills Setup](/hermes/skills/catalog/cuellarfr-design-skills-setup)
- [Vibe Building Skills - Design and Marketing](/hermes/skills/catalog/sanky369-vibe-building-skills-setup)
- [Claude Design Skillstack - 3D & Animation Setup](/hermes/skills/catalog/claudedesignskills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start every engagement with canva-brand-check or canva-design-feedback on one existing design; both are read-only and tell you whether the brand kit is configured before you change anything.
- For bulk work, read the template's field schema first and keep a column that names the output, so each generated design is titled from a distinguishing value rather than a row number.
- Ask for channel variants only when the source layout survives a crop; a landscape poster restretched to vertical is worse than a rebuild, which is what canva-edit-design is for.
- Keep comment-driven changes separate from your own edits, so a client can see exactly which feedback was applied and which needs their decision.
- Pin the plugin version you tested rather than tracking the marketplace head, because the router skill changes which MCP tool each request uses.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
