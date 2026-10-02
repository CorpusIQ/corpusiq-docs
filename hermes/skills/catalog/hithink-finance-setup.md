---
title: "Hithink Finance - Tonghuashun A-Share Data Skill Setup"
description: "hithink-tech/financial-api - 2 skills, 1.8K combined installs. Official agent entry to Tonghuashun (同花顺), China's largest retail-investor financial data platform - real-time and historical A-share quotes, fundamentals, indices, and limit-up boards via API, MCP, CLI, or Python."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hithink-finance-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "finance"]
---

# Hithink Finance - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/hithink-tech/financial-api) (1.8K combined installs)
**GitHub:** [hithink-tech/financial-api](https://github.com/hithink-tech/financial-api) (2,077⭐, MIT)
**Category:** Financial Data & Market Intelligence
**First Seen:** July 10, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

Tonghuashun (同花顺) is China's dominant retail-investor financial data platform - the iFinD vendor's consumer counterpart and the most-installed A-share data brand in the country. This is the vendor's official agent entry point: natural-language routing ("查一下贵州茅台今天的价格") into real-time quotes, historical K-line data, financial reports, index constituents, sector data, and limit-up (涨停) boards, with API, MCP, CLI, and Python access modes. The strongest complement to the already-documented Wind cluster: Wind covers institutional research, Hithink covers retail-grade A-share market data.

---

## Installation

```bash
npx skills add hithink-tech/financial-api --skill hithink-finance
```

The skill is a routing layer: it identifies the data task from natural language, probes available capabilities, and dispatches to the matching access mode (API / MCP / CLI / Python). SKILL.md content is Simplified Chinese - the agent must be able to follow Chinese-language contracts.

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| hithink-finance | 1.8K | Unified router for all Tonghuashun financial data tasks |
| financial-api | 1 | Low-level API contract reference |

## Prerequisites

- Tonghuashun developer credentials (iFinD/Hithink account) for data access
- A-share data access terms apply for mainland-China market data
- No Python package install required for CLI/API mode; Python mode uses the vendor SDK

## CorpusIQ Use Cases

- **Finance-vertical intelligence** - retail-grade A-share data (limit-up boards, sector rotation, real-time quotes) fills the gap Wind's institutional cluster leaves open for finance-focused CorpusIQ operators
- **Data-connector reference architecture** - the dual MCP + REST + CLI + Python exposure pattern is a reference for CorpusIQ's own multi-connector product surface
- **China-market operations** - operators tracking Chinese suppliers, customers, or competitors get agent-native access to listed-company fundamentals

## Limitations / Verification

- SKILL.md and data contracts are Chinese-language; English-only agents need a translation pass before first use
- Data access requires vendor credentials - the skill routes correctly without them but cannot fetch data
- Verify install: `npx skills list | grep hithink-finance`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/hithink-tech/financial-api/hithink-finance/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/hithink-tech/financial-api/hithink-finance/security/socket) · [Snyk: Pass](https://www.skills.sh/hithink-tech/financial-api/hithink-finance/security/snyk)

## Related

- [Wind Skills - 82-Skill Financial Terminal Cluster](/hermes/skills/catalog/wind-skills-setup)
