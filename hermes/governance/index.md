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
8. **Content ontology** — pre-execution gate for all public content. Six dimensions: Public vs Internal, Human vs AI, Audience, Naming, Help-First, Freshness. Load before every external action.
9. **GitHub repo synchronization** — Every new tool, application, architecture change, memory entry, skill, cron job, or system modification must be pushed to the `CorpusIQ/corpusiq-docs` repository immediately after the change. No change goes undocumented. The repo is the single source of truth for system state.
10. **Platform connection failure** — When a platform connection fails (auth error, ban, shadowban, rate limit, token missing): STOP. Do not retry. Do not loop. Log the failure and move on. Crashing by retrying nonstop is worse than being silent on a dead platform. Only retry on explicit user instruction.
11. **Email sender identity** — From name is permanently locked. One account, one name. Never change the sender name on outbound emails. Changing names from the same account triggers Gmail impersonation detection and account flags.

## Monitoring Stack

```
Layer 1: Process — agent alive, CPU/memory bounds, no zombies
Layer 2: Operations — crons firing, emails flowing, APIs valid
Layer 3: Quality — outputs meeting thresholds, correct channels
```

---

*← [Infrastructure](/hermes/infrastructure/) | [Content Ops](/hermes/content-ops/) →*
*↑ [Home](/hermes/)*
