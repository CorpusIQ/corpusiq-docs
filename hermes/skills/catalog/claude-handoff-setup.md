---
title: Claude Handoff — Session Handoff Pattern for Hermes Agents
description: Hand the current conversation off to a fresh background agent that picks up work immediately. 63.5K+ installs. Essential pattern for long-running multi-session agent workflows.
---

# Claude Handoff — Setup Guide

**Source:** [mattpocock/skills](https://skills.sh/mattpocock/skills/claude-handoff) (63,500+ installs)
**Category:** Agent Infrastructure / Session Management
**Quality Tier:** 🟢 Production

The session handoff pattern: summarize the current conversation state so a fresh background agent can continue the work immediately. Spawns a background agent seeded with the handoff summary as its prompt. Essential for long-running agent workflows that span multiple sessions or context windows.

---

## Installation

```bash
npx skills add mattpocock/skills --skill claude-handoff
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Claude Code / Hermes** | Any version supporting background agents |
| **Session awareness** | Agent must understand its current task state |

---

## Key Capabilities

### The Handoff Pattern

1. **Summarize** — Write a concise handoff summary of the current conversation state
2. **Launch** — Spawn a background agent seeded with the summary as its prompt
3. **Name** — Always pass `--name` with a descriptive identifier
4. **Continue** — The fresh agent picks up where the previous one left off

### What to Include in a Handoff

- Current task goal and progress
- Decisions made and rationale
- Files created/modified with paths
- Active blockers and unresolved issues
- Suggested skills for the next agent to invoke
- References to existing artifacts (PRDs, plans, ADRs, issues)

### What NOT to Include

- Content already captured in other artifacts (reference by path/URL instead)
- Sensitive information (API keys, passwords, PII)
- Operational telemetry or verbose logs

---

## Quick Start

```bash
# Basic handoff
claude --bg --name "Continue market research" \
  "You are continuing market research for CorpusIQ. 
   Progress: analyzed 3 of 5 competitors. 
   Remaining: competitor D and E. 
   Files: ~/corpusiq-brain/research/competitor-analysis.md 
   Suggested skills: corpusiq-research-intelligence-framework"

# List active background agents
claude agents

# Check agent status
claude agents --status
```

---

## Hermes Integration

For CorpusIQ Hermes agents, the handoff pattern maps to our session-handoff ritual:

### Session Handoff Protocol

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Session N      │ ──► │  Handoff Summary  │ ──► │   Session N+1    │
│  (Active Work)   │     │  (GBrain/Honcho)  │     │  (Continues)     │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

### Handoff Template for CorpusIQ

```markdown
# Session Handoff — YYYY-MM-DD

## Task
[One-line goal]

## Progress
- [Completed items with results]
- [In-progress items with current state]

## Decisions
- [Decision 1]: [rationale]
- [Decision 2]: [rationale]

## Files
- `path/to/file` — [what it contains, state]

## Blockers
- [Blocker 1]: [mitigation attempted]

## Next Steps
1. [Immediate next action]
2. [Secondary action]

## Suggested Skills
- [skill-name-1]
- [skill-name-2]

## See Also
- [[related-page-1]]
- [[related-page-2]]
```

---

## Tips

- Handoffs should be self-contained — the new agent has no context from your session
- Reference files by absolute path so the new agent can access them immediately
- Include "suggested skills" so the next agent loads the right capabilities
- Redact API keys, passwords, and PII before writing the handoff summary
- Keep handoffs focused on one task domain — split unrelated work into separate handoffs

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Background agent starts wrong directory | Pass full paths in the handoff summary |
| Agent loads wrong skills | Be explicit in "Suggested Skills" section |
| Handoff too long | Reference existing files instead of duplicating content |
| Lost agent state | Check `claude agents` for active background processes |

---

## See Also

- [[corpusiq-session-handoff]] — CorpusIQ session handoff to Honcho + GBrain
- [[hermes-session-maintenance-setup]] — Hermes session state management
- [[claude-api-setup]] — Claude API integration for Hermes
