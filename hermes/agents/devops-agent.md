# DevOps / SRE Agent Configuration

## Role Description

The DevOps Agent is your embedded SRE teammate — it monitors infrastructure health, triages incidents, analyzes logs, tracks deployment health, and automates routine operations tasks. It connects to your observability stack, CI/CD pipelines, cloud providers, and incident management tools to provide a real-time operational picture without requiring you to context-switch between dashboards. The agent responds to both scheduled health checks and ad-hoc queries like "show me error rates for the payment service in the last hour" or "what changed in the last deploy that might cause the latency spike?"

This agent is designed for engineering teams that want proactive operational intelligence without adding headcount. It surfaces issues before they become outages, correlates deployment events with metric anomalies, and accelerates root-cause analysis by pulling relevant logs and recent changes automatically.

## Recommended Model

**Claude Sonnet 4** or **DeepSeek V3** — DevOps work requires precise technical reasoning, log pattern recognition, and the ability to correlate events across multiple systems. Both models excel at structured analysis and can parse JSON logs, stack traces, and infrastructure-as-code. For always-on monitoring and simple alert classification, **Claude Haiku** is cost-effective and fast.

## Key Skills to Load

- `infra-health` — CPU, memory, disk, network across instances; anomaly detection; capacity forecasting
- `deployment-monitor` — Deployment success rate, rollback frequency, lead time for changes, change failure rate
- `incident-response` — Alert triage, runbook execution, stakeholder notification, post-incident timeline generation
- `log-analysis` — Error pattern detection, log correlation across services, spike detection, slow-query surfacing
- `ssl-cert-monitor` — Certificate expiration tracking, renewal reminders
- `cost-optimization` — Cloud spend anomalies, underutilized resources, reserved instance coverage gaps

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **PostgreSQL / MSSQL / MongoDB** | Database health, slow queries, connection pools, replication lag |
| **Stripe** | Payment infrastructure health, failure rates (if applicable) |
| **Slack** | Incident alerts, deployment notifications, daily health reports |
| **Email** | On-call notifications, vendor alerts, SSL renewal reminders |
| **GA4 / PostHog** | Application-side error tracking, user-facing error rates |

> **Note:** Cloud provider APIs (AWS CloudWatch, GCP Monitoring, Azure Monitor), CI/CD platforms (GitHub Actions, GitLab CI, CircleCI), and observability tools (Datadog, Grafana, PagerDuty) are accessed via custom skills and API integrations. Configure these in your Hermes profile's `tools` section.

## Sample Cron Schedule

```cron
# Infrastructure health check every 15 minutes
*/15 * * * * hermes skill infra-health --alert-on anomaly

# Database health every 30 minutes
*/30 * * * * hermes skill infra-health --target databases --metrics slow_queries,connections,replication_lag

# Daily deployment report at 9:00 AM
0 9 * * 1-5 hermes skill deployment-monitor --period last_24h

# SSL certificate check every Monday at 8:00 AM
0 8 * * 1 hermes skill ssl-cert-monitor

# Weekly cost optimization scan every Friday at 3:00 PM
0 15 * * 5 hermes skill cost-optimization

# Log error spike check every hour
0 * * * * hermes skill log-analysis --spike-check --period 1h
```

## Quick-Start Command

```bash
hermes agent create devops \
  --model claude-sonnet-4 \
  --skills infra-health,deployment-monitor,incident-response,log-analysis,ssl-cert-monitor,cost-optimization \
  --connectors postgres,slack,email \
  --profile devops \
  --description "Infrastructure monitoring and SRE operations agent"
```

## Daily Workflow

The agent runs infrastructure health checks every 15 minutes, alerting on CPU/memory/disk anomalies with context about recent deploys or traffic changes. Every morning it delivers a deployment health report showing what shipped in the last 24 hours, any rollbacks, and whether DORA metrics are trending up or down. During incidents, it automatically pulls relevant logs from the window surrounding the alert, identifies recent deployments or config changes, and drafts an incident timeline. On Fridays, it scans for cost optimization opportunities — idle load balancers, oversized instances, unattached volumes.

## Configuration Notes

Define your alert routing rules (which severity goes to which Slack channel or on-call rotation) in canonical facts. Store runbook URLs and escalation policies so the agent can include them in incident notifications. Configure log sources and their locations. Set anomaly detection thresholds per service — a 10% CPU spike on a batch worker means something very different from the same spike on a customer-facing API.

## Extending

Add `chaos-engineering` for scheduled GameDays. Integrate with Terraform or Pulumi state for infrastructure drift detection. Add `dependency-health` to monitor upstream API dependencies. Build a `capacity-planner` that forecasts resource needs based on growth trends.
