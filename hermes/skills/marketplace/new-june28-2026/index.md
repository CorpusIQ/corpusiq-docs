---
title: "New June 28, 2026 — Threads Growth Skill, NemoClaw User Guide, Huawei Hermes Deployment"
description: "3 newly discovered skills — Threads growth automation (745 installs), NemoClaw security user guide (99 installs), Huawei Cloud Hermes deployment (43 installs)"
---

# New Skills Discovered — June 28, 2026

**Sources:** [skills.sh](https://skills.sh) API sweep (14 queries across 5 ecosystem repos)
**Total new:** 3 skills | **Highlight:** Threads Growth Skill (745 installs from aradotso/marketing-skills)

Three skills surfaced in a late-night API sweep that weren't covered by existing catalog pages: a Threads growth/marketing skill with 745 installs, NVIDIA's NemoClaw security guide for Hermes/OpenClaw agents, and a Huawei Cloud deployment template for Hermes on Flexus servers.

---

## ⭐ Standout Find: Threads Growth Skill (745 installs)

**Repo:** [aradotso/marketing-skills](https://github.com/aradotso/marketing-skills)
**Installs:** 745 | **Publisher:** aradotso (same org as hermes-skills, 50+ Hermes skills)

A Threads growth and marketing automation skill for Hermes agents. Part of the aradotso marketing-skills collection — the same publisher behind the hermes-skills ecosystem (50+ Hermes-native skills). Enables agents to execute Threads growth strategies, content scheduling, and audience engagement.

```bash
npx skills add aradotso/marketing-skills --skill threads-growth-skill
```

**Why it matters for CorpusIQ:** Directly applicable to CorpusIQ's growth operations. Threads is Meta's fastest-growing platform with 200M+ users. This skill lets Hermes agents execute Threads growth strategies autonomously — content publishing, engagement automation, and audience analytics. Combined with existing social media skills (X/Twitter, LinkedIn, Instagram), this completes the Meta social stack.

> See [full setup guide →](/hermes/skills/catalog/threads-growth-skill-setup/)

---

## 🔒 NemoClaw User Guide (99 installs)

**Repo:** [nvidia/skills](https://github.com/nvidia/skills)
**Installs:** 99 | **Publisher:** NVIDIA

A security-focused user guide for NemoClaw — a hardened OpenClaw variant for Hermes agents. Covers security best practices, permission models, and safe deployment patterns for autonomous agent workflows.

```bash
npx skills add nvidia/skills --skill nemoclaw-user-guide
```

**Why it matters:** NVIDIA's entry into the Hermes/OpenClaw skill ecosystem signals enterprise validation. NemoClaw addresses the security concerns that enterprises have about autonomous agents — permission gates, audit logging, and secure execution boundaries. For CorpusIQ operators running production agent workflows, this provides a security baseline from a trusted enterprise vendor.

> See [full setup guide →](/hermes/skills/catalog/nemoclaw-user-guide-setup/)

---

## ☁️ Huawei Cloud Flexus — Hermes Deployment (43 installs)

**Repo:** [huaweicloud/huaweicloud-skills](https://github.com/huaweicloud/huaweicloud-skills)
**Installs:** 43 | **Publisher:** Huawei Cloud

A deployment template for running Hermes Agent on Huawei Cloud Flexus L-series servers. Includes ARM64 support, Docker Compose configuration, and cloud-specific optimizations. Part of a broader Huawei Cloud skills collection that also includes OpenClaw deployment (54 installs) and JiuwenSwarm deployment (44 installs).

```bash
npx skills add huaweicloud/huaweicloud-skills --skill huawei-cloud-flexus-l-server-hermes-deployment
```

**Why it matters:** Expands Hermes deployment options into the Huawei Cloud ecosystem — the third-largest cloud provider globally. For CorpusIQ operators targeting Asian markets or running on Huawei infrastructure, this provides a tested production deployment path. The broader huaweicloud-skills collection (5+ skills) suggests growing Hermes adoption in the Chinese cloud ecosystem.

> See [full setup guide →](/hermes/skills/catalog/huawei-hermes-deployment-setup/)

---

## Installation Summary

```bash
# Threads Growth Skill — 745 installs
npx skills add aradotso/marketing-skills --skill threads-growth-skill

# NemoClaw User Guide — 99 installs
npx skills add nvidia/skills --skill nemoclaw-user-guide

# Huawei Hermes Deployment — 43 installs
npx skills add huaweicloud/huaweicloud-skills --skill huawei-cloud-flexus-l-server-hermes-deployment
```

---

## Impact Assessment

**Threads Growth Skill** is the standout find at 745 installs — it fills the Threads gap in CorpusIQ's social media automation stack and comes from the trusted aradotso publisher (same org behind 50+ Hermes skills).

**NemoClaw User Guide** signals NVIDIA's entry into the Hermes security ecosystem — enterprise-grade security guidance for autonomous agent deployments.

**Huawei Hermes Deployment** opens Hermes to the #3 global cloud provider, particularly relevant for Asian market expansion and ARM64 production deployments.

---

*← [June 27 Discovery](/hermes/skills/marketplace/new-june27-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
