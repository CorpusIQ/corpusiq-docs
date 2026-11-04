---
title: "Brave Search Skills - Web Grounding for Agents"
description: "brave/brave-search-skills on skills.sh: 18.0K combined installs across 13 listings; official Brave Search API skills for grounding and local data."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/brave-search-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "web search", "rag grounding", "search api"]
---

# Brave Search Skills - Setup Guide

**Source:** [brave/brave-search-skills](https://www.skills.sh/brave/brave-search-skills) via skills.sh - 18.0K combined installs across 13 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 193 stars, MIT licence, last pushed 2026-10-29, 13 SKILL.md directories (12 under skills/, one under clawhub/)
**Category:** Web search for agents: official Brave Search API skills for grounding, news, local and summarization workflows
**Quality Tier:** 🟡 Yellow: bx-search draws a Gen Agent Trust Hub Fail, and three other sampled skills carry Snyk Warns

This is Brave's own repository: official skills for using the Brave Search API with coding agents, published under a MIT licence by the vendor that runs the endpoint. Thirteen skills, mostly one per endpoint, each a short wrapper that documents the request shape and the response you should expect back.

Two of the thirteen are where most agents should start. `bx` is an all-in-one CLI over the other endpoints that returns pre-extracted, token-budgeted content, and `llm-context` does the same job over HTTP against `/res/v1/llm/context`. The README marks both as recommended. The rest cover web, images, news and videos search, three local skills, `suggest`, `spellcheck`, and `answers` for AI-generated answers over an OpenAI-compatible chat endpoint.

It is a paid API. The README sends you to api.search.brave.com for a key, and its rate-limit note points at your plan on that dashboard; it does not describe a free tier, and this guide does not claim one.

## Installation

The README lists your key first. Its own security note prefers agent-native config over shell profile exports, because scoped configs limit what a coding agent can read. Claude Code takes the key through settings:

```json
{
  "env": {
    "BRAVE_SEARCH_API_KEY": "your-key"
  }
}
```

For any other agent, the portable version is an environment variable:

```bash
export BRAVE_SEARCH_API_KEY="your-key"
```

Claude Code also supports the plugin marketplace, which needs no git and auto-updates:

```text
/plugin marketplace add brave/brave-search-skills
/plugin install brave-search-skills@brave-search
```

The no-git route copies every skill into the user-level directory in one line:

```bash
mkdir -p ~/.claude/skills && curl -sL https://github.com/brave/brave-search-skills/archive/main.tar.gz | tar xz -C ~/.claude/skills --strip-components=2 brave-search-skills-main/skills
```

There is a universal installer too, for agents outside the README's table:

```bash
npx openskills install brave/brave-search-skills
```

The README documents the same pattern per agent, with the skills directory swapped for `.cursor/skills`, `.github/skills`, `.agents/skills` (Codex), `.windsurf/skills` or `~/.openclaw/skills`. For Hermes, copy the `skills/` directories into the profile skills directory and keep the API key in the profile environment.

## What It Provides

Twelve endpoint skills plus one CLI variant, all indexed above the table threshold.

| Skill | Installs | Use For |
|---|---|---|
| web-search | 4,714 | Ranked web results with snippets and thumbnails; freshness, SafeSearch, Goggles, pagination |
| images-search | 1,700 | Image results with title, source URL and thumbnail; up to 200 per call |
| news-search | 1,672 | News articles with freshness and date-range filters, plus Goggles ranking |
| llm-context | 1,303 | Pre-extracted page text, tables and code for RAG grounding, over GET or POST |
| videos-search | 1,252 | Video results with duration, view count and creator, plus freshness filters |
| answers | 1,245 | AI-grounded answers over an OpenAI-compatible chat completions endpoint, with citations |
| local-pois | 1,165 | Full business detail for known POI IDs: ratings, hours, contact, up to 20 per call |
| bx | 1,145 | All-in-one CLI over the other endpoints, with token-budgeted output for shell work |
| local-descriptions | 1,142 | AI-written POI descriptions grounded in web context, max 20 IDs per request |
| spellcheck | 1,134 | Query correction for pre-search cleanup or a did-you-mean prompt |
| suggest | 1,124 | Query autocomplete under 100ms, typo-resilient, with optional rich entity data |
| local-place-search | 424 | Standalone place search by coordinates or location string, no POI ID needed |
| bx-search | 12 | OpenClaw packaging of the bx CLI skill under clawhub/, licence MIT-0 |

All 13 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Grounding is the difference between an agent that searches and an agent that cites. `llm-context` returns page text already extracted for a model, so a Hermes agent can quote a source without a second fetch, parse and strip step.

Endpoint-per-skill is a clean design. The agent loads a short skill for the endpoint it needs instead of carrying a full API manual in context, which matters on a long session with a fixed window.

Goggles are the feature with no equivalent in most search APIs: a small text program that discards, boosts or downranks domains, carried by web, news, images, videos and `llm-context`. For a researcher agent, that is a reusable filter you write once and pass on every query.

`answers` speaks the OpenAI chat completions shape, so an agent already wired for an OpenAI-compatible client can point at Brave without a new SDK. Research mode adds multi-search iteration, streaming required.

Local coverage is three skills deep: `local-place-search` finds the place with no prior call, then `local-pois` and `local-descriptions` enrich the IDs it returns. That chain is the pattern to copy for any two-step lookup.

The caution is cost and quota. Every call is billable against a plan, and nothing in the skills caps a retry loop.

## Usage

| You say | What happens |
|---|---|
| "Search the docs for this error" | bx runs a token-budgeted context query and returns extracted page text |
| "What shipped in the last day?" | news-search with freshness set to the past day |
| "Find every page on our domain that mentions pricing" | web-search with a Goggles program that scopes and boosts the domain |
| "What is the best coffee near this address?" | local-place-search finds the place, then local-pois and local-descriptions enrich it |
| "Ground this answer in sources" | llm-context returns extracted content with URLs to cite |
| "Fix the typo before searching" | spellcheck returns the corrected query |
| "Give me an answer with citations" | answers posts to the chat completions endpoint in single-search or research mode |

## Verification

Confirm the skills landed:

```bash
ls ~/.claude/skills
```

Then fetch one raw file before installing anything. This path is `skills/web-search/SKILL.md` on branch main and returned 200 when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/brave/brave-search-skills/main/skills/web-search/SKILL.md | head -20
```

Frontmatter plus an endpoint description confirms the listing is backed by a real file. `skills/llm-context/SKILL.md` and `clawhub/bx-search/SKILL.md` are the other two paths worth checking, since the second one sits outside `skills/`. The install index is at https://www.skills.sh/brave/brave-search-skills.

To check the key end to end, the README's own web search call is the smallest test:

```bash
curl -s "https://api.search.brave.com/res/v1/web/search?q=agent+skills" -H "Accept: application/json" -H "X-Subscription-Token: ${BRAVE_SEARCH_API_KEY}" | head -20
```

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| web-search | Pass | Pass | Warn |
| llm-context | Pass | Pass | Warn |
| local-pois | Pass | Pass | Warn |
| spellcheck | Pass | Pass | Pass |
| bx-search | Fail | Pass | Warn |

`bx-search` is the only Fail in the sample, and it is also the only listing that asks the agent to prefer itself over a built-in search tool. Read that skill's body before adding it to a profile, and keep the API key scoped rather than exported globally, as the README's own security note advises.

## Limitations

- Snapshot data, verified November 4, 2026: 18,032 combined installs across 13 indexed listings; 193 GitHub stars; MIT licence; last pushed 2026-10-29. Counts drift over time.
- A key and a plan are required. The README documents no free tier and ties rate limits to the plan on the API dashboard, so check pricing before wiring this into a recurring loop.
- `bx` is a wrapper, not the binary. The CLI itself ships separately from brave/brave-search-cli and is installed with the skill's own install script or an OpenClaw release download.
- `bx-search` lives under `clawhub/`, not `skills/`, carries 12 installs against 4,714 for `web-search`, and is absent from the README's endpoint table. It is an OpenClaw packaging of the same CLI under MIT-0.
- The README's Available Skills table documents 12 skills while the install index carries 13 listings; the extra one is `bx-search`.
- Every request is billable, and the skills carry no caching or retry cap. An agent that re-searches on a failed parse spends quota without a signal.

## Related

- [Tavily Search - Official LLM-Optimized Web Search CLI Setup](/hermes/skills/catalog/tavily-search-setup)
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `llm-context` for grounding and `bx` for shell work. The README marks both as recommended, and they cover most agent traffic.
- Keep the key in agent-native config, as the README's security note says. A shell export is inherited by every process the agent spawns.
- Use Goggles to cut noise before paginating. A three-line `$discard` and `$site` program is cheaper than filtering results after the fact.
- Cache results inside a task. The same query rarely changes within a run, and every repeat call is billed.
- Skip `spellcheck` mid-flow. Most search endpoints already correct queries, so it earns its place only in a pre-search or did-you-mean UI.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
