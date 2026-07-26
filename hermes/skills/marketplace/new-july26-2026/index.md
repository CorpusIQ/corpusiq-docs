---
title: "New Skills — July 26, 2026 Marketplace Sweep"
description: "6 new enterprise publishers, 6 setup guides created, ~146K+ combined installs. Enterprise platform sweep of skills.sh for Hermes-relevant skills from Cloudflare, AWS, Google, HashiCorp, MongoDB, and Databricks."
---

# New Skills — July 26, 2026

## Summary

| Metric | Count |
|---|---|
| New publishers found | 6 |
| Setup guides created | 6 |
| Combined installs | ~146,000+ |
| Combined GitHub stars | 20,956 ⭐ |
| Quality: 🟢 Production | 5 |
| Quality: 🟡 Beta | 1 |
| Quality: 🔵 Community | 0 |

## New Skills

### Platform / Edge Computing

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Cloudflare Skills** | cloudflare/skills | 100K+ | 2,481⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/cloudflare-skills-setup/) |

### Cloud Infrastructure

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **AWS Agent Toolkit** | aws/agent-toolkit-for-aws | 4.3K+ | 2,119⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/aws-agent-toolkit-setup/) |
| **Google Skills** | google/skills | 30K+ | 15,250⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/google-skills-setup/) |

### Infrastructure / DevOps

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **HashiCorp Agent Skills** | hashicorp/agent-skills | 3.2K+ | 759⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/hashicorp-agent-skills-setup/) |

### Database / Data Infrastructure

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **MongoDB Agent Skills** | mongodb/agent-skills | 3.5K+ | 163⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/mongodb-agent-skills-setup/) |

### Data & AI Platform

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Databricks Agent Skills** | databricks/databricks-agent-skills | 798+ | 225⭐ | 🟡 | [Setup Guide](/hermes/skills/catalog/databricks-agent-skills-setup/) |

## 🔑 Standout Finds

### cloudflare/skills (100K+ installs, 2,481⭐)
The highest-install platform skills publisher on skills.sh. Cloudflare's Wrangler CLI (39.4K installs), Workers Best Practices (32.7K), and Web Performance (28.9K) are the top-three most-installed platform-specific skills across any publisher. The Agents SDK and MCP server deployment skills are directly applicable to Hermes agent infrastructure at the edge.

### google/skills (30K+ installs, 15,250⭐)
The largest enterprise skills collection on skills.sh with 75+ skills spanning Google Cloud, GKE, Gemini AI, BigQuery, Ads, and Analytics. The 15K GitHub stars make it the most-starred skills repository documented to date. Gemini API skills (4.5K installs) provide direct access to Google's most capable models for Hermes agent reasoning.

### aws/agent-toolkit-for-aws (4.3K+ installs, 2,119⭐)
AWS's official agent toolkit with 19 core skills for IAM, CDK, serverless, containers, and Bedrock AI. The IAM skill (4.3K installs) is the most-installed platform infrastructure skill. Directly applicable to provisioning and managing CorpusIQ's AWS infrastructure through agent-native workflows.

## Other Highlights

- **hashicorp/agent-skills** (3.2K installs): Terraform skills for infrastructure-as-code. Essential for Hermes agents managing multi-cloud infrastructure with version-controlled, declarative configurations.
- **mongodb/agent-skills** (3.5K installs): Vector search, natural language querying, and MCP server setup for MongoDB. Key for agent semantic memory and real-time stream processing.
- **databricks/databricks-agent-skills** (798+ installs): Delta Live Tables, Unity Catalog, and model serving for enterprise data and AI workloads. Beta tier but strong foundation for data-intensive agent operations.

## Discovery Method

Enterprise publisher sweep: searched skills.sh by owner for all major cloud and infrastructure platforms (cloudflare, aws, google, hashicorp, mongodb, databricks, microsoft, stripe, vercel, supabase, nvidia). Cross-referenced 11 publishers against 310 existing catalog entries. Confirmed 6 new publishers not previously catalogued. Skipped microsoft (low install counts, niche), stripe (already catalogued), vercel (already catalogued), supabase (already catalogued), and nvidia (specialized AI/ML only).

## Notes

- This sweep specifically targeted enterprise platform publishers that previous sweeps (focused on broad search terms) had missed. The owner-scoped search approach revealed high-value skills from major platforms.
- **cloudflare/skills** has the highest combined install count (100K+) of any single publisher documented outside of the top community packages (like obra/superpowers at 1.2M).
- **google/skills** at 75+ skills and 15K stars is the most comprehensive agent skills collection from any single platform vendor.
- **microsoft** has skills (vscode, aspire-skills, skills-for-fabric, win-dev-skills) but all had fewer than 200 installs each — deprioritized pending install growth.
- **nvidia/skills** (1.6K installs) covers Jetson, TAO, and NeMo but is specialized for hardware and ML research — deferred for a future AI/ML-specific sweep.
- 310 catalog entries now exist (up from 304 after this sweep).
