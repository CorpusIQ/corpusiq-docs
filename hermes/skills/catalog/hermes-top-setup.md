---
title: "hermes-top — Setup Guide"
description: "Install and run hermes-top, a live htop/btop-style terminal dashboard for Hermes Agent that reads state.db directly."
skill_name: hermes-top
category: Monitoring
source_repo: markmnl/hermes-top
stars: 1
language: Go
platforms: [Linux, macOS, Windows]
---

# hermes-top — Full Setup Guide

A read-only, `htop`/`btop`-style live terminal dashboard for [Hermes Agent](https://github.com/NousResearch/hermes-agent). Reads Hermes's SQLite `state.db` directly — **never writes, cannot interfere with a running Hermes.**

---

## Prerequisites

- **Go 1.26+** (build only — binary is self-contained)
- **Hermes Agent v0.18 or newer** — must have run at least once so `state.db` exists
- Terminal with 256-color support (most modern terminals)

The SQLite driver is [`modernc.org/sqlite`](https://modernc.org/sqlite) — a pure Go implementation. **No CGO, no system libsqlite3.** Single static binary, cross-compiles trivially.

---

## Install

### Build from source

```bash
git clone https://github.com/markmnl/hermes-top.git
cd hermes-top
go build -o hermes-top ./cmd/hermes-top
```

### Run without installing

```bash
go run ./cmd/hermes-top
```

### Move to PATH (optional)

```bash
sudo mv hermes-top /usr/local/bin/
# or
mv hermes-top ~/.local/bin/
```

---

## Usage

### Basic usage

```bash
./hermes-top
```

Launches the TUI. Reads `state.db` from the default location (see Database Location below).

### Flags

| Flag | Default | Meaning |
|------|---------|---------|
| `--db PATH` | (auto) | Path to Hermes `state.db`. Supports `~` expansion. |
| `--interval DUR` | `400ms` | Refresh interval, clamped to `250ms`–`500ms`. |
| `--dump` | off | Print one text snapshot of the database and exit (no TUI). Scriptable. |

### Examples

```bash
# Custom database path
hermes-top --db /path/to/custom/state.db

# One-shot snapshot for scripting
hermes-top --dump > hermes-status-$(date +%Y%m%d-%H%M).txt

# Faster refresh
hermes-top --interval 250ms

# Remote Hermes instance (via SSH)
ssh user@server 'HERMES_HOME=/opt/hermes hermes-top --dump'
```

---

## Database Location

`hermes-top` resolves the database path in this order:

1. `--db PATH` if given (supports `~`).
2. `$HERMES_HOME/state.db` if `HERMES_HOME` is set.
3. `~/.hermes/state.db` (the platform default).

If the file does not exist, it prints the resolved path and a hint, then exits non-zero.

---

## TUI Layout

Three panes, side by side:

```
┌──────────────┬──────────────────┬──────────────────┐
│   SESSIONS   │     ACTIONS      │     EVENTS       │
│              │                  │                  │
│  session-1   │  tool_call       │  model_switch    │
│  session-2   │  read_file       │  token_usage     │
│  session-3   │  terminal        │  error           │
│  ...         │  ...             │  ...             │
└──────────────┴──────────────────┴──────────────────┘
```

| Pane | Shows |
|------|-------|
| **Sessions** | Active/recent Hermes sessions with model, profile, and status |
| **Actions** | Tool calls, skill loads, subagent spawns — with timing and status |
| **Events** | Model switches, token usage, errors, lifecycle events |

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `↑` / `k`, `↓` / `j` | Move cursor in focused pane |
| `Tab` | Cycle focus: sessions → actions → events |
| `Enter` / `→` | Expand highlighted entry to full pretty-printed JSON |
| `←` | Collapse highlighted entry |
| `/` | Filter events (type to filter live; `Enter` applies, `Esc` clears) |
| `g` | Jump to top of focused pane |
| `G` | Jump to bottom of focused pane (re-enables auto-follow) |
| `r` | Force immediate refresh |
| `q` / `Ctrl-C` | Quit |

### Auto-follow behavior

Actions and events panes auto-follow new rows while the cursor is on the newest entry (like `tail -f`). Move the cursor up and the position freezes as new rows arrive. Press `G` to re-pin to the newest entry.

---

## JSON Display

Tool arguments and results are JSON. By default each entry is rendered as a single readable line — `key=value` with escapes decoded (so `&` shows as `&`, not `&amp;`) and subtle syntax coloring.

**Expand:** Highlight an entry and press `Enter` to expand it inline into full, indented, syntax-highlighted JSON.

**Collapse:** Press `←` to collapse back to single-line view.

Non-JSON payloads (e.g., assistant prose) expand to the full wrapped text.

---

## Cross-Compilation

Because `hermes-top` uses a pure-Go SQLite driver with zero CGO, cross-compilation is trivial:

```bash
# Linux → macOS (ARM)
GOOS=darwin GOARCH=arm64 go build -o hermes-top-darwin-arm64 ./cmd/hermes-top

# Linux → Windows
GOOS=windows GOARCH=amd64 go build -o hermes-top.exe ./cmd/hermes-top

# macOS → Linux
GOOS=linux GOARCH=amd64 go build -o hermes-top-linux-amd64 ./cmd/hermes-top
```

---

## Troubleshooting

### "state.db not found"

```bash
# Check if Hermes has run at least once
ls -la ~/.hermes/state.db

# If HERMES_HOME is set
ls -la $HERMES_HOME/state.db

# Explicit path
hermes-top --db /explicit/path/to/state.db
```

### "Go version too old"

Requires Go 1.26+. Check your version:

```bash
go version
# Should show: go version go1.26.x ...
```

### Terminal colors not rendering

`hermes-top` uses 256-color terminal escape codes. Ensure your terminal supports them:

```bash
echo $TERM
# Should show: xterm-256color, screen-256color, tmux-256color, etc.
```

### Running against a remote Hermes

`hermes-top` reads `state.db` directly — it cannot connect to a remote Hermes over the network. To monitor a remote instance:

```bash
# Option 1: SSH + local read
ssh remote-host 'hermes-top --db /path/to/state.db'

# Option 2: Sync state.db locally (read-only copy)
rsync -avz remote-host:~/.hermes/state.db /tmp/remote-state.db
hermes-top --db /tmp/remote-state.db
```

---

## Related Tools

- [hermes-hud](https://github.com/Lucasdjs22/hermes-hud) — Alternative terminal HUD for agent memory, skills, and behavior
- [hermes-flight-recorder](https://github.com/zwright8/hermes-flight-recorder) — Trace-based scorecards and static eval reports
- [hermes-doctor](https://github.com/503496348-ops/hermes-doctor) — Self-diagnosis and self-healing plugin

---

*Powered by CorpusIQ*
