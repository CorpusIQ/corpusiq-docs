---
title: "Self-Improving Agent — Universal Agent Self-Evolution Framework Setup"
description: "32.2K+ installs. Multi-memory architecture (semantic + episodic + working) with hooks-based self-correction for AI agents that learn from every interaction. Setup guide for Hermes agents."
---

# Self-Improving Agent — Setup Guide

**Source:** [charon-fan/agent-playbook](https://skills.sh/charon-fan/agent-playbook/self-improving-agent) (32,200+ installs)
**Category:** Agent Infrastructure / Self-Evolution
**Quality Tier:** 🟢 Production

A universal self-improvement system that learns from ALL skill experiences — not just PRDs or specific task types. Uses multi-memory architecture (semantic + episodic + working) with hooks-based self-correction to continuously evolve the agent's codebase and capabilities. Based on 2025 lifelong learning research including SimpleMem, Multi-Memory architecture surveys, and Evo-Memory benchmarks.

---

## Installation

```bash
npx skills add charon-fan/agent-playbook --skill self-improving-agent
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ for hooks support |
| **File System Access** | Read/Write for memory storage and skill updates |
| **Agent Runtime** | Claude Code, Hermes Agent, or any hook-compatible agent |

---

## Key Capabilities

### Multi-Memory Architecture
- **Semantic Memory** (`memory/semantic-patterns.json`): Stores abstract patterns and rules reusable across contexts
- **Episodic Memory** (`memory/episodic/`): Stores specific experiences and outcomes from each interaction
- **Working Memory** (`memory/working/`): Holds current session context for error recovery

### Self-Improvement Loop
After any skill completes, automatically extracts experiences, abstracts patterns, and proposes skill updates with evolution markers. Supports confidence tracking and promotion policies to prevent over-generalization.

### Hooks Integration
Auto-triggers on skill events:
- `before_start`: Session logging
- `after_complete`: Pattern extraction, skill updates, PR creation (ask-first)
- `on_error`: Error capture and self-correction proposals

### Evolution Priority Matrix
Pre-configured priority matrix for triggering evolution across skills: PRD patterns → architecting → API design → debugging → code review → security → performance. Tracks confidence scores and application counts.

---

## Quick Start

```bash
# Install
npx skills add charon-fan/agent-playbook --skill self-improving-agent

# Initialize memory structure
mkdir -p memory/{semantic,episodic,working}

# The agent now learns from every interaction automatically via hooks
```

### Hook Configuration (Claude Code)

Add to Claude Code settings:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "bash ${SKILLS_DIR}/self-improving-agent/hooks/post-bash.sh"
        }]
      }
    ],
    "Stop": [
      {
        "hooks": [{
          "type": "command",
          "command": "bash ${SKILLS_DIR}/self-improving-agent/hooks/session-end.sh"
        }]
      }
    ]
  }
}
```

### Manual Trigger

```bash
# Trigger self-improvement manually
agent-playbook self-improve
```

---

## Verification

```bash
# Check memory structure exists
ls memory/semantic/ memory/episodic/ memory/working/

# Review extracted patterns
cat memory/semantic-patterns.json | jq '.patterns | length'

# Check recent episodes
ls -la memory/episodic/ | tail -5
```

---

## Notes

- Promotes findings with clear evidence thresholds — does NOT silently mutate skill files without approval
- Separates *capture* (always-on) from *promotion* (validated only) — prevents pollution of production skill guidance
- Based on published 2025 research: SimpleMem (efficient lifelong memory), Multi-Memory LLM Agent Survey (ACM), and Evo-Memory (DeepMind benchmark)
- Confidence tracking ensures single experiences don't trigger premature pattern generalization
- Ideal for agents that run diverse skill sets and need continuous improvement without manual tuning

---
