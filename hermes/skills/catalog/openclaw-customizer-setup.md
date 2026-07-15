---
title: OpenClaw Customizer — Setup Guide
description: Portable, version-controlled configuration for Claude Code and OpenAI Codex. Symlink-based skill syncing across machines with Git version control.
---

# OpenClaw Customizer — Setup Guide

## Prerequisites
- **Git** installed
- **Claude Code** and/or **OpenAI Codex** installed
- **Bash** shell

## Capabilities

| Capability | Description |
|-----------|-------------|
| **One-Command Setup** | `./setup.sh` symlinks everything into place |
| **Skill Syncing** | Symlink skills from Git repo into `~/.claude/skills/` and `~/.codex/skills/` |
| **Shared MCP Config** | `.mcp.json` symlinked for consistent MCP server access |
| **Codex Exclusion List** | `codex-exclude` file filters skills not relevant to Codex |
| **Cross-Machine Sync** | Git push/pull to keep agent configs identical across machines |
| **Auto-Sync on Session Start** | Codex skills auto-synced via `sync-codex-skills.sh` on every session |

## Installation

```bash
git clone https://github.com/petekp/claude-code-setup.git
cd claude-code-setup
./setup.sh
```

## How It Works

The setup script creates this symlink structure:

```
~/.claude/
├── skills/         → <repo>/skills/
├── scripts/        → <repo>/scripts/
├── settings.json   → <repo>/settings.json
├── statusline-command.sh → <repo>/ (copied)

~/.mcp.json         → <repo>/.mcp.json

~/.codex/skills/
├── skill-a/        → <repo>/skills/skill-a/  (symlinked individually)
├── skill-b/        → <repo>/skills/skill-b/
└── ...             (only skills not in codex-exclude)
```

Edit files in either location — they're the same files. Commit and push to sync across machines.

## Codex Skill Syncing

Codex doesn't support directory-level symlinks, so skills are symlinked individually:

```bash
# Runs automatically on every Claude Code session start
scripts/sync-codex-skills.sh
```

Skills listed in `codex-exclude` are skipped — use this for skills that only make sense in Claude Code.

## Configuration Files

### settings.json

```json
{
  "model": "claude-sonnet-4-20250514",
  "maxTokens": 4096,
  "temperature": 0.7,
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read(*)",
      "Write(*)",
      "Edit(*)"
    ]
  }
}
```

### .mcp.json

Shared MCP server configuration — add CorpusIQ MCP endpoint here:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": ["-y", "@corpusiq/mcp-server"],
      "env": {
        "CORPUSIQ_API_KEY": "${CORPUSIQ_API_KEY}"
      }
    }
  }
}
```

## CorpusIQ Use Cases

1. **Multi-Machine Agent Consistency:** CorpusIQ runs agents on both DGX Spark (Linux) and Mac Mini (macOS). A shared Git-backed config ensures both machines use identical skills, MCP servers, and settings.

2. **Team Onboarding:** New team members clone the config repo, run `./setup.sh`, and instantly have the full CorpusIQ agent toolkit — no manual skill installation needed.

3. **Skill Versioning:** Skills change rapidly. Git tracking means you can roll back to a known-good skill version if an update breaks something.

4. **Selective Codex Deployment:** Not all Claude Code skills work in Codex. The `codex-exclude` list prevents broken skills from being loaded.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Symlinks broken after OS update | macOS SIP restrictions | Re-run `./setup.sh` |
| Codex skills not updating | `sync-codex-skills.sh` not running | Check `~/.claude/settings.json` for `statusline-command` |
| Git conflicts on `settings.json` | Multiple machines editing same file | Use machine-specific settings branches or `.gitignore` patterns |
| "Permission denied" on setup | Script not executable | `chmod +x setup.sh` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
