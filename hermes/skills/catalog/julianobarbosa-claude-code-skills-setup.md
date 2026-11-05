---
title: "Julianobarbosa Skills - Data and Editor Toolkit"
description: "julianobarbosa/claude-code-skills on skills.sh: 14.1K combined installs across 173 listings; MarkItDown, Obsidian vaults, Neovim and ArgoCD."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/julianobarbosa-claude-code-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "devops", "obsidian", "markitdown"]
---

# Julianobarbosa Skills - Setup Guide

**Source:** [julianobarbosa/claude-code-skills](https://www.skills.sh/julianobarbosa/claude-code-skills) via skills.sh - 14.1K combined installs across 173 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 15 stars, MIT licence, last pushed 2026-10-27, 128 SKILL.md directories under skills/
**Category:** DevOps and knowledge work for agents: document conversion, Obsidian vaults, editor configuration and platform runbooks
**Quality Tier:** 🟡 Beta - Snyk Fail on power-bi and a Snyk Warn on markitdown; MIT; 15 stars.

This is a working engineer's skill collection rather than a vendor product pack. The README opens with "55+ custom Claude Code skills for Python development, DevOps, infrastructure automation, and productivity", grouped into authentication, cloud, containers, DNS, developer tools, observability, Obsidian, languages and utilities. Every skill follows the same shape: a `SKILL.md` with YAML frontmatter, plus optional `references/` and `scripts/` directories loaded only when needed.

The install mechanism is deliberately plain. There is no plugin manifest and no marketplace entry; `scripts/install-skills.sh` symlinks skill directories into `~/.claude/skills/`, and any agent that reads a skills directory can point at `skills/<name>/SKILL.md` instead.

## Installation

The README documents the Claude Code routes. Clone into the user-level skills directory:

```bash
git clone https://github.com/julianobarbosa/claude-code-skills.git ~/.claude/skills
```

For a single project, the README clones into that project instead:

```bash
git clone https://github.com/julianobarbosa/claude-code-skills.git .claude/skills
```

The README writes `YOUR_USERNAME` in both commands as a placeholder; substitute `julianobarbosa`. It also documents a script that symlinks individual skills, run from the clone root:

```bash
./scripts/install-skills.sh
```

The README lists a fourth route for the Claude desktop app, uploading individual `.skill` packages through Settings > Skills. No skills.sh CLI install command is documented, and there is no plugin marketplace manifest, so the clone plus symlink path is the one that works for a non-Claude agent.

## What It Provides

Six listings clear the 200 install threshold.

| Skill | Installs | Use For |
|---|---|---|
| markitdown | 1,654 | Converting PDF, Word, PowerPoint, Excel, images, audio, HTML, CSV, JSON, XML, ZIP, EPub, Jupyter notebooks and YouTube URLs to Markdown |
| obsidian-vault-management | 310 | Creating and editing vault notes, templates and daily notes, and building dataview queries over the vault |
| neovim | 305 | Working inside a modular Lua Neovim configuration: plugins, keybindings, LSP servers and debugging |
| markitdown-skill | 252 | A second MarkItDown entry point, listed separately from markitdown |
| obsidian | 243 | Obsidian fundamentals: vault operations, plugin development, URI scheme automation and Local REST API integration |
| argocd-advanced | 216 | Multi-cluster ApplicationSet generators, automated image updates, cluster bootstrapping and workload onboarding |

The remaining 167 indexed listings range from 1 to 199 installs.

## Why This Matters for Hermes Agents

Document conversion is the quiet bottleneck in most agent work. A PDF, a deck, an Excel workbook or a YouTube URL all have to become text before anything else can happen, and `markitdown` is the most-installed skill in this repo because it wraps Microsoft's converter with the input types agents actually meet.

The Obsidian pair is a useful split to copy. `obsidian` covers vault operations, plugin development and the Local REST API; `obsidian-vault-management` covers note and template authoring plus dataview queries. One skill changes the vault, the other writes inside it, which keeps each prompt short.

The infrastructure skills show the same discipline at a larger scale: `argocd-advanced` handles multi-cluster ApplicationSets and image updates rather than repeating basic CLI commands, and the observability group covers Prometheus, Grafana, Loki, Mimir, Tempo and Pyroscope as separate small skills.

For a Hermes agent, the value is breadth with a consistent loading contract. Skills carry references and scripts in known subdirectories, so an agent can read the frontmatter, decide, and load one reference instead of ingesting the whole repository.

## Usage

| You say | What happens |
|---|---|
| "Convert this deck and these PDFs to Markdown" | markitdown runs the converter across the listed inputs and returns Markdown per file |
| "Turn this YouTube talk into notes" | markitdown accepts the URL as an input type and writes the transcript Markdown |
| "Add a daily note template to my vault" | obsidian-vault-management writes the template and wires the daily notes config |
| "List every note tagged project with a dataview query" | obsidian-vault-management builds the query against the vault |
| "Add a keybinding and an LSP server to my Neovim config" | neovim edits the Lua configuration following its lazy.nvim layout |
| "Roll out a new cluster with an ApplicationSet" | argocd-advanced generates the ApplicationSet and walks the bootstrapping steps |
| "Why is my ArgoCD image updater not tagging?" | argocd-advanced reads the image updater reference and checks the registry configuration |

## Verification

Fetch the most-installed skill and confirm the frontmatter and converter scope:

```bash
curl -fsSL https://raw.githubusercontent.com/julianobarbosa/claude-code-skills/main/skills/markitdown/SKILL.md | head -6
```

The response should start with `name: markitdown` and a description listing the supported formats. After running the install script, confirm the symlinks landed as one directory per skill:

```bash
ls ~/.claude/skills | head -20
```

If you used the symlink script, confirm the links resolve to the clone:

```bash
ls -l ~/.claude/skills/markitdown
```

The repo's deeper skills keep extra material in `references/` and `scripts/`, so `argocd-advanced` is worth opening to check that nested reference directories came along with the link.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| markitdown | Pass | Pass | Warn |
| obsidian-vault-management | Pass | Pass | Pass |
| neovim | Pass | Pass | Pass |
| power-bi | Pass | Pass | Fail |

## Limitations

- Snapshot data, verified 2026-11-04: 14,078 combined installs across 173 indexed listings; 15 GitHub stars; MIT licence; last pushed 2026-10-27. Counts drift over time.
- skills.sh indexes 173 listings against 128 SKILL.md directories in the tree, and several names are near duplicates, so the listing count overstates the number of distinct skills.
- The README's own statistics table still reports 55 skills, 200+ reference docs, about 25 Python scripts and about 20 shell scripts, which predates the current tree. Treat both the README count and the listing count as approximate.
- `power-bi` carries a Snyk Fail in the sampled set and sits below the install threshold, so it is absent from the table but present in the repo. Review it before use.
- The install script symlinks rather than copies. Moving or deleting the clone breaks every installed skill, so keep it at a stable path.
- No plugin manifest or skills.sh CLI command is documented, so agents other than Claude Code have to be pointed at `skills/<name>/SKILL.md` by hand.

## Related

- [Obsidian Agent Skills Setup Guide](/hermes/skills/catalog/obsidian-skills-setup)
- [memoria-vault - Multi-Agent Research OS for Obsidian Setup](/hermes/skills/catalog/memoria-vault-setup)
- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill by hand before running the script. Copying or symlinking `skills/markitdown` alone takes a minute and proves your agent reads the directory at all.
- Prefer `obsidian-vault-management` for authoring and `obsidian` for API and plugin work. Loading both for a note edit wastes context on plugin development material.
- Give `markitdown` a file path rather than pasted text. The skill's value is the format detection and the converter flags, not summarization.
- Treat `argocd-advanced` as the escalation path after `argocd`. The advanced skill assumes the core CLI and API material is already understood.
- Keep the clone out of a directory that syncs to a cloud drive. Symlinks and sync clients disagree, and the failure looks like a missing skill.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
