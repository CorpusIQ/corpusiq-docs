---
title: Databricks Agent Skills — Data & AI Platform Skills for Hermes Agents
description: Databricks' official agent skills collection — apps, pipelines, lakehouse, model serving, and vector search. 798+ combined installs across 6 skills for building on the Databricks Data Intelligence Platform.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/databricks-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Databricks Agent Skills — Setup Guide

**Source:** [databricks/databricks-agent-skills](https://skills.sh/databricks/databricks-agent-skills) (798+ combined installs)
**GitHub:** [databricks/databricks-agent-skills](https://github.com/databricks/databricks-agent-skills) (225 ⭐)
**Category:** Data & AI Platform
**Quality Tier:** 🟡 Beta

Databricks Agent Skills is the official skills collection for the Databricks Data Intelligence Platform. It covers Databricks Apps, Delta Live Tables pipelines, Unity Catalog lakehouse management, model serving, vector search for RAG, and execution compute. These skills teach Hermes agents to build, deploy, and manage data and AI workloads on Databricks.

---

## Installation

```bash
# Core platform skills
npx skills add databricks/databricks-agent-skills --skill databricks-apps
npx skills add databricks/databricks-agent-skills --skill databricks-pipelines
npx skills add databricks/databricks-agent-skills --skill databricks-lakebase

# AI and ML
npx skills add databricks/databricks-agent-skills --skill databricks-model-serving
npx skills add databricks/databricks-agent-skills --skill databricks-vector-search

# Compute
npx skills add databricks/databricks-agent-skills --skill databricks-execution-compute
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **databricks-apps** | 798 | Databricks Apps — build and deploy data applications with native authentication |
| **databricks-pipelines** | 681 | Delta Live Tables — declarative ETL pipelines with quality enforcement |
| **databricks-lakebase** | 612 | Unity Catalog lakehouse — governed data and AI asset management |
| **databricks-model-serving** | 501 | Model serving endpoints for real-time and batch inference |
| **databricks-vector-search** | 180 | Vector search indexes for RAG and semantic search applications |
| **databricks-execution-compute** | 83 | Compute configuration for jobs, clusters, and SQL warehouses |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Databricks workspace** | Free trial at https://www.databricks.com/try-databricks |
| **Databricks CLI** | `pip install databricks-cli` or `brew install databricks-cli` |
| **Workspace access token** | Generate at User Settings > Developer > Access Tokens |
| **Python 3.9+** | Required for Databricks SDK and PySpark |

---

## Key Capabilities

### Databricks Apps
Build data applications that run natively on Databricks with built-in authentication, compute, and data access. Apps can be dashboards, APIs, or full web applications backed by Databricks SQL warehouses or serverless compute.

### Delta Live Tables
Declarative ETL pipeline framework with automatic data quality enforcement, schema evolution, and incremental processing. Define expectations for data quality and get automatic monitoring and alerting when quality rules are violated.

### Unity Catalog Lakehouse
Centralized governance for data and AI assets. Manage tables, views, volumes, models, and functions with fine-grained access control. Enable data discovery with tags and lineage tracking.

### Model Serving
Deploy ML models as REST endpoints for real-time inference. Support for MLflow models, foundation models from Databricks Marketplace, and custom LLM deployments. Auto-scaling and GPU acceleration for production inference.

### Vector Search
Create and query vector indexes for semantic search and RAG. Integrate with Databricks embedding models. Power retrieval-augmented generation pipelines with managed vector infrastructure.

---

## Quick Start

```bash
# 1. Install Databricks CLI
pip install databricks-cli

# 2. Configure authentication
databricks configure --token

# 3. Add the core skills
npx skills add databricks/databricks-agent-skills --skill databricks-lakebase
npx skills add databricks/databricks-agent-skills --skill databricks-pipelines
```

---

## Hermes Integration Notes

- **Data pipelines:** Delta Live Tables for CorpusIQ growth data pipelines with automated quality enforcement
- **Vector memory:** Databricks Vector Search as a managed vector store for agent semantic memory
- **Model serving:** Deploy fine-tuned models for growth prediction and lead scoring behind REST endpoints
- **Data governance:** Unity Catalog for managing CorpusIQ's data assets with fine-grained access control
- **Compute management:** Execution compute skills for optimizing Spark jobs that process social media and analytics data

---

## Links

- **skills.sh:** https://skills.sh/databricks/databricks-agent-skills
- **GitHub:** https://github.com/databricks/databricks-agent-skills
- **Databricks Docs:** https://docs.databricks.com
- **Unity Catalog:** https://docs.databricks.com/data-governance/unity-catalog
