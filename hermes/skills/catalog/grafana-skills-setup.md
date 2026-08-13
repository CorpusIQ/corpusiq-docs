---
title: Grafana Skills — Observability & Monitoring Platform for Hermes Agents
description: Grafana's official agent skills — dashboarding, PromQL, Loki, Mimir, Pyroscope, Beyla, alerting, infrastructure monitoring. 16K+ combined installs across 8 skills for agent infrastructure observability.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/grafana-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Grafana Skills — Setup Guide

**Source:** [grafana/skills](https://skills.sh/grafana/skills) (16K+ combined installs)
**GitHub:** [grafana/skills](https://github.com/grafana/skills) (200 ⭐)
**Category:** Observability / DevOps
**Quality Tier:** 🟢 Production

Grafana Skills is the official agent skills collection for the Grafana observability platform. It covers dashboard creation, PromQL querying, log aggregation with Loki, metrics with Mimir, profiling with Pyroscope, eBPF auto-instrumentation with Beyla, and alerting/incident response management. These skills enable Hermes agents to build, monitor, and respond to infrastructure observability needs.

---

## Installation

```bash
# Core observability skills (highest installs)
npx skills add grafana/skills --skill dashboarding
npx skills add grafana/skills --skill promql
npx skills add grafana/skills --skill grafana-oss

# Monitoring & alerting
npx skills add grafana/skills --skill app-observability
npx skills add grafana/skills --skill infrastructure
npx skills add grafana/skills --skill alerting-irm

# Specialized tools
npx skills add grafana/skills --skill loki
npx skills add grafana/skills --skill mimir
npx skills add grafana/skills --skill pyroscope
npx skills add grafana/skills --skill beyla
npx skills add grafana/skills --skill assistant-mcp
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **dashboarding** | 2.9K | Build Grafana dashboards — panels, visualizations, variables, data sources |
| **promql** | 2.6K | PromQL query language for Prometheus metrics — aggregation, functions, recording rules |
| **grafana-oss** | 2.5K | Grafana OSS deployment and configuration — data sources, auth, plugins, provisioning |
| **assistant-mcp** | 1.8K | Grafana Assistant MCP server — natural language querying of observability data |
| **app-observability** | 1.8K | Application observability patterns — traces, RED metrics, SLOs, error budgets |
| **infrastructure** | 1.8K | Infrastructure monitoring — node metrics, Kubernetes, cloud provider integrations |
| **alerting-irm** | 2.2K | Alerting and Incident Response Management — alert rules, notification policies, on-call |
| **loki** | 2.4K | Log aggregation with Grafana Loki — LogQL queries, log parsing, structured metadata |
| **mimir** | 2.1K | Metrics storage with Grafana Mimir — long-term Prometheus storage, multi-tenancy |
| **pyroscope** | 2.1K | Continuous profiling with Grafana Pyroscope — flame graphs, performance analysis |
| **beyla** | 2.1K | eBPF auto-instrumentation with Grafana Beyla — zero-code observability for HTTP/gRPC services |

---

## 🔑 Standout Features

### Natural Language Observability (assistant-mcp)
The Grafana Assistant MCP server lets Hermes agents query observability data using natural language. Instead of writing PromQL or LogQL, agents can ask "show me error rates for the last hour" or "what services had the highest latency today" — the MCP server translates to queries and returns results.

### Zero-Code Instrumentation (beyla)
eBPF-based auto-instrumentation requires no code changes. Hermes agents can deploy Beyla to get HTTP/gRPC metrics, traces, and service maps without modifying application code — ideal for monitoring existing infrastructure.

### Unified Observability Stack
Grafana's integrated approach — metrics (Mimir/Prometheus), logs (Loki), traces (Tempo), profiles (Pyroscope) — means one skills repo covers the full observability spectrum. Agents can correlate across all signals.

---

## Hermes Agent Use Cases

- **Agent Infrastructure Monitoring**: Build dashboards tracking Hermes agent health, token usage, API latency, and error rates
- **Cost Observability**: Create dashboards monitoring LLM API costs, database egress, and infrastructure spend
- **Alerting**: Set up alerts for agent failures, rate limit hits, cost spikes, or performance degradation
- **Performance Profiling**: Use Pyroscope to profile agent code and identify bottlenecks
- **Log Analysis**: Use Loki + LogQL to search and analyze agent logs at scale

---

## Discovery Method

Publisher sweep via `npx skills find "dashboard" --owner "grafana"`. Grafana was not previously catalogued in any sweep. Confirmed 11 skills across the skills repo. The dashboarding skill at 2.9K installs is the most-installed observability-specific skill on skills.sh.

---

## Notes

- **dashboarding** (2.9K) is the highest-install observability skill — directly applicable to CorpusIQ's own infrastructure monitoring
- **assistant-mcp** enables natural language Grafana queries — perfect for agent-to-agent communication about system health
- **beyla** provides zero-code instrumentation — deploy once, get full observability across all services
- The Grafana stack is open source — no vendor lock-in, self-hostable for agent infrastructure
