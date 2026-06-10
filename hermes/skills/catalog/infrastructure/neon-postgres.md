---
name: neon-postgres
description: Serverless Postgres for agent state storage. Ideal database backend for AI agents. 40.4K installs.
triggers:
  - "neon postgres"
source: skills.sh marketplace
category: infrastructure
setup: npx skills add neondatabase/agent-skills
---

# Neon Postgres

Serverless Postgres for agent state storage.

## Setup

```bash
npx skills add neondatabase/agent-skills@neon-postgres
```

## Capabilities

Database provisioning, connection pooling, branching, point-in-time recovery.

## Hermes Integration

Install with `npx skills add` or via the Hermes skills manager. The skill auto-registers tools and workflows for the agent.

## Source

Discovered via skills.sh marketplace scan, June 2026.
