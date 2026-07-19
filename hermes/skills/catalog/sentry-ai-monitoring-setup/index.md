---
title: Sentry AI Monitoring — Full Setup Guide for Hermes Agents
description: Error tracking and monitoring for AI agent deployments. Sentry feature setup (2.7K), Node.js SDK (2.6K), and AI monitoring dashboard (616). From getsentry — the industry-standard error tracking platform.
---

# Sentry AI Monitoring — Setup Guide

**Source:** [getsentry/sentry-for-ai](https://github.com/getsentry/sentry-for-ai) + [getsentry/sentry-agent-skills](https://github.com/getsentry/sentry-agent-skills)
**Skills:** `sentry-feature-setup` (2,700), `sentry-node-sdk` (2,600), `sentry-setup-ai-monitoring` (616)
**Category:** Monitoring / Observability
**Platform:** Sentry (4M+ developers, industry standard)

Sentry's dedicated AI agent monitoring suite. Three skills covering progressive rollout tracking, agent-aware error instrumentation, and purpose-built AI monitoring dashboards. Unlike generic error trackers, these skills understand agent failure modes: infinite loops, tool timeouts, context corruption, credential rotation failures, and MCP connection drops.

---

## Installation

```bash
# Install all three Sentry AI skills
npx skills add getsentry/sentry-for-ai@sentry-feature-setup
npx skills add getsentry/sentry-for-ai@sentry-node-sdk
npx skills add getsentry/sentry-agent-skills@sentry-setup-ai-monitoring
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Sentry account** | [sentry.io](https://sentry.io) — free tier: 5K errors/month, 1 user |
| **Sentry DSN** | From Sentry → Settings → Projects → [Project] → Client Keys (DSN) |
| **Node.js 18+** | For the sentry-node-sdk skill |
| **Hermes Agent** | Any version |

```bash
export SENTRY_DSN="https://xxxxxx@sentry.io/project-id"
# Or add to ~/.hermes/config.yaml under env:
```

---

## Skill 1: sentry-feature-setup (2,700 installs)

### Overview
Feature flag and release monitoring for agent deployments. Track which agent versions, model configurations, and skill combinations correlate with error rates. Progressive rollout support — ship new skills to a subset of agent instances, monitor error rates, then expand or roll back.

### Capabilities
- **Release tracking:** Associate every error with a specific agent version + skill set
- **Feature flags:** Toggle skills on/off per agent instance; correlate with error patterns
- **Progressive rollout:** Canary deployment — 10% → 25% → 50% → 100% with automatic rollback on error spike
- **Model correlation:** Track error rates by model (Sonnet vs Opus vs DeepSeek) to identify model-specific failure modes
- **Skill health scores:** Per-skill error rate, latency, and success rate dashboards

### Configuration
```yaml
# In ~/.hermes/config.yaml
monitoring:
  sentry:
    dsn: "${SENTRY_DSN}"
    release: "hermes-${HERMES_VERSION}"
    environment: "production"
    feature_flags:
      progressive_rollout: true
      canary_percentage: 10
      auto_rollback: true
      rollback_threshold: 5%  # Error rate threshold
```

### Usage
```bash
# Tag current deployment
npx skills run sentry-feature-setup --tag-release "v2.4.1-skills-update"

# Start canary rollout of new skill
npx skills run sentry-feature-setup \
  --canary "apify-lead-generation" \
  --percentage 10 \
  --monitor-duration "24h"

# Check skill health
npx skills run sentry-feature-setup --health-check "apify-lead-generation"
```

---

## Skill 2: sentry-node-sdk (2,600 installs)

### Overview
Sentry's Node.js SDK instrumented specifically for agent runtimes. Auto-captures unhandled promise rejections, tool call failures, and MCP connection errors — but adds agent-specific context: current skill name, tool chain, model identifier, token usage, and session ID. Drop-in replacement for generic `console.error()` or `try/catch` logging.

### What It Captures Automatically
| Error Type | Captured Context |
|---|---|
| **Tool call failure** | Tool name, parameters (sanitized), error message, stack trace |
| **MCP connection error** | Server name, transport type, reconnect attempts, latency |
| **Model API error** | Model name, provider, status code, retry count, token usage at failure |
| **Skill execution error** | Skill name, step number, input hash, duration |
| **Rate limit (429)** | Endpoint, retry-after header, current rate-limit state |
| **Context window overflow** | Current token count, max tokens, model, last 5 messages truncated |
| **Credential rotation failure** | Service name, token age, attempt count (never logs the token itself) |

### Integration
```javascript
// In any Hermes tool or skill
const Sentry = require('@sentry/node');

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: 'production',
  tracesSampleRate: 0.1,  // 10% of agent sessions
});

// Agent context is automatically attached:
// - skill: current skill name
// - tool_chain: chain of tools leading to error
// - model: active LLM model
// - session_id: Hermes session UUID
// - token_usage: tokens consumed this session
```

### Hermes Integration
The skill instruments Hermes' error handling automatically. Once installed, every unhandled error in a Hermes session is captured with full agent context and routed to your Sentry project. No code changes required — the skill wraps the error boundary.

---

## Skill 3: sentry-setup-ai-monitoring (616 installs)

### Overview
Purpose-built AI monitoring dashboards and alerting. Pre-configured views for agent-specific metrics: tool call latency distributions, model response times, context window utilization, skill invocation counts, and error categorization by failure type. Ships with alert rules for common agent failure patterns.

### Pre-Built Dashboards

| Dashboard | What It Shows |
|---|---|
| **Agent Error Overview** | Error count, rate, and breakdown by skill/tool/model |
| **Tool Performance** | P50/P95/P99 latency per tool, error rate per tool, invocation count |
| **Model Health** | Response time by model, error rate by model, token usage by model |
| **Session Analytics** | Session duration distribution, error sessions vs clean sessions, token efficiency |
| **Skill Reliability** | Per-skill success rate, failure mode breakdown, execution duration |
| **MCP Health** | Server uptime, connection drops, latency by transport type |

### Alert Rules (Pre-Configured)

```yaml
alerts:
  - name: "Agent error spike"
    condition: error_rate > 5% over 15min window
    action: slack #hermes-alerts

  - name: "Tool timeout cascade"
    condition: tool_timeout_count > 10 in 5min window
    action: slack #hermes-alerts + auto-pause agent

  - name: "Context window near limit"
    condition: token_usage > 85% of max
    action: log + auto-compact

  - name: "MCP connection flapping"
    condition: mcp_reconnect_count > 5 in 10min
    action: slack #infra-alerts

  - name: "Model degradation"
    condition: model_error_rate > 2% over 30min
    action: slack #hermes-alerts + auto-switch-model
```

### Usage
```bash
# Open the AI monitoring dashboard
npx skills run sentry-setup-ai-monitoring --dashboard

# Configure alerts
npx skills run sentry-setup-ai-monitoring \
  --configure-alerts \
  --slack-webhook "https://hooks.slack.com/..."

# Export agent reliability report
npx skills run sentry-setup-ai-monitoring \
  --report weekly \
  --output "agent-reliability-$(date +%Y-%m-%d).pdf"
```

---

## CorpusIQ Use Cases

| Use Case | Skills Used |
|---|---|
| **Cron job reliability** | sentry-feature-setup + sentry-setup-ai-monitoring — track every cron execution, alert on failures, weekly reliability reports |
| **Skill deployment safety** | sentry-feature-setup — canary new skills before full rollout; auto-rollback on error spike |
| **Model performance tracking** | sentry-node-sdk + sentry-setup-ai-monitoring — compare Sonnet vs Opus error rates and latency; data-driven model routing |
| **Growth agent uptime** | sentry-setup-ai-monitoring — ensure social monitoring, lead gen, and content posting never silently fail |
| **Multi-agent observability** | All three — unified dashboard across CorpusIQ's growth, BD, support, and dev agents |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **SENTRY_DSN not recognized** | Verify env var: `echo $SENTRY_DSN`. Add to `~/.hermes/config.yaml` `env:` block |
| **No errors appearing in Sentry** | Check `sentry.io` → Project → Settings → Client Keys → verify DSN. Check network egress allows `*.sentry.io` |
| **Too many events (rate limited)** | Reduce `tracesSampleRate` from 1.0 to 0.1 (10% sampling). Free tier: 5K errors/month |
| **PII in error reports** | Enable PII scrubbing: Sentry → Project → Settings → Security & Privacy → Data Scrubbing |
| **Dashboard empty** | Wait 5-10 minutes for first data. Run a test: `npx skills run sentry-setup-ai-monitoring --test-event` |

---

## Verification

```bash
# Verify all Sentry skills installed
npx skills list | grep sentry

# Send a test event
npx skills run sentry-node-sdk --test-event

# Check Sentry dashboard
npx skills run sentry-setup-ai-monitoring --dashboard

# Verify alert configuration
npx skills run sentry-setup-ai-monitoring --test-alert
```

---

## Integration with Existing Monitoring

CorpusIQ already uses several monitoring systems. Sentry AI monitoring complements them:

| Existing System | Sentry Adds |
|---|---|
| **Token health cron** | Error tracking for the cron itself — detect when token refresh fails silently |
| **System auditor** | Agent-specific error categorization (tool failure vs model error vs MCP drop) |
| **Daily HTML reports** | Real-time alerting (don't wait for the daily report to discover failures) |
| **Honcho session tracking** | Structured error context per session for post-mortem analysis |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july17-2026-update/) →*
*Powered by CorpusIQ*
