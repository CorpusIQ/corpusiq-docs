---
title: "New Skills — July 26, 2026 Marketplace Sweep (Update #2)"
description: "3 new publishers, 3 setup guides created, ~43K+ combined installs. DevOps/observability sweep of skills.sh for Hermes-relevant skills from Datadog, LaunchDarkly, and Railway."
---

# New Skills — July 26, 2026 (Update #2)

## Summary

| Metric | Count |
|---|---|
| New publishers found | 3 |
| Setup guides created | 3 |
| Combined installs | ~43,000+ |
| Combined GitHub stars | 466 ⭐ |
| Quality: 🟢 Production | 3 |
| Quality: 🟡 Beta | 0 |
| Quality: 🔵 Community | 0 |

## New Skills

### Observability / Monitoring

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Datadog Agent Skills** | datadog-labs/agent-skills | 12K+ | 146⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/datadog-agent-skills-setup/) |

### Feature Management / Experimentation

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **LaunchDarkly Agent Skills** | launchdarkly/ai-tooling | 26K+ | 20⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/launchdarkly-agent-skills-setup/) |

### Platform / Deployment

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **Railway Agent Skills** | railwayapp/railway-skills | 5.5K+ | 300⭐ | 🟢 | [Setup Guide](/hermes/skills/catalog/railway-agent-skills-setup/) |

## 🔑 Standout Finds

### datadog-labs/agent-skills (12K+ installs, 146⭐)
The most comprehensive observability skills suite on skills.sh with 20+ skills spanning logs, monitors, APM, LLM observability, CI/CD, and audit. The **Agent Observability (LLMO)** skills are uniquely positioned — Datadog is the first major observability platform to ship agent-native skills for evaluating and improving LLM-powered agents. The 8-skill eval pipeline (classify → RCA → bootstrap evaluators → dataset → experiment → analyze) is production-grade agent quality infrastructure.

### launchdarkly/ai-tooling (26K+ installs, 20⭐)
The highest-install feature management skills on skills.sh with 25+ skills across feature flags, experiments, metrics, and AgentControl (LLM prompt management). **AgentControl** is the standout: it treats LLM prompts as feature-flagged configurations, enabling A/B testing of system prompts, multi-agent graph orchestration with routing, and online eval attachment. This is LaunchDarkly applied to AI agents themselves — a category-defining approach.

### railwayapp/railway-skills (5.5K+ installs, 300⭐)
The highest-starred deployment platform skills outside of the major cloud providers. Railway's one-command agent setup (`curl -fsSL agents.railway.com | sh`) is the smoothest onboarding of any platform skill — it installs skills, configures MCP, and verifies auth in a single step. The multi-plugin packaging (Claude Code, Codex, Grok Build, Cursor) makes Railway the most broadly compatible deployment skill.

## Other Highlights

- **Datadog LLMO skills fill a critical gap.** No other observability platform offers agent-native LLM evaluation tools. The `agent-observability-eval-pipeline` skill provides an 8-phase feedback loop from failure detection to experiment analysis — directly applicable to Hermes agents running in production.
- **LaunchDarkly AgentControl is category-defining.** Feature-flagging LLM prompts, managing multi-agent routing graphs, and attaching evals to configs is a new paradigm. Other feature flag platforms (Split, Optimizely, CloudBees) have no equivalent agent skills.
- **Railway's plugin packaging is the gold standard.** The `claude-plugins-official` listing, Cursor Marketplace presence, and Codex plugin manifest make Railway the most broadly accessible deployment skill across agent platforms.

## Discovery Method

DevOps/observability platform sweep: following the July 26 enterprise sweep (Cloudflare, AWS, Google, HashiCorp, MongoDB, Databricks) and design/DB update (Neon, Anthropic, Figma, Grafana, PlanetScale), this third sweep targeted observability, feature management, and deployment platforms. Used `curl` + skills.sh `/api/search` endpoint with owner-scoped queries across 30+ additional publishers. Cross-referenced against 321 existing catalog entries. Confirmed 3 new publishers not previously catalogued.

Publishers checked but deprioritized: Kong (379 inst, `membranedev` wrapper), Splunk (546 inst, wrapper), New Relic (226 inst, wrapper), PagerDuty (275 inst, wrapper), Sentry (already catalogued via other publishers), WorkOS (1.2K inst, already catalogued), Upstash (2.1K inst, already catalogued).

## Notes

- This is the third marketplace sweep of July 26 — following the morning enterprise sweep (6 publishers, 146K+ installs) and the afternoon design/DB update (5 publishers, 190K+ installs). Combined: **14 new publishers, ~379K+ installs found today**.
- **datadog-labs/agent-skills** at 12K installs is the first major observability platform with agent-native skills — Grafana (16K) was catalogued in the previous update but Datadog's LLMO skills are uniquely comprehensive.
- **launchdarkly/ai-tooling** at 26K installs makes LaunchDarkly the highest-install feature management platform on skills.sh. The repo is `launchdarkly/ai-tooling` but skills.sh lists it as `launchdarkly/agent-skills`.
- **railwayapp/railway-skills** at 300 GitHub stars has the highest star count of any deployment platform skills repo — higher than Cloudflare (2,481 in total but distributed across repos). Railway's community engagement is notably strong.
- 324 catalog entries now exist (up from 321 after this sweep).
- Firecrawl was unavailable for web extraction — all skill content was fetched via raw `curl` to GitHub raw content URLs.
