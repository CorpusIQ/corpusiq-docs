---
title: Hermes Kanban Obsidian Integration — Task Management Setup Guide
description: Bridge Hermes Agent with Obsidian vaults for Kanban-style task management — sync agent task boards with your knowledge base.
publisher: aradotso/hermes-skills
installs: 136
quality_tier: 🔵 Community
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-kanban-obsidian-integration-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes Kanban Obsidian Integration — Task Management Setup Guide

The Hermes Kanban Obsidian Integration bridges Hermes Agent with Obsidian vaults. Hermes agents can read, create, and update Kanban boards stored in Obsidian — syncing agent task management with your personal knowledge base.

**Publisher:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills)  
**Source:** skills.sh  
**Quality Tier:** 🔵 Community

---

## What It Does

- **Obsidian Kanban Sync:** Hermes reads/writes Kanban boards in your Obsidian vault
- **Task Creation:** Hermes creates tasks on boards from conversation context
- **Status Updates:** Agent automatically moves tasks across columns (Todo → Doing → Done)
- **Metadata Enrichment:** Tasks get agent-added context, links, and tags
- **Bidirectional:** Changes made in Obsidian are visible to Hermes and vice versa

---

## Prerequisites

| Requirement | Check |
|-------------|-------|
| Hermes Agent installed | `hermes --version` |
| Obsidian installed | App or vault directory accessible |
| Obsidian Kanban plugin | Community plugin installed in Obsidian |
| `npx` available | `npx --version` |

---

## Installation

### Step 1: Install Obsidian Kanban Plugin

In Obsidian:
1. Settings → Community Plugins → Browse
2. Search "Kanban" by mgmeyers
3. Install and Enable

### Step 2: Install the Skill

```bash
npx skills add https://github.com/aradotso/hermes-skills --skill hermes-kanban-obsidian-integration
```

### Step 3: Configure Vault Path

```bash
hermes skill invoke hermes-kanban-obsidian-integration \
  --config vault_path="~/Documents/Obsidian/CorpusIQ"
```

---

## Configuration

Create `~/.hermes/obsidian/config.yaml`:

```yaml
vault_path: "~/Documents/Obsidian/CorpusIQ"
kanban_folder: "Kanban"            # Subfolder for Kanban boards
default_board: "Agent Tasks"       # Default board name
sync_interval: 60                   # Seconds between sync checks
auto_create_boards: true            # Create boards if they don't exist
link_style: wikilink                # wikilink | markdown
```

---

## Usage

### Create a Task from Hermes

```
"Add a task to research competitors to my Agent Tasks board"
```

Hermes translates this to:

```bash
hermes skill invoke hermes-kanban-obsidian-integration \
  --board "Agent Tasks" \
  --add "Research competitors" \
  --column "Todo" \
  --tags "research,competitors,q3-2026" \
  --due "2026-08-07"
```

### List Tasks on a Board

```bash
hermes skill invoke hermes-kanban-obsidian-integration --board "Agent Tasks" --list
```

**Sample Output:**
```
Board: Agent Tasks
━━━━━━━━━━━━━━━━━━━━━━━━━
Todo (3):
  📋 Research competitors [research] Due: Aug 7
  📋 Draft content calendar [content] Due: Aug 5
  📋 Audit SEO performance [seo]

Doing (1):
  🔄 Social media sweep [social] Started: Jul 31

Done (12):
  ✅ Setup email monitoring [infra] Completed: Jul 30
  ... (11 more)
━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Move a Task

```bash
hermes skill invoke hermes-kanban-obsidian-integration \
  --board "Agent Tasks" \
  --task "Research competitors" \
  --move "Doing"
```

### Add Context to a Task

```bash
hermes skill invoke hermes-kanban-obsidian-integration \
  --board "Agent Tasks" \
  --task "Research competitors" \
  --note "Top 3 competitors identified: Synthex, AgentFlow, TaskPilot. See [[Competitive Analysis]]"
```

---

## Obsidian View

From Obsidian, the board looks like a standard Kanban board. Tasks added by Hermes include:

- `🤖` prefix to distinguish agent-created tasks
- Auto-generated metadata (created date, agent profile, session ID)
- WikiLinks to relevant notes
- Tags for filtering

---

## Integration with CorpusIQ

For CorpusIQ workflows:

- **Task Tracking:** All agent tasks visible in Obsidian alongside human tasks
- **Meeting Prep:** Hermes populates a board with pre-meeting research
- **Daily Standup:** Hermes fills a "Yesterday/Today/Blockers" Kanban
- **Content Pipeline:** Track content from idea → draft → review → published

### Example: Daily Standup Board

```bash
hermes skill invoke hermes-kanban-obsidian-integration \
  --board "Daily Standup" \
  --add-column "Yesterday" \
  --add-column "Today" \
  --add-column "Blockers"
```

---

## Verification

```bash
# Check connection to vault
hermes skill invoke hermes-kanban-obsidian-integration --check

# Create test board
hermes skill invoke hermes-kanban-obsidian-integration \
  --board "Test Board" \
  --add "Test task from Hermes" \
  --column "Todo"

# Verify it appears in Obsidian
# Open Obsidian → Kanban folder → Test Board
```

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "Vault not found" | Wrong vault path | Verify path with `ls ~/Documents/Obsidian/` |
| "Kanban plugin not detected" | Plugin not installed | Install "Kanban" plugin in Obsidian Community Plugins |
| Tasks not syncing | Sync interval too long | Reduce `sync_interval` or manually trigger sync |
| Duplicate tasks | Race condition with manual edits | Use `--idempotent` flag to prevent duplicates |

---

## Related Skills

- [Oh-My-Hermes Workflow](/hermes/skills/catalog/oh-my-hermes-workflow-setup/) — Workflow framework
- [Minions Mission Control](/hermes/skills/catalog/minions-hermes-mission-control-setup/) — Multi-agent coordination
- [Obsidian Giveaway Pack](/hermes/skills/catalog/hermes-obsidian-giveaway-pack-setup)

---

*Discovered July 31, 2026 · Published by aradotso/hermes-skills · 136 installs*
