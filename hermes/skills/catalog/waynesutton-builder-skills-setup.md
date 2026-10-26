---
title: "Wayne Sutton Builder Skills - Convex App Development Setup"
description: "Setup guide for waynesutton/builder-skills - 37.6K combined installs. 17 skills for building Convex apps plus a PRD-first project workflow loop."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/waynesutton-builder-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-19"
tags: ["hermes skill", "agent skill", "skill setup", "convex", "backend", "developer workflow"]
---

# Wayne Sutton Builder Skills - Setup Guide

**Source:** [waynesutton/builder-skills](https://www.skills.sh/waynesutton/builder-skills) via skills.sh - 37.6K combined installs across 18 indexed listings; first seen Oct 11, 2026 (evening sweep)
**GitHub:** [waynesutton/builder-skills](https://github.com/waynesutton/builder-skills) (406 stars, Apache-2.0 license; pushed Sep 28, 2026; `skills/<name>/SKILL.md` layout; 17 skills plus 2 starter templates)
**Category:** Backend Platform (BaaS) / Developer Workflow
**Quality Tier:** 🟡 Beta - opinionated single-maintainer suite (406 stars, Apache-2.0); active Sep 2026; all sampled verdicts Pass

Wayne Sutton ships 17 skills for builders working on Convex, the TypeScript-first backend platform. Thirteen teach an agent the documented Convex patterns - validators on every function, indexes over filters, idempotent mutations, signature-verified webhooks, zero-downtime migrations - each pointing at docs.convex.dev/llms.txt and pushing depth into references/ so the agent only loads what the task needs. The other four run the project: write a PRD before touching code, keep task.md, changelog.md, and files.md true from git evidence, avoid scope creep, and never run a git command that can destroy uncommitted work.

This is a distinct, opinionated set: the README says so directly ("This repo is my opinionated set, tuned for how I build"). The skills ship through three channels - skills.sh, a Claude Code plugin marketplace, and an npm CLI - and work with Claude Code, Codex, Cursor, OpenCode, and anything that reads a SKILL.md.

---

## Installation

Install with skills.sh (files land in your repo and stay editable):

```bash
npx skills add waynesutton/builder-skills

# later, pull author updates
npx skills update
```

Claude Code plugin (managed, auto-updating):

```bash
claude plugins marketplace add waynesutton/builder-skills
claude plugins install builder-skills@waynesutton
```

Or from inside a Claude Code session:

```text
/plugin marketplace add waynesutton/builder-skills
/plugin install builder-skills@waynesutton
```

npm CLI (default target is `.claude/skills`; use `--target codex|cursor|opencode` for others):

```bash
npx @waynesutton/builder-skills install-all
npx @waynesutton/builder-skills install-templates
```

## What It Provides

Install counts from the Oct 11, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| convex | 5,669 | Router for any Convex task; the rules that apply everywhere (validators, indexes, idempotency) |
| convex-best-practices | 3,894 | Production patterns and the rules the @convex-dev/eslint-plugin enforces |
| convex-functions | 3,175 | Queries, mutations, actions, and internal functions with arg and return validators |
| convex-schema-validator | 3,017 | Schema design: tables, validators, indexes, and relationships |
| convex-realtime | 2,877 | Reactive UIs: live queries, optimistic updates, pagination, and presence |
| convex-cron-jobs | 2,789 | Cron jobs and scheduled functions, batching, and cancellation |
| convex-http-actions | 2,728 | Webhooks with signature checks, REST-style routes, CORS, and streaming responses |
| convex-security-check | 2,718 | Ten-minute pre-merge security pass over a Convex backend |
| convex-file-storage | 2,645 | Upload URLs, blob storage, serving, metadata, and deletion |
| convex-migrations | 2,584 | Zero-downtime schema changes: optional fields, batched backfills, validator flips |
| convex-security-audit | 1,549 | Deep launch review: authorization model, per-table access paths, rate limiting |
| convex-agents | 1,457 | AI agents on the Convex agent component: threads, tools, streaming, and RAG |
| avoid-feature-creep | 1,247 | Keeps a change scoped; moves "while we are here" edits to a suggestions list |
| convex-component-authoring | 1,144 | Reusable components with defineComponent, client wrappers, and npm publish setup |

The remaining 4 indexed listings range from 1 to 68 installs (convex-eslint at 68 has no counterpart in the current tree; project-workflow, project-docs, and git-safety at 1 each).

## Why This Matters for Hermes Agents

Most platform skill sets are either the vendor's official library or a loose prompt dump; this one is a working developer's opinionated narrowing of a platform, and that shape has three lessons for agent builders. First, the rules-first design: every skill leads with the failure it prevents (filter instead of withIndex, missing returns validator, api.* instead of internal.*, Date.now() inside a cached query) and then points at the live docs for the current API, which keeps the skills from rotting as the platform changes. Second, the workflow skills encode a complete unattended loop - PRD, task tracking, changelog and file docs synced from git evidence, and a git-safety gate that forbids destructive commands without an explicit yes - and that loop is portable to any project an agent works on, Convex or not. Third, the packaging: seventeen small router skills with progressive disclosure beat one large prompt, and the same SKILL.md folders install across Claude Code, Codex, Cursor, and OpenCode. If you run agents against a Convex backend, this suite is a direct quality lift; if you do not, the four workflow skills still earn their place.

## Usage

| You say | What happens |
|---|---|
| "Add a webhook endpoint that verifies signatures" | convex-http-actions builds the convex/http.ts route with signature checks and CORS |
| "Review this backend before we merge" | convex-security-check runs a ten-minute pass: public functions, missing auth, unvalidated args |
| "Change this live table's schema without downtime" | convex-migrations: optional field, batched backfill, validator flip, cleanup |
| "Write a PRD before touching this feature" | project-workflow triages first, writes the PRD in prds/, and tracks it in task.md |
| "Sync the changelog with what actually shipped" | project-docs reads git log and the working tree, then updates changelog.md, files.md, and task.md |
| "Build a support agent with streaming and RAG" | convex-agents sets up threads, tool calls over queries and mutations, and vector search |
| "The agent keeps adding refactors I did not ask for" | avoid-feature-creep moves the extra edits to a suggestions list and keeps the change scoped |

## Verification

```bash
# In the project where you installed: confirm the skills landed
ls .claude/skills

# Review the router skill from GitHub before installing (path verified Oct 11, 2026)
curl -sL https://raw.githubusercontent.com/waynesutton/builder-skills/main/skills/convex/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Oct 11, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| convex | Pass | Pass | Pass |
| convex-realtime | Pass | Pass | Pass |
| convex-security-check | Pass | Pass | Pass |

## Limitations

- Convex-specific for 13 of the 17 skills; the workflow set (project-workflow, project-docs, git-safety, avoid-feature-creep) applies to any project.
- Independent set, not the official get-convex library: the README positions it as the author's opinionated tuning; review the patterns before adopting them wholesale.
- The install index outruns the tree slightly: convex-eslint is indexed on skills.sh (68 installs) with no matching directory in the current repo tree.
- install-templates writes starter files into your project root (AGENTS.md, task.md, changelog.md, files.md, prds/) and two editable skills; it does not overwrite existing files.
- Snapshot data, verified Oct 11, 2026: 37,564 combined installs across 18 indexed listings; 406 GitHub stars; Apache-2.0; last pushed Sep 28, 2026. Counts drift over time.

## Related

- [Convex Agent Skills - Backend Platform (BaaS) Setup](/hermes/skills/catalog/convex-agent-skills-setup) - the official Convex skill set; this guide's set is the independent, workflow-focused companion
- [Neon Agent Skills - Serverless Postgres Setup](/hermes/skills/catalog/neon-agent-skills-setup) - serverless database skills for a different backend stack
- [Supabase Agent Skills - Backend Platform Setup](/hermes/skills/catalog/supabase) - alternative backend-as-a-service skill set
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the convex router skill; it routes to the correct builder skill and carries the platform-wide rules.
- Pair the security skills: run convex-security-check before every merge and convex-security-audit before launch.
- Run install-templates once per project to get the PRD loop (prds/, task.md, changelog.md, files.md) plus the two editable house-style skills.
- Update later with npx skills update; the installed files stay yours to edit.
- The four workflow skills are not Convex-bound - reuse them on any repo you run agents against.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
