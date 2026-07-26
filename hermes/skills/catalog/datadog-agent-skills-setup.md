---
title: "Datadog Agent Skills Setup Guide"
description: "Install and configure Datadog agent skills for monitoring, logging, APM, LLM observability, and audit — 20+ skills, ~12K installs"
---

# Datadog Agent Skills

**Publisher:** [datadog-labs/agent-skills](https://github.com/datadog-labs/agent-skills) (146⭐)
**Skills.sh:** `npx skills add datadog-labs/agent-skills`
**Installs:** ~12,000+ combined across 20+ skills
**Quality:** 🟢 Production — official Datadog Labs repository

> Datadog skills for Claude Code, Codex CLI, Gemini CLI, Cursor, Windsurf, OpenCode, and other AI agents. Essential monitoring, logging, tracing, and observability through the `pup` CLI.

## What It Does

| Skill | Category | Installs | Purpose |
|-------|----------|----------|---------|
| **dd-pup** | Core CLI | 2,573 | Primary CLI — commands, auth, PATH setup |
| **dd-monitors** | Monitoring | 1,198 | Create, manage, mute monitors and alerts |
| **dd-logs** | Logging | 1,314 | Search logs, pipelines, archives |
| **dd-apm** | APM | 1,266 | Traces, services, performance, Single-Step Instrumentation |
| **dd-docs** | Docs | 1,156 | Search Datadog documentation |
| **dd-browser-sdk** | Browser | 263 | RUM, Logs, Session Replay, version migration |
| **dd-audit** | Audit | 404 | Audit Trail investigations — SOC 2/PCI compliance, AI activity auditing |
| **dd-apps** | Platform | 39 | Build Datadog Apps — scaffold, run, upload, publish |
| **agent-observability-*** | LLM Obs | 233-237 | LLM trace analysis, eval generation, session classification (8 skills) |
| **dd-software-delivery** | CI/CD | — | Unblock PR pipelines, triage flaky tests |

## Why This Matters for Hermes Agents

Datadog skills give Hermes agents production-grade observability — search logs, query traces, manage monitors, and analyze LLM performance — all through the `pup` CLI without leaving the agent context. The **Agent Observability (LLMO)** skills are particularly relevant for teams running Hermes in production: they enable root-cause analysis of agent failures, automated eval generation, and session quality classification.

## Installation

### Prerequisites

```bash
# Install pup CLI (required for all Datadog skills)
# Option 1: Homebrew (macOS/Linux) — recommended
brew tap datadog-labs/pack
brew install datadog-labs/pack/pup

# Option 2: Build from source
git clone https://github.com/datadog-labs/pup.git && cd pup
cargo build --release
cp target/release/pup ~/.local/bin

# Authenticate
pup auth login

# Verify
pup auth status
```

### Method 1: skills.sh (recommended for Hermes agents)

Install the full Datadog skills suite:

```bash
npx skills add datadog-labs/agent-skills \
  --skill dd-pup \
  --skill dd-monitors \
  --skill dd-logs \
  --skill dd-apm \
  --skill dd-docs \
  --skill dd-browser-sdk \
  --skill dd-audit \
  --skill service-remapping \
  --skill agent-install \
  --skill enable-ssi \
  --skill verify-ssi \
  --skill troubleshoot-ssi \
  --skill onboarding-summary \
  --skill agent-observability-experiment-analyzer \
  --skill agent-observability-experiment-py-bootstrap \
  --skill agent-observability-trace-rca \
  --skill agent-observability-eval-bootstrap \
  --skill agent-observability-eval-pipeline \
  --skill agent-observability-session-classify \
  --skill agent-observability-auto-experiment \
  --skill agent-observability-replay-trace \
  --full-depth -y
```

### Method 2: Core skills only

```bash
npx skills add datadog-labs/agent-skills \
  --skill dd-pup \
  --skill dd-monitors \
  --skill dd-logs \
  --skill dd-apm \
  --skill dd-docs \
  --full-depth -y
```

### Method 3: Agent Observability (LLMO) skills only

```bash
npx skills add datadog-labs/agent-skills \
  --skill agent-observability-experiment-analyzer \
  --skill agent-observability-experiment-py-bootstrap \
  --skill agent-observability-trace-rca \
  --skill agent-observability-eval-bootstrap \
  --skill agent-observability-eval-pipeline \
  --skill agent-observability-session-classify \
  --skill agent-observability-auto-experiment \
  --skill agent-observability-replay-trace \
  --full-depth -y
```

### Method 4: CI/CD skills

```bash
npx skills add datadog-labs/agent-skills \
  --skill dd-software-delivery/unblock-pr \
  --skill dd-software-delivery/triage-flaky-test \
  --full-depth -y
```

## Quick Reference

| Task | Command |
|------|---------|
| Search error logs | `pup logs search --query "status:error" --from 1h` |
| List monitors | `pup monitors list` |
| Schedule downtime | `pup downtime create --file downtime.json` |
| Find slow traces | `pup traces search --query "service:api @duration:>500ms" --from 1h` |
| Query metrics | `pup metrics query --query "avg:system.cpu.user{*}"` |
| Check auth | `pup auth status` |
| Refresh token | `pup auth refresh` |

## Agent Observability (LLMO) — 8-Skill Pipeline

The LLM Observability skills form a complete eval pipeline for agent monitoring:

```
session-classify → trace-rca → eval-bootstrap → eval-pipeline → experiment → analyze
```

| Skill | Purpose |
|-------|---------|
| `session-classify` | Classify whether user intent was satisfied (trace + RUM signals) |
| `trace-rca` | Root-cause production failures using eval judge signal or runtime errors |
| `eval-bootstrap` | Generate evaluator code from traces, optionally seeded by RCA output |
| `eval-pipeline` | 8-phase pipeline: classify → RCA → bootstrap → dataset → publish → experiment → run → analyze |
| `experiment-analyzer` | Analyze and compare offline LLM experiments |
| `experiment-py-bootstrap` | Generate self-contained Python experiment code using `ddtrace.llmobs` SDK |
| `auto-experiment` | Local hill-climb: baseline-eval, make focused change, re-score, keep if better |
| `replay-trace` | Iterate on one trace: re-run against local code, diff old vs new output |

### LLMO MCP Requirements

```bash
# Required for all LLMO skills
claude mcp add --scope user --transport http "datadog-llmo-mcp" \
  'https://mcp.datadoghq.com/api/unstable/mcp-server/mcp?toolsets=llmobs'

# Required for experiment-analyzer (notebook export) and session-classify (RUM signals)
claude mcp add --scope user --transport http "datadog-mcp-core" \
  'https://mcp.datadoghq.com/api/unstable/mcp-server/mcp?toolsets=core'
```

## Usage Examples

### Monitor Management
```
"Search Datadog logs for errors in the last hour"
"Create a monitor for API response time exceeding 500ms"
"List all monitors and mute the staging ones"
"Investigate why CPU spiked on the production cluster at 3am"
```

### LLM Observability
```
"Analyze agent session quality from yesterday's traces"
"Root-cause why 15% of agent sessions failed yesterday"
"Generate eval code from the production failure patterns"
"Set up an experiment comparing two prompt variants for the support agent"
"Classify this week's agent sessions by user satisfaction"
```

### CI/CD
```
"Unblock the main branch PR pipeline — check what's failing"
"Triage the flaky test in the auth service"
```

### Audit
```
"Show who changed the production database monitor"
"Audit API key usage for SOC 2 compliance evidence"
"Investigate the AWS cost spike at 2am — who deployed what"
```

## Verification

```bash
# Verify pup CLI is working
pup auth status        # Should show authenticated

# Verify skills are installed
hermes skills list | grep dd-

# Quick smoke test
pup monitors list      # Should return monitor list (may be empty)

# LLMO: verify MCP tools are available
# After adding the MCP servers, restart the agent and query:
"List my Datadog LLM Observability experiments"
```

## Pro Tips

1. **OAuth tokens expire in ~1 hour.** If commands fail with 401/403, run `pup auth refresh` before retrying. The `dd-pup` skill includes auto-refresh logic.

2. **Start with core skills only** (`dd-pup`, `dd-monitors`, `dd-logs`, `dd-apm`, `dd-docs`). The LLMO and audit skills add significant depth but require MCP server setup and API access.

3. **The LLMO eval pipeline is powerful for production Hermes deployments.** If you're running agent workloads at scale, the `agent-observability-eval-pipeline` gives you a complete 8-phase feedback loop from failure detection to experiment analysis.

4. **`pup` commands respect your Datadog role permissions.** If the agent can't see certain monitors or logs, check the API key's RBAC scope — not the skill.

5. **CI/CD skills require both `pup` CLI and the Datadog MCP server.** Install both before using `triage-flaky-test` or `unblock-pr`.

## Related Skills

- [Grafana Agent Skills](/hermes/skills/catalog/grafana-skills-setup/) — alternative observability platform
- [MongoDB Agent Skills](/hermes/skills/catalog/mongodb-agent-skills-setup/) — database monitoring companion
- [AWS Agent Toolkit](/hermes/skills/catalog/aws-agent-toolkit-setup/) — cloud infrastructure monitoring
- [Cloudflare Skills](/hermes/skills/catalog/cloudflare-skills-setup/) — edge observability

---

*Source: [skills.sh — datadog-labs/agent-skills](https://skills.sh/datadog-labs/agent-skills) · [GitHub](https://github.com/datadog-labs/agent-skills) · ~12,000 combined installs across 20+ skills*
