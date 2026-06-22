---
title: Hermes OpenSpec — Plugin Setup Guide
description: OpenSpec integration plugin for Hermes Agent. Adds agent tools wrapping the openspec CLI plus a dashboard tab for browsing change proposals, specs, and branch diffs. Kanban board for spec-driven development.
category: skills
subcategory: setup
skill_name: hermes-openspec
author: FelineStateMachine
last_updated: 2026-06-21
hermes_version: any (plugin system)
---

# Hermes OpenSpec — Setup Guide

**Plugin:** [FelineStateMachine/hermes-openspec](https://github.com/FelineStateMachine/hermes-openspec)
**What it does:** Bridges Hermes Agent with OpenSpec — the spec-driven development standard that keeps spec files living in the repo alongside code. Adds 6 agent tools + a `/openspec` dashboard tab with kanban board and spec browser.

> OpenSpec keeps specs in the repo. Hermes OpenSpec lets your agent read, validate, and track them — and gives you a dashboard to browse everything.

---

## Quick Install

```bash
# Install the plugin
hermes plugins install FelineStateMachine/hermes-openspec

# Enable it (prompts during install, or run explicitly)
hermes plugins enable openspec
```

Restart Hermes. The OpenSpec tab appears at `/openspec`.

### Optional: Install OpenSpec CLI

Five of the six agent tools require the `openspec` CLI binary. The dashboard and `openspec_context` tool work without it.

```bash
npm install -g @fission-ai/openspec@latest
```

If installed to a non-standard location:

```bash
export OPENSPEC_BIN=/home/user/.npm-global/bin/openspec
```

## Prerequisites

| Requirement | Minimum | Notes |
|-------------|---------|-------|
| Hermes Agent | Plugin support | `hermes plugins install` must work |
| OpenSpec CLI | Latest | Optional — needed for 5 of 6 tools. Install via npm. |
| Git | any | For branch diffs and commit-date sorting |
| OpenSpec repos | n/a | Must have `openspec/` directory in the repo |

## What You Get

### Agent Tools (6 total)

| Tool | Requires CLI? | What It Does |
|------|:---:|--------------|
| `openspec_context` | No | Resolve an `os_*` identifier into repo path + change/spec content. **Entry point — call this first.** |
| `openspec_list` | Yes | List changes or specs in a project (sorted by recent or name) |
| `openspec_show` | Yes | Show a change or spec as JSON: proposals, tasks, designs, deltas, requirements |
| `openspec_validate` | Yes | Validate OpenSpec changes or specs |
| `openspec_status` | Yes | Show artifact completion status for a change (feeds into kanban) |
| `openspec_instructions` | Yes | Enriched instructions for creating artifacts or applying tasks |

### Dashboard Tab (`/openspec`)

| Feature | What You See |
|---------|-------------|
| **Change Board** | Kanban-style: ideas → draft → todo → in_progress → done → archived. Click any change to read proposal, tasks, design, and spec deltas. |
| **Spec Browser** | Current specs in the worktree, sorted alphabetically or by last git commit date. Compare against HEAD (dirty mode) or arbitrary git refs. |
| **Deep-linking** | URL hash like `#project-name/token` for direct navigation. |
| **Repo Registration** | Add repos by path from the UI. Each gets a vanity name and stable `name/os_*` tokens. |

## Verification

After installation, confirm everything works:

```bash
# Confirm plugin is installed and enabled
hermes plugins list --plain

# Check that openspec binary is found (if installed)
openspec --version

# Query dashboard API
curl http://127.0.0.1:9119/api/plugins/openspec/sources
```

Register a repo to test:
- UI: OpenSpec tab → **Add source**
- Agent: `openspec_context(identifier="/path/to/your/repo")`

The repo must have an `openspec/` directory with OpenSpec-compliant files.

## Usage Patterns

### Basic: Browse specs from the dashboard

Navigate to `/openspec` in Hermes Web UI. Register repos with OpenSpec directories. Browse the kanban board to see what's in progress, what's in draft, what's completed.

### Intermediate: Ask Hermes about specs

```
"What's the status of the auth refactor change?"
"List all open change proposals in the api project."
"Show me the spec deltas for the rate-limiting change."
```

Hermes will use `openspec_list`, `openspec_show`, and `openspec_status` tools to answer.

### Advanced: Spec-driven development workflow

1. Create change proposal: `openspec_instructions` tool
2. Validate before sharing: `openspec_validate` tool
3. Track progress: kanban board auto-updates from artifact status
4. Review before merge: compare spec against HEAD

## File Structure

```
hermes-openspec/
├── plugin.yaml              # Tool plugin manifest — declares 6 agent tools
├── __init__.py              # Plugin registration — wires tools, sets check_fn gating
├── schemas.py               # Tool parameter schemas (JSON Schema)
├── tools.py                 # Tool handlers — wraps openspec CLI binary
├── registry.py              # SQLite registry (sources at <hermes_home>/openspec.db)
├── dashboard/
│   ├── manifest.json        # Dashboard tab manifest
│   ├── plugin_api.py        # FastAPI routes for the tab
│   └── ...                  # Frontend assets
└── screenshots/
    ├── board.png            # Change board preview
    └── specs.png            # Spec browser preview
```

## Updating

```bash
hermes plugins update openspec
```

> **Important:** If backend API routes changed (`plugin_api.py`), restart Hermes to remount them. The dashboard rescan (`/api/dashboard/plugins/rescan`) reloads frontend assets but does NOT remount backend routes.

## Error Recovery

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Plugin not in tab list | Not enabled | `hermes plugins enable openspec` + restart |
| `openspec_show` returns error | CLI missing | `npm install -g @fission-ai/openspec@latest` |
| `openspec_context` fails | No repo registered | Register repo via UI or agent tool |
| Dashboard blank | Plugin routes not mounted | Restart Hermes |
| Binary not found | Non-standard PATH | `export OPENSPEC_BIN=/path/to/openspec` |

## When NOT to Use

- You don't use OpenSpec for spec-driven development
- Your team prefers a different spec format (RFC, ADR, Notion)
- You only need `openspec_context` (installing the CLI is unnecessary for that one tool)

## Why This Matters

OpenSpec keeps spec files (`openspec/changes/`, `openspec/specs/`, `openspec/ideas/`) inside the repo alongside code. But without Hermes integration, there's no way to browse specs from the dashboard, and the agent has no native tools to resolve OpenSpec identifiers or run CLI commands.

This plugin bridges both gaps — giving your agent the ability to read, validate, and track specs programmatically, and giving you a visual dashboard to see everything at a glance.

---

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — community-curated agent skills. Discover more at [skills.sh](https://skills.sh).*
