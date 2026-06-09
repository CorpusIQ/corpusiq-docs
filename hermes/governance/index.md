---
title: Agent Governance
description: Production governance for autonomous agents — system registry, email ops, cron management, monitoring
---

# Agent Governance

Safety rails, monitoring, and operational rules for autonomous agents. Seven governance rules, session management, and audit trails.

| Page | What You'll Learn |
|------|-------------------|
| [System Registry](/hermes/governance/registry/) | Configuration registry, environment variables, service inventory, canonical facts |
| [Email Operations](/hermes/governance/email/) | Dual-account management, send checklist, response standards, HTML templates |
| [Cron Scheduling](/hermes/governance/scheduling/) | Job management, scheduling patterns, chain jobs, delivery channels |
| [System Monitoring](/hermes/governance/monitoring/) | Health checks, drift detection, alerting, self-healing crons, audits |

## Seven Governance Rules

1. **Constitution first** — load CONSTITUTION.md before any action
2. **Task history** — check TASK_HISTORY.md before every action
3. **System registry** — verify SYSTEM_REGISTRY.md before creating anything
4. **Profile constraint** — single profile, no exceptions
5. **Done-only reporting** — never report scheduled/queued/planned work
6. **Execution discipline** — action first, reporting second
7. **Session governance** — session DB, token optimization, compaction

## Monitoring Stack

```
Layer 1: Process — agent alive, CPU/memory bounds, no zombies
Layer 2: Operations — crons firing, emails flowing, APIs valid
Layer 3: Quality — outputs meeting thresholds, correct channels
```

---

*← [Infrastructure](/hermes/infrastructure/) | [Content Ops](/hermes/content-ops/) →*
*↑ [Home](/hermes/)*
