---
title: "CorpusIQ Agent Pack - Two Role Agents for AI Coding Tools"
description: "Two drop-in role agent files for Claude Code, Cursor, Codex, OpenCode and other AI coding tools."

category: Agents
tags:
  - corpusiq-agent-pack
  - role-agents
  - connector-grounded
  - verified-figures
last_updated: 2026-11-14
canonical: "https://www.corpusiq.io/docs/hermes/agent-pack/"
robots: "index,follow"
---

# CorpusIQ Agent Pack

Two role agents, one file each. Copy a file into the tool you already use, connect CorpusIQ MCP, and the agent answers business questions from your own systems rather than from model memory.

The pack exists because of one failure mode. A general assistant asked about revenue will produce a number. It may be last quarter's, it may be from a blog post, and it will be stated with the same confidence as a figure pulled from the ledger. A role agent that expects a connector behaves differently: it reads the number, names the system it came from, and says plainly when a connector is down instead of filling the gap.

## The two agents

| Agent | Answers | Reads from |
|---|---|---|
| [Business Analyst](business-analyst.md) | Margin, cash, receivables, spending and board-pack questions | QuickBooks, Stripe, Shopify, GA4, Search Console, Google Ads, Meta Ads |
| [Growth Analyst](growth-analyst.md) | Where the acquisition funnel leaks, and what each step costs | GA4, Search Console, Google Ads, Meta Ads, LinkedIn Ads, PostHog, Klaviyo, Mailchimp, Stripe |

Each file is self-contained: identity, mission, working rules, output shape and the connector set it depends on.

## What makes them different from a prompt

- **A number or a stated gap.** Every figure carries the system it came from. When a connector is unreachable the agent reports that and stops, rather than estimating.
- **Definitions travel with the answer.** Which period is closed, which system counts a customer, which metric a team argues about. The agent holds that context across the conversation.
- **Read-only by construction.** The retrieval tools behind both agents are read-only. Neither agent can post a journal entry, edit a record or change a campaign.
- **Tool-agnostic.** The files are plain markdown, so they work in Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Qwen and Osaurus without a rewrite.

## Install

1. Connect at least one business system in CorpusIQ, so the agent has something to read.
2. Connect CorpusIQ MCP to the tool you are using. The endpoint and the client-specific setup steps are in the connector documentation.
3. Copy the agent file into the tool's agent or instruction location, for example a project `AGENTS.md`, a Claude Code subagent file, or a Cursor rules directory.
4. Ask a question that has an answer in a connected system. If the agent answers without naming a source, the file was not loaded.

## Choose the right starting point

The [Agent Library](https://www.corpusiq.io/docs/hermes/agents/) carries nine departmental agents built for the same purpose: sales, marketing, DevOps, support, finance, executive, research, legal and HR. This pack is narrower on purpose. Two agents, both analytical, both built around a figure that has to survive scrutiny.

If the question is "what happened and why" in the numbers, start here. If the question is "who does this job", start with the Agent Library.

## FAQ: Common Questions

<details>
<summary><strong>Do these agents need CorpusIQ MCP?</strong></summary>

Yes. The connector set is the point. Without a connection the agent will say it cannot see the figure, which is the behaviour it is designed for.
</details>

<details>
<summary><strong>Can I edit the files?</strong></summary>

Yes. They are plain markdown. Teams typically narrow the connector list and add their own definitions of a customer, a churned account or a qualified lead.
</details>

<details>
<summary><strong>Can an agent change anything in a connected system?</strong></summary>

No. The retrieval tools documented across this pack are read-only.
</details>

<details>
<summary><strong>Which AI tools can load them?</strong></summary>

Any tool that reads a markdown instruction file or supports subagents. The pack is tested with Claude Code, Cursor, Codex, OpenCode, Gemini CLI, Qwen and Osaurus.
</details>

---

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
