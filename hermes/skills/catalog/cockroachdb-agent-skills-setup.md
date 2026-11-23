---
title: "CockroachDB Agent Skills - Operational Database Setup"
description: "CockroachDB agent skills spanning onboarding, development, performance, resilience, observability and security - 4.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cockroachdb-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "database", "postgres", "distributed-sql"]
---

# CockroachDB Agent Skills - Operational Database Setup

**Source:** [cockroachlabs/cockroachdb-skills](https://www.skills.sh/cockroachlabs/cockroachdb-skills) via skills.sh - 4.3K combined installs across 34 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [cockroachlabs/cockroachdb-skills](https://github.com/cockroachlabs/cockroachdb-skills) - 24 stars, Apache-2.0, main branch, last pushed Jul 22, 2026; skills are nested under nine domain directories as skills/<domain>/<skill>/SKILL.md.
**Category:** Distributed SQL Database Operations
**Quality Tier:** 🟡 Yellow - 2 Warn cells (Snyk on profiling-statement-fingerprints and triaging-live-sql-activity) and no Fail cells across the 20-skill sample.

CockroachDB Skills is a curated collection of structured, machine-executable capabilities that encode CockroachDB expertise for AI agents, automation systems and developer tools. The skills are organized into nine operational domains spanning the full database lifecycle: onboarding and migrations, application development, performance and scaling, operations and lifecycle, resilience and disaster recovery, observability and diagnostics, security and governance, integrations and ecosystem, and cost and usage management. Each skill is a directory containing a SKILL.md with frontmatter and structured content, and the repository validates every skill against the Agent Skills Specification in CI.

What makes the suite notable is its design discipline. The README states that each skill addresses one specific task with clear boundaries, uses progressive disclosure so core concepts come before edge cases, adds guardrails by default on anything that can modify data or availability, and links to official CockroachDB documentation rather than duplicating it. Most skills describe SQL-only procedures that work without DB Console access, and the one-line install claims compatibility with Claude Code, Cursor, Windsurf and 40+ other agents.

## Installation

Install the full set through the skills CLI:

```bash
npx skills add cockroachlabs/cockroachdb-skills
```

The repository also ships a 5-minute installation guide at docs/installation.md and a usage guide at docs/usage.md for discovering and invoking individual skills. Skills can be validated locally with:

```bash
python scripts/validate-spec.py skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cockroachdb-sql | 162 | writing and optimizing CockroachDB SQL and schema design |
| designing-application-transactions | 135 | correct transaction patterns: retries, locking and pessimistic reads |
| auditing-table-statistics | 134 | checking optimizer statistics for staleness and coverage |
| analyzing-range-distribution | 134 | finding hotspots and uneven range distribution with SHOW RANGES |
| reviewing-cluster-health | 132 | tier-appropriate cluster health checks |
| hardening-user-privileges | 132 | tightening roles, admin grants and PUBLIC permissions |
| benchmarking-transaction-patterns | 132 | comparing multi-statement versus single-statement transactions |
| analyzing-schema-change-storage-risk | 132 | estimating backfill storage before schema changes |
| monitoring-background-jobs | 131 | tracking failed, paused and long-running jobs |
| profiling-statement-fingerprints | 131 | ranking slow or error-prone statements from statistics |
| profiling-transaction-fingerprints | 131 | finding high-retry transactions and contention |
| managing-tls-certificates | 130 | CA config, client certs, rotation and SSL troubleshooting |
| auditing-cloud-cluster-security | 130 | assessing security posture across network, auth and encryption |
| triaging-live-sql-activity | 129 | finding long-running queries and busy sessions live |
| managing-cluster-settings | 129 | reviewing and modifying cluster settings by tier |
| configuring-audit-logging | 128 | SQL audit logging for auth and privilege events |
| performing-cluster-maintenance | 127 | planned maintenance and node drain procedures |
| molt-verify | 126 | comparing source and target databases after migration |
| designing-multi-region-applications | 126 | choosing multi-region patterns like REGIONAL BY ROW |
| managing-cluster-capacity | 125 | scaling nodes, compute and cost across tiers |
| configuring-private-connectivity | 125 | PrivateLink and VPC peering for private access |
| configuring-log-export | 125 | exporting logs and metrics to CloudWatch or Datadog |
| configuring-ip-allowlists | 125 | restricting access to authorized CIDR ranges |
| provisioning-cluster-for-production | 125 | initial provisioning and production deployment |
| molt-fetch | 124 | migrating data from PostgreSQL, MySQL, Oracle or MSSQL |
| enforcing-password-policies | 124 | minimum length, complexity and hash cost rules |
| configuring-sso-and-scim | 124 | SSO authentication and SCIM 2.0 provisioning |
| managing-certificates-and-encryption | 124 | TLS and encryption key lifecycle, including CMEK rotation |
| molt-replicator | 123 | continuous CDC replication after a molt fetch |
| enabling-cmek-encryption | 122 | customer-managed encryption keys on the Advanced plan |
| preparing-compliance-documentation | 122 | SOC 2, PCI, ISO 27001, HIPAA and GDPR evidence |
| upgrading-cluster-version | 120 | tier-appropriate version upgrades |
| setting-up-local-cluster | 115 | downloading and starting a local cluster for development |

The remaining 1 indexed listing is auditing-cis-benchmark at 84 installs.

## Why This Matters for Hermes Agents

An agent that operates CockroachDB without these skills reaches for generic PostgreSQL advice that misses distributed-database specifics: sequential primary keys that create write hotspots, transaction retry storms that need a retry loop with backoff, or schema-change backfills that exhaust disk mid-flight. The highest-value skill is cockroachdb-sql, the umbrella for writing schema and query patterns that account for primary keys, type mappings and distributed best practices, followed by the observability skills that diagnose performance through SQL-only interfaces when DB Console access is unavailable. The security and governance block is unusually deep: privilege hardening, TLS, audit logging, CMEK, SSO and SCIM, IP allowlists and compliance documentation each get a dedicated skill with tier-specific guidance. For an operator the guardrails matter most: the README requires safety checks and rollback guidance on anything that can modify data or availability, which is exactly where a coding agent is most likely to cause damage.

## Usage

| You say | What happens |
|---|---|
| Install CockroachDB skills | Adds cockroachlabs/cockroachdb-skills through the skills CLI |
| Set up a local cluster for development | Uses setting-up-local-cluster to download and start the binary |
| Migrate from PostgreSQL | Uses molt-fetch, molt-replicator and molt-verify for load, CDC and checks |
| Why is my cluster slow right now? | Uses triaging-live-sql-activity to find long-running queries live |
| Why does my transaction keep retrying? | Uses profiling-transaction-fingerprints to find contention |
| Lock down cluster access | Uses hardening-user-privileges and configuring-ip-allowlists |
| Prepare for a SOC 2 audit | Uses preparing-compliance-documentation and auditing-cloud-cluster-security |

## Verification

Confirm the repository README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/cockroachlabs/cockroachdb-skills/main/README.md | head -40
```

Confirm the SQL umbrella skill body is present before relying on it for schema and query guidance:

```bash
curl -sL https://raw.githubusercontent.com/cockroachlabs/cockroachdb-skills/main/skills/cockroachdb-query-and-schema-design/cockroachdb-sql/SKILL.md | head -30
```

Confirm the cluster health skill body is present before using it for a health review:

```bash
curl -sL https://raw.githubusercontent.com/cockroachlabs/cockroachdb-skills/main/skills/cockroachdb-operations-and-lifecycle/reviewing-cluster-health/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cockroachdb-sql | Pass | Pass | Pass |
| designing-application-transactions | Pass | Pass | Pass |
| auditing-table-statistics | Pass | Pass | Pass |
| analyzing-range-distribution | Pass | Pass | Pass |
| reviewing-cluster-health | Pass | Pass | Pass |
| hardening-user-privileges | Pass | Pass | Pass |
| benchmarking-transaction-patterns | Pass | Pass | Pass |
| analyzing-schema-change-storage-risk | Pass | Pass | Pass |
| monitoring-background-jobs | Pass | Pass | Pass |
| profiling-statement-fingerprints | Pass | Pass | Warn |
| profiling-transaction-fingerprints | Pass | Pass | Pass |
| managing-tls-certificates | Pass | Pass | Pass |
| auditing-cloud-cluster-security | Pass | Pass | Pass |
| triaging-live-sql-activity | Pass | Pass | Warn |
| managing-cluster-settings | Pass | Pass | Pass |
| configuring-audit-logging | Pass | Pass | Pass |
| performing-cluster-maintenance | Pass | Pass | Pass |
| molt-verify | Pass | Pass | Pass |
| designing-multi-region-applications | Pass | Pass | Pass |
| managing-cluster-capacity | Pass | Pass | Pass |

Two Snyk Warns (profiling-statement-fingerprints and triaging-live-sql-activity) and no Fail across the 20 sampled skills; 14 of the 34 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 4,318 combined installs across 34 indexed listings; 24 GitHub stars; Apache-2.0; last pushed Jul 22, 2026. Counts drift over time.
- The install band is flat: the 33 in-table skills range only from 115 to 162 installs, and most sit between 120 and 135, so ordering within the table carries little quality signal.
- The one listing not shown in the table above, auditing-cis-benchmark, sits at 84 installs, clearly below the rest of the band.
- 14 of the 34 indexed listings carry no published security verdict in the sampled set.
- The nine domain directories in the tree include four (performance and scaling, resilience and disaster recovery, integrations and ecosystem, cost and usage management) that currently hold only a placeholder, so the indexed skill set does not yet span all nine domains the README names.

## Related

- [Neon Postgres Skills - Database Design and Performance](/hermes/skills/catalog/neon-postgres-skills-setup)
- [PlanetScale Database Skills - MySQL & Postgres](/hermes/skills/catalog/planetscale-database-skills-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read cockroachdb-sql first: it encodes the anti-patterns (missing primary keys, sequential ID hotspots, wrong type usage) that shape every other skill's advice.
- Prefer the SQL-only observability skills when DB Console access is unavailable, since most diagnose through system tables and SHOW statements.
- Run analyzing-schema-change-storage-risk before any CREATE INDEX or ALTER PRIMARY KEY on a large table to avoid mid-backfill disk exhaustion.
- Chain the migration skills in order: molt-fetch loads, molt-replicator sets up CDC, then molt-verify checks schema and row consistency.
- Every skill is tier-aware (Self-Hosted, Advanced, Standard, Basic), so confirm which tier you are on before following a procedure.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
