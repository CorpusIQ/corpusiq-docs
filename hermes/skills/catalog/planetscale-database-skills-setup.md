---
title: PlanetScale Database Skills — MySQL & Postgres for Hermes Agents
description: PlanetScale's official database agent skills — MySQL, Postgres, Vitess, Neki best practices. 15K+ combined installs across 4 skills for database-driven agent workflows.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/planetscale-database-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# PlanetScale Database Skills — Setup Guide

**Source:** [planetscale/database-skills](https://skills.sh/planetscale/database-skills) (15K+ combined installs)
**GitHub:** [planetscale/database-skills](https://github.com/planetscale/database-skills) (556 ⭐)
**Category:** Database / Infrastructure
**Quality Tier:** 🟢 Production

PlanetScale Database Skills is the official skills collection for working with databases through PlanetScale's platform. It covers MySQL best practices, Postgres deployment, Vitess sharding, and Neki — PlanetScale's agent-native database tooling. These skills teach Hermes agents how to design schemas, optimize queries, manage database workflows, and operate at scale.

---

## Installation

```bash
# Core database skills (highest installs)
npx skills add planetscale/database-skills --skill mysql
npx skills add planetscale/database-skills --skill postgres

# Advanced scaling
npx skills add planetscale/database-skills --skill vitess
npx skills add planetscale/database-skills --skill neki

# Agent operating model (from planetscale/skills repo)
npx skills add planetscale/skills --skill planetscale-mcp-agent-operating-model
npx skills add planetscale/skills --skill planetscale-best-practices-matrix
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **mysql** | 6.5K | MySQL best practices — schema design, query optimization, indexing, connection pooling |
| **postgres** | 6.2K | Postgres deployment and optimization — extensions, vacuuming, replication, performance tuning |
| **vitess** | 1.2K | Vitess sharding for MySQL at scale — VTGate, VTTablet, sharding keys, resharding workflows |
| **neki** | 1.2K | Neki — PlanetScale's agent-native database tooling for schema management and migrations |

---

## 🔑 Standout Features

### Dual Database Expertise (mysql + postgres)
PlanetScale is unique in offering deep skills for both MySQL and Postgres at near-identical install volumes (6.5K and 6.2K). Most database platforms bias heavily toward one engine — PlanetScale's balanced coverage makes these skills applicable regardless of database choice.

### Vitess at Scale
Vitess (1.2K installs) is the database clustering system that powers YouTube and scaled MySQL to millions of queries per second. The Vitess skill teaches agents how to shard, reshard, and manage horizontally-scaled MySQL — knowledge that's directly transferable to any large-scale database operation.

### Agent-Native Database Tooling (neki)
Neki is specifically designed for agent database workflows — schema management, safe migrations, and query optimization through agent-native interfaces rather than traditional CLIs.

---

## Hermes Agent Use Cases

- **Schema Design**: Generate optimized MySQL/Postgres schemas from application requirements
- **Query Optimization**: Analyze and optimize slow queries, add proper indexes, rewrite inefficient joins
- **Migration Management**: Plan and execute safe database migrations with rollback capability
- **Database Selection**: Evaluate MySQL vs Postgres for specific agent workloads
- **Scaling Planning**: Use Vitess knowledge to plan horizontal scaling strategies for growing datasets

---

## Discovery Method

Publisher sweep via `npx skills find "database" --owner "planetscale"`. PlanetScale was not previously catalogued in any sweep. Confirmed 4 skills across the database-skills repo plus additional agent-operating-model skills from the planetscale/skills repo.

---

## Notes

- **mysql** (6.5K) and **postgres** (6.2K) are the most balanced dual-database skills on skills.sh — unique in offering production-grade skills for both engines
- **vitess** is the only database sharding skill on skills.sh — directly applicable to CorpusIQ's scaling needs as user data grows
- **neki** represents the emerging category of "agent-native" database tooling — designed for AI agents rather than human operators
- PlanetScale's platform uses a git-like branching model for databases — conceptually aligned with Neon's approach and ideal for agent workflows
