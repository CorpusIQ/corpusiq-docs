---
title: writing-plans + subagent-driven-development Setup Guide
description: Complete setup guide for the writing-plans and subagent-driven-development skills from nousresearch/hermes-agent. Plan-based development workflow with delegate_task subagent execution and 2-stage review.
---

# writing-plans + subagent-driven-development Setup

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skills.sh:** [writing-plans](https://skills.sh/nousresearch/hermes-agent/writing-plans) | [subagent-driven-development](https://skills.sh/nousresearch/hermes-agent/subagent-driven-development)

## 1. Installation

```bash
npx skills add nousresearch/hermes-agent --skill writing-plans
npx skills add nousresearch/hermes-agent --skill subagent-driven-development
```

## 2. Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ with `delegate_task` tool enabled |
| Subagent config | `delegation.max_concurrent_children` set in config.yaml |
| No external API keys | Both skills are local-only |

## 3. Capabilities

### writing-plans

| Capability | Trigger | Output |
|-----------|---------|--------|
| Task decomposition | "write a plan for X" | Numbered task list with file paths |
| Dependency mapping | Complex multi-file features | Dependency graph with execution order |
| Code scaffolding | "scaffold the plan" | Stub files with signatures |
| Effort estimation | Plan review | Per-task complexity scores |

### subagent-driven-development

| Capability | Trigger | Output |
|-----------|---------|--------|
| Parallel execution | "execute the plan" | Spawned subagents per task |
| 2-stage review | After each subagent completes | Review → approve/reject → retry |
| Result reconciliation | After all subagents complete | Merged results, conflict resolution |
| Rollback on failure | Subagent failure | Clean revert of failed task artifacts |

## 4. CLI / Command Reference

```bash
# Load skills in a session
# The agent auto-loads these when relevant  --  no manual trigger needed

# Manual invocation pattern:
# 1. Ask Hermes to write a plan
# "Write an implementation plan for adding dark mode to the dashboard"
# → writing-plans skill activates, produces numbered task list

# 2. Execute the plan
# "Execute the dark mode plan"
# → subagent-driven-development activates, spawns workers

# 3. Review progress
# "Show me the status of the dark mode implementation"
# → Agent reconciles subagent results, shows completion state
```

## 5. CorpusIQ Use Cases

| Use Case | How It Works |
|----------|-------------|
| **Feature development** | Break new CorpusIQ features into plans, execute in parallel  --  3-5x faster than sequential |
| **Docs updates** | Plan doc page creation across multiple sections, execute simultaneously |
| **System audit fixes** | Decompose audit findings into fix tasks, delegate to subagents |
| **Connector integration** | Plan connector setup (MCP server + docs + tests), execute in parallel |
| **Multi-platform content** | Plan social posts across platforms, delegate per-platform formatting |

## 6. Troubleshooting

| Issue | Solution |
|-------|----------|
| Subagent context missing files | Ensure `context` field in `delegate_task` includes all relevant file paths |
| Subagent results conflict | Review the reconciliation output  --  agent flags conflicts for manual resolution |
| Plan too granular | Ask "simplify the plan to 3-5 tasks"  --  plans auto-scale to feature complexity |
| Subagent timeout | Increase `delegation.timeout` in config.yaml; split oversized tasks |

**Verification:**
```bash
# Verify skills installed
npx skills list | grep -E "writing-plans|subagent-driven-development"

# Test plan generation
# In a Hermes session: "Write a plan for adding a hello-world endpoint"
# Should produce: numbered tasks with file paths and dependencies
```

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
