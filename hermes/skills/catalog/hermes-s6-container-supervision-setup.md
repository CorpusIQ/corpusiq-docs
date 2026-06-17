---
title: hermes-s6-container-supervision Setup Guide
description: Production-grade s6 supervision for Hermes agent containers — health checks, auto-restarts, logging, and process management.
---

# hermes-s6-container-supervision

**Install:** `npx skills add nousresearch/hermes-agent/hermes-s6-container-supervision`
**Installs:** 76
**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/hermes-s6-container-supervision)

## Overview

The `hermes-s6-container-supervision` skill enables production-grade process supervision for Hermes agents running in containers. Built on the s6 supervision suite, it provides health checks, automatic restarts, log rotation, and process lifecycle management — essential for long-running agent deployments.

## What It Does

- **Health checks:** Monitors Hermes agent processes for crashes, hangs, and resource exhaustion
- **Auto-restart:** Automatically restarts failed agent processes with configurable backoff
- **Log management:** Captures stdout/stderr with rotation and retention policies
- **Container awareness:** Designed for Docker/Podman containers — proper signal handling, PID 1 behavior
- **Multi-agent support:** Supervise multiple Hermes agent instances from one s6 service directory

## Why CorpusIQ Needs This

CorpusIQ runs Hermes agents on DGX Spark and Mac Mini worker nodes. Agent processes that crash silently or hang indefinitely create operational blind spots. s6 supervision ensures:

1. **Zero manual intervention:** Agents restart automatically on failure
2. **Observability:** Structured logs for debugging and audit trails
3. **Production readiness:** Proper signal handling for graceful shutdowns during deploys
4. **Resource management:** Detect and respond to memory leaks or CPU spikes

## Installation

```bash
# Install the skill
npx skills add nousresearch/hermes-agent/hermes-s6-container-supervision

# Verify installation
ls skills/hermes-s6-container-supervision/
```

## Basic Usage

### 1. Create a service definition for your Hermes agent

```bash
# Example: /etc/s6/sv/hermes-agent/run
#!/bin/execlineb -P
hermes agent run --profile corpusiq
```

### 2. Enable the service

```bash
# Link into the supervision tree
ln -s /etc/s6/sv/hermes-agent /etc/s6/service/
```

### 3. Verify supervision is active

```bash
s6-svstat /etc/s6/service/hermes-agent
# Output: up (pid 1234) 3600 seconds
```

## Configuration

The skill provides these configuration options:

| Setting | Default | Description |
|---------|---------|-------------|
| `restart_policy` | `always` | Restart behavior: `always`, `on-failure`, `never` |
| `max_restarts` | `10` | Maximum restarts per hour before escalation |
| `health_check_interval` | `30s` | Time between health checks |
| `log_retention_days` | `30` | Days to retain agent logs |
| `memory_limit_mb` | `2048` | Soft memory limit with warning |

## Docker Integration

```dockerfile
FROM node:20-slim

# Install Hermes and s6
RUN npm install -g hermes-agent
RUN apt-get update && apt-get install -y s6

# Copy service definitions
COPY s6-services/ /etc/s6/service/

# s6 as PID 1
ENTRYPOINT ["/usr/bin/s6-svscan", "/etc/s6/service"]
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Agent not restarting | Check `max_restarts` — may have hit the per-hour limit |
| Logs not rotating | Verify `log_retention_days` and disk space |
| s6 not detecting crash | Confirm the agent's `run` script exits on crash (no trap-based recovery) |
| Multiple instances conflict | Use unique service directories per agent instance |

## Related Skills

- [hermes-agent](/hermes/skills/catalog/) — Core Hermes agent skill
- [docker-management](/hermes/skills/marketplace/new-june17-2026/) — Docker container management
- [openclaw-migration](/hermes/skills/marketplace/new-june17-2026/) — Migration path from OpenClaw

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
