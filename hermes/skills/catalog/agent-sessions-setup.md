---
title: "agent-sessions — macOS Agent Session Browser Setup"
description: "Install and configure agent-sessions (683⭐) — a local-first macOS app for browsing, searching, and resuming AI coding-agent session histories across Hermes Agent, Claude Code, Codex, and Cursor."
skill_name: agent-sessions
category: session-management
difficulty: Easy
platforms: [macOS]
---

# agent-sessions — Full Setup Guide

**Repo:** [jazzyalex/agent-sessions](https://github.com/jazzyalex/agent-sessions) | ⭐ 683
**Author:** jazzyalex | **Language:** Swift | **License:** MIT
**Platform:** macOS (native SwiftUI)

agent-sessions is a local-first macOS app that lets you browse, search, analyze, and resume AI coding-agent session histories across Hermes Agent, Claude Code, Codex, and Cursor. All session data stays on your machine — no cloud sync, no telemetry.

---

## Prerequisites

- macOS 14 (Sonoma) or later
- At least one supported agent runtime installed (Hermes Agent, Claude Code, Codex, or Cursor)
- Xcode 16+ (only if building from source)

---

## Installation

### Option A: Download from GitHub Releases (Recommended)

1. Go to the [Releases page](https://github.com/jazzyalex/agent-sessions/releases)
2. Download the latest `.dmg` file
3. Open the DMG and drag `agent-sessions.app` to your Applications folder
4. On first launch, right-click → Open to bypass Gatekeeper (the app is not notarized yet)

### Option B: Build from Source

```bash
git clone https://github.com/jazzyalex/agent-sessions.git
cd agent-sessions
open agent-sessions.xcodeproj
# In Xcode: Product → Archive → Distribute App → Copy App
```

---

## Configuration

### 1. First Launch

On first launch, agent-sessions scans standard agent session directories:

| Agent | Default Session Path |
|-------|---------------------|
| Hermes Agent | `~/.hermes/profiles/*/state.db` |
| Claude Code | `~/.claude/sessions/` |
| Codex | `~/.codex/sessions/` |
| Cursor | `~/Library/Application Support/Cursor/User/workspaceStorage/` |

### 2. Custom Session Paths

If your sessions are stored in non-standard locations:

1. Open agent-sessions → **Settings** (⌘,)
2. Click the **Sessions** tab
3. Click **+** to add a custom path
4. Browse to your session directory
5. agent-sessions auto-detects the format

### 3. Supported Formats

agent-sessions auto-detects these session formats:
- **Hermes Agent:** SQLite state databases (`.db`)
- **Claude Code:** JSON session files
- **Codex:** Session directories with metadata
- **Cursor:** VS Code workspace storage

---

## Usage

### Browsing Sessions

The main window shows all sessions across all agents, sorted by last activity:

1. **Left sidebar:** Agents and session groups
2. **Center panel:** Session list with preview snippets
3. **Right panel:** Full session transcript (read-only)

### Searching Sessions

Press **⌘F** to search across all sessions:

- **Full-text search:** Searches all messages in all sessions
- **Agent filter:** Click agent icons to filter by runtime
- **Date range:** Use the calendar picker to narrow by date
- **Bookmark:** Click ★ to bookmark important sessions

### Resuming Sessions

To resume a session in its original agent:

1. Select the session in the list
2. Click **Resume** (or press **⌘R**)
3. agent-sessions opens the agent with the session context restored

**Note:** Resume behavior varies by agent:
- **Hermes Agent:** Opens a new terminal with `hermes --resume <session-id>`
- **Claude Code:** Opens Claude Code with the session file
- **Codex:** Opens Codex with `--session` flag
- **Cursor:** Opens the workspace

### Analyzing Sessions

Click the **Analytics** tab (⌘2) for session insights:

- **Token usage trends:** Per-agent, per-session, per-day
- **Tool call frequency:** Which tools are used most
- **Session duration:** How long sessions typically run
- **Model usage:** Which models are called most often

---

## Integration with Hermes Agent

### Hermes Session Path

agent-sessions auto-discovers Hermes sessions at:

```bash
~/.hermes/profiles/<profile-name>/state.db
```

If you use multiple Hermes profiles (e.g., `corpusiq`, `default`), agent-sessions lists all of them.

### Hermes Session Format

Hermes stores sessions as rows in a SQLite database. agent-sessions reads:
- `sessions` table: session metadata, timestamps
- `messages` table: individual message content, role, tool calls
- `tools` table: tool execution logs

### Known Limitation

Hermes sessions stored in `~/.hermes/profiles/` may be locked by a running Hermes gateway. If agent-sessions shows "Database locked," close the Hermes gateway first or use a read-only copy.

---

## Troubleshooting

### "No sessions found"

**Cause:** agent-sessions couldn't find any agent session directories.

**Fix:**
1. Open Settings → Sessions
2. Verify session paths are correct
3. Click **Rescan** to force a re-scan
4. Check that sessions exist: `ls ~/.hermes/profiles/*/state.db`

### "Unsupported format"

**Cause:** The session format is not recognized.

**Fix:** Check the repo issues for format support requests. Currently supported: Hermes SQLite, Claude Code JSON, Codex metadata directories, Cursor workspace storage.

### "Database locked" (Hermes)

**Cause:** Hermes gateway has an active write lock on the state database.

**Fix:**
```bash
# Stop the Hermes gateway
hermes gateway stop

# Open agent-sessions (it reads the DB in read-only mode)
# Restart gateway when done
hermes gateway start
```

---

## Security Notes

- **All data stays local.** agent-sessions reads session files directly — nothing is uploaded.
- **No network access.** The app does not phone home or send telemetry.
- **Read-only by default.** agent-sessions never modifies session data unless you explicitly save a bookmark.
- **Build from source** if you want to audit the code before running.

---

## Alternatives

| Tool | Platform | Stars | Notes |
|------|----------|:-----:|-------|
| agent-sessions | macOS | 683 | This guide |
| Hermes WebUI | Web | 15K | Full agent control panel |
| Hermex | iOS | 450 | Native iPhone app |
| OpenClaw Session Viewer | CLI | — | Built into OpenClaw |

---

*Guide last updated: July 4, 2026 | [Repo](https://github.com/jazzyalex/agent-sessions) | [Report issue](https://github.com/CorpusIQ/corpusiq-docs/issues)*
