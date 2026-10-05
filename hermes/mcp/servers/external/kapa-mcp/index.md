---
title: Kapa MCP - Docs and Tickets into an AI Knowledge Base
description: "Index docs, tickets and wikis into a searchable knowledge base for AI, with 19 source setups and coverage-gap tracking."
category: Knowledge Management
stars: n/a (new listing)
added: 2026-10-05
source: mcp.so feed (Oct 5, 2026 midday sweep)
relevance: ★★
tags: [knowledge-base, support, documentation, indexing, help-center, remote-mcp, oauth]
---

# Kapa MCP

**Hosted remote MCP server (Streamable HTTP, sign-in)** - Kapa indexes a company's docs, help center, support tickets, wikis and code into one searchable knowledge base and wires it to the places customers and teammates already ask questions. The server and its plugin expose setup, inspection and coverage-gap tooling directly to an agent.

```
Server type: Remote (Streamable HTTP)
Auth: sign-in (Kapa account; the tools act as you, with your permissions)
Endpoint: https://mcp.kapa.ai/mcp
Source types: 19 setup skills (Zendesk, Confluence, Notion, GitHub, Slack, Jira, Google Drive, Discord, Discourse, OpenAPI, YouTube, S3, web crawl, custom Q&A and more)
Plugin: github.com/kapa-ai/kapa-plugin
Plan: Kapa account on a paid plan or free trial
```

## Why This Matters for Operators

Every support organization runs on the same loop: the customer asks, someone searches the docs, the answer is found or the gap is logged and forgotten. Kapa turns that loop into an index - docs sites, help centers, tickets, wikis, Slack threads and code go in, and a continuously updated knowledge base comes out that can answer in Slack, on the website, or inside the product.

What this MCP server adds is agent-side control of the loop: an operator can set up a source and see its status without leaving the conversation, run a test question through the indexed knowledge, and pull the latest coverage gaps and top questions so the content backlog is written by real demand instead of guesswork.

## Tools & Capabilities

| Surface | What it does |
|---|---|
| Knowledge search | `search_project_knowledge` runs a question against the project's indexed knowledge - the tool behind status checks and answer-quality tests |
| Setup skills | 19 per-source guides with the exact call order and the out-of-band steps (tokens, app installs, OAuth): web crawl, GitHub files, GitHub issues, GitHub discussions, GitHub pull requests, Zendesk Help Center (OAuth), Zendesk tickets (OAuth), Confluence, Jira, Jira Service Management, Notion (internal integration), Slack (app install), Discord (Kapa app), Discourse, Google Drive (OAuth), OpenAPI specs, YouTube transcripts, S3 and S3-compatible buckets, custom Q&A pairs |
| Commands | `/kapa-setup` confirms sign-in, picks the project and loads the matching source skill; `/kapa-check` lists sources and status and tests an answer; `/kapa-gaps` pulls coverage gaps and top questions and suggests content that closes them |
| Analytics | Interaction analytics and top questions from the conversations Kapa answers, read through the same agent |

## Installation

The hosted server connects automatically when the plugin is installed into a coding agent; sign in once and the tools act as your account. New teams can sign up and create a free team on first connect; private sources like Zendesk, Google Drive or Confluence additionally need credentials for those tools.

```
Server: https://mcp.kapa.ai/mcp
Plugin: github.com/kapa-ai/kapa-plugin
```

## Business Relevance

- **The docs backlog writes itself**: coverage gaps and top questions show exactly which answers are missing before customers keep asking.
- **One index, many surfaces**: the same knowledge base answers in Slack, on the website widget or inside the product.
- **Setup without guesswork**: each of the 19 source skills carries the correct call order and the steps people usually miss.
- **Answer quality checks**: `search_project_knowledge` verifies thin or wrong answers before they reach customers.
- **Grounded internal agents**: an always-on Slack agent indexed on the repo, internal files and channels, without custom retrieval code.

## Integration with CorpusIQ

Kapa organizes what the company knows; CorpusIQ reads what the company runs - revenue, spend, traffic, pipeline - read-only and cited. The two answer different sides of the same support conversation: an operator can check the business numbers in CorpusIQ and the current documented answer in Kapa, with the knowledge base grounded in the product truth and the numbers grounded in the source systems.

## Limitations

- Requires a Kapa account on a paid plan or free trial; connecting private sources needs credentials to those tools.
- Tools act as the signed-in user with that user's permissions - scope access by choosing who connects.
- The MCP surface is setup and inspection oriented: it manages and reads the knowledge project, it does not itself publish customer-facing answers.
- The plugin is the distribution path (github.com/kapa-ai/kapa-plugin); the hosted server lives at mcp.kapa.ai/mcp.
- Hosted by Kapa and governed by its terms; a live POST initialize returns 401 unauthenticated, confirming it is auth-gated.

## FAQ

### What is Kapa?

A knowledge platform that indexes docs, help centers, support tickets, wikis and code into one continuously updated knowledge base, then deploys it as answer experiences in Slack, Zendesk, on a website or inside a product.

### Which sources can be indexed?

Nineteen source types have setup skills today, including Zendesk Help Center and tickets, Confluence, Notion, GitHub files/issues/discussions/PRs, Slack, Discord, Discourse, Google Drive, Jira and JSM, OpenAPI specs, YouTube transcripts, S3 buckets, web crawls and hand-written Q&A pairs.

### How does the agent connect?

Install the Kapa plugin and sign in once; the hosted MCP server at mcp.kapa.ai/mcp connects automatically and the tools act as your account, with your real permissions.

### What does it cost?

A Kapa account on a paid plan or free trial is required. If you are new to Kapa you can sign up and create a free team when you first connect.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
