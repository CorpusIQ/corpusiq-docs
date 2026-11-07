---
title: "Tiangong Skills - Data Fetch and Report Utilities"
description: "tiangong-ai/agent-skills on skills.sh: 9.1K combined installs across 62 listings; RSS, email, paper and environmental data utilities for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tiangong-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "research utilities", "data fetch", "rss"]
---

# Tiangong Skills - Setup Guide

**Source:** [tiangong-ai/agent-skills](https://www.skills.sh/tiangong-ai/agent-skills) via skills.sh - 9.1K combined installs across 62 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 11 stars, MIT, last pushed 2026-10-20, 62 SKILL.md directories, one per skill, at the repository root
**Category:** Research utilities for agents: RSS and paper fetching, image conversion, environmental data and recurring summary jobs
**Quality Tier:** 🟡 Review - a 62-skill catalogue with clean Trust Hub and Socket verdicts across the sample, small star count, and one sampled skill failing Snyk.

This is a catalogue rather than a single skill: 62 directories, each with its own `SKILL.md`, installed together or picked one at a time. The spread is wide. Four email skills cover SMTP send and IMAP fetch, append and full sync. A cluster of RSS and full-text skills feeds a SQLite store and produces time-windowed digests. Twenty-one "atomic data" skills wrap the Tiangong CLI's data runtime for AirNow, EPA EIS records, Federal Register, NASA FIRMS fire detections, OpenAQ, Regulations.gov, USBR, USGS water, three Open-Meteo sources, GDELT and Bluesky. The rest are knowledge-base search and ingest wrappers, an academic paper downloader, an image converter, a duplicate-image remover and a thesis typesetting workflow.

The design rule shared by the data skills is worth understanding before you install anything. Each one is a thin semantic layer: it supplies intent routing and result-use boundaries, while the CLI owns source discovery, input and output schemas, API-key injection, pagination, limits, validation and receipts. Each directory carries `references/tiangong-data-requirement.json`, which declares the capability and operation contract majors it needs, and the caller or workspace runtime lock picks the actual CLI build. There is no second provider connector runtime and no per-skill package lock.

The repository moved from a personal account to the tiangong-ai organisation in September 2026 with its history intact. The CLI package `@tiangong-ai/cli` and the command `tiangong-ai` did not change.

## Installation

The README manages skills with the `skills` CLI from vercel-labs/skills. If you want it globally, its own install line is:

```bash
npm i skills -g
```

List what the repository offers without installing anything:

```bash
npx skills add https://github.com/tiangong-ai/agent-skills --list
```

Install everything, project scope by default:

```bash
npx skills add https://github.com/tiangong-ai/agent-skills
```

Install selected skills by name, which is the sane default for a 62-skill repository:

```bash
npx skills add https://github.com/tiangong-ai/agent-skills --skill tiangong-auto-research --skill tiangong-kb-sci-search
```

Target specific agents, or install user-wide rather than per project:

```bash
npx skills add https://github.com/tiangong-ai/agent-skills -a codex -a claude-code
npx skills add https://github.com/tiangong-ai/agent-skills -g
```

The interactive install asks you to choose symlink (recommended) or copy. Scope destinations differ by agent: Codex project scope is `./.agents/skills` and global scope is `$HOME/.agents/skills`, while Claude Code project scope is `./.claude/skills` and global scope is `$CLAUDE_CONFIG_DIR/skills` when set, otherwise `$HOME/.claude/skills`. The README's own advice is to read the path the pinned CLI reports rather than deriving it by analogy.

`npx skills add` installs or links skill files. It does not provision language runtimes or run post-install hooks, so a skill with a locked runtime bootstrap expects you to run those steps from its own instructions.

## What It Provides

Five listings clear the 100-install threshold, and they account for nearly all of the traffic:

| Skill | Installs | Use For |
|---|---|---|
| email-smtp-send | 6,734 | Outbound email over SMTP with local attachments and optional IMAP append to the Sent mailbox |
| email-imap-fetch | 369 | Reading a mailbox over IMAP with env-configured credentials |
| ai-tech-rss-fetch | 235 | Subscribing to AI and tech RSS or OPML sources and persisting normalized metadata to SQLite with dedupe |
| dify-knowledge-base-search | 111 | Searching a Dify knowledge base from an agent task |
| document-granular-decompose | 102 | Breaking a document into granular pieces for downstream indexing or retrieval |

The remaining 57 indexed listings range from 1 to 91 installs.

The tail is where the environmental and research breadth sits, and it is worth reading rather than skipping: `ai-tech-summary` builds time-windowed digests from the SQLite store, `sustainability-rss-fetch` and its summary and full-text companions do the same for sustainability sources, `gdelt-doc-search`, `gdelt-events-fetch`, `gdelt-gkg-fetch` and `gdelt-mentions-fetch` cover the GDELT tables, and `open-meteo-historical-fetch`, `open-meteo-flood-fetch`, `nasa-firms-fire-fetch`, `usgs-water-iv-fetch` and `airnow-hourly-obs-fetch` cover physical-world data. Low install counts here mean small audience, not weak content: these are narrow professional sources.

The `tiangong-auto-research` orchestrator is the other piece worth knowing about. It plans research work, acquires sources, runs independent review and keeps a portable audit, with a guarded setup layer that binds source commits, tree hashes, destinations, licence choices and credential bindings. Its `workbuddy` companion is a thin adapter for a WorkBuddy or CodeBuddy producer. Both sit at 4 installs and both expect a locked CLI runtime before they will do anything useful.

## Why This Matters for Hermes Agents

The email skills are the practical entry point for most Hermes setups. `email-smtp-send` validates its configuration before delivery, returns machine-readable JSON status and error output, and can append the sent message to the IMAP Sent folder so the message shows up in the user's mail client rather than only in your logs. `email-imap-fetch`, `email-imap-append` and `email-imap-full-fetch` cover the read and sync side. That is a complete, credential-driven mail loop that does not require a vendor SDK.

The data skills encode a discipline that agent tooling usually lacks: describe before run. The documented flow is to read the requirement JSON, run `data describe` against the resolved CLI, confirm the capability ID and contract majors match, copy the current versions from that response into the run request, then run a static `data doctor` that fails closed when the logical credential is missing. Facts remembered from an older skill revision are explicitly not a substitute. If you have ever shipped an agent that confidently called a stale endpoint, this is the pattern that prevents it.

The RSS and summary cluster is a worked example of persistence done properly. Metadata goes into SQLite with layered identity keys and content fingerprints, so repeated runs dedupe instead of duplicating, and full-text fetch is a separate opt-in skill rather than a hidden cost inside the fetch step. Summaries are produced by the agent over selected records, not by a fixed template, which keeps the judgement where it belongs.

The catalogue is also honest about failure. Three capabilities, `gdelt.doc-search`, `usbr.project-records` and `usbr.rise`, are documented as discoverable but suspended after their production live gates failed, and Auto Research will not offer them for execution. Thin skills and stable requirements stay in place for diagnosis and later requalification. A repository that publishes its own suspensions is easier to trust than one that only publishes its features.

## Usage

| You say | What happens |
|---|---|
| "Send this report to the client with the PDF attached" | `email-smtp-send` checks its SMTP config, sends the MIME message with the attachment and can append a copy to the IMAP Sent folder |
| "What came into the shared inbox since Friday" | An IMAP fetch skill pulls the window and returns message metadata for the agent to work over |
| "Subscribe to these AI feeds and tell me what is new this week" | `ai-tech-rss-fetch` syncs and dedupes into SQLite, then `ai-tech-summary` builds the digest from selected records |
| "Pull air quality readings for this sensor and window" | A data skill describes the capability, checks the credential, then fetches raw or hourly measurements with a receipt |
| "Search GDELT for coverage of this phrase" | A GDELT skill routes to the matching table operation, subject to the CLI describing it as available |
| "Convert these screenshots to JPG and drop duplicates" | `convert-image-to-jpg` and `remove-similar-image` run as separate steps in one task |
| "Download this open-access paper" | `academic-paper-download` fetches from legal OA sources with provenance and a hash manifest beside the file |

## Verification

Read one skill before installing the set. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/tiangong-ai/agent-skills/main/ai-tech-rss-fetch/SKILL.md | head -30
```

It should open with frontmatter naming `ai-tech-rss-fetch` and a description that scopes it to feed subscription, incremental sync with deduplication, and metadata persistence without full-text extraction.

After install, confirm the count and the layout. The repository has 64 top-level directories, of which 62 hold a `SKILL.md`; the other two are `_docs` and `scripts`:

```bash
ls ~/.claude/skills | grep -c .
find ~/.claude/skills/ai-tech-rss-fetch -maxdepth 1 -type f -name SKILL.md
npx skills list
```

`npx skills list` is the CLI's own view of what is installed and where, which is more reliable than guessing a destination path. `npx skills check` reports available updates and `npx skills update` applies them.

For the knowledge-base ingest skill, the README pins an exact CLI release, `@tiangong-ai/cli@0.0.48`, and gives a credential-free smoke test that touches no backend: run the version command from that pinned package, then the knowledge-base help surface. The version must print `0.0.48`, and the help must list the bulk scan, metadata dry-run, collection list and schema, ingest, and status surfaces. Anything else means the resolved CLI is not the reviewed one. Read the exact invocation from `README.md` rather than reconstructing it, because the version pin is the whole point.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| email-smtp-send | Pass | Pass | Pass |
| github-contribution-period-analysis | Pass | Pass | Warn |
| regulationsgov-comment-detail-fetch | Pass | Pass | Warn |
| tiangong-kb-course-search | Pass | Pass | Fail |
| apply-environmental-thinking | Pass | Pass | Pass |

Five sampled skills out of 62, so the table is a sample and not a verdict on the catalogue. The failing row deserves attention: `tiangong-kb-course-search` passed Trust Hub and Socket and failed Snyk, and its install count is 12, so it is not a skill anyone is relying on at scale yet.

The credential model is the real security surface. These skills read API keys and mailbox passwords from the environment, and the OpenAQ documentation is explicit that the key must never appear in argv, request JSON, a skill-local file, logs or output. Hold every skill in this repository to that standard, and prefer an env file with owner-only permissions over anything checked into a workspace.

The email skills touch the most sensitive path in the set. A mail-sending skill with SMTP credentials can send as you, so scope the credential to a mailbox you are willing to have automated, and keep a human in the loop on outbound mail until you have watched it behave.

## Limitations

- Snapshot data, verified 2026-11-06: 9,130 combined installs across 62 indexed listings; 11 GitHub stars; MIT; last pushed 2026-10-20. Counts drift over time.
- Install counts are heavily concentrated. One skill holds 6,734 of the 9,130 installs and the bottom 30 listings are all under 30, so catalogue traffic is not evidence that any individual tail skill works.
- The data skills depend on a resolved Tiangong CLI build and a matching contract major. A version mismatch is a stop condition, not something the skill papers over, and `npx skills add` will not install the runtime for you.
- Three capabilities are suspended after failed live gates: `gdelt.doc-search`, `usbr.project-records` and `usbr.rise`. They remain discoverable for diagnosis, which can read as availability if you skim the directory list.
- Credentials are per skill and live in the environment. Nothing in the install provisions them, and the repository deliberately delegates that to each skill's `references/env.md`.
- Only five of the 62 skills have published scanner verdicts, and one of those fails Snyk, so most of the catalogue is unscanned as far as skills.sh is concerned.

## Related

- [Tavily Research - AI-Powered Deep Research with Citations](/hermes/skills/catalog/tavily-research-setup)
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup)
- [Astronomer Agents - Airflow Data Engineering Setup](/hermes/skills/catalog/astronomer-agents-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by name, not by repository. Pulling all 62 skills into every session costs context you will never spend, and the five skills above threshold are the ones with a track record.
- Read `references/tiangong-data-requirement.json` before the first run of any data skill. It tells you which contract major you need, which is the difference between a working call and a schema error three steps in.
- Pin the CLI per workspace rather than globally. The requirement files are written for a resolved build, and a global upgrade can move a capability out from under a working pipeline.
- Use the JSON output. Every one of these skills returns structured status and error payloads, and parsing them is what lets an agent report a real failure instead of a plausible summary.
- Keep the email skills pointed at one mailbox and one purpose. SMTP credentials are the highest-value secret in the set and the hardest to rotate quietly.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
