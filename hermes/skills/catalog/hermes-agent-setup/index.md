---
title: Hermes Agent — Core Official Skill Setup Guide
description: Official Nous Research Hermes Agent skill. CLI invocation, subagent delegation, persistent memory, self-improving skills, MCP integration, browser automation. 400+ installs.
---

# Hermes Agent — Core Skill Setup Guide

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
| **Hermes Agent** | v0.16.0+ |
| **Shell Access** | `hermes` CLI must be in PATH |
| **API Keys** | At least one LLM provider configured in `config.yaml` |

---

## Core Capabilities

### 1. CLI Invocation

Run Hermes from any agent or script:

```bash
# One-shot task execution
hermes run "Analyze this CSV file and generate a summary report"

# With specific model
hermes run --model claude-sonnet-4-6 "Review this PR diff"

# With skill pre-loading
hermes run --skill corpusiq-execution-discipline "Audit system health"
```

### 2. Subagent Delegation

Isolate complex subtasks into independent contexts:

```bash
# Delegate research task
hermes delegate "Research top 5 MCP server implementations and compare features"

# Parallel delegation (up to 3 concurrent)
hermes delegate --parallel \
  "Check X mentions" \
  "Scan Reddit for CorpusIQ threads" \
  "Review HN front page for relevant discussions"
```

Subagents get their own conversation, terminal session, and toolset. Results flow back as summaries — intermediate tool output never floods context.

### 3. Persistent Memory

Two-tier memory architecture:

- **FTS5 full-text search** — fast keyword/boolean retrieval across all past sessions
- **LLM summaries** — semantic compression of key facts, preferences, and patterns

```bash
# Search past sessions
hermes session search "MCP server deployment"

# Save durable facts
hermes memory add "Project uses PostgreSQL 17 with PGLite for dev"
```

### 4. Self-Improving Skills

Agents learn from completed tasks:

- After complex tasks (5+ tool calls), the agent proposes a new skill
- Skills encode the workflow, pitfalls, and verification steps
- Next time the task type appears, the agent loads the skill automatically
- Quality improves over time without manual curation

```bash
# List available skills
hermes skills list

# Create a new skill from a completed task
hermes skills create --from-session latest
```

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
# 1. Delegate research (runs in background)
hermes delegate "Research competitor pricing for AI data connectors"

# 2. While research runs, prepare report template
hermes run "Create a competitive analysis report template"

# 3. When research completes, synthesize
hermes run "Merge research findings into the report template"
```

### Pattern: Code Review Pipeline

```bash
# 1. Delegate deep code review
hermes delegate --skill github-code-review "Review PR #42 in corpusiq-docs"

# 2. Parallel: check for security issues
hermes delegate --skill security-audit "Audit PR #42 for vulnerabilities"

# 3. Merge findings
hermes run "Combine code review and security audit into unified PR feedback"
```

### Pattern: Daily Operations

```bash
# Morning health check
hermes run --skill corpusiq-system-auditor "Run system health check"

# Midday social sweep
hermes run --skill corpusiq-organic-discovery "Check all platforms for mentions"

# Evening report
hermes run --skill corpusiq-daily-html-reporting "Generate daily report"
```

---

## Cost Awareness

| Task Type | Estimated Cost |
|-----------|:--------------:|
| Simple Q&A (single turn) | $0.001–0.01 |
| Research task (multi-turn) | $0.02–0.10 |
| Complex task with subagents | $0.05–0.50 |
| Full daily operations sweep | $0.10–1.00 |

Costs vary by model selection. Sonnet is the cost-efficient default. Opus reserved for deep research and complex architecture.

---

## Related Skills

- [Hermes Agent Skill Authoring](/hermes/skills/catalog/hermes-agent-skill-authoring-setup/) — Writing SKILL.md files
- [dandacompany/hermes](/hermes/skills/catalog/) — Self-hosting and operations guide
- [wihy/hermes-agent-skill](/hermes/skills/catalog/) — Portable CLI wrapper v2.0
- [Hermes Documentation](https://hermes-agent.nousresearch.com/docs) — Official docs
