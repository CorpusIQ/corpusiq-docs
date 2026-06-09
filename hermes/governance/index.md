---
title: Agent Governance & Operations
description: Production governance for autonomous agents — system registry, email ops, cron management, token lifecycle
---

# Governance & Operations

The most overlooked aspect of autonomous systems. Without governance, agents drift. With governance, they compound.

## System Registry

Every component is registered before creation. Prevents system sprawl.

```
~/.hermes/profiles/{profile}/
  SYSTEM_REGISTRY.md    — Component inventory
  TASK_HISTORY.md       — Action log  
  data/
    post-log.jsonl      — Social publishing
    activity-log.jsonl  — All platform actions
    lead-pipeline.jsonl — Lead tracking
```

## Email Operations

Autonomous monitoring of media@corpusiq.io and info@corpusiq.io.

Pipeline: Monitor → Qualify → Route → Research → Draft → Escalate

## Cron Management

38 active scheduled processes across email, social, content, knowledge, infrastructure, growth, and job applications.

Every cron is verified by actual execution — not `last_status: ok`.

## Authentication Lifecycle

| Service | Auth | Refresh |
|---------|------|---------|
| Gmail API | OAuth 2.0 | Auto |
| YouTube | OAuth 2.0 | Auto |
| HeyGen | API Key | Manual |
| Postiz | API Key | Manual |
| CorpusIQ MCP | OAuth 2.0 | Auto |

Token refresh automation, expiration monitoring, alerting.

## Daily Report

6 PM Arizona — HTML report: social, leads, email, learnings, self-improvement, tomorrow.

---

*Next: [Infrastructure](/infrastructure/) · [Architecture Overview](/architecture/)*
