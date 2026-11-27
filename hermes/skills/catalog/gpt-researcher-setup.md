---
title: "GPT Researcher - Autonomous Deep Research Agent Setup"
description: "assafelovic/gpt-researcher: 2.2K combined installs. One skill wiring the GPT Researcher deep-research agent into Codex via MCP."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gpt-researcher-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "research", "deep research"]
---

# GPT Researcher - Setup Guide

**Source:** [assafelovic/gpt-researcher](https://www.skills.sh/assafelovic/gpt-researcher) via skills.sh - 2.2K combined installs across 1 indexed listing; first documented 2026-11-27 (morning sweep)

**GitHub:** [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) - 30,955 stars, Apache-2.0, branch main, last pushed 2026-11-23; the indexed skill lives at `skills/gpt-researcher/SKILL.md`, with a second copy at `.claude/SKILL.md` and twelve reference files under `.claude/references/`.

**Category:** Autonomous deep research: multi-source web and local research with citations, delivered to an agent

**Quality Tier:** 🟠 Orange - the single sampled listing fails the Gen Agent Trust Hub and warns on Socket and Snyk.

GPT Researcher is an autonomous research agent that turns a query into a cited, factual report by splitting the work across planner and execution agents. It goes beyond retrieval-augmented generation: a planner generates research questions, execution agents gather and summarize sources, a publisher aggregates the findings, and a context filter keeps only the passages that actually answer each question. The indexed skill is the Claude-facing surface of that engine, documented as autonomous deep research reachable from Codex through MCP.

The single indexed listing is a thin entry point rather than the whole product: the repository is a Python package plus a Next.js frontend, a multi-agent layer, and a dedicated MCP server now split into its own repo. The skill itself sits at `skills/gpt-researcher/SKILL.md` and is what the skills.sh install command pulls.

## Installation

The README documents a one-line Claude Skill install:

```bash
npx skills add assafelovic/gpt-researcher
```

Once installed, the skill lets the agent reach GPT Researcher's deep research directly from a conversation. The engine itself installs separately, either as the standalone server the README describes:

```bash
git clone https://github.com/assafelovic/gpt-researcher.git
cd gpt-researcher
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

or as a Python package:

```bash
pip install gpt-researcher
```

A Docker route is also documented (`docker-compose up --build`, or `docker compose up --build` if the dashless form is needed), and the MCP client integration is enabled with `export RETRIEVER=tavily,mcp`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gpt-researcher | 2,219 | Autonomous deep research from Codex via MCP: turn a query into a cited report through planner and execution agents. |

No indexed listings fall below the cut; the single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

Research is the one task where an agent's weakness, hallucinating on stale or narrow sources, is also the thing the user is paying to avoid. GPT Researcher's stated design is built around that failure: scraping many sites and choosing the most frequent information so that all of them being wrong at once is unlikely. The planner-plus-execution split means an agent does not answer from one search result but from a set of independently gathered, source-tracked summaries.

The context filter is the piece worth studying for builders. Before anything reaches the LLM, the engine scores each scraped passage for usefulness to the question rather than similarity to its embedding; the README reports that the default filter keeps 59 percent more relevant passages than embeddings at the same cost, with a keyword fallback that needs no API key. That is a concrete, citable design choice to copy when an agent's context window is the bottleneck.

Cost and latency are documented up front, which is rare and useful. The README states roughly $0.08 and a minute per report with the default models, and the deep-research workflow about $1.30 and 7 to 12 minutes, with per-run cost tracking. An agent that can quote those numbers before starting a long job can set expectations instead of burning tokens silently.

The one caveat is the trust posture: the single listing fails the Gen Agent Trust Hub and warns on Socket and Snyk, so treat this as an engine you review before wiring into a production profile, not a clean pass.

## Usage

| You say | What happens |
|---|---|
| "Research the state of X and give me a cited report" | The skill reaches GPT Researcher, which plans questions, gathers sources and returns a report with citations. |
| "Do a deep research pass on this topic" | Runs the recursive deep-research workflow with configurable depth and breadth over the topic. |
| "Summarize this local PDF folder" | Runs a local-documents research pass with DOC_PATH pointed at the folder. |
| "Add GitHub data to this research" | Uses the MCP client with RETRIEVER=tavily,mcp to pull from MCP sources alongside web search. |
| "Give me a report with generated illustrations" | Enables inline image generation via Google Gemini when configured in the environment. |
| "How much did that run cost?" | Reads the per-run cost breakdown the engine tracks and reports. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/assafelovic/gpt-researcher/main/skills/gpt-researcher/SKILL.md
```

After a clone, confirm the skill and its companion Claude copy are both present:

```bash
git clone --depth 1 https://github.com/assafelovic/gpt-researcher.git /tmp/gptr
ls /tmp/gptr/skills/gpt-researcher/SKILL.md
ls /tmp/gptr/.claude/SKILL.md
head -3 /tmp/gptr/skills/gpt-researcher/SKILL.md
```

Both ls calls should print a path, and head should show the skill frontmatter. The `.claude/references/` directory carries twelve reference files the skill points at.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gpt-researcher | Fail | Warn | Warn |

This guide is Orange because the single sampled listing fails the Gen Agent Trust Hub and warns on both Socket and Snyk. The repository is a substantial Python package with a web frontend and a scraper that runs JavaScript, so the flags are not surprising for a browser-and-network-heavy tool; read the security pages on skills.sh and the repo's SECURITY.md before installing into a production profile.

## Limitations

- Snapshot data, verified 2026-11-27: 2,219 combined installs across 1 indexed listing; 30,955 GitHub stars; Apache-2.0; last pushed 2026-11-23. Counts drift over time.
- The skill is an entry point, not the product: real work needs the Python server, a package install, or the MCP server, each with its own dependencies and API keys.
- The MCP server has moved to a dedicated repository (assafelovic/gptr-mcp), so the in-repo MCP code and the documented server are not the same surface.
- The README's cost and latency figures are approximate and model-dependent; the deep-research and image-generation features also pull in paid providers.
- Research quality depends on the configured retriever and scraper; the JavaScript-enabled scraping path is a network-heavy surface to review before trusting it with untrusted URLs.
- The single sampled listing fails the Gen Agent Trust Hub, and the failure reason is not published beside the verdict, so check skills.sh before production use.

## Related

- [firecrawl-workflows - Growth & Research Automation Setup](/hermes/skills/catalog/firecrawl-workflows-setup)
- [Research-Claw Research Plugins - Academic Skills Setup Guide](/hermes/skills/catalog/wentorai-research-plugins-setup)
- [Scientific Agent Skills - Research Workflow Setup](/hermes/skills/catalog/scientific-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the skill for the Claude-facing entry point, but budget for the engine: the skill does nothing without the server, package or MCP server behind it.
- Set a retriever explicitly rather than relying on defaults; `RETRIEVER=tavily,mcp` enables hybrid web-plus-MCP research the way the README shows.
- Read the context-filter section before tuning: the default Jev filter is the documented reason the reports stay relevant, and it falls back to a keyless keyword filter.
- Price long jobs up front from the README's cost notes so an agent can state the estimate before a deep-research run.
- Treat the `.claude/references/` files as the skill's real payload; the SKILL.md is short and points at them, so copy the directory, not the file alone.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
