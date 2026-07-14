---
title: Docker Hermes Agent Setup  --  Reproducible Container Deployment Guide
description: Deploy Hermes Agent as a Docker container for reproducible AI automation. Docker Compose setup with persistent volumes, MCP server integration, cron persistence, and production checklist. Works on any host.
category: setup
tags: [docker, hermes-agent, setup-guide, container, docker-compose, reproducible, cicd, deployment]
last_updated: 2026-07-08
---

# Docker Hermes Agent Setup  --  Reproducible Container Deployment

Deploy Hermes Agent as a Docker container for identical behavior on your laptop, a cloud VPS, or a CI/CD pipeline. No Python version conflicts, no dependency hell  --  just consistent, reproducible AI agent deployment. This Docker setup guide covers Compose configuration, volume management, MCP integration, and production hardening.

## Overview

Docker deployment is the most portable way to run Hermes Agent. The official `nousresearch/hermes-agent:latest` image ships with all dependencies pre-installed. Mount your config as a volume for persistence, set API keys as environment variables, and you're running in under 2 minutes.

## How It Works

| Component | Docker Approach |
|---|---|
| **Hermes binary** | Pre-installed in container image |
| **Configuration** | Persistent named volume (`hermes_data`) |
| **API keys** | Environment variables in `.env` file |
| **Skills** | Mount local `./skills` directory (read-only) |
| **Crons** | Stored in volume, survive restarts |
| **MCP servers** | Run inside container, added via `docker compose exec` |

## Quick Start

```bash
docker run -d --name hermes-agent \
  -v ~/.hermes:/home/hermes/.hermes \
  -e OPENROUTER_API_KEY=*** \
  --restart unless-stopped \
  nousresearch/hermes-agent:latest
```

## Full docker-compose.yml

```yaml
version: "3.8"

services:
  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-agent
    restart: unless-stopped

    volumes:
      - hermes_data:/home/hermes/.hermes
      - ./skills:/home/hermes/skills:ro

    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-}
      - DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY:-}
      - OPENAI_API_KEY=${OPENAI_API_KEY:-}
      - HERMES_PROFILE=${HERMES_PROFILE:-docker}
      - HERMES_DEFAULT_MODEL=${HERMES_DEFAULT_MODEL:-openrouter/anthropic/claude-sonnet-4}
      - TZ=${TZ:-UTC}

    ports:
      - "127.0.0.1:8080:8080"

    healthcheck:
      test: ["CMD", "hermes", "doctor", "--check"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 30s

volumes:
  hermes_data:
    driver: local
```

## Launch

```bash
cp providers.env.example .env  # Edit with your API keys
docker compose up -d
docker compose logs -f hermes
docker compose exec hermes hermes doctor
```

## Adding MCP Servers

```bash
docker compose exec hermes hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp
docker compose exec hermes hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev \
  --header "Authorization: Bearer ***"
```

See the [MCP Integration Guide](/hermes/mcp/) for all available servers.

## Crons and Persistence

```bash
docker compose exec hermes hermes cron create \
  --name "email-watch" \
  --prompt "Check inbox. Summarize unread." \
  --schedule "*/15 * * * *"
```

Crons survive container restarts and image updates because they're stored in the `hermes_data` volume. Follow [cron design best practices](/docs/hermes/best-practices/cron-design.html) for production-grade scheduling.

## Production Checklist

```bash
# 1. Resource limits
# Add to docker-compose.yml:
#   deploy:
#     resources:
#       limits:
#         memory: 2G
#         cpus: "2"

# 2. Log rotation
#   logging:
#     driver: "json-file"
#     options:
#       max-size: "10m"
#       max-file: "3"

# 3. Monitor health
docker compose ps
docker compose exec hermes hermes gateway status
```

## Docker on Different Hosts

| Host | Notes |
|---|---|
| **Local laptop** | Development and testing |
| **Cloud VPS** | Add `--restart unless-stopped` for 24/7 |
| **NAS / home server** | Mount large volumes for GBrain embeddings |
| **CI/CD** | Ephemeral volumes for automated testing |

## Benefits

- **Reproducible**: Identical behavior everywhere
- **No dependency conflicts**: Everything bundled in container
- **Portable**: Same Compose file works on laptop, VPS, or CI/CD
- **Persistent**: Named volumes survive updates and restarts
- **Production-ready**: Health checks, restart policies, log rotation built in

## FAQ

### Do I need to rebuild the Docker image for updates?
No  --  `docker compose pull` fetches the latest image from Docker Hub. Your config, skills, and crons persist in the mounted volume.

### Can I run GPU-accelerated models in Docker?
Yes, if the host has an NVIDIA GPU and the NVIDIA Container Toolkit installed. Pass `--gpus all` to `docker run` or add `deploy.resources.reservations.devices` in Compose.

### How do I add custom skills to Docker Hermes?
Mount your skills directory: `- ./skills:/home/hermes/skills:ro`. New skills are immediately available. See the [custom skills guide](/docs/hermes/skills/creating-skills.html).

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup/)  --  All platform options
- [Cloud VPS Setup](cloud-vps.md)  --  Docker on cloud
- [Gaming PC Setup](gaming-pc.md)  --  Docker with GPU passthrough
- [MCP Integration Guide](/hermes/mcp/)  --  Connect tools inside containers
- [Creating Custom Skills](/docs/hermes/skills/creating-skills.html)  --  Mount skills in Docker
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
