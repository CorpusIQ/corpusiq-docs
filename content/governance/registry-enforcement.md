# Registry Enforcement

## How we prevent unregistered sprawl in autonomous agent systems.

The most common failure in long-running agent deployments is accumulation: crons nobody remembers creating, scripts nobody knows still run, workflows that drifted from their original purpose.

Our fix: if it is not in a registry, it does not exist and cannot execute.

---

## The Rule

Every script, cron, workflow, agent, tool, platform, API, server, and automation must have a corresponding entry in its registry.

| Thing | Registry |
|-------|----------|
| Agent | Agent registry — role, tools, memory, owner |
| Workflow | Workflow registry — trigger, inputs, outputs, validation, owner |
| Tool | Tool registry — agents that use it, purpose |
| Cron job | Cron registry — schedule, workflow, agent, delivery target |
| Memory system | Memory registry — type, location, readers, writers, retention |

---

## Enforcement

Before any execution:
1. Verify the thing exists in its registry.
2. If not found: block execution. Log the violation.
3. Either register it properly or decommission it.

For existing systems: a daily drift check compares crontab, scripts, and running processes against registries. Any mismatch is flagged.

---

## Why This Matters

Unregistered execution is the root cause of duplicate work, competing pipelines, and orphaned automations. Registration creates accountability. Accountability prevents drift.

---

*Part of the CorpusIQ Agent Operating System documentation.*
