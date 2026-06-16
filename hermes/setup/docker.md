# Docker — Reproducible Deployment

Deploy Hermes Agent as a container. Identical behavior on your laptop, a cloud VPS, or a CI/CD pipeline. No Python version conflicts, no dependency hell.

## Prerequisites

```bash
# Docker Engine 24+
docker --version

# Docker Compose (v2)
docker compose version
```

## Quick Start

```bash
docker run -d --name hermes-agent \
  -v ~/.hermes:/home/hermes/.hermes \
  -e OPENROUTER_API_KEY="your-key" \
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
      # Persistent config, profiles, skills, crons
      - hermes_data:/home/hermes/.hermes
      # Optional: mount local skills for development
      - ./skills:/home/hermes/skills:ro

    environment:
      # Model providers (use at least one)
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-}
      - DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY:-}
      - OPENAI_API_KEY=${OPENAI_API_KEY:-}

      # Profile and model
      - HERMES_PROFILE=${HERMES_PROFILE:-docker}
      - HERMES_DEFAULT_MODEL=${HERMES_DEFAULT_MODEL:-openrouter/anthropic/claude-sonnet-4}

      # Optional: Telegram messaging
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN:-}
      - TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID:-}

      # Timezone
      - TZ=${TZ:-UTC}

    # Expose if using web dashboard
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

## .env File

```bash
# providers.env
OPENROUTER_API_KEY=sk-or-v1-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
HERMES_PROFILE=docker
TZ=America/New_York
```

## Launch

```bash
# Create .env from template
cp providers.env.example .env
# Edit .env with your API keys

# Start
docker compose up -d

# Check logs
docker compose logs -f hermes

# Verify
docker compose exec hermes hermes doctor
```

## Volume Mounts Explained

| Mount | Purpose | Persistent? |
|---|---|---|
| `hermes_data:/home/hermes/.hermes` | Profiles, config, skills, crons | Yes |
| `./skills:/home/hermes/skills:ro` | Custom skills (read-only) | Source of truth on host |

Always mount `hermes_data` as a named volume or bind mount. Without it, all your profiles and crons vanish on container restart.

## Adding MCP Servers

MCP servers run inside the container. Add them via `docker compose exec`:

```bash
# Add CorpusIQ MCP
docker compose exec hermes hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp

# Add Honcho memory
docker compose exec hermes hermes mcp add honcho -- npx mcp-remote https://mcp.honcho.dev \
  --header "Authorization: Bearer your-token" \
  --header "X-Honcho-Workspace-ID: your-workspace"
```

## Crons and Persistence

Crons persist because `hermes_data` volume stores them:

```bash
docker compose exec hermes hermes cron create \
  --name "email-watch" \
  --prompt "Check inbox. Summarize unread. Silent if empty." \
  --schedule "*/15 * * * *"
```

Crons survive container restarts and image updates.

## Docker on Different Hosts

| Host | Notes |
|---|---|
| **Local laptop** | Good for development and testing |
| **Cloud VPS** | Add `--restart unless-stopped` for 24/7 uptime |
| **NAS / home server** | Mount large volumes for GBrain embeddings |
| **CI/CD** | Ephemeral volumes; use for automated testing |

## Production Checklist

```bash
# 1. Set restart policy
docker compose up -d --restart unless-stopped

# 2. Limit resource usage
# Add to docker-compose.yml:
#   deploy:
#     resources:
#       limits:
#         memory: 2G
#         cpus: "2"

# 3. Set up log rotation
# Add to docker-compose.yml:
#   logging:
#     driver: "json-file"
#     options:
#       max-size: "10m"
#       max-file: "3"

# 4. Monitor health
docker compose ps
docker compose exec hermes hermes gateway status
```

## Upgrading

```bash
docker compose pull        # Get latest image
docker compose up -d       # Recreate container
docker compose exec hermes hermes --version  # Verify
```

---

*Next: [Cloud VPS Setup](cloud-vps.md) · [Infrastructure Overview](/hermes/infrastructure/)*
