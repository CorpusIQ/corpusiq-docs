---
title: Auto Updater — OpenClaw Self-Updating Setup Guide
description: Setup guide for the openclaw-auto-updater skill — keep your OpenClaw agent and its skills automatically updated. Zero-touch maintenance for long-running agents.
last_updated: 2026-07-08
---

# Auto Updater — OpenClaw Self-Updating

**Publisher:** [teylersf](https://skills.sh/teylersf/openclaw-auto-updater) | **Installs:** 1,148 | **Category:** DevOps

Automatically keeps your OpenClaw installation and all installed skills up to date. Checks for new versions on a configurable schedule, downloads updates, and applies them — all without manual intervention.

## Prerequisites

- OpenClaw installed and running
- Node.js 18+
- Git installed (for pulling skill updates)
- `npx` available

## Installation

```bash
npx skills add teylersf/openclaw-auto-updater/auto-updater
```

## Configuration

```json
{
  "autoUpdater": {
    "schedule": "0 4 * * *",
    "channels": {
      "openclaw": "stable",
      "skills": "latest"
    },
    "notifyOnUpdate": true,
    "backupBeforeUpdate": true,
    "autoRestart": true,
    "maxRetries": 3
  }
}
```

| Setting | Default | Description |
|---------|---------|-------------|
| `schedule` | `0 4 * * *` | Cron expression — when to check for updates |
| `channels.openclaw` | `stable` | Release channel: `stable`, `beta`, or `canary` |
| `channels.skills` | `latest` | Skill update channel: `latest` or `pinned` |
| `notifyOnUpdate` | `true` | Log/notify when updates are found and applied |
| `backupBeforeUpdate` | `true` | Backup config before applying updates |
| `autoRestart` | `true` | Restart agent after updates complete |
| `maxRetries` | `3` | Retry failed updates before alerting |

## Capabilities

### Automatic OpenClaw Updates

- Checks GitHub releases for new OpenClaw versions
- Downloads and verifies release artifacts
- Applies updates during low-activity windows
- Validates checksums before installation

### Skill Updates

- Scans all installed skills for newer versions
- Pulls latest from skills.sh or GitHub
- Handles dependency conflicts
- Runs skill-specific migration scripts

### Safety Features

- Pre-update backups of config files
- Rollback on failed updates
- Notification of breaking changes
- Dry-run mode for testing

## CLI Reference

```
Command                        Description
─────────────────────────────────────────────────
auto-updater check             Check for available updates
auto-updater apply             Apply pending updates
auto-updater status            Show current versions
auto-updater rollback          Revert last update
auto-updater dry-run           Preview updates without applying
auto-updater schedule          Show/change update schedule
```

## CorpusIQ Use Cases

- **Long-running production agents:** Zero-touch maintenance for agents running 24/7 on DGX/Mac Mini
- **Multi-agent deployments:** Keep all worker agents at the same version across nodes
- **Cron-based agents:** Ensure nightly-scheduled agents always run the latest code
- **Security patching:** Automatic application of security fixes as they're released

## Troubleshooting

### Update fails to apply

```bash
# Check current version
auto-updater status

# Run in verbose mode
auto-updater check --verbose

# Try dry-run first
auto-updater dry-run
```

### Skill update conflicts

```bash
# List affected skills
auto-updater check --skills-only

# Update one at a time
auto-updater apply --skill-by-skill

# Force reinstall problematic skill
npx skills remove <skill> && npx skills add <skill>
```

### Agent won't restart after update

```bash
# Check backup was created
ls -la ~/.openclaw/backups/

# Restore from backup
auto-updater rollback

# Check logs for specific failure
tail -100 ~/.openclaw/logs/update.log
```

---

*← [Auto Updater Setup Guide](/hermes/skills/catalog/openclaw-auto-updater-setup/) | [Discovery Page](/hermes/skills/marketplace/new-june28-2026/) →*

*↑ [Skills Catalog](/hermes/skills/catalog/)*

---

*Part of the Hermes Skills Library — curated by CorpusIQ. Content remains attributed to original authors and repositories. [CorpusIQ](https://corpusiq.io) — one MCP endpoint, all your business tools.*
