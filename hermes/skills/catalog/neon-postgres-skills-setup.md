---
title: "Neon Postgres Skills - Database Design and Performance"
description: "neondatabase/postgres-skills on skills.sh: 2.5K combined installs; 2 indexed skills covering Postgres design, indexing and query tuning"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/neon-postgres-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "postgres", "neon", "database", "sql"]
---

# Neon Postgres Skills - Setup Guide

**Source:** [neondatabase/postgres-skills](https://www.skills.sh/neondatabase/postgres-skills) via skills.sh - 2.5K combined installs across 2 indexed listings; first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 55 stars, Apache-2.0 via LICENSE, `main` branch, last pushed 2026-10-06, 2 SKILL.md files (`skills/postgres-best-practices` and `.agents/skills/skill-creator`), plugin manifests under `.claude-plugin/`, README.md at the repository root
**Category:** Databases: Postgres schema design, indexing, query performance and connection handling
**Quality Tier:** 🟡 Solid with caveats - Apache-2.0 official Neon skills, but one Fail verdict in the two sampled listings.

Neon publishes this repository as a curated Postgres corpus rather than a product integration. There is no Neon API skill, no connection-string helper and nothing that requires you to run on Neon: the README states the goal as vendor-agnostic guidance for Postgres users regardless of provider, and the content is commissioned from named practitioners. The README names Stas Kelvich, a Neon cofounder and long-time Postgres contributor, and Jonathan Katz of the PostgreSQL core team, as reviewers, and states that contributions are paid. It also states an AI policy: skills must be written by humans, with AI tools allowed for review and testing only.

The suite is effectively one skill. `postgres-best-practices` is the substantive listing: a `SKILL.md` entry point plus 13 reference files, one per topic area, covering schema design, indexing, query optimization, query patterns, performance diagnostics, connection pooling, bulk loading, backup and restore, hot standby, logical replication, major version upgrades, transaction isolation and security roles. The skill body states that it covers PostgreSQL 14 through 18 and tags version-specific features, for example `[PG15+]` and `[PG18+]`. The second indexed listing is `skill-creator`, a generic guide to authoring skills that sits in `.agents/skills/` and is mirrored into `.claude/skills/` and `.cursor/skills/` as a symlink. It is not Postgres content.

That split matters more than the install counts suggest, and it is the first thing to understand before installing: two listings, one Postgres skill.

## Installation

The README documents one command and nothing else:

```bash
npx skills add neondatabase/postgres-skills
```

That takes both skills. To take only the Postgres content, name it explicitly:

```bash
npx skills add neondatabase/postgres-skills --skill postgres-best-practices
```

The repository also ships `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, which describe a plugin called `postgres-skills` that points at `./skills/`, but the README does not document a plugin install command. Use the `npx` route above and treat the manifests as packaging metadata rather than instructions.

There is nothing to configure. The skill is markdown and reference files, it makes no network calls of its own, and it does not need a Neon account, a connection string or an API key. Its guidance applies to any Postgres 14 to 18 deployment, which is why the install is a single command with no follow-up step.

What you get on disk is one skill directory with a `SKILL.md` and a `references/` folder holding the 13 topic files. The design is progressive disclosure: the entry point routes to a reference file when a task matches its area, so an agent working on an index does not load the replication notes. That is the main reason the skill stays useful in a small context window despite covering ten subject areas.

## What It Provides

The threshold for this guide is zero installs, so both indexed listings appear below with the install integers exactly as skills.sh reports them:

| Skill | Installs | Use For |
|---|---|---|
| postgres-best-practices | 2,038 | Schema design, indexing strategy, query optimization, migrations, connection pooling and common Postgres pitfalls, with version-tagged guidance for PostgreSQL 14 through 18 |
| skill-creator | 443 | Authoring or updating a skill: structure, frontmatter, progressive disclosure and packaging scripts, with no Postgres content of its own |

Both rows are above zero, so nothing is summarised away. The gap between 2,038 and 443 is the clearest signal in the pack: people install the Postgres skill, and the skill-authoring skill travels along because it is in the same repository and the default command installs everything.

The depth is in the references rather than the entry point. The 13 files are `schema-design`, `indexing`, `query-optimization`, `query-patterns`, `performance-diagnostics`, `connection-pooling`, `bulk-loading`, `backup-restore`, `hot-standby`, `logical-replication`, `major-version-upgrades`, `transaction-isolation` and `security-roles`. Each one is a self-contained note, which is what makes the skill usable as a review checklist rather than only as generation guidance: an agent can open `indexing.md` while reviewing an existing migration and leave the rest unread.

The version table in the entry point is worth noting for a different reason. It lists initial release and end of life for PostgreSQL 14 through 18, with 14 ending in November 2026, 15 in November 2027, 16 in November 2028, 17 in November 2029 and 18 in November 2030, and it states that PostgreSQL provides five years of support per major version with the latest minor always recommended. That is a maintenance schedule an agent can act on, not just background reading.

## Why This Matters for Hermes Agents

Hermes agents write a lot of SQL, and the failure mode is rarely syntax. It is a missing index on a foreign key, a `text` column where a `timestamptz` belonged, a migration that takes an exclusive lock on a large table at peak, or a connection pool configured for a serverless runtime that opens a new connection per invocation. These are judgement errors that a model reproduces confidently, and a reference corpus is the cheapest correction available.

The progressive-disclosure structure is the part worth copying. One entry point with a routing table plus thirteen topic files gives an agent a small always-loaded surface and a deep library it can open on demand. That is a better fit for a coding agent than one enormous database guide, and it is a pattern that transfers to any domain where the knowledge is broad but the task is narrow.

The second transferable piece is the review framing. The skill is written as guidelines and pitfalls, with a diagnostics reference and a performance section, so it works when the agent is checking someone else's schema as well as when it is generating a new one. A Hermes agent that reviews migrations before they merge gets more value from this than one that only writes fresh DDL.

The third is the sourcing discipline. The README names its reviewers, states that contributions are paid, and forbids AI-authored content. For a domain where the difference between correct and plausible is a production incident, provenance is a feature: you can trace a recommendation to a practitioner with a public track record, which is more than most skill repositories offer.

The counterweight is coverage. This is one skill, and the licence covers the text rather than any guarantee of correctness. Treat it as a strong second opinion from experienced practitioners, not as an authority that overrides your own EXPLAIN output.

## Usage

| You say | What happens |
|---|---|
| "Review this schema before we ship it" | Walks the DDL against schema-design and indexing guidance, checking types, keys, constraints, normalization choices and missing indexes, and returns a prioritized list |
| "This query takes four seconds, make it fast" | Opens the query-optimization and performance-diagnostics references, proposes a plan-reading approach, index candidates and rewrite options rather than guessing at a fix |
| "We need to add a nullable column to a 50 million row table. Is that safe?" | Applies the migration guidance for the server version, explains lock behaviour and the safer patterns, and flags the version-specific options |
| "Should this be a JSONB column or a join table?" | Works through the schema-design trade-offs for the access pattern you describe, with the query-pattern notes on when each shape stops paying off |
| "Our connection count spikes under load" | Opens connection-pooling guidance, separates pool sizing from server limits and covers the pooling options that fit the runtime |
| "We are still on Postgres 14. What breaks first?" | Reads the support table and the major-version-upgrades reference, then sequences the upgrade with the version tags that apply |
| "Package our internal deploy checklist as a skill" | Uses the skill-creator guidance to shape the skill, write frontmatter and decide what belongs in `references/` versus the entry point |

## Verification

The layout is `skills/postgres-best-practices/SKILL.md`, and this fetch returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/neondatabase/postgres-skills/main/skills/postgres-best-practices/SKILL.md | head -8
```

It opens with YAML frontmatter holding `name: postgres-best-practices` and a description starting "Best practices and guidelines for working with Postgres", then the heading `# Postgres Best Practices` and a short statement of scope. The reference files sit beside it under `references/`, so the same path with `/references/indexing.md` appended should also return 200. A 404 on either means the layout moved.

After an install, confirm the skill landed in the directory your agent reads:

```bash
ls ~/.agents/skills | grep -E '^(postgres-best-practices|skill-creator)$'
ls ~/.claude/skills | grep -E '^(postgres-best-practices|skill-creator)$'
```

One line means you installed the Postgres skill only; two means the default command took both. If neither line returns anything, the CLI targeted a different agent than the one you are running.

The depth check is worth one command, because the reference folder is most of the value:

```bash
curl -fsSL "https://api.github.com/repos/neondatabase/postgres-skills/git/trees/main?recursive=1" | grep -c '"path": "skills/postgres-best-practices/references/'
```

That returns 13. Fewer means the checkout is partial or the references were reorganised.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| postgres-best-practices | Pass | Pass | Pass |
| skill-creator | Fail | Pass | Pass |

`postgres-best-practices` is clean on all three scanners, which fits what it is: markdown guidance with no scripts and no network calls. `skill-creator` carries a Gen Agent Trust Hub Fail while Socket and Snyk both pass. That combination is worth reading carefully rather than treating as a binary verdict: the skill ships three Python scripts (`init_skill.py`, `package_skill.py`, `quick_validate.py`) and a `LICENSE.txt` of its own under `.agents/skills/skill-creator/`, and it is a vendored copy of a skill maintained outside this repository. Read those scripts before running them, and install `postgres-best-practices` alone if you only want the Postgres content.

The operational risk in the Postgres skill is not code execution, it is advice applied to production. Guidance on index creation, `ALTER TABLE` behaviour, connection pooling and major version upgrades lands in migrations that run against real data. The skill states version tags for a reason: an option that is safe on PostgreSQL 16 may not exist on 14, and a pattern that helps on a primary can hurt on a hot standby. Have a human review any DDL the agent produces before it runs outside a scratch database, and take a backup before an upgrade path the skill recommends.

The repository is Apache-2.0, which includes an express patent grant and requires you to keep the licence and notices on redistribution. That is more permissive than a copyleft licence for internal use and safe to vendor into a product, provided the notice travels with the files.

## Limitations

- Snapshot data, verified 2026-11-09: 2,481 combined installs across 2 indexed listings; 55 GitHub stars; Apache-2.0; last pushed 2026-10-06. Counts drift over time.
- Only one of the two listings is Postgres content. `skill-creator` is a generic skill-authoring guide under `.agents/skills/`, mirrored into `.claude/skills/` and `.cursor/skills/`, so a headline figure of 2,481 installs overstates Postgres adoption by the 443 that belong to the meta skill.
- The README documents only `postgres-best-practices` in its Available Skills section. `skill-creator` is indexed by skills.sh and installable by name, but it is not described as part of the suite, and its own frontmatter points at a `LICENSE.txt` that exists only inside its own folder.
- Coverage is guidance, not verification. The references describe patterns; they do not run `EXPLAIN`, inspect your schema or check your version. An agent can apply a correct rule to the wrong situation, and nothing in the skill catches that.
- The suite is small and moves slowly: two skills, 55 stars, last push 2026-10-06, and the README's paid-contribution contact is a databricks.com address rather than a neon.tech one. Nothing in the repository explains that mismatch, so do not read the org name as a statement about who maintains the content day to day.
- Contributor affiliations are disclosed in the README (Neon cofounder, AWS product manager), which is good practice but also means platform-specific habits can appear in vendor-neutral guidance. Verify anything that reads like a hosting recommendation against your own deployment.

## Related

- [Neon Agent Skills - Serverless Postgres Platform](/hermes/skills/catalog/neon-agent-skills-setup)
- [dbt Agent Skills - Official dbt Labs Analytics Suite Setup](/hermes/skills/catalog/dbt-agent-skills-setup)
- [ClickHouse Agent Skills - Official Analytics Suite Setup](/hermes/skills/catalog/clickhouse-agent-skills-setup)

## Pro Tips

- Install `postgres-best-practices` by name. The default command also pulls `skill-creator`, which is a different job with a different verdict, and most Postgres work does not need it.
- Point the agent at a reference file rather than the entry point for review tasks. "Read `references/indexing.md` and audit this schema" produces a sharper answer than "use the postgres skill".
- Keep the version in the prompt. The skill tags features by major version, so telling the agent it is on 15 rather than 18 removes a whole class of wrong recommendations.
- Use it as a pre-merge reviewer, not an author. The references are at their best when checking DDL and query plans that already exist, because the agent has something concrete to compare against.
- Read the `security-roles` and `transaction-isolation` references before touching an agent that can run migrations. Those two areas are where a plausible suggestion becomes a permission or locking incident.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
