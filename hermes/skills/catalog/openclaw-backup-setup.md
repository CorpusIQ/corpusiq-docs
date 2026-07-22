---
title: OpenClaw Backup — Encrypted Agent Workspace Backup for Hermes
description: Automated AES-256-CBC encrypted backup and restore for Hermes/OpenClaw agent workspace files. Upload to soul-upload.com with auto-generated passwords per backup.
---

# OpenClaw Backup — Setup Guide

**Source:** [theagentservice/skills](https://skills.sh/theagentservice/skills/openclaw-backup) (3,100+ installs)
**Category:** Agent Infrastructure / Backup
**Quality Tier:** 🔵 Community

Automated encrypted backup and restore for agent workspace files (SOUL.md, MEMORY.md, IDENTITY.md, AGENTS.md, TOOLS.md). Uses tar + openssl (AES-256-CBC) encryption and soul-upload.com API. Auto-generates a new random password for each backup — no password reuse.

---

## Installation

```bash
npx skills add theagentservice/skills --skill openclaw-backup
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3.7+** | Script runtime |
| **requests** | `pip install requests` |
| **tar** | File archiving (system built-in) |
| **openssl** | AES-256-CBC encryption (system built-in) |
| **curl** | HTTP requests (system built-in) |

---

## Key Capabilities

### Core Functions

| Capability | Description |
|---|---|
| **Upload Backup** | Encrypt and upload workspace files to soul-upload.com with auto-generated password |
| **Download Backup** | Download and decrypt backups from soul-upload.com using stored password |
| **Delete Backup** | Delete backups from remote storage |

### Default Backup Files

If unspecified, these OpenClaw/Hermes workspace files are backed up by default:

- `SOUL.md` — Agent core identity and goals
- `MEMORY.md` — Agent memory and context
- `IDENTITY.md` — Agent identity definition
- `AGENTS.md` — Agent configuration
- `TOOLS.md` — Tool registrations

### Security Model

All backups use **AES-256-CBC encryption** via openssl. Each backup receives a unique auto-generated random password — never reuse passwords across backups. The password is stored in a recovery file locally; without it, backups are irrecoverable.

---

## Quick Start

```bash
# Upload a backup (default workspace files)
python backup.py upload

# Upload specific files
python backup.py upload --files SOUL.md MEMORY.md IDENTITY.md

# Download a backup by ID
python backup.py download <backup-id>

# List available backups
python backup.py list

# Delete a remote backup
python backup.py delete <backup-id>
```

---

## Hermes Integration

For Hermes agents, integrate into the session-end ritual:

1. Before shutdown, back up all workspace files
2. Store the recovery password in `~/.hermes/profiles/corpusiq/backup-recovery.json`
3. On new session start, verify backup integrity
4. Schedule weekly full backups via cron

### Cron Example

```bash
# Weekly encrypted backup (Sunday 2 AM)
0 2 * * 0 cd ~/corpusiq-brain && python backup.py upload --files SOUL.md CONSTITUTION.md SYSTEM_REGISTRY.md
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| `openssl: command not found` | `sudo apt install openssl` (Linux) or `brew install openssl` (macOS) |
| Upload fails (auth) | Verify soul-upload.com API key in environment |
| Decrypt fails | Ensure you have the correct recovery password — each backup uses a unique password |
| Missing Python dependencies | `pip install requests` |

---

## See Also

- Hermes Backup Recovery Setup — General Hermes backup strategy
- Hermes Full Backup Setup — Full system backup guide
- [soul-upload.com](https://soul-upload.com) — Backup storage service
