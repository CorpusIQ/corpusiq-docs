---
title: Hermes Agent - Core Official Skill Setup Guide
description: Official Nous Research Hermes Agent skill. CLI invocation, subagent delegation, persistent memory, self-improving skills, MCP integration, browser automation. 400+ installs.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hermes-agent-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Hermes Agent - Core Skill Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/NousResearch/hermes-agent) (Official)
**Skill:** `hermes-agent` · **Installs:** 400+ · **Category:** Core / Agent Framework
**Platform:** Linux, macOS, Windows

The official Hermes Agent core skill from Nous Research. Bundles the essential capabilities every Hermes agent needs: CLI invocation patterns, subagent delegation (`delegate_task`), persistent memory (FTS5 + LLM summaries), self-improving skills that auto-create from completed tasks, MCP bidirectional integration, browser automation, code execution, and web research.

---

## Installation

```bash
# Install via skills.sh
npx skills add nousresearch/hermes-agent --skill hermes-agent -g -y

# Or clone the full repo
git clone https://github.com/NousResearch/hermes-agent.git
# Skill is at: hermes-agent/skills/hermes-agent/SKILL.md
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.20.0+ |
| **Shell Access** | `hermes` CLI must be in PATH |
| **API Keys** | At least one LLM provider configured in `config.yaml` |

---

## Core Capabilities

### 1. CLI Invocation

Run Hermes from any agent or script:

```bash
# One-shot task execution: -z prints only the final response text
hermes -z "Analyze this CSV file and generate a summary report"

# With a specific model for this run
hermes -z -m <provider/model> "Review this PR diff"

# With a skill preloaded (repeat the flag or comma-separate several)
hermes -z --skills corpusiq-execution-discipline "Audit system health"

# Interactive session instead of one-shot
hermes chat
```

### 2. Subagent Delegation

Isolate complex subtasks into independent contexts. Delegation is the `delegate_task` tool the agent calls inside a session, not a CLI subcommand, so you ask for it in the prompt:

```bash
# Delegate a research task and merge the result
hermes -z "Delegate a research task: compare the top 5 MCP server implementations on transports, auth and tool counts. Return a comparison table."

# Parallel delegation: name the workstreams and let the agent fan out
hermes -z "Delegate three parallel tasks, one each: X mentions of CorpusIQ, Reddit threads about MCP servers, and relevant HN front-page discussions. Merge the findings."
```

The number of concurrent children is configurable (`delegation.max_concurrent_children` in `config.yaml`).

Subagents get their own conversation, terminal session, and toolset. Results flow back as summaries - intermediate tool output never floods context.

### 3. Persistent Memory

Two-tier memory architecture:

- **FTS5 full-text search** - fast keyword/boolean retrieval across all past sessions
- **LLM summaries** - semantic compression of key facts, preferences, and patterns

```bash
# Browse past sessions and resume one
hermes sessions browse

# Session and message counts, plus current database size
hermes sessions stats

# Token, cost and tool usage across the last 30 days
hermes insights --days 30
```

Durable facts live in `MEMORY.md` and `USER.md` under the Hermes home, which the agent writes and compacts itself. `hermes memory` configures an external memory provider (`setup`, `status`, `off`, `reset`) rather than adding a fact from the shell.

### 4. Self-Improving Skills

Agents learn from completed tasks:

- After complex tasks (5+ tool calls), the agent proposes a new skill
- Skills encode the workflow, pitfalls, and verification steps
- Next time the task type appears, the agent loads the skill automatically
- Quality improves over time without manual curation

```bash
# List available skills
hermes skills list

# Browse registries and install a skill
hermes skills search "mcp"
hermes skills install <name>
```

New skills are authored by the agent itself mid-session with its skill tools, which is why the loop compounds without manual curation.

### 5. MCP Integration

Bidirectional Model Context Protocol:

- **Client**: Connect to external MCP servers (53+ tools registered)
- **Server**: Expose Hermes capabilities as MCP tools for other agents

```bash
# List connected MCP servers
hermes mcp list

# Test a connection
hermes mcp test <server-name>
```

### 6. Browser Automation

Built-in browser tools for web interaction:

- Navigate, snapshot, click, type, scroll, vision analysis
- Console inspection for JS errors
- Screenshot capture with AI annotation

---

## Common Patterns

### Pattern: Research → Synthesize → Report

```bash
# 1. Delegate research (the agent fans out to a subagent)
hermes -z "Delegate research on competitor pricing for AI data connectors and return a source-cited summary."

# 2. While research runs, prepare the report template
hermes -z "Create a competitive analysis report template"

# 3. When research completes, synthesize
hermes -z "Merge the research findings into the report template"
```

### Pattern: Code Review Pipeline

```bash
# 1. Delegate a deep code review with the review skill preloaded
hermes -z --skills github-code-review "Review PR #42 in corpusiq-docs"

# 2. Parallel: a security pass on the same PR
hermes -z --skills security-audit "Audit PR #42 for vulnerabilities"

# 3. Merge findings
hermes -z "Combine the code review and security audit into one set of PR feedback"
```

### Pattern: Daily Operations

```bash
# Morning health check
hermes -z --skills corpusiq-system-auditor "Run system health check"

# Midday social sweep
hermes -z --skills corpusiq-organic-discovery "Check all platforms for mentions"

# Evening report
hermes -z --skills corpusiq-daily-html-reporting "Generate daily report"
```

---

## Cost Awareness

| Task Type | Estimated Cost |
|-----------|:--------------:|
| Simple Q&A (single turn) | $0.001-0.01 |
| Research task (multi-turn) | $0.02-0.10 |
| Complex task with subagents | $0.05-0.50 |
| Full daily operations sweep | $0.10-1.00 |

Costs vary by model selection. Sonnet is the cost-efficient default. Opus reserved for deep research and complex architecture.

---

## Related Skills

- [Hermes Agent Skill Authoring](/hermes/skills/catalog/hermes-agent-skill-authoring-setup) - Writing SKILL.md files
- [dandacompany/hermes](/hermes/skills/catalog) - Self-hosting and operations guide
- [wihy/hermes-agent-skill](/hermes/skills/catalog) - Portable CLI wrapper v2.0
- [Hermes Documentation](https://hermes-agent.nousresearch.com/docs) - Official docs
