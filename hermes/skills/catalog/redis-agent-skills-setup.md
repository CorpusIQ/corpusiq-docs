---
title: "Redis Agent Skills - Official Data Modeling & Caching Setup"
description: "Redis' official agent skill collection: data modeling, semantic caching, connections, security, observability, clustering, and search. 19.9K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/redis-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-01"
tags: ["hermes skill", "agent skill", "skill setup", "redis", "database", "caching", "data"]
---

# Redis Agent Skills - Setup Guide

**Source:** [redis/agent-skills](https://github.com/redis/agent-skills) (163⭐, MIT)
**Skill family:** `redis/agent-skills` (12 indexed skills)
**Combined Installs:** ~19,866 across indexed listings (Oct 1, 2026 snapshot)
**Category:** Data / Infrastructure
**Quality Tier:** 🟡 Trusted (official Redis, Inc. publisher; MIT LICENSE in-repo; low star count for an official org)

Redis ships an official collection of agent skills covering the operational decisions that agents most often get wrong: choosing the right data structure, client/connection strategy, security posture, and observability. The skills are authored by Redis, Inc. (`author: Redis, Inc.` in each SKILL.md) and carry per-skill MIT licenses. The cluster includes AI-focused guidance (`iris-development`, `redis-semantic-cache`) alongside classic data-modeling and cluster-operation skills.

---

## Installation

```bash
npx skills add redis/agent-skills
```

## Roster - Indexed Skills

| Skill | Installs | What It Does |
|---|---|---|
| redis-core | 3,337 | Data-structure modeling - String, Hash, List, Set, Sorted Set, JSON, Stream, Vector Set |
| redis-development | 3,258 | Umbrella plugin entry for the Redis development skill set |
| redis-connections | 2,375 | Connection pooling, multiplexing, pipelining, RESP3 client-side caching |
| redis-security | 2,055 | auth (requirepass/ACL users), TLS, least-privilege ACL, network exposure |
| redis-observability | 1,967 | Metrics to monitor, built-in commands, diagnosing memory/connection issues |
| redis-semantic-cache | 1,645 | Redis LangCache - semantic caching of LLM responses on Redis Cloud |
| redis-clustering | 1,583 | Cluster/replication, hash tags, avoiding CROSSSLOT, reading from replicas |
| iris-development | 1,451 | Iris (Redis AI umbrella) - Agent Memory (RAM) data plane on Redis Cloud |
| redis-search | 1,308 | FT.CREATE schema design, field types, DIALECT 2 queries, vector search |
| redis-query-engine | 453 | Query engine guidance |
| redis-vector-search | 433 | Vector search guidance |
| redis-best-practices | 1 | Best-practices stub (minimal installs) |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Cache design | redis-semantic-cache + redis-core to plan an LLM response cache and key model |
| Agent memory | iris-development for Redis Agent Memory as an agent's long-term store |
| Production hardening | redis-security + redis-observability before shipping a Redis-backed service |
| Search/vector | redis-search + redis-vector-search for hybrid RAG retrieval on Redis |

## Limitations / Verification

- skills.sh indexing verified Oct 1, 2026: 12 skills indexed; 8 SKILL.md files verified via raw.githubusercontent on branch `main`.
- Repo has 16 SKILL.md files: each skill is duplicated under `skills/` and `plugins/redis-development/skills/` (plugin layout). Not all skills are indexed on skills.sh.
- Star count (163) is low for an official org repo - the "Trusted" tier reflects the **publisher identity** (Redis, Inc.), not community traction. Verify before relying in production.
- No live install test performed; install counts are from the Oct 1, 2026 sweep snapshot.

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
