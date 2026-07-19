---
title: "Cursor Delegate — Hermes Agent Skill for Cursor CLI Delegation"
description: "Install and configure the cursor-delegate skill (matdev83/hermes-cursor-dispatcher) for Hermes Agent — safely delegate coding work to Cursor CLI with isolated Git worktrees, structured result capture, and Hermes-owns-acceptance workflow."
---

# Cursor Delegate Setup Guide

**Repo:** [matdev83/hermes-cursor-dispatcher](https://github.com/matdev83/hermes-cursor-dispatcher)
**Version:** v1.1.0
**Stars:** 1
**License:** MIT
**Created:** July 19, 2026
**Install:** `npx skills add matdev83/hermes-cursor-dispatcher --skill cursor-delegate -g -y`

## What It Is

A skill for Hermes Agent that safely delegates repository-level coding, debugging, refactoring, or implementation work to Cursor CLI (`agent`). The skill:

- Transfers exact UTF-8 prompts through a Python wrapper (no shell interpretation)
- Prefers isolated Git worktrees for implementation
- Captures structured results with bounded log tails
- Requires Hermes to independently inspect diffs, run tests, and accept/reject
- Integrates natively with Grok models (default: `grok-4.5-xhigh`)

**Key design rule:** Cursor is an external implementation executor — **never** a source of truth. Hermes owns task construction, workspace selection, safe invocation, diff review, independent tests, corrective iterations, and the final acceptance decision.

## Prerequisites

- **Cursor CLI** installed and in `$PATH` (`agent --version` must work)
- Git 2.30+
- Python 3.10+ (for the wrapper script)
- Hermes Agent with `terminal` toolset access

Verify Cursor CLI:
```bash
agent --help
agent --version
```

## Installation

```bash
npx skills add matdev83/hermes-cursor-dispatcher --skill cursor-delegate -g -y
```

This places the skill at `$HERMES_HOME/skills/cursor-delegate/`.

Verify:
```bash
ls $HERMES_HOME/skills/cursor-delegate/
# Should show: SKILL.md  scripts/  templates/
```

## How It Works

### Wrapper Script

The bundled wrapper is `$HERMES_HOME/skills/cursor-delegate/scripts/cursor_delegate.py`. It:

1. Reads an exact UTF-8 prompt from a file
2. Sends it to Cursor CLI through stdin (no shell interpretation)
3. Uses `shell=False`, explicit `cwd`, a narrowly allowlisted environment
4. Runs with a timeout in an isolated process group
5. Captures bounded log tails (mode-0600 prefixes)

### Why Not Shell Interpolation?

Never invoke Cursor by interpolating arbitrary prompt text into a shell command. The wrapper avoids:
- Per-argument size limits on Linux
- Shell metacharacter injection
- `eval`, `shell=True`, or `echo` as prompt transport
- Environment variable prompt smuggling

### Cursor CLI Contract

The wrapper assumes Cursor CLI supports:
- Executable: `agent`
- Headless mode: `--print`
- Output formats: `text`, `json`, `stream-json`
- Read-only modes: `--mode plan`, `--mode ask`
- Edit mode: default (no `--mode edit` flag needed)
- Workspace selection: `--workspace <path>`
- Headless trust: `--trust`
- Model selection: `--model <id>`
- Prompt input through stdin

Default model: `grok-4.5-xhigh` (verified against installed CLI).

The wrapper accepts `--mode edit` but deliberately omits it from Cursor's argv for edit mode. It does not pass `--force`, `--yolo`, `--approve-mcps`, `--add-dir`, or arbitrary headers.

## Mandatory Workflow

### Step 1: Inspect Before Delegating

Hermes must first inspect:
- Repository structure and applicable instruction files
- Relevant modules, interfaces, and implementation constraints
- Current tests and repository-specific validation commands
- Current branch, `git status --short`, repository root, and `HEAD`

### Step 2: Workspace Selection

Choose the appropriate workspace:
- **Detached worktree** (preferred): Isolates Cursor's changes from the main working tree
- **Current working directory**: Only if the repo is clean and the change is trivial

```bash
# Preferred: isolated worktree
git worktree add --detach /tmp/cursor-work-$(date +%s) HEAD
```

### Step 3: Write Prompt to File

Write the exact prompt to a temporary file (never inline in shell):

```python
prompt = """Task: Refactor the database connection pool in src/db/pool.py
Context: Current implementation has a race condition under high concurrency.
Requirements:
1. Use connection-per-thread pattern
2. Add timeout on acquisition
3. Maintain backward compatibility with existing callers
4. Run existing tests: pytest tests/db/ -x
"""
write_file("/tmp/cursor_prompt.txt", prompt)
```

### Step 4: Invoke the Wrapper

```bash
python3 $HERMES_HOME/skills/cursor-delegate/scripts/cursor_delegate.py \
  --workspace /tmp/cursor-work-20260719 \
  --prompt-file /tmp/cursor_prompt.txt \
  --timeout 600 \
  --model grok-4.5-xhigh
```

The wrapper returns structured JSON:
```json
{
  "exit_code": 0,
  "stdout_tail": "...",
  "stderr_tail": "...",
  "timeout": false,
  "log_file": "/tmp/cursor_delegate_20260719_120000.log"
}
```

### Step 5: Diff Review

Hermes MUST independently inspect the diff:
```bash
cd /tmp/cursor-work-20260719
git diff
git diff --stat
```

Do NOT accept Cursor's report without inspecting actual changes.

### Step 6: Independent Tests

```bash
cd /tmp/cursor-work-20260719
pytest tests/db/ -x -v
```

### Step 7: Accept or Reject

- **Accept**: Apply the diff to the main branch, commit with attribution
- **Reject**: Discard the worktree, document why, possibly retry with adjusted prompt

## Safety Boundaries

The wrapper enforces:

| Boundary | Mechanism |
|----------|-----------|
| **No shell injection** | Prompt from file, `shell=False` |
| **Output bounds** | 50KB stdout, 50KB stderr hard caps |
| **Process isolation** | Separate process group, kill on timeout |
| **No secret leakage** | Prompt file is mode 0600, deleted after run |
| **No privilege escalation** | Never passes `--trust` without explicit user approval |
| **Workspace isolation** | Detached worktree, never on dirty repo |

The wrapper **does NOT** pass:
- `--force` — no forced overwrites
- `--yolo` — no skip-confirmation
- `--approve-mcps` — no MCP auto-approval
- `--add-dir` — no directory injection
- Arbitrary headers — no HTTP header manipulation

## When to Use

**Use for:**
- Non-trivial implementation, debugging, migration, or refactoring
- Repository changes where a second coding executor adds value
- Tasks with large Markdown prompts, code blocks, or structured data
- Independent implementation attempts in isolated Git worktrees

**Do NOT use for:**
- One-line local edits Hermes can safely make directly
- Operations outside a clearly selected workspace
- Prompts containing secret values (API keys, tokens, passwords)
- Arbitrary MCP access or implicit privilege escalation
- Accepting Cursor's report without inspecting actual changes

## Error Recovery

### Cursor CLI not found
```bash
which agent || echo "Cursor CLI not installed. Install from cursor.com/cli"
```

### Timeout
The wrapper has a configurable timeout (default: 600s). If exceeded:
1. The Cursor process group is killed
2. Partial output is captured in the log file
3. The worktree may contain partial changes — discard and retry

### Model not available
```bash
agent --list-models
# Verify grok-4.5-xhigh or override with --model
```

### Worktree conflicts
```bash
# Clean up stale worktrees
git worktree list
git worktree remove /tmp/cursor-work-* --force
```

## Pitfalls

1. **Never trust Cursor's self-report** — Always inspect the actual diff. Cursor may claim success while producing broken code.

2. **Dirty repos** — The wrapper does NOT check for uncommitted changes. Hermes must verify `git status --short` before delegating.

3. **Model alias drift** — `grok-4.5-xhigh` may not appear in `agent --list-models` but was verified working. If it fails, check model availability with `agent --list-models` and override with `--model`.

4. **Large repos** — Worktree creation on large repos (1GB+) may take several seconds. Account for this in timeout calculations.

5. **Tests may not exist** — If the repo has no tests for the changed area, Hermes must manually verify correctness through code review.

## Verification Checklist

- [ ] `agent --version` returns a version number
- [ ] `agent --help` shows supported flags
- [ ] Skill directory exists: `ls $HERMES_HOME/skills/cursor-delegate/`
- [ ] Wrapper exists: `ls $HERMES_HOME/skills/cursor-delegate/scripts/cursor_delegate.py`
- [ ] `python3 $HERMES_HOME/skills/cursor-delegate/scripts/cursor_delegate.py --help` shows usage
- [ ] `git worktree --help` confirms git version supports worktrees

## See Also

- [Official Repo](https://github.com/matdev83/hermes-cursor-dispatcher)
- [Cursor CLI Documentation](https://docs.cursor.com/cli)
- [Hermes Agent Delegation Docs](https://hermes-agent.nousresearch.com/docs)

---

*Discovered July 19, 2026 · [Marketplace →](/hermes/skills/marketplace/new-july19-2026/)*
