---
title: "React Router Skills - Data and Framework Modes"
description: "remix-run/agent-skills on skills.sh: 5.2K combined installs across 3 listings; React Router framework, data and declarative mode skills, now archived."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/react-router-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "react router", "react", "routing"]
---

# React Router Skills - Setup Guide

**Source:** [remix-run/agent-skills](https://www.skills.sh/remix-run/agent-skills) via skills.sh - 5.2K combined installs across 3 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 134 stars, MIT with a LICENSE file in the repository root, branch `main`, last pushed 2026-06-18, 3 SKILL.md directories under `skills/`, repository marked archived
**Category:** React Router guidance for agents: framework, data and declarative modes with routes, loaders, actions and type safety
**Quality Tier:** 🟡 Yellow - every sampled skill passes Gen Agent Trust Hub, Socket and Snyk and the licence is plain MIT, but the repository is archived and the publisher now sends installs to the skill inside remix-run/react-router instead.

React Router has three modes, and the difference between them is the part models get wrong: framework mode is the full-stack setup with `app/routes.ts`, the Vite plugin and server rendering, data mode is `createBrowserRouter` plus `RouterProvider` bolted onto an existing React app, and declarative mode is plain `BrowserRouter` with `<Routes>` and `<Route>` and no loaders at all. This repository split its guidance along exactly those three lines, one skill per mode, each with a `references/` directory of topic pages the agent loads on demand.

The repository is archived. Its README opens with a warning block stating that the skills repo "has been archived in favor of" three changes: putting the React Router Agent Skill directly in the remix-run/react-router repository at `.agents/skills/react-router`, publishing the official docs in `node_modules`, and making the skill "much leaner and encouraging Agents to use those docs in `node_modules` directly". The same block says the new skill installs with `npx skills add https://github.com/remix-run/react-router --skill react-router`, and that adding the skill will become part of React Router's CLI when starting a new project. The three per-mode skills below are therefore a frozen snapshot of a maintained idea, not dead content: the mode distinctions they teach still hold, and anyone still on the archived listing gets the same reference tree.

## Installation

Start with the path the publisher currently documents. The archived repository's README points readers at the skill that now ships in the main React Router repository:

```bash
npx skills add https://github.com/remix-run/react-router --skill react-router
```

The archived repository still installs, and it is the only source for the per-mode split. All three commands below appear verbatim in its README:

```bash
npx skills add remix-run/agent-skills
```

```bash
npx skills add remix-run/agent-skills --skill react-router-framework-mode
npx skills add remix-run/agent-skills --skill react-router-data-mode
npx skills add remix-run/agent-skills --skill react-router-declarative-mode
```

The install counts on skills.sh still belong to the archived repository, so the 5.2K combined figure and the per-skill rows below describe that listing, not the replacement skill in remix-run/react-router.

If you would rather place the files yourself, clone the repository and copy the skill directories you want. Copy the whole directory, not just `SKILL.md`: each skill's file routes the agent to topic pages under `references/` that sit beside it.

```bash
git clone https://github.com/remix-run/agent-skills.git
mkdir -p .agents/skills
cp -r agent-skills/skills/react-router-framework-mode .agents/skills/
```

## What It Provides

All three indexed listings clear the 500-install bar, so the table is the whole surface:

| Skill | Installs | Use For |
|---|---|---|
| react-router-framework-mode | 3,649 | Full-stack apps in framework mode: route config in `app/routes.ts`, loaders and actions, error boundaries, SSR, SPA and pre-rendering, middleware, sessions and route type safety |
| react-router-data-mode | 907 | `createBrowserRouter` and `RouterProvider` inside an existing React app: route objects, loaders, actions, `Form`, `useFetcher`, and pending or optimistic UI without the Vite plugin |
| react-router-declarative-mode | 694 | `BrowserRouter` with JSX `<Routes>` and `<Route>`: `Link` and `NavLink` navigation, `useParams`, `useSearchParams`, `useLocation`, and no loaders or actions |

No indexed listings fall below the threshold.

The reference trees are what separate these from a prompt. Framework mode ships twelve reference pages (routing, route modules, special files, data loading, actions, navigation, pending UI, error handling, rendering strategies, middleware, sessions, type safety). Data mode ships seven, declarative mode three. Framework mode also carries a version table, because middleware needs React Router 7.9.0 or later and the core loader and action features need 7.0.0 or later, and it tells the agent to run `npm list react-router` before implementing anything that depends on those versions.

## Why This Matters for Hermes Agents

React Router 7 merged what used to be Remix into the router, so the same import path now covers three different mental models. A model answering from training data mixes them: it writes `createBrowserRouter` for a framework-mode project, or reaches for `loader` in an app that only ever uses `<Route element>`. Each of those mistakes is cheap to make and expensive to find, because the code compiles and then fails at navigation time.

The skills fix that by making mode selection explicit. Each `SKILL.md` opens with a "When to Apply" list that is essentially a mode fingerprint: `app/routes.ts` and `react-router.config.ts` mean framework mode, `createBrowserRouter` means data mode, `<BrowserRouter>` means declarative mode. An agent that reads the right file gets the right API surface for its project.

The reference tables also replace guessing with a lookup. The framework skill's twelve pages cover the parts that are genuinely version-sensitive: `clientLoader` versus `loader`, streaming, `v8_middleware`, cookie sessions, and the auto-generated route types. Asking an agent to invent that is asking it to interpolate between versions.

For Hermes agents the practical gain is routing work that survives review. A `<Form>` that posts to an `action`, a typed `useLoaderData`, a pending state driven by `useNavigation` all come out of the reference pages rather than from memory, and the guidance stays inside one mode instead of blending three.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a new React Router app with SSR" | The framework-mode skill wins on `react-router.config.ts`, and the agent configures routes in `app/routes.ts` with server rendering rather than writing a client-only router |
| "Add data loading to this existing Vite React app" | The data-mode skill applies: `createBrowserRouter`, a `loader` per route, and no framework plugin is introduced |
| "This form submission loses the pending state" | Framework or data mode loads `pending-ui.md` and rewrites the mutation around `useNavigation` or `useFetcher` state instead of a manual `isLoading` flag |
| "Why does my `useParams` return undefined?" | Declarative mode applies, and the routing reference covers nested `<Route path>` matching before any data APIs are suggested |
| "Add auth that survives a refresh" | The framework session reference drives cookie sessions and protected routes, with the middleware page for the 7.9.0 flag path |
| "Upgrade this app to React Router 7" | The version table in framework mode sets the floor at 7.0.0 for loaders and actions and 7.9.0 for middleware, after `npm list react-router` |

## Verification

Read the skill before installing it. All three paths below returned HTTP 200 on the archived repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/remix-run/agent-skills/main/skills/react-router-framework-mode/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/remix-run/agent-skills/main/skills/react-router-data-mode/SKILL.md | head -30
curl -fsSL https://raw.githubusercontent.com/remix-run/agent-skills/main/skills/react-router-declarative-mode/SKILL.md | head -30
```

Each should open with `name:` and `description:` frontmatter and then a "When to Apply" list plus a references table. If the references table is missing, you are reading a stale copy.

After install, confirm the reference directories came across, because a copy that took only `SKILL.md` leaves the agent with the pointers and none of the pages:

```bash
ls .agents/skills/react-router-framework-mode/references | wc -l
```

That count should be 12 for framework mode, 7 for data mode and 3 for declarative mode.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-router-framework-mode | Pass | Pass | Pass |
| react-router-data-mode | Pass | Pass | Pass |
| react-router-declarative-mode | Pass | Pass | Pass |

The payload is markdown: `SKILL.md` plus reference pages, with no scripts, no install hooks and no network calls at run time. The only commands the skills tell an agent to run are `npm list react-router` and ordinary edits to project files.

Two cautions are worth stating. The repository is archived, so a compromised or mistyped fork is a real risk: install from `remix-run/agent-skills` or from `remix-run/react-router`, and treat any other owner as unvetted. And the licence is MIT with a LICENSE file in the repository root, which covers reuse but says nothing about the accuracy of the reference pages.

## Limitations

- Snapshot data, verified 2026-11-07: 5,250 combined installs across 3 indexed listings; 134 GitHub stars; MIT; last pushed 2026-06-18. Counts drift over time.
- The repository is archived. Its README says the skill now lives in remix-run/react-router at `.agents/skills/react-router` and that the skill will ship through React Router's CLI for new projects, so these three per-mode skills receive no further updates.
- The index shape and the current publisher shape disagree: this listing counts three per-mode skills, while the maintained replacement is a single `react-router` skill. Installs recorded here are historical.
- The skills are only as current as React Router 7 was in June 2026. Middleware is flagged as needing 7.9.0, and anything added after the last push is absent.
- Data mode and framework mode overlap heavily, and the two skills differ mainly in the entry point they assume. An agent that loads both can follow the wrong one.
- Nothing enforces any of it: there is no linter, no test and no version check beyond the one command the skill tells the agent to run.

## Related

- [Sergiodxa Agent Skills - Frontend Practice Setup](/hermes/skills/catalog/sergiodxa-agent-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [Frontend God Mode - Design Skills Bundle Setup](/hermes/skills/catalog/frontend-god-mode-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Name the mode in the prompt. "In framework mode" or "using createBrowserRouter" decides which skill loads and removes the only real ambiguity in this suite.
- Install the replacement if you are starting fresh. `npx skills add https://github.com/remix-run/react-router --skill react-router` is the maintained path; use the archived repo only when you want the per-mode split.
- Keep the references. The tables at the end of each `SKILL.md` are the part that carries version-specific detail, and a `SKILL.md`-only copy is mostly a routing hint.
- Ask the agent to run `npm list react-router` first on upgrade work. The framework skill's version table is the cheapest way to stop it recommending middleware on a 7.6 project.
- Pin the React Router minor version in the project. The guidance tracks 7.x conventions, and a pinned version makes any mismatch obvious in review.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
