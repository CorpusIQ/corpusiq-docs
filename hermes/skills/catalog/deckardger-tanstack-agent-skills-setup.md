---
title: "TanStack Agent Skills - Query and Router Setup"
description: "deckardger/tanstack-agent-skills: 32.8K combined installs. Four rule-based skills for TanStack Query, Router, Start and cross-library integration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/deckardger-tanstack-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "tanstack", "react", "typescript"]
---

# TanStack Agent Skills - Setup Guide

**Source:** [deckardger/tanstack-agent-skills](https://www.skills.sh/deckardger/tanstack-agent-skills) via skills.sh - 32.8K combined installs across 4 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [deckardger/tanstack-agent-skills](https://github.com/deckardger/tanstack-agent-skills) - 228 stars, MIT, branch main, last pushed 2026-09-09; 4 `SKILL.md` files, one per directory under `skills/`, each with a `rules/` folder of numbered rule documents beside it (38 files under `tanstack-query`, 36 under `tanstack-router`, 32 under `tanstack-start`, 4 under `tanstack-integration`)

**Category:** TanStack frontend stack for agents: TanStack Query, Router, Table and Form patterns

**Quality Tier:** 🟢 Green - all four sampled skills Pass on all three auditors, and the repository is MIT-licensed markdown with no install scripts

Four skills cover the TanStack surface that most React applications actually touch: `tanstack-query` for data fetching, caching, mutations and server state, `tanstack-router` for type-safe routing, loaders, search params and navigation, `tanstack-start` for server functions, middleware, SSR and authentication, and `tanstack-integration` for the wiring between them. Each one is a `SKILL.md` that states the rule categories and their priority, plus a `rules/` folder holding one markdown file per rule, so the agent can read the summary and then open the specific rule it needs.

The design worth noting is that the rules are graded by impact. Query opens with Query Keys and Caching as CRITICAL, then Mutations and Error Handling as HIGH, then prefetching, infinite queries, SSR and performance below that. Router does the same with type safety and route organisation at CRITICAL. That ordering is the most useful part of the suite for an agent, because it gives a default order of attack on any TanStack question rather than a flat list of tips.

## Installation

The README documents one command, and the manual alternative of adding the skills to a project's `.cursor/` directory or Claude Code configuration:

```bash
npx skills add DeckardGer/tanstack-agent-skills
```

There is no plugin marketplace route and no per-skill installer flag in the README, so a single skill is installed by copying its directory. For this profile the durable install is the directory copy, which keeps each `rules/` folder and its `SKILL.md` together:

```bash
git clone --depth 1 https://github.com/DeckardGer/tanstack-agent-skills.git /tmp/tanstack-skills
cp -r /tmp/tanstack-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all four directories. For a profile that only writes React with Query, `tanstack-query` alone is coherent; add `tanstack-router` when routing is in scope, `tanstack-start` when the app is full-stack, and `tanstack-integration` last, since its four rules only make sense once Query and Router are both in play.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tanstack-query-best-practices | 12,935 | Data fetching, caching and server state with TanStack Query: query key structure, staleTime and invalidation, optimistic mutations, error boundaries and retry, intent and route prefetching, infinite queries, SSR hydration and select transforms. |
| tanstack-start-best-practices | 9,861 | Full-stack React on TanStack Start: `createServerFn` patterns, input validation and CSRF protection, request and function middleware, session handling and route protection, API routes, hydration safety, streaming and selective SSR. |
| tanstack-router-best-practices | 7,122 | Type-safe routing with TanStack Router: router registration and context typing, file-based route trees and pathless layouts, loaders and query integration, search param validation, not-found and error boundaries, links, route masks and code splitting. |
| tanstack-integration-best-practices | 2,931 | Wiring Query to Router and Start in one app: QueryClient context and provider setup, the loader plus query pattern, `ensureQueryData`, one caching source of truth, and dehydration and hydration across the SSR boundary. |

All 4 indexed listings clear the threshold and appear above. Every listing maps to a directory in the tree, with the naming difference noted below.

## Why This Matters for Hermes Agents

TanStack code has a large surface of things that compile and still behave wrongly. A query key that is not serialisable, a `staleTime` set in the wrong place, a loader that fetches instead of ensuring, a search param read without validation, a server function that trusts its input: each one typechecks, each one fails later, and each one is covered by a rule file in this repository. The skill descriptions carry the trigger conditions, so the agent routes on "we are fetching server data" or "we are setting up routing" rather than waiting to be told which library is in the file.

The priority grades are what make the suite usable at speed. When an agent is asked to review a data layer, "Query Keys and Caching first" is a concrete order that matches how these bugs actually cluster, and the rule files under `rules/` mean the agent can pull `qk-factory-pattern.md` or `qk-serializable.md` on demand instead of loading all 38 query rules into context.

The integration skill is the piece most suites leave out. Query and Router each have defensible local patterns that fight each other on SSR: a loader that also fetches, a cache with two sources of truth, hydration that duplicates a request. Four rules that only exist to settle that boundary are worth more than another hundred tips inside either library.

## Usage

| You say | What happens |
|---|---|
| "Our query keys are a mess, tidy them up" | `tanstack-query-best-practices` works from the query key rules: hierarchical organisation, a key factory, serialisable keys and dependencies, in that order. |
| "This tab refetches everything when it regains focus" | The same skill moves to the caching rules: `staleTime`, `gcTime` and invalidation, with structural sharing and select transforms checked before anything is rewritten. |
| "Add a mutation that updates the list optimistically" | Query's mutation rules apply: optimistic update, rollback on error, and invalidation once the request settles. |
| "Validate this search param and keep the type" | `tanstack-router-best-practices` applies the search param rules, covering validation, type inheritance, middleware and defaults. |
| "Our loader fetches data the query already has" | `tanstack-integration-best-practices` replaces the fetch with `ensureQueryData` and points the loader at the query cache as the single source of truth. |
| "Add auth to these server functions" | `tanstack-start-best-practices` applies the authentication and security rules: session management, route protection, input validation and CSRF before the handler body. |
| "Why does this page flash empty on first paint" | The SSR rules take over: Start's hydration safety file, plus the server-side `staleTime` rule that decides whether the client refetches the moment it mounts. |

## Verification

The raw path for the largest skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} tanstack-query\n" \
  https://raw.githubusercontent.com/DeckardGer/tanstack-agent-skills/main/skills/tanstack-query/SKILL.md
```

Expect `200`. After the copy lands, confirm the four directories and that `rules/` came along, since the rules are where the substance lives:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/tanstack-*/ | wc -l
head -4 ~/.hermes/profiles/corpusiq/skills/tanstack-query/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/tanstack-query/rules | wc -l
```

The count should print 4, the header should show `name: tanstack-query-best-practices` followed by a one-line description, and the rule count should print 38.

## Security

All four sampled skills Pass all three auditors, and this is the cleanest of the four guide packs in this batch: MIT licensed, no install hook, and no executable content of any kind in the tree.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tanstack-query-best-practices | Pass | Pass | Pass |
| tanstack-start-best-practices | Pass | Pass | Pass |
| tanstack-router-best-practices | Pass | Pass | Pass |
| tanstack-integration-best-practices | Pass | Pass | Pass |

The risk here is instructional, not mechanical. There is nothing to execute: the repository holds markdown, and `npx skills add` copies it into an agent's skill directory. What that markdown can still do is steer an agent into a pattern that is wrong for the project in front of it, most plausibly in `tanstack-start`, where the security rules cover input validation, CSRF protection and sensitive data but the skill cannot see whether the application already has a session layer that handles them.

Treat the rules as a checklist to verify against the codebase, not as an authority. Two specific habits are worth enforcing: keep secrets in environment configuration rather than in server function arguments, and confirm that any generated `createServerFn` validates its inputs before it touches storage or a third-party API. Both skills say as much; whether the agent applies it is a routing question.

## Limitations

- Snapshot data, verified 2026-10-31: 32,849 combined installs across 4 indexed listings; 228 GitHub stars; MIT; last pushed 2026-09-09. Counts drift over time.
- The last push is the oldest of the TanStack ecosystem's active repos, so the rules describe patterns as they stood in September 2026. Framework releases since then are not reflected, and a rule that was accurate then can read as stale advice for a current release.
- Listing names and directory names differ. skills.sh and each `SKILL.md` carry the `-best-practices` suffix, while the directories under `skills/` do not, so `tanstack-query` on disk is `tanstack-query-best-practices` in the index; a script that installs by listing name and a copy of the directory will create different folder names.
- Rule counts in the README and in the tree do not line up exactly. Query is described as 32 or more rules across 8 categories and ships 38 rule files, router is described as 36 and ships 36, start is described as 32 and ships 32, and integration is described as 13 rules across 4 categories while the tree holds 4 category files, so the integration count is per category rather than per file.
- Install counts are not a ranking. Query holds 12,935 and integration holds 2,931, but integration is the one that prevents the SSR duplication bugs the other three cannot see on their own.
- Query and integration overlap by design. Loader patterns appear in both, and an agent asked to fix a loader may route to either; the integration rules are the more specific answer when Query and Router are both installed.
- Nothing here knows about TanStack Table or TanStack Form despite the category line. The repository covers Query, Router, Start and their integration only.

## Related

- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `SKILL.md` before `rules/`. Each skill's front page states the categories in priority order, which is enough to pick the two or three rule files worth opening; loading all 38 query rules buys nothing.
- Start every Query review at the key rules. `qk-factory-pattern.md` and `qk-serializable.md` catch the mistakes that make caching behave unpredictably, and they are cheaper to fix than the symptoms they cause.
- Install `tanstack-integration` even if the app looks like a plain Query app. The moment a router loader enters the picture the four integration rules become the deciding ones, and they are graded at CRITICAL for setup for that reason.
- Treat the September 2026 push date as the boundary of the advice. Verify version-sensitive details against the installed package rather than the rule text, and prefer the framework's own types when the two disagree.
- Keep the directory names as cloned. Installing by listing name produces `tanstack-query-best-practices` folders, which then do not match the paths this guide and the README use.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
