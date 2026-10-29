---
title: "Docker Hermes Agent Setup - CorpusIQ Docs"
description: Deploy Hermes Agent as a Docker container for reproducible AI automation. Docker Compose setup with persistent volumes, MCP server integration, cron persistence, and production checklist. Works on any host.
category: setup
tags: [docker, hermes-agent, setup-guide, container, docker-compose, reproducible, cicd, deployment]
last_updated: 2026-10-29
canonical: "https://www.corpusiq.io/docs/hermes/setup/docker/"
robots: "index,follow"

---

# Docker Hermes Agent Setup  --  Reproducible Container Deployment

Deploy Hermes Agent as a Docker container for identical behavior on your laptop, a cloud VPS, or a CI/CD pipeline. No Python version conflicts, no dependency hell  --  just consistent, reproducible AI agent deployment. This Docker setup guide covers Compose configuration, volume management, MCP integration, and production hardening.

## Overview

Docker deployment is the most portable way to run Hermes Agent. The official `nousresearch/hermes-agent` image ships with all dependencies pre-installed (Python 3.14, Node.js, Chromium). Mount your data directory as a volume for persistence, set API keys as environment variables, and you're running in under 2 minutes.

The image is **stateless**: every piece of mutable state lives in the single data directory mounted from the host at `/opt/data`. The installed application tree at `/opt/hermes` is root-owned and read-only to the runtime user, so a plain image pull upgrades the agent without touching your config.

| Image tag | Meaning |
|---|---|
| `latest` / `stable` | Accepted by the stable release gate |
| `main` | Development image built from the main branch |
| `X.Y.Z` | Versioned stable image; pin a digest for exact deployments |

## How It Works

| Component | Docker Approach |
|---|---|
| **Hermes binary** | Pre-installed at `/opt/hermes` in the container image |
| **Configuration** | Host directory mounted at `/opt/data` (`~/.hermes` by default) |
| **API keys** | `/opt/data/.env` inside the container, or environment variables |
| **Skills** | Under `/opt/data/skills` in the mounted volume |
| **Crons** | Stored in the volume, survive restarts |
| **MCP servers** | Run inside container, added via `docker compose exec` |

## Quick Start

Run the setup wizard once to write your keys to `~/.hermes/.env`:

```bash
mkdir -p ~/.hermes
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent setup
```

Then start the container as a persistent gateway:

```bash
docker run -d --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  nousresearch/hermes-agent gateway run
```

Port 8642 exposes the gateway's OpenAI-compatible API server and health endpoint. It is optional if you only use chat platforms, and required if you want the dashboard or external tools to reach the gateway. Inside the official image the gateway is supervised by s6-overlay, so a crash restarts it in seconds without losing the container.

## Full docker-compose.yml

```yaml
services:
  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped

    command: ["gateway", "run"]

    volumes:
      # All mutable state lives here: config, .env, skills, sessions, crons.
      - ~/.hermes:/opt/data

    environment:
      # Keep files created in the container owned by your host user.
      - HERMES_UID=${HERMES_UID:-10000}
      - HERMES_GID=${HERMES_GID:-10000}
      - TZ=${TZ:-UTC}

    ports:
      - "127.0.0.1:8642:8642"   # OpenAI-compatible API server (optional)
      - "127.0.0.1:9119:9119"   # dashboard (only with HERMES_DASHBOARD=1)

    healthcheck:
      # Liveness only. `hermes doctor` exits non-zero on advisories such as
      # npm vulnerability notices, so it would mark a working container
      # unhealthy. Use it interactively, not as a healthcheck.
      test: ["CMD", "hermes", "--version"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 30s
```

The top-level `version:` key is obsolete in Compose v2 and is omitted here; Docker Compose warns about it and ignores the value.

## Launch

```bash
mkdir -p ~/.hermes
export HERMES_UID=$(id -u) HERMES_GID=$(id -g)
docker compose up -d
docker compose logs -f hermes
docker compose exec hermes hermes doctor
```

The model is a config value, not an environment variable. Set it inside the container:

```bash
docker compose exec hermes hermes model          # interactive picker
docker compose exec hermes hermes config set model.default "anthropic/claude-sonnet-4.6"
```

## Adding MCP Servers

```bash
# Remote HTTP/SSE server
docker compose exec hermes hermes mcp add corpusiq --url https://mcp2.corpusiq.io/mcp

# Remote server that needs a bearer token (prompts for the key, saves it to /opt/data/.env)
docker compose exec hermes hermes mcp add honcho --url https://mcp.honcho.dev --auth header

# Stdio server: --args must be the last option
docker compose exec hermes hermes mcp add github --command npx --args @modelcontextprotocol/server-github
```

Verify with `docker compose exec hermes hermes mcp test corpusiq`. See the [MCP Integration Guide](/hermes/mcp) for all available servers.

## Crons and Persistence

The schedule and the prompt are positional arguments; `--name` and `--deliver` are flags:

```bash
docker compose exec hermes hermes cron create "*/15 * * * *" \
  "Check inbox. Summarize unread." \
  --name email-watch \
  --deliver local
```

Crons survive container restarts and image updates because they're stored under `/opt/data` in the mounted volume. Follow [cron design best practices](/hermes/best-practices/cron-design) for production-grade scheduling.

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
- **Persistent**: The mounted data directory survives updates and restarts
- **Production-ready**: Health checks, restart policies, log rotation built in

## FAQ

### Do I need to rebuild the Docker image for updates?
No  --  `docker compose pull` fetches the latest image from Docker Hub. Your config, skills, and crons persist in the mounted volume.

### Can I run GPU-accelerated models in Docker?
Yes, if the host has an NVIDIA GPU and the NVIDIA Container Toolkit installed. Pass `--gpus all` to `docker run` or add `deploy.resources.reservations.devices` in Compose.

### How do I add custom skills to Docker Hermes?
Put them in the mounted data directory: `~/.hermes/skills/` on the host is `/opt/data/skills` in the container. No extra mount is needed, and new skills are picked up on the next session. See the [custom skills guide](/hermes/skills/creating-skills).

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup)  --  All platform options
- [Cloud VPS Setup](cloud-vps.md)  --  Docker on cloud
- [Gaming PC Setup](gaming-pc.md)  --  Docker with GPU passthrough
- [MCP Integration Guide](/hermes/mcp)  --  Connect tools inside containers
- [Creating Custom Skills](/hermes/skills/creating-skills)  --  Mount skills in Docker
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
