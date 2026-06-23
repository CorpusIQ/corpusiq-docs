---
title: Herman's Skill Playbook — Setup Guide
description: Execution skills by Herman (Hermes Agent) — GitHub installs, plugin management, DuckDB ops, API config, data analysis, memory management, GDrive uploads. 8 skills in 1 playbook.
skill_name: herman-skill-playbook
author: darraappen2 (Herman)
stars: 0
license: Not specified
created: June 19, 2026
last_updated: June 22, 2026
---

# Herman's Skill Playbook — Setup Guide

**Author:** [darraappen2](https://github.com/darraappen2)
**Repo:** [darraappen2/herman-skill-playbook](https://github.com/darraappen2/herman-skill-playbook)
**Created:** June 19, 2026

A single comprehensive playbook by Herman (a Hermes Agent) containing 8 execution-focused skills: GitHub installs, plugin management, service management, DuckDB operations, API configuration, data analysis, memory management, and Google Drive uploads.

> *"Eksekusi dulu, diskusi belakangan"* — Execute first, discuss later.

---

## What's Included

| # | Skill | Description |
|---|-------|-------------|
| 1 | **GitHub Install** | Install skill/plugin from GitHub — inspect, clone, copy |
| 2 | **Plugin Install** | Install platform adapters into Hermes plugins directory |
| 3 | **Service Management** | Start/poll/kill background processes with health checks |
| 4 | **Database Ops** | DuckDB query, backup, CSV import |
| 5 | **API Config** | Setup provider/model via `hermes config set` CLI |
| 6 | **Data Analysis** | Multi-dimensional analysis (divisi/bulan/dept/outlet) via DuckDB |
| 7 | **Memory Management** | Save/update/delete facts cross-session via `memory` tool |
| 8 | **Upload GDrive** | rclone copy/sync to Google Drive |

---

## Core Principles

The playbook enforces five execution principles:

1. **🔥 Load skill first, then execute** — ALWAYS use `skill_view(name='...')` BEFORE running a task. Skills contain the correct workflow.
2. **Execute first, discuss later** — Run commands, see results, then correct if needed.
3. **Inspect before install** — Check repo/file structure before executing.
4. **Backup before changing** — Always backup config/DB before modification.
5. **Verify after execution** — Confirm results are accurate before reporting.

### When to Use Skill vs Execute Code

| Situation | Use | Example |
|-----------|-----|---------|
| Data analysis, download, ETL | `skill_view` → `terminal`/`execute_code` | Load gdrive-csv-duckdb then query |
| Install tool/plugin from GitHub | `skill_view` → `terminal` | Load github-repo-management |
| Setup service (API router, etc.) | `skill_view` → `terminal` | Load service-management |
| Ad-hoc task, one-shot script | `execute_code` directly | Quick calculation, format conversion |
| Simple 1-liner query | `terminal` directly | `duckdb db.duckdb -c "SELECT 1"` |

---

## Installation

### Quick Install

```bash
# Clone the repo
git clone https://github.com/darraappen2/herman-skill-playbook.git /tmp/herman-playbook

# Copy the playbook to your Hermes home
cp /tmp/herman-playbook/herman-skill-playbook.md ~/.hermes/

# Copy the backup script
cp /tmp/herman-playbook/scripts/backup.sh ~/.hermes/scripts/
```

### As a Hermes Skill

```bash
# Create as a formal skill
cp /tmp/herman-playbook/herman-skill-playbook.md ~/.hermes/skills/herman-playbook/SKILL.md

# Load in any Hermes session
skill_view(name='herman-playbook')
```

---

## Skill Details

### 1. GitHub Install

Inspect a repo's structure before cloning and install the skill/plugin.

```bash
# Inspect repo structure
python -c "import urllib.request, json
url='https://api.github.com/repos/<owner>/<repo>/contents/'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
data = json.load(urllib.request.urlopen(req))
print('\n'.join(f\"{item['name']}|{item['type']}\" for item in data))"

# Clone & install shallow
git clone --depth 1 <repo-url> /tmp/<repo-name>
cp -r /tmp/<repo-name>/skills/<skill-name> ~/.hermes/skills/
```

### 2. Plugin Install

Install platform adapters into Hermes plugins directory.

```bash
cp -r /tmp/<repo>/<plugin-name> ~/.hermes/plugins/

# Verify structure
ls -la ~/.hermes/plugins/<plugin-name>/
```

### 3. Service Management

Launch, monitor, and control background processes.

```bash
# Start in background with persistence
terminal(background=true, notify_on_complete=false) <command>

# Check status
process(action='poll', session_id='proc_xxx')

# Health check
curl -s http://localhost:<port>/ | head -c 200
ss -ltnp | rg ':<port>'
```

### 4. Database Operations

DuckDB query, backup, and CSV import.

```bash
# Query
duckdb /path/to/db.duckdb -c "SELECT * FROM table LIMIT 5"

# Backup before modification
cp /path/to/db.duckdb /path/to/db.duckdb.bak.$(date +%Y%m%d)

# CSV import
duckdb /path/to/db.duckdb -c \
  "CREATE TABLE IF NOT EXISTS data AS SELECT * FROM read_csv_auto('/path/to/file.csv')"
```

### 5. API Configuration

Configure Hermes provider/model via CLI.

```bash
# Set config
hermes config set model.provider ''
hermes config set model.base_url 'http://localhost:20128/v1'
hermes config set model.api_key '<api-key>'
hermes config set model.default '<provider>/<model-id>'
```

### 6. Data Analysis

Multi-dimensional analysis using DuckDB — division, month, department, outlet.

```bash
# Example: Sales analysis by division and month
duckdb /path/to/db.duckdb -c "
  SELECT division, strftime('%Y-%m', date) as month, SUM(amount) as total
  FROM sales
  GROUP BY division, month
  ORDER BY division, month
"
```

### 7. Memory Management

Cross-session fact persistence using Hermes' `memory` tool.

```python
# Save a fact
memory(action='add', target='memory', content='User prefers concise responses')

# Update a fact
memory(action='replace', target='memory', old_text='User prefers...', content='Updated...')

# Remove outdated
memory(action='remove', target='memory', old_text='Outdated fact...')
```

### 8. Upload GDrive

rclone-based Google Drive sync.

```bash
# Copy to GDrive
rclone copy /path/to/file gdrive:folder/ --progress

# Sync (mirrors — deletes remote files not in source)
rclone sync /path/to/dir gdrive:folder/ --progress

# Fast listing for large directories
rclone ls gdrive:folder/ --fast-list
```

---

## Backup Script

The included `scripts/backup.sh` provides a cron-ready backup template:

```bash
#!/bin/bash
# Copy to crontab: 0 2 * * * /home/hermes/.hermes/scripts/backup.sh

BACKUP_DIR="/home/hermes/backups/$(date +%Y%m%d)"
mkdir -p "$BACKUP_DIR"

# Backup configs
cp ~/.hermes/config.yaml "$BACKUP_DIR/"
cp ~/.hermes/profiles/corpusiq/config.yaml "$BACKUP_DIR/profile-config.yaml"

# Backup databases
cp /path/to/*.duckdb "$BACKUP_DIR/"

# Upload to GDrive (optional)
rclone copy "$BACKUP_DIR" gdrive:hermes-backups/$(date +%Y%m%d)/
```

---

## Why This Matters

Herman's playbook fills a critical gap: **operational execution patterns for Hermes agents in production**. Unlike most skills that focus on what an agent should do conceptually, this playbook provides the exact commands, patterns, and gotchas for common operational tasks:

- **Load-before-execute discipline** — Enforces the skill-first pattern that prevents agents from hallucinating workflows
- **Backup-before-mutate** — Every DB config change is backed up first
- **Health-check verification** — Services are verified with real curl/port checks, not assumptions
- **Rclone for GDrive** — Uses the battle-tested rclone instead of fragile API wrappers
- **Practical DuckDB** — Real queries for multi-dimensional analysis, not toy examples

---

## Dependencies

| Dependency | Required For |
|------------|-------------|
| DuckDB CLI | Database operations, data analysis |
| rclone | Google Drive uploads |
| Python 3.10+ | Repo inspection scripts |
| Hermes Agent | All operations |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) | [darraappen2/herman-skill-playbook on GitHub](https://github.com/darraappen2/herman-skill-playbook)*
