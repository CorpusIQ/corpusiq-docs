---
title: "AskHound MCP - Find People Asking for What You Sell"
description: "Demand discovery over MCP: search Hacker News, Stack Exchange, Bluesky and GitHub for people describing the problem you solve, score intent, track packs over time and mark each conversation replied, skipped or seen."
category: "Marketing / Demand Discovery"
stars: n/a (new listing)
added: 2026-10-18
source: "mcpservers.org /all page 1 (October 18, 2026 night sweep)"
relevance: ★★★
tags: [demand-discovery, social-listening, hacker-news, stack-exchange, bluesky, github, intent, prospecting, local-mcp, remote-mcp]
last_updated: "2026-10-24"
---

# AskHound MCP

**People describe their problems in public before they search for a vendor. AskHound searches the places they do it, Hacker News, Stack Exchange, Bluesky and GitHub, for the phrase that matches what you sell, filters by recency and intent, keeps a pack of saved queries that returns only new results, and records whether a human answered, skipped or already saw each one. It ships a local stdio server, a remote stateless endpoint and a CLI over the same data.**

```
Server type: Local stdio MCP, remote Streamable HTTP MCP, and a CLI
Remote endpoint: https://askhound.haullabs.dev/api/mcp (stateless; optional Bearer license)
Local: npx -y https://askhound.haullabs.dev/askhound-0.1.5.tgz mcp
CLI: askhound search | queries | pack save/run | mark | login | sync | mcp
Sources (local): Hacker News (hn.algolia.com), Stack Exchange (api.stackexchange.com 2.3), Bluesky (api.bsky.app searchPosts), GitHub (api.github.com search/issues)
Sources (remote): Stack Exchange and Bluesky only; use the local server for Hacker News and GitHub
Environment: GITHUB_TOKEN (10 to 30 requests a minute on GitHub search), STACKEXCHANGE_KEY, ASKHOUND_HOME (default ~/.askhound)
Telemetry: at most one anonymous ping a day; opt out with ASKHOUND_TELEMETRY=0 or DO_NOT_TRACK=1
Source: askhound.mjs, MIT
```

## Why This Matters for Operators

Outbound starts with a list somebody bought. Demand discovery starts with a sentence somebody typed: "any alternative to X that does Y", "how do you handle Z without a spreadsheet". The second is a warmer conversation and a much smaller pile.

The hard part was never finding one thread. It was running the same set of queries every day without re-reading yesterday's results, and knowing which conversations a human already handled. AskHound is built around those two chores: packs that return only new matches, and a reply state that survives between runs. That makes it usable as a standing job rather than a one-off search.

## Tools

**Local MCP (all four sources, queried from your machine)**

| Tool | What it does |
|---|---|
| `find_conversations` | Search for a phrase across the enabled sources, with recency window, context words and negative terms |
| `run_pack` | Run a saved pack and return new results since the last run |
| `mark_conversation` | Record a conversation as replied, skipped or seen |
| `list_packs` | List the saved packs and their queries |
| `reply_policy` | Read the disclosure-first reply policy the tool applies |

**Remote MCP (stateless, Stack Exchange and Bluesky only)**

`find_conversations`, `build_intent_queries`, `run_intent_pack`, `reply_policy`.

**CLI**

```bash
askhound search "invoice reconciliation" --sources hn,se,bsky --days 30 --min-intent 2
askhound queries --competitor Otter.ai --competitor Fireflies --category "transcript export"
askhound pack save weekly-ap --competitor A --category "invoice matching"
askhound pack run weekly-ap --days 14 --md report.md
askhound mark <url> replied
```

## Setup in Hermes

```bash
# remote, no install
hermes mcp add askhound --url https://askhound.haullabs.dev/api/mcp

# local, all four sources
hermes mcp add askhound-local --command npx --args -y https://askhound.haullabs.dev/askhound-0.1.5.tgz mcp
```

The remote endpoint answers an unauthenticated `initialize` with server name `askhound` version 0.1.5 and a tools capability block, so it can be added and tested before any license exists. A paid license adds cloud reply-state sync and more packs; the browser tool's free allowance is three searches a day per IP, and the CLI and local MCP carry their own rate limits from the upstream sources rather than a plan quota.

## Integration with CorpusIQ

Demand discovery produces the raw material; CorpusIQ produces the evidence. An assistant can find a thread where a business owner describes stitching numbers together from three dashboards, check whether the claim in the thread matches what the traffic and revenue data actually show, and answer with a specific, cited reply instead of a generic pitch. The pack keeps the thread; the connector keeps the numbers behind the answer.

## Limits

- **Public sources only:** four communities, queried through their public APIs. No LinkedIn, no Reddit, no X
- **Remote coverage is narrower:** the hosted endpoint serves Stack Exchange and Bluesky; Hacker News and GitHub need the local server
- **Rate limits belong to the upstreams:** GitHub search runs on your token (10 to 30 a minute), Stack Exchange on its own quota, so a broad sweep should be paced
- **Watches are paid:** email digests are available on paid plans (beta), and Slack, Discord and webhook channels on higher tiers
- **Reply state is local unless licensed:** cloud sync of what was replied and skipped requires a license key
- **It finds conversations, it does not send replies:** posting stays with the human or another tool, and the bundled policy is disclosure-first

## FAQ

### Do I need a key to start?

No. The local CLI and local MCP run free against the public APIs, and the remote endpoint accepts unauthenticated calls. Optional environment tokens raise GitHub and Stack Exchange limits; a license key adds cloud sync and watches.

### Can it see private communities?

No. It queries public search APIs only: Hacker News via Algolia, Stack Exchange, the Bluesky public AppView, and GitHub issues and pull requests.

### What is the reply policy for?

It encodes the disclosure rule the tool assumes: say who you are and that you build the thing, answer the question first, and never drop a link where it does not answer anything. Reading it before a sweep keeps an automated find from turning into an automated spam run.

## Verification

- `POST initialize` to `https://askhound.haullabs.dev/api/mcp` returns HTTP 200 with `serverInfo` name `askhound` version `0.1.5`, a `tools` capability block and server instructions
- The publisher documents the CLI, the local and remote tool lists, the REST surface (license, watches, quota, state, report), the four sources and the telemetry opt-out
- The CLI tarball and a pinned version URL are published at askhound.haullabs.dev
