---
title: "Obsidian Agent Skills - Markdown, Bases and Canvas"
description: "obsidianmd/obsidian-skills: 428.0K combined installs across 7 listings, the official Obsidian skills for Markdown, Bases, JSON Canvas and the CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/obsidian-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "obsidian", "notes", "markdown"]
source: "https://github.com/obsidianmd/obsidian-skills"
skills_sh: "https://skills.sh/obsidianmd/obsidian-skills"
---

# Obsidian Agent Skills - Setup Guide

**Source:** [obsidianmd/obsidian-skills](https://www.skills.sh/obsidianmd/obsidian-skills) via skills.sh - 428.0K combined installs across 7 indexed listings; first seen Nov 14, 2026 (rename reconcile, formerly kepano/obsidian-skills)
**GitHub:** 52,390 stars, MIT license, `main` branch, last pushed 2026-11-11, 7 `SKILL.md` files under `plugins/obsidian/skills/`
**Category:** Notes and knowledge management: Obsidian Flavored Markdown, Bases, JSON Canvas, the Obsidian CLI and headless vault operations
**Quality Tier:** 🟡 Yellow - the official Obsidian repository under MIT, with four of six sampled skills passing all three auditors and one Gen Agent Trust Hub Warn on obsidian-cli.

These are Obsidian's own agent skills, and the four largest are why the package is worth installing. obsidian-markdown, obsidian-cli, obsidian-bases and json-canvas each sit between 77,571 and 96,586 installs, and together they cover the three open formats Obsidian publishes plus the CLI that drives a vault. The remaining three skills are smaller and more specific: defuddle for stripping a web page down to clean markdown, knap for rendering templates from JSON or CSV, and obsidian-headless for sync and publish without the desktop app.

The repo moved from `kepano/obsidian-skills` to `obsidianmd/obsidian-skills`, so an older clone or an older install command still points at the retired owner. GitHub redirects the clone, but the skills.sh listings, the plugin marketplace entry, the star count and the install figures all moved with it. This page follows the current owner: 428,048 combined installs across 7 listings, where the earlier snapshot recorded roughly 44K.

Every skill follows the Agent Skills specification, so the same files load in Claude Code, Codex, OpenCode and Cursor. Two of the seven need outside tooling: obsidian-cli needs the Obsidian CLI, and obsidian-headless needs the Obsidian Headless service, both documented at help.obsidian.md.

## Installation

Claude Code marketplace, from a terminal:

```bash
claude plugin marketplace add obsidianmd/obsidian-skills
claude plugin install obsidian@obsidian-skills
```

Then `claude plugin update obsidian@obsidian-skills` picks up new skills. Inside a Claude Code session the same two commands work as `/plugin marketplace add obsidianmd/obsidian-skills` and `/plugin install obsidian@obsidian-skills`.

The skills.sh route works for any skills-compatible agent:

```bash
npx skills add https://github.com/obsidianmd/obsidian-skills
```

Codex uses `codex plugin marketplace add obsidianmd/obsidian-skills` and then installs Obsidian from the plugin directory. For OpenCode, clone the whole repository into `~/.opencode/skills/obsidian-skills` rather than copying the inner `skills/` folder, because the skills resolve at `plugins/obsidian/skills/<name>/SKILL.md`. Cursor installs Obsidian from the Cursor Marketplace.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| obsidian-markdown | 96,586 | Create and edit Obsidian Flavored Markdown: wikilinks, embeds, callouts, properties and other Obsidian-only syntax. |
| obsidian-cli | 85,544 | Drive a vault through the Obsidian CLI, including plugin and theme development. |
| obsidian-bases | 83,050 | Create and edit Bases files with views, filters, formulas and summaries. |
| json-canvas | 77,571 | Create and edit JSON Canvas files with nodes, edges, groups and connections. |
| defuddle | 77,353 | Extract clean markdown from web pages, removing the clutter that burns context tokens. |
| knap | 7,623 | Render markdown templates from JSON or CSV data, including batch file generation. |
| obsidian-headless | 321 | Sync and publish vaults from the command line without the desktop app. |

All 7 indexed listings appear in the table above, so there is no tail.

## Why This Matters for Hermes Agents

The value is format fidelity. A general-purpose agent writing to a vault produces plain markdown and breaks the moment it meets a callout, a property block, a base view or a canvas node. These skills carry the syntax rules for the three open formats Obsidian publishes, so an agent writes a file the app can open rather than a file that renders as raw text.

The CLI and headless skills turn that from file editing into vault operations. An agent can run a command against a live vault, work with plugins and themes, and sync or publish without the desktop app in the loop, which is what a scheduled job needs.

The rename history is the operational lesson. Because the repository moved owners, three different identity strings are in circulation for one project: the retired `kepano` owner, the current `obsidianmd` owner and the plugin id `obsidian@obsidian-skills`. Pin the current owner in scripts, and treat any older clone as stale rather than as a second project.

## Usage

| You say | What happens |
|---|---|
| "Write a note with a callout and properties" | obsidian-markdown applies Obsidian Flavored Markdown for callouts, properties and embeds. |
| "Build a table view over my notes" | obsidian-bases writes a Base with views, filters and formulas. |
| "Map this project as a canvas" | json-canvas emits nodes, edges and groups in JSON Canvas format. |
| "List what changed in my vault today" | obsidian-cli runs the vault command through the Obsidian CLI. |
| "Publish the vault without opening the app" | obsidian-headless syncs and publishes from the command line. |
| "Turn this article into clean notes" | defuddle extracts readable markdown from the page before the agent summarises it. |
| "Generate 40 client notes from a CSV" | knap renders the template against each row in a batch. |

## Verification

Probe the skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/obsidianmd/obsidian-skills/main/plugins/obsidian/skills/obsidian-markdown/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/obsidianmd/obsidian-skills/main/plugins/obsidian/skills/obsidian-bases/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/obsidianmd/obsidian-skills/main/plugins/obsidian/skills/obsidian-cli/SKILL.md
```

Every skill lives at `plugins/obsidian/skills/<name>/SKILL.md`, and the README documents the same seven names, so an install that produces fewer files is incomplete.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| obsidian-markdown | Pass | Pass | Pass |
| obsidian-cli | Warn | Pass | Pass |
| obsidian-bases | Pass | Pass | Pass |
| json-canvas | Pass | Pass | Pass |
| defuddle | Pass | Pass | Warn |
| knap | Pass | Pass | Warn |

Six of the seven listings were sampled. Four pass all three auditors; obsidian-cli takes a Gen Agent Trust Hub Warn and defuddle and knap each take a Snyk Warn. No sampled skill fails any auditor. obsidian-headless, the smallest listing, publishes no verdict. The skills are markdown and instruction files with no executable payload of their own, but obsidian-cli and obsidian-headless shell out to Obsidian tooling that the skill-level verdicts do not cover.

## Limitations

- Snapshot data, verified 2026-11-14: 428,048 combined installs across 7 indexed listings; 52,390 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- The repository moved from `kepano/obsidian-skills` to `obsidianmd/obsidian-skills`. GitHub redirects the old clone URL, but install scripts and skills.sh links that cite the retired owner should be repointed.
- Two skills depend on outside tooling: obsidian-cli on the Obsidian CLI and obsidian-headless on Obsidian Headless. Neither ships in this repository.
- obsidian-headless publishes no security verdict on skills.sh, and the sample covers only 6 of the 7 listings.
- vault access depends on a real vault path and, for plugin and theme work, on the plugins being installed and active. The README assumes a working Obsidian install rather than describing vault setup.

## Related

- [Obsidian Visual Skills - Canvas, Excalidraw and Mermaid](/hermes/skills/catalog/axton-obsidian-visual-skills-setup)
- [Hermes Kanban Obsidian Integration](/hermes/skills/catalog/hermes-kanban-obsidian-integration-setup)
- [Baoyu Design - Local Artifact Editors for Agents](/hermes/skills/catalog/baoyu-design-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install through the plugin marketplace rather than copying folders: `claude plugin update obsidian@obsidian-skills` is then a one-command refresh.
- For OpenCode, clone the whole repo into `~/.opencode/skills/obsidian-skills`; copying only the inner `skills/` folder breaks the path resolution.
- Ask for the format by name ("a Base", "a canvas") so the agent loads the right skill instead of writing plain markdown.
- Use defuddle before summarising a long article; clean markdown is markedly cheaper in tokens than a rendered page.
- Check the owner in any tutorial you follow: instructions written for `kepano/obsidian-skills` predate the move to the Obsidian organisation.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
