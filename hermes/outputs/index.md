# Hermes Agent Outputs & Implementation Guide

Welcome to the Hermes Agent field manual. This section shows you what Hermes can do in practice — not through feature lists or marketing claims, but through concrete, copy-paste-ready implementations organized by industry, company size, and workflow pattern. Every guide here includes real cron schedules, real skill patterns, and real integration examples you can adapt and deploy.

## What You'll Find Here

This isn't documentation about Hermes. It's documentation for *using* Hermes — patterns that work, automations that pay for themselves in the first week, and architectures that scale from solo founder to enterprise.

### By Industry (Case Studies)

Each industry case study covers the specific workflows, compliance requirements, and tool integrations that matter in that domain. They include exact cron schedules, skill descriptions, and data source configurations.

| Case Study | What You'll Learn |
|------------|-------------------|
| [Compliance & Audit](case-studies/compliance-audit.md) | SOC 2 evidence collection, HIPAA audit trails, GDPR compliance checks, change management monitoring, and continuous reporting for audit readiness |
| [Healthcare](case-studies/healthcare.md) | Patient record management, appointment scheduling, insurance verification, lab result notification, and HIPAA-compliant agent workflows with privacy-first patterns |
| [Financial Services](case-studies/financial-services.md) | Portfolio monitoring and drift detection, daily transaction reconciliation, fraud pattern detection, regulatory filing automation, and market data integration |
| [Manufacturing](case-studies/manufacturing.md) | Supply chain monitoring, inventory reorder automation, quality control with SPC rules, equipment maintenance scheduling, and IoT sensor integration patterns |
| [Real Estate](case-studies/real-estate.md) | Multi-platform listing syndication, lead qualification and routing, market analysis automation, showing coordination, and transaction milestone tracking |
| [Professional Services](case-studies/professional-services.md) | Client onboarding orchestration, calendar-to-timesheet automation, project budget burn monitoring, invoice generation, and weekly client status reporting |
| [Customer Support](case-studies/customer-support.md) | Multi-channel ticket triage, knowledge base search integration, real-time SLA monitoring with escalation, intelligent routing, and customer health signal detection |
| [Revenue Operations](case-studies/revenue-operations.md) | Pipeline hygiene enforcement, weighted forecasting, commission calculation, cross-source revenue reconciliation, and marketing-to-sales handoff tracking |

### By Company Size

The same Hermes Agent adapts to vastly different environments. These guides cover the patterns, infrastructure, and governance appropriate to your stage.

| Guide | For Teams Of | Focus |
|-------|-------------|-------|
| [Startup](by-company-size/startup.md) | 1-50 employees | Solo founder patterns, essential crons, scrappy setup with free tiers, doing more with less, scaling automation with your company |
| [Mid-Market](by-company-size/mid-market.md) | 50-500 employees | Multi-team orchestration, departmental profiles, approval workflows, shared infrastructure, governance without bureaucracy |
| [Enterprise](by-company-size/enterprise.md) | 500+ employees | Security compliance, multi-region deployment, segregation of duties, change management integration, audit-grade logging, framework-specific compliance (SOC 2, HIPAA, GDPR, SOX) |

### Workflow Templates

Ready-to-deploy cron + skill templates for the most common automation needs.

[**Copy-Paste Cron Templates**](workflows/templates.md) — A field guide of YAML cron configurations you can drop into `~/.hermes/cron/` today. Covers:

- **Email monitoring:** Support inbox triage, vendor invoice detection, lead alert monitoring
- **Report generation:** Daily executive summary, weekly business review, monthly close package
- **Data sync:** CRM-to-billing reconciliation, database-to-analytics validation, multi-platform listing sync
- **Alerting:** Metric anomaly detection, SLA breach warnings, system health checks
- **Integration-specific:** Stripe revenue monitoring, GA4 traffic anomaly detection, CRM pipeline health

Each template includes the cron schedule, skill description, data sources, and output destination. Replace the placeholder values with your own and deploy.

## How to Use These Guides

### If You're New to Hermes Agent

1. **Start with the Startup guide** regardless of your company size — it covers the fundamentals of building your first automations.
2. **Read the Workflow Templates next** — pick one template that solves your most painful manual task and deploy it today.
3. **Then explore the case study for your industry** — it'll show you patterns specific to your domain.

### If You're Scaling Your Usage

1. **Read the company-size guide that matches your current stage** — the patterns change meaningfully between startup, mid-market, and enterprise.
2. **Browse case studies outside your industry** — patterns from manufacturing apply to supply chain in any business; patterns from financial services apply to any reconciliation problem.
3. **Use the templates as a starting point** — they're designed to be adapted, not adopted wholesale.

### If You're Evaluating Hermes for Your Team

1. **Find your industry case study** — map the documented automations to your team's current manual processes.
2. **Read the company-size guide for your stage** — understand the operational overhead and governance patterns.
3. **Estimate time recovery** — each documented automation typically replaces 2-10 hours/week of manual work.

## What Hermes Agent Automates

Across all these guides, certain patterns recur. Hermes Agent consistently automates:

**Cross-system reconciliation.** Matching data between tools that should agree but don't — CRM vs. billing, database vs. analytics, purchase orders vs. shipments. This is the single highest-value automation category for most organizations.

**Monitoring and alerting.** Continuous checking of metrics, statuses, and deadlines with intelligent escalation. Hermes doesn't just detect problems — it provides the context needed to resolve them.

**Report generation.** Compiling data from multiple sources into structured, scheduled reports. Morning summaries, weekly reviews, monthly close packages — Hermes produces them on schedule without anyone remembering to run them.

**Workflow orchestration.** Moving data through multi-step processes: onboarding sequences, approval chains, escalation paths. Hermes connects the systems so people don't have to.

**Compliance evidence.** Continuous collection of configuration snapshots, access logs, and control evidence. Audit readiness as a byproduct of operations rather than a quarterly fire drill.

## The Architecture Behind These Patterns

Every guide in this section leverages the same Hermes Agent primitives:

- **Cron schedules:** Standard cron expressions drive all scheduled automations. From every-5-minute triage to monthly close reports.
- **Skills:** Reusable automation routines that query data sources, apply logic, and produce output. Skills are plain files in `~/.hermes/skills/`.
- **MCP Connectors:** Hermes connects to your existing tools through the Model Context Protocol. Database connectors (PostgreSQL, MSSQL, MongoDB), SaaS connectors (HubSpot, Stripe, GA4, Slack, Gmail, and dozens more), and file connectors (Google Drive, OneDrive, Dropbox) — all available without custom integration work.
- **Profiles:** Isolated environments for different teams, departments, or compliance boundaries. Each profile has its own skills, crons, and connector configurations.
- **Alert routing:** Skills deliver output to Slack channels, email addresses, Google Drive folders, or ticketing systems — wherever your team works.

## Contributing Your Patterns

These guides represent patterns that work across industries and company sizes. If you've built a Hermes automation that solved a real problem, consider sharing the pattern. The community grows stronger with every documented use case.

## Next Steps

Pick one guide that matches your situation and build your first automation in the next hour. Start with monitoring (Hermes tells you something needs attention), graduate to suggestions (Hermes proposes an action), and eventually reach autonomous execution for well-proven patterns.

The distance between reading about automation and having automation running is one cron job. Start there.
