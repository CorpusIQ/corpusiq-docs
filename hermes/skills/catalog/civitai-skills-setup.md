---
title: "Civitai Skills - Open Source Platform Dev Workflows"
description: "civitai/civitai: 5.1K combined installs. Skills from the Civitai open source platform teaching agents its own Next.js, tRPC and moderation workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/civitai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "civitai", "stable diffusion", "platform development"]
---

# Civitai Skills - Setup Guide

**Source:** [civitai/civitai](https://www.skills.sh/civitai/civitai) via skills.sh - 5.1K combined installs across 56 indexed listings; first seen 2026-11-28 (morning sweep)

**GitHub:** [civitai/civitai](https://github.com/civitai/civitai) - 7,332 stars, Apache-2.0 licence, branch main, last pushed 2026-11-28; skills live under `.claude/skills/<name>/SKILL.md`, with a second directory at `apps/event-engine/.claude/skills/`.

**Category:** Platform development skills - the Civitai open source platform teaching agents its own Next.js, tRPC, Prisma and ClickHouse workflows

**Quality Tier:** 🟠 Orange - Fail cells land here (civitai-orchestration on the Gen Agent Trust Hub; postgres-query, mod-actions and retool-query on Snyk), with Warn cells across the rest of the sample.

Civitai is the open source codebase behind civitai.com, a platform where people share and collaborate on stable diffusion models, textual inversions, hypernetworks and other generative AI assets. The skills in this repository are not a guide to that user-facing product: they are Civitai's own internal agent skills, teaching a coding agent how to work inside the Civitai codebase itself, a Next.js and tRPC monorepo with Prisma plus Postgres for data, ClickHouse for analytics, and moderation tooling for a large public platform.

The 56 indexed listings run from clickup and quick-mockups at well over a thousand installs each down to a long tail of small single-purpose helpers. The two high-install skills dominate the install count: clickup wraps the ClickUp task API for issue tracking, and quick-mockups generates Mantine plus Tailwind UI mockups in parallel. The tail covers read-only data access (Postgres, ClickHouse, Redis, Meilisearch and Retool-era data), moderation actions, feature flags, support tickets, dev-server and worktree management, and content-policy plus generation-onboarding workflows.

## Installation

The README installs the whole platform for local development, not a skill bundle. Skills are committed into the repo and load from `.claude/skills/<name>/SKILL.md` when an agent works in the checkout:

```sh
git clone https://github.com/civitai/civitai.git
cd civitai
nvm use
corepack enable
git submodule update --init event-engine-common
cp .env-example .env.development
docker compose -f docker-compose.base.yml up -d
pnpm install
pnpm dev
```

Prerequisites: Docker with Compose v2, Node.js 24.22.3 (the version pinned in `.nvmrc`; `package.json` declares `engines.node: ">=24.0.0 <25"`), and pnpm, which the repo enforces through a `preinstall` hook. A Nix flake (`nix run .#dev`) and devcontainers are also documented; the signals and buzz services require an internal GitHub package token.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| clickup | 1,766 | Interact with ClickUp tasks and docs: get task details, view comments, create and manage tasks, and create or edit docs from ClickUp task or doc URLs and IDs. |
| quick-mockups | 1,693 | Create multiple UI design mockups in parallel using Mantine v7 plus Tailwind, following Civitai's design system. |

The remaining 54 indexed listings range from 2 to 135 installs.

The two rows above follow the skills.sh install index. Three indexed listings have no matching directory in the current tree (ralph, worktree and opensearch-admin), while the tree also holds a `rgb-proxy` skill directory that carries no indexed listing.

## Why This Matters for Hermes Agents

This is a rare look at how a large, production, open source platform wires agent skills into its own development loop. The skills are committed into the repo and load from `.claude/skills/<name>/SKILL.md`, so an agent working in the checkout picks them up without any marketplace or plugin registration.

The most instructive pattern is the read-only default: the data skills (postgres-query, clickhouse-query, redis-inspect and retool-query) all document read-only connections by default and require an explicit target before touching anything. That is a safe pattern to copy for any agent that queries production data.

The moderation and content-policy skills show how a platform encodes its own compliance workflow for an agent, from strikes and reports to NCMEC/CSAM reporting. That is a useful model for builders who need agents to follow a governed, auditable process rather than free-form judgement.

Finally, the long tail of single-purpose skills (add-generation-support, add-ecosystem, scaffold-civitai-app and similar) shows a granular, one-skill-per-workflow structure that is cheap to trigger and easy to audit, even though most of those skills carry only a handful of installs.

## Usage

| You say | What happens |
|---|---|
| "Look up ticket CIV-1234 in ClickUp" | Uses clickup to fetch the task, comments and docs tied to the URL or ID. |
| "Mock up three layout options for this feature" | Uses quick-mockups to generate parallel Mantine plus Tailwind mockups. |
| "Check the queue health in Meilisearch" | Uses meilisearch-admin to inspect index status, tasks and settings. |
| "Why is this query slow?" | Uses postgres-query to run EXPLAIN against a read-only target. |
| "What does the moderation record say about this user?" | Uses mod-actions to query strikes, reports and moderation history. |
| "Turn the feature on for 10 percent of users" | Uses flipt to create or configure a feature flag rollout. |
| "What are the recent ClickHouse events for this model?" | Uses clickhouse-query to explore analytics and event data. |

## Verification

Skills are part of the checkout, so the cleanest pre-install check is to fetch a skill's SKILL.md directly and read its frontmatter. The layout on branch main is `.claude/skills/<name>/SKILL.md`:

```bash
curl -sL https://raw.githubusercontent.com/civitai/civitai/main/.claude/skills/quick-mockups/SKILL.md
```

After a clone, confirm the skill directories and read one skill's frontmatter:

```bash
git clone --depth 1 https://github.com/civitai/civitai.git /tmp/civitai
ls /tmp/civitai/.claude/skills/
head -5 /tmp/civitai/.claude/skills/postgres-query/SKILL.md
```

The listing should show 53 skill directories under `.claude/skills/` (including a `rgb-proxy` directory that carries no indexed listing) plus `agent-review` and `clickhouse-query` again under `apps/event-engine/.claude/skills/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| clickup | Pass | Warn | Warn |
| quick-mockups | Pass | Pass | Pass |
| meilisearch-admin | Pass | Pass | Warn |
| postgres-query | Pass | Pass | Fail |
| clickhouse-query | Pass | Pass | Pass |
| redis-inspect | Pass | Pass | Warn |
| browser-automation | Warn | Warn | Warn |
| mod-actions | Pass | Pass | Fail |
| discord | Pass | Pass | Warn |
| dev-server | Warn | Warn | Warn |
| flipt | Pass | Pass | Warn |
| civitai-orchestration | Fail | Pass | Warn |
| retool-query | Pass | Pass | Fail |
| component-preview | Pass | Pass | Pass |
| ralph | Pass | Pass | Warn |
| agent-review | Warn | Pass | Pass |
| worktree | Warn | Pass | Pass |
| ux-design | Pass | Pass | Pass |
| metabase | Pass | Pass | Pass |
| freshdesk | Pass | Pass | Warn |

This guide is Orange because the sampled verdicts include Fail cells: civitai-orchestration on the Gen Agent Trust Hub, and postgres-query, mod-actions and retool-query on Snyk. Warn cells sit across most of the rest of the sample, including clickup, browser-automation, dev-server and freshdesk. Only 20 of the 56 indexed listings were sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 5,104 combined installs across 56 indexed listings; 7332 GitHub stars; Apache-2.0 licence; last pushed 2026-11-28. Counts drift over time.
- The skills document Civitai's own codebase work, not the platform's user-facing product: most assume the Civitai repo, its tRPC API, its databases and its internal services, so they are of limited use outside a Civitai checkout.
- The install index outruns the tree: ralph, worktree and opensearch-admin carry install counts but have no matching directory in the current tree, and the tree's `rgb-proxy` skill has no indexed listing.
- Many skills need internal credentials (ClickUp, Discord, Freshdesk, Stripe, Cloudflare, Flipt and the moderator database), and the README's signals and buzz services require a private ghcr.io token, so a public clone cannot exercise the full suite.
- The security verdicts cover 20 of the 56 indexed listings; the other 36 were not sampled.
- The README notes that services requiring external input (Orchestration, Signals, Buzz) will not work in a local setup.

## Related

- [Medusa Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/medusa-agent-skills-setup)
- [Dify Skills - Official Dev Workflow Suite Setup](/hermes/skills/catalog/dify-skills-setup)
- [Bagisto Agent Skills - Official Ecommerce Platform Setup](/hermes/skills/catalog/bagisto-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read a skill's SKILL.md before relying on it: the frontmatter description plus the body is the full instruction set, and most of these skills assume the Civitai repo.
- Treat the data skills as the pattern for read-only defaults: postgres-query, clickhouse-query, redis-inspect and retool-query all default to read-only connections and require an explicit target.
- Prefer the repo's own setup path (nvm use, corepack, pnpm) over guessing a Node version; the engines range is enforced and the wrong major surfaces as odd test failures.
- Because the suite includes moderation and CSAM-reporting tooling plus Fail cells in its verdicts, re-check the skills.sh security pages before pulling any skill into a production profile.
- Since three indexed listings have no tree counterpart, confirm a skill exists in the current checkout before wiring it into a router.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
