---
title: "Honeycomb Agent Skill - Observability Setup"
description: "honeycombio/agent-skill: 4.1K combined installs across 8 listings, Honeycomb skills for OpenTelemetry, SLOs, queries and production investigation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/honeycomb-agent-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "honeycomb", "observability", "opentelemetry"]
---

# Honeycomb Agent Skill - Setup Guide

**Source:** [honeycombio/agent-skill](https://www.skills.sh/honeycombio/agent-skill) via skills.sh - 4.1K combined installs across 8 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 28 stars, MIT license, `main` branch, last pushed 2026-11-09, 11 `SKILL.md` files under `honeycomb/skills/` plus agents and a setup command
**Category:** Observability and OpenTelemetry instrumentation
**Quality Tier:** 🟡 Yellow - one of the two sampled skills carries a Snyk Warn while the other passes all three auditors.

Honeycomb's agent skill is built to complement its MCP server rather than replace it: the skills carry the judgement about instrumenting a system, and the MCP server carries the live queries against Honeycomb. The repository ships nine documented skills, two agent personas (a production investigator and an instrumentation advisor) and a `/honeycomb-setup` command that walks through wiring the MCP server.

The bulk of the install base sits in one place. `otel-instrumentation` accounts for 3,637 of the 4,105 combined installs, which says what people actually want from this collection: an agent that instruments code correctly with OpenTelemetry rather than a broad observability assistant.

## Installation

Install the plugin through Claude Code's marketplace:

```bash
claude plugin marketplace add honeycombio/agent-skill
claude plugin install honeycomb
```

The same repository works as a plugin marketplace for OpenAI Codex (`codex plugin marketplace add honeycombio/agent-skill`), Auggie (`auggie plugin marketplace add honeycombio/agent-skill` followed by `auggie plugin install honeycomb`) and GitHub Copilot CLI (`copilot plugin install honeycombio/agent-skill:honeycomb`). Cursor imports it from the plugin directory.

After installing, run `/honeycomb-setup` inside Claude Code or Cursor to configure the Honeycomb MCP server interactively. Without the MCP server, the skills still work for instrumentation code but cannot query your data.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| otel-instrumentation | 3,637 | Instrumenting applications with OpenTelemetry for Honeycomb: spans, attributes, semantic conventions and exporter setup. |
| query-patterns | 124 | Writing Honeycomb queries against the MCP server. |
| create-honeycomb-board | 110 | Creating boards that group the queries a team needs. |
| production-investigation | 68 | The multi-step investigation workflow for a production incident. |
| metrics-queries | 47 | Metrics queries alongside the trace-based ones. |
| slos-and-triggers | 44 | Defining SLOs and the triggers that watch them. |
| otel-genai-instrumentation | 41 | Instrumenting LLM and agent calls with the GenAI semantic conventions. |
| verify-recent-trace | 34 | Confirming that a trace actually arrived after an instrumentation change. |

All 8 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Instrumentation is a task where the failure is silent. Code that runs, logs nothing useful and exports no spans looks fine in review, and the problem only surfaces during an incident when the data you need was never captured. The instrumentation skill encodes the conventions that make traces useful: attribute naming, span boundaries, and the semantic conventions that Honeycomb's UI relies on for grouping and comparison.

The investigation skill is the other half. It turns an incident question into a sequence, which is what an agent needs to avoid the usual loop of broad queries and vague answers. Pairing it with the MCP server means the agent can move from code to telemetry without leaving the conversation.

The GenAI instrumentation skill is timely for agent builders. Tracing LLM calls needs different attributes than tracing HTTP handlers, and the conventions for prompts, token counts and model names are still settling. Having them written down is worth more than a generic observability primer.

## Usage

| You say | What happens |
|---|---|
| "Instrument this service with OpenTelemetry" | Uses the instrumentation skill to add spans, attributes and the exporter configuration. |
| "Why is checkout slow for one customer segment?" | Uses the investigation workflow with queries against the MCP server. |
| "Add tracing to our agent's LLM calls" | Uses the GenAI instrumentation skill for the model-specific attribute conventions. |
| "Build a board for the payments team" | Creates the board with the queries the team needs for its service. |
| "Set an SLO on p99 latency" | Uses the SLO and trigger skill to define the objective and the alert. |
| "Did my last deploy actually emit traces?" | Uses `verify-recent-trace` to confirm data arrived before the change is called done. |

## Verification

Check the skill files and the MCP configuration path before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/honeycombio/agent-skill/main/honeycomb/skills/otel-instrumentation/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/honeycombio/agent-skill/main/honeycomb/skills/production-investigation/SKILL.md
```

Skill paths sit under `honeycomb/skills/<name>/SKILL.md`. The MCP server is configured separately, either by the setup command or by hand in the host's MCP configuration.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| otel-instrumentation | Pass | Pass | Pass |
| production-investigation | Pass | Pass | Warn |

One of the two sampled skills carries a Snyk Warn. The MCP server it pairs with holds an API key that can read your telemetry, so scope that key to the environments you intend an agent to inspect.

## Limitations

- Snapshot data, verified 2026-11-14: 4,105 combined installs across 8 indexed listings; 28 GitHub stars; MIT; last pushed 2026-11-09. Counts drift over time.
- The README documents 9 skills while the tree carries 11 `SKILL.md` files; the install index lists 8, so the three counts do not agree.
- The install base is concentrated: 3,637 of 4,105 installs belong to `otel-instrumentation`, so the query and SLO skills are comparatively untested by the community.
- Live querying needs the Honeycomb MCP server and an API key. The skills alone cannot read your telemetry.
- The repository is small (28 stars) and young, so expect the guidance to move.
- Snyk warns on `production-investigation`, the skill an agent would use during an incident. Review it before enabling unattended use.

## Related

- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Sentry AI Monitoring - Agent Error Tracking Setup](/hermes/skills/catalog/sentry-ai-monitoring-setup)
- [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/honeycomb-setup` rather than hand-writing the MCP configuration; it handles the environment and key prompts.
- Ask the agent to verify a recent trace after any instrumentation change, so a silent no-op is caught in the same session.
- Scope the Honeycomb API key per environment, since an agent with production access can read every span.
- Use the GenAI skill for LLM calls: the generic instrumentation skill will not produce the model-level attributes.
- Start from an existing board before creating a new one; the query patterns skill keeps naming consistent.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
