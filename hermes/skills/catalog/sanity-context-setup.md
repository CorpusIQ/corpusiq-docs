---
title: "Sanity Context Skills - Structured Content Setup"
description: "Official Sanity Context skills: 3.5K combined installs across 4 listings for agent context setup, prompt shaping and GROQ queries over CMS content"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sanity-context-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "sanity", "cms", "mcp server", "content retrieval"]
---

# Sanity Context Skills - Setup Guide

**Source:** [sanity-io/context](https://www.skills.sh/sanity-io/context) via skills.sh - 3.5K combined installs across 4 indexed listings (3,479 exact); first seen 2026-02-04 (Nov 10, 2026 sweep)
**GitHub:** 7 stars, no LICENSE file, `main` branch, last pushed 2026-11-10, created 2026-02-02, 293 blobs with 3 `SKILL.md` files at `skills/create-agent-with-sanity-context/`, `skills/shape-your-agent/` and `skills/dial-your-context/`
**Category:** Structured content: agent context construction, prompt shaping and content retrieval over Sanity
**Quality Tier:** 🟠 Early and unlicensed - all three sampled skills pass every scanner and the repository was pushed on the sweep date, but it ships no LICENSE file and carries 7 stars.

Sanity Context is a hosted MCP endpoint that connects an agent to the Sanity Content Lake, where content is stored as queryable documents rather than rendered pages. The repository is Sanity's own, and the three skills in it are setup guides for that endpoint rather than a general CMS toolkit: one builds the agent, one writes the endpoint's Instructions field, one writes the agent's system prompt.

The design argument in the README is worth the read on its own. Instead of vectorizing content into embeddings and hoping similarity search lands, the agent queries the actual data model: filter by fields, traverse references between documents, and fold semantic ranking into a GROQ query. Embeddings for exploration, structured queries for precision. A query that filters `category == "shoes"` and then scores by `text::semanticSimilarity()` is the shape the skills teach.

Sanity also runs a second, older MCP endpoint called the Sanity MCP Server, and the README draws the line clearly: that one gives coding assistants full access to a workspace, this one is read-only and scoped for production agents that serve end users. Installing the wrong one is the most common way to get an agent that can rewrite your content.

## Installation

The README's skills route installs every skill in one command:

```bash
npx skills add sanity-io/context --all
```

Then prompt the agent to use the entry-point skill:

```
Use the create-agent-with-sanity-context skill to help me build an agent.
```

The skill walks through creating the MCP endpoint, connecting the agent, and configuring it for a stack (Next.js, SvelteKit, Express, Python and others). `dial-your-context` and `shape-your-agent` are the follow-ups, run when the agent is connected but answering badly.

The skills assume a context that exists. Four prerequisites come first, and every one of them fails in a way that looks like a bug rather than a missing step:

- Context enabled for the organization, by an organization admin on the org's Labs page in Manage.
- For GROQ mode, a Sanity project with content and a schema deployed from Studio v5.1.0 or later (`npx sanity schema deploy`). For Knowledge Base mode, a built Knowledge Base.
- An organization API token with Context permissions. Viewer for a read-only agent, Editor if it also records Insights. Project tokens do not work.
- An LLM API key for the agent itself.

The endpoint can also be created without the skills, from the Context app in the dashboard or from the CLI, which prints the MCP URL:

```bash
npx sanity@latest context mcp create <name> --title "<title>" --organization <organizationId> --project <projectId> --dataset <dataset>
```

That URL has the shape `https://api.sanity.io/v2026-11-03/context/organizations/:organizationId/mcp/:endpointName`. Any MCP-compatible framework can connect to it with an `Authorization: Bearer` header carrying the organization token; the README shows the Vercel AI SDK version and tells you to keep the token server-side. The Studio plugin that older guides describe was removed in 3.0.0, and the README links a migration guide for anyone still on it.

## What It Provides

All 3 indexed listings at or above the 500-install threshold appear below; the fourth sits under the table:

| Skill | Installs | Use For |
|---|---|---|
| create-agent-with-sanity-context | 1,218 | End-to-end build of an agent over Sanity content: creates the Context MCP endpoint in GROQ or Knowledge Base mode, connects the agent, and configures it for the chosen stack. |
| shape-your-agent | 1,122 | Interactive session that writes the agent's system prompt: personality, tone and voice, boundaries and guardrails, refusal behaviour and communication rules. |
| dial-your-context | 1,119 | Interactive session that writes the endpoint's Instructions field: content filters, schema relationship guidance and which content the agent may reach, aimed at agents giving wrong answers from Sanity queries. |

The remaining 1 indexed listing ranges from 20 to 20 installs: optimize-agent-prompt (20), an index-only name with no counterpart in the current `skills/` tree.

The three in-tree skills divide the work along a line that is easy to blur. `create-agent-with-sanity-context` owns the plumbing and the endpoint configuration. `dial-your-context` owns dataset knowledge, the field in the Context app that tells the agent how your schema hangs together. `shape-your-agent` owns behaviour, the system prompt that decides tone and refusals. The create skill's own text says Sanity Context gives agents the schema and teaches them GROQ but cannot know the domain, which is exactly the gap the other two fill.

## Why This Matters for Hermes Agents

Retrieval quality is the difference between an agent that answers a product question with a price and one that answers with a paragraph of marketing copy that mentions a price. Semantic similarity is good at the second and bad at the first, because "under 150 dollars" and "affordable" sit close in embedding space while only one of them is true.

A schema-aware endpoint changes what the agent can do with one call. It filters on real fields, follows references (a product's brand, a brand's products), and ranks the filtered set semantically. That is a different class of answer, and it comes from the data model rather than from a larger context window.

The three skills matter because the endpoint alone is not enough. An agent with schema access and no instructions produces confident wrong queries. The Instructions field and the system prompt are where an operator states the domain rules, and having a skill that interviews you for them is more useful than a blank text box.

There is also a clean separation of concerns worth copying into other stacks: this endpoint is read-only and scoped, so it can serve end users, while the workspace-level Sanity MCP Server stays in the hands of developers. An agent that can only read cannot publish.

## Usage

| You say | What happens |
|---|---|
| "Build a support bot over our Sanity content" | The create skill sets up the Context MCP endpoint against the dataset, connects the agent, and writes the first integration for your framework |
| "It keeps answering with the wrong product" | dial-your-context interviews you about the schema and writes Instructions that name the fields to filter on and the references to follow |
| "Make it stop promising refunds" | shape-your-agent writes boundaries and refusal behaviour into the system prompt |
| "Search should respect category and size filters" | The endpoint's GROQ tools take the filter, and the skill documents which fields are safe to filter on |
| "Find trail running shoes under 150 dollars" | A structured filter narrows the set, then semantic scoring ranks it, in one GROQ query rather than two retrieval passes |
| "We want search over PDFs and website pages too" | A Knowledge Base endpoint is built ahead of time from datasets, websites and files, and serves search and read tools instead of GROQ tools |
| "Show me what people asked last week" | Agent Insights records conversations through the AI SDK integration and classifies them by success, sentiment and content gaps |

## Verification

Each in-tree skill resolves to a raw `SKILL.md` one directory below `skills/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/sanity-io/context/main/skills/create-agent-with-sanity-context/SKILL.md | head -3
```

It should print the frontmatter delimiter, then `name: create-agent-with-sanity-context`, then a description beginning `Build AI agents with structured access to Sanity content via Sanity Context`. The same layout holds for `skills/dial-your-context/SKILL.md` and `skills/shape-your-agent/SKILL.md`.

Once installed, confirm the directory is there:

```bash
test -f ~/.claude/skills/shape-your-agent/SKILL.md && echo ok
```

The endpoint itself is verifiable without the skills. The README's troubleshooting section gives the check, and a tool list in the response means the token and URL are both good:

```bash
curl -X POST https://api.sanity.io/v2026-11-03/context/organizations/:organizationId/mcp/:endpointName \
  -H "Authorization: Bearer $SANITY_ORG_TOKEN" \
  -H "Accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "tools/list", "id": 1}'
```

A 401 means the token is missing, malformed, or from a different organization. A 403 with JSON-RPC code `-32007` and `contextGrantRequired` means the token is a project token rather than an organization token with Context permissions.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| create-agent-with-sanity-context | Pass | Pass | Pass |
| shape-your-agent | Pass | Pass | Pass |
| dial-your-context | Pass | Pass | Pass |

All three sampled skills pass all three scanners. That is the strongest signal in this guide and the reason the tier is not lower, but the scanner verdicts cover the skill text, not the deployment you build with it.

Three properties need your own review. The token is an organization API token, so one credential reaches every project in the organization; the README's instruction to keep it server-side is not optional. Choosing Editor scope to enable Insights widens that credential from read to write, and an agent that records conversations writes a transcript of them against your project. And Knowledge Base mode is marked beta in the README, which means the tool surface can change under a working integration.

The absence of a LICENSE file is the other half of the picture. The code is public and the skills install, but no reuse terms are stated anywhere in the repository, so treat redistribution and commercial embedding as unanswered rather than permitted.

## Limitations

- Snapshot data, verified 2026-11-10: 3,479 combined installs across 4 indexed listings; 7 GitHub stars; no LICENSE file; last pushed 2026-11-10. Counts drift over time.
- The repository carries no license. GitHub reports none, the tree has no LICENSE file, and no README section addresses terms, so the legal position for vendoring these skills is unstated.
- The install index outruns the tree: optimize-agent-prompt has an install count but no matching directory under `skills/`, so four listings resolve to three skills.
- The skills are setup guides for a hosted service, not a library. Every path through them ends at a Sanity organization with Context enabled, an organization token, and a deployed schema from Studio v5.1.0 or later.
- GROQ mode needs a deployed schema per dataset, and an endpoint whose project and dataset have no deployed Studio application returns an error rather than partial results.
- Knowledge Base mode is beta. Search and read tools on a Knowledge Base endpoint are a different surface from the GROQ tools, and the skills are written around the GROQ path.
- 7 stars on a repository published in February 2026 is thin public signal: few outside readers, few issues, and no community track record for the skill text.

## Related

- [Sanity Agent Toolkit - Headless CMS Setup](/hermes/skills/catalog/sanity-agent-toolkit-setup)
- [Payload CMS Skills - Schema and Migration Setup](/hermes/skills/catalog/payloadcms-skills-setup)
- [MCP Use Setup - Fullstack MCP Framework for Hermes](/hermes/skills/catalog/mcp-use-setup)

## Pro Tips

- Confirm which endpoint you are installing. The Sanity MCP Server gives a workspace full access; Context is read-only and scoped. Getting this backwards is a content-integrity incident, not a setup mistake.
- Deploy the schema before anything else. `npx sanity schema deploy` from Studio v5.1.0 or later is the prerequisite that produces the most confusing errors when missed.
- Run `dial-your-context` after the first bad answer, not before. The Instructions field works best when it describes failures you actually saw.
- Keep a Viewer token for the agent and a separate Editor token for Insights collection, so the serving path cannot write even if a prompt tries.
- Check for a GROQ filter on the endpoint when results come back empty. A filter that matches no published documents behaves exactly like a broken connection.
- Re-read `shape-your-agent` output before shipping it. Refusal behaviour written by a model tends to be either too broad or too polite, and the system prompt is the last place to catch that.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
