# Hermes Best Practices: Overview

Welcome to the Hermes community best practices guide. This document and its companion guides capture what we've learned about building reliable, secure, and maintainable Hermes setups. Whether you're running your first cron or managing a team deployment, these practices help you avoid the mistakes we've already made.

## How to Use This Guide

Each best-practices document stands alone — read the ones relevant to your current work. The anti-patterns section below is a quick reference for what not to do. The maturity model helps you assess where you are and where to go next.

## The Core Principles

**Explicit over implicit.** Hermes should do what you told it to do, not what it guessed you meant. Explicit tools, explicit permissions, explicit confirmations. The best Hermes setup is the one where you never wonder "why did it do that?"

**Observable over magical.** Every automated decision should be traceable. Every cron should log its work. Every skill invocation should leave an audit trail. Debugging a Hermes pipeline should be a matter of reading logs, not guessing.

**Composable over monolithic.** Small, focused skills compose into powerful workflows. A single "do everything" skill is brittle. Five well-scoped skills that chain together are flexible and testable.

**Least privilege by default.** Start with read-only access. Add write capabilities only when the use case demands it. Add approval gates before write capabilities go live. It's easier to loosen permissions than to recover from over-privileged automation.

## Anti-Patterns Quick Reference

These patterns cause the majority of production incidents. Avoid them.

| Anti-Pattern | Why It Hurts | What to Do Instead |
|-------------|-------------|-------------------|
| Hardcoded credentials in skills | Breach on first share | Secrets manager or env vars |
| God crons that do everything | One failure cascades | Single-responsibility crons |
| Silent error swallowing | False confidence | Alert on persistent failure |
| No approval on write ops | Unintended external actions | Tiered confirmation gates |
| Unbounded database queries | Timeouts, resource exhaustion | Pagination and limits |
| Memory as dumping ground | Context pollution, staleness | Curated, pruned memories |
| Copy-pasted skill logic | Bug propagation | Shared utility skills |
| Console-only logging | No audit trail | Structured persistent logging |
| Auto-updating dependencies | Supply-chain risk | Version pinning in production |
| Model selection by habit | Cost/latency waste | Task-aware model routing |

## Maturity Model

Use this to assess your Hermes adoption and plan next steps.

### Level 1: Getting Started

- Running ad-hoc queries through the chat interface
- No persistent memory or skills configured
- One or two connectors authenticated (email, calendar)
- Manual model selection, default settings
- **Next step:** Identify one repeatable task to turn into a skill

### Level 2: Structured Usage

- 3-5 skills for common workflows
- Basic memory configured (user preferences, project context)
- Connectors for major data sources
- Manual cron execution (run the skill daily/weekly)
- Logs reviewed when something breaks
- **Next step:** Automate the most valuable recurring task with cron

### Level 3: Automated Operations

- Scheduled crons for monitoring, reporting, and routine tasks
- Tiered model selection (small models for classification, frontier for reasoning)
- Error handling with retry and alerting
- Skills published within your team with documentation
- Approval gates on all write operations
- **Next step:** Implement cross-team skill sharing and review process

### Level 4: Team-Scale Deployment

- 15+ production skills maintained by multiple team members
- Automated model selection with fallback chains
- Comprehensive monitoring and alerting for all crons
- Audit logging reviewed weekly
- Credential rotation on a documented schedule
- Community contribution (publishing skills, reporting issues)
- **Next step:** Contribute to MCP server ecosystem, mentor new users

### Level 5: Platform Integration

- Hermes integrated into CI/CD, deployment, and incident response pipelines
- Custom MCP servers for internal systems
- Team-wide memory management with shared context
- Capacity planning and cost optimization
- Security compliance reviews per quarter
- Active community participation (skill reviews, documentation, support)
- **Next step:** Publish case studies, speak at community events, shape the roadmap

## Navigating the Best Practices

- **[Cron Design](cron-design.md):** Idempotency, error handling, rate limiting, monitoring
- **[Model Selection](model-selection.md):** When to use which model, cost optimization, fallback chains
- **[Memory Management](memory-management.md):** Memory systems, compaction, context optimization
- **[Security](security.md):** Token management, least privilege, approval gates, audit logging
- **[Skill Development](skill-development.md):** Skill design, testing, documentation, lifecycle
- **[MCP Design](mcp-design.md):** Server development, tool design, error handling, testing

## Community Values

The Hermes community thrives on:

**Generosity.** Share what you build. A skill that helps you probably helps others. A bug report saves someone else hours.

**Honesty.** If a best practice doesn't work for your use case, say so. The guides improve through real-world feedback, not theoretical agreement.

**Inclusivity.** Good automation works for everyone on the team — technical and non-technical, new hires and veterans. Design skills with clear documentation and intuitive trigger patterns.

**Pragmatism.** The perfect is the enemy of the deployed. A skill that works today and saves time is better than a theoretically perfect skill that ships next quarter. Iterate.

Start where you are, automate what hurts most, and share what you learn. The rest follows.
