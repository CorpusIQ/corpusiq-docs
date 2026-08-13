---
title: Google Skills — Official Google Agent Skills for Hermes Agents
description: Google's official agent skills collection — Cloud recipes, GKE, Gemini APIs, BigQuery, agent platform, and Google Ads/Analytics. 30K+ combined installs across 75+ skills. 15K+ GitHub stars.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/google-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Google Skills — Setup Guide

**Source:** [google/skills](https://skills.sh/google/skills) (30K+ combined installs)
**GitHub:** [google/skills](https://github.com/google/skills) (15,250 ⭐)
**Category:** Platform / Cloud & AI
**Quality Tier:** 🟢 Production

Google Skills is the official agent skills collection for Google products and technologies. With 75+ skills spanning Google Cloud, GKE, Gemini AI, BigQuery, Ads, Analytics, and the Agent Platform, this is the single largest publisher of enterprise-grade agent skills on skills.sh. These skills teach Hermes agents how to provision cloud infrastructure, manage Kubernetes clusters, query petabyte-scale datasets, run AI inference, and orchestrate AI agents on Google's platform.

---

## Installation

```bash
# Cloud recipes (highest installs)
npx skills add google/skills --skill google-cloud-recipe-onboarding
npx skills add google/skills --skill google-cloud-recipe-auth
npx skills add google/skills --skill google-cloud-recipe-foundation-builder

# Gemini AI
npx skills add google/skills --skill gemini-interactions-api
npx skills add google/skills --skill gemini-api
npx skills add google/skills --skill gemini-agents-api
npx skills add google/skills --skill gemini-live-api

# GKE (Kubernetes)
npx skills add google/skills --skill gke-basics
npx skills add google/skills --skill gke-cluster-creation
npx skills add google/skills --skill gke-workload-security

# BigQuery and analytics
npx skills add google/skills --skill bigquery-basics
npx skills add google/skills --skill bigquery-ai-ml

# Agent Platform
npx skills add google/skills --skill agent-platform-deploy
npx skills add google/skills --skill agent-platform-eval-flywheel

# CLI
npx skills add google/skills --skill gcloud

# Ads and Analytics (growth operations)
npx skills add google/skills --skill google-ads-api-quickstart
npx skills add google/skills --skill google-analytics-data-api-basics
```

---

## Included Skills (Top 25 by Relevance)

### Cloud Recipes (9.4K installs each)
| Skill | Installs | Purpose |
|---|---|---|
| **google-cloud-recipe-onboarding** | 9.4K | New Google Cloud project setup with best practices, billing, and IAM |
| **google-cloud-recipe-auth** | 9.0K | Authentication patterns for cloud applications and service accounts |
| **google-cloud-recipe-foundation-builder** | — | Enterprise landing zone with security, networking, and compliance |

### Gemini AI
| Skill | Installs | Purpose |
|---|---|---|
| **gemini-interactions-api** | 4.5K | Gemini API interactions including multimodal prompts, streaming, and function calling |
| **gemini-api** | — | Core Gemini API with text, code, image, and audio generation |
| **gemini-agents-api** | 3.6K | Build AI agents with Gemini: tool use, memory, and multi-step reasoning |
| **gemini-live-api** | — | Real-time bidirectional streaming with Gemini for voice and video |

### GKE (Kubernetes Engine) — 20+ skills
| Skill | Installs | Purpose |
|---|---|---|
| **gke-basics** | — | GKE fundamentals: clusters, node pools, workloads, and services |
| **gke-cluster-creation** | — | Cluster provisioning with best-practice configurations |
| **gke-workload-security** | — | Pod security, network policies, and workload identity |
| **gke-inference** | — | Deploy AI inference workloads on GKE with GPU and TPU support |
| **gke-cost-optimization** | — | Spot VMs, committed use discounts, and resource right-sizing |

### BigQuery and Analytics
| Skill | Installs | Purpose |
|---|---|---|
| **bigquery-basics** | — | SQL queries, partitioning, clustering, and performance optimization |
| **bigquery-ai-ml** | — | BigQuery ML for in-database model training and prediction |
| **bigquery-bigframes** | — | BigQuery DataFrames for pandas-compatible analytics at scale |

### Agent Platform
| Skill | Installs | Purpose |
|---|---|---|
| **agent-platform-deploy** | — | Deploy AI agents with managed infrastructure, monitoring, and scaling |
| **agent-platform-eval-flywheel** | — | Continuous evaluation pipeline for agent quality and performance |
| **agent-platform-rag-engine-management** | — | Manage RAG knowledge bases with automated indexing and retrieval |
| **agent-platform-skill-registry** | — | Centralized skill registry for multi-agent orchestration |
| **agent-platform-prompt-management** | — | Version-controlled prompt templates with A/B testing |

### Ads and Analytics
| Skill | Installs | Purpose |
|---|---|---|
| **google-ads-api-quickstart** | — | Google Ads API for campaign management, reporting, and optimization |
| **google-analytics-data-api-basics** | — | GA4 Data API for user behavior analysis and attribution |
| **google-analytics-admin-api-basics** | — | GA4 Admin API for property configuration and user management |

### Additional Highlights
| Skill | Installs | Purpose |
|---|---|---|
| **gcloud** | 3.9K | gcloud CLI for all Google Cloud operations |
| **google-cloud-solution-rag-enterprise-search** | — | RAG architecture with Vertex AI Search and GKE |
| **google-cloud-storage-basics** | — | Cloud Storage for object storage with lifecycle management |
| **firebase-basics** | — | Firebase for mobile and web app backends |
| **cloud-run-basics** | — | Serverless container deployment with Cloud Run |
| **alloydb-basics** | — | AlloyDB for PostgreSQL-compatible managed database |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Google Cloud account** | Free tier with $300 credits at https://cloud.google.com/free |
| **gcloud CLI** | `curl https://sdk.cloud.google.com | bash` or package manager |
| **Google Cloud project** | Create via `gcloud projects create` or Cloud Console |
| **Authentication** | `gcloud auth login` for user creds or service account key |
| **Node.js 18+** | Required for some skills |

---

## Key Capabilities

### Gemini AI Integration
Direct access to Google's most capable models through the Gemini API. Skills cover multimodal prompting (text, image, audio, video), function calling for tool use, streaming responses, and building autonomous agents with memory and reasoning. The `gemini-live-api` skill enables real-time bidirectional communication for voice and video agents.

### Agent Platform
Google's managed AI agent platform provides deployment, evaluation flywheels, RAG engine management, skill registries, and prompt management. This is the infrastructure layer for running production AI agents at scale. The eval flywheel enables continuous quality monitoring across agent deployments.

### GKE for AI Workloads
Twenty-plus GKE skills cover everything from cluster creation to GPU and TPU inference deployment. GKE provides the compute substrate for large-scale agent operations with autoscaling, workload identity, and cost optimization patterns.

### BigQuery Analytics
Petabyte-scale SQL analytics with built-in ML capabilities. BigQuery ML enables training and deploying models directly on your data warehouse. BigFrames provides a pandas-compatible DataFrame API that translates to BigQuery SQL.

### Growth Operations
Google Ads and Analytics skills directly support CorpusIQ growth operations. The Ads API enables programmatic campaign management and optimization. GA4 Data API provides user behavior analysis for attribution and conversion tracking.

---

## Quick Start

```bash
# 1. Install gcloud CLI and authenticate
gcloud auth login

# 2. Add the cloud onboarding recipe
npx skills add google/skills --skill google-cloud-recipe-onboarding

# 3. Add Gemini interactions for AI capabilities
npx skills add google/skills --skill gemini-interactions-api

# 4. Add gcloud CLI skill
npx skills add google/skills --skill gcloud
```

---

## Hermes Integration Notes

- **Agent hosting:** Deploy CorpusIQ agents on Agent Platform with managed infrastructure and continuous evaluation
- **AI inference:** Use Gemini API as an alternative model backend for Hermes agent reasoning tasks
- **Data warehouse:** BigQuery for storing and analyzing growth metrics, session data, and user behavior
- **Growth analytics:** GA4 Data API for attribution modeling and conversion tracking across CorpusIQ channels
- **Advertising ops:** Google Ads API for managing paid acquisition campaigns programmatically
- **Infrastructure:** GKE for running agent workloads with GPU and TPU acceleration

---

## Links

- **skills.sh:** https://skills.sh/google/skills
- **GitHub:** https://github.com/google/skills
- **Google Cloud Docs:** https://cloud.google.com/docs
- **Gemini API Docs:** https://ai.google.dev/gemini-api/docs
- **Agent Platform:** https://cloud.google.com/agent-platform
