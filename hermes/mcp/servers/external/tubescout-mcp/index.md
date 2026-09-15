---
title: "TubeScout MCP - Keyless YouTube Research for AI Agents"
description: "Local keyless MCP server that turns YouTube into a research engine: filtered video search, engagement resonance metrics, resilient transcripts (single or batch of 10), channel scans and YouTube autocomplete as search-demand data, plus a context-aware skill pack for idea mining and demand-gap analysis."
category: Content & Research
stars: 0
added: 2026-08-27
source: "mcp.so GitHub issue #3792"
relevance: ★★
tags: [youtube, research, transcripts, market-research, content-analysis, stdio-mcp]
---

# TubeScout MCP

**Local stdio MCP server (TypeScript, MIT) that turns YouTube into a research engine for AI agents - no API key required.** Six tools: filtered video search, video metadata with engagement resonance, resilient transcripts (single or batch of 10), channel scans, and YouTube autocomplete as live search-demand data. Bundles six context-aware research skills for Claude Code, Codex and OpenCode: skeptic's video breakdowns, idea mining, niche validation, channel intel, tutorial-to-playbook, and demand-gap analysis. Install with `npx -y tubescout`, or as a Claude Code plugin via `/plugin marketplace add not0lucky/tubescout`. npm package published Aug 27, 2026 (v0.1.1).

```
Server type: Local (stdio, run via npx)
Auth: None (keyless - talks to YouTube's internal InnerTube API)
Install: npx -y tubescout (npm v0.1.1), or Claude Code plugin not0lucky/tubescout
Tools: 6 (all read-only)
Skills: 6 context-aware research methods (SKILL.md pack)
Repo: github.com/not0lucky/tubescout (MIT, created Aug 27, 2026)
Category: Content & Research
Built by: Anir (agramprojects.com)
```

## Why This Matters for Operators

YouTube is where founders and builders show receipts - revenue dashboards, playbooks, real numbers on camera - but nothing mines it systematically. TubeScout makes YouTube queryable like a database: search with upload-window and duration filters, pull engagement signals (including `likesPer1kViews` resonance), and read transcripts at scale through a three-strategy fallback chain. The differentiating surface is demand data: `get_search_suggestions` exposes YouTube autocomplete as real keyword demand, and the bundled skills turn that into operator work products - niche validation, idea mining, demand-vs-supply gap analysis, and competitive channel intel. For market researchers, product operators and content strategists this is research tooling, not video plumbing.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_videos` | Search with filters: upload window, duration, sort by views or date |
| `get_video` | Full metadata plus engagement (`likesPer1kViews` resonance signal) |
| `get_transcript` | Plain-text transcript via a resilient 3-strategy fallback chain |
| `get_transcripts` | Batch transcripts (up to 10 videos), per-video error tolerant |
| `get_channel_videos` | Channel positioning plus recent uploads with view counts |
| `get_search_suggestions` | YouTube autocomplete = real search demand for keyword research |

**Skill pack (the research methods):** `/yt-breakdown` (extract and stress-test every claim and number in a video), `/yt-idea-mine` (product ideas backed by demand signals and pains builders describe on camera), `/yt-validate` (go/no-go verdict: demand, saturation, competitor numbers), `/yt-channel-intel` (read a channel's strategy: cadence, outliers, what performs), `/yt-playbook` (turn a tutorial into executable steps adapted to your stack), `/yt-gap` (heavily searched topics served by weak or old videos - content plans and product angles). All skills are context-aware: they read the conversation for what you are building and tailor verdicts accordingly.

## Installation

```bash
# Claude Code
claude mcp add --scope user tubescout -- npx -y tubescout

# Codex
codex mcp add tubescout -- npx -y tubescout
```

OpenCode: add to `~/.config/opencode/opencode.json` under `"mcp"`: `"tubescout": { "type": "local", "command": ["npx", "-y", "tubescout"], "enabled": true }`.

The skill pack installs separately: clone the repo and run `./scripts/install-skills.sh` (installs into `~/.claude/skills`, `~/.codex/skills`, `~/.config/opencode/skills`), or install the all-in-one Claude Code plugin.

## Configuration

- **No key, no quota.** The server uses youtubei.js to talk to YouTube's internal InnerTube API, the same endpoint the site itself uses.
- **Transcript fallback chain:** ANDROID-client timedtext track, then the InnerTube transcript endpoint (retried with backoff when it 400s), then local `yt-dlp` if installed. Each response reports which source served it.
- **Run it locally.** YouTube aggressively rate-limits datacenter IPs - this is a local stdio server by design, not a hosted service.
- `npx` always pulls the latest version, so YouTube internals changes are handled by updating.

## Business Relevance

- **Market researchers and product operators** mine niches for validated product ideas with demand signals plus pains real builders describe on camera.
- **Content and SEO strategists** find demand-vs-supply gaps: heavily searched topics served by weak, old or misfit videos.
- **Competitive analysts** read a channel's strategy from its own numbers: cadence, outliers, what performs versus what gets published.

## Integration with CorpusIQ

Complementary to CorpusIQ's business-data connectors: an agent can pull a company's own revenue, bookings and customer context from CorpusIQ, then use TubeScout to mine YouTube for the market signals around it - competitor playbooks, demand gaps and niche validation. CorpusIQ answers what is happening inside the business; TubeScout answers what the market is saying on camera.

## Limitations

- Local-only by design: YouTube rate-limits datacenter IPs, so there is no hosted deployment.
- Videos with captions disabled cannot be transcribed (the error says so explicitly).
- Caption scraping sits in YouTube ToS gray area - fine for local research tooling, not for building a hosted paid product on it.
- Brand new project (npm v0.1.1, repo created Aug 27, 2026, 0 stars) - the fallback chain and rate-limit behavior have not aged in production.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [tube-bridge MCP - Self-Hosted YouTube Research and Transcript Corpora](/docs/hermes/mcp/servers/external/tube-bridge-mcp)
- [BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/docs/hermes/mcp/servers/external/bulktranscripts-mcp)
- [Viral Outliers MCP - Overperforming Social Post Database](/docs/hermes/mcp/servers/external/viral-outliers-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/servers)
