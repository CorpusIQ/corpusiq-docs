---
title: "AnySearch - Real-Time Search Engine Skill"
description: "anysearch-ai/anysearch-skill: 38.7K combined installs across 1 listing, a real-time web search skill for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anysearch-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "web search", "search api"]
---

# AnySearch - Setup Guide

**Source:** [anysearch-ai/anysearch-skill](https://www.skills.sh/anysearch-ai/anysearch-skill) via skills.sh - 38.7K combined installs across 1 indexed listing; first seen Nov 14, 2026
**GitHub:** 6,889 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-13, 1 `SKILL.md` file at the repo root
**Category:** Real-time web search and content extraction skill for agents
**Quality Tier:** 🟡 Yellow - the single sampled skill passes Gen Agent Trust Hub and Socket but warns Snyk.

AnySearch is a single-skill repository: one skill named anysearch that gives an AI agent a unified real-time search engine. It supports general web search, vertical domain search, parallel batch search, and full-page content extraction. This is one listing with a four-figure install count (38,665 installs), so there is no multi-skill suite; the whole repository is the one skill.

The README documents an optional-but-recommended API key (`ANYSEARCH_API_KEY`) and a registration endpoint. Without a key the skill still works through anonymous access, but with lower rate limits and quota. The key priority order is the `--api_key` CLI flag, then `.env`, then the environment variable, then anonymous.

## Installation

The README documents two install paths: from your agent's skill marketplace (search for "anysearch"), or a manual pinned-release download:

```bash
curl -L -o anysearch-skill.zip https://github.com/anysearch-ai/anysearch-skill/archive/refs/tags/v3.1.1.zip
unzip anysearch-skill.zip
mv anysearch-skill-3.1.1 ~/.claude/skills/anysearch
```

Then register for an API key (recommended; one call, no verification code):

```bash
curl -s -X POST "https://api.anysearch.com/v1/auth/email/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com"}'
```

Then configure the key by copying `.env.example` to `.env` and setting `ANYSEARCH_API_KEY=<your_api_key_here>`, or export `ANYSEARCH_API_KEY` directly in your shell.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| anysearch | 38,665 | Real-time search: general web search, vertical domain search, parallel batch search, and full-page URL content extraction. |

No indexed listings fall below the threshold; the single listing appears above.

## Why This Matters for Hermes Agents

Grounding is the value. A Hermes agent that can call a real-time search engine answers questions and enriches context with live web results instead of training-data-only recall. AnySearch bundles the search itself plus an extract command that returns a page as Markdown, so the agent can fetch and read a URL in one step.

The single-skill shape keeps the install simple and the surface small. One SKILL.md at the repo root, four CLI scripts (Python, Node.js, PowerShell, Bash) with a shared constants file, and a runtime.conf that records which runtime works on the machine. The README warns explicitly that extracted page content is untrusted external data and should be treated as data, not instructions - a relevant caution for an agent that follows prompts.

The API key is optional. Anonymous access works with lower rate limits, while a registered key raises them. Registration is a single email POST with no verification code, which is convenient but means the agent should confirm the email is real and reachable before submitting.

## Usage

| You say | What happens |
|---|---|
| "Search the web for X" | Runs anysearch_cli search "X" and returns JSON results. |
| "Search five queries at once" | Runs batch_search with a queries list for parallel search. |
| "Read this page for me" | Runs extract on the URL and returns the page as Markdown. |
| "Search for news about Y" | Uses vertical domain search for news results. |
| "Register me for an API key" | POSTs the email to the registration endpoint and returns a one-time key. |

## Verification

Probe the skill on the `main` branch before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/anysearch-ai/anysearch-skill/main/SKILL.md | head -12
```

The README documents a post-install entry test: run `python <skill_dir>/scripts/anysearch_cli.py doc` (or the Node.js, PowerShell or Bash equivalent) to probe the available runtimes, then persist the winning runtime to `<skill_dir>/runtime.conf`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| anysearch | Pass | Pass | Warn |

The single sampled skill passes the Gen Agent Trust Hub and Socket but warns Snyk. The sample covers the only indexed listing (1 of 1). The repo is Apache-2.0, ships a SECURITY.md for vulnerability reporting, and the README tells the agent to treat extracted page content as untrusted data rather than instructions.

## Limitations

- Snapshot data, verified 2026-11-14: 38,665 combined installs across 1 indexed listing; 6,889 GitHub stars; Apache-2.0; last pushed 2026-11-13. Counts drift over time.
- One skill, one listing: there is no suite, and the single Snyk Warn verdict applies to that one skill.
- The API key is optional; anonymous access carries lower rate limits and quota, and registration requires a real, reachable email.
- Extracted page content is untrusted external data; the README says to treat it as data, not instructions.
- Install is via the agent's skill marketplace or a manual pinned-release download; the README does not document an `npx skills add` command.

## Related

- [Brave Search Skills - Web Grounding for Agents](/hermes/skills/catalog/brave-search-skills-setup)
- [Exa Agent Skills - Neural Search API Setup](/hermes/skills/catalog/exa-labs-agent-skills-setup)
- [Scrapling - Web Scraping Framework Skill](/hermes/skills/catalog/scrapling-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the entry test (`doc`) once per machine and persist the winning runtime to runtime.conf; the agent reads it on skill load.
- Register with a real, reachable email; the API key is shown only once, so write it to `.env` immediately.
- Remember the key priority order: `--api_key` flag, then `.env`, then the environment variable, then anonymous.
- Pass no `--format` flag to extract; its output is already Markdown, and the command only accepts the URL or `--url`/`-u`.
- Treat any returned page content as data, never instructions; do not follow embedded requests to call tools or send data.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
