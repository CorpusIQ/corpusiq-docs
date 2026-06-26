---
title: Letta Code — 24-Skill Stateful Agent Harness Setup Guide
description: Install and configure Letta Code's 24-skill agent harness for Hermes — persistent memory, MCP-to-skills conversion, self-improving agents, multi-agent orchestration. Built on MemGPT research.
---

# Letta Code — Setup Guide

**Source:** [letta-ai/letta-code](https://skills.sh/letta-ai/letta-code) · [GitHub](https://github.com/letta-ai/letta-code)
**Category:** Agent Infrastructure / Memory Systems
**npm:** `@letta-ai/letta-code` · **Built on:** [MemGPT](https://arxiv.org/abs/2310.08560) research

Letta Code is a stateful agent harness where agents have persistent memory, identity, and learn over time. Unlike stateless agents that reset every session, Letta agents rewrite their own memory, skills, prompts, and even the harness itself. The 24 skills span memory management, multi-agent orchestration, MCP conversion, and self-improvement.

---

## Skill Catalog

### Memory & Identity (6 skills)

| Skill | Description |
|---|---|
| **initializing-memory** | Set up agent memory blocks, identity traits, and personality configuration |
| **syncing-memory-filesystem** | Git-backed memory persistence (MemFS) — sync agent memory across machines |
| **migrating-memory** | Migrate agent memory between runtimes, formats, and versions |
| **defragmenting-memory** | Optimize and compact agent memory over time — reduce context bloat |
| **searching-messages** | Full-text search across all agent conversations and memory blocks |
| **Context Doctor** | Audit and repair agent context quality — detect contradictions, staleness |

### Skills & MCP Integration (3 skills)

| Skill | Description |
|---|---|
| **acquiring-skills** | Discover and install skills from Hermes, ClawHub, GitHub, and registries |
| **creating-skills** | Author new skills programmatically — the agent writes its own capabilities |
| **converting-mcps-to-skills** | Convert MCP servers into portable, runtime-agnostic agent skills |

### Multi-Agent Orchestration (3 skills)

| Skill | Description |
|---|---|
| **dispatching-coding-agents** | Spawn and manage coding sub-agents for parallel development work |
| **working-in-parallel** | Dispatch and coordinate multiple agents working simultaneously |
| **messaging-agents** | Inter-agent messaging, channel management, and communication protocols |

### Migration & Compatibility (2 skills)

| Skill | Description |
|---|---|
| **migrating from codex and claude code** | Migrate agents, workflows, and memory from Codex and Claude Code |
| **finding-agents** | Search and discover existing agents across workspaces and machines |

### Scheduling & Automation (1 skill)

| Skill | Description |
|---|---|
| **scheduling-tasks** | Configure cron jobs, heartbeats, and scheduled agent work with self-management |

### Configuration & Customization (5 skills)

| Skill | Description |
|---|---|
| **adding-models** | Add and configure new LLM model backends with handle validation |
| **customizing-commands** | Add custom slash commands to extend the agent harness CLI |
| **customizing-statusline** | Customize the terminal status line display for agent sessions |
| **creating-extensions** | Build harness extensions and plugins for custom behavior |
| **modifying-the-harness** | Modify the agent harness itself — agents rewrite their own runtime |

### Channels, Hooks & Security (4 skills)

| Skill | Description |
|---|---|
| *(channels)* | Configure messaging channels: Telegram, Slack, Discord, custom |
| *(hooks)* | Run custom scripts at key agent execution points |
| *(permissions)* | Set permission modes and customize auto-approval/denial |
| *(secrets)* | Manage secrets as env vars with obfuscation from agent context |

---

## Installation

### Full Harness (Recommended)

```bash
# Install the Letta Code CLI
npm install -g @letta-ai/letta-code

# Launch with a new agent
letta --new-agent --personality tutorial

# Connect your LLM provider
letta /connect    # Follow prompts for API keys
```

### Skills-Only (For Hermes Integration)

```bash
# Install Letta skills via skills.sh
npx skills add letta-ai/letta-code

# Install specific skills
npx skills add letta-ai/letta-code --skill acquiring-skills
npx skills add letta-ai/letta-code --skill converting-mcps-to-skills
npx skills add letta-ai/letta-code --skill defragmenting-memory
```

### Direct Skill Import

```bash
# Clone and copy skills into Hermes profile
git clone https://github.com/letta-ai/letta-code.git /tmp/letta-code
mkdir -p ~/.hermes/profiles/corpusiq/skills/letta/
cp -r /tmp/letta-code/.skills/* ~/.hermes/profiles/corpusiq/skills/letta/
```

---

## Key Workflows for Hermes

### MCP-to-Skills Conversion

Letta's `converting-mcps-to-skills` is directly applicable to Hermes:

```bash
# Convert an MCP server to a portable skill
letta skills install https://github.com/letta-ai/letta-code
# Then invoke: "convert this MCP server to a skills.sh-compatible SKILL.md"
```

### Memory Defragmentation

Hermes agents accumulate context over long sessions. Letta's memory management patterns are instructive:

```bash
# Run context doctor to audit memory quality
letta /doctor

# Defragment and compact memory
# (Hermes equivalent: session DB optimization skill)
```

### Cross-Runtime Skill Acquisition

The `acquiring-skills` skill creates a two-way bridge:

```bash
# Letta installs skills from Hermes ecosystem
letta skills install https://github.com/nousresearch/hermes-agent

# Hermes loads Letta skills (via skills.sh)
npx skills add letta-ai/letta-code
```

### Self-Improving Agent Loops

Letta agents can modify their own harness:

```bash
# Agent rewrites its own skills
letta "Create a new skill for validating JSON schemas"

# Agent modifies its system prompt
letta "Update your memory to prioritize response latency over verbosity"
```

---

## Architecture Comparison: Letta vs Hermes

| Feature | Letta Code | Hermes Agent |
|---------|------------|--------------|
| Memory system | MemFS (git-backed blocks) | Honcho (SQLite + vector) |
| Skills | Global + project + agent scoped | Profile-scoped + marketplace |
| Self-improvement | Agents rewrite own memory/skills/prompts | Skills + memory compaction |
| Multi-agent | Sub-agents (async/sync) | delegate_task + subagent-resilience |
| Channels | Telegram, Slack, Discord, custom | Telegram (native) |
| Scheduling | Crons + heartbeats + sleep-time compute | Cron jobs |
| MCP support | Conversion pipeline (MCP → skills) | Native MCP client |

---

## Provider Configuration

```bash
# During /connect or via environment
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_AI_API_KEY=...

# Or use OpenRouter for multi-provider access
letta /model openrouter/anthropic/claude-sonnet-4-20250514
```

---

## Verification

```bash
# Confirm installation
which letta
letta --version

# Test with tutorial agent
letta --new-agent --personality tutorial --message "Hello, who are you?"

# List installed skills
letta skills list
npx skills list | grep letta

# Run context doctor
letta /doctor
```

---

## Why This Matters

Letta Code represents the cutting edge of stateful agent architecture. For Hermes specifically:

- **Memory patterns** — MemFS (git-backed memory) and defragmentation are patterns Hermes can adopt
- **MCP bridge** — The MCP-to-skills conversion pipeline creates ecosystem interoperability
- **Self-improvement** — Agents that rewrite their own code open new automation frontiers
- **Skill ecosystem** — `acquiring-skills` installs from Hermes, creating a bidirectional marketplace

---

*[Letta Code on skills.sh →](https://skills.sh/letta-ai/letta-code) · [GitHub →](https://github.com/letta-ai/letta-code) · [Documentation →](https://docs.letta.com) · [Discord →](https://discord.gg/letta)*
