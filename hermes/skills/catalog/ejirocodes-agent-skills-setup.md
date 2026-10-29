---
title: "Ejiro Agent Skills - Svelte, Vue, NestJS and Exa Setup"
description: "ejirocodes/agent-skills: 18.9K combined installs. Seven skills covering Svelte 5 runes, Vue 3 TypeScript, NestJS 11 and Exa search, RAG and research."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ejirocodes-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "svelte", "vue", "nestjs", "exa"]
---

# Ejiro Agent Skills - Setup Guide

**Source:** [ejirocodes/agent-skills](https://www.skills.sh/ejirocodes/agent-skills) via skills.sh - 18.9K combined installs across 8 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [ejirocodes/agent-skills](https://github.com/ejirocodes/agent-skills) - 6 stars, MIT, branch main, last pushed 2026-06-25; four plugin directories (`svelte`, `vue`, `nestjs`, `exa`), each holding a `skills/<name>/` folder, for 7 `SKILL.md` files in the clone plus a `.claude-plugin/marketplace.json` at the root and no `package.json`

**Category:** Framework best-practice skills for Svelte 5, Vue 3 and NestJS 11, plus Exa.ai search, RAG and research skills

**Quality Tier:** 🟡 Beta - single-author collection, 6 GitHub stars, MIT, 7 skill directories, and three of the six sampled skills carry a Snyk warning

Ejiro Asiuwhu maintains this as a curated set of skills for coding assistants, and the framing in the README is narrow on purpose: encode the patterns, breaking changes and deprecations that a model's training data usually misses. Seven skills ship in four plugins. Three are framework suites for Svelte 5, Vue 3 and NestJS 11, and four cover Exa.ai: web search, RAG pipelines, deep research with citations, and company or people lookup. The install weight sits almost entirely on one skill, since svelte5-best-practices alone accounts for 17,221 of the 18,886 installs.

Each plugin follows the same layout. A `SKILL.md` stays short and acts as an entry point and router, and the detail lives in `references/` files split by topic: `runes.md`, `snippets.md`, `events.md`, `typescript.md`, `migration.md`, `sveltekit.md` and `performance.md` for Svelte, `mcp-tools.md` and `langchain.md` for the Exa RAG skill, and similar per-domain splits elsewhere. That is progressive disclosure in practice, so an agent loads only the reference it needs instead of the whole suite. The README also states what the collection is not: it is not a code generator and it does not run your tooling, it supplies the rules and the worked example that a coding agent then applies.

## Installation

The README installs one plugin at a time through the skills.sh CLI, using the plugin directory rather than the repository root:

```bash
npx skills add ejirocodes/agent-skills/svelte
npx skills add ejirocodes/agent-skills/vue
npx skills add ejirocodes/agent-skills/nestjs
npx skills add ejirocodes/agent-skills/exa-search
npx skills add ejirocodes/agent-skills/exa-rag
npx skills add ejirocodes/agent-skills/exa-research
npx skills add ejirocodes/agent-skills/exa-entities
```

Claude Code takes the plugin marketplace instead. The marketplace name is `ejirocodes-skills`, and the Exa plugin installs as one unit that carries all four Exa skills:

```shell
/plugin marketplace add ejirocodes/agent-skills
```

```shell
/plugin install svelte5-best-practices@ejirocodes-skills
/plugin install vue-best-practices@ejirocodes-skills
/plugin install nestjs-best-practices@ejirocodes-skills
/plugin install exa@ejirocodes-skills
```

Nothing in the repository is written for Hermes, so the manual route is a directory copy of whichever plugin you want:

```bash
git clone https://github.com/ejirocodes/agent-skills.git
cp -R agent-skills/svelte/skills/* ~/.hermes/profiles/corpusiq/skills/
cp -R agent-skills/exa/skills/* ~/.hermes/profiles/corpusiq/skills/
```

The Exa skills assume you have an API key. The search skill's triggers name `EXA_API_KEY`, and the SDK examples import `exa_py` for Python or `exa-js` for TypeScript, so the Python route needs `pip install exa-py` before any example will run.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| svelte5-best-practices | 17,221 | Writing, reviewing or refactoring Svelte 5 and SvelteKit code: runes ($state, $derived, $effect, $props, $bindable), snippets in place of slots, callback props instead of event dispatchers, typed props and generic components, load functions and form actions, SSR state isolation, and Svelte 4 to 5 or store to rune migration. |
| nestjs-best-practices | 438 | NestJS 11 work on modules, providers and dependency injection: guards, interceptors, pipes, ValidationPipe with class-validator DTOs, JWT and Passport auth, TypeORM, Prisma or Drizzle repositories, Swagger and GraphQL decorators, TCP, Redis, NATS and Kafka microservices, and unit plus E2E testing patterns. |
| vue-best-practices | 282 | Vue 3 with TypeScript: extracting component props, generic components, defineModel and withDefaults, Volar and vueCompilerOptions setup, vue-tsc template checking and strictTemplates, CSS modules, typed vue-router params, Pinia store mocking, and HMR or moduleResolution debugging. |
| exa-research | 242 | Answer API and deep search with sourced citations: research automation, Q&A with attributed sources, citation extraction, streaming answers, and fact checks against the returned pages. |
| exa-entities | 236 | Company and people search for lead generation, recruiting and competitive intelligence, including profile lookup and Websets for collecting or monitoring sets of entities at scale. |
| exa-search | 233 | Core Exa integration in exa_py or exa-js: choosing auto, neural or keyword mode, domain and date filters, search_and_contents, find_similar, text and highlights retrieval, summaries, livecrawl, and category search. |
| exa-rag | 233 | RAG pipelines over live web results: LangChain retrievers, LlamaIndex as a data source, the Vercel AI SDK for Next.js apps, and Exa exposed as a Claude MCP server or an OpenAI function tool. |

The remaining 1 indexed listing is skill-creator (1 install), which is indexed on skills.sh but has no directory in the current tree.

## Why This Matters for Hermes Agents

Framework knowledge decays faster than model weights. Svelte 5 replaced slots with snippets and stores with runes, Vue 3 tooling moved to Volar 3 and vue-tsc, and NestJS 11 carries the Express v5 migration and its own breaking changes. An agent that answers from memory writes Svelte 4 code into a Svelte 5 file and then apologises. These three skills state the current pattern next to the old one, which is the difference between a plausible diff and a mergeable one.

The Exa group gives Hermes a research leg it otherwise assembles by hand. exa-research returns answers with citations attached through the Answer API, which is exactly the shape the grounded-citations workflow wants, and exa-search exposes the lower-level control (mode, filters, contents, livecrawl) when a summary is not enough. exa-entities covers the growth side: company and people search for prospecting, competitor mapping and list building, with Websets when the task needs a monitored set rather than a one-off query.

The structure is cheap to run. A `SKILL.md` is small, and the reference files that carry the worked examples only load when the task needs them, so keeping six of these installed costs far less context than their combined page count suggests. That matters for an agent that already carries a large skill library.

## Usage

| You say | What happens |
|---|---|
| "Build a Svelte 5 form component with validation and typed props" | svelte5-best-practices uses runes for state derivation, a snippet for the field markup, callback props instead of createEventDispatcher, and typed props instead of untyped exports. |
| "Migrate this Svelte 4 component's stores to runes" | The same skill follows its migration reference: store subscriptions become $state and $derived, slots become snippets, and each rewrite is shown against the original. |
| "Set up SvelteKit form actions with progressive enhancement" | svelte5-best-practices routes to the SvelteKit reference for load functions, form actions, page typing and SSR state isolation. |
| "Add JWT auth with Passport to this NestJS module" | nestjs-best-practices applies module, guard and strategy patterns together, keeping DTO validation in the pipe layer and the guard responsible for the token. |
| "Why does vue-tsc fail on this component's props" | vue-best-practices works through props extraction, generic components and vueCompilerOptions or strictTemplates settings before suggesting a code change. |
| "Answer this question with sources for every claim" | exa-research calls the Answer API or deep search and returns the answer with the citations that came back, rather than a summary written from memory. |
| "Find the companies in this category and who runs them" | exa-entities runs a company search, follows it with a people search, and can turn the result into a Webset for repeat collection. |

The README recommends naming the skill in the prompt, for example `Use svelte skill, help me create a form component with validation`, because triggering otherwise depends on how closely your wording matches the skill's keywords.

## Verification

Probe the paths before installing anything, and read the two skills that carry the most behavior. All seven URLs below returned 200 on the main branch when this guide was written:

```bash
for p in svelte/skills/svelte5-best-practices/SKILL.md \
         nestjs/skills/nestjs-best-practices/SKILL.md \
         vue/skills/vue-best-practices/SKILL.md \
         exa/skills/exa-search/SKILL.md \
         exa/skills/exa-rag/SKILL.md \
         exa/skills/exa-research/SKILL.md \
         exa/skills/exa-entities/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/ejirocodes/agent-skills/main/$p"
done
```

Read svelte5-best-practices first, since it is the skill almost every install in the index represents, then exa-search, because the other three Exa skills build on the same SDK surface:

- https://raw.githubusercontent.com/ejirocodes/agent-skills/main/svelte/skills/svelte5-best-practices/SKILL.md
- https://raw.githubusercontent.com/ejirocodes/agent-skills/main/exa/skills/exa-search/SKILL.md

The references are what make the skills useful, and they live one level deeper. Spot-check that a plugin's references came along with its `SKILL.md`:

```bash
for p in svelte/skills/svelte5-best-practices/references/runes.md \
         svelte/skills/svelte5-best-practices/references/migration.md \
         exa/skills/exa-rag/references/mcp-tools.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/ejirocodes/agent-skills/main/$p"
done
```

After install, confirm what actually landed and that the directory name matches the frontmatter name:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E '^(svelte5|vue-best|nestjs|exa-)'
head -5 ~/.hermes/profiles/corpusiq/skills/svelte5-best-practices/SKILL.md
```

If the Exa skills are the reason for installing, check the key is visible to the process before blaming the skill: `python3 -c "import os; print(bool(os.environ.get('EXA_API_KEY')))"` should print `True`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| svelte5-best-practices | Pass | Pass | Pass |
| nestjs-best-practices | Pass | Pass | Pass |
| vue-best-practices | Pass | Pass | Pass |
| exa-research | Pass | Pass | Warn W011 |
| exa-entities | Pass | Pass | Warn W011 |
| exa-search | Pass | Pass | Warn W011 |

All three framework skills pass all three auditors. The three warnings land on the Exa skills that make network calls with your key, which is also where the real risk sits: those skills write API client code, so the key has to exist somewhere the generated code can read it. Keep it in the environment, never in a file the skill is asked to produce, and prefer a key scoped to one project over an account-wide one.

The repository itself is inert. The root holds a license, a README, four plugin directories and a `.claude-plugin/marketplace.json`, with no `package.json`, so a clone runs no npm lifecycle script and nothing executes on install. Every skill directory is markdown: one `SKILL.md` plus `references/*.md`, which is why the Snyk warnings are best read as a prompt to check code the skill generates rather than as evidence of anything running at install time.

Two things deserve a read before you trust the output. The NestJS skill teaches authentication and ORM patterns, so generated guards, Passport strategies and repository code should get the same review you would give a contractor's PR. The Exa skills send your queries to a third-party API, so anything you paste into a research prompt leaves the machine.

## Limitations

- Snapshot data, verified 2026-10-28: 18886 combined installs across 8 indexed listings; 6 GitHub stars; MIT license; last pushed 2026-06-25. Counts drift over time.
- The install index outruns the tree: 8 indexed listings against 7 `SKILL.md` directories in the clone. `skill-creator` (1 install) has no directory under `exa/`, `nestjs/`, `svelte/` or `vue/`, so there is no local copy to read before installing it.
- One skill carries almost all the signal. svelte5-best-practices accounts for 17,221 of the 18,886 installs, the next listing (nestjs-best-practices, 438) is smaller by more than an order of magnitude, and skill-creator sits at a single install. Read the combined figure as a Svelte-driven number rather than a verdict on the suite.
- The collection is small and paused. Last push was 2026-06-25, roughly four months before this snapshot, and the README roadmap still lists React 19, Angular, Solid, Go, Rust, Docker and a testing group as future work.
- Coverage is framework-specific and version-bound: Svelte 5, Vue 3 with TypeScript, NestJS 11. There is nothing here for React, Angular or a plain Node service, and each skill will age with its framework's next major release.
- Install documentation covers the skills.sh CLI and the Claude Code plugin marketplace only. Nothing names Hermes, the `--agent` flag is not documented in this README, and the directory copy above is the route to use.

## Related

- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)
- [Feature-Sliced Design Skill - Frontend Architecture Setup](/hermes/skills/catalog/feature-sliced-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by plugin, not by repository. `npx skills add ejirocodes/agent-skills/svelte` lands one skill with its references, while installing the whole repo drags in four Exa skills that share trigger words with your ordinary research prompts.
- Name the skill in the prompt the way the README does. `Use svelte skill, ...` is more reliable than hoping that "make this component reactive" matches the trigger list, especially with several framework skills installed at once.
- Send the agent to the reference file when the answer looks thin. `runes.md`, `migration.md` and `sveltekit.md` hold the correct and incorrect pairs; a `SKILL.md` alone is a summary.
- Type-check whatever the skill writes. These skills teach patterns but run no tooling, so `vue-tsc`, `svelte-check` or the NestJS build is the step that proves the generated code compiles.
- Keep the four Exa skills separate in your head: exa-search for raw search and contents, exa-rag for pipeline and framework code, exa-research for cited answers, exa-entities for people and companies. Reaching for the wrong one produces working code for the wrong job.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
