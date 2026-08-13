---
title: Obsidian Agent Skills Setup Guide
description: Install and configure kepano/obsidian-skills (44K★) for Hermes Agent — workflows for open Obsidian formats, vault management, and note operations.
category: hermes-skills
publisher: kepano
stars: 44,167
maturity: production
license: MIT
skills_sh: https://skills.sh/kepano/obsidian-skills
source: https://github.com/kepano/obsidian-skills
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/obsidian-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Obsidian Agent Skills — Setup Guide

Official Obsidian Agent Skills by [kepano](https://github.com/kepano/obsidian-skills) (44,167★ GitHub stars). Agent Skills-spec-compatible workflows for open Obsidian formats — vault management, note creation, linking, and plugin operations. MIT licensed, production-grade.

## What It Provides

- **Vault navigation** — browse, search, and traverse Obsidian vaults
- **Note creation & editing** — create, update, and link notes using Obsidian-flavored Markdown
- **Wikilink management** — resolve, create, and audit `[[wikilinks]]`
- **Plugin awareness** — understand Dataview, Kanban, Calendar, and other common plugin formats
- **Template workflows** — apply Obsidian templates to new notes
- **Graph analysis** — query the knowledge graph for related notes and orphans

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/kepano/obsidian-skills

# Or via Hermes CLI
hermes skills install skills-sh/kepano/obsidian-skills

# Manual clone
git clone https://github.com/kepano/obsidian-skills.git ~/.hermes/skills/obsidian-skills
```

## Configuration

The skill needs the path to your Obsidian vault:

```yaml
# In your Hermes profile config
obsidian:
  vault_path: "~/Documents/Obsidian"  # or your vault location
  daily_notes_folder: "Daily"
  templates_folder: "Templates"
```

## Key Workflows

### 1. Create a linked note

Ask Hermes to create a note with proper wikilinks:

```
Create a meeting note in my Obsidian vault about the Q3 planning session.
Link it to the [[Q3-2026]] and [[Product-Roadmap]] notes.
```

### 2. Query the knowledge graph

```
What notes in my vault are orphans (no inbound links)?
Show me all notes connected to [[CorpusIQ]].
```

### 3. Apply templates

```
Create a new project note using the Project template in my vault.
```

### 4. Daily notes integration

```
Add today's tasks to my daily note and link any active projects.
```

## Verification

```bash
# Test that the skill loads
hermes skills list | grep obsidian

# Test vault access
hermes chat -q "List the top-level folders in my Obsidian vault at ~/Documents/Obsidian"
```

## Compatibility

- **Hermes Agent**: Full support via agentskills.io spec
- **Claude Code**: Supported
- **OpenClaw**: Supported
- **Obsidian**: v1.5.0+ (any vault with .obsidian config)

## Pitfalls

- **Vault path must be absolute** — `~` expansion may not work in all harnesses. Use full paths.
- **Large vaults (>10K notes)**: First scan may be slow. Use `.obsidianignore` patterns to exclude large binary folders.
- **Plugin-dependent features**: Dataview queries, Kanban boards, and Calendar entries require those plugins to be installed and active in the vault.
- **Sync conflicts**: If using Obsidian Sync, ensure the agent operates on the local vault copy — not a sync daemon that might conflict.

## See Also

- [Obsidian Agent Skills repo](https://github.com/kepano/obsidian-skills)
- [agentskills.io spec](https://agentskills.io/)
- [Obsidian Developer Docs](https://docs.obsidian.md/)
- [Hermes Kanban Obsidian Integration](/hermes/skills/catalog/hermes-kanban-obsidian-integration-setup/)

---

*Setup guide by CorpusIQ. Source: [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) (MIT).*
