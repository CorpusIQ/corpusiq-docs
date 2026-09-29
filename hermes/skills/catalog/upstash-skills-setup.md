---
title: "Upstash Skills - Serverless Backend Setup"
description: "Official Upstash skills for Redis, Rate Limit, QStash and Workflow SDKs in Claude Code agents. 40k+ indexed installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/upstash-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "serverless", "redis"]
---

# Upstash Skills - Setup Guide

**Source:** [upstash/skills](https://github.com/upstash/skills) (27⭐)
**Skill family:** `upstash/skills` (6 installable skills)
**Combined Installs:** ~40,658 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

A collection of skills published by Upstash, the serverless data platform (official vendor), covering its main SDKs: Redis, rate limiting, QStash, and Workflow, plus a general Upstash pack and a CLI skill. Install counts are dominated by the Redis SDK guide (14,335) and the Rate Limit TypeScript SDK guide (13,969). All six skills were verified by the Sep 29, 2026 skills.sh sweep.

---

## Installation

```bash
npx skills add upstash/skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| upstash-redis-js | 14,335 | Complete skills guide for the Upstash Redis SDK |
| upstash-ratelimit-js | 13,969 | Guide for the Rate Limit TypeScript SDK |
| upstash | 2,670 | General Upstash platform skills |
| upstash-qstash-js | 1,591 | QStash JavaScript SDK guide |
| upstash-workflow-js | 1,469 | Upstash Workflow SDK guide |
| upstash-cli | - | Upstash CLI (install count not in snapshot) |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Agent state via Redis | Let agents follow upstash-redis-js patterns for serverless Redis state and caching. |
| Rate limiting | Apply upstash-ratelimit-js guidance when building throttle and quota logic. |
| Durable background jobs | Use upstash-qstash-js and upstash-workflow-js patterns for message queues and workflows. |

## Limitations / Verification

- Verified: skills.sh indexing of Sep 29, 2026 (6/6 skills; install counts as reported).
- Not verified: no live install test performed. The underlying services require an Upstash account.
- Star count (27) from the Sep 29, 2026 sweep.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
