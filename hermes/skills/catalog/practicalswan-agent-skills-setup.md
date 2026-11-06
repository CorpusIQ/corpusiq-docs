---
title: "PracticalSwan Agent Skills - 253 Skill Library"
description: "practicalswan/agent-skills on skills.sh: 6.6K combined installs across 200 listings; 253 shared skills for Copilot, Claude Code and Codex."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/practicalswan-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "skill library", "cross-client", "documents"]
---

# PracticalSwan Agent Skills - Setup Guide

**Source:** [practicalswan/agent-skills](https://www.skills.sh/practicalswan/agent-skills) via skills.sh - 6.6K combined installs across 200 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 24 stars, MIT licence, last pushed 2026-10-19, 253 SKILL.md directories at the repository root with AGENTS.md and CLAUDE.md beside them
**Category:** Cross-client agent library: 253 skills shared across Claude Code, Codex and GitHub Copilot with host-aware routing
**Quality Tier:** 🟡 Caution - Snyk Warned on two of five sampled skills (figma-implement-design, tavily-research); every Gen Agent Trust Hub and Socket sample passed; MIT; 24 stars.

This is one person's working skill catalog, published as a repository. The README reports 253 tracked skill folders: 221 maintained skills and 32 copied official Superpowers skills, with a local workspace that can hold more when per-machine overlays are present. The catalog version is 2.0, dated 2026-07-29, and it is explicit about scope: supported clients are GitHub Copilot, Claude Code and Codex, and sync is restricted to three personal skill roots.

What makes it more than a folder dump is the normalization pass. Every maintained skill carries the same frontmatter contract (`name`, `version`, `last_updated`, `tags`, `description`), its own `CHANGELOG.md`, a cross-client portability section, an MCP section naming a preferred server plus a no-MCP fallback, an `Anti-Patterns` section, a `Verification Protocol` section immediately after it, and a final `Related Skills` section. A validator enforces all of that, which means the 221 maintained skills are consistent in shape even where they came from different upstreams.

The collection is assembled rather than authored end to end. The README documents a Tavily suite of eight skills, a Stitch design suite, Figma and Hugging Face imports, NVIDIA deepstream skills, a vendored Codex plugin scanner and a set of official Playwright workflows. Provenance lives in `REFERENCE_SOURCES.md` and `scripts/skill-registry.json`, and individual folders keep their own licence files where the upstream required it.

## Installation

The repository publishes no npm installer of its own. Its documented route is a copy of skill folders into a client skill root, with a PowerShell sync script for the maintainer's three personal roots. On Linux or macOS the equivalent is a clone plus a per-skill copy:

```bash
git clone https://github.com/practicalswan/agent-skills.git
mkdir -p ~/.claude/skills
cp -r agent-skills/powerpoint-ppt ~/.claude/skills/
cp -r agent-skills/frontend-design ~/.claude/skills/
cp -r agent-skills/excel-sheet ~/.claude/skills/
```

Copy only what you need. Each folder is self-contained, and 253 of them at once puts a large description surface in front of the router. The README's own sync script is Windows-only and writes to `C:\Users\LOQ\.claude\skills`, `C:\Users\LOQ\.codex\skills` and `C:\Users\LOQ\.agents\skills`, so do not expect it to run as written on a POSIX host.

If you want the repository's validation pass before installing, it runs on Python and needs no network:

```bash
cd agent-skills
python scripts/validate-skills.py
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| powerpoint-ppt | 1,646 | Building and editing .pptx decks: slide composition from structured content, templates and branding, placeholders, images, and text extraction for review |
| word-document | 794 | Reading and writing .docx files, including tables, footnotes, comments, images, headers, styles, and PDF conversion |
| frontend-design | 231 | Front-end work with deliberate art direction: pages, components, dashboards, marketing sites and commerce flows, checked against rendered output |
| php-development | 64 | PHP 8 work with XAMPP, RESTful APIs, PDO against MySQL or MariaDB, and authentication |
| serena-usage | 62 | Serena MCP project memory and symbol navigation, keeping context and continuity across sessions |
| mongodb-mongoose | 47 | MongoDB schemas, models, aggregation pipelines, migrations and Atlas connections for Node.js and Next.js apps |
| excel-sheet | 40 | Excel workbooks: cell formatting, formulas, charts, pivot tables and spreadsheet analysis |

The remaining 193 indexed listings range from 13 to 39 installs.

## Why This Matters for Hermes Agents

The interesting part of this catalog is not any single skill. It is that the same skill folder is written to run under three different clients at once. Each maintained `SKILL.md` carries a portability section that states what changes between Copilot, Claude Code and Codex, and an MCP section that names a preferred server and then a fallback path for hosts where that server is absent. An agent that reads its own skill file therefore knows what to do when a tool it expected is missing, instead of failing at the first call.

That fallback discipline is the pattern worth copying. Most skill packs assume their tools exist. This one documents the degraded path next to the happy path, which is the difference between a workflow that stops and a workflow that finishes with less.

The `Verification Protocol` section, required immediately after `Anti-Patterns`, is the second pattern. It gives the agent a check it can run against its own output before reporting done, which is what makes a 200 skill catalog usable rather than a menu of claims.

The catalog also includes `agent-skillguard`, a local scanner that reads files for risky instructions, broad permissions, suspicious downloads, prompt-injection patterns and possible secret exposure before a skill is installed, returning file-and-line findings and remediation without running or uploading anything. For anyone routinely installing third-party skills, that is a useful gate to have in the same library.

Finally, the inventory numbering matters when you evaluate coverage. The README's 253 folders include 32 copied official Superpowers skills that the author tracks but does not maintain, and the install index covers 200 listings, so a folder count is not a maintained-skill count.

## Usage

| You say | What happens |
|---|---|
| "Build a 10 slide deck from this outline" | powerpoint-ppt composes slides from the structure, applies layout and template rules, and writes a .pptx |
| "Extract the text from this deck for review" | powerpoint-ppt pulls slide text into a readable form |
| "Review this contract and fix the table formatting" | word-document reads the .docx, edits the table, and preserves styles and footnotes |
| "Redesign this dashboard page with a real art direction" | frontend-design sets a direction, then implements responsive states and checks the rendered result |
| "Set up a PHP API endpoint with PDO" | php-development scaffolds the endpoint, the PDO layer and the auth check |
| "Why does this query return duplicates?" | mongodb-mongoose works through the aggregation pipeline and the schema that produced it |
| "Scan this skill folder before I install it" | agent-skillguard reports risky instructions and secret exposure by file and line |

## Verification

Confirm the skill you installed is the one the index describes. Raw paths are the skill folder at the repository root, on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/practicalswan/agent-skills/main/powerpoint-ppt/SKILL.md | head -8
```

It should open with `name: powerpoint-ppt`, a `version: "2.0"` line, and a description naming .pptx manipulation through an MCP server. Then check that the copy kept the whole folder, because the catalog treats the changelog as part of the skill:

```bash
ls ~/.claude/skills/powerpoint-ppt
```

That should list `SKILL.md`, `CHANGELOG.md`, `examples/`, `scripts/` and `LICENSE.txt`. A folder holding only `SKILL.md` is a partial copy, and the repository's own validator would reject it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| powerpoint-ppt | Pass | Pass | Pass |
| writing-skills | Pass | Pass | Pass |
| figma-implement-design | Pass | Pass | Warn |
| tavily-research | Pass | Pass | Warn |
| figma-generate-design | Pass | Pass | Pass |

Two of the five sampled skills carry a Snyk warning, which is why this guide is tiered Caution rather than Production. The warnings are on a Figma implementation skill and on a Tavily research skill, both of which describe integrations with external services rather than local file work. Read the Snyk finding on the skills.sh security page before enabling either one in a session that holds credentials.

Beyond the sample, the surface varies by folder. This is an assembled catalog: some skills bundle helper scripts under `scripts/`, the Tavily suite documents a CLI install path and reads a `TAVILY_API_KEY`, and the Office skills talk to an MCP server whose availability depends on the host. Prefer the skills that are markdown only when you cannot review a folder, and run `agent-skillguard` against anything you did not read.

## Limitations

- Snapshot data, verified 2026-11-05: 6,614 combined installs across 200 indexed listings; 24 GitHub stars; MIT; last pushed 2026-10-19. Counts drift over time.
- The documentation is written for one Windows machine. Paths like `C:\Users\LOQ\.copilot\skills` appear in the README, AGENTS.md and MIGRATION.md, and the sync script is PowerShell that refuses to write outside three specific roots. Port it before relying on it.
- The repository reports 253 tracked skill folders while the install index covers 200 listings. The difference is a mix of copied Superpowers skills, local overlays and folders with no listing, so neither number is the maintained-skill count.
- 24 stars is a small signal for a catalog this size. Treat it as one practitioner's workspace rather than a reviewed distribution, and read the folder you install.
- Provenance and licensing are per folder. The repository is MIT, individual skills keep their own licence files, and at least one consolidated folder preserves Apache-2.0 art-direction material alongside MIT content. Check the folder's own files before redistribution.
- Two sampled skills carry Snyk warnings, and the sample is five of 200 listings. Verdicts on the other 195 are unread here.

## Related

- [Agentic Awesome Skills (AAS) - 2,000+ Skill Catalog Setup](/hermes/skills/catalog/agentic-awesome-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill](/hermes/skills/catalog/claude-code-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

## Pro Tips

- Install the Office pair first if you work with documents. The two highest-install skills are the PowerPoint and Word skills, they share an MCP dependency worth testing once, and `excel-sheet` reuses it.
- Run the validator on any folder you edit. It enforces section order and rejects changelog headings outside Added, Changed and Fixed, which is a fast way to learn the catalog's conventions.
- Use the `Verification Protocol` section as your acceptance test. The skill states what done looks like, which is cheaper than re-reading the output yourself.
- Keep a copy of `agent-skillguard` in the skill root even if you skip the rest. It is the one skill here that protects the install path rather than a task.
- Pin the commit you copied. There is no installer, so nothing records where a folder came from unless you note the revision yourself.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
