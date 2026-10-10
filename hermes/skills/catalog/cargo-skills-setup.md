---
title: "Cargo Skills - GTM Engineering Suite for Agents Setup"
description: "Setup guide for getcargohq/cargo-skills - 142.8K combined installs. 19 GTM engineering skills: lead lists, enrichment, email, CRM sync, orchestration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cargo-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "gtm engineering", "sales automation", "lead generation"]
---

# Cargo Skills - Setup Guide

**Source:** [getcargohq/cargo-skills](https://www.skills.sh/getcargohq/cargo-skills) via skills.sh - 142.8K combined installs across 28 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [getcargohq/cargo-skills](https://github.com/getcargohq/cargo-skills) (19 stars, MIT; pushed Oct 9, 2026; skills live at the repo root)
**Category:** GTM Engineering / Sales Automation
**Quality Tier:** 🟡 Beta - company-backed (Cargo), MIT, pushed Oct 9, 2026; low stars (19); all sampled verdicts Pass

Cargo Skills is a nineteen-skill bundle from Cargo (getcargohq) that turns Claude Code, Codex, Cursor, or any skills.sh-compatible agent into a go-to-market engineering workstation: build lead lists, find and verify emails and phone numbers, enrich companies and contacts through provider waterfalls, score and qualify leads, write outreach, sync to a CRM, and monitor buying signals like job changes, funding rounds, and tech-stack intent.

The skills run on the Cargo CLI against Cargo, an AI-native revenue platform with 138 integrations (HubSpot, Salesforce, Attio, Pipedrive, Outreach, Salesloft, and more) and 50 credits-based data providers with per-action costs documented up front. The bundle ships nineteen skills: a router (cargo), an onboarding demo (cargo-quickstart), an outcome front door (cargo-gtm) that routes real-world goals to recipes, and sixteen capability skills spanning each CLI domain, diagnostics, and the hosted MCP server.

---

## Installation

```bash
# Whole bundle via skills.sh - works in Claude Code, Codex, Cursor, and any compatible agent
npx skills add getcargohq/cargo-skills --all

# Hermes Agent: lands all nineteen under .hermes/skills/ (or ~/.hermes/skills/ with -g) as siblings
npx skills add getcargohq/cargo-skills --agent hermes-agent

# Or install one skill at a time from inside Hermes
hermes skills install skills-sh/getcargohq/cargo-skills/cargo-gtm

# Prerequisite: the Cargo CLI the skills run on, then sign in (emailed code, no browser)
npm install -g @cargo-ai/cli
cargo-ai login --email you@company.com
cargo-ai whoami
```

`--all` is shorthand for `--skill '*' --agent '*' -y`: it takes every skill in the bundle and behaves the same in a terminal, in CI, and inside an agent. An alternative Claude Code plugin channel adds an approval hook for safe CLI calls, session-lifecycle hooks, and native subagents: run `/plugin marketplace add getcargohq/cargo-skills` then `/plugin install cargo@cargo`. Pick one channel only - the plugin and `skills add` both register the skills, and running both duplicates them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cargo-connection | 8,747 | Authenticate connectors and discover integration actions across 120+ integrations |
| cargo-gtm | 8,560 | Outcome front door: routes goals to bundled recipes (prospecting, TAM, signals) |
| cargo-ai | 8,554 | Create and configure AI agents, RAG knowledge, MCP servers; inspect agent memories |
| cargo-workspace-management | 8,550 | Invite users, create and rotate API tokens, organize folders, manage roles |
| cargo-orchestration | 8,545 | Execute actions, chain workflows, trigger batches, and poll async operations |
| cargo-analytics | 8,542 | Download run results, export segment data, monitor error rates and success metrics |
| cargo-storage | 8,540 | Inspect models and DDL, create columns, set relationships, query storage with SQL |
| cargo-billing | 8,536 | Track credit consumption per workflow or connector; check subscription and invoices |
| cargo-context | 8,498 | Browse and edit the git-backed GTM context repo; inspect the knowledge graph |
| cargo | 8,455 | Router skill: the always-loadable front door for any Cargo CLI task |
| cargo-content | 8,406 | Upload knowledge files; build native and connector-backed libraries for RAG |
| cargo-hosting | 8,348 | Scaffold, deploy, and promote hosted apps and edge workers |
| cargo-quickstart | 7,423 | Guided first-run demo: 25 persona-matched leads in under two minutes |
| cargo-cdk | 7,421 | Declarative workspace-as-code: define builders, then init, plan, and deploy |
| cargo-diagnostics | 7,330 | Forensic runbooks: trace a run, sweep a batch for errors, profile credit spend |
| cargo-observability | 4,879 | Threshold alerts on workflow telemetry that fire notifications or actions |
| cargo-segmentation | 4,652 | Build saved audience segments; size an audience before spending on it |
| cargo-mailbox-management | 3,725 | Provision sending inboxes, run provider warm-up and the 5 to 40 per day send ramp |
| cargo-mcp | 3,281 | Drive Cargo from the hosted MCP server with no CLI installed |

The remaining 9 indexed listings range from 2 to 1,737 installs.

## Why This Matters for Hermes Agents

Cargo's skills are built for agents that act on real revenue data, not just talk about it: each wraps concrete CLI operations with cost transparency, so an agent can probe a source on a few rows, price it per hit, and only then fan out across a list. The bundle installs through skills.sh with the hermes-agent target and lands as siblings under .hermes/skills/, so the cross-skill references that drive the router, outcome, and capability graph resolve the same way they do on other channels. Two Hermes-specific differences are worth knowing up front: the plugin channel's approval hook does not apply here (Hermes gates tool calls with its own approval policy, and its pre_tool_call hooks can only block a call, never pre-approve one, so expect cargo-ai commands to prompt), and no session-lifecycle hooks ship with the bundle, so the session's three jobs (refresh, register, finalize) are the agent's to run by hand. The router skill already accounts for agents without lifecycle hooks, so day-to-day use works out of the box; the hooks only add hard enforcement and session logging on top.

## Usage

| You say | What happens |
|---|---|
| "Find me 50 VPs of Sales at Series B fintechs and verify their emails." | cargo-gtm routes to the prospecting recipe: source, enrich, verify, then sync, with a cost receipt per step. |
| "Build a TAM list of seed-stage SaaS companies in Europe." | The build-tam recipe scales a Total Addressable Market list from 100 to 10,000 companies. |
| "Alert me when the enrichment error rate goes above 5%." | cargo-observability creates a scheduled threshold alert that fires a notification or action on breach. |
| "Set up our whole workspace as code so I can review it in a PR." | cargo-cdk defines every resource in code and deploys it with cargo-ai project (init, plan, deploy). |
| "How many credits did the enrichment play consume last month?" | cargo-billing queries credit consumption broken down by workflow, connector, or date range. |
| "Trace why one run misbehaved." | cargo-diagnostics runs a forensic sweep across the run, SQL, and billing surfaces. |
| "Trigger the scoring play on our new MQL segment." | cargo-orchestration discovers the workflow, builds the input, triggers the batch, and polls until done. |

## Verification

Confirm the bundle landed and the CLI is authenticated, then review any skill's source before trusting it:

```bash
# List installed skills
npx skills list | grep cargo

# Hermes install location
ls .hermes/skills/ | grep cargo

# Confirm the CLI is signed in
cargo-ai whoami

# Review a skill's full source before install
curl -sL https://raw.githubusercontent.com/getcargohq/cargo-skills/main/cargo-connection/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cargo-connection | Pass | Pass | Pass |
| cargo-gtm | Pass | Pass | Warn |
| cargo-ai | Pass | Pass | Pass |

## Limitations

- New, low-traction repo: 19 GitHub stars and first seen Oct 9, 2026, so independent third-party validation is thin.
- cargo-gtm carries a Snyk Warn while the other sampled skills pass; re-check the skills.sh security pages before production use.
- The skills are wrappers over the external Cargo CLI and a Cargo workspace: a new account starts with 100 free credits (no card), then usage is credits-based and paid.
- On Hermes the plugin channel (approval hook, session hooks, native subagents) does not apply, and the session's three jobs (refresh, register, finalize) must be run by hand.
- Install this bundle or the standalone getcargohq/gtm-skills repo, not both - standalone skills defer to cargo-gtm when the pack is present.
- The old curl install.sh bootstrap is retired; use the plugin, the INSTALL.md paste flow, or the manual CLI commands.

- Snapshot data, verified Oct 10, 2026: 142,805 combined installs across 28 indexed listings; 19 GitHub stars; MIT; last pushed Oct 9, 2026. Counts drift over time.

## Related

- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/hermes/skills/catalog/apify-growth-skills-setup) - adjacent lead-gen and scraping skills for growth pipelines
- [firecrawl-workflows - Growth & Research Automation Setup](/hermes/skills/catalog/firecrawl-workflows-setup) - research and crawling workflows that pair with Cargo's sourcing recipes
- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup) - content operations for the outreach side of a GTM stack
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup) - marketing playbooks that complement signal-driven outreach
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run cargo-quickstart first: one question ("who do you sell to?"), 25 leads in under two minutes, with a cost receipt.
- Load the cargo router skill when stitching several capability skills together; it explains the UUID flow between skills and async polling.
- Cost a source before scaling it: probe candidates on 5 to 10 rows and price per hit before any fan-out (source-planning recipe).
- Keep the CLI at the bundle's pinned version in cargo/cli-version; the skills and CLI are verified together at that pin.
- On Hermes, run the session's three jobs (refresh, register, finalize) yourself since no lifecycle hooks are bundled.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
