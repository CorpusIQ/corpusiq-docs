---
title: "Delete Hermes Agent Sessions and Prune state.db"
description: "List, delete, archive and prune Hermes Agent sessions, then reclaim state.db disk space with optimize. Dry-run first, pin what you want to keep."
canonical: "https://www.corpusiq.io/docs/hermes/setup/session-cleanup/"
robots: "index,follow"
category: setup
tags: [hermes-agent, sessions, state-db, sqlite, maintenance, disk-space]
last_updated: 2026-11-01
---

# Delete Hermes Agent Sessions and Prune state.db

Every Hermes Agent conversation is a session stored in `state.db`, a SQLite database in your Hermes home. Sessions accumulate as you work, and the file grows with them. Hermes ships the commands to list sessions, delete one, prune a date range, archive instead of deleting, and reclaim the disk space afterwards. None of them require a plugin.

The short version:

```bash
hermes sessions list --limit 20                    # see what is there
hermes sessions delete <session-id>                # remove one session
hermes sessions prune --older-than 30 --dry-run    # preview a range
hermes sessions prune --older-than 30              # delete that range
hermes sessions optimize                           # reclaim the space
```

## What each command does

| Command | Effect | Changes data |
|---|---|---|
| `hermes sessions list` | Recent sessions with title, workspace, last active time and ID | No |
| `hermes sessions stats` | Session and message counts, plus current database size | No |
| `hermes sessions export` | Writes sessions out to JSONL, Markdown, QMD, HTML or a trace file | No |
| `hermes sessions delete <id>` | Deletes one session | Yes |
| `hermes sessions prune` | Deletes every session matching the filters you pass | Yes |
| `hermes sessions archive` | Soft-hides matching sessions and keeps the data | Yes |
| `hermes sessions pin <id>` | Marks sessions as keep, exempt from the stale sweep and from prune | Yes |
| `hermes sessions optimize` | Merges search-index segments and VACUUMs the database | Reclaims space |

## Delete a single session

List first, then delete by ID:

```bash
hermes sessions list --limit 20
hermes sessions delete local-9b97db23af8d03f7d4150d45a222a82956cdca462efc51a5ba5dc4e6ef222822
```

`delete` asks for confirmation unless you pass `--yes`. There is no undo, so export anything you may want later first.

## Prune a range of sessions

`prune` takes the same filters you would expect from a log rotation tool:

| Flag | Matches |
|---|---|
| `--older-than AGE` | Last active more than AGE ago. Bare numbers are days; `12h`, `2d` and `1w` also work |
| `--newer-than AGE` | Last active within the last AGE |
| `--before` / `--after` | An ISO timestamp boundary |
| `--source` | One source, for example `cli`, `telegram` or `discord` |
| `--title` | Sessions whose title contains a substring |
| `--min-messages` / `--max-messages` | Session size in messages |
| `--min-tokens` / `--max-tokens`, `--min-cost` / `--max-cost` | Spent budget per session |
| `--min-tool-calls` / `--max-tool-calls` | Tool call count |
| `--include-archived`, `--include-pinned` | Widen the match to archived or pinned sessions |

Two defaults are worth knowing before you run it. A bare `hermes sessions prune` with no filters assumes `--older-than 90`, and any filter you pass matches sessions of every age. That second rule is the one that surprises people, so use `--dry-run`:

```bash
hermes sessions prune --older-than 30 --dry-run
```

A dry run prints the cutoff and the match count without writing anything. When the count looks right, run the same command without `--dry-run` and add `--yes` to skip the prompt.

## Archive instead of delete

`hermes sessions archive` takes the same filters, does the same matching and writes nothing destructive. Archived sessions stay in the database and drop out of the default listing, which is what you want for sessions you may need to read again. They come back into scope with `--include-archived`.

Use `pin` for the opposite intent. A pinned session is exempt from the stale sweep and from prune:

```bash
hermes sessions pin <session-id>
hermes sessions pinned
```

## Reclaim the disk space

Deleting rows does not shrink a SQLite file. The pages stay allocated and are reused by later writes, so the file only gets smaller after a VACUUM. `hermes sessions optimize` merges the search-index segments and runs the VACUUM in one step. It changes no data.

Run it when nothing else is holding the database:

```bash
hermes gateway stop
hermes sessions optimize
hermes gateway start
```

The gateway, the desktop app, the dashboard and the cron dispatcher all keep `state.db` open. Optimize refuses to run while another Hermes process holds the file, and `--force` overrides that refusal. The command's own help states the risk plainly: rewriting the store under a live writer can leave every agent refusing turns until all writers are stopped. Stop the writers, then optimize.

Two related stores are separate from `state.db` and have their own commands:

- `hermes sessions optimize-storage` migrates the search index to the compact v23 layout, which reclaims space on large databases without touching session content.
- `hermes checkpoints status` reports the filesystem checkpoint store, the shadow git repo that snapshots working directories before file edits. `hermes checkpoints prune` deletes orphaned checkpoints and garbage-collects the store, and `hermes checkpoints clear` wipes the rollback history entirely.

## Safety checklist

1. Run `hermes sessions stats` to record the size you are starting from.
2. Run the delete or prune you intend with `--dry-run` and read the match count.
3. Export anything you might need: `hermes sessions export --format md sessions.md`.
4. Pin the sessions you want to survive a future sweep.
5. Delete or prune without `--dry-run`.
6. Optimize in a quiet window, with the gateway stopped.
7. Run `hermes sessions stats` again to confirm the file shrank.

## What deletion does and does not touch

Deleting a session removes that session and its messages from the session store. It does not touch your configuration, your skills, your cron jobs, your memory files, or the checkpoint store. Those live in separate paths under your Hermes home, and each has its own management command.

## FAQ

**Does deleting sessions reduce token cost?**
No. Tokens are model usage, not storage. Deleting sessions frees disk space only.

**Why does `state.db` stay the same size after I delete sessions?**
SQLite does not return freed pages to the filesystem until a VACUUM. Run `hermes sessions optimize`.

**Can I undo a delete?**
No. Deletion is permanent. Archive keeps the session and hides it instead, and an export gives you a file you can keep.

**Do archived sessions still count toward database size?**
Yes. Archiving hides a session from the default listing, it does not remove the data. Prune them when you no longer need them.

**Does prune delete my current session?**
Prune matches on last-active time, so a session you are actively using falls outside an `--older-than` window. Read the dry run before you confirm.

**Is it safe to run while the gateway is up?**
Listing, stats and export are read-only and safe at any time. Delete and prune are ordinary writes and safe while the gateway runs. Optimize is the one command that needs the writers stopped.

## Related Pages

- [Setup Overview](/hermes/setup) - All platform options
- [Docker Setup](docker.md) - Persistent data volume in a container
- [Mac Mini Standalone Setup](mac-mini-standalone.md) - Long-lived host where the database grows
- [Troubleshooting Guide](/hermes/troubleshooting) - Gateway and database errors

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
