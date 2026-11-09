---
title: "Context7 Skill - Documentation Lookup via REST"
description: "netresearch/context7-skill on skills.sh: 2.1K combined installs; a Context7 REST API documentation lookup skill for agents without the MCP server."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/context7-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "documentation", "context7", "rest api", "library docs"]
---

# Context7 Skill - Setup Guide

**Source:** [netresearch/context7-skill](https://www.skills.sh/netresearch/context7-skill) via skills.sh - 2,112 installs across 1 indexed listing (2.1K combined); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 87 stars, license NOASSERTION (no standard OSI license is declared at the repository level), `main` branch, last pushed 2026-11-09, 38 files with 1 SKILL.md at `skills/context7/SKILL.md` and the `scripts/context7.sh` wrapper beside it
**Category:** Documentation retrieval: a REST API wrapper that fetches current library docs and API references without an MCP server occupying the context window
**Quality Tier:** 🟡 Watch - a focused single-skill repository with CI checks and a split license, but GitHub reports NOASSERTION, Snyk returns Warn on the one indexed listing, and the count is one listing at 2.1K installs.

Context7 is Upstash's documentation service: a model asks for a library and a topic and gets current documentation back, which is the answer to training data that stops at a version boundary. The usual way to reach it is the Context7 MCP server, and the tradeoff is context: the README measures the MCP route at roughly 500 to 2,000 tokens held permanently for tool schemas, against roughly 100 tokens on demand for this skill.

This repository takes the other route. `SKILL.md` is one file, and `scripts/context7.sh` calls the Context7 REST API directly with `search` and `docs` subcommands. Netresearch DTT GmbH built it, the README frames it as a fallback for when the MCP server is "unavailable or not configured", and the frontmatter says the same thing: it fetches the same current docs directly when MCP is not there.

The adoption number is single-source and small: 2,112 installs against 87 stars, one indexed listing, and every install route in the README funnels to the same skill directory.

## Installation

The README recommends the marketplace route, which is Claude Code only. Add the Netresearch marketplace once, then install the plugin:

```text
/plugin marketplace add netresearch/claude-code-marketplace
/plugin install context7@netresearch-claude-code-marketplace
```

For any Agent Skills compatible agent, including Hermes through the skills CLI:

```bash
npx skills add https://github.com/netresearch/context7-skill --skill context7
```

Without a marketplace, the README gives a plain clone. Since Claude Code 2.1.157 a plugin directory under the personal skills directory loads on its own:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/netresearch/context7-skill.git \
  ~/.claude/skills/context7
```

It loads as `context7@skills-dir` on the next session, updates with `git -C ~/.claude/skills/context7 pull`, and is removed by deleting the directory. The README notes this route has no `claude plugin update`, so a pull is the only refresh.

Two package-manager routes exist for projects that already vendored skills into a dependency tree. For PHP, `composer require netresearch/context7-skill` requires `netresearch/composer-agent-skill-plugin`. For Node, install `@netresearch/agent-skill-coordinator` alongside `github:netresearch/context7-skill`; the coordinator discovers the skill in `node_modules` and registers it in `AGENTS.md` through a `postinstall` hook, and pnpm needs `@netresearch/agent-skill-coordinator` in `pnpm.onlyBuiltDependencies` or the hook is skipped.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| context7 | 2,112 | Looking up current documentation, API references, framework patterns and code examples for a named library over the Context7 REST API, with topic filtering, when the MCP server is unavailable or not configured |

One row clears the threshold, and since the threshold is zero no rows fall below it.

The body is a trigger document plus a script contract. The triggers are the phrasings a developer actually uses: "how do I use [library]", "what's the API for [library]", "[library] documentation", "show me [library] patterns". The README lists 50 or more libraries by example, React, Next.js, Vue, Express and Prisma among them, and the frontmatter widens that to "ANY library" with React, Next.js, Vue, Django and Laravel as samples.

The script has two commands, and they are the whole interface:

```bash
# Search for a library ID
scripts/context7.sh search "prisma"

# Fetch documentation with topic
scripts/context7.sh docs "/prisma/prisma" "queries"
```

The two-step shape is the part worth understanding. `search` resolves a human library name to the identifier the docs endpoint expects, and `docs` takes that identifier plus an optional topic, so a request for Prisma query patterns returns the queries section rather than the full manual. Topic filtering is the feature that keeps the payload small, and it is why this fits a narrow context budget better than a general documentation fetch.

## Why This Matters for Hermes Agents

Hermes runs long sessions against a fixed context budget, and an MCP server that holds tool schemas for the whole session spends that budget on a capability the session may never use. This skill spends nothing until a documentation question appears, then spends one script call.

The second fit is that the interface is a shell script. A Hermes agent can call `scripts/context7.sh docs "/prisma/prisma" "queries"` through its terminal tool with no protocol layer, no server process to start, and no session state to keep. That also makes it scriptable inside a larger job: fetch the docs, write them to scratch, and read the section that matters.

The third is failure behaviour. A skill that only works when MCP is configured has a hard dependency; this one exists for the case where it is not, which is the normal state in a fresh environment, a CI container, or a restricted network where a local server is not an option.

The counterweight is scope. This fetches documentation and nothing else. It does not answer questions about an internal codebase, it does not cache across sessions, and it is only as good as the Context7 index for the library in question.

## Usage

| You say | What happens |
|---|---|
| "How do I use React hooks" | Matches the trigger set, resolves the React library ID, then fetches the hooks section instead of the whole React manual |
| "What is the Next.js App Router API" | Fetches the App Router topic for the Next.js docs entry and answers from the current version rather than training data |
| "Show me Prisma query patterns" | Runs `scripts/context7.sh docs "/prisma/prisma" "queries"` and reads the queries topic |
| "Express middleware documentation" | Resolves Express, then filters to the middleware topic |
| "Which library ID should I use for Vue" | Runs the `search` subcommand first, then passes the returned identifier to `docs` |
| "The Context7 MCP server is not configured here" | Uses the REST path directly, which is the case the README built the skill for |
| "The docs call is being rate limited" | Sets `CONTEXT7_API_KEY` before the call, which the README documents as the route to higher rate limits |

## Verification

The skill body is a single file inside the skills tree:

```bash
curl -fsSL https://raw.githubusercontent.com/netresearch/context7-skill/main/skills/context7/SKILL.md | head -10
```

This returns 200 and opens with YAML frontmatter whose `description` names the trigger phrases and the MCP-unavailable condition. The script is the part that does the work, so fetch it too:

```bash
curl -fsSL https://raw.githubusercontent.com/netresearch/context7-skill/main/skills/context7/scripts/context7.sh | head -20
```

That also returns 200 and shows the argument handling for `search` and `docs`. A 404 here means the wrapper moved and the skill body's relative path is stale.

After a manual clone, confirm the file landed under the directory the client loads, not one level off:

```bash
test -f ~/.claude/skills/context7/skills/context7/SKILL.md && echo ok
```

The clone directory is the plugin root, so `SKILL.md` sits two segments below it. The README's own tests are a stronger check than any of the above and need only bash, jq, git and python3:

```bash
bash tests/context7.sh
bash tests/check-plugin-version.sh
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| context7 | Pass | Pass | Warn |

What leaves the machine is narrow and worth stating exactly. Each invocation sends a library name or library ID and an optional topic string to the Context7 REST API, which the README credits to Upstash. The skill holds no other data source, and the README documents exactly one credential: `CONTEXT7_API_KEY`, marked optional and described as the route to higher rate limits. No account, token or organisation identifier is documented beyond that.

The credential handling is better than most scripts of this shape. The repository's own test suite puts a fake `curl` first on `PATH` and asserts that the `Authorization` header is sent only when `CONTEXT7_API_KEY` is set, and that the header reaches `curl` on standard input rather than as a command-line argument, which keeps the key out of the process list. That is a deliberate design choice, and it is tested on every pull request.

The remaining exposure is the Snyk Warn on the single listing and the fact that there is no second scanner opinion to weigh it against. Pass on Trust Hub and Socket says the two samples found no malware or suspicious install behaviour; Warn on Snyk says one scanner wants a human look. Read `SKILL.md` and `scripts/context7.sh` before deploying, which for a two-file skill is a few minutes.

Two governance details are relevant to a production review. The repository publishes a security assurance case at `docs/SECURITY-ASSURANCE.md` with threat model, trust boundaries and limits, and its pull request checks include secret scanning, workflow static analysis, dependency review with a high-severity failure threshold, Composer Audit and Opengrep SAST. Those checks describe the repository, not your install: the npm route runs a `postinstall` hook that edits `AGENTS.md`, so review that diff on the first install.

## Limitations

- Snapshot data, verified 2026-11-09: 2,112 combined installs across 1 indexed listing; 87 GitHub stars; no standard OSI license declared (GitHub reports NOASSERTION); last pushed 2026-11-09. Counts drift over time.
- The license needs reading rather than assuming. GitHub reports NOASSERTION, which means no standard license is detected at the repository level, while the README documents split licensing: MIT for code and CC-BY-SA-4.0 for content, with `LICENSE-MIT` and `LICENSE-CC-BY-SA-4.0` as separate files. Treat the terms as source-available-with-conditions and read both files before redistributing.
- Snyk returns Warn on the only indexed listing, and a single listing means there is no second data point to compare it against.
- The skill depends on a remote service it does not control. Context7 availability, rate limits and library coverage are Upstash decisions, and the README documents only `CONTEXT7_API_KEY` as the lever for limits.
- The recommended install route is Claude Code specific: `/plugin marketplace add` has no equivalent in other agents, and the plugin directory route relies on Claude Code 2.1.157 or newer. Other agents go through the skills CLI or a manual clone.
- The npm route registers the skill in `AGENTS.md` through a `postinstall` hook, so installs are not side-effect free even though the skill itself is a Markdown file and a shell script.

## Related

- [Upstash Context7 - Versioned Library Docs Setup](/hermes/skills/catalog/upstash-context7-setup)
- [Mintlify Docs Skills - Documentation Platform Setup](/hermes/skills/catalog/mintlify-docs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `search` before `docs` when the library name is ambiguous. The docs endpoint wants a Context7 identifier such as `/prisma/prisma`, not the name a developer typed.
- Always pass a topic. The README's whole argument against the MCP server is token cost, and an unfiltered docs fetch gives that advantage back.
- Set `CONTEXT7_API_KEY` in the environment rather than on a command line. The script is written to pass the header through standard input, and an inline assignment in a shared shell history defeats that.
- Keep both routes if the machine already has MCP configured. The skill is the fallback, not a replacement, and switching costs nothing because it is one directory.
- Read `tests/context7.sh` before trusting the wrapper. It is short, it documents the URL the script builds for each command, and it is the fastest way to see how errors and rate limits surface.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
