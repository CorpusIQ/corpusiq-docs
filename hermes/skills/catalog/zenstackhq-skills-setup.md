---
title: "ZenStack Skills - TypeScript Database Toolkit Setup Guide"
description: "zenstackhq/skills: 9 ZenStack V3 agent skills for schema modeling, access control, querying, CRUD APIs and migrations - 4.7K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zenstackhq-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "typescript", "zenstack", "orm"]
---

# ZenStack Skills - TypeScript Database Toolkit Setup Guide

**Source:** [zenstackhq/skills](https://www.skills.sh/zenstackhq/skills) via skills.sh - 4.7K combined installs across 9 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [zenstackhq/skills](https://github.com/zenstackhq/skills) - 3 stars, MIT license, main branch, last pushed Oct 28, 2026; nine skills under `skills/<name>/SKILL.md`, each with a `references/` folder of distilled ZenStack documentation.
**Category:** Backend Data and Access Control
**Quality Tier:** 🟢 Green - all 9 sampled verdicts Pass across Gen Agent Trust Hub, Socket and Snyk.

ZenStack is a TypeScript database toolkit that layers a built-in access-control engine and an automatic CRUD service on top of a Prisma-compatible ORM. The `zenstackhq/skills` collection teaches AI coding agents to build with ZenStack V3 correctly and idiomatically, rather than guessing at ZModel syntax, access policies, migrations or plugin APIs. It installs through the `skills` CLI in the Agent Skills format, so the guidance works across Claude Code, Cursor, Codex, Copilot and other hosts.

The repository ships nine skills, each a directory with a SKILL.md file plus a `references/` folder of plain-markdown ZenStack docs, so an agent can read the full documentation offline. The skills cover the whole lifecycle: setting up a project, modeling a `.zmodel` schema, querying and mutating data, enforcing access control, running database migrations, exposing automatic CRUD APIs, migrating from Prisma or ZenStack V2, and developing plugins. First seen in the Nov 20, 2026 evening sweep.

## Installation

```bash
npx skills add zenstackhq/skills
```

Install into your user or global directory so the skills are available across all projects:

```bash
npx skills add zenstackhq/skills -g
```

List the available skills without installing, then install only the ones you need for a specific agent:

```bash
npx skills add zenstackhq/skills --list
npx skills add zenstackhq/skills --skill zenstack-schema-modeling --skill zenstack-querying -a claude-code
```

Use a skill once without installing it, piping the generated prompt into your agent:

```bash
npx skills use zenstackhq/skills@zenstack-access-control | claude
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| zenstack-access-control | 556 | access policies (@@allow / @@deny), the auth() function, field-level and post-update rules |
| zenstack-db-migration | 551 | migrations: zen migrate dev/deploy/reset, db push/pull, seeding and deployment pipelines |
| zenstack-crud-server | 548 | automatic CRUD web APIs (Query as a Service), server adapters, OpenAPI and client SDKs |
| zenstack-plugin-dev | 521 | plugins: custom ZModel attributes, CLI code generators and runtime hooks |
| zenstack-migrate-from-prisma | 520 | convert an existing Prisma project to ZenStack V3 |
| zenstack-migrate-from-v2 | 515 | upgrade a ZenStack V2 project to V3 |
| zenstack-project-setup | 510 | install ZenStack, scaffold a project and run the zen CLI |
| zenstack-querying | 494 | the ZenStackClient, Prisma-compatible ORM API, relations, transactions and the Kysely query builder |
| zenstack-schema-modeling | 470 | author .zmodel schemas: models, relations, enums, mixins and typed JSON |

All 9 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

The biggest risk when an agent writes ZenStack code is guessing: ZModel syntax, access-policy semantics and the exact ZenStackClient API are easy to get subtly wrong, and a wrong access policy is a security bug, not a cosmetic one. These skills replace guesswork with current ZenStack V3 guidance, so an agent emits code that compiles against the real API. Access control is the standout: the zenstack-access-control skill walks through @@allow and @@deny policies, the auth() function and field-level rules, which matters because an agent that misplaces a policy can silently over-expose data. The querying and schema-modeling skills pin down the Prisma-compatible surface, so developers moving from Prisma get a faithful map rather than a hallucinated one. Because each skill bundles a references/ folder of stripped-down ZenStack docs, an agent can read the source material offline instead of inventing flag names. The migration skills give a scripted path for the two most common transitions: adopting ZenStack from plain Prisma, and upgrading from the older V2 line. For builders shipping a CRUD backend, zenstack-crud-server turns a schema into REST or RPC endpoints with per-request access control, which is the fastest route from model to API.

## Usage

| You say | What happens |
|---|---|
| Set up a new ZenStack V3 project with the zen CLI | Scaffolds the project, installs dependencies and walks through zen generate |
| Model users, posts and a many-to-many relation in ZModel | Produces a .zmodel schema with models, fields and relations |
| Add access control so only authors can update their own posts | Writes @@allow and @@deny policies with auth() and field-level rules |
| Expose this schema as a REST API with per-request auth | Generates automatic CRUD endpoints through a server adapter |
| Migrate my Prisma schema to ZenStack | Converts schema.prisma to ZModel and swaps the client |
| Query with joins and a transaction | Uses the Prisma-compatible API with select/include and interactive transactions |
| Upgrade this ZenStack V2 project to V3 | Renames packages, moves policies to the plugin and updates adapters |

## Verification

```bash
# after install, confirm the skills land in the project skills directory
npx skills add zenstackhq/skills --list
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/zenstackhq/skills/main/skills/zenstack-schema-modeling/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Each skill lives at `skills/<name>/SKILL.md` on the main branch with a `references/` folder alongside, so the nine skills install as plain directories under the project or user skills path.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| zenstack-access-control | Pass | Pass | Pass |
| zenstack-db-migration | Pass | Pass | Pass |
| zenstack-crud-server | Pass | Pass | Pass |
| zenstack-plugin-dev | Pass | Pass | Pass |
| zenstack-migrate-from-prisma | Pass | Pass | Pass |
| zenstack-migrate-from-v2 | Pass | Pass | Pass |
| zenstack-project-setup | Pass | Pass | Pass |
| zenstack-querying | Pass | Pass | Pass |
| zenstack-schema-modeling | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 4,685 combined installs across 9 indexed listings; 3 GitHub stars; MIT license; last pushed Oct 28, 2026. Counts drift over time.
- Small publisher: 3 stars and modest install counts mean less community scrutiny than larger ZenStack tooling, so review each skill before trusting it in production.
- Version coupling: all nine skills target ZenStack V3, so the guidance does not apply to V2 projects except through the migrate-from-v2 skill, and it will drift as V3 evolves.
- Prisma dependence: the skills assume a Prisma-style workflow, so projects that do not use Prisma or ZenStack get limited direct value.

## Related

- [Next.js Agent Skills - App Router Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Supabase Server Skills - Backend Data Setup](/hermes/skills/catalog/supabase-server-skills-setup)
- [Claude Code Next.js Skills - App Router Setup](/hermes/skills/catalog/claude-code-nextjs-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the skills your stack needs with --skill selectors; the full nine cover Prisma and V2 migrations you may not be using.
- Run zenstack-schema-modeling before zenstack-querying when starting from scratch, so the schema exists before the client code.
- Review the zenstack-access-control skill before exposing any API; a misplaced @@allow policy over-exposes data.
- Read a skill's references/ folder for the full distilled docs when the SKILL.md instruction is too compressed.
- Pin ZenStack versions in your project so the V3 guidance stays in sync with the installed runtime.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
