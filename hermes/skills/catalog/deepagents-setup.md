---
title: "Deep Agents - Batteries-Included Agent Harness Setup"
description: "Example and built-in skills in LangChain's Deep Agents harness: 21.8K combined installs across 20 indexed listings for research, SQL and writing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/deepagents-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "agent harness", "subagents", "langchain"]
---

# Deep Agents - Setup Guide

**Source:** [langchain-ai/deepagents](https://www.skills.sh/langchain-ai/deepagents) via skills.sh - 21.8K combined installs across 20 indexed listings; first documented 2026-10-27 (Oct 27 morning sweep)

**GitHub:** [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) - 30,639 stars, MIT, branch main, 26 `SKILL.md` directories in the tree: 4 under `libs/code/examples/skills/`, 4 under `libs/code/deepagents_code/built_in_skills/`, 15 inside per-example agent directories under `examples/`, 1 at `.agents/skills/` and 2 safety skills under `libs/talon/`

**Category:** Agent frameworks and harnesses

**Quality Tier:** 🟡 Beta - large repository following, 30.6K stars, 20 indexed listings for one harness

Deep Agents is LangChain's opinionated agent harness: an agent loop with a filesystem, sub-agents that run in isolated context windows, context management, shell access, persistent memory, human-in-the-loop approval and on-demand skills bundled in. It sits on top of LangGraph as the graph runtime and `create_agent` as a minimal harness, and the README is explicit about the layering rather than treating the three as separate products.

The skills indexed under this repository are not one published skill package. They are the example skills and built-in skills that ship with the harness, spread across `libs/code/examples/skills/`, `libs/code/deepagents_code/built_in_skills/` and the per-example agent directories under `examples/`. skills.sh indexes each `SKILL.md` directory individually, which is why one harness produces 20 listings and 21.8K combined installs. Read this guide as a tour of working skills inside a harness reference implementation, not as an install of a curated suite.

## Installation

The Python library is the shortest path to the harness. The README documents one command and a factory call:

```bash
uv add deepagents
```

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="openai:gpt-6-astra",
    system_prompt="You are a research assistant.",
)
```

The terminal coding agent, Deep Agents Code, is a pre-built agent shipped from the same repository. The README gives the installer verbatim:

```bash
curl -LsSf https://langch.in/dcode | bash
```

That installer is the normal path to the built-in skills, since Deep Agents Code is the agent that ships and loads them. From there you can scaffold your own skill with the built-in creator:

```bash
dcode skills create my-skill
dcode skills create my-skill --project
```

The skills.sh CLI form works on the indexed listings. The repository-wide install is the generic path:

```bash
npx skills add langchain-ai/deepagents
```

Per-skill installs take one name at a time. Confirm the name exists in the current tree first, because several of these skills live inside example agents rather than a single `skills/` root:

```bash
npx skills add langchain-ai/deepagents --skill langgraph-docs
```

The other option is to copy a skill directory into one of the discovery paths the harness documents: `~/.agents/skills/` for user scope shared across agent tools, or `.deepagents/skills/` for project scope. Project skills override user skills and any user or project skill overrides a built-in of the same name.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| langgraph-docs | 4,547 | Fetching the LangGraph documentation index from `docs.langchain.com/llms.txt`, picking the two to four most relevant pages, and answering implementation questions on stateful agents, multi-agent workflows and human-in-the-loop patterns from the fetched text. |
| web-research | 3,896 | Multi-source research with a written plan: a `research_plan.md` of two to five subtopics, up to three parallel subagents at three to five searches each, findings saved to files, then a synthesised report with cited URLs. |
| social-media | 2,729 | LinkedIn posts and X threads: platform length and tone rules, a hook on the first line, thread structure, hashtags, and a required companion image written to `linkedin/<slug>/` or `tweets/<slug>/`. |
| arxiv-search | 2,327 | Running the bundled `arxiv_search.py` against arXiv for a query with an optional paper cap, returning titles and abstracts sorted by relevance. |
| blog-post | 2,214 | Long-form posts and tutorials: hook, problem context, body and conclusion structure, SEO handling, and a required `hero.png` cover image under `blogs/<slug>/`. |
| skill-creator | 1,326 | The built-in skill authoring guide: the five skill discovery directories and their precedence, progressive disclosure rules, `init_skill.py` scaffolding, `quick_validate.py` checks and the frontmatter contract. |
| query-writing | 1,268 | Text-to-SQL: SELECTs through to multi-table JOINs, aggregations and subqueries, planned with a todo list for complex queries, executed through the `sql_*` tools with a LIMIT and a DML ban. |
| schema-exploration | 1,267 | Database orientation: listing tables, describing column types and primary and foreign keys, and mapping the JOIN path an entity question needs. |

The remaining 12 indexed listings range from 29 to 271 installs.

## Why This Matters for Hermes Agents

Most skill libraries are collections of instructions. This one is the reference implementation of an agent that uses skills, and that is the more useful artifact for anyone building their own harness. The delegation pattern in `web-research` is the clearest example: write a plan file, hand each subtopic to a subagent that saves its own findings file, then read those files and synthesise. Nothing passes between the agents in chat history, which is exactly what keeps a long run inside its context window.

The `skill-creator` directory is the piece worth reading even if you install nothing. It documents five skill directories with a precedence order, the progressive disclosure rules that decide what belongs in `SKILL.md` versus a `references/` folder, and a validation script that checks naming, description limits and the allowed frontmatter keys. Any team writing skills against a harness has to answer those questions, and this answers them in writing.

The skills themselves are tool-bound rather than generic. `query-writing` drives `sql_db_query` and `sql_db_schema`, `arxiv-search` shells out to a Python script it ships, and the content skills call `generate_image` or `task`. That is a feature for a harness and a caveat for a plain Hermes agent: the reasoning transfers, the tool calls have to be remapped.

## Usage

| You say | What happens |
|---|---|
| "How do I add human-in-the-loop approval in LangGraph" | langgraph-docs pulls the documentation index, selects two to four pages and answers from the fetched text rather than from training data. |
| "Research how teams run agent memory in production and cite sources" | web-research writes a plan, delegates up to three subtopics in parallel, saves findings to files and synthesises a report with URLs. |
| "Turn this release into a LinkedIn post" | social-media researches the topic first, drafts a hook and body within the platform limits, then generates the companion image. |
| "Find recent papers on retrieval evaluation" | arxiv-search runs the bundled script with a paper cap and returns titles and abstracts sorted by relevance. |
| "What tables are in this database and how do they join" | schema-exploration lists tables, describes columns and types, and maps the foreign key chain for the entity in question. |
| "Revenue by country, top five" | query-writing inspects the schema, writes the JOIN with GROUP BY, executes it with a LIMIT and formats the result. |
| "Create a skill for our deploy checklist" | skill-creator asks for concrete examples, scaffolds the directory with `init_skill.py` or `dcode skills create`, then validates the frontmatter. |

## Verification

Every raw path below returned 200 on 2026-10-27 against branch main, so the layout is real rather than inferred:

```bash
for p in libs/code/examples/skills/langgraph-docs/SKILL.md \
         libs/code/examples/skills/web-research/SKILL.md \
         examples/content-builder-agent/skills/social-media/SKILL.md \
         libs/code/examples/skills/arxiv-search/SKILL.md \
         examples/content-builder-agent/skills/blog-post/SKILL.md \
         libs/code/deepagents_code/built_in_skills/skill-creator/SKILL.md \
         examples/text-to-sql-agent/skills/query-writing/SKILL.md \
         examples/text-to-sql-agent/skills/schema-exploration/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/langchain-ai/deepagents/main/$p"
done
```

To see what the index resolves for a name before writing anything, run the per-skill form and stop at the prompt:

```bash
npx skills add langchain-ai/deepagents --skill schema-exploration
```

After an install, confirm the folder landed in one of the five sources the harness loads from, listed here from lowest to highest precedence: the package `built_in_skills/`, `$DEEPAGENTS_HOME/<agent>/skills/`, `~/.agents/skills/`, `.deepagents/skills/` and `.agents/skills/`. A skill you scaffold yourself can be checked with `quick_validate.py`, which ships in the `skill-creator` directory next to `init_skill.py`:

```bash
scripts/quick_validate.py <path/to/skill-folder>
```

## Security

skills.sh verdicts were not sampled for this fire (2026-10-27), so none of the rows below carry an auditor result and you must check the skills.sh security pages for each listing before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| langgraph-docs | Not checked | Not checked | Not checked |
| web-research | Not checked | Not checked | Not checked |
| social-media | Not checked | Not checked | Not checked |
| arxiv-search | Not checked | Not checked | Not checked |
| blog-post | Not checked | Not checked | Not checked |
| skill-creator | Not checked | Not checked | Not checked |
| query-writing | Not checked | Not checked | Not checked |
| schema-exploration | Not checked | Not checked | Not checked |

The repository states its own position plainly in the README: Deep Agents follows a trust the LLM model, and the agent can do anything its tools allow, so boundaries belong at the tool and sandbox level rather than in the prompt. That is the right frame for these skills too. `query-writing` and `schema-exploration` execute SQL against a live database, and while the skill's own guidelines forbid INSERT, UPDATE, DELETE and DROP, that is an instruction to the model rather than a permission boundary. Grant a read-only connection.

Two operational items deserve a read before you run them. The Deep Agents Code installer is a curl pipe into bash, so fetch and inspect the script before executing it. And `arxiv-search` runs a bundled Python file that reaches arxiv.org and needs the `arxiv` package installed in the agent's environment.

## Limitations

- Snapshot data, verified 2026-10-27: 21,754 combined installs across 20 indexed listings; 30,639 GitHub stars; MIT; branch main. Counts drift over time.
- These are example and built-in skills that ship with the harness, not one published skill package. They live under `libs/code/examples/skills/`, `libs/code/deepagents_code/built_in_skills/` and per-example agent directories under `examples/`, and skills.sh indexes each directory separately, so 20 listings measure people adding a directory rather than adoption of a suite.
- The `swarm` listing (98 installs) has no matching directory in the current tree, so nothing can be verified about what it contains.
- Several skills assume the tool surface of the example agent that ships them: `sql_db_query` and `sql_db_schema` for the SQL pair, `generate_image` for the content pair, `fetch_url` and `task` for research. A Hermes agent without those tools gets instructions it cannot execute as written.
- Two listings share a name with a sibling copy: `blog-post` and `social-media` exist under both `examples/content-builder-agent/skills/` and `examples/deploy-content-writer/skills/`. The install index does not say which copy a given install received, so read the raw path you actually plan to use.
- Install counts measure distribution, not measured quality. No per-skill version or changelog exists, so a skill can change under you when main moves.

## Related

- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [ECC - Agent Harness Performance Optimization](/hermes/skills/catalog/ecc-agent-harness-setup)
- [Agent Architect - Agent System Design Setup](/hermes/skills/catalog/agent-architect-setup)
- [MCP Client - MCP Client Operations Setup](/hermes/skills/catalog/mcp-client-setup)

## Pro Tips

- Read `skill-creator` before any other skill in the repository. The five discovery directories and their precedence order explain why an installed skill sometimes loses to a project copy, which is the single most confusing failure when two agents share a machine.
- Copy the `web-research` plan-file pattern into your own delegation skills. A written plan plus one findings file per subtopic is what makes a multi-agent run reviewable after the fact.
- Check the raw path before installing a duplicated name. `blog-post` and `social-media` exist in two example agents, and the listing name alone does not tell you which copy you get.
- Treat these skills as reasoning templates when your tool names differ. Rewrite `sql_db_query` or `generate_image` to your own tools before shipping a copy into your stack, or the agent will stall looking for a tool it does not have.
- Keep the SQL pair on a read-only connection. The skills are careful about DML in their instructions, but the database user is the thing that actually enforces it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
