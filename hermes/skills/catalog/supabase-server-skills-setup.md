---
title: "Supabase Server Skill - Edge Function Auth Setup"
description: "supabase/server: 10.2K combined installs. One MIT skill for @supabase/server: auth modes, Edge Function handlers and clients."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/supabase-server-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "supabase", "edge functions", "authentication", "typescript"]
---

# Supabase Server Skill - Setup Guide

**Source:** [supabase/server](https://www.skills.sh/supabase/server) via skills.sh - 10.2K combined installs across 1 indexed listing; first documented 2026-11-02 (evening sweep)

**GitHub:** [supabase/server](https://github.com/supabase/server) - 94 stars, MIT, branch main, last pushed 2026-10-19; one skill at `skills/supabase-server/SKILL.md`, 481 lines with no `references/` folder, inside a package monorepo that also holds `src/`, `docs/`, `e2e/`, `examples/` and `scripts/`

**Category:** Server-side Supabase code for agents: request-scoped auth, Edge Functions, Hono and framework bridges, and client creation

**Quality Tier:** 🟡 Yellow - Snyk warns on the single sampled listing, which is the whole index here, though the licence is MIT and the skill is published by the vendor whose package it documents

This is not a skills repository with a product attached. It is `@supabase/server`, a published npm package at version 1.9.2, and the skill is one folder inside it. The package gives server-side code a single wrapper that validates inbound credentials, builds RLS-scoped and admin clients, and handles CORS, so a handler only runs after auth has succeeded. The skill exists so an agent writing that code reads the vendor's rules instead of reconstructing them from a 0.x tutorial it saw in training.

The layout is the first thing to understand, because it decides what a copy of the skill actually contains. `skills/supabase-server/` holds exactly one file, `SKILL.md`, and nothing else. The knowledge that file points at lives one level up in `docs/`: twelve entries covering getting started, auth modes, core primitives, environment variables, error handling, API reference, security, Postgres, MCP, SSR frameworks, TypeScript generics and the deprecated adapters. The `SKILL.md` documentation section is explicit about where to find them: the repository root when you are working in the SDK repo, or `node_modules/@supabase/server/docs/` when the package is installed as a dependency. The package manifest confirms the intent, since `files` lists `dist`, `docs` and `skills`.

## Installation

The README documents the skill in a short section of its own, after the package install commands:

```bash
npx skills add supabase/server
```

The package itself is a normal dependency, and the Deno route needs no install at all:

```bash
npm install @supabase/server
pnpm add @supabase/server
```

```ts
// Deno / Supabase Edge Functions
import { withSupabase } from "npm:@supabase/server@1";
```

Copying the folder by hand is not equivalent to installing the package. If you clone the repository and drop `skills/supabase-server/` into a profile, you get a 481-line `SKILL.md` whose documentation table resolves to nothing, because the `docs/` directory it references is a sibling of `skills/`, not a child of it. Either install the npm package alongside the skill so the docs land in `node_modules`, or clone the repository and keep the tree intact.

What the skill actually needs in order to be useful is the package under an agent's hands. It targets TypeScript server code running under Node 22 or later, since the package's `engines` field requires `>=22`, and the Hono bridge is documented as needing Node 22 as well. It also assumes `supabase/` Edge Functions with a `config.toml` in reach, because one of its first warnings is that non-user auth modes need `verify_jwt = false` on the function or the platform rejects the request before the handler sees it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| supabase-server | 10,220 | Planning and writing server-side code that imports `@supabase/server`: choosing one of the four `auth` modes, wrapping a fetch handler with `withSupabase`, using `createSupabaseContext` for custom error responses, the `core` primitives `verifyAuth`, `verifyCredentials` and `extractCredentials`, `createContextClient` and `createAdminClient`, framework bridges, and migrating legacy `Deno.serve` or `createClient` patterns. |

All 1 indexed listings clear the threshold and appear in the table above.

The `SKILL.md` opens with three warnings before it explains anything, and they set the tone. The config option is `auth`, not `allow`, because `allow` was deprecated and will be removed. The auth mode values are `none` and `publishable`, not the removed `always` and `public`, and the field on the context is `authMode`, not `authType`. And the legacy `anon` and `service_role` keys are on their way out in favour of `sb_publishable_...` and `sb_secret_...`, with the instruction to never call `createClient(url, anonKey)` directly and to use the auth modes instead.

From there it covers the entry points (`@supabase/server`, `/core`, `/adapters/hono`, `/oauth-protected-resource`), quick starts for Edge Functions, Cloudflare Workers and the framework bridges, audience and issuer pinning with `fromSupabaseUrl`, the conditions under which `auth: 'none'` is acceptable, and a recipe section for function-to-function calls with a secret key and for calling Edge Functions from SQL with `pg_net` and Vault. The Hono, H3, Elysia and NestJS adapters are marked deprecated with a removal date of December 1, 2026, and are replaced by a `@supabase/middleware` bridge the agent copies into the project.

## Why This Matters for Hermes Agents

Server-side auth is where agent-written code does the most damage with the fewest symptoms. A handler that creates a client with a service-role key and returns rows looks perfect in review and bypasses every RLS policy in production. This skill is built to prevent exactly that shape, because it teaches one wrapper and four named auth modes instead of a menu of client constructors, and it maps every legacy pattern an agent is likely to emit onto the correct replacement.

The migration table is the part that earns its place. `allow` to `auth`, `'public'` to `'publishable'`, `'always'` to `'none'`, `authType` to `authMode`, `claims` to `jwtClaims`, and `SUPABASE_ANON_KEY` to `auth: 'publishable'` are all renames that older examples will get wrong. An agent working from a 2025 blog post will produce code that fails at runtime or, worse, silently accepts a mode value that no longer exists, and the skill states the mapping up front so the correction happens before the code is written rather than in review.

The platform detail is the second win. Supabase Edge Functions verify a JWT by default, so a function using `auth: 'publishable'`, `auth: 'secret'` or `auth: 'none'` is rejected by the platform before the skill's own logic runs unless `verify_jwt = false` is set for that function in `config.toml`. That single line explains a class of bug that otherwise presents as a mysterious 401 on an endpoint with no auth requirement, and it is documented in the skill rather than left to be discovered.

The third win is the attention paid to ordering and to failure semantics. Array auth is first-match-wins, and a present but invalid JWT rejects with `InvalidJwtError` rather than falling through to the next mode, which means an endpoint declared as `['user', 'none']` will not silently serve anonymous requests when a caller sends an expired token. An agent that understands that will tell you to drop the `Authorization` header instead of debugging a downgrade that is not happening.

## Usage

| You say | What happens |
|---|---|
| "Add a Supabase Edge Function that returns the signed-in user's todos" | Writes a `withSupabase({ auth: 'user' }, ...)` default export and reads `ctx.supabase.from('todos')`, which is RLS-scoped to that user. |
| "This function returns 401 before my code runs" | Checks `supabase/config.toml` and adds `verify_jwt = false` for the function, since the mode is not `user`. |
| "Let our mobile app read the catalogue before login" | Uses `auth: 'publishable'`, which validates the `apikey` header against the default publishable key and keeps the database anonymous, and shows the client sending `sb_publishable_...`. |
| "Return a proper error payload instead of throwing" | Switches to `createSupabaseContext`, which returns `{ data, error }` so the handler can shape the status and body. |
| "Migrate this function off `Deno.serve` and the anon key" | Rewrites it to the auth modes, replaces `SUPABASE_ANON_KEY` with `auth: 'publishable'`, and renames `allow` and `authType` per the migration table. |
| "One function needs to call another internally" | Uses `auth: 'secret'` on the called function and `ctx.supabaseAdmin.functions.invoke()` from the caller, with `verify_jwt = false` on the callee. |
| "Refresh the rankings table from a cron job" | Uses `auth: 'secret'` with the key sent in the `apikey` header, or the `pg_net` recipe with the key stored in Vault. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/supabase/server/main/skills/supabase-server/SKILL.md
```

After a clone, confirm the skill is a single file and that the docs it points at are present beside it:

```bash
git clone --depth 1 https://github.com/supabase/server.git /tmp/supabase-server
find /tmp/supabase-server -name SKILL.md | wc -l
ls /tmp/supabase-server/skills/supabase-server
ls /tmp/supabase-server/docs | wc -l
head -3 /tmp/supabase-server/skills/supabase-server/SKILL.md
```

The first count should print 1, the skill listing should show `SKILL.md` alone, the docs count should print 12, and `head` should show `name: supabase-server` with the description the runtime routes on. On the installed copy, the check that matters is whether the docs are reachable from where the agent looks:

```bash
ls ~/.hermes/profiles/corpusiq/skills/supabase-server
ls node_modules/@supabase/server/docs 2>/dev/null | wc -l
```

If the first listing shows only `SKILL.md` and the second prints 12, the skill can reach its documentation through the package. If the second prints 0, the agent holds a map with no territory behind it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| supabase-server | Pass | Pass | Warn |

Two auditors pass and Snyk warns on the one listing that exists. The skill folder holds no executable content at all, just Markdown, so the warn is about the instructions and the package they describe rather than about anything that runs on install.

The material risk in this skill is credential handling, and it is worth being deliberate about it. The skill deals with three kinds of secret: a user JWT in the `Authorization` header, an `sb_publishable_...` key that is safe to ship to clients, and an `sb_secret_...` key that bypasses RLS. It repeatedly steers agents away from the legacy `anon` and `service_role` environment variables and toward named auth modes, which is the safer default because the mode is visible in the handler signature. It also refuses to let an agent quietly choose `auth: 'none'`: the section on that mode instructs the agent to confirm with the user whether the endpoint is truly public, and to propose `auth: 'secret'` for service-to-service calls and webhooks instead.

Read `docs/security.md` in the package before production, and keep secret keys in Supabase's environment or Vault rather than in source. The skill's own example for the `pg_net` recipe stores the key in Vault so it never appears in a query, which is the pattern to copy.

## Limitations

- Snapshot data, verified 2026-11-02: 10,220 combined installs across 1 indexed listing; 94 GitHub stars; MIT; last pushed 2026-10-19. Counts drift over time.
- The skill directory contains one file and no references. Its documentation map points at `docs/` in the repository root or in `node_modules/@supabase/server/docs/`, so a hand-copied skill folder is a 481-line summary with dead pointers.
- This is a package repository first and a skills source second. The README documents `@supabase/server` for humans, and the skill section is a single paragraph, so package-level facts such as the Node 22 engine requirement are stated in the manifest rather than in the guide.
- The API surface is mid-migration. The framework adapters for Hono, H3, Elysia and NestJS are deprecated with removal on December 1, 2026, and the 0.x to 1.x renames make older examples wrong in ways that still compile.
- One listing and 94 stars is thin adoption data for a vendor package, so the install figure reflects skills.sh indexing rather than broad third-party use.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [supabase Skills](/hermes/skills/catalog/supabase)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the npm package next to the skill, even on a machine that only writes code. Without `docs/` in `node_modules` the skill's documentation pointers all miss.
- Get the auth mode into the handler signature before writing the body. `withSupabase({ auth: 'user' }, ...)` makes the trust boundary readable in review, which a bare `createClient` never does.
- Check `config.toml` first when a non-user function returns 401. `verify_jwt = false` is the one-line fix and it applies per function.
- Treat `auth: 'none'` as a decision to justify. The skill says to confirm with the user, and the right alternatives are `auth: 'secret'` for services and webhooks and a server-verified signature for third-party callbacks.
- Grep for `allow:`, `authType` and `SUPABASE_ANON_KEY` before trusting an existing function. Those three tokens mark code written against the old surface, and the migration table gives the replacement for each.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
