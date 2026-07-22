---
title: Dockerize and Deploy — Containerize any repo for Hermes Agent deployment
description: Dockerfile, docker-compose with volumes, and preflight script generation. 44+ installs from rockclaver/systemcraft.
---

# Dockerize and Deploy — Setup Guide

**Source:** [rockclaver/systemcraft](https://skills.sh/rockclaver/systemcraft/dockerize-and-deploy) (44+ installs)
**Category:** Engineering / DevOps
**Quality Tier:** 🔵 Community

Systematic skill for containerizing any repository. Generates multi-stage Dockerfiles, docker-compose configurations for dev and production, preflight validation scripts, and a deploy pipeline — one phase at a time.

---

## Installation

```bash
npx skills add rockclaver/systemcraft --skill dockerize-and-deploy
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Docker** | Docker Engine with BuildKit |
| **Docker Compose** | v2+ for compose configurations |
| **Git repo** | Target repository to containerize |

---

## Key Capabilities

### Phase 1: Dockerfile Generation
Multi-stage builds: builder installs/compiles, runtime copies artifacts only. Non-root user, pinned base images (e.g., `node:20.11-alpine`), `.dockerignore` excludes `node_modules`/`.env`/`.git`.

### Phase 2: Development Compose
Source mounts for hot reload, debug ports, named volumes. Stack runs with `docker compose up -d`.

### Phase 3: Production Compose
No source mounts, `restart: unless-stopped`, healthchecks, explicit volumes, `mem_limit`/`cpus` limits.

### Phase 4: Pre-flight Validation
Validates env vars, Docker availability, port conflicts, DB reachability, and runs a dry-run build.

### Phase 5: Deploy Script
Pull/build image → run migrations → rolling restart → health-check → print status. Aborts on preflight failure.

---

## Quick Start

```bash
# After installation, invoke the skill on your repo
# Phase 1: Dockerfile
docker build -t app:test .

# Phase 2: Compose validation
docker compose config

# Phase 3: Start stack
docker compose up -d && docker compose ps

# Phase 4: Pre-flight
bash scripts/preflight.sh
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep dockerize-and-deploy

# Verify Docker is available
docker --version && docker compose version
```

---

## Notes

- Never embed secrets in Docker/compose files — use environment variables or secrets management
- Always run containers as non-root user
- No `latest` image tags in production — pin versions
- DB volumes use named volumes only, never host bind mounts
- Guardrails enforced: no secrets, non-root, pinned tags, named volumes
- References included for volume/healthcheck patterns, resource limits, and rolling deploy strategies
- Quality tier 🔵 Community: 44 installs, newer skill with room for growth
