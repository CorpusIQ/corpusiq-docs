---
title: "next-safe-action Skills - Forms and Validation"
description: "next-safe-action/skills on skills.sh: 9.4K combined installs across 9 listings; typed server actions, forms, hooks, middleware and validation errors."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/next-safe-action-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "nextjs", "react", "typescript"]
---

# next-safe-action Skills - Setup Guide

**Source:** [next-safe-action/skills](https://www.skills.sh/next-safe-action/skills) via skills.sh - 9.4K combined installs across 9 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 1 star, no LICENSE file in the repository, last pushed 2026-09-03, 9 SKILL.md directories under skills/
**Category:** Next.js server action layer: typed clients, form and hook integration, middleware, validation errors and Vitest coverage
**Quality Tier:** 🟡 Beta - no LICENSE file in the repository; every sampled audit Pass; 1 star.

next-safe-action is a Next.js library for type-safe server actions. This companion repository ships nine skills that document its API surface one slice at a time: how to create the client, how to wire forms and React hooks, how middleware and authentication compose, how validation errors are shaped and returned, and how to test the whole thing with Vitest.

The split is deliberately by surface area rather than by feature size. Every skill maps to one import path in the library, so an agent that knows the user is touching `useAction` can load the hooks skill instead of the whole library reference. The README documents installation through Vercel's Skills CLI and lists every skill with a one-line description.

## Installation

Install all nine skills:

```bash
npx skills add next-safe-action/skills --skill '*'
```

Install a single skill:

```bash
npx skills add next-safe-action/skills --skill 'safe-action-client'
```

Install globally so the skills are available across all projects:

```bash
npx skills add next-safe-action/skills -g
```

Target a specific agent:

```bash
npx skills add next-safe-action/skills --agent claude
```

List what the repository ships before installing:

```bash
npx skills add next-safe-action/skills --list
```

## What It Provides

Seven listings clear the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| safe-action-forms | 1,242 | The react-hook-form adapter (useHookFormAction, mapToHookFormErrors), native HTML forms, bind arguments and file uploads |
| safe-action-client | 1,238 | Creating the safe action client, input and output validation with Standard Schema (Zod, Yup, Valibot) and server error handling |
| safe-action-hooks | 1,231 | React hooks (useAction, useOptimisticAction, useStateAction), optimistic UI, status callbacks, executeAsync and queued mutations |
| safe-action-advanced | 1,226 | Bind arguments, metadata schemas, framework errors (redirect, notFound, forbidden, unauthorized) and type inference utilities |
| safe-action-validation-errors | 1,216 | returnValidationErrors, formatted vs flattened error shapes, custom shapes and field-level or form-level display |
| safe-action-middleware | 1,197 | Authentication, authorization, logging, rate limiting, error interception and context extension with createMiddleware |
| safe-action-testing | 1,145 | Vitest patterns for server actions, middleware behavior, hooks with React Testing Library and error scenarios |

The remaining 2 indexed listings range from 450 to 490 installs: safe-action-better-auth (490) and safe-action-tanstack-query (450).

## Why This Matters for Hermes Agents

Server actions sit on a boundary that models get wrong in a specific way: they write something that typechecks but cannot round-trip through the client, or they reach for `useActionState` when the project uses `useAction`. A skill that names the exact hook and its callbacks removes that class of error before the first attempt.

The validation error skill is the highest-value piece for a coding agent. Form error shape is where a generated component most often breaks a real user flow, and the flattened versus formatted distinction is the kind of detail that no model infers from a type signature.

Middleware is the other boundary that agents improvise badly, usually by writing authentication inline in every action. The middleware skill covers context extension and standalone reusable middleware, which is the pattern that keeps auth out of individual handlers.

The testing skill closes the loop. Wiring Vitest around server actions and hooks is mechanical but easy to skip, and an agent with the pattern in front of it writes the first test instead of deferring it.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a typed action that takes an email and a name" | safe-action-client creates the client and the action with input and output validation |
| "Use react-hook-form for this action" | safe-action-forms wires useHookFormAction and maps server errors onto form fields |
| "Add optimistic updates to this like button" | safe-action-hooks switches to useOptimisticAction and handles the status callbacks |
| "Block this action unless the user is an admin" | safe-action-middleware extends the context with the session and authorizes before validation |
| "Show field-level errors on the signup form" | safe-action-validation-errors returns structured errors and renders them per field |
| "Test the action and the middleware" | safe-action-testing writes Vitest cases for the action, the middleware and the error paths |
| "Add TanStack Query to this action" | safe-action-tanstack-query wires mutationOptions, ActionMutationError handling and query invalidation |

## Verification

Fetch the client skill to review it before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/next-safe-action/skills/main/skills/safe-action-client/SKILL.md | head -8
```

It should open with `name: safe-action-client` and a description naming createSafeActionClient and Standard Schema. Then confirm the installed directories:

```bash
ls ~/.claude/skills | grep safe-action
```

Nine directories should appear for a full install. Asking the installer for the list is the cheaper check, since it does not depend on which skills directory your agent reads:

```bash
npx skills add next-safe-action/skills --list
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| safe-action-forms | Pass | Pass | Pass |
| safe-action-client | Pass | Pass | Pass |
| safe-action-validation-errors | Pass | Pass | Pass |
| safe-action-tanstack-query | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-05: 9,435 combined installs across 9 indexed listings; 1 GitHub star; no LICENSE file; last pushed 2026-09-03. Counts drift over time.
- The repository has no LICENSE file, so default copyright applies. Treat redistribution of the skill text as a permissions question rather than as an open licence grant.
- One GitHub star and no release history make this a small community companion repo rather than a vendor-maintained suite. Review the skill text against your installed library version before trusting it in a long-lived project.
- The README declares no supported next-safe-action major version, so the documented signatures can trail the library you actually have installed.
- `safe-action-better-auth` (490) and `safe-action-tanstack-query` (450) fall below the table threshold but are still part of the nine-skill install, so an integration choice made on install count alone will miss both adapters.
- The skills describe usage patterns only. They do not generate routes, migrations or project scaffolding.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)
- [Better Auth Skills - Authentication Infrastructure Setup](/hermes/skills/catalog/better-auth-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all nine rather than one at a time. The skills cross-reference each other, and the hooks skill assumes the client skill's vocabulary.
- Load `safe-action-client` first in any new project: it fixes the validation and error-handling contract that every other skill builds on.
- Keep middleware in one place. If the agent starts writing auth inside individual actions, point it back at `safe-action-middleware` and the reusable `createMiddleware()` shape.
- Ask for the test in the same request as the action. `safe-action-testing` documents the Vitest harness that is otherwise skipped.
- Pair the form work with the error skill: `useHookFormAction` and `returnValidationErrors` are two halves of the same flow and break apart when used separately.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
