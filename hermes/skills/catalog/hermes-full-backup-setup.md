---
title: "Hermes Full Backup — Setup Guide"
description: "Install and use the Hermes Complete Backup script for disaster recovery. Self-contained Python script, zero dependencies."
skill_name: hermes-full-backup
category: DevOps/DR
source_repo: edouardleroy/hermes-full-backup
stars: 1
language: Python
platforms: [Linux, macOS, Windows]
---

# Hermes Full Backup — Full Setup Guide

A self-contained Python backup script for Hermes Agent disaster recovery. Creates a `.zip` with everything needed to restore Hermes from scratch on a clean OS.

**Stdlib only** — `zipfile` + `argparse` + `pathlib`. Works on any Python 3 installation.

---

## What Gets Backed Up

### Full backup (default)

| Component | Files |
|-----------|-------|
| **Config** | `config.yaml`, `.env`, `state.db`, `auth.json` |
| **Skills** | All installed skills with their references, scripts, and assets |
| **Cron jobs** | All scheduled cron task definitions |
| **Memories** | Durable memory store |
| **Profiles** | All agent profiles (CorpusIQ, etc.) |
| **Source code** | Hermes Agent source (if available) |
| **Binaries** | `uv.exe` and other tool binaries |
| **Installer** | `install.bat` for Windows restore |
| **Recovery instructions** | Auto-generated `LEEME.txt` with restore steps |

### Quick backup (`--quick`)

Config + skills only — no source code, binaries, or installer. Useful for frequent lightweight snapshots.

---

## Install

```bash
git clone https://github.com/edouardleroy/hermes-full-backup.git
cd hermes-full-backup
```

The script is self-contained — no `pip install` needed. Just run it:

```bash
python hermes-complete-backup.py --help
```

---

## Usage

### Quick backup (recommended for daily use)

```bash
python hermes-complete-backup.py --quick -o ~/hermes-backup-$(date +%Y%m%d).zip
```

Backs up config + skills. Fast (~seconds), small file.

### Full backup

```bash
python hermes-complete-backup.py -o ~/hermes-full-$(date +%Y%m%d).zip
```

Backs up everything: config, skills, sessions, source code, binaries, installer. Takes longer (~30-60 seconds), larger file.

### With external config

```bash
python hermes-complete-backup.py --json-config custom-paths.json
```

`custom-paths.json` example:

```json
{
  "hermes_home": "/opt/hermes",
  "backup_dir": "/mnt/backups/hermes",
  "exclude": ["sessions/archive", "logs"]
}
```

### Scheduled daily backup (cron)

Add to your Hermes crontab or system crontab:

```bash
# Daily quick backup at 2 AM
0 2 * * * cd ~/hermes-full-backup && python hermes-complete-backup.py --quick -o ~/backups/hermes-$(date +\%Y\%m\%d).zip

# Weekly full backup on Sunday at 3 AM
0 3 * * 0 cd ~/hermes-full-backup && python hermes-complete-backup.py -o ~/backups/hermes-full-$(date +\%Y\%m\%d).zip
```

---

## Restore Procedure

### From a full backup

```bash
# 1. Extract the backup
unzip hermes-full-20260704.zip -d /tmp/hermes-restore

# 2. Review recovery instructions
cat /tmp/hermes-restore/LEEME.txt

# 3. Restore Hermes Home
cp -r /tmp/hermes-restore/hermes_home/* ~/.hermes/

# 4. Reinstall Hermes Agent (if source code was included)
cd /tmp/hermes-restore/source
# Follow the Hermes install instructions for your platform

# 5. Verify
hermes --version
hermes skills list
hermes cron list
```

### From a quick backup (config + skills only)

```bash
unzip hermes-backup-20260704.zip -d /tmp/hermes-restore
cp /tmp/hermes-restore/config.yaml ~/.hermes/
cp /tmp/hermes-restore/.env ~/.hermes/
cp -r /tmp/hermes-restore/skills/* ~/.hermes/skills/
# Reinstall Hermes Agent separately
```

---

## ⚠️ Security Warning

The backup ZIP contains sensitive files:

- `.env` — API keys and tokens
- `auth.json` — OAuth tokens and credentials
- `state.db` — Session history with potentially sensitive tool output

**Treat backup ZIPs like secrets.** Store them encrypted, restrict access, and never commit them to version control.

The auto-generated `LEEME.txt` inside every backup includes a credential warning:

```
⚠️ ADVERTENCIA DE SEGURIDAD
Este archivo ZIP contiene tus credenciales de Hermes (.env, auth.json).
Guárdalo en un lugar seguro. No lo compartas ni lo subas a repositorios públicos.
```

---

## Script Architecture

### Key design decisions

| Decision | Reason |
|----------|--------|
| Single file, stdlib only | Runs on any Python 3 — no venv, no pip, no deps |
| `$HERMES_HOME` as source of truth | Works on Windows, Linux, macOS without path changes |
| `--json-config` for overrides | Customize without editing the script |
| Credential warning in LEEME.txt | User must know the ZIP contains secrets |
| `--quick` mode | Frequent backups without the weight of source code |

### File structure inside the ZIP

```
hermes-full-20260704.zip
├── LEEME.txt                     ← Recovery instructions + security warning
├── hermes_home/
│   ├── config.yaml
│   ├── .env
│   ├── state.db
│   ├── auth.json
│   ├── skills/
│   ├── cron/
│   ├── memories/
│   └── profiles/
├── source/                       ← (full backup only) Hermes Agent source
├── binaries/                     ← (full backup only) uv.exe, etc.
└── install.bat                   ← (full backup only) Windows installer
```

---

## Troubleshooting

### "$HERMES_HOME not set"

The script uses `$HERMES_HOME` to locate your Hermes installation. If not set, it defaults to `~/.hermes`.

```bash
# Set it explicitly
export HERMES_HOME=~/.hermes
python hermes-complete-backup.py --quick

# Or use --json-config to specify the path
python hermes-complete-backup.py --json-config <(echo '{"hermes_home": "/custom/path"}')
```

### "Permission denied" on .env or auth.json

The backup reads these files. Ensure they're readable by your user:

```bash
chmod 600 ~/.hermes/.env ~/.hermes/auth.json
```

### Large backup files

Full backups include source code and binaries — they can be 100MB+. Use `--quick` for daily backups and reserve full backups for weekly/monthly.

### Windows paths

On Windows, use forward slashes or escaped backslashes:

```bash
python hermes-complete-backup.py -o C:/Users/you/backups/hermes.zip
# or
python hermes-complete-backup.py -o C:\\Users\\you\\backups\\hermes.zip
```

---

## Related Tools

- [Hermes Agent Install Guide](https://hermes-agent.nousresearch.com/docs) — Official install docs
- [Hermes Backup Script (alternative)](https://github.com/edouardleroy/hermes-full-backup) — This script's repo with tests and docs

---

*Powered by CorpusIQ*
