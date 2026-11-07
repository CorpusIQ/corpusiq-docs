---
title: "Hermes Backup and Restore - Native Commands and Snapshots"
description: Use hermes backup for a full zip archive or a quick state snapshot, then restore with hermes import or /snapshot restore. What is included and excluded.
category: setup
tags: [hermes-agent, backup, restore, snapshot, disaster-recovery, state, cron]
last_updated: 2026-11-07
canonical: "https://www.corpusiq.io/docs/hermes/setup/backup-and-restore/"
robots: "index,follow"

---

# Hermes Backup and Restore - Native Commands and Snapshots

Hermes Agent ships two backup paths and two matching restore paths, with no extra tooling required. Use them before an upgrade, before editing configuration that could break a running agent, and on a schedule if the machine holds work you cannot rebuild.

This page documents the built-in commands, what each one actually captures, what it deliberately leaves out, and how to restore. If you would rather use a community script with its own retention logic, see the [full backup script guide](/hermes/skills/catalog/hermes-full-backup-setup) or the [backup and recovery skill](/hermes/skills/catalog/hermes-backup-recovery-setup) instead.

## Overview

| What you want | Command | Output | Restore with |
|---|---|---|---|
| Fast snapshot of critical state | `hermes backup --quick` | A state snapshot directory | `/snapshot restore <id>` in a CLI session |
| Complete portable archive | `hermes backup` | A `.zip` file | `hermes import <zipfile>` |

Both commands operate on the active Hermes home directory, which defaults to `~/.hermes` and is overridden by `HERMES_HOME`. Both take a cross-process lock, so you cannot corrupt a backup by running one while the gateway is up.

## How It Works

| Component | Quick snapshot | Full backup |
|---|---|---|
| **Storage** | `state-snapshots/<timestamp>-<label>/` inside the Hermes home | One `.zip` at the path you choose |
| **Typical size** | Megabytes - state and config only | Depends on sessions and media; can be gigabytes |
| **Skills and sessions** | Not included | Included |
| **SQLite databases** | Included (key state files only) | Included (every database) |
| **Portable to another machine** | Not by itself - it is a local recovery point | Yes - that is the point of the zip |
| **Retention** | 20 most recent snapshots | `--keep N`, default 3 archives |

Two details matter more than the table:

1. **Live SQLite databases are copied with `sqlite3.backup()`, not by reading the file.** That produces a consistent database image while the gateway is writing to it. The `-wal`, `-shm` and `-journal` sidecars are therefore excluded on purpose: pairing a fresh snapshot with a stale sidecar is what produces a torn restore on the next open.
2. **The codebase is never archived.** `hermes-agent`, nested `.git` directories, `node_modules`, virtualenvs, Python bytecode and tool caches are all skipped, because they are reinstallable. A backup is your data, not your program.

## Quick State Snapshot

`hermes backup --quick` does not write a zip. It writes a state snapshot, which is the same mechanism the updater uses as its pre-update safety net.

```bash
# Snapshot with a label you will recognise later
hermes backup --quick --label before-upgrade
```

Real output from a run:

```text
State snapshot created: 20261106-194536-before-upgrade
  2 snapshot(s) stored in ~/.hermes/profiles/<profile>/state-snapshots/
  Restore with: /snapshot restore 20261106-194536-before-upgrade
```

Restoring a snapshot happens inside a Hermes CLI session, not from the shell. There is no `hermes snapshot` subcommand:

```text
/snapshot list
/snapshot restore 20261106-194536-before-upgrade
```

### What a quick snapshot captures

Files, config, and the databases that hold state you cannot regenerate:

- `state.db`, plus the per-profile stores `projects.db`, `response_store.db`, `memory_store.db`, `verification_evidence.db`
- `config.yaml`, `.env`, `auth.json`
- `cron/jobs.json` and `cron/executions.db`
- `gateway_state.json`, `channel_directory.json`, `channel_aliases.json`, `processes.json`
- `kanban.db` and `kanban/boards` (non-default boards; workspace attachments are skipped as regenerable)
- Pairing stores, including platform-specific pairing JSON files

Skills, sessions, and delivered media are not part of a quick snapshot. If you need those, take a full backup.

## Full Backup

`hermes backup` writes one zip containing your configuration, skills, sessions, memory, cron definitions, and data.

```bash
# Default output: ~/hermes-backup-<timestamp>.zip
hermes backup

# Explicit path
hermes backup --output /mnt/backups/hermes-$(date +%F).zip

# Keep the newest 7 archives in the output directory instead of the default 3
hermes backup --output /mnt/backups --keep 7

# Keep everything, never prune
hermes backup --output /mnt/backups --keep 0
```

`--keep` only prunes files matching the `hermes-backup-*.zip` naming pattern in the output directory. It will not touch archives you named yourself, so a custom filename outside that pattern is never deleted.

### What a full backup excludes

| Excluded | Why |
|---|---|
| `hermes-agent` and nested `.git` | Re-clone instead |
| `node_modules`, venvs, `site-packages` | Reinstall instead |
| `__pycache__`, `*.pyc`, `*.pyo` | Regenerated on import |
| `.cache` and tool caches | Regenerable |
| `browser-profiles`, `browser-profile` | Chromium holds these locked while running, and they contain your live cookies and saved logins |
| Prior `backups/` and `state-snapshots/` | Otherwise each backup nests the last one |
| `checkpoints/` | Session trajectory caches |
| Model and runtime downloads | Regenerable |
| `*.db-wal`, `*.db-shm`, `*.db-journal` | Replaced by the consistent database snapshot |
| `.backup.lock`, `gateway.pid`, `cron.pid` | Meaningless on another machine |

Everything under `cache/` is also skipped except the subdirectories that hold delivered media and generated artifacts: `images`, `audio`, `videos`, `documents`, `screenshots`, `citations`, and generated files. Those are things the agent produced for you and nothing can rebuild them.

## Restore From a Full Backup

```bash
# Extract into the Hermes home, prompting before overwriting
hermes import ~/hermes-backup-2026-11-06.zip

# Overwrite existing files without prompting
hermes import ~/hermes-backup-2026-11-06.zip --force
```

`hermes import` writes into the active Hermes home. Restoring onto a different machine is the intended use: install Hermes, stop the gateway, import the archive, then start the gateway again. Your skills, cron jobs, and configuration come back with the data.

## Verify a Backup Before You Trust It

A backup you have never opened is a guess. Two cheap checks:

```bash
# 1. The archive is readable and has the file count you expect
unzip -l ~/hermes-backup-2026-11-06.zip | tail -3

# 2. The state database inside it is a real SQLite file
unzip -p ~/hermes-backup-2026-11-06.zip state.db > /tmp/state.check.db
sqlite3 /tmp/state.check.db "PRAGMA integrity_check;"
```

`PRAGMA integrity_check` should print `ok`. If it prints anything else, take a new backup and investigate before relying on the old one.

## Scheduled Backups

A daily snapshot and a weekly archive is a reasonable default. Snapshot first, because it is cheap:

```bash
# Quick snapshot at 02:15 every day
15 2 * * * /usr/local/bin/hermes backup --quick --label nightly

# Full archive every Sunday at 03:15, keep the newest 4
15 3 * * 0 /usr/local/bin/hermes backup --output /mnt/backups --keep 4
```

Cron runs with a minimal environment. If your Hermes install is not on the cron `PATH`, use the absolute path to the binary, and export `HERMES_HOME` in the crontab if you run more than one profile.

For off-machine durability, point `--output` at a mounted remote volume and let a separate tool handle versioning. The zip is a plain file, so any object storage or backup program can carry it.

## Security Warning

A full backup contains `.env` and `auth.json`. That means API keys, OAuth tokens, and every credential your agent uses.

- Treat the archive as secret material, at the same level as the credentials themselves
- Never commit it to a repository, attach it to a ticket, or upload it to a shared drive
- Encrypt it before it leaves the machine if the destination is not under your control
- Rotate any key that was inside an archive you lost control of

## Troubleshooting

### "No such file or directory" on restore

`hermes import` expects the path to the zip, and it writes relative to the active Hermes home. If you set `HERMES_HOME` in a different shell than the one you are restoring in, you are restoring into the wrong home. Check `echo $HERMES_HOME` first.

### The snapshot is listed but restoring it changes nothing

The gateway keeps state in memory. Stop the gateway, restore, then start it again, so nothing writes the old state back over the restored files.

### A backup hangs

A full backup takes a lock and snapshots every database. If another backup or an update is holding the slot, the second run waits. If a database is locked by a running browser session, the full backup skips the excluded profile directories but can still wait on an in-use database. Stop the process that holds it, or use `--quick` for the fast path.

### The archive is much smaller than expected

Check whether your sessions and media live outside the Hermes home. A backup covers the home directory only. Anything you have symlinked elsewhere, such as a model directory or an external vault, is not in the archive and needs its own backup plan.

## FAQ

### Is `hermes backup --quick` a zip file?

No. It creates a state snapshot directory and prints a `/snapshot restore` command. Use `hermes backup` without `--quick` when you need a single portable archive.

### Can I restore a quick snapshot on another machine?

Not with `hermes import`, which reads zip archives. Copy the snapshot directory and the rest of the Hermes home, or take a full backup instead.

### Does the backup stop the agent?

No. Both commands take a cross-process lock and copy databases with `sqlite3.backup()`, which is safe while the gateway is writing. A restore is different: stop the gateway first.

### Are my browser cookies in the backup?

No. Live browser profile directories are excluded, because they contain a credential store and cannot be copied while Chromium holds them open.

### How many backups does Hermes keep?

Twenty quick snapshots by default. For full archives, `--keep` defaults to 3 and only prunes files matching `hermes-backup-*.zip`; `--keep 0` disables pruning.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup) - All platform options
- [Docker Setup](docker.md) - Persisting the data directory in a container
- [Cloud VPS Setup](cloud-vps.md) - Running the agent on always-on infrastructure
- [Session Cleanup](session-cleanup.md) - Keeping the state database small
- [Full Backup Script Guide](/hermes/skills/catalog/hermes-full-backup-setup) - Third-party script with its own retention logic
- [Backup and Recovery Skill](/hermes/skills/catalog/hermes-backup-recovery-setup) - Skill-based recovery workflow

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*