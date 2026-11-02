---
title: "Encore Skills - Backend Service Development Setup"
description: "encoredev/skills: 16.8K combined installs. Encore agent skills for typed APIs, Postgres, Pub/Sub, cron and deploys in Go and TypeScript."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/encore-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "backend", "encore", "go", "typescript"]
---

# Encore Skills - Setup Guide

**Source:** [encoredev/skills](https://www.skills.sh/encoredev/skills) via skills.sh - 16.8K combined installs across 40 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [encoredev/skills](https://github.com/encoredev/skills) - 30 stars, Apache-2.0 with a `LICENSE` file in the root, branch main, last pushed 2026-10-26; 38 `SKILL.md` directories under `encore/`, one per skill, with a Claude Code plugin manifest under `plugins/encore-skills/`

**Category:** Backend services for agents: Encore.ts and Encore.go APIs, databases, queues and infrastructure from code

**Quality Tier:** 🟡 Beta - Apache-2.0, current, and Markdown only, with every sampled verdict a Pass except one Snyk warning, but 30 stars is thin adoption for a 16.8K install base

Encore is a backend framework for Go and TypeScript where the code declares the infrastructure: you ask for a database, a Pub/Sub topic or a cron job in source, and Encore provisions it. This repository is the vendor's own skill set for that framework, published by the Encore team, and it mirrors the documentation for both languages side by side. Thirty-eight skills ship in the tree, split almost evenly between the TypeScript and Go families, with six setup skills and one architecture skill covering both.

The setup chain is the part that makes the pack usable unattended. `encore-install` installs or updates the CLI and the Docker and Node dependencies, `encore-login` handles sign-in including a browserless auth key, `encore-link-app` joins a local app to Encore Cloud, `encore-create-app` scaffolds one without prompts, `encore-run` starts it and checks it, and `encore-mcp` connects an AI tool to the local and cloud MCP servers. That is a complete path from a machine without Encore to a running service.

Each skill is a single `SKILL.md` with a `description` and a `when_to_use` block full of trigger phrases, so routing is described in the file rather than inferred. The repository also ships `AGENTS.md` and `CLAUDE.md` with a table of trigger keywords per skill, which is a useful thing to read once before you rely on the routing.

## Installation

The README's command installs the whole set:

```bash
npx skills add encoredev/skills
```

It documents the variants as well: list first, install specific skills, target specific agents, or install globally:

```bash
npx skills add encoredev/skills --list
npx skills add encoredev/skills --skill encore-getting-started --skill encore-api
npx skills add encoredev/skills -a cursor -a claude-code
npx skills add encoredev/skills -g
```

The README says this works with Cursor, Claude Code, Codex, OpenCode and more than ten other agents. Nothing in the repository mentions Hermes, but the payload is Markdown, so a Hermes profile skills directory takes the same folders.

The Claude Code marketplace route is documented too, and this repository carries the manifest it needs:

```bash
claude plugin marketplace add encoredev/skills
claude plugin install encore-skills@encore-skills
```

The manual route from the README is to copy the `SKILL.md` files from `encore/` into your agent's skills directory. Note that the directory names are the short form (`api`, `go-api`, `code-review`) while the skill names in the frontmatter carry the prefix (`encore-api`, `encore-go-api`, `encore-code-review`), so copy the folders rather than flattening them:

```bash
git clone https://github.com/encoredev/skills.git /tmp/encore-skills-src
mkdir -p ~/.hermes/profiles/corpusiq/skills
for skill in /tmp/encore-skills-src/encore/*; do
  [ -f "$skill/SKILL.md" ] || continue
  destination="$HOME/.hermes/profiles/corpusiq/skills/encore-$(basename "$skill")"
  [ -e "$destination" ] || cp -R "$skill" "$destination"
done
```

Local development then needs Docker, because `encore run` provisions Postgres and Redis containers on your machine. Production goes two ways: Encore Cloud provisions into your own AWS or GCP account, or you self-host with the generated infrastructure configuration.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| encore-api | 849 | Typed TypeScript endpoints with `api(...)`: request and response interfaces, path, query, header and cookie params, request validation and `APIError`. |
| encore-auth | 841 | Protecting endpoints: `authHandler`, `Gateway`, `getAuthData` and the `auth: true` option. |
| encore-service | 839 | Service implementation and project layout: `encore.service.ts`, service directories, systems and typed calls through `~encore/clients`. |
| encore-code-review | 839 | Reviewing existing Encore.ts code for best practices and common anti-patterns. |
| encore-database | 819 | PostgreSQL from Encore.ts with `SQLDatabase`: schema migrations and SQL queries. |
| encore-testing | 807 | Tests with `encore test` and vitest or jest, including isolated per-test databases and calling handlers directly. |
| encore-frontend | 783 | Connecting a React, Next.js, Vue or Svelte frontend to an Encore.ts backend. |
| encore-migrate | 745 | Moving an existing backend onto Encore through a DISCOVER, PLAN, MIGRATE workflow tracked in `migration-plan.md`, targeting either language. |
| encore-getting-started | 690 | Encore.ts from scratch: install the CLI, log in, create an app, check it runs and connect MCP, ending where building starts. |
| encore-go-auth | 577 | Go endpoint authentication: `auth.AuthHandler`, `auth.UserID`, the Authorization header and `//encore:api auth`. |
| encore-go-testing | 576 | Tests with `encore test` and the standard `testing` package, including isolated per-test databases and `*testing.T` patterns. |
| encore-go-service | 575 | Go service packages, internal subpackages, systems and typed service calls. |
| encore-go-api | 575 | Go endpoints via `//encore:api` annotations: typed request and response structs, params and error returns. |
| encore-go-database | 573 | PostgreSQL from Encore Go with `sqldb.NewDatabase`, migrations and queries. |
| encore-go-code-review | 573 | Reviewing Encore Go code for best practices and common anti-patterns. |
| encore-go-getting-started | 539 | Encore Go from scratch, the same install, login, create, run and MCP path as the TypeScript starter. |
| encore-secret | 438 | API keys, credentials and signing secrets through `secret(...)` from `encore.dev/config`. |
| encore-cron | 436 | Periodic work with `CronJob`: interval syntax such as `every: "1h"` and cron expressions such as `schedule: "0 9 * * 1"`. |
| encore-cache | 436 | Redis caching with `CacheCluster` and typed keyspaces: TTLs, atomic increments and per-keyspace data shapes. |
| encore-pubsub | 435 | Async messaging with `Topic` and `Subscription`: broadcast events, decouple producers from consumers, run background handlers. |
| encore-bucket | 435 | Object storage with `Bucket`: uploads, images, documents and blobs. |

The remaining 19 indexed listings range from 16 to 434 installs.

The tail starts one install under the cut, at `encore-webhook` (434), which covers inbound webhooks through `api.raw(...)`, and it runs down through the Go infrastructure skills (`encore-go-secret`, `encore-go-pubsub`, `encore-go-bucket`, `encore-go-cron`, `encore-go-cache`) to the operational skills: `encore-deploy` (33), `encore-run`, `encore-mcp`, `encore-login`, `encore-link-app`, `encore-install` and `encore-create-app` (16 each). The low counts on the setup skills are worth reading carefully, because those are the ones an agent needs first.

The index is two rows wider than the tree. `encore-infrastructure` (331) and `encore-go-infrastructure` (211) carry install counts but have no matching directory under `encore/`, so the coverage they describe is not in this snapshot.

## Why This Matters for Hermes Agents

Infrastructure is where an agent guesses most expensively. Told to add a database, a general-purpose agent writes connection strings, a Docker compose file and a migration runner, and the result works on one machine. Encore's model is that the declaration is the API: `SQLDatabase` or `sqldb.NewDatabase` creates the resource, and the skill's job is to write the declaration correctly instead of hand-rolling the plumbing.

The paired language families are the useful detail. Twelve feature skills exist twice, once as `encore-<feature>` for TypeScript and once as `encore-go-<feature>` for Go, and each pair sits a few hundred installs from its twin. An agent working across both languages does not have to translate guidance from one to the other, and `encore-architecture` covers the decision that comes before either: where the service boundaries are and who owns which data.

The setup chain is what makes this a candidate for unattended work. Install, login with an auth key, link or create an app, run it, then check it with `encore check` before anything is committed. That last step matters more than it sounds, because it is a real compile-and-wire check rather than a model's opinion that the code looks right.

The risk profile is operational rather than code execution. The pack ships no scripts at all, so installing it cannot run anything, but the skills do instruct the agent to run CLI commands that create apps, deploy to your cloud account and hold credentials. A skill that can create infrastructure in your AWS or GCP account is a skill worth scoping before you let it run without a human in the loop.

## Usage

| You say | What happens |
|---|---|
| "Set up Encore on this machine" | encore-install finds or installs the CLI, checks Docker and Node, and fixes PATH problems, then encore-login signs in with a browser or an auth key. |
| "Add a typed endpoint at POST /orders" | encore-api writes the `api(...)` handler with a typed request and response, params, validation and the right `APIError` for the failure cases. |
| "Create a Postgres table for orders with a migration" | encore-database declares the `SQLDatabase`, adds the schema migration and writes the query layer. |
| "Fan these events out to background workers" | encore-pubsub declares a `Topic` and `Subscription`, then moves the processing into the subscription handler. |
| "Run the app and tell me why it will not start" | encore-run starts it locally, reads the startup error, fixes the cause and re-checks with `encore check`. |
| "Protect these endpoints behind auth" | encore-auth wires `authHandler` and `auth: true`, and hands the caller identity to the handler through `getAuthData`. |
| "Move our Express backend onto Encore" | encore-migrate runs DISCOVER, PLAN, MIGRATE, tracks the plan in `migration-plan.md` and ports services to Encore.ts or Encore Go. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-11-02:

```bash
for p in api secret migrate; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/encoredev/skills/main/encore/$p/SKILL.md"
done
```

After a clone, count the tree and read one skill's routing block. The `when_to_use` field is what the agent matches on, so it is the field worth reviewing:

```bash
git clone --depth 1 https://github.com/encoredev/skills.git /tmp/encore-skills
find /tmp/encore-skills/encore -name SKILL.md | wc -l
sed -n '1,6p' /tmp/encore-skills/encore/api/SKILL.md
head -20 /tmp/encore-skills/AGENTS.md
```

The count should be 38. The `sed` prints the `name`, `description` and `when_to_use` of the API skill, and `AGENTS.md` carries the same trigger keywords in a table across every skill, which is the fastest way to see whether the routing you expect is the routing you will get.

The README's own `--list` flag is a network check rather than a file check, and it is the one the vendor documents:

```bash
npx skills add encoredev/skills --list
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| encore-api | Pass | Pass | Pass |
| encore-go-testing | Pass | Pass | Pass |
| encore-bucket | Pass | Pass | Pass |
| encore-logging | Pass | Pass | Pass |
| encore-create-app | Pass | Pass | Warn |

Four of the five sampled listings pass all three auditors. `encore-create-app` is the single Snyk warning, and it is also the skill that scaffolds a new application and can register or clone an existing one against your Encore Cloud account, so the warning sits on the skill with the widest reach into your infrastructure rather than on the safest one.

What lands on disk is the smallest surface in this set: 41 Markdown files, two JSON manifests, one `LICENSE`, and no scripts at all. There is no executable, no dependency install and no post-install step, so nothing runs when the pack is cloned. Each skill directory holds exactly one `SKILL.md`.

The real risk is what the instructions ask the agent to run. These skills drive the `encore` CLI, which provisions Docker containers locally and infrastructure in your own cloud account, and they handle login credentials and secrets through the CLI. If you are running them unattended, scope the cloud credentials the agent can reach, and keep `encore-secret` and `encore-login` behind a review rather than a cron job.

## Limitations

- Snapshot data, verified 2026-11-02: 16,784 combined installs across 40 indexed listings; 30 GitHub stars; Apache-2.0; last pushed 2026-10-26. Counts drift over time.
- The index is two rows wider than the tree: `encore-infrastructure` (331) and `encore-go-infrastructure` (211) carry install counts but have no matching directory under `encore/` in this snapshot.
- Nothing in the repository mentions Hermes. The documented surfaces are Cursor, Claude Code, Codex, OpenCode and the Claude Code plugin marketplace, and the skills assume you are working inside an Encore project.
- Local development needs Docker for `encore run` to provision Postgres and Redis, so the first run is heavier than a Markdown install suggests.
- Production needs an Encore Cloud account to provision into your AWS or GCP account, or a self-hosted setup built from the generated infrastructure configuration. `encore-deploy` and `encore-login` both assume that account exists.
- The setup skills carry the lowest install counts in the pack, at 16 each, so they are the least exercised part of the suite even though they are the first thing an agent needs.

## Related

- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [NestJS Best Practices - 40-Rule Agent Skill Setup Guide](/hermes/skills/catalog/agent-nestjs-skills-setup)
- [M. Collina Node Skills - Fastify & Node.js Agent Suite Setup](/hermes/skills/catalog/mcollina-node-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `encore-getting-started` plus the one or two feature skills you need. The starter skill points at the others step by step, so a partial install still has a working path from a bare machine to a running app.
- Read `AGENTS.md` before you trust the routing. It lists the trigger keywords for all 38 skills in one table, which is the cheapest way to see which skill will pick up a phrase like "not logged in" or "port in use".
- Run `encore check` after every change, not just before a commit. It compiles and wires the app, and it catches the class of mistake a model cannot see by reading its own code.
- Keep the Go and TypeScript families straight by prefix. The directories are short names (`api`) while the skills are prefixed (`encore-api`, `encore-go-api`), and installing a folder under the wrong name is the easiest way to lose a skill silently.
- Treat the setup skills as a reviewed chain, not a cron job. They log in, create apps and register infrastructure in your cloud account, and the pack's own sampling flags `encore-create-app`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
