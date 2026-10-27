---
title: "New Skills - October 27, 2026 Morning"
description: "Skills.sh sweep (Oct 27 morning): 885 skills scanned, the standing window silent again, and 5 queued publisher clusters shipped for 126,276 combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/marketplace/new-oct27-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 27, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 91 NEW, 269 PARTIAL. It was the seventeenth consecutive fire with nothing new above the 1,000-install trigger, and its top row was `zzci/skills` at 365 installs.

The trending board served 505 entries across 51 sources and every one of the 51 was already in the catalog. So this fire drew on the queue the Oct 26 topic probe left behind: sixteen publisher clusters sized above the 5,000-install floor and waiting for guides. Five of them are documented below.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 885 (0 failed queries) |
| NEW (not in catalog) | 91 |
| PARTIAL (source known, skill not cataloged) | 269 |
| Trending board | 505 entries / 51 sources, all 51 covered |
| Above-floor finds in the window | 0 (top row 365) |
| Queued converts documented | 5 |
| New publisher guides | 5 (103 indexed listings, 126,276 combined installs) |
| Marketplace count | 1,182+ to 1,187+ |

## New Publisher Guides

### 1. Anthropic Financial Services (31,133 combined)

**Source:** [anthropics/financial-services](https://www.skills.sh/anthropics/financial-services), 13 indexed listings, top skill `earnings-analysis` at 3,365; 40,842 stars; Apache-2.0; branch main.

Anthropic's own reference implementation for finance work: investment banking, equity research, private equity, fund administration and wealth management. It ships named workflow agents (Pitch Agent, Market Researcher, Earnings Reviewer, Model Builder, GL Reconciler, Month-End Closer), vertical skill bundles, and MCP connectors to commercial data providers. There are two delivery paths from one source: a Claude Cowork plugin, or the same system prompt and skills deployed through the Claude Managed Agents API. That second path is what makes it readable outside the Claude client.

The install spread is unusually flat across the suite, from 1,959 to 3,365, which is what a vendor drop looks like before the community has sorted it. Three listings (`equity-research`, `macro-rates-monitor`, `option-vol-analysis`) live under `plugins/partner-built/lseg/` and are LSEG authored, not Anthropic's own. The connectors reach commercial providers, so a full install is not free even though the skills are.

### 2. Motion Design Skills (26,619 combined)

**Source:** [iart-ai/motion-design-skills](https://www.skills.sh/iart-ai/motion-design-skills), 9 indexed listings, top skill `motion-art-direction` at 3,438; 167 stars; MIT; branch main.

Nine skills for one discipline, split by job rather than by topic: one decides direction, one sets how things should move, two carry the engines (After Effects, Remotion), five carry brand elements (color, composition, logos, backgrounds, edit rhythm). The output shape is the tell that practitioners wrote these: `animation-principles` returns durations, cubic-bezier curves, stagger offsets and spring configs, `shot-composition` returns layer structure and camera-move plans with numbers, `color-motion` returns exact OKLCH and hex values.

Every listing sits between 2,658 and 3,438 installs, the tightest band in the catalog, and every `SKILL.md` is version 0.1.0. These are knowledge skills, not renderers: `after-effects` needs the application and `remotion-video` needs a Remotion project, so treat the pack as the reasoning layer above the tool.

### 3. Astronomer Agents (25,523 combined)

**Source:** [astronomer/agents](https://www.skills.sh/astronomer/agents), 38 indexed listings, top skill `airflow` at 1,461; 456 stars; Apache-2.0; branch main.

Astronomer's agent layer for data engineering, and it is three products in one repository: an Airflow MCP server (`astro-airflow-mcp`), an `af` CLI that talks to the Airflow REST API, and 35 skills covering DAG authoring, testing, debugging, lineage, freshness, the Airflow 2 to 3 migration, dbt through Cosmos, and warehouse SQL analysis.

The split matters in practice. A question about a failing task and a question about revenue by product route to different skills with different tools behind them. Three indexed listings (`init`, `initializing-warehouse`, `discovering-data`) carry install counts but have no directory in the current tree, and `airflow-adapter` lives inside the MCP server's own `.claude/skills/` rather than the top-level `skills/` tree.

### 4. Deep Agents (21,754 combined)

**Source:** [langchain-ai/deepagents](https://www.skills.sh/langchain-ai/deepagents), 20 indexed listings, top skill `langgraph-docs` at 4,547; 30,639 stars; MIT; branch main.

LangChain's opinionated agent harness: filesystem, sub-agents in isolated context windows, context management, shell access, persistent memory, human-in-the-loop approval and on-demand skills. It sits on LangGraph as the graph runtime and `create_agent` as a minimal harness.

The skills indexed under it are not one published package. They are the example and built-in skills that ship with the harness (`libs/code/examples/skills/`, `libs/code/deepagents_code/built_in_skills/`, and per-example agent directories under `examples/`), and skills.sh indexes each `SKILL.md` directory separately, so 20 listings measure people adding a directory rather than adoption of a suite. Several of them assume the tool surface of the example agent that ships them: `sql_db_query` for the SQL pair, `generate_image` for the content pair. Read it as a working tour of harness skills, not a curated install. `swarm` carries 98 installs and has no matching directory in the tree.

### 5. Pydantic Skills (21,247 combined)

**Source:** [pydantic/skills](https://www.skills.sh/pydantic/skills), 23 indexed listings, top skill `building-pydantic-ai-agents` at 5,696; 145 stars; MIT; branch main.

Pydantic Services' first-party agent tooling for the three surfaces it owns: Pydantic for validation, Pydantic AI for agents, Logfire for the traces, logs and evals those agents produce. It packages the material as five host plugins for Claude Code, Codex and Cursor plus standalone `SKILL.md` files in the agentskills.io layout for any other agent.

`logfire-setup` is a router rather than an installer: it inspects the request and hands off to a specialist for instrumentation, infrastructure metrics, evals, frontend observability, Gateway routing or coding-agent capture, and each specialist owns its own auth and verification steps. A separate family of nine `migrating-*` skills moves existing code over to Pydantic AI from LangChain, the OpenAI Agents SDK, Vercel AI SDK, Google ADK, Claude Agent SDK, Mastra, Agno, Pi and Deep Agents. Two trees back the 23 listings: 21 standalone skills mirrored into 22 packaged copies, so install one tree, not both.

## What Was Checked and Rejected

Nothing was rejected on security grounds this fire, and no source above needed a security exclusion: skills.sh verdicts were not sampled for these five, so every guide says so plainly and points the reader at the skills.sh security pages rather than inventing a verdict.

Reconfirmed this fire: the standing window's silence is not a measurement artifact. The NEW set has stayed in the same 19 to 106 row band for seventeen fires while the total install weight moves between the board, the topic probes and the publisher queries.

## Queue for the Next Fire

Eleven sized publisher clusters from the Oct 26 topic probe are still waiting, led by cap-go/capgo-skills (45,261), mblode/agent-skills (32,174), shipshitdev/skills (27,426), iart-ai family siblings, sumsub/agent-skills (24,593), qdrant/skills (14,361) and pydantic siblings. Beyond them sit the remaining probed sources, each of which needs a publisher query before it can be dismissed: board rows have understated a publisher by as much as 652x.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
