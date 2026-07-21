---
title: "Hermes Backup Recovery — Encrypted Backup Skill for Hermes Agent"
description: "Back up, verify, restore, and health-check your Hermes Agent deployment state with age encryption."
---

# Hermes Backup Recovery Setup Guide

**Repo:** [JimmyHuang2002/hermes-backup-recovery](https://github.com/JimmyHuang2002/hermes-backup-recovery)
**Stars:** ⭐0 | **License:** MIT | **Language:** Shell

## Overview

An Agent Skill for backing up, verifying, restoring, and health-checking a Hermes Agent deployment's state. Uses age encryption for secure backups. Hardware-agnostic — works on Raspberry Pi, cloud VMs, and desktop.

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

- Brand new (0 stars, July 21) — minimal testing
- Requires age CLI for encryption
