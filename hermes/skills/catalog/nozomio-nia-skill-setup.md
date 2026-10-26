---
title: "Nia Skill - Code and Docs Indexing Setup"
description: "nozomio-labs/nia-skill: 56.2K installs from one listing. Index repos, docs, papers and datasets through one wrapper set of shell scripts."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nozomio-nia-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "code search", "retrieval", "research"]
---

# Nia Skill - Setup Guide

**Source:** [nozomio-labs/nia-skill](https://www.skills.sh/nozomio-labs/nia-skill) via skills.sh - 56.2K combined installs across 1 indexed listing; snapshot taken Oct 26, 2026. That figure is carried by a single listing and does not indicate repository popularity: the repo has 26 GitHub stars and 4 forks.
**GitHub:** [nozomio-labs/nia-skill](https://github.com/nozomio-labs/nia-skill) (26 stars; no LICENSE file in the repo, GitHub reports no license while the README's own License section says MIT; pushed 2026-03-29; branch `master`; one `SKILL.md` at the repo root plus 25 shell scripts under `scripts/`)
**Category:** Retrieval / Code and Documentation Indexing
**Quality Tier:** 🟡 Beta (one listing carries 56.2K installs on a 26-star repo, no LICENSE file, no push since 2026-03-29, and a Snyk Fail plus a Socket Warn on its only skill)

Nia is a hosted indexing and search service at trynia.ai, published from the nozomio-labs GitHub organisation, and this repository is its agent-side wrapper. A single `SKILL.md` at the repo root teaches an agent a strict retrieval order - check what is already indexed, search it, and only fall back to web search when nothing is indexed - and 25 bash scripts implement every call against the Nia API at `https://apigcp.trynia.ai/v2`.

The scope is wide for one skill: GitHub repositories, documentation sites, arXiv papers, HuggingFace datasets, local folders, Slack workspaces, Google Drive, X accounts, package registries (npm, PyPI, crates.io, Go proxy, RubyGems), plus an autonomous research agent and a live GitHub code searcher behind a paid plan. Each surface is a separate script with subcommands, so the agent loads instructions once and then shells out to the exact source type it needs.

## Installation

```bash
# Install the skill itself
npx skills add nozomio-labs/nia-skill
```

The scripts are plain bash and need two tools plus an API key:

```bash
# The README lists two runtime dependencies: curl and jq
command -v curl && command -v jq

# API key: either environment variable or config file
export NIA_API_KEY="your-api-key"
# alternative, lower precedence than the environment variable
mkdir -p ~/.config/nia && echo "your-api-key" > ~/.config/nia/api_key
```

A key comes from signing up at trynia.ai, from the guided setup wizard the README names (`npx nia-wizard@latest`), or programmatically through the bundled auth script:

```bash
./scripts/auth.sh signup <email> <password> <organization_name>
./scripts/auth.sh bootstrap-key <bootstrap_token>
./scripts/auth.sh login-key <email> <password>
```

Indexing a first source is what makes the skill useful, and index jobs take one to five minutes according to `SKILL.md`:

```bash
./scripts/repos.sh index "owner/repo"
./scripts/nia.sh sources
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| Nia | 56,227 | Index and search repositories, docs, arXiv papers, HuggingFace datasets, local folders, Slack, Drive, X and package registries, with Oracle research and Tracer code search on the Pro tier |

No indexed listings fall below the threshold; the single listing appears above. There is no tail to summarize, which is the unusual part of this entry: the whole 56,227 figure comes from one skill that is installed as a unit, not from a suite of separately adopted skills. Treat it as a service-integration number rather than evidence that 56,227 teams run this repo.

## Why This Matters for Hermes Agents

The default failure mode for a Hermes research task is the web fetch: truncated pages, summarised snippets, and a model that fills the gaps from memory. This skill exists to interrupt that. Its `SKILL.md` opens with a mandatory workflow that tells the agent to inventory what is already indexed, search it, and only then consider `search.sh web` or `search.sh deep`. For a session that repeatedly asks "how does this library actually implement X", an indexed repository answering from full source beats a documentation page every time.

The second gain is that every surface speaks the same shape. `repos.sh grep`, `sources.sh grep`, `folders.sh grep` and `fs.sh grep` share environment variables for case sensitivity, whole word, context lines and output mode, and most endpoints accept a UUID, a display name or a URL interchangeably. An agent that learns four commands can search code, docs, local notes and Slack without learning four different tools.

Third, the write path is real. `fs.sh` can write, move and delete files on an indexed source, `sources.sh` can delete or bulk-delete sources, and the connectors create Slack and Drive installations. That means an agent can keep an indexed workspace current, and it also means the security section below is not boilerplate.

Finally, the retrieval order is the transferable idea even if you never install this repo. Deciding that indexed, version-pinned sources outrank live web fetches is the same discipline that keeps a Hermes session from confidently quoting last year's API.

## Usage

| You say | What happens |
|---|---|
| "How does streaming work in the Vercel AI SDK?" | `repos.sh index vercel/ai`, waits for the job, then `search.sh query "how does streaming work" vercel/ai` and answers with file references |
| "What does our Stripe integration docs say about idempotency?" | `sources.sh index "https://docs.stripe.com"` once, then `sources.sh grep` and `search.sh query` against that source |
| "Find every place this repo calls the deprecated endpoint" | `repos.sh grep "owner/repo" "deprecated_endpoint"` returns line-level matches without indexing the whole tree |
| "Summarise this arXiv paper" | `papers.sh index 2312.00752`, then `document.sh <source_id> "what is the method"` for a cited answer |
| "What did the team decide in Slack last week?" | `slack.sh configure-channels` then `slack.sh grep <installation_id> "decision"`, or `SLACK_WORKSPACES=<id> search.sh query` |
| "Which of my dependencies have newer docs?" | `deps.sh analyze package.json` maps the manifest, then `deps.sh subscribe` subscribes to the matching documentation sources |
| "Research this market across many repos" | `oracle.sh job "<query>"` on the Pro tier creates an async research job, polled with `oracle.sh job-status` |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -i nia
```

Read the instructions before installing. Both URLs below returned HTTP 200 when checked with `curl` on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/nozomio-labs/nia-skill/master/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/nozomio-labs/nia-skill/master/README.md | head -40
```

Prove the key and the API path work before trusting a workflow. `scripts/usage.sh` is a single `GET $BASE_URL/usage`, so calling it directly isolates the credential from the wrapper:

```bash
curl -s -H "Authorization: Bearer $NIA_API_KEY" https://apigcp.trynia.ai/v2/usage | jq .
./scripts/usage.sh
```

A request to that URL with no header returned HTTP 500 rather than 404 on Oct 26, 2026, which confirms the path exists but says nothing about your key. Run `usage.sh` first and check that numbers come back before indexing anything.

## Security

skills.sh verdicts for the only indexed skill (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| Nia | Pass | Warn | Fail |

Only one listing exists, so only one page could be sampled; the usual two-to-four sample is not possible here. The Socket Warn and the Snyk Fail on a repository with no LICENSE file are the two facts that should decide how you deploy this.

What the scripts actually do, read from `scripts/`: every wrapper sends `Authorization: Bearer $NIA_API_KEY` to `https://apigcp.trynia.ai/v2`, so all indexed content leaves your machine and lives in Nia's cloud. `auth.sh` creates accounts and mints API keys, and with `SAVE_KEY=true` writes the key to `~/.config/nia/api_key` in plain text. `fs.sh` exposes write, write-batch, delete, mkdir and mv against indexed sources. `sources.sh` exposes delete and bulk-delete, and its curation commands can change trust levels. `slack.sh register-token` accepts a Slack bot token as a command-line argument, which puts it in shell history and in any process listing, and it can index channel history. `google-drive.sh` runs an OAuth flow and can index selected files. `repos.sh index` publishes to a global index by default, with `ADD_GLOBAL=false` as the opt-out for private repositories.

## Limitations

- There is no LICENSE file in the repository. GitHub reports no license, while the README's License section says MIT. Until the publisher adds the file, treat the code as unlicensed and ask before redistributing it.
- The install count is a single-listing artifact. 56,227 installs sit on one skill attached to a 26-star repo with 4 forks, so it says nothing about review depth or production adoption.
- The repo is quiet: last push 2026-03-29, roughly seven months before this snapshot. The API base URL is versioned (`/v2`), but an unmaintained wrapper can drift from the service it calls.
- The branch is `master`, not `main`. Keep that in any raw URL you build, and do not "fix" it.
- The README's own Scripts table lists 18 scripts, while `scripts/` contains 25 shell files. `nia.sh`, `x.sh`, `connectors.sh`, `document.sh`, `extract.sh` and `fs.sh` are documented only in `SKILL.md`, so the README undercounts the surface you are installing.
- Several workflows are paywalled. `oracle.sh`, `tracer.sh` and `search.sh deep` are marked Pro in `SKILL.md`, and the README does not state what the free tier includes.
- Snapshot data, verified Oct 26, 2026: 56,227 combined installs across 1 indexed listing; 26 GitHub stars; no license file; last pushed 2026-03-29. Counts drift over time.

## Related

- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup) - the same research discipline without a hosted index behind it.
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup) - a lighter research dependency when you do not need a persistent index.
- [Hermes ArXiv Agent - ArXiv Paper Fetcher Setup](/hermes/skills/catalog/hermes-arxiv-agent-setup) - paper retrieval without the Nia account.
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup) - the live-web path Nia treats as a last resort.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Index before you ask. A `repos.sh index` on the one repository a task depends on is worth more than ten universal searches, and `nia.sh sources` tells you what is already there in one call.
- Never put `search.sh universal` in front of a Slack question. It does not search Slack; use `search.sh query` with `SLACK_WORKSPACES`, or `slack.sh grep` directly.
- Use `ADD_GLOBAL=false` on `repos.sh index` for anything private, then confirm with `repos.sh list` that the source did not enter the shared index.
- Redirect the scripts' JSON into `jq` rather than reading it raw; every wrapper already pipes through `jq` when available, and the output is stable enough to diff between runs.
- Keep the API key in the environment for the session instead of the config file when the host is shared, and revoke keys you minted with `auth.sh` once the task is done.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
