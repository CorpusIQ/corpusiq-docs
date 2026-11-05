---
title: "Exa Agent Skills - Neural Search API Setup"
description: "exa-labs/agent-skills on skills.sh: 9.5K combined installs across 5 listings; Exa neural search, contents extraction, company research and lead lists."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/exa-labs-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "exa", "web search", "research"]
---

# Exa Agent Skills - Setup Guide

**Source:** [exa-labs/agent-skills](https://www.skills.sh/exa-labs/agent-skills) via skills.sh - 9.5K combined installs across 5 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 65 stars, MIT licence, last pushed 2026-11-03, 5 SKILL.md directories under skills/
**Category:** Search and research API suite: semantic web search, contents extraction, company research and ICP lead generation
**Quality Tier:** 🟡 Beta - Snyk Warn on build-with-exa and exa-search; MIT; 65 stars.

Exa runs a semantic web index that answers queries by meaning rather than by keyword match. This is the official skills repository for its API, five skills covering the platform at two levels: one broad skill that teaches endpoint selection across search, contents, answer, Agent API, monitors, websets and the OpenAI-compatible endpoints, and four narrow skills that each drill into a single surface.

Two of the narrow skills call the REST API directly with cURL or raw HTTP, which makes them useful to an agent that has no SDK installed. The other two sit on top of Exa Agent: one researches companies and competitors, the other builds ICP-based lead lists and writes them to CSV. Every skill needs an API key from the Exa dashboard, passed as `EXA_API_KEY`.

## Installation

The README installs the set through the Skills CLI:

```bash
npx skills add exa-labs/agent-skills
```

Before using any skill, create an API key at the Exa dashboard and expose it to your agent as `EXA_API_KEY`. The README treats the key as the only prerequisite; there is no separate CLI to install, because `exa-search` and `exa-contents` speak HTTP directly and `build-with-exa` covers the `exa-py` and `exa-js` SDKs for projects that want one.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| build-with-exa | 4,404 | Choosing Exa endpoints and writing calls across search, contents, answer, Agent API, monitors, websets, OpenAI-compatible endpoints, exa-py and exa-js |
| exa-search | 1,606 | POST /search over cURL or raw HTTP: ranked results, domain and category filters, freshness, highlights, structured output and streaming |
| exa-contents | 1,300 | POST /contents over cURL or raw HTTP for text, highlights, summaries, links, subpages and freshness-controlled crawling from known URLs |
| company-research | 1,095 | Researching companies, competitors, funding, news, leadership and market context with Exa Agent and advanced search |
| lead-generation | 1,076 | Generating ICP-based lead lists with Exa Agent, structured scoring and CSV output |

All 5 indexed listings clear the 500-install threshold and appear in the table above, so there is no below-threshold tail.

## Why This Matters for Hermes Agents

An agent that needs current web data usually gets one of two tools: a keyword search API that returns links, or a scraper that returns HTML. Exa's search returns ranked pages with extracted content attached, which collapses two steps into one and removes the fetch layer that most often fails on bot walls.

The two HTTP skills matter because they are SDK-free. An agent working inside a container with no package install permissions can still call `POST /search` and `POST /contents` with cURL and get structured results, so the skill text becomes the harness rather than a wrapper around a dependency.

`build-with-exa` is the routing layer. Endpoint choice is where generated Exa code usually goes wrong, and the skill exists to answer that question first: search for discovery, contents for known URLs, Agent API for multi-step research, websets when the task needs the WebSets surface.

The two research skills turn all of that into business output: a competitor brief or a scored lead list in CSV, produced by an agent rather than by a person opening tabs.

## Usage

| You say | What happens |
|---|---|
| "Which Exa endpoint should I use for this?" | build-with-exa picks between search, contents, answer, Agent API and websets |
| "Search the web for recent papers on this topic and give me highlights" | exa-search calls POST /search with freshness and highlight options |
| "Extract the main text from these twelve URLs" | exa-contents calls POST /contents and returns text, summaries and per-URL status |
| "Research this company against its competitors" | company-research gathers funding, news, leadership and market context |
| "Build me a list of 50 companies matching this ICP" | lead-generation enriches and scores matches and writes a CSV |
| "Use Exa from Python in this service" | build-with-exa shows the exa-py call shape for the chosen endpoint |

## Verification

Read a skill before installing it, and confirm the frontmatter describes the surface you expect:

```bash
curl -fsSL https://raw.githubusercontent.com/exa-labs/agent-skills/main/skills/exa-search/SKILL.md | head -8
```

It should open with `name: exa-search` and a description naming POST /search over cURL or raw HTTP. After the install, check the directories:

```bash
ls ~/.claude/skills | grep -E 'exa|company-research|lead-generation'
```

Five directories should appear. Then confirm the key is visible to the agent process, since every skill fails without it:

```bash
test -n "$EXA_API_KEY" && echo "EXA_API_KEY is set"
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| build-with-exa | Pass | Pass | Warn |
| exa-search | Pass | Pass | Warn |
| exa-contents | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified 2026-11-05: 9,481 combined installs across 5 indexed listings; 65 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- All three sampled skills carry a Snyk Warn, and the skills are instructed to run HTTP calls with your `EXA_API_KEY`. Keep the key in a secret store rather than in a prompt or a committed file.
- The suite is API documentation in skill form. It does not install the Exa SDKs, and `exa-search` and `exa-contents` assume you can reach `api.exa.ai` from the agent's network.
- `company-research` and `lead-generation` run through Exa Agent, while `exa-search` and `exa-contents` are direct endpoints. The two groups have different latency and billing profiles.
- `build-with-exa` overlaps the two HTTP skills on purpose. Loading all three for one task wastes context; pick the broad skill for endpoint choice and one narrow skill for call shape.
- 65 stars and a five-skill scope mean this is a young repository. Expect endpoint names and parameters to change with the API.

## Related

- [Tavily Search - Official LLM-Optimized Web Search CLI Setup](/hermes/skills/catalog/tavily-search-setup)
- [Firecrawl Skills - Web Scraping, Research & Workflow Suite Setup](/hermes/skills/catalog/firecrawl-skills-setup)
- [Open WebSearch Skills - Agent Web Search Setup](/hermes/skills/catalog/open-websearch-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the endpoint before asking for the code. `build-with-exa` answers the routing question in a few lines, and picking wrong is the most expensive mistake with this API.
- Use `exa-contents` whenever you already have URLs. Re-searching for pages you already found is the common waste pattern.
- Ask for highlights rather than full text when the agent only needs to quote or rank, and full text when it needs to reason over the page.
- Treat `lead-generation` output as a draft list. It writes CSV with scores, which is the right shape for review but not for an unattended send.
- Store `EXA_API_KEY` in the agent's environment, never in a skill file. The skills read it from the environment and there is no reason for it to exist anywhere else.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
