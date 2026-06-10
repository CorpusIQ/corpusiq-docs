---
title: Session Handoff — Anti-Amnesia Pattern
description: How autonomous agents recover context after restart — session handoff, auto-recovery, and persistent state across sessions
---

# Session Handoff — Anti-Amnesia Pattern

The fundamental problem with autonomous agents: they lose everything on restart. Every session starts from zero. The operator has to re-explain active tasks, blocked items, decisions made. This breaks the promise of autonomy.

The anti-amnesia pattern fixes this. It's a two-part system: **save before shutdown, recover on startup**.

## The Problem

LLM agents are stateless. Each session is a fresh context window. Even with persistent memory tools, the agent doesn't know *what to look for* unless it's told. You restart Hermes, say "hi", and get:

> "Hello! How can I help you today?"

Instead of:

> "Welcome back. HN and TikTok are rate-limited from testing. LinkedIn fires its first cron at 5am tomorrow. We were mid-way through the platform connectivity sprint."

The first response wastes time. The second lets you pick up where you left off.

## The Pattern

### Save Before Shutdown

When a session ends (user says "bye", milestone reached, or before restart), the agent writes a structured handoff:

```
TASK_HISTORY.md gets appended with:
  - Active tasks and their status
  - Blocked items with reasons
  - Decisions made this session
  - Platform state (what's working, what's not)
```

This isn't a diary. It's a machine-readable checkpoint. Just the facts needed to resume.

### Recover on Startup

The session-start skill includes automatic context recovery. Before doing anything else:

1. Read `TASK_HISTORY.md` (last 50 lines)
2. Query `session_search()` for recent sessions
3. Query GBrain for pages tagged `active-task`
4. Reconstruct and present: "Here's what we were doing..."

The agent doesn't wait to be asked. Recovery is automatic.

## Architecture

```
Session End
    ↓
corpusiq-session-handoff skill
    ├── Writes structured state to TASK_HISTORY.md
    ├── Saves handoff page to GBrain (tagged: active-task)
    └── Updates active task tags

[Restart — agent has no context]

Session Start
    ↓
corpusiq-session-start skill (Step 6: Context Recovery)
    ├── Reads TASK_HISTORY.md
    ├── Queries session_search for last sessions
    ├── Queries GBrain for active-task tagged pages
    ├── Reconstructs state
    └── Reports: "Resuming X, Y blocked, Z pending"
```

## What Gets Saved

Not everything. Only what survives a restart:

| Saved | Not Saved |
|-------|-----------|
| Active task names + status | Individual tool call results |
| Blocked items + reasons | Intermediate debugging state |
| Platform connection states | File paths (re-discoverable) |
| Decisions made this session | Conversation history (in session_search) |
| Cron job states | Transient errors |

## Implementation

Two skills power this:

**`corpusiq-session-handoff`** — Runs at session end. Writes structured state. Tags GBrain pages. Appends to TASK_HISTORY.md.

**`corpusiq-session-start`** — Runs at session start. Step 6 recovers context from TASK_HISTORY.md, session_search, and GBrain before any other action.

## Why This Works

Most "memory" solutions try to preserve everything. They fail because:
- Context windows fill up
- Embeddings drift
- Relevance decays

The anti-amnesia pattern preserves *decision state*, not *data*. It answers one question: "What were we doing and where did we leave off?"

The rest is re-discoverable.

---

*Built with CorpusIQ — autonomous agents that remember what they're doing*
