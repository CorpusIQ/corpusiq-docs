---
title: "Asyraf Hussin Skills - Clean Code Suite"
description: "asyrafhussin/agent-skills: 29.0K combined installs. Twenty-four rule-based skills for Laravel, PHP, React, testing, SEO and technical debt audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/asyrafhussin-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "laravel", "php", "code review"]
---

# Asyraf Hussin Skills - Setup Guide

**Source:** [asyrafhussin/agent-skills](https://www.skills.sh/asyrafhussin/agent-skills) via skills.sh - 29.0K combined installs across 24 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [asyrafhussin/agent-skills](https://github.com/asyrafhussin/agent-skills) - 95 stars, MIT, branch main, last pushed 2026-08-27; 24 skill directories under `skills/`, each holding `SKILL.md`, `AGENTS.md`, a `rules/` folder and `metadata.json`, 768 files and 6.5 MB in total

**Category:** Engineering standards for agents: clean code, review checklists, architecture and delivery discipline

**Quality Tier:** 🟡 Yellow - four of the five sampled skills Pass all three auditors, but Socket marks `web-design-guidelines` as Warn

This repository is the most conventional pack in the batch, and that is its selling point. Each of the 24 skills is a rulebook: a numbered set of rules grouped into categories, with each rule carrying an incorrect and a correct example, a rationale, and an impact level. `laravel-owasp-security` audits against OWASP Top 10 for a Laravel and React/Inertia stack, `technical-debt` produces a ranked debt ledger scored by effort and impact on a P0 to P3 scale, and `code-slop` classifies a diff as CLEAN, SUSPICIOUS, INFLATED or CRITICAL. An agent that reads these does not get opinions, it gets a checklist with a verdict at the end.

The stack is narrower than the title suggests, and that narrowness is deliberate: PHP 8.0 through 8.5, Laravel 13 on MySQL, React with Vite or Inertia, TypeScript, Tailwind and Playwright. The frontmatter pins those versions explicitly, with `laravelVersion: "13.x"` and `phpVersion: "8.3+"` on the Laravel skills and `pestVersion: "4.x"` on `laravel-testing`, so an agent knows which generation of advice it is reading. If your stack is a different PHP or Laravel major, expect to translate.

## Installation

The README recommends the skills CLI, which handles scope and agent selection for you:

```bash
npx skills add AsyrafHussin/agent-skills
```

A single skill, several named skills, a global install, or a listing without installing:

```bash
npx skills add AsyrafHussin/agent-skills --skill laravel-best-practices
npx skills add AsyrafHussin/agent-skills --skill laravel-best-practices --skill seo-best-practices
npx skills add AsyrafHussin/agent-skills -g
npx skills add AsyrafHussin/agent-skills -a claude-code
npx skills add AsyrafHussin/agent-skills --list
```

The manual route is a clone and a copy, which is also the route that works for Hermes:

```bash
git clone https://github.com/AsyrafHussin/agent-skills.git
cp -r agent-skills/skills/* .claude/skills/
cp -r agent-skills/skills/laravel-best-practices .claude/skills/
```

Swap the destination for this profile and the copy is durable:

```bash
git clone --depth 1 https://github.com/AsyrafHussin/agent-skills.git /tmp/asyraf-skills
cp -r /tmp/asyraf-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

All 24 directories land, each with its `rules/` folder, which is where most of the content lives; a copy that takes only `SKILL.md` loses the examples. The README's management commands work against the CLI install rather than a copied directory: `npx skills list`, `npx skills find laravel`, `npx skills remove` and `npx skills update`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| php-best-practices | 3,721 | PHP 8.0 through 8.5: strict types, enums, readonly, property hooks, PSR-4 and PSR-12, SOLID, error handling and version-aware feature advice across 51 rules. |
| react-vite-best-practices | 2,902 | React on Vite: build configuration, code splitting, lazy loading, HMR, asset handling and bundle analysis across 23 rules. |
| laravel-best-practices | 2,310 | Laravel 13 conventions: controllers, models, migrations, validation, services and application structure across 31 rules in 7 categories. |
| laravel-inertia-react | 1,987 | Laravel with Inertia.js and React: page components, `useForm` handling, shared data and persistent layouts. |
| clean-code-principles | 1,862 | Language-agnostic SOLID, DRY, KISS and design-pattern review for architecture conversations, quality checks and refactors. |
| typescript-react-patterns | 1,093 | Typed React: component props, hooks, events, refs, generics, context and utility types across 33 rules in 7 categories. |
| laravel-database-optimization | 1,076 | Eloquent queries, N+1 detection, indexing, Redis caching, pagination and transactions across 33 rules in 9 categories. |
| laravel-owasp-security | 1,034 | OWASP Top 10 audit and secure coding for Laravel with React/Inertia: authentication, payments, file uploads and API design. |
| tailwind-best-practices | 979 | Tailwind 3.4 and 4: responsive design, dark mode, reusable component styles, configuration and the v3 to v4 migration across 29 rules. |
| api-design-patterns | 960 | REST design: resources, error responses, pagination, versioning, response format and documentation across 38 rules in 7 categories. |
| laravel-testing | 953 | Feature and unit tests with Pest PHP 4 or PHPUnit 12: HTTP tests, model factories, database assertions, facade mocks and auth testing across 24 rules. |
| testing-best-practices | 932 | Unit testing, integration testing and test-driven development with Jest or Vitest across 34 rules in 7 categories. |
| web-design-guidelines | 922 | WCAG accessibility audits, semantic HTML, keyboard navigation, forms and interface performance across 23 rules in 4 categories. |
| git-workflow | 872 | Branching strategies, commit conventions and pull request workflow for a history that stays readable. |
| e2e-playwright-testing | 828 | Playwright end-to-end tests: locator strategies, authentication reuse, form flows with SPA gotchas, assertions and CI configuration across 8 rules. |
| state-management | 815 | TanStack Query v5 and Zustand v5: data fetching, caching, mutations and client-side state. |
| code-slop | 812 | Taste-level review of AI-generated code: narration comments, generic names, premature interfaces, defensive overdose and mock-everything tests, with CLEAN, SUSPICIOUS, INFLATED or CRITICAL verdicts across 24 rules. |
| seo-best-practices | 759 | Meta tags, structured data, Core Web Vitals, sitemaps and Open Graph, with a coding reference and an audit mode across 31 rules in 8 categories. |
| technical-debt | 726 | A ranked debt ledger by effort and impact on a P0 to P3 scale, with audit mode returning PASS, FAIL or N/A across 42 rules in 10 categories. |
| laravel-queues | 726 | Queue drivers, job design and idempotency, retries and failure handling, worker scaling, Bus batching and Horizon across 20 rules in 6 categories. |
| laravel-ai-sdk | 691 | The Laravel AI SDK: agents, tool calling, structured output, streaming, embeddings, reranking and AI fakes in tests across 17 rules. |
| prd-writing | 686 | A six-step workflow for writing Product Requirements Documents, backed by 25 rules in 7 categories. |
| project-docs | 682 | Documentation lifecycle for PHP/Laravel and TypeScript/React projects: bootstrapping `docs/`, naming conventions, freshness and cleanup of AI-generated junk across 25 rules. |
| laravel-mcp | 682 | Building MCP servers in Laravel: tools, prompts and resources exposed to AI clients across 7 rules in 5 categories. |

No indexed listings fall below the threshold, so all 24 indexed listings clear it and appear in the table above.

Every listing has a matching directory in the clone, and every skill carries the same four-part structure, so there is no index-versus-tree gap here and no half-shipped skill. The four audit-style skills are the ones to notice, because they change behaviour rather than offering advice: `technical-debt`, `code-slop`, `seo-best-practices` and `web-design-guidelines` all run in an audit mode that returns a verdict, and `project-docs` adds a bootstrap mode for setting up a documentation tree from nothing.

## Why This Matters for Hermes Agents

An agent writing Laravel code without a rulebook converges on whatever pattern it saw most often in training, which is usually the tutorial version: fat controllers, `find()` inside a loop, validation in the wrong class. This pack replaces that with explicit rules and paired examples, and the pairing matters more than the rule count, since a wrong example next to a right one is what lets an agent recognize the pattern it is about to repeat.

The audit modes are the real differentiator. `technical-debt` returns a ranked ledger rather than a list, so a session that starts with "what should we fix first" ends with priorities instead of observations. `code-slop` covers the failure mode that metrics miss entirely: code that passes every gate, has full coverage, and still reads like a tutorial because the comments narrate and the tests mock everything. The README is direct that the two are complements, `code-slop` for taste and `technical-debt` for metrics, and running both is the intended full audit.

The stack coverage is coherent within its lane. A Laravel and React team gets ORM performance, queue design, Pest testing, OWASP review, Inertia form handling, Tailwind, accessibility and SEO from one install, with version pins that keep the advice in the right generation. That is a better fit for that team than any of the general-purpose engineering packs, which tend to be language-agnostic and therefore vague exactly where Laravel is specific.

Delivery discipline rounds it out. `git-workflow` covers branching and commit conventions, `prd-writing` gives a six-step specification workflow, `project-docs` handles the documentation lifecycle including cleanup of AI-generated junk, and `laravel-mcp` covers exposing a Laravel application to agents as MCP tools. The pack is a full working standard rather than a review checklist, and it is small enough to install whole, at 6.5 MB of markdown.

## Usage

| You say | What happens |
|---|---|
| "Review this Laravel controller" | `laravel-best-practices` walks the controller against its 31 rules and returns the conventions it breaks with the corrected form beside each. |
| "What should we refactor first" | `technical-debt` runs audit mode, scores findings by effort and impact, and outputs a P0 to P3 ledger with PASS, FAIL or N/A per rule. |
| "Does this diff look AI-generated" | `code-slop` classifies the change as CLEAN, SUSPICIOUS, INFLATED or CRITICAL, naming the narration comments, generic names or mock-everything tests behind the verdict. |
| "Our listing page takes four seconds" | `laravel-database-optimization` looks for N+1 queries first, then indexing, Redis caching and pagination, before touching application code. |
| "Audit the checkout form for accessibility" | `web-design-guidelines` runs the WCAG pass over semantics, keyboard navigation, labelling and form errors. |
| "Write Pest tests for the invite flow" | `laravel-testing` supplies the feature test shape: factories, database assertions, facade mocks and the HTTP assertions Pest 4 expects. |
| "Set up a docs folder for this project" | `project-docs` runs bootstrap mode, lays out `docs/` by convention, and seeds only the files the project actually needs. |

## Verification

The raw path for the highest-install skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} php-best-practices\n" \
  https://raw.githubusercontent.com/asyrafhussin/agent-skills/main/skills/php-best-practices/SKILL.md
```

Expect `200`. After the copy, confirm the four-part structure survived, since `rules/` and `metadata.json` are what make the audit skills work:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/{php-best-practices,laravel-best-practices,technical-debt,code-slop}/ | wc -l
ls ~/.hermes/profiles/corpusiq/skills/php-best-practices
head -6 ~/.hermes/profiles/corpusiq/skills/technical-debt/SKILL.md
```

The first command prints 4, the second should list `AGENTS.md`, `metadata.json`, `README.md`, `rules` and `SKILL.md`, and the header should show `name: technical-debt` with a `license: MIT` line and a `metadata:` block carrying the author and version. If `rules/` is empty, the copy missed the bulk of the skill.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| php-best-practices | Pass | Pass | Pass |
| laravel-database-optimization | Pass | Pass | Pass |
| web-design-guidelines | Pass | Warn | Pass |
| technical-debt | Pass | Pass | Pass |
| laravel-mcp | Pass | Pass | Pass |

No Fail appears in the sample. One Warn does: Socket flags `web-design-guidelines`, the accessibility and UI audit skill, and the reason is not stated in the verdict, so read the Socket page before relying on it in a pipeline that gates on security results.

The risk surface is close to zero by construction, and this is the cleanest pack in the batch on that measure. The clone holds 768 files, 744 of them markdown and 24 of them `metadata.json`, with no scripts, no hooks and no executable code of any kind. The skills tell an agent what to look for and how to phrase a verdict; they never ask it to run a binary or fetch a remote artifact, and nothing happens at install beyond a file copy. The failure mode is therefore advice quality rather than compromise, and the only credentials concern is what your own agent does with the code these skills point it at.

Two content-level cautions are worth carrying. `laravel-owasp-security` and `code-slop` both instruct an agent to review authentication, payments and uploads, and a review that ends with an agent editing auth code is a bigger risk than any rule these skills contain, so keep review authority separate from edit authority. `laravel-mcp` covers exposing a Laravel application to AI clients as MCP tools, which is an intentional new attack surface; treat its guidance as a starting point and audit the resulting tool scopes yourself.

## Limitations

- Snapshot data, verified 2026-10-31: 29,010 combined installs across 24 indexed listings; 95 GitHub stars; MIT; last pushed 2026-08-27. Counts drift over time.
- The title promises clean code, the contents are mostly Laravel. Nine of the 24 are Laravel or PHP-specific and the React skills assume that ecosystem beside them, so a non-PHP team gets real value from `clean-code-principles`, `git-workflow`, `testing-best-practices` and `api-design-patterns` and little from the rest.
- Versions are pinned and will age. `laravelVersion: "13.x"`, `phpVersion: "8.3+"`, `pestVersion: "4.x"` and `phpunitVersion: "12.x"` in the frontmatter mean the advice targets one generation, and the repository has not been pushed since 2026-08-27.
- Install counts are not a ranking. `php-best-practices` leads at 3,721 while `technical-debt` sits at 726 and is the more distinctive skill, and the two audit skills that pair with it, `code-slop` at 812 and `project-docs` at 682, are also mid-table.
- The review skills overlap by design. `clean-code-principles`, `code-slop` and `technical-debt` can all be pulled into the same review, and `testing-best-practices` overlaps `laravel-testing` on TDD, so an agent needs the disambiguation the README provides or it will run two checklists over one diff.
- One maintainer, and a single 95-star repository. There is no release process, no test suite for the skills themselves and no changelog discipline beyond the per-skill `metadata.json` versions, so a regression in a rule arrives silently.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)
- [Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup - Setup Guide](/hermes/skills/catalog/claude-mpm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole pack if you are on Laravel. It is 6.5 MB of markdown with no code, and the cross-references between `laravel-best-practices`, `laravel-database-optimization`, `laravel-testing` and `laravel-owasp-security` are worth more than the disk cost.
- Run `technical-debt` and `code-slop` together on the same diff. The first ranks by metrics, the second judges by taste, and the README's own comparison says neither catches what the other does.
- Copy `rules/` with the skill. The paired incorrect and correct examples live there, and they are what makes an agent recognize a pattern rather than recite a rule.
- Check the version pins before trusting a recommendation. Each Laravel skill declares its `laravelVersion` and `phpVersion` in frontmatter, so an agent working on Laravel 11 can tell at a glance that the advice targets 13.
- Use audit mode for reporting and coding reference for writing. Four skills support both, and the audit output with PASS, FAIL and N/A per rule is far easier to put in front of a team than prose.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
