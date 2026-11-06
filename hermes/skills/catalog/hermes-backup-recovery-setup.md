---
title: "Hermes Backup Recovery Setup Guide"
description: "Back up, verify, restore, and health-check your Hermes Agent deployment state with age encryption. Repo: JimmyHuang2002/hermes-backup-recovery."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-backup-recovery-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes Backup Recovery Setup Guide

**Repo:** [JimmyHuang2002/hermes-backup-recovery](https://github.com/JimmyHuang2002/hermes-backup-recovery)
**Stars:** ⭐0 | **License:** MIT | **Language:** Shell

## Overview

An Agent Skill for backing up, verifying, restoring, and health-checking a Hermes Agent deployment's state. Uses age encryption for secure backups. Hardware-agnostic - works on Raspberry Pi, cloud VMs, and desktop.

## Installation

```bash
npx skills add JimmyHuang2002/hermes-backup-recovery -g -y
```

## Usage

```bash
hermes-backup create   # Create encrypted backup
hermes-backup verify   # Verify backup integrity
hermes-backup restore  # Restore from backup
hermes-backup health   # Health check
```

## Pitfalls

- Brand new (0 stars, July 21) - minimal testing
- Requires age CLI for encryption

## Native Alternative

Hermes Agent ships its own backup paths, so you do not need a skill for the basic case. `hermes backup --quick` writes a restorable state snapshot, `hermes backup` writes a full zip archive, and `hermes import` restores that archive. See [Hermes Backup and Restore](/hermes/setup/backup-and-restore) for the commands, what each one captures, and how to verify an archive before trusting it. Use this skill when you specifically want age-encrypted backups or its health-check step.
