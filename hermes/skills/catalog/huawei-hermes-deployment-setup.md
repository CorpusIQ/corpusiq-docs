---
title: Huawei Cloud Hermes Deployment — Full Setup Guide
description: Deploy Hermes Agent on Huawei Cloud Flexus L-series servers using the huaweicloud-skills deployment template (43 installs). Production Docker Compose with ARM64 support.
---

# Huawei Cloud Flexus — Hermes Deployment Guide

**Source:** [huaweicloud/huaweicloud-skills](https://skills.sh/huaweicloud/huaweicloud-skills) (43 installs)
**Category:** Infrastructure & Deployment

A production deployment template for running Hermes Agent on Huawei Cloud Flexus L-series servers. Includes Docker Compose configuration, ARM64 architecture support, and cloud-specific optimizations. Part of a broader Huawei Cloud skills collection (5+ skills) covering OpenClaw deployment, JiuwenSwarm, and cloud operations.

---

## Installation

```bash
npx skills add huaweicloud/huaweicloud-skills --skill huawei-cloud-flexus-l-server-hermes-deployment
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Huawei Cloud Account** | Flexus L-series instance with at least 4 vCPUs, 8GB RAM |
| **Docker & Docker Compose** | Installed on the Flexus instance |
| **Hermes Agent** | v0.16.0+ |
| **Domain (optional)** | For HTTPS access to Hermes Web UI |
| **ARM64 or x86_64** | Template supports both architectures |

Huawei Cloud environment:

```bash
export HUAWEI_CLOUD_REGION="ap-southeast-3"
export HUAWEI_CLOUD_ACCESS_KEY="<your-access-key>"
export HUAWEI_CLOUD_SECRET_KEY="<your-secret-key>"
```

---

## Key Capabilities

### Deployment Features

| Capability | How to Trigger | Notes |
|---|---|---|
| One-click deploy | `bash deploy.sh` | Provisions full Hermes stack on Flexus |
| Docker Compose stack | Automatic | Hermes + PostgreSQL + Redis + Nginx |
| ARM64 optimized | Auto-detected | Native ARM64 builds for Apple Silicon / Graviton |
| Cloud storage integration | Configured in `.env` | OBS (Object Storage) for backups and logs |
| Auto-scaling | Via Huawei Cloud AS | Scale worker nodes based on load |

### CLI Command Reference

```bash
# Deploy Hermes to Huawei Cloud Flexus
bash SKILL_DIR/scripts/deploy.sh --region ap-southeast-3

# Check deployment status
bash SKILL_DIR/scripts/status.sh

# Tear down deployment
bash SKILL_DIR/scripts/destroy.sh

# View logs
bash SKILL_DIR/scripts/logs.sh --service hermes-agent
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Asian Market Deployment** | Deploy CorpusIQ agent infrastructure in Huawei Cloud's Asia-Pacific regions for lower latency |
| **ARM64 Production** | Run Hermes agents on ARM64 Flexus instances — cost-efficient for always-on cron agents |
| **Multi-Cloud Strategy** | Add Huawei Cloud as a deployment option alongside AWS/GCP/Azure |
| **China Market Access** | Huawei Cloud provides compliant infrastructure for Chinese market operations |
| **Disaster Recovery** | Use Huawei Cloud as a secondary region for agent failover |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "Docker daemon not running" | `sudo systemctl start docker && sudo systemctl enable docker` |
| "ARM64 image not found" | Rebuild: `docker compose build --no-cache` |
| "OBS access denied" | Verify IAM permissions for OBS bucket access in Huawei Cloud console |
| "Port 443 already in use" | Change Nginx port in `docker-compose.override.yml` |

## Verification

```bash
# Verify skill installed
hermes skills list | grep huawei-cloud-flexus

# Check deployment template
ls SKILL_DIR/templates/docker-compose.yml

# Dry-run deployment
bash SKILL_DIR/scripts/deploy.sh --dry-run
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 28 Discovery](/hermes/skills/marketplace/new-june28-2026/) →*
*Powered by CorpusIQ*
