---
title: OpenClaw Backup — Setup Guide for Hermes Agents
description: Encrypted backup and restore for OpenClaw workspace files using AES-256-CBC. Auto-generated passwords, tar archives, and soul-upload.com API integration. 3.1K+ installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openclaw-backup-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# OpenClaw Backup — Setup Guide

**Source:** [theagentservice/skills](https://github.com/theagentservice/skills) (Community)
**Skill:** `openclaw-backup` · **Installs:** 3.1K+ · **Category:** Backup / DevOps
**Platform:** Linux, macOS

OpenClaw Backup provides encrypted backup and restore for OpenClaw Agent workspace files — SOUL.md, MEMORY.md, IDENTITY.md, AGENTS.md, TOOLS.md. Uses tar for archiving, openssl for AES-256-CBC encryption, and the soul-upload.com API for remote storage. Each backup gets a unique auto-generated password.

## Installation

```bash
npx skills add theagentservice/skills@openclaw-backup
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Python 3.7+ | Script runtime |
| `requests` library | `pip install requests` |
| `tar` | File archiving |
| `openssl` | AES-256-CBC encryption |
| OpenClaw workspace | SOUL.md, MEMORY.md, IDENTITY.md, AGENTS.md, TOOLS.md |

## Core Functions

### 1. Upload Backup

Encrypt and upload workspace files with auto-generated password:

- Archives workspace files into a tar
- Encrypts with `openssl enc -aes-256-cbc`
- Uploads to soul-upload.com
- Stores the unique password in a recovery file
- **Never reuse passwords** — each backup gets a new one

### 2. Download Backup

Download and decrypt backups using stored password:

- Fetches encrypted archive from soul-upload.com
- Decrypts with the password from the recovery file
- Extracts to the target workspace directory

### 3. Delete Backup

Remove backups from remote storage:

- Deletes specified backup by ID
- Cleans up local recovery file entry

## Security Model

| Property | Implementation |
|----------|---------------|
| Encryption | AES-256-CBC via openssl |
| Key Generation | Auto-generated random password per backup |
| Key Storage | Local recovery file (protect this!) |
| Transport | HTTPS to soul-upload.com API |
| Password Reuse | Prohibited — unique password per backup |

## Recovery File

The recovery file maps backup IDs to their encryption passwords. **Protect this file** — it's the only way to decrypt backups:

```bash
# Example recovery file entry
backup_20260728_120000: aB3xK9mQ7rW2vY5n
```

## Workflow

```bash
# 1. Upload a backup
# The skill archives, encrypts, and uploads workspace files
# Saves password to recovery file

# 2. List backups
# Queries soul-upload.com for available backups

# 3. Restore a backup
# Downloads, decrypts, and extracts to workspace
npx skills run openclaw-backup --restore <backup-id>

# 4. Delete old backup
npx skills run openclaw-backup --delete <backup-id>
```

## Verification

After setup:
- Verify `openssl version` returns a valid version
- Verify `pip show requests` confirms the library is installed
- Test upload with a small workspace
- Confirm the recovery file is created and contains the password
- Test restore to a temp directory

## Related Skills

- [Clawd Strike Setup](/hermes/skills/catalog/clawdstrike-setup/)
- [OpenClaw Ecosystem (June 26)](/hermes/skills/catalog/openclaw-ecosystem-june26-setup/)
