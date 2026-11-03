---
title: "Next.js Cache Architecture - Setup Guide"
description: "mohamed-hossam1/nextjs-skills: 5.1K combined installs. Next.js 16 cache skill: use cache, tag registries, invalidation, plus a server action handler."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nextjs-cache-architecture-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "nextjs", "react", "caching", "typescript"]
---

# Next.js Cache Architecture - Setup Guide

**Source:** [mohamed-hossam1/nextjs-skills](https://www.skills.sh/mohamed-hossam1/nextjs-skills) via skills.sh - 5.1K combined installs across 2 indexed listings; first documented 2026-11-02 (evening sweep)

**GitHub:** [mohamed-hossam1/nextjs-skills](https://github.com/mohamed-hossam1/nextjs-skills) - 10 stars, MIT license, branch main, last pushed 2026-05-30; 2 skills under `skills/`, where `nextjs-cache-architecture` holds a 369-line `SKILL.md`, an `overlay.yaml` routing manifest, 4 references, 3 drop-in assets, `scripts/audit.mjs` and `evals/evals.json`, and `next-action-handler` holds a `SKILL.md` and one reference

**Category:** Next.js 16 App Router caching for agents: the use cache directive, tag registries, revalidation utilities, partial prerendering boundaries and server action plumbing

**Quality Tier:** 🟢 Green - every sampled listing passes all three auditors, the license is MIT, there is no install script, and the repository ships a zero-dependency static audit that reads a project without writing to it

This is a two-skill repository from a single author, Mohamed Hossam, and the shape of it is more interesting than the install count suggests. `nextjs-cache-architecture` is not a prose guide; it is a build system for one architectural decision. The README documents the layout as a contract: `SKILL.md` is the always-loaded core with the architecture, the steps and the common mistakes, `overlay.yaml` is a routing manifest carrying prompt signals and validators, `references/` is loaded on demand, `assets/` holds templates the agent copies into your repository, `scripts/` holds verifiers, and `evals/` holds test cases for the skill itself.

The cache skill's position is that caching in Next.js 16 has three load-bearing pieces and they have to exist on day one: a tag registry where every tag string lives in one file, a revalidation utility module where every `updateTag()` call lives, and `"use cache"` placed on data-fetching functions or cached child components rather than on pages. The remaining steps follow from that spine: enable `cacheComponents` in `next.config.ts`, write the registry, write the revalidation module, fetch in data functions, structure each page as a static shell plus Suspense boundaries, read `cookies()` and `headers()` outside the cache boundary and pass values in as arguments, and wire mutations to the utilities instead of calling invalidation inline.

`overlay.yaml` is worth reading even if you never install the skill. It declares activation signals (`use cache`, cache components, PPR, cacheLife, cacheTag, updateTag, unstable_cache, with an `allOf` and `anyOf` scoring rule and `minScore: 6`) plus three validators that fire on deprecated patterns: a bare `unstable_cache(` call, a singular `cacheHandler:` config key, and a single-argument `revalidateTag(tag)` call.

## Installation

The README documents one install command per skill, and the per-skill form is the one to use because the repository has no default:

```bash
npx skills add https://github.com/mohamed-hossam1/nextjs-skills --skill nextjs-cache-architecture
npx skills add https://github.com/mohamed-hossam1/nextjs-skills --skill next-action-handler
```

The manual route is a folder copy. Take the whole folder, because the assets are templates the agent is instructed to copy into your project and the references carry the debugging detail:

```bash
git clone --depth 1 https://github.com/mohamed-hossam1/nextjs-skills.git /tmp/nextjs-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills/nextjs-cache-architecture
cp -R /tmp/nextjs-skills/skills/nextjs-cache-architecture/. ~/.hermes/profiles/corpusiq/skills/nextjs-cache-architecture/
```

The skill writes code but installs nothing. What it requires is stated as a table in the README: Next.js 16 or newer, `cacheComponents: true` in `next.config.ts`, and the App Router. Pages Router, the edge runtime and static export (`output: "export"`) are all listed as unsupported, which matters because a Next.js 15 project will load the skill and then take advice that does not apply.

The second skill is heavier on the environment. `next-action-handler` targets a server action layer built on `next-safe-action`, `zod`, `better-auth` and `pino`, and its own `SKILL.md` documents `npm install -D next-action-handler` followed by `npx next-action-handler@latest add`, which installs those dependencies and writes a handler module into `lib/next-action-handler/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nextjs-cache-architecture | 5,058 | Designing and implementing caching in a Next.js 16 App Router project: enabling cache components, building the tag registry and revalidation utilities, placing `"use cache"` on data functions, structuring pages as a static shell with Suspense boundaries for partial prerendering, handling personalized content by reading request APIs outside the boundary, choosing `cacheLife` profiles, picking between `updateTag` and `revalidateTag(tag, "max")`, migrating off `unstable_cache`, and debugging stale or wrongly fresh data with a symptom table and a sign-off checklist. Ships three drop-in templates (`tags.ts`, `revalidate.ts`, `SuspenseOnSearchParams.tsx`) and a static audit script. |
| next-action-handler | 5 | Standardizing server actions on top of `next-safe-action` and `zod`: `actionClient` and `authedActionClient`, action metadata and `actionName`, `validationErrors`, `outputSchema`, `handleServerError`, better-auth error mapping and pino logging, installed through its own `npx next-action-handler@latest add` command. |

All 2 indexed listings clear the threshold and appear in the table above.

The install split is the honest signal in this pack. The cache skill carries essentially all of the distribution at 5,058, while the action handler sits at 5, which is close enough to zero that you should treat it as unreviewed by the wider community. The cache skill, by contrast, is 369 lines of opinionated instruction with a reference set behind it: `core-concepts.md` for how cache keys are derived and what `cacheLife` profiles mean, `personalized-content.md` for the read-outside pattern, `debugging-and-checklist.md` for the end-to-end walk, and `migration-from-unstable-cache.md` for moving an existing codebase.

## Why This Matters for Hermes Agents

Next.js 16 changed the caching contract, and the change is the kind that an agent trained on older code will get wrong in a way that compiles. `unstable_cache` is out, the `"use cache"` directive is in, `cacheComponents` replaces the old implicit behaviour, and `revalidateTag` now takes a second argument. The skill's validators exist precisely because those three deprecations look like working code right up until the data goes stale.

The subtle failures are placement failures. A `"use cache"` directive after an `await` means the function runs uncached on every request, with no error and no log. A `cookies()` call inside a cached function throws or returns the wrong user's data. A mutation that calls `updateTag()` before the write leaves the list reading stale. The skill lists all three in a symptom table with the fix beside the symptom, which is the format an agent can actually act on.

The second-order benefit is architectural. Left alone, an agent puts `"use cache"` wherever a page looks slow, which produces a codebase where caching is sprayed across pages with no invalidation owner. The three-piece spine, one registry, one revalidation module, cache on data not pages, gives the agent a target shape and gives a reviewer one file to check when something goes stale.

The audit script is the part that closes the loop. `scripts/audit.mjs` reads a project and checks the parts of the checklist that can be verified without running the app, exiting 0 when the checks pass, 1 when one fails and 2 on a bad invocation. It imports only `node:fs`, `node:path` and `node:url`, it has no runtime dependencies, and it writes nothing to the tree it inspects, which makes it safe to run on a repository an agent just modified.

## Usage

| You say | What happens |
|---|---|
| "Set up caching for my posts and comments tables" | Builds the tag registry, the revalidation module and the cached data functions, then wires the mutation actions to the utilities and runs the audit. |
| "My list still shows stale data after a create" | Walks the symptom table: checks whether the revalidation utility runs after the write, whether the tag string is registered, and whether the collection tag is invalidated alongside the entity tag. |
| "Cache this page but keep the user greeting live" | Reads `cookies()` or `auth()` outside the boundary, passes the value as a prop so it becomes part of the cache key, and keeps the dynamic part inside its own Suspense boundary. |
| "Our filter page doesn't show a loading state" | Swaps the plain `<Suspense>` for the `SuspenseOnSearchParams` asset, since a standard boundary does not re-trigger on searchParams-only navigation. |
| "We still use unstable_cache, migrate it" | Reads `references/migration-from-unstable-cache.md`, maps each cached function to a `"use cache"` function with `cacheTag` and `cacheLife`, and the overlay validator flags anything left behind. |
| "Check what the agent built before I merge" | Runs `node scripts/audit.mjs .` for the static checklist and reports which items passed, then names the ones that need a `next build` to confirm. |
| "Standardize our server actions" | Switches to `next-action-handler` for `authedActionClient`, input and output validation, normalized errors and pino logging. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/mohamed-hossam1/nextjs-skills/main/skills/nextjs-cache-architecture/SKILL.md
```

The audit script is the second path worth confirming, since it is the only executable in the repository:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/mohamed-hossam1/nextjs-skills/main/skills/nextjs-cache-architecture/scripts/audit.mjs
```

After a clone, check that the references and assets arrived and then run the audit against a project:

```bash
git clone --depth 1 https://github.com/mohamed-hossam1/nextjs-skills.git /tmp/nextjs-skills
find /tmp/nextjs-skills -name SKILL.md | wc -l
ls /tmp/nextjs-skills/skills/nextjs-cache-architecture/references | wc -l
ls /tmp/nextjs-skills/skills/nextjs-cache-architecture/assets
node /tmp/nextjs-skills/skills/nextjs-cache-architecture/scripts/audit.mjs /path/to/your/app
head -3 /tmp/nextjs-skills/skills/nextjs-cache-architecture/SKILL.md
```

The first count prints 2, the second 4, the assets listing shows `tags.ts`, `revalidate.ts` and `SuspenseOnSearchParams.tsx`, and `head` shows `name: nextjs-cache-architecture` with `version` 2.2.0 in the metadata block.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nextjs-cache-architecture | Pass | Pass | Pass |
| next-action-handler | Pass | Pass | Pass |

Both listings pass every auditor, and the repository is MIT licensed, which is about as clean as a skill package gets. There is no postinstall hook, no network call and no code that runs on load. The one executable is `scripts/audit.mjs`, which reads a project tree and prints results; grepping it for `writeFile`, `mkdir` and `rm` returns nothing, so it inspects without modifying.

The caveats are about what the skills make you run, not what they contain. `next-action-handler` tells the agent to run `npx next-action-handler@latest add`, which installs six packages and writes a handler module into `lib/next-action-handler/`; `@latest` is explicitly there to force the newest published version, so pin it if you care about reproducibility. Nothing in the cache skill executes, but it does instruct the agent to write files into your project: the three assets are meant to be copied to `lib/cache/tags.ts`, `lib/cache/revalidate.ts` and `components/SuspenseOnSearchParams.tsx`.

Ten stars and one author is the real risk here, and it is a maintenance risk rather than a security one. Read the templates before they land in your repository, and prefer the generated code over blind trust in the prose describing it.

## Limitations

- Snapshot data, verified 2026-11-02: 5,063 combined installs across 2 indexed listings; 10 GitHub stars; MIT; last pushed 2026-05-30. Counts drift over time.
- The distribution is one skill. `next-action-handler` has 5 installs against 5,058 for the cache skill, so it should be treated as unproven by the community regardless of its audit result.
- Requirements are narrow and stated as absolutes: Next.js 16 or newer, `cacheComponents: true`, App Router only. Pages Router, edge runtime and static export are unsupported, and nothing in the skill detects a project that violates those.
- One reference in `next-action-handler` is committed as a path containing a space (`references / patterns.md`), so tooling that globs `references/` will not find it.
- The whole suite rests on one author and 10 stars. The cache skill is unusually well instrumented for its size, but there is no second maintainer, no issue history to read and no release process beyond the branch.
- The audit script covers only the checks that can be run statically. Anything that requires building the app, including dynamic-versus-static route classification, still needs `next build`, and the skill says so.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Patterns.dev Skills - UI and Rendering Patterns Setup](/hermes/skills/catalog/patterns-dev-skills-setup)
- [Claude Code Next.js Skills - Next.js 16 and AI SDK Setup](/hermes/skills/catalog/claude-code-nextjs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the three pieces in one request. A tag registry plus a revalidation module plus cache-on-data is the whole architecture, and asking for a page to be cached without them is how you get a stale-data bug three weeks later.
- Run the audit before the build. `node scripts/audit.mjs .` catches the static checklist items in a second, and it exits non-zero, so it drops into CI without a wrapper.
- Watch the directive placement. If a cached function is running on every request, look for an `await` before the `"use cache"` line before you look anywhere else.
- Use `updateTag` for the same-request case and `revalidateTag(tag, "max")` for background invalidation from a webhook. The single-argument form is deprecated and the skill calls it out twice, once in the API table and once in a validator.
- Copy the templates rather than describing them. `assets/tags.ts` uses an `as const satisfies` shape that rejects malformed registry entries at compile time, which is worth more than a paraphrase of it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
