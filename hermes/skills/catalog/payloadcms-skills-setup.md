---
title: "Payload CMS Skills - Schema and Migration Setup"
description: "payloadcms/skills on skills.sh: 9.1K combined installs across 2 listings; Payload schema, hooks, access control and content migration skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/payloadcms-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "payload cms", "nextjs", "cms migration"]
---

# Payload CMS Skills - Setup Guide

**Source:** [payloadcms/skills](https://www.skills.sh/payloadcms/skills) via skills.sh - 9.1K combined installs across 2 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 172 stars, no LICENSE file (the README states MIT), last pushed 2026-08-10, 2 SKILL.md directories under skills/
**Category:** Payload CMS development guidance for agents: collections, fields, hooks, access control, queries and content migration
**Quality Tier:** 🟡 Beta - no LICENSE file in the repository; every sampled audit Pass; 172 stars.

Payload is a Next.js native CMS with a TypeScript-first architecture, and its configuration surface is large: collections, field types, hooks, access control functions, database adapters, transactions and the Local, REST and GraphQL APIs. This repository carries two skills from the Payload team that cover the two jobs agents most often get wrong in a Payload project, building the config and moving content into it.

`payload` is a substantial skill, one SKILL.md plus a `reference/` directory of eleven topic files covering collections, fields, hooks, access control, advanced access control, queries, endpoints, adapters, plugin development and field type guards. `cms-migration` is an interactive workflow instead of a reference: it asks for a data sample, analyses the shape of the source data, and proposes Payload collection configs through conversation before any import runs.

## Installation

The README installs cross-agent through skills.sh, and the command covers both skills:

```bash
npx skills add payloadcms/skills
```

No per-skill install flag is documented for this repository. The README describes the skills as packaged instructions and scripts that extend agent capabilities, and points at `skills/payload/README.md` and `skills/cms-migration/SKILL.md` for the full documentation of each one.

## What It Provides

Two listings, both above the threshold.

| Skill | Installs | Use For |
|---|---|---|
| payload | 7,055 | Working in a Payload project: collections, fields, hooks, access control patterns, Local and REST and GraphQL queries, database adapters, jobs queue, endpoints, localization and plugins |
| cms-migration | 2,003 | Migrating content into Payload from WordPress, Contentful, Strapi, Sanity, Webflow or another CMS, starting from a data export |

No indexed listings fall below the threshold; all 2 appear above.

## Why This Matters for Hermes Agents

Payload config is where agents improvise most confidently and cause the most damage. A field named the wrong type, a hook attached to the wrong lifecycle method, or an access control function that quietly returns true all type-check and all ship. `payload` answers those from a reference set rather than from memory, and its quick reference table maps a task to the exact pattern and the exact file section: computed fields via `virtual: true` with a field-level `hooks.afterRead`, conditional fields via `admin.condition`, draft and publish via `versions: { drafts: true }`.

It also encodes the access control trap that catches almost every Payload project. The skill's quick reference is blunt about it: Local API user operations need `user` plus `overrideAccess: false`, because the default call path does not apply the access rules an agent assumes it does.

`cms-migration` handles the other half. Most failed CMS migrations fail before any data moves, because the source shape was never mapped properly. The skill is config-first: establish the collection structure through conversation, then import, and it carries the recurring ambiguities as named pitfalls, select versus relationship being the classic one, with rich text handling close behind.

Together they give an agent a defined starting order for a Payload build: collections and fields from the reference, access control decided per collection, then migration driven from real source data.

## Usage

| You say | What happens |
|---|---|
| "Add a posts collection with drafts and live preview" | payload writes the collection config with versioning and preview wiring |
| "This field should be computed, not stored" | payload adds a `virtual: true` field with a field-level `afterRead` hook |
| "Why does this hook not fire on update" | payload checks which lifecycle hook is in use and rewrites it to the right one |
| "Our API returns every user's records" | payload reviews the access control function and the `overrideAccess` setting on the Local API call |
| "Migrate our WordPress posts into Payload" | cms-migration asks for an export sample, maps fields and proposes collection configs |
| "Should this be a select or a relationship" | cms-migration resolves it against the source data pattern and the field reference |
| "Move our Sanity content across with the images intact" | cms-migration designs upload collections and relationship fields before the import |

## Verification

Read the skill file before installing, since its description is the trigger:

```bash
curl -fsSL https://raw.githubusercontent.com/payloadcms/skills/main/skills/payload/SKILL.md | head -4
```

It should open with `name: payload` and a description naming `payload.config.ts`, collections and fields. The reference files the skill routes to are fetchable too, which is the quickest way to check a specific pattern before trusting a summary:

```bash
curl -fsSL https://raw.githubusercontent.com/payloadcms/skills/main/skills/payload/reference/ACCESS-CONTROL.md | head -20
```

After installing, confirm both directories landed:

```bash
ls ~/.claude/skills | grep -E 'payload|cms-migration'
```

Two directories should appear. Check that the reference set came with the `payload` skill, because the skill is far less useful without it:

```bash
ls ~/.claude/skills/payload/reference
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| payload | Pass | Pass | Pass |
| cms-migration | Pass | Pass | Pass |

Both skills are markdown instructions and reference documents. The licensing position needs a look though: the repository ships no LICENSE file while its README ends with an MIT licence statement, so treat it as MIT by intent and confirm with the maintainers before redistributing the content.

## Limitations

- Snapshot data, verified 2026-11-05: 9,058 combined installs across 2 indexed listings; 172 GitHub stars; no LICENSE file in the repository, README states MIT; last pushed 2026-08-10. Counts drift over time.
- The license gap is unresolved upstream: no LICENSE file at the repo root, MIT claimed in the README. Get written clarification before vendoring or republishing these files.
- `payload` is large, a 518-line SKILL.md plus eleven reference files. Loading it costs context, so it earns its place on Payload work and wastes a window elsewhere.
- `cms-migration` is interactive by design: it asks for a data sample and iterates on collection configs. A fully autonomous run needs the export dropped in the repo and the sample path stated up front.
- Both skills assume Payload on Next.js with TypeScript, which is the architecture the skill describes. Older or non-Next.js Payload setups are outside what it documents.
- Install counts are heavily skewed to `payload` at 7,055 against 2,003 for the migration workflow, so the migration path has less field testing behind it.

## Related

- [Sanity Agent Toolkit - Headless CMS Setup](/hermes/skills/catalog/sanity-agent-toolkit-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the reference file, not the whole skill. `reference/ACCESS-CONTROL.md` is a cheaper and more precise read than "how does Payload access control work".
- Decide access control per collection before writing hooks. Retrofitting it after the API surface exists is where the `overrideAccess` mistakes come from.
- Run `cms-migration` with a real export in the repository. The workflow's first step is a data sample, and a described sample produces guessed field types.
- Watch the select versus relationship call on migration. A source field that looks like a tag list is often a relationship that later needs its own collection.
- Keep migrations off production credentials until the collection configs are agreed. The skill's config-first order exists so imports happen once, against a settled schema.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
