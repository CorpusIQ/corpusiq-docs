---
title: Infra Deploy (Cal.com) — GCP Cloud Run deployment for Hermes Agent infrastructure
description: Deploy Cal.com self-hosted to GCP Cloud Run with Supabase PostgreSQL. 108+ installs from terrylica/cc-skills.
---

# Infra Deploy (Cal.com) — Setup Guide

**Source:** [terrylica/cc-skills](https://skills.sh/terrylica/cc-skills/infra-deploy) (108+ installs)
**Category:** Engineering / DevOps
**Quality Tier:** 🟡 Beta

Deploy Cal.com self-hosted to GCP Cloud Run with Supabase PostgreSQL, or run locally via Docker Compose. Includes webhook relay for Pushover notifications, Supabase database management, and 1Password secret integration.

---

## Installation

```bash
npx skills add terrylica/cc-skills --skill infra-deploy
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **GCP account** | Cloud Run, Artifact Registry, Cloud Build APIs enabled |
| **Supabase** | PostgreSQL project with connection URL |
| **1Password CLI** | For secret management (Claude Automation vault) |
| **Docker** | For local dev and container builds |
| **gcloud CLI** | Authenticated to target GCP project |

---

## Key Capabilities

### GCP Cloud Run Deployment
Multi-step deployment: verify GCP APIs → build Docker container → push to Artifact Registry → deploy to Cloud Run with env vars from 1Password. Managed platform with auto-scaling (0-2 instances, 512Mi memory).

### Docker Compose (Local Dev)
Templated docker-compose with Cal.com + PostgreSQL 15, healthchecks, named volumes, and `.env` template with all required variables.

### Webhook Relay (Pushover)
Lightweight Cloud Run service bridging Cal.com webhooks to Pushover emergency alerts. Zero dependencies (Python stdlib only). Includes health verification, webhook registration, and simulated booking test.

### Supabase Management
Connection verification, Prisma migration deployment, and database URL resolution from 1Password.

---

## Quick Start

```bash
# Preflight: verify GCP config
echo "CALCOM_GCP_PROJECT: ${CALCOM_GCP_PROJECT:-NOT_SET}"
gcloud auth list --filter="status=ACTIVE" --format="value(account)"

# Local dev with Docker Compose
cd ~/fork-tools/cal.com
docker compose up -d

# Deploy to Cloud Run
docker build -t calcom-self-hosted .
docker tag calcom-self-hosted "${REGION}-docker.pkg.dev/${PROJECT}/calcom/calcom:latest"
docker push "${REGION}-docker.pkg.dev/${PROJECT}/calcom/calcom:latest"
gcloud run deploy calcom --image=... --region=... --platform=managed
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep infra-deploy

# Verify GCP APIs
gcloud services list --enabled --project="$CALCOM_GCP_PROJECT" | grep -E "run|artifact|build"

# Check Supabase connection
psql "$DATABASE_URL" -c "SELECT version();"
```

---

## Notes

- Self-evolving skill: instructions updated when parameters drift or workarounds needed
- All secrets stored in 1Password Claude Automation vault (biometric-free access)
- Cal.com-specific but deployment patterns (Cloud Run + Supabase + webhooks) generalize to other apps
- Includes post-change checklist for YAML validation, trigger keywords, and path patterns
- Uses `.mise.local.toml` for local environment variable management
- Quality tier 🟡 Beta: 108 installs, actively maintained
