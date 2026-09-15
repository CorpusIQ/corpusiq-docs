---
title: Alibaba Cloud AIOps Skills - 270-Skill Cloud Operations
description: "aliyun/alibabacloud-aiops-skills - 270 first-party Alibaba Cloud Agent Skills: ECS, SLS, DMS, RDS, DataWorks, OSS, Flink, Hologres, security, and cost operations. 30.8K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alibaba-cloud-aiops-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "alibaba cloud", "cloud", "devops", "aiops"]
---

# Alibaba Cloud AIOps Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/aliyun/alibabacloud-aiops-skills) (270 skills, ~30.8K combined installs)
**GitHub:** [aliyun/alibabacloud-aiops-skills](https://github.com/aliyun/alibabacloud-aiops-skills) (244⭐, 29 forks, Python, pushed Sep 11, 2026 - same-day active; no LICENSE file present)
**Category:** Cloud Operations / DevOps
**First Seen:** Mar 30, 2026 on skills.sh (surfaced in the Sep 11, 2026 sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub Pass / Socket Warn / Snyk Warn on the flagship skill)

The official Alibaba Cloud Agent Skills collection - 270 skills (the largest single-vendor suite catalogued in the docs to date) that give an agent hands-on control of Alibaba Cloud services: ECS diagnostics, SLS log queries, RDS copilots, DataWorks data ops, OSS management, Flink and Hologres operations, security-center workflows, and cost governance. Published under the first-party `aliyun` org with bilingual READMEs (English + 简体中文). Combined installs clear the 20K bar outright.

---

## Installation

Install all skills:

```bash
npx skills add aliyun/alibabacloud-aiops-skills
```

Install a single skill (recommended - 270 skills is a large surface):

```bash
npx skills add aliyun/alibabacloud-aiops-skills --skill alibabacloud-sls-query
```

For Hermes Agent, copy selected skill folders from a clone:

```bash
git clone https://github.com/aliyun/alibabacloud-aiops-skills.git
cp -r alibabacloud-aiops-skills/skills/developertools/solutions/alibabacloud-sls-query ~/.hermes/skills/
```

## Skill Roster (top 20 of 270)

| Skill | Installs | What It Does |
|---|---|---|
| `alibabacloud-find-skills` | 2.1K | Search, discover, and browse Alibaba Cloud agent skills (meta-skill index) |
| `alibabacloud-sls-query` | 1.5K | SLS log service queries |
| `alibabacloud-dms-skill` | 1.5K | Database Management Service operations |
| `alibabacloud-ecs-diagnose` | 644 | ECS instance diagnosis |
| `alibabacloud-cli-guidance` | 508 | Alibaba Cloud CLI guidance |
| `alibabacloud-ram-permission-diagnose` | 490 | RAM permission troubleshooting |
| `alibabacloud-dataworks-datastudio-develop` | 481 | DataWorks DataStudio development |
| `alibabacloud-rds-copilot` | 428 | RDS database copilot |
| `alibabacloud-bailian-rag-knowledgebase` | 403 | Bailian (Qwen ecosystem) RAG knowledge base construction |
| `alibabacloud-das-agent` | 361 | Database Autonomy Service |
| `alibabacloud-dataworks-data-ops` | 342 | DataWorks operational management |
| `alibabacloud-resourcecenter-search` | 337 | Cross-service resource search |
| `alibabacloud-odps-project-manage` | 291 | MaxCompute (ODPS) project management |
| `alibabacloud-cms-alert-rule-create` | 280 | Cloud Monitor alert rules |
| `alibabacloud-network-reachability-analysis` | 270 | Network path analysis |
| `alibabacloud-oss-manage-cron-upload` | 256 | OSS scheduled upload management |
| `alibabacloud-cfw-exposure-detection` | 249 | Cloud Firewall exposure detection |
| `alibabacloud-ecs-code-deploy` | 242 | Code deployment to ECS |
| `alibabacloud-governance-evaluation-report` | 233 | Cloud governance evaluation reports |
| `alibabacloud-cfw-ips-event` | 231 | Cloud Firewall IPS events |

The remaining 250 cover Flink, Hologres, Elasticsearch, PolarDB, KMS secrets, DataWorks workspaces, DTS migrations, AnalyticDB, and dozens more product-scoped operations.

## Quick Start

1. Install only the skills for services you use - `--skill` installs keep the surface small
2. Most skills need Alibaba Cloud credentials (AccessKey via CLI or environment)
3. `alibabacloud-find-skills` is the entry point: ask it to find the right skill for a cloud task

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Cloud ops reference** | 270 product-scoped operational skills is the most complete vendor pattern for wrapping cloud APIs in agent instructions - a template for any multi-service integration |
| **China-region infrastructure** | For operators running Alibaba Cloud (or evaluating it), these skills make agent-driven ECS/RDS/SLS operations feasible |
| **RAG and data ops** | Bailian RAG knowledge base and DataWorks skills cover the Qwen/Aliyun AI stack for data-heavy users |

## Limitations / Verification

- **Two audit Warnings:** the flagship skill renders Socket Warn and Snyk Warn - review-first, especially given the suite size.
- **No LICENSE file:** the repo ships no LICENSE file (verified Sep 11, 2026). Flag for legal before redistribution.
- **270-skill surface:** broad installs pull a very large instruction surface; per-skill install is strongly recommended.
- **Credential scope:** skills operate real cloud resources - scope AccessKeys tightly before letting an agent use them.

```bash
# Verify skill installed
ls ~/.hermes/skills/alibabacloud-sls-query/SKILL.md
```

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Warn |
| Snyk | Warn |

## Related

- [Alibaba Open Code Review - AI Code Review CLI Setup](/docs/hermes/skills/catalog/alibaba-open-code-review-setup)
- [Microsoft Azure Skills - Cloud Platform Setup](/docs/hermes/skills/catalog/microsoft-azure-skills-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
