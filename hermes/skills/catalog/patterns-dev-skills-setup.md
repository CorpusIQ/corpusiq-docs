---
title: "Patterns.dev Skills - UI and Rendering Patterns Setup"
description: "patternsdev/skills: 53.7K combined installs. 58 focused Agent Skills covering JS, React and Vue rendering, performance and design patterns."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/patterns-dev-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "react", "javascript", "web performance"]
---

# Patterns.dev Skills - Setup Guide

**Source:** [patternsdev/skills](https://www.skills.sh/patternsdev/skills) via skills.sh - 53.7K combined installs across 58 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [patternsdev/skills](https://github.com/patternsdev/skills) - 258 stars, no LICENSE file at root, branch main, last pushed 2026-04-15; 58 `SKILL.md` files, one per pattern, across `javascript/` (29), `react/` (18) and `vue/` (11)

**Category:** Frontend pattern reference, rendering strategy and web performance guidance

**Quality Tier:** 🟢 Green - all five sampled skills Pass on all three auditors and the suite is markdown only, but the repository carries no LICENSE file at root and has not been pushed since 2026-04-15

patterns.dev publishes its pattern library as Agent Skills, and the repository is deliberately flat: 58 directories, each holding a single `SKILL.md` for a single pattern, grouped into three trees by technology. The README is explicit about the trade it makes against the website. The site version carries interactive CodeSandbox embeds, animated videos, diagrams and visual walkthroughs; the skills are agent-optimized and stripped down to prose and code blocks, with no images and no iframes.

Each card is written to be read by an agent rather than skimmed by a human. Frontmatter carries a `description` that names the trigger situation, `paths` globs for the file types the pattern applies to, and `related_skills` links to neighbours, and the body typically opens with a "When to Use" block followed by "Instructions" and a detailed "Details" section that keeps the source article's reasoning. The distribution is narrow: 20 of the 58 listings sit at or above 1,101 installs, the top 16 of those fall inside a 564 install band from 1,495 to 2,059, and the remaining 38 trail off to 185. That shape reads as stack-level installs of a tree rather than a popularity ranking of individual patterns, which is worth remembering before you read anything into the ordering.

## Installation

The README's quick start installs a whole technology tree at once:

```bash
npx skills add PatternsDev/skills/javascript
npx skills add PatternsDev/skills/react
npx skills add PatternsDev/skills/vue
```

Single patterns install by folder name:

```bash
npx skills add PatternsDev/skills --skill hooks-pattern
npx skills add PatternsDev/skills --skill singleton-pattern
npx skills add PatternsDev/skills --skill composables
npx skills add PatternsDev/skills --skill ai-ui-patterns
```

The README flags the trap in that second form: `--skill` takes the skill folder name (`hooks-pattern`, `ai-ui-patterns`), not the path (`react/hooks-pattern`).

The manual route is a directory copy, which is also the durable route for a Hermes profile:

```bash
cp -r react/hooks-pattern ~/.cursor/skills/
cp -r javascript/singleton-pattern ~/.cursor/skills/
cp -r vue/composables ~/.cursor/skills/
```

The README lists `.cursor/skills/`, `.claude/skills/` and `.codex/skills/` as targets; the same copy works with `~/.hermes/profiles/corpusiq/skills/` substituted for the client directory. The checkout verified for this guide holds exactly 58 `SKILL.md` files, 29 under `javascript/`, 18 under `react/` and 11 under `vue/`, which matches the 58 indexed listings one for one.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ai-ui-patterns | 2,059 | Design patterns for AI-powered React interfaces: chat surfaces, streaming responses, assistants and AI-specific interaction flows |
| react-2026 | 2,026 | Picking a modern React stack: framework, build tool, routing, state management and AI integration guidance for a new or modernized app |
| dynamic-import | 1,578 | Lazy loading modules with import() so code that is not needed at startup stays out of the initial bundle |
| bundle-splitting | 1,574 | Splitting a large JavaScript bundle into smaller chunks to cut load time and improve FCP and LCP |
| compression | 1,568 | Gzip and Brotli compression of scripts to reduce network transfer time in production builds |
| loading-sequence | 1,562 | Reordering how critical resources are discovered and loaded to improve FCP, LCP and FID |
| preload | 1,560 | Preloading fonts, hero images and key scripts that would otherwise be discovered late in the loading waterfall |
| import-on-interaction | 1,553 | Loading heavy components or libraries on click, hover or form input instead of at page load |
| prefetch | 1,549 | Fetching and caching resources the user will likely need next, during browser idle time |
| import-on-visibility | 1,540 | Intersection Observer loading of below-the-fold components and images once they scroll into view |
| third-party | 1,533 | Reducing the cost that analytics, ads and widget scripts add to page load and Core Web Vitals |
| virtual-lists | 1,529 | Windowing long lists and tables so hundreds or thousands of rows render without scroll jank |
| route-based | 1,526 | Splitting code per route so a single-page app does not ship every feature bundle up front |
| tree-shaking | 1,522 | Eliminating unused exports at build time to shrink the final bundle |
| prpl | 1,500 | The PRPL initial load pattern for progressive web apps: push critical resources, render the initial route, pre-cache the rest, lazy load on demand |
| static-import | 1,495 | Static ES2015 import syntax for dependencies needed at load time that benefit from static analysis and tree shaking |
| hooks-pattern | 1,141 | Custom React hooks that extract shared stateful logic such as form handling, subscriptions and side effects |
| react-composition-2026 | 1,121 | Modern React composition patterns for component APIs, shared UI libraries and refactoring prop-heavy components |
| presentational-container-pattern | 1,119 | Separating data fetching and business logic from rendering so views stay testable and reusable |
| react-render-optimization | 1,101 | Cutting unnecessary re-renders, tightening memoization, improving state design and diagnosing React performance issues |

The remaining 38 indexed listings range from 185 to 1,080 installs.

## Why This Matters for Hermes Agents

Most frontend guidance for agents ships as one large rules file, which means a project that needs two rules pays for all of them. This suite is 58 separable cards and the install unit is a directory, so a Hermes profile working on a React dashboard can carry `react-render-optimization`, `bundle-splitting` and `virtual-lists` without dragging the Vue tree into every session.

The metadata is what makes selective install practical. Each card names its trigger in `description` and its file scope in `paths:` globs, so a harness that routes or scopes skills has something machine-readable to key on instead of a prose preamble, and `related_skills` lets an agent walk sideways to the neighbouring pattern when the first card is close but not exact.

The "When NOT to Use" blocks are the part most skill suites skip, and they are the part that keeps an agent from over-applying a pattern. The `prefetch` card, for instance, says plainly not to prefetch resources that are unlikely to be needed, not to prefetch on metered connections, and not to prefetch content that will be stale by the time it is used, which is exactly the correction a model needs when it has learned that prefetching is good.

Rendering strategy is where the suite is strongest as an agent reference. Client-side rendering, server-side rendering, static rendering, incremental static rendering, streaming SSR, progressive hydration, selective hydration and React Server Components are eight separate cards rather than one paragraph, so an agent asked whether a page should be ISR or streamed can read one file and answer with a named tradeoff instead of a preference.

The cards also stay framework-agnostic on purpose. The repository's own positioning note contrasts this with Vercel's Next.js-first rules: code splitting here is `React.lazy()` with `Suspense` rather than Next.js-specific APIs, data fetching is taught through TanStack Query and SWR, and bundle work uses Vite config and Rollup `manualChunks`, with a dedicated `vite-bundle-optimization` card for the Vite case.

Two caveats belong with the recommendation. Nothing here executes: there are no scripts, hooks, MCP servers or install-time actions in the repository, so the payload is instructions a model reads, and the value is exactly the quality of that prose. And the whole tree is 582 KB of markdown with the largest single card at 28 KB, which is real context if you install the three trees wholesale rather than the handful of patterns your project actually touches.

## Usage

| You say | What happens |
|---|---|
| "The dashboard re-renders on every keystroke" | The agent pulls `react-render-optimization`, which orders its patterns by impact and asks for the biggest wins before micro-optimization. |
| "The bundle is too big and LCP is bad" | `bundle-splitting`, `tree-shaking`, `dynamic-import` and `compression` cover the build-level change each one needs, from `manualChunks` to Brotli. |
| "Should this page be ISR or streaming SSR?" | The rendering cards state when each strategy applies, so the answer comes back as a named tradeoff with the framework requirement attached. |
| "Our analytics tag is tanking Core Web Vitals" | `third-party` says to use `async` or `defer`, to lazy-load embeds behind a facade, and to keep the critical path free of vendor scripts. |
| "The 5,000 row table janks when I scroll" | `virtual-lists` explains windowing and points at `react-window` with `react-window-infinite-loader` for the incremental case. |
| "We are starting a new React app, what stack?" | `react-2026` recommends a framework for SSR or SEO, Vite plus TanStack Router for SPAs and dashboards, and TanStack Query for server state. |
| "Review this Vue component" | If the `vue/` tree is installed, `composables`, `script-setup` and `provide-inject` carry the equivalent guidance for Vue. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/patternsdev/skills/main/react/ai-ui-patterns/SKILL.md
```

After a copy lands in the profile, confirm that the directories are present and that the frontmatter survived the copy:

```bash
find ~/.hermes/profiles/corpusiq/skills -name SKILL.md | wc -l
grep -h '^name:' ~/.hermes/profiles/corpusiq/skills/*/SKILL.md | sort
head -14 ~/.hermes/profiles/corpusiq/skills/hooks-pattern/SKILL.md
```

The count should equal the number of directories you copied, and a tree install should read 58. The `head` output should show `name: hooks-pattern`, the one-line `description`, the `paths` globs and `license: MIT`; if the `description` is missing, the copy took a file that is not a card and the skill will not route.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ai-ui-patterns | Pass | Pass | Pass |
| react-2026 | Pass | Pass | Pass |
| dynamic-import | Pass | Pass | Pass |
| bundle-splitting | Pass | Pass | Pass |
| renderless-components | Pass | Pass | Pass |

All five sampled listings Pass all three auditors, and there is no Warn and no Fail anywhere in the sample, so nothing here needs a warning stated before the table. The qualification is sample size: five of 58 listings were checked, and the rest carry no audit result in this guide either way.

The risk surface is small and it is textual. The repository holds markdown only, with no `scripts/`, no install hook, no network call and no MCP server, so a card cannot execute anything on its own; what it can do is steer an agent toward a technique, which is why the sampling is worth doing but is not a substitute for reading the card you install.

The licence is the item to settle before you redistribute. There is no LICENSE file at the root, GitHub reports no license field, and yet all 58 `SKILL.md` files declare `license: MIT` in their frontmatter. That per-file declaration is the only grant on offer, so a profile that copies the text for internal use is on firm ground while anyone vendoring or republishing the prose should get the terms confirmed first.

## Limitations

- Snapshot data, verified 2026-10-30: 53,715 combined installs across 58 indexed listings; 258 GitHub stars; no LICENSE file at root; last pushed 2026-04-15. Counts drift over time.
- There is no LICENSE file at the root of the repository. Every one of the 58 `SKILL.md` files declares `license: MIT`, but the repository as a whole ships no licence file and GitHub reports no field, so the per-file declaration is the only grant and a release that depends on the licence should have it confirmed in writing.
- The repository is stale. Last push 2026-04-15 is more than six months before this snapshot, and the body of the `react-2026` card is written to 2025 stack guidance, so version-specific claims about React 19 APIs, Vite configuration and TanStack majors should be re-checked against current documentation rather than trusted as current.
- The counts are not a ranking. All 58 listings sit between 185 and 2,059 installs and the top 16 fall inside a 564 install band, which looks like whole-tree installs rather than per-pattern demand; judge a card by its body, not by the number beside it.
- A whole-tree install is expensive context. The 58 cards total 582 KB of markdown and the largest single card is 28 KB, so a three-tree install puts every rendering, performance and design pattern in reach at once.
- The cards teach rather than check. There is no linter, no profiler and no build integration, so an agent can quote the pattern correctly and still apply it to the wrong problem; the "When NOT to Use" blocks are the only guard rail and they are prose.

## Related

- [PStack Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/pstack-setup)
- [Ship Shit Dev Skills - 14 Command Routers Setup](/hermes/skills/catalog/shipshitdev-skills-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by folder, not by tree. `npx skills add PatternsDev/skills --skill virtual-lists` costs one card of context; `npx skills add PatternsDev/skills/react` costs 18 cards and roughly 215 KB.
- Read the "When NOT to Use" block before the instructions. It is short, it is the reason these cards do not become blanket advice, and the `prefetch` and `preload` pair is a good demonstration of two patterns that look interchangeable until you read the exclusions.
- Pair the design patterns with the performance ones in the same session. `hooks-pattern` plus `react-render-optimization` answers "is this re-render my state design or my component shape" without a second lookup.
- Skip `react-2026` for version questions and use it for stack shape. The card is useful for the framework, router and state-management decision, but its version-specific detail predates the snapshot.
- Keep the copy inside the profile skills directory and pin the commit you copied from. The repository has not moved since 2026-04-15, so re-checking for updates is cheap and a stale vendored copy is the likelier failure.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
