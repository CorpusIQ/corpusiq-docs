---
title: "Boristane Agent Skills - Wide Event Logging Setup"
description: "boristane/agent-skills: 5.0K combined installs across 1 listing; wide-event canonical log line logging best practices for debugging and analytics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/boristane-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "logging", "observability", "wide events"]
---

# Boristane Agent Skills - Setup Guide

**Source:** [boristane/agent-skills](https://www.skills.sh/boristane/agent-skills) via skills.sh - 5.0K combined installs across 1 indexed listing; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 128 stars, no licence file, `main` branch, last pushed 2026-01-21. One skill directory, skills/logging-best-practices/, holding SKILL.md, README.md, metadata.json, and a rules/ folder with four guideline files.
**Category:** Logging and observability
**Quality Tier:** 🟠 Orange - no licence file; the single sampled skill passes all three verdicts.

boristane/agent-skills is a one-skill collection: logging-best-practices, which encodes wide-event logging (canonical log lines) guidance for agents. All 4,998 combined installs belong to that single listing.

The skill is guidance, not code: a SKILL.md plus a rules/ folder of four guideline files covering context, pitfalls, structure, and wide events. It follows the Agent Skills format and activates when an agent writes or reviews logging code.

## Installation

```bash
npx add-skill boristane/agent-skills
```

Skills are available automatically once installed; the agent uses them when a relevant task is detected. The README's examples are adding logging to an endpoint, reviewing logging code, and setting up logging for a service.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| logging-best-practices | 4,998 | Apply wide-event (canonical log line) logging: one context-rich event per request with high-cardinality fields, business and environment context, a single configured logger, and middleware-based infrastructure. |

The single indexed listing clears the threshold and appears in the table above.

## Why This Matters for Hermes Agents

Wide-event logging is the difference between logs you can query and logs you only read by hand. The skill pushes one context-rich event per request per service, with high-cardinality fields and business and environment context, so a single line answers questions that would otherwise need many joins.

For an agent adding logging, the default is a mix of ad-hoc console.log calls with no shared shape. This skill gives it a structure: one logger instance configured at startup, infrastructure logging in middleware, business context in handlers. The guidance is tool-agnostic and applies whether the agent is writing JavaScript, Python, or Go.

Because the skill is plain SKILL.md text, a harness that reads skill files, including Hermes, can load it directly. There are no scripts or dependencies to install or audit.

## Usage

| You say | What happens |
|---|---|
| "Add logging to this endpoint" | The agent applies wide-event structure: one event per request with business and environment context. |
| "Review my logging code" | The agent checks cardinality, field richness, logger configuration, and whether business context is captured. |
| "Help me set up logging for this service" | The agent designs the logger, middleware, and handler-level context per the skill's rules. |
| "What should go in this log line?" | The skill's structure and context rules decide what is worth logging and what is noise. |

## Verification

Probe the skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/boristane/agent-skills/main/skills/logging-best-practices/SKILL.md
```

Then install and ask the agent to add logging to an endpoint; confirm the emitted code uses one structured event rather than scattered console.log calls.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - the repo has no licence file. Re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| logging-best-practices | Pass | Pass | Pass |

The single sampled skill passes all three verdicts. The skill ships no code, scripts, or network calls.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,998 combined installs across 1 indexed listing; 128 GitHub stars; no licence file; last pushed 2026-01-21. Counts drift over time.
- There is no licence file, so treat the repo as all-rights-reserved rather than open source.
- A single skill: it only covers logging, and only as guidance. It ships no logging code or instrumentation library.
- The guidance is opinionated about the wide-event pattern and expects you to bring the logger and platform; it references Logging Sucks, wide-events, and Stripe's canonical log lines as background.

## Related

- [Honeycomb Agent Skill - Observability Setup](/hermes/skills/catalog/honeycomb-agent-skill-setup)
- [PostHog Instrumentation Skill - Analytics and Feature Flags](/hermes/skills/catalog/posthog-instrumentation-skill-setup)
- [Dash0 OpenTelemetry Skills - Setup Guide](/hermes/skills/catalog/dash0-otel-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Apply the wide-event pattern at service boundaries first; one canonical line per request makes analytics and debugging tractable.
- Keep the single-logger rule: one instance configured at startup, not a logger per file.
- Carry environment context (commit hash, version, region, instance ID) in the event, not in prose.
- Use the middleware pattern so infrastructure fields stay in one place and handlers add only business context.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
