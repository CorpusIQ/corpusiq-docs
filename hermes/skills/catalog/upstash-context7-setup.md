---
title: "Upstash Context7 - Versioned Library Docs Setup"
description: "upstash/context7: 25.5K combined installs. Agent skills that fetch version-specific library docs through the ctx7 CLI or the Context7 MCP server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/upstash-context7-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "documentation lookup", "mcp", "cli", "context7"]
---

# Upstash Context7 - Setup Guide

**Source:** [upstash/context7](https://www.skills.sh/upstash/context7) via skills.sh - 25.5K combined installs across 8 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [upstash/context7](https://github.com/upstash/context7) - 63,945 stars, MIT License, branch master, last pushed 2026-10-30; 10 `SKILL.md` files in four layout families, `skills/<name>/SKILL.md` for the three canonical skills, `packages/pi/skills/context7-docs/SKILL.md`, `packages/opencode/skills/context7-mcp/SKILL.md` and `plugins/<host>/context7/skills/context7-mcp/SKILL.md` generated for Cursor, Codex, Copilot, Antigravity and the generic agent-plugins host, beside `packages/` (cli, mcp, sdk, ai-sdk tools, pi extension), `docs/`, `rules/`, `i18n/`, `server.json` and two marketplace manifests

**Category:** Up-to-date library documentation retrieval for coding agents

**Quality Tier:** 🟡 Beta - 4 sampled Warn verdict(s), four Warn cells across three of the five sampled skills, on a suite whose only job is piping third-party library docs into agent context

Upstash maintains Context7, and this repository is the platform itself: the MCP server source, the `ctx7` CLI, the SDK packages and the agent skills that wrap them. The README states the problem in the terms a builder recognises, with code examples that are "outdated and based on year-old training data", hallucinated APIs that do not exist, and generic answers for old package versions, and it answers with version-specific documentation and code examples pulled from source repositories straight into the agent's context.

The suite reaches agents by two routes and the index reflects both. CLI + Skills installs a `find-docs` skill that tells the agent to resolve a library ID and then query docs with the `ctx7` CLI, with no MCP server involved. MCP mode registers the hosted server and gives the agent the `resolve-library-id` and `query-docs` tools natively. Eight indexed listings, 25.5K combined installs and 63,945 GitHub stars make this the reference implementation that most other documentation skills are measured against.

One structural caveat belongs up front: the README says this repository hosts the MCP server's source code while the API backend, parsing engine and crawling engine are private and not part of the repository. The skills are readable, the retrieval path is not.

## Installation

The README's install route is the `ctx7` CLI, which requires Node.js 22.13 or newer. One command authenticates over OAuth, generates an API key and installs the skill for the mode you pick:

```bash
npx ctx7 setup
```

The README notes that `--cursor`, `--claude` and `--opencode` target a specific agent, and the bundled setup reference in `skills/context7-cli/references/setup.md` adds the mode and auth flags: `--mcp` or `--cli` to skip the mode prompt, `--project` for a project-level config, `--yes` to skip confirmation, and `--api-key` to reuse an existing key. Removal is symmetrical:

```bash
npx ctx7 remove
```

```bash
npm uninstall -g ctx7
```

The manual route is the server URL `https://mcp.context7.com/mcp` in any MCP client, with the API key passed in an `Authorization: Bearer` header; the repo's own Cursor plugin ships `mcp.json` pointing at the `/mcp/oauth` variant instead, which is worth knowing when you compare configs. A free key from the Context7 dashboard lifts the rate limits.

There is no skills.sh install path in this README and no Hermes target among the generated hosts, so the durable route for this profile is a directory copy from a clone:

```bash
cp -R skills/find-docs ~/.hermes/profiles/corpusiq/skills/find-docs
cp -R skills/context7-cli ~/.hermes/profiles/corpusiq/skills/context7-cli
```

Copy whole directories. `context7-cli` ships `references/docs.md` and `references/setup.md` next to `SKILL.md`, and a markdown-only copy leaves the agent pointing at two files it does not have. `find-docs` is a single file and copies cleanly. The setup reference's CLI + Skills mode writes to `~/.claude/skills`, `~/.cursor/skills` or `~/.agent/skills` depending on the flag, none of which is the Hermes profile.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| find-docs | 9,655 | The CLI + Skills route: instructs the agent to run `npx ctx7@latest library <name> "<query>"` to resolve a library ID and then `npx ctx7@latest docs <libraryId> "<query>"`, and to prefer it over web search for any library, framework, SDK or CLI question. |
| context7-cli | 8,012 | The `ctx7` CLI skill: fetching documentation, plus configuring Context7 for Claude Code, Cursor, OpenCode and Antigravity, with `references/docs.md` for the two-step lookup and `references/setup.md` for setup modes, flags and auth paths. |
| context7-mcp | 6,400 | The MCP route: `resolve-library-id` then `query-docs` against the hosted server, which is what the per-host plugins under `plugins/<host>/context7/skills/` install alongside their `mcp.json` and Context7 rule file. |
| documentation-lookup | 1,326 | The skill `ctx7 setup` installs per the CLI changelog, and the name Upstash's marketplace manifest uses for it: pulling version-specific documentation and code examples from source repositories into the agent's context. It has no directory of its own in the current tree because it is generated at setup time. |

The remaining 4 indexed listings range from 7 to 47 installs.

## Why This Matters for Hermes Agents

Library questions are where an agent's context goes stale most quietly, because a plausible signature that no longer exists looks exactly like a correct one. A skill that fetches documentation at call time turns that into a tool call with a citable library ID, and the returned snippets can be shown to the person who asked.

The two-mode split is the part that decides whether this works in your setup. CLI + Skills needs Node.js 22.13 or newer and a network call, and nothing else; MCP mode needs a client that can register `https://mcp.context7.com/mcp` with an authorization header. For a Hermes cron or subagent that wakes up without conversational context, `find-docs` is the mode with no client dependency to configure first.

Version pinning is the feature worth wiring into a prompt template. The ID shape `/org/project/version`, for example `/vercel/next.js/v16.2.9`, targets the major version actually in the project instead of whatever was indexed last, which is the difference between a matching example and a migration warning in a review.

The resolution step also returns evidence. Each match carries source reputation and a benchmark score against a 100 ceiling, so an agent can say why it trusted one package's docs over another rather than asserting authority. The docs reference caps `ctx7 library` at three calls per question, which bounds both cost and the resolution loop an unattended job can get stuck in.

## Usage

| You say | What happens |
|---|---|
| "How do I clean up a useEffect with async operations?" | `find-docs` runs `ctx7 library react` with that query, picks the closest match, then queries `ctx7 docs /facebook/react`, and answers from the returned snippets with the library ID named. |
| "Set up app router with a proxy in Next.js 16" | The lookup targets a version-specific ID such as `/vercel/next.js/v16.2.9` instead of the unversioned one, so the answer matches the major version in the project rather than the newest indexed docs. |
| "Define one-to-many relations with cascade delete in Prisma" | Resolution lands on `/prisma/prisma` and the docs call returns the relation syntax for the indexed Prisma version, which is the Prisma question the skill files use as their own example. |
| "Send an SMS with Twilio, but I write Ruby" | The docs call passes `--language Ruby` against `/websites/twilio`, and the CLI ranks Ruby examples first, matching the `language` argument the MCP `query-docs` tool exposes. |
| "Wire Context7 into Cursor on this laptop" | `context7-cli` walks the setup reference: mode choice, agent target, then the MCP entry in the host config file and the Context7 rule file that tells the agent to reach for it unprompted. |
| "Which Context7 source is trustworthy for this package?" | The resolution output carries source reputation and benchmark score per match, so the answer cites High or Medium reputation plus snippet count instead of asserting authority. |
| "Stop guessing API signatures in this repository" | Route the repository's library questions to `find-docs` and add the README's rule line, so the agent fetches docs for library work without being asked each time. |

## Verification

Both raw paths below returned 200 on branch master when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} find-docs\n" \
  https://raw.githubusercontent.com/upstash/context7/master/skills/find-docs/SKILL.md
curl -sL -o /dev/null -w "%{http_code} cursor-plugin\n" \
  https://raw.githubusercontent.com/upstash/context7/master/plugins/cursor/context7/skills/context7-mcp/SKILL.md
```

Expect `200` twice. Those two paths are deliberately different layouts: `skills/find-docs/` is the canonical copy, and `plugins/cursor/context7/skills/` is a generated host adapter, so a 200 on both tells you the tree still carries the pair the index describes. Read a `SKILL.md` before installing, because its description is the whole routing contract: `find-docs` wins its triggers by naming React, Next.js, Prisma, Express, Tailwind, Django and Spring Boot explicitly and by telling the agent to distrust its own recall.

After a copy lands in the profile, confirm the frontmatter and that the references came along:

```bash
head -6 ~/.hermes/profiles/corpusiq/skills/find-docs/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/context7-cli/references/
```

A good copy shows `name: find-docs` and a multi-line `description:` and nothing else, and the directory listing shows `docs.md` and `setup.md`. For a functional check, the skill's own worked example is the cheapest proof the CLI can reach the service:

```bash
npx ctx7@latest docs /facebook/react "How to clean up useEffect with async operations"
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| find-docs | Pass | Pass | Pass |
| context7-cli | Pass | Pass | Warn |
| context7-mcp | Pass | Pass | Pass |
| documentation-lookup | Pass | Pass | Warn |
| docs | Warn | Pass | Warn |

No FAIL appears in the sampled five. The four Warns sit on `context7-cli`, `documentation-lookup` and `docs`, and the pack records the verdict rather than the finding behind it, so read those Snyk and Gen Agent Trust Hub entries on skills.sh before you install them.

The risk class here is not code execution, it is what the skill puts into the model's context. Retrieved documentation is community-contributed and the README's own disclaimer says its accuracy, completeness and security cannot be guaranteed, while the skill's instruction is to treat those snippets as the answer. That makes retrieved text a prompt-injection surface: an instruction embedded in a code sample arrives as trusted material, so quote it to the user rather than acting on it, and keep the fetched content clearly framed as data.

Two habits follow. Never put credentials, personal data or proprietary code into a resolution query, which the CLI reference states outright and which the query field makes easy to get wrong because it is free text built from the user's question. And keep the API key in the MCP client config or an environment variable rather than a prompt: the README's only reference to it is a `Authorization: Bearer` header, and keys are issued from the Context7 dashboard.

## Limitations

- Snapshot data, verified 2026-10-30: 25,472 combined installs across 8 indexed listings; 63,945 GitHub stars; MIT License; last pushed 2026-10-30. Counts drift over time.
- The install index outruns the tree. Eight listings map to four named skill directories: `ctx7-cli`, `context7-docs-lookup` and `docs` have no matching directory in the current checkout, and `documentation-lookup` exists only as what `ctx7 setup` writes at install time.
- The branch is `master`, not `main`, and every raw URL plus the README's own cover image depends on it. Do not rewrite a link or a clone instruction to `main`.
- Every useful path is a live call. `ctx7` needs Node.js 22.13 or newer, both modes reach the hosted Context7 service, and rate limits apply with an API key recommended for higher ones, so an air-gapped or review-only agent gets a skill that can describe the workflow but retrieve nothing.
- The retrieval path is closed. The README states that this repository hosts the MCP server source while the API backend, parsing engine and crawling engine stay private, so reading the skills tells you the protocol and never how a library or version gets indexed.
- Four of the eight listings sit between 7 and 47 installs, which is publication noise rather than adoption signal. Judge the skill by its `SKILL.md` and the lookups it actually performs.

## Related

- [Qdrant Skills - Vector Search, Retrieval and Memory Setup](/hermes/skills/catalog/qdrant-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `find-docs` first. It is one file, needs no MCP client and no config edit, and it changes the default from recalled APIs to fetched ones in a single copy.
- Pin the version in the library ID, not in the prose. A task about Next.js 16 should resolve to `/vercel/next.js/v16.2.9`, because the unversioned ID returns whatever was indexed last and quietly undoes the point of the skill.
- Give the library ID when you already know it. The README's `use library /supabase/supabase` form skips the matching step, which is cheaper and far more deterministic than hoping the resolver picks the package you meant.
- Keep the CLI current. The skill opens with `npm install -g ctx7@latest` or `npx ctx7@latest`, and the reason is plain: an old client can mis-handle newer ID shapes and version suffixes.
- Treat retrieved docs as untrusted input. They are community-contributed, so an instruction that arrives inside a code snippet should be quoted back to the user, never executed as if the agent had decided it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
