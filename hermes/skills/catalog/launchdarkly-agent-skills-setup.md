---
title: "LaunchDarkly Agent Skills Setup Guide"
description: "Install and configure LaunchDarkly agent skills for feature flags, experiments, metrics, and AI agent control — 25+ skills, ~26K installs"
---

# LaunchDarkly Agent Skills

**Publisher:** [launchdarkly/ai-tooling](https://github.com/launchdarkly/ai-tooling) (20⭐)
**Skills.sh:** `npx skills add launchdarkly/agent-skills`
**Installs:** ~26,000+ combined across 25+ skills
**Quality:** 🟢 Production — official LaunchDarkly repository

> LaunchDarkly's public collection of agent skills and playbooks. Modular, text-based playbooks that teach an agent how to execute feature flag workflows safely and consistently — from flag creation through cleanup, plus experiment setup, AgentControl for LLM prompt management, and full onboarding sequences.

## What It Does

### Feature Flags (9 skills)

| Skill | Installs | Purpose |
|-------|----------|---------|
| **launchdarkly-flag-discovery** | 2,966 | Audit flags, find stale/launched flags, assess removal readiness |
| **launchdarkly-flag-cleanup** | 2,964 | Safely remove flags from code using LaunchDarkly as source of truth |
| **launchdarkly-flag-create** | 2,953 | Create new feature flags fitting existing codebase patterns |
| **launchdarkly-flag-targeting** | 2,950 | Control targeting, rollouts, rules, cross-environment config |
| **launchdarkly-flag-command** | 1,439 | Resolve `/flag` style requests into fast lookup and disambiguation |
| **launchdarkly-guarded-rollout** | 2,397 | Configure progressive traffic rollouts with metric monitoring and rollback |
| **should-flag-change** | — | Advisory: whether a code change (diff/PR) should ship behind a flag |
| **flag-release** | — | Record a flag's automated release for a PR |
| **flag-and-release-change** | — | End-to-end PR orchestrator: decide → create + wire → record release |

### AgentControl (10 skills)

| Skill | Purpose |
|-------|---------|
| **configs-create** | Create configs with variations for agent or completion mode |
| **configs-update** | Update and delete configs, manage lifecycle |
| **configs-variations** | Manage config variations for A/B testing |
| **configs-targeting** | Configure targeting rules for config rollouts |
| **tools** | Create and attach tools for function calling |
| **projects** | Create and manage projects to organize configs |
| **online-evals** | Attach LLM-as-a-judge evaluators to configs |
| **snippets** | Create and manage reusable prompt snippets across configs |
| **agent-graphs** | Create and manage multi-agent graphs with routing and handoffs |
| **migrate** | Migrate hardcoded LLM prompts to AgentControl in 5 stages |

### Experiments & Metrics (5 skills)

| Skill | Installs | Purpose |
|-------|----------|---------|
| **launchdarkly-experiment-setup** | 2,402 | Set up experiments with metrics, treatments, data collection |
| **launchdarkly-metric-choose** | 2,696 | Select the right metric type for an experiment |
| **launchdarkly-metric-create** | 2,688 | Create metrics and instrument tracking events |
| **launchdarkly-metric-instrument** | 2,688 | Add tracking calls to code for existing metrics |

### Onboarding (4 skills)

| Skill | Purpose |
|-------|---------|
| **onboarding** | End-to-end LaunchDarkly setup: kickoff roadmap, MCP, SDK, first flag |
| **mcp-configure** | Configure LaunchDarkly hosted MCP server (OAuth, no API keys) |
| **sdk-install** | Install and initialize the correct SDK (detect → plan → apply) |
| **first-flag** | Create a boolean flag, evaluate it, toggle for end-to-end proof |

## Why This Matters for Hermes Agents

LaunchDarkly skills transform feature flag management from manual dashboard clicking into agent-native workflows. A Hermes agent with these skills can autonomously audit stale flags, create new ones matching existing patterns, and configure guarded rollouts — all without leaving the codebase context. The **AgentControl** skills are uniquely positioned: they manage LLM prompts themselves as feature-flagged configurations, enabling A/B testing of agent prompts, multi-agent graph orchestration, and online eval attachment.

## Installation

### Prerequisites

- A LaunchDarkly account with API access
- An [API access token](https://docs.launchdarkly.com/home/account/api) with appropriate permissions
- Claude Code, Codex CLI, Cursor, or Hermes agent with MCP support

### Method 1: Claude Code Plugin (recommended)

```bash
# Add LaunchDarkly as a plugin marketplace
/plugin marketplace add launchdarkly/ai-tooling

# Install the plugin (includes all skills + MCP server)
/plugin install launchdarkly@launchdarkly-ai-tooling

# Authenticate the MCP server when prompted
```

### Method 2: skills.sh CLI

```bash
# Install all LaunchDarkly skills
npx skills add launchdarkly/ai-tooling --full-depth -y

# Or install specific skill categories
npx skills add launchdarkly/ai-tooling \
  --skill feature-flags/launchdarkly-flag-discovery \
  --skill feature-flags/launchdarkly-flag-cleanup \
  --skill feature-flags/launchdarkly-flag-create \
  --full-depth -y
```

### Method 3: Cursor Plugin

1. Open Cursor → **Settings > Plugins**
2. Search for **LaunchDarkly** in the marketplace
3. Or install from URL: `https://github.com/launchdarkly/ai-tooling`

### Method 4: Manual Copy

```bash
git clone https://github.com/launchdarkly/ai-tooling.git
cd ai-tooling

# Copy specific skills to your agent's skills directory
cp -r skills/feature-flags/launchdarkly-flag-cleanup ~/.hermes/skills/
cp -r skills/experiments/launchdarkly-experiment-setup ~/.hermes/skills/
```

## Quick Reference

| Workflow | Trigger Phrase |
|----------|---------------|
| Flag audit | "Which feature flags are stale and should be cleaned up?" |
| Flag creation | "Create a feature flag for the new checkout flow" |
| Flag cleanup | "Remove the `new-checkout-flow` feature flag from this codebase" |
| Rollout | "Roll out dark-mode to 25% of users in production" |
| Experiment setup | "Set up an experiment comparing the old vs new recommendation algorithm" |
| Guarded rollout | "Configure a guarded rollout for the payment service migration — 10% traffic, monitor error rate" |
| AgentControl migration | "Migrate our hardcoded support agent prompt to AgentControl" |
| Multi-agent graph | "Create an agent graph that routes product questions to the product agent and billing to the support agent" |

## Usage Examples

### Feature Flag Lifecycle
```
"Audit all feature flags in this repo — which ones are stale?"
"Create a boolean flag called 'new-search-ui' following our existing patterns"
"Wire the flag into the search component and create a PR with the flag change"
"Roll out new-search-ui to 10% of users, monitor for errors"
"Clean up the 'old-search-backend' flag — it's 100% launched everywhere"
```

### Experimentation
```
"Set up an A/B experiment: new recommendation algo vs current — measure conversion rate"
"Choose the right metric type for measuring signup completion rate"
"Instrument the signup flow with a conversion tracking event"
```

### AgentControl (AI Agent Configuration)
```
"Migrate our customer support agent's hardcoded system prompt to AgentControl"
"Create a prompt variation for the support agent with a more empathetic tone"
"Attach an LLM-as-judge evaluator to measure response quality"
"Set up an agent graph: triage agent → routes to product/support/billing specialist agents"
"Create a reusable prompt snippet for our brand voice guidelines"
```

## Verification

```bash
# Verify MCP server is configured
# In Claude Code: /status should show launchdarkly MCP connected

# Quick smoke test — ask the agent:
"List my LaunchDarkly feature flags"
"Show me any stale flags in production"

# AgentControl: verify config management
"Show my AgentControl projects"
```

## Pro Tips

1. **Start with the `onboarding` skill.** It provides an end-to-end setup sequence: MCP configuration → SDK installation → first flag creation. Complete this once and subsequent skills work without friction.

2. **`flag-and-release-change` is the highest-leverage single skill.** It orchestrates the entire PR workflow — deciding whether a change needs a flag, creating it, wiring it into code, and recording the release. Use it as your default entry point for any code change that might need flagging.

3. **AgentControl is LaunchDarkly for LLM prompts.** If you're A/B testing system prompts, managing multi-agent routing, or attaching evals to agent configurations, these skills replace manual prompt engineering workflows with version-controlled, feature-flagged configurations.

4. **The MCP server gives direct flag access.** Unlike skills.sh-only installs that require API token management, the Claude Code plugin and Cursor plugin include the LaunchDarkly MCP server for OAuth-based, keyless authentication.

5. **`launchdarkly-flag-cleanup` uses LaunchDarkly as source of truth.** It checks actual flag states (not just code references) to determine what's safe to remove — preventing the common mistake of removing a flag that's still active in one environment.

## Related Skills

- [Datadog Agent Skills](/hermes/skills/catalog/datadog-agent-skills-setup/) — monitor feature flag impact on system metrics
- [MongoDB Agent Skills](/hermes/skills/catalog/mongodb-agent-skills-setup/) — feature flag state storage alternative
- [AWS Agent Toolkit](/hermes/skills/catalog/aws-agent-toolkit-setup/) — CloudWatch Evidently integration for experiments

---

*Source: [skills.sh — launchdarkly/agent-skills](https://skills.sh/launchdarkly/agent-skills) · [GitHub](https://github.com/launchdarkly/ai-tooling) · ~26,000 combined installs across 25+ skills*
