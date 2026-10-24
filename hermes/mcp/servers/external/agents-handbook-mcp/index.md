---
title: "Agents Handbook MCP - Tested Playbooks Before the Run"
description: "Fifty-four agent playbooks with trust grades, risk grades and human checkpoints, readable over a keyless MCP server."
category: Productivity
stars: n/a (hosted knowledge surface; playbooks readable as markdown)
added: 2026-10-21
source: "mcpservers.org /all page 3 (agentshandbook-com)"
relevance: ★★
tags: [agent-playbooks, runbooks, human-checkpoints, evidence-grading, failure-modes, field-log, remote-mcp]
---

# Agents Handbook MCP

**The expensive part of an agent run is not the model call. It is the step nobody wrote down: which actions spend money, which ones send a message that cannot be recalled, and which ones delete data. Agents Handbook exists to put those steps in front of an agent before it starts.**

```
Server type: Remote (Streamable HTTP), no sign-in
Endpoint: https://agentshandbook.com/mcp
Auth: none for search and read; a contributor key for credited reports
Live check: unauthenticated POST initialize returned HTTP 200 (serverInfo agentshandbook 0.1.0, protocol 2025-06-18, tools, resources and prompts capabilities, with server instructions)
Tools: 11, counted from tools/list rather than claimed
Corpus: 54 playbooks, ten categories
Vendor: Agents Handbook (agentshandbook.com)
```

## Why This Matters for Operators

An agent that has a tool list but no procedure will invent one, and the invention is where money and messages leak. A written procedure is only trustworthy if it carries three things: the checks between steps, the known failure modes, and some evidence that somebody actually ran it. Most "prompt libraries" carry none of the three.

This one carries all three as data the agent can query. Every playbook states its trust level, from `reported` through `corroborated`, `tested` and `confirmed`, and a risk level of low, medium or high. Every playbook lists human checkpoints, defined by the vendor as the steps that spend money, send messages, submit forms or delete data. Failures live in a separate lessons surface, so an agent can ask what goes wrong with this job before starting it rather than after.

## What It Actually Does

Eleven tools, enumerated live:

- `search_playbooks` finds playbooks for a job described in plain words, filtered by agent slug, category, minimum trust or a result limit of up to 25. It returns slugs, titles, trust, risk, the agents each playbook is written for, and a URL plus a markdown URL.
- `get_playbook` returns one playbook as markdown: summary, human checkpoints, the prompt variant written for the calling agent, the steps with their checks, and attribution unless it is turned off.
- `get_lessons` returns known failure modes and their fixes, filtered by agent, playbook, lesson slug or a plain-words description of the problem.
- `list_tasks` lists the jobs covered, grouped by category, with the agents that have playbooks for each. `get_agent` returns a profile of a specific agent: what it is good at, its limits and how it connects to tools.
- `whats_new` lists recently updated playbooks and the latest community run reports.
- `report_run` records how a run actually went, `worked`, `worked_with_changes` or `failed`, with what changed and an optional lesson. `submit_use_case`, `submit_playbook`, `check_submission` and `register_contributor` are the contribution side, all entering a review queue rather than publishing directly.

A live call with a real query is part of this entry rather than a handshake: `search_playbooks` on "reconcile receipts against bank transactions" with `min_trust: corroborated` returned one playbook, `match-receipts-to-bank-transactions-for-your-accountant`, graded corroborated and high risk, with the four agents it is written for, its page URL and its markdown twin.

## Installation

```bash
claude mcp add --transport http agentshandbook https://agentshandbook.com/mcp
```

Nothing else is required: no key, no account, no OAuth. Every page also has a markdown twin, so a client that cannot use MCP can read the same material by appending `.md` to any URL, and there is a plain search endpoint at `https://agentshandbook.com/api/v1/search?q=`.

## Configuration

```json
{
  "mcpServers": {
    "agentshandbook": {
      "type": "http",
      "url": "https://agentshandbook.com/mcp"
    }
  }
}
```

## Limits Worth Knowing

- Playbook text is third-party reference material, as the server's own instructions say. A playbook is a procedure to check, not an authority, and the trust grade is the vendor's own label rather than an audit.
- Run reports are reviewed before they count, so the field log lags reality by however long review takes. It is not a live success rate.
- The corpus is small and uneven across categories: 54 playbooks over ten categories, weighted to money, life admin, shopping, travel, work and software, with operator-heavy topics thinner than developer topics.
- The site markets itself to individual operators and agent users, and some playbooks reach into personal finance and tax. Those carry high risk grades for a reason, and they are personal-data workflows a business should not run from a shared agent.
- No pricing published. It is free and keyless to read; contribution is credited by key, not paid.

## FAQ

### What is the difference between the trust levels?
`reported` means somebody says they ran it, `corroborated` means a second source or check agrees, `tested` and `confirmed` are stronger still. Only the vendor assigns them, so the useful move is to filter by `min_trust` and read the checkpoints rather than trusting the label alone.

### Does an agent need the whole playbook, or is search enough?
Search returns the slug, title, outcome and grades, which is enough to decide whether the job is covered. Running it needs `get_playbook`, because the checkpoints, the per-agent prompt variant and the steps with checks are what the playbook actually is.

### Why catalogue this when it was held at the midday sweep?
The midday pass read it at title level and held it as an agent-playbook knowledge surface. Read to detail this cycle, it earns an entry on its own mechanics rather than on its topic: eleven tools counted from `tools/list`, a keyless endpoint, numbered human checkpoints as a first-class field, evidence and risk grades on every playbook, a separate lessons surface, and a report-back loop that is reviewed rather than auto-published. That shape is close to the governance contract this docs set publishes, which makes it worth an entry as a comparison point rather than a recommendation.

## See Also

- [Runbook v1 - Governed MCP Workflow Contract](/hermes/mcp/runbook-v1)
