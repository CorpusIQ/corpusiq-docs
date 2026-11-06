---
title: "Rebyte Skills - Template Setup and Deploy Skills"
description: "rebyteai-template/rebyte-skills: 7.0K combined installs across 50 listings; setup and deploy runbooks for Astro, FastAPI, Axum and Next stacks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rebyte-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "templates", "scaffolding", "deployment"]
---

# Rebyte Skills - Setup Guide

**Source:** [rebyteai-template/rebyte-skills](https://www.skills.sh/rebyteai-template/rebyte-skills) via skills.sh - 7.0K combined installs across 50 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 18 stars, no LICENSE file in the repository root, last pushed 2026-06-16, 51 SKILL.md directories in a flat tree (one per template id plus common/stripe-skill)
**Category:** Starter templates for agents: setup and deploy skills across Astro, FastAPI, Axum, Deno, Express and Next stacks
**Quality Tier:** 🟡 Review - no LICENSE file in the repository root and the sampled skills.sh verdicts include a Fail (tailadmin-nextjs on Gen Agent Trust Hub) plus several Warns.

Rebyte Skills is the eng0 template collection: a repository where every template id carries a runbook that clones a starter project, installs dependencies, builds it and deploys it to Vercel or Netlify. The catalogue is broad for its size, covering landing pages and portfolios (awwwards-landing-page, award-winning-website, magic-portfolio), full-stack starters (nextjs-supabase, nuxt-starter-netlify, tanstack-chat-netlify), backends (fastapi-fullstack, express-typescript-starter, nestjs-typescript-starter, deno-monorepo-template, axum-rust-template, go-backend-clean-architecture), dashboards (tailadmin-nextjs, mantis-react-admin, happiness-dashboard), slide decks (py-intro, denuvo-slides, kubecon-llm-k8s) and payments (stripe-subscription, stripe-one-time-payment).

Two skills carry the shape of the whole set: `setup` initializes a template in an empty project directory (clone, install dependencies, configure environment, verify with a build) and `build-and-deploy` takes a finished project to production (build, deploy to Vercel or Netlify, handle environment variables, run database migrations where applicable). Each listing is a filled-in instance of that pattern for one specific template.

## Installation

The repository ships no installer and no plugin manifest. Its README documents two usage paths, and both are manual. For other code agents it gives these steps verbatim:

```text
1. Navigate to the template directory: eng0-template-skills/[template-id]/
2. Read the relevant skill file: setup/SKILL.md or build-and-deploy/SKILL.md
3. Follow the step-by-step instructions
```

For Claude Code the README states that "Skills are automatically available" and that you describe what you want, for example "Set up the vite-react template in this directory" or "Deploy this project to Vercel". There is no `npx skills add` line in the README and no marketplace manifest at the repository root, so install on a non-Claude agent means cloning the repository and pointing the agent at the template directory.

One layout difference matters before you copy anything: the README describes a `setup/` and `build-and-deploy/` split, but the current tree holds a single `SKILL.md` at the root of each template id, with the whole runbook inline. The awwwards-landing-page skill, for example, opens with the clone step it runs for you:

```bash
git clone --depth 1 https://github.com/Eng0AI/awwwards-landing-page-template.git .
```

followed by `npm install`, `npm run build`, and a Vercel deploy sequence that carries the repository's own warning: use `vercel build --prod` then `vercel deploy --prebuilt --prod`, never `vercel --prod` directly.

## What It Provides

Eight listings clear the 100-install threshold. Three are landing page templates, three are financial or market data skills, one builds charts, and one is a backend starter.

| Skill | Installs | Use For |
|---|---|---|
| awwwards-landing-page | 1,338 | Designer portfolio build: Next.js with Locomotive Scroll, GSAP and Framer Motion, then build and deploy |
| financial-deep-research | 982 | Multi-source financial research with verified claims, regulatory compliance tracking and market comparisons |
| gsap-awwwards-website | 823 | SPYLT product landing page: GSAP scroll animation, React 19 and Tailwind CSS 4 |
| market-data | 369 | Market data over SQL: bulk historical 1-minute OHLCV, SEC XBRL fundamentals and news lookups |
| award-winning-website | 363 | Gaming landing page with GSAP scroll animations, 3D effects and video storytelling |
| echarts | 332 | pyecharts chart construction, chart options and self-contained HTML report output |
| sec-edgar-skill | 234 | SEC filing analysis with EdgarTools: 10-K, 10-Q and 8-K reading, insider activity, revenue trends |
| fastapi-backend-template | 219 | FastAPI backend runbook: PostgreSQL, async SQLAlchemy 2.0, Alembic migrations and Docker |

The remaining 42 indexed listings range from 41 to 88 installs. They are the rest of the template catalogue: go-backend-clean-architecture, developer-portfolio, chrome-extension-boilerplate-react-vite, web-app-builder, tailadmin-nextjs, mantis-react-admin, fastapi-fullstack, vite-react, vite-vue, nextjs-supabase, magic-portfolio, stripe-subscription, seo-analytics, ai-chatbot, axum-rust-template, astrowind, tanstack-chat-netlify, nuxt-starter-netlify, ncine-presentation, happiness-dashboard, denuvo-slides, kubecon-llm-k8s, deep-research, langchain-agent, natural-language-postgres, nano-banana, stripe-one-time-payment, langchain-retrieval-agent, nestjs-typescript-starter, formsmd-builder, nextjs-blog-netlify, content-ops-netlify, langchain-retrieval, gatsby-ecommerce-netlify, dillion-portfolio, screwfast, py-intro, deno-monorepo-template, express-mcp, astro-supabase-netlify, express-typescript-starter and natural-language-postgres-presentation.

## Why This Matters for Hermes Agents

Scaffolding is where an agent's confidence costs the most time. Cloning a template, wiring environment variables, picking a package manager, running the first build and getting the deploy flags right is a sequence with many small failure points, and a general-purpose agent improvises all of them. A template runbook replaces improvisation with the exact commands the template author used.

The stacks cover most of the "build me a starter" requests a Hermes agent receives: Astro, Next.js, Nuxt, Vite React and Vue, FastAPI, Express, NestJS, Deno, Axum and Go clean architecture, each with its own conventions for ports, package managers and directories.

The deploy half is the part most useful to copy. The Vercel and Netlify sections carry the quirks, including the prebuilt deploy sequence and the environment variable placement, which are exactly the details that break a first deploy. A runbook that names the token variable you must set is worth more than a summary of what deployment is.

The finance skills are a second, separate cluster, and they are reusable outside the templates. `sec-edgar-skill` documents filing access through EdgarTools, `financial-deep-research` imposes a multi-source verification discipline, `market-data` documents a SQL interface over price, fundamentals and news data, and `echarts` produces charts. Together they let an agent answer a financial question with cited sources and a rendered chart instead of prose.

## Usage

| You say | What happens |
|---|---|
| "Set up the vite-react template in this directory" | The template runbook clones the starter, installs dependencies and verifies with a build |
| "Deploy this project to Vercel" | The build-and-deploy path runs the prebuilt Vercel sequence and checks the environment variables |
| "Initialize the ai-chatbot template here" | ai-chatbot clones the Next.js 15 chat starter with Auth.js and Drizzle and wires the models |
| "Scaffold a FastAPI backend with migrations" | fastapi-backend-template sets up PostgreSQL, async SQLAlchemy 2.0, Alembic and Docker |
| "Build me a landing page with scroll animation" | awwwards-landing-page or award-winning-website supplies the GSAP structure and the deployed shape |
| "Analyse this company's 10-K" | sec-edgar-skill pulls the filing through EdgarTools and walks revenue and insider sections |
| "Chart this revenue series" | echarts builds the pyecharts chart and writes a self-contained HTML report |

## Verification

Review a runbook before you let an agent execute it. Both paths below returned HTTP 200 on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/rebyteai-template/rebyte-skills/main/awwwards-landing-page/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/rebyteai-template/rebyte-skills/main/financial-deep-research/SKILL.md | head -5
```

The first should open with `name: awwwards-landing-page` and a one-line description naming Locomotive Scroll, GSAP and Framer Motion, then the Tech Stack block. The second should open with `name: financial-deep-research` and a longer description that names multi-source synthesis and regulatory compliance tracking.

There is no agent skills directory to inspect after install, because nothing installs into one. Confirm the checkout instead:

```bash
find . -name SKILL.md | wc -l
```

That should print 51 from the repository root, one file per template id plus `common/stripe-skill/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| awwwards-landing-page | Warn | Pass | Warn |
| tailadmin-nextjs | Fail | Pass | Warn |
| nuxt-starter-netlify | Pass | Pass | Pass |
| formsmd-builder | Pass | Pass | Pass |
| natural-language-postgres-presentation | Warn | Warn | Warn |

Treat every runbook in this repository as an execution surface rather than a document. The skills tell an agent to `git clone` a template repository (the awwwards skill clones `github.com/Eng0AI/awwwards-landing-page-template`), run `npm install` from that template's tree, and deploy with a token in the environment. That means three trust decisions per template: the skill text, the template repository it clones, and the package tree it installs.

The tailadmin-nextjs Fail is the verdict to read before using that template. A Fail on Gen Agent Trust Hub is not a statement about the code quality of TailAdmin itself, but it is a reason to read the full security page rather than inherit the result.

There is no LICENSE file in the repository root, so the terms for reusing the skill text are simply not stated. Treat redistribution as unresolved until the maintainer adds one.

## Limitations

- Snapshot data, verified 2026-11-06: 6,971 combined installs across 50 indexed listings; 18 GitHub stars; no licence file; last pushed 2026-06-16. Counts drift over time.
- No LICENSE file in the repository root. Nothing in the tree states the terms for copying, adapting or redistributing the skill text.
- The install index and the tree differ by one. 50 listings carry install counts, the tree holds 51 SKILL.md files, and the extra one is `common/stripe-skill/SKILL.md`, which has no listing of its own.
- The README describes a `setup/` and `build-and-deploy/` directory per template. The current tree does not have that split: each template id carries one SKILL.md with the runbook inline.
- Nine indexed listings are absent from the README's template table: deep-research, echarts, financial-deep-research, formsmd-builder, market-data, nano-banana, sec-edgar-skill, seo-analytics and web-app-builder. Their names are resolved from their own SKILL.md files, not from the README.
- Deployment needs credentials the skills do not provide. The Vercel and Netlify sections assume a token in the environment, and database migrations assume a reachable database.
- The repository has no commits after 2026-06-16, so template dependencies and framework versions are pinned to that date.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Harmony Next Skills - Setup Guide](/hermes/skills/catalog/harmony-next-skills-setup)
- [Svelte AI Tools - Official Svelte and SvelteKit Setup](/hermes/skills/catalog/svelte-ai-tools-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the template id, not the stack. "Scaffold nextjs-supabase" points the agent at one directory; "build me a Next.js app with Supabase" makes it choose and improvise.
- Read the deploy section of the runbook before the agent touches production. The prebuilt sequence deploys the artifact you built locally, and the skill warns against the flag that rebuilds on the platform instead.
- Let the runbook clone into an empty directory. The awwwards skill handles a non-empty target by cloning to a temp directory and moving the files in, which is a step the skill added for a reason.
- Keep the stack's own instructions intact when the project is full stack. fastapi-fullstack and nextjs-supabase assume different data layers and runtimes, so borrow the deploy section from one and the application section from the other, not both wholesale.
- Use the finance cluster on its own. sec-edgar-skill, market-data and echarts work without any template, which makes them the cheapest way to test whether this repository's instruction style suits your agent.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
