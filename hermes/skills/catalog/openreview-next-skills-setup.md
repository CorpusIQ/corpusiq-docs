---
title: "OpenReview Next.js Skills - Vercel Engineering Suite"
description: "vercel-labs/openreview on skills.sh: 11.0K combined installs across 7 listings; Next.js, React and UI review skills from Vercel Labs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openreview-next-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "nextjs", "react", "vercel", "code review"]
---

# OpenReview Next.js Skills - Setup Guide

**Source:** [vercel-labs/openreview](https://www.skills.sh/vercel-labs/openreview) via skills.sh - 11.0K combined installs across 7 indexed listings; snapshot 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 1,705 stars, no licence declared (the metadata licence field is null), `main` branch, last pushed 2026-03-06, 180 files with 7 `SKILL.md` files under `.agents/skills/`, one directory per skill
**Category:** Frontend and web: Next.js conventions, Cache Components, framework upgrades, React and React Native performance, UI review
**Quality Tier:** 🟡 Yellow - all seven listings come back Pass on all three scanners, but the repository declares no licence, so reuse terms are undefined outside the skills CLI.

The repository is named for the product it contains: OpenReview is a self-hosted AI code review bot, an open-source project from Vercel Labs that you deploy to Vercel, connect to a GitHub App, and trigger by mentioning `@openreview` in a pull request comment. The README marks it as beta, built internally to exercise Vercel technologies together, and warns about rough edges and breaking changes.

What gets installed here is a different artifact. The seven indexed skills are the bot's built-in review skills, sitting in `.agents/skills/` at the repository root, and they are plain Next.js, React and React Native engineering guidance. Installing them gives an agent the review rules without the bot: no Vercel deployment, no GitHub App, no Claude call. That distinction is the whole reason the install numbers look odd against the repository description, 11,021 installs of review rules against 1,705 stars on a code review product.

## Installation

The skills CLI command from the index names one skill at a time:

```bash
npx skills add https://github.com/vercel-labs/openreview --skill next-best-practices
```

Each of the seven listings installs the same way with a different `--skill` value: `next-cache-components`, `next-upgrade`, `vercel-react-best-practices`, `web-design-guidelines`, `vercel-composition-patterns` or `vercel-react-native-skills`.

There is no top-level `skills/` directory. The layout is `.agents/skills/<name>/SKILL.md`, which is also where the README says its own agent discovers skills at runtime, and the same path a custom skill would use. The README documents no manual copy step for these skills, so a hand install means placing one of those directories into your agent's skills directory unchanged.

The README's own Setup section is about the bot, not the skills: deploy to Vercel, create a GitHub App with a webhook at `/api/webhooks`, grant Contents, Issues and Pull requests read and write plus Metadata read-only, subscribe to issue comment and pull request review comment events, then set the environment variables. Local development of the bot is `bun install` followed by `bun dev`. None of that is needed to use the skills.

## What It Provides

The threshold for this guide is zero installs, so all seven indexed listings appear below:

| Skill | Installs | Use For |
|---|---|---|
| next-best-practices | 6,593 | Next.js file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image and font optimization, bundling |
| next-cache-components | 1,926 | Next.js 16 Cache Components: partial prerendering, the use cache directive, cacheLife, cacheTag and updateTag |
| next-upgrade | 1,123 | Upgrading Next.js to the current version along the official migration guides and codemods |
| vercel-react-best-practices | 396 | React and Next.js performance guidelines for writing, reviewing or refactoring components, data fetching and bundles |
| web-design-guidelines | 374 | Reviewing UI code against the Web Interface Guidelines, including accessibility and UX audits |
| vercel-composition-patterns | 367 | React composition patterns for boolean prop proliferation, compound components, render props and context providers, including React 19 API changes |
| vercel-react-native-skills | 242 | React Native and Expo practice for performant mobile apps: list performance, animations, native modules |

All 7 indexed listings clear the zero-install threshold; none fall below it.

The weight sits in one skill. `next-best-practices` at 6,593 installs is more than half of the suite, and it is the broadest: file conventions, server and client boundaries, data access, async APIs, metadata, errors, route handlers, images, fonts and bundling in one body of rules. `next-cache-components` is the longest file of the seven at 411 lines, which fits a topic where partial prerendering, `use cache`, `cacheLife`, `cacheTag` and `updateTag` interact and the failure mode is a page that silently renders dynamically.

The other five are narrow by design. `next-upgrade` is 50 lines and routes the agent to migration guides and codemods rather than restating them, which means it depends on an external document staying current. `web-design-guidelines` is the shortest at 39 lines because it points at the Web Interface Guidelines as the standard and describes the review. `vercel-react-native-skills` is the only listing that leaves the web target, and it is also the smallest at 242 installs.

## Why This Matters for Hermes Agents

Next.js review is a task where a model without rules produces a plausible, wrong answer: a client component where a server component belonged, a fetch that defeats caching, a `useEffect` that duplicates data the router already had. The `next-best-practices` body turns those into checks, which is the form guidance survives in a long context.

The Cache Components skill covers the part of Next.js 16 that most training data predates. Partial prerendering, `use cache` and the tag invalidation API are recent enough that a model will reach for the older `revalidate` and `dynamic` answers, and a wrong cache answer is expensive in production: it either ships stale content or turns every request dynamic.

The upgrade skill is the one that changes behaviour rather than opinion. It tells the agent to follow the official migration guide and codemods, which is the difference between a codemod run you can review as a diff and a hand-rewrite of a routing layer.

Two of the seven are review skills in the narrow sense. `web-design-guidelines` and `vercel-react-best-practices` exist to audit code that already exists, so they fit a Hermes workflow that opens a pull request, reads the diff and posts findings, with no separate review tool.

The honest counterweight: these skills describe what to check, not what to run. Nothing here lints, tests or executes your project, and none of it is a substitute for the bot if you want automated pull request comments. You are installing a reviewer's checklist and wiring it to your own reading.

## Usage

| You say | What happens |
|---|---|
| "Review this pull request against Next.js conventions" | Walks the next-best-practices rules: file conventions, server and client boundaries, data patterns, async APIs, metadata and error handling, and reports violations per file |
| "This page is rendering dynamically even though nothing user-specific is on it" | Switches to next-cache-components and checks whether the route is set up for partial prerendering, whether the data read is inside `use cache`, and which tag invalidation call the write path uses |
| "Upgrade this app to the current Next.js version" | Runs next-upgrade: identifies the current version, points at the matching migration guide, and applies the codemods the guide names rather than rewriting by hand |
| "The dashboard re-renders on every keystroke" | Applies vercel-react-best-practices to component structure, memoization boundaries, data fetching and bundle size, then proposes the smallest change that fixes the render |
| "Audit the settings page for accessibility" | Uses web-design-guidelines to review the markup against the Web Interface Guidelines and returns findings with the element and the rule |
| "This component takes eleven boolean props" | Applies vercel-composition-patterns: compound components, render props or context, plus the React 19 API changes, instead of adding a twelfth prop |
| "Our React Native feed drops frames while scrolling" | Uses vercel-react-native-skills on list virtualization, image and animation work, and native module boundaries |

## Verification

Read one skill before installing any of them. This URL returns 200 and is the largest listing in the suite:

```bash
curl -fsSL https://raw.githubusercontent.com/vercel-labs/openreview/main/.agents/skills/next-best-practices/SKILL.md | head -6
```

The frontmatter holds `name: next-best-practices`, the same description string the index shows, and `user-invocable: false`, which is a signal that the skill is written to be loaded by a review agent rather than typed as a slash command. The body opens with a `# Next.js Best Practices` heading and a line telling the reader to apply the rules when writing or reviewing Next.js code, followed by a file conventions section.

The narrow skills are worth one fetch each, because a short file can be a pointer rather than a skill:

```bash
curl -fsSL https://raw.githubusercontent.com/vercel-labs/openreview/main/.agents/skills/web-design-guidelines/SKILL.md | wc -l
```

That returns 39, the shortest of the seven. If the path 404s, the layout moved away from `.agents/skills/` and the install command's `--skill` names no longer resolve.

After an install, confirm the directory landed under the name the client indexes:

```bash
test -f ~/.claude/skills/next-best-practices/SKILL.md && echo ok
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| next-best-practices | Pass | Pass | Pass |
| next-cache-components | Pass | Pass | Pass |
| next-upgrade | Pass | Pass | Pass |
| vercel-react-best-practices | Pass | Pass | Pass |
| web-design-guidelines | Pass | Pass | Pass |
| vercel-composition-patterns | Pass | Pass | Pass |
| vercel-react-native-skills | Pass | Pass | Pass |

All seven are Markdown instruction files. There is no installer, no script and no network call in a skill directory, and three scanners returning Pass on every listing reflects that absence of executable payload rather than an audit of the code an agent will write from the rules.

The repository around them is a different surface. If you deploy OpenReview itself, you create a GitHub App with read and write on contents, issues and pull requests, install it on repositories, and let a model run inside a sandbox that clones your code, runs your tooling, commits and pushes to the pull request branch. Pull request bodies, comments and diffs are attacker-controlled text in that loop, and the agent has push rights, so a prompt injection inside a diff is a write to your branch. Scope the App to named repositories, review what the sandbox can reach, and treat the bot's commits like any other contributor's.

Secrets are the second half. The deployment needs `ANTHROPIC_API_KEY`, `GITHUB_APP_ID`, `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY` (with escaped newlines), `GITHUB_APP_WEBHOOK_SECRET` and an optional `REDIS_URL` for persistent state. The private key is the write credential for every installed repository; keep it in the hosting environment rather than in the repository, and rotate the App key if it leaks. Without `REDIS_URL` state falls back to memory, which is fine for a trial and wrong for anything you depend on.

One habit covers the skills themselves. `next-upgrade` and the review skills propose edits to files, so commit or stash before letting an agent apply them, and read the diff. A clean scanner verdict says nothing about whether a codemod was appropriate for your tree.

## Limitations

- Snapshot data, verified 2026-11-09: 11,021 combined installs across 7 indexed listings; 1,705 GitHub stars; no licence declared; last pushed 2026-03-06. Counts drift over time.
- The repository declares no licence. The GitHub licence field is null, and the README's own License section naming MIT is a statement without a detected licence file behind it, so reuse, redistribution and derivative rules are undefined. Treat the skills as all rights reserved until the publisher resolves it.
- Last push was 2026-03-06, eight months before this snapshot. The skills target Next.js 16 Cache Components and React 19, both of which are moving, so the guidance ages faster than the repository does.
- The name misleads. The repository is a code review bot; the indexed skills are its review rules for Next.js, React and React Native. Nothing here deploys the bot, and installing all seven does not give you `@openreview` in a pull request.
- The README's Setup section covers the deployment, not skill installation, and it lists no per-agent install table. The only install path this guide can state is the skills CLI command from the index.
- 11,021 installs against 1,705 stars is a distribution signal, not an evaluation one, and the count is dominated by `next-best-practices` at 6,593. The four smallest listings sit between 242 and 396 installs.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)
- [Vercel Plugin Skills - Full Vercel Ecosystem Agent Setup](/hermes/skills/catalog/vercel-plugin-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `next-best-practices` alone if you only want one. It carries more than half of the suite's installs and covers the conventions the other Next.js skills assume.
- Check the framework version before trusting the cache guidance. `next-cache-components` is written for Next.js 16 and its directives do not exist in earlier releases.
- Pair `next-upgrade` with a clean tree. It routes to codemods, and a codemod on top of uncommitted work is the one way this suite can cost you a day.
- Use `web-design-guidelines` as a second pass, not a first. It reviews existing markup against the Web Interface Guidelines, so it has nothing to say about a page that does not exist yet.
- Keep the skills and the bot separate in your head. Installing rules for your own agent needs no GitHub App, no Vercel project and no Anthropic key.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
