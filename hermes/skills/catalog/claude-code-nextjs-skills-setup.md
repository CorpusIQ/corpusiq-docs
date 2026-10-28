---
title: "Claude Code Next.js Skills - Next.js 16 and AI SDK Setup"
description: "laguagu's 25 skills: 8,686 combined installs. Next.js 16, AI SDK 6/7, shadcn/ui, pgvector search, SEO, and browser verification."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-code-nextjs-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "nextjs", "ai-sdk", "shadcn"]
---

# Claude Code Next.js Skills - Setup Guide

**Source:** [laguagu/claude-code-nextjs-skills](https://www.skills.sh/laguagu/claude-code-nextjs-skills) via skills.sh - 8.7K combined installs across 25 indexed listings; verified 2026-10-27 (Oct 27 evening sweep)

**GitHub:** [laguagu/claude-code-nextjs-skills](https://github.com/laguagu/claude-code-nextjs-skills) - 70 stars, MIT, branch main, 25 skill directories under `skills/`, each one `SKILL.md` plus a `references/` or rules folder; latest commit 2026-10-26 ships release 1.3.0

**Category:** Next.js and AI SDK application engineering

**Quality Tier:** 🟡 Beta - single maintainer, 70 stars, 25 skills against 25 indexed listings that are not the same set, and two listings carry more than half of the install volume

This repository is one maintainer's working set for building AI applications on Next.js, packaged so an agent loads only the part a task needs. The stack it covers is specific and current: Next.js 16, the Vercel AI SDK at major versions 6 and 7, shadcn/ui, pgvector retrieval, and browser verification. It ships as the `nextjs-ai-skills` plugin (version 1.3.0) for the `laguagu` Claude Code marketplace, with a root `plugin.json` for the Agent Plugins format and a `.claude-plugin/marketplace.json` for the plugin commands. The 25 skills total 8,686 installs across 25 indexed listings on skills.sh, and 12 of them are attributed to upstream sources in the README, including Vercel, Anthropic, Supabase, shadcn and addyosmani, with those upstream licenses retained.

The install distribution is uneven and worth knowing before you read the table. `nextjs-seo` (2,416) and `openai-agents-sdk` (2,234) carry more than half of the combined figure, `nextjs-shadcn` (837) is the only other listing above 900, and the remaining 22 listings are all under 300. That shape reflects demand rather than quality: the SEO and Python agent skills get installed as standalone references, while the Next.js-specific skills are mostly used inside the plugin, where they install as one unit.

## Installation

The README documents the Claude Code plugin path first. Both commands run inside the host:

```text
/plugin marketplace add laguagu/claude-code-nextjs-skills
/plugin install nextjs-ai-skills@laguagu
```

The plugin exposes the skills as `/nextjs-ai-skills:<skill>`, for example `/nextjs-ai-skills:ai-app` to scaffold an application or `/nextjs-ai-skills:go` to check one in a browser, and the README notes that relevant skills also activate from a plain request. Updating uses the shell commands the README gives:

```bash
claude plugin marketplace update laguagu
claude plugin update nextjs-ai-skills@laguagu
```

The plugin was previously published as `claude-code-nextjs-skills`. The README says to uninstall that name and install `nextjs-ai-skills@laguagu` instead, so an old install does not shadow the current one.

Without the plugin, a skill is just a directory. Clone the repository and copy the folder you need, plus any sibling skill it references, into the agent's skills directory:

```bash
git clone --depth 1 https://github.com/laguagu/claude-code-nextjs-skills.git
```

The README names `.claude/skills/` for Claude Code and `.agents/skills/` for Codex, or `~/.claude/skills/` and `~/.agents/skills/` for all projects. Clients that read the Agent Plugins format can use the root `plugin.json` directly. Copying is also the only path that works for a Hermes agent, since `mcp.json` and the plugin manifest are host features rather than skill content.

The plugin bundles one MCP server. `mcp.json` registers `next-devtools`, started as `npx -y next-devtools-mcp@latest` over stdio. Chrome DevTools MCP is not in that file; the `chrome-devtools` skill documents its own setup.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nextjs-seo | 2,416 | App Router SEO implementation and audits: metadata and social images, sitemaps and robots, canonicals and localization, structured data, Core Web Vitals evidence and AI crawler policy. |
| openai-agents-sdk | 2,234 | Python OpenAI Agents SDK work: agents, multi-agent handoffs, function tools, guardrails, sessions, streaming and tracing, including Azure OpenAI through its native client or LiteLLM. |
| nextjs-shadcn | 837 | Building and polishing Next.js interfaces with shadcn/ui: typography, theme tokens, backgrounds, presets and design-system lint through `@shadcn/lint`. |
| next-best-practices | 272 | Next.js App Router rules for file conventions, RSC boundaries, async request APIs, data patterns, hydration errors, metadata, route handlers and bundling. |
| react-best-practices | 253 | Vercel Engineering's React and Next.js performance guide: 70 rules in 8 categories covering data waterfalls, bundle size, re-renders and Server Components. |
| postgres-semantic-search | 218 | PostgreSQL retrieval with pgvector, full-text search, pg_trgm, hybrid RRF fusion, ParadeDB BM25 and reranking, plus tested SQL building blocks in `scripts/`. |
| cache-components | 214 | Next.js Cache Components and Partial Prerendering: `use cache`, `cacheLife`, `cacheTag`, `updateTag` and `revalidateTag`, and static versus dynamic boundaries. |
| ai-sdk-6 | 212 | Vercel AI SDK v6 work in a codebase already on `ai@6`: ToolLoopAgent, useChat, generateText, streamText, tool approval, provider tools and MCP integration. |

The remaining 17 indexed listings range from 9 to 191 installs: ai-app (191), web-design-guidelines (187), ai-elements (178), frontend-design (178), skill-creator (166), shadcn (156), nextjs-chatbot (154), ai-sdk (143), supabase-postgres-best-practices (138), hetzner-cloud (112), chrome-devtools (109), go (106), handoff (90), ai-sdk-7 (48), icons (34), vercel-react-view-transitions (31) and vercel-react-best-practices (9).

## Why This Matters for Hermes Agents

The skills solve a problem that generic Next.js advice cannot: version drift. The Next.js 16 notes in `next-best-practices` list changes that invalidate most examples an agent has memorized. Synchronous access to `cookies()`, `headers()`, `params` and `searchParams` is gone, `middleware.ts` is superseded by `proxy.ts` running on Node.js only, Turbopack is the default for both `dev` and `build`, and `next lint` no longer exists. An agent writing from memory produces code that compiles under 15 and fails under 16.

The AI SDK skills handle the same drift with an explicit router. `ai-sdk` answers general AI SDK questions, but its first job is version discovery: it identifies the installed major and hands version-specific work to `ai-sdk-6` or `ai-sdk-7`, while `ai-sdk-7` owns the v6 to v7 migration path. That structure means a Hermes agent can resolve the actual `ai` dependency in the project before writing imports, instead of guessing which API generation the repository is on.

Grounding is the second lever. `nextjs-seo` and `next-best-practices` instruct the agent to read the installed Next.js documentation under `node_modules/next/dist/docs/` and the bundled type definitions, rather than treating training data as the API reference. `postgres-semantic-search` goes further and is organized around silent failures: cases that return fewer rows, zero rows or plausible results without raising an error, which is exactly the class of bug an agent will otherwise report as success.

The suite also closes the loop after a change. `go` opens the running application and verifies that recent UI work actually works, while `chrome-devtools` inspects the DOM, console, network and performance when it does not. Both are cheap to invoke and both produce evidence an agent can cite, which is the difference between "I updated the component" and "the page renders and the control responds".

Finally, the skills state their own boundaries. `nextjs-seo` says it is not for general Next.js feature work, `chrome-devtools` separates live debugging from Playwright suites, and `postgres-semantic-search` routes schema, RLS and query tuning to Supabase's skill. Routing that is written down beats routing an agent invents.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a chat app with streaming and tool calls" | ai-app builds the full-stack Next.js application on the AI SDK with the shadcn/ui AI Elements patterns. |
| "Add metadata, a sitemap and JSON-LD to the marketing pages" | nextjs-seo verifies production URLs, status codes, canonicals and crawl rules first, then implements the Metadata API, sitemap and robots routes, and checks the emitted absolute URLs. |
| "This dashboard re-renders on every keystroke" | react-best-practices applies the matching performance rules for waterfalls, bundle size and re-render scope, then refactors the component tree. |
| "Give me semantic search over our support docs" | postgres-semantic-search picks the column type by embedding dimension, starts from an exact vector baseline, builds eval sets, then adds hybrid RRF fusion and a reranker only where they win. |
| "Upgrade this project to Next.js 16" | next-best-practices walks the breaking changes for the affected areas and names the codemods, using the project's own package runner. |
| "Does the new settings page actually work?" | go opens the running app and exercises the change in a browser; chrome-devtools takes over for console errors, network failures or performance measurements if something breaks. |
| "Cache this page for an hour and bust it when content changes" | cache-components applies `use cache` with `cacheLife` and `cacheTag`, then wires `updateTag` or `revalidateTag` at the write path. |
| "Build a Python agent with guardrails and handoffs" | openai-agents-sdk resolves the installed `openai-agents` version from `importlib.metadata` before writing `Agent`, `Runner`, `function_tool` and handoff code. |

## Verification

Every skill lives at `skills/<name>/SKILL.md` on `main`, so the raw path is predictable. Probe the ones you plan to install:

```bash
for p in skills/nextjs-seo/SKILL.md \
         skills/openai-agents-sdk/SKILL.md \
         skills/nextjs-shadcn/SKILL.md \
         skills/postgres-semantic-search/SKILL.md \
         skills/next-best-practices/SKILL.md \
         skills/cache-components/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/laguagu/claude-code-nextjs-skills/main/$p"
done
```

All six returned 200 on 2026-10-27. Read two of them before installing, because they set the scope of what the rest of the suite will do to a repository:

- https://raw.githubusercontent.com/laguagu/claude-code-nextjs-skills/main/skills/postgres-semantic-search/SKILL.md
- https://raw.githubusercontent.com/laguagu/claude-code-nextjs-skills/main/skills/nextjs-shadcn/SKILL.md

The MCP wiring is in a separate file, worth fetching on its own:

- https://raw.githubusercontent.com/laguagu/claude-code-nextjs-skills/main/mcp.json

After a plugin install, `/plugin` lists the enabled skills and each one answers as `/nextjs-ai-skills:<skill>`. A manual copy instead lands as one folder per skill in the agent's skills directory, and `next-devtools`, the MCP server from `mcp.json`, is not wired at all, so check which of the two you did before debugging a missing tool.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled for this fire, so every cell below reads Not checked. Re-check each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nextjs-seo | Not checked | Not checked | Not checked |
| openai-agents-sdk | Not checked | Not checked | Not checked |
| nextjs-shadcn | Not checked | Not checked | Not checked |
| next-best-practices | Not checked | Not checked | Not checked |
| react-best-practices | Not checked | Not checked | Not checked |
| postgres-semantic-search | Not checked | Not checked | Not checked |
| cache-components | Not checked | Not checked | Not checked |
| ai-sdk-6 | Not checked | Not checked | Not checked |

The concrete risks are visible in the files, and they are about commands and write scope rather than obfuscated code. `mcp.json` starts a third-party npm package as `npx -y next-devtools-mcp@latest`, which resolves a floating tag at every session start and runs it with stdio access to the development machine. The `chrome-devtools` skill documents the same pattern for `chrome-devtools-mcp@latest`, though it adds isolation and telemetry opt-out flags. Pin a version in either case if the host is not disposable.

`postgres-semantic-search` ships executable DDL in `scripts/setup.sql`, `indexes.sql`, `semantic_search.sql`, `hybrid_search_fts.sql`, `hybrid_search_bm25.sql`, `fuzzy_search.sql` and `prefix_tsquery.sql`. The setup file creates the `vector` and `pg_trgm` extensions, then creates `documents` and `chunks` tables with `vector(1536)` columns, and its own header tells you the functions hard-code the table, column and dimension choices. Read it before running it against an existing database: that is schema write access, not a query.

Package and registry operations are the other write path. The `shadcn` skill declares `allowed-tools` limited to `npx shadcn@latest`, `pnpm dlx shadcn@latest` and `bunx --bun shadcn@latest`, and the `nextjs-shadcn` skill notes that `shadcn docs`, `add` and `view` need the registry over the network, so component source is fetched remotely and written into the project. `next-best-practices` likewise instructs agents to run `npx @next/codemod@latest middleware-to-proxy .` and the experimental `npx next@canary upgrade`, and a codemod rewrites source files across the project.

`openai-agents-sdk` assumes provider credentials in the environment, and its own text says the wheel ships no documentation, so the agent inspects the installed package. Keep API keys in environment variables scoped to the session, and do not paste them into a prompt that will end up in a transcript. Beyond `shadcn`, none of these skills narrow their tool permissions, so treat every install as full repository write access for the agent that loads it.

## Limitations

- Snapshot data, verified 2026-10-27: 8,686 combined installs across 25 indexed listings; 70 GitHub stars; MIT; branch main. Counts drift over time.
- Directories and listings do not match one for one even though both number 25. `agent-harness-review` is in the tree but carries no indexed listing, and `vercel-react-best-practices` is indexed at 9 installs with no directory in the current tree; the closest in-tree skill is `vercel-react-view-transitions`.
- The install volume is concentrated. Two listings hold more than half of the 8,686 combined installs and 22 of the 25 sit under 300, so a high combined figure is not evidence that the Next.js-specific skills are widely exercised.
- Repository content is MIT, but 12 skills are attributed to upstream projects with their own licenses, including Apache 2.0 for `ai-sdk`, `skill-creator`, `frontend-design` and `ai-elements`. Review the upstream terms for the skills you redistribute, not just the root LICENSE.
- The README marks `ai-elements` as deprecated upstream at the end of November 2026 and points new chat UI at the shadcn/ui AI Elements patterns instead. Treat that skill as migration support rather than a place to start.
- The Claude Code plugin path provides the slash commands and the bundled `next-devtools` MCP server. Copying directories into `.claude/skills/`, `.agents/skills/` or a Hermes skills directory gives you the instructions only, with no command namespace and no MCP wiring.
- Security verdicts were not sampled for this sweep, so the Not checked table above carries no assurance either way.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [shadcn Skill - shadcn/ui Component Workflows Setup](/hermes/skills/catalog/shadcn-ui-setup)
- [Chrome DevTools MCP Skills - Browser Debugging & Automation Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup)

## Pro Tips

- Install the plugin once, not 25 copies. The skills cross-reference each other (`nextjs-shadcn` defers to `frontend-design` and `icons`, `nextjs-chatbot` defers to `ai-sdk`), and copying a folder without its sibling leaves a dangling pointer.
- Ask `ai-sdk` first when the version is unknown. It reads the installed major and routes; installing `ai-sdk-6` and `ai-sdk-7` together only pays off if you maintain codebases on both.
- Run `postgres-semantic-search` one variable at a time. Its own build order is baseline, eval sets, hybrid, reranker, and it asks for a measured gain beyond run-to-run spread before you keep a change.
- Pair `nextjs-seo` with `go`. The skill is explicit that a sitemap supports discovery but does not guarantee indexing, so verify the rendered page and the served HTML rather than trusting the report.
- Pin `next-devtools-mcp` instead of `@latest` in `mcp.json` on any host you care about, and read `scripts/setup.sql` before letting an agent run it against a database with data in it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
