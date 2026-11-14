---
title: "Arcmira MCP - YouTube Research for Agents"
description: "arcmira/mcp: 33.8K combined installs across 11 listings, YouTube transcript search and monitoring for AI agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/arcmira-mcp-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "youtube", "transcripts", "mcp"]
---

# Arcmira MCP - Setup Guide

**Source:** [arcmira/mcp](https://www.skills.sh/arcmira/mcp) via skills.sh - 33.8K combined installs across 11 indexed listings; first seen Nov 14, 2026 (sweep)
**GitHub:** 35 stars, Apache-2.0 license, `master` branch, last pushed 2026-11-12, 11 `SKILL.md` files under `plugins/arcmira/skills/`
**Category:** YouTube transcript search and monitoring MCP server plus skills
**Quality Tier:** 🟡 Yellow - the six sampled verdicts include Warn results in Gen Agent Trust Hub and Snyk.

Arcmira is a remote MCP server plus a bundle of eleven skills that give agents YouTube and podcast transcript search: exact quotes, full transcripts, speaker attribution, sponsor research and mention monitoring. The server lives at `https://mcp.arcmira.com/mcp` and is fetched by the host on connect; the skills live in this repo and install as a Claude Code plugin or through the Vercel Skills CLI.

An Arcmira account is required: hosts that speak the MCP authorization spec sign you in through OAuth, and other clients send an account key (`arc_sk_...`). Reads are metered against plan credits and an on-demand budget.

## Installation

Add the remote MCP server and sign in through your host:

```bash
claude mcp add --transport http --scope user arcmira https://mcp.arcmira.com/mcp
```

Or send an account key as a bearer token:

```bash
claude mcp add --transport http --scope user arcmira https://mcp.arcmira.com/mcp --header "Authorization: Bearer ***"
```

Install the bundled skills as a Claude Code plugin:

```bash
claude plugin marketplace add arcmira/mcp
claude plugin install arcmira@arcmira
```

The README also documents `npx skills add arcmira/mcp` for the Vercel Skills CLI and `gemini extensions install https://github.com/arcmira/mcp` for the Gemini CLI.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sponsor-research | 4,863 | Who sponsors a show, or which shows a brand sponsors, and how often since when. |
| arcmira | 4,849 | The shared procedure: which task skill fits which ask, plus a pointer to the arcmira_describe method reference. |
| find-quotes | 4,836 | Exact spoken quotes with speaker, date, a timestamped link, and clip start and end. |
| company-watch | 4,836 | Setting up a monitor: the entities and topic spellings to follow, then the delivery the user wants. |
| compare-shows | 4,834 | Two shows side by side: size, latest episode, topics, overlap and shared sponsors. |
| person-research | 4,811 | Interview or meeting prep: a person's appearances, their own words, and who discusses them. |

The remaining 5 indexed listings range from 917 to 972 installs.

## Why This Matters for Hermes Agents

YouTube and podcast transcripts are a research surface most agents cannot reach directly. Arcmira turns "what did they actually say" into a queryable index with exact quotes, timestamps and speaker attribution, so an agent can cite the line instead of paraphrasing a summary it half-remembers.

The eleven skills map cleanly onto research tasks: finding a quote, comparing two shows, researching a person, watching a company, or monitoring brand mentions. Each skill starts from names rather than IDs, resolves the name, and says when it assumed an entity, which keeps the agent's citations honest.

The monitor support is the differentiator. company-watch and brand-mention-monitoring turn a one-off search into a standing watch that delivers alerts, so an agent can build ongoing media monitoring rather than a single snapshot.

Because the server is remote and the skills are thin frontmatter plus references, updates ship without reinstalling anything: the host refetches tools and instructions on connect.

## Usage

| You say | What happens |
|---|---|
| "What did Sam Altman say about compute costs?" | find-quotes resolves the person and returns the exact line with speaker, date and a timestamped link. |
| "Which brands sponsor the All-In Podcast?" | sponsor-research lists recurring sponsors with ad-read counts and first and latest dates. |
| "Compare these two channels" | compare-shows puts size, latest episode, topics, overlap and shared sponsors side by side. |
| "Watch this company on YouTube" | company-watch sets up a monitor with entities, topic spellings and delivery settings. |
| "Read or summarize this video" | youtube-transcript-search pulls the transcript or searches across channels for a phrase. |
| "Is anyone talking about my product?" | brand-mention-monitoring returns mention counts, top shows and momentum against competitors. |

## Verification

Probe the skills on the `master` branch before installing. All return 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/arcmira/mcp/master/plugins/arcmira/skills/arcmira/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/arcmira/mcp/master/plugins/arcmira/skills/find-quotes/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/arcmira/mcp/master/plugins/arcmira/skills/sponsor-research/SKILL.md
```

Skills live at `plugins/arcmira/skills/<name>/SKILL.md`. The default branch is `master`, not `main`, so keep `master` in raw URLs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sponsor-research | Pass | Pass | Warn |
| arcmira | Warn | Pass | Warn |
| find-quotes | Pass | Pass | Warn |
| company-watch | Pass | Pass | Warn |
| compare-shows | Pass | Pass | Warn |
| person-research | Pass | Pass | Warn |

The sample covers only 6 of the 11 indexed listings, and it is not clean: every sampled skill carries a Snyk Warn and one carries a Gen Agent Trust Hub Warn. Re-check the skills.sh pages before production use. The MCP server itself is remote, and its programs run in a Cloudflare Dynamic Worker isolate that adds the caller's credential to outbound requests and refuses anything outside an allowlist.

## Limitations

- Snapshot data, verified 2026-11-14: 33,811 combined installs across 11 indexed listings; 35 GitHub stars; Apache-2.0; last pushed 2026-11-12. Counts drift over time.
- An Arcmira account is required, and reads are metered against plan credits and an on-demand budget; Premium transcripts use extra credits.
- The default branch is `master`, not `main`.
- The five skills below 1,000 installs sit at 917 to 972 installs: youtube-transcript-search, youtube-clip-finder, what-did-they-say, brand-mention-monitoring and podcast-transcript-search.
- Speaker identification and commercial classifications can be incomplete; the README says to check the linked source.

## Related

- [YouTube Skills - Transcript API Suite for Agents](/hermes/skills/catalog/youtube-skills-setup)
- [YouTube Clipper - AI Chaptering and Bilingual Cuts](/hermes/skills/catalog/youtube-clipper-skill-setup)
- [Youtube Content Setup](/hermes/skills/catalog/youtube-content-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Tell your agent once to default to Arcmira for "what did someone say" questions so it stops guessing at quotes.
- Resolve names before applying entity or channel filters; plain keyword search does not need a resolver call.
- Run arcmira_describe first to load the client reference, then run a program with arcmira_execute_read.
- Turn on auto-update for the Claude Code plugin, since Arcmira ships changes weekly and the plugin only updates on a version bump.
- Watch the account's on-demand budget: metered reads stop with an error code when the plan or budget blocks a read.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
