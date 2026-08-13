---
title: Monitoring Expert — Setup Guide for Hermes Agents
description: Configure monitoring systems, implement observability pipelines, create dashboards — 3.9K+ installs
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/monitoring-expert-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Monitoring Expert — Setup Guide

**Source:** [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills) (Community)
**Skill:** `monitoring-expert` · **Installs:** 3,900+ · **Category:** DevOps & Infrastructure
**Platform:** Linux, macOS, Windows

Monitoring Expert is an observability and performance specialist skill that implements comprehensive monitoring, alerting, tracing, and performance testing systems. It covers Prometheus/Grafana stacks, structured logging pipelines, distributed tracing instrumentation, load testing with k6/Artillery, and capacity planning. Ideal for Hermes agents managing infrastructure or debugging production issues.

## Installation

```bash
npx skills add jeffallan/claude-skills@monitoring-expert
```

## What It Does

The skill follows a four-stage observability workflow:

1. **Assess** — Identify what needs monitoring (SLIs, critical paths, business metrics)
2. **Instrument** — Add logging, metrics, and traces to applications
3. **Collect** — Configure aggregation and storage (Prometheus, log shippers, OTLP)
4. **Visualize** — Build dashboards using RED (Rate/Errors/Duration) or USE (Utilization/Saturation/Errors) methods

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v1.0+ |
| Target application | Access to instrument code |
| Monitoring stack | Prometheus, Grafana, or Datadog (optional) |
| Load testing tools | k6 or Artillery (optional) |

## Usage with Hermes

Trigger the skill for any observability task:

```
"Set up application monitoring for our Node.js API"
"Add structured logging to the Python service"
"Create a Grafana dashboard for API latency"
"Run a load test against production with k6"
"Profile CPU/memory bottlenecks in the worker process"
"Define alerting rules for 5xx error rates"
```

### Example: Setting Up API Monitoring

```
"Configure Prometheus metrics for our Express.js API — track request rate, error rate, and p95 latency"
```

The skill instruments the application with appropriate metrics libraries, configures scrape endpoints, builds Grafana dashboards, and defines alerting rules.

## Core Capabilities

| Capability | Tools/Frameworks |
|------------|-----------------|
| Metrics collection | Prometheus, OpenTelemetry |
| Visualization | Grafana, Datadog |
| Logging pipelines | Structured logging, log shippers |
| Distributed tracing | OpenTelemetry, Jaeger |
| Load testing | k6, Artillery |
| Profiling | CPU/memory profilers |
| Capacity planning | Trend analysis, forecasting |

## Guardrails

- Always verify data arrives before building dashboards
- Use RED method for services, USE method for resources
- Alert on symptoms, not causes
- Never alert on raw metrics without aggregation windows

## Related Skills

- [AWS Agent Toolkit Setup](/docs/hermes/skills/catalog/aws-agent-toolkit-setup/) — AWS infrastructure monitoring
- [Sentry AI Monitoring Setup](/docs/hermes/skills/catalog/sentry-ai-monitoring-setup/) — Error tracking
- [HashiCorp Agent Skills Setup](/docs/hermes/skills/catalog/hashicorp-agent-skills-setup/) — Infrastructure management

## Source

- **skills.sh:** [jeffallan/claude-skills@monitoring-expert](https://skills.sh/jeffallan/claude-skills)
- **GitHub:** [github.com/jeffallan/claude-skills](https://github.com/jeffallan/claude-skills)
