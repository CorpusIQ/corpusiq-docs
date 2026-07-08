---
title: Security Best Practices for Hermes Agent  --  Credentials, Approval Gates & Audit
description: Hermes Agent security best practices. Token and credential management, least-privilege access, tiered approval gates, audit logging, secrets management, plugin verification, and operational security checklist.
category: best-practices
tags: [hermes-agent, security, credentials, approval-gates, audit-logging, least-privilege, token-management, secrets]
last_updated: 2026-07-08
---

# Security Best Practices  --  Protect Your Hermes Agent Deployment

Hermes Agent connects to your data, executes code, and runs scheduled tasks  --  all capabilities that require thoughtful security design. These security best practices cover credential management, approval gates, audit logging, and the patterns that prevent the most common security failures in production AI agent deployments.

## Overview

Security with Hermes Agent follows the [least-privilege principle](/hermes/best-practices/): start read-only, add write capabilities only with explicit approval gates, and log everything. Each connector to external services (email, CRM, databases) is a potential attack surface  --  managing tokens and permissions correctly is non-negotiable.

## How It Works

### Credential Management

**Never hardcode credentials** in skills, crons, or prompt templates. Use environment variables or a secrets manager. A skill reading `api_key = "sk-abc123"` is a breach waiting to happen.

**Least privilege for every connector.** Grant only the permissions Hermes Agent actually needs. Read-only Gmail scope, SELECT-only database role, scoped API keys with explicit boundaries.

**Rotate credentials quarterly.** Document rotation procedures so it's a 5-minute task, not a fire drill.

**No shared API keys.** Each team member needs their own credentials for audit trails and individual revocation.

### Tiered Approval Gates

| Tier | Type | Approval Required | Examples |
|---|---|---|---|
| Tier 0 | Read-only | None | Queries, reports, analysis |
| Tier 1 | Internal write | One-click confirm | Draft docs, internal notes |
| Tier 2 | External write | Explicit confirmation + preview | Sending emails, posting messages |
| Tier 3 | High-impact | Multi-step with reason capture | Financial transactions, bulk changes |

### Audit Logging

Log every significant action: what was done, by whom, when, with what inputs, and the result. Use structured logging (JSON), not free-text. Store logs in append-only storage for 30-90 days minimum. Schedule weekly log reviews or set up automated anomaly detection.

### Secrets and Sensitive Data

**Never store in memory/context:** API keys, passwords, credit card numbers, PII, auth tokens, private keys. Strip sensitive fields before data enters model context. Redact PII in logs.

## Operational Security Checklist

- [ ] All credentials in secrets manager, never in version control
- [ ] Each connector uses scoped, least-privilege credentials
- [ ] Write operations require confirmation gates
- [ ] Audit logging enabled and reviewed weekly
- [ ] Sensitive data stripped before model context
- [ ] Community skills reviewed before installation
- [ ] Credentials rotate on documented schedule
- [ ] Logs stored append-only and immutable
- [ ] Anomalous activity triggers alerts

## Benefits

- **Breach prevention**: Hardened credential management eliminates the #1 attack vector
- **Compliance ready**: Audit logging satisfies SOC 2, HIPAA, and internal review requirements
- **Safe automation**: Approval gates let you automate writes without losing control
- **Revocable access**: Individual credentials mean you can cut off one user without disrupting the team

## FAQ

### How do I manage API keys securely with Hermes Agent?
Never hardcode keys in skills or prompts. Use environment variables, a secrets manager, or the built-in credential store. Each connector should use scoped keys with only the permissions Hermes Agent needs  --  prefer read-only where possible.

### What actions require human approval in Hermes Agent?
Any write operation that affects external systems: sending emails, updating CRM records, modifying databases, posting to Slack, executing financial transactions. Configure [tiered approval gates](security.md#tiered-approval-gates) appropriate to the risk level.

### How often should I rotate Hermes Agent credentials?
Rotate API keys and tokens quarterly at minimum. Document the rotation procedure for each connector so it's a quick task. Set calendar reminders  --  expired tokens are the #1 cause of silent automation failures.

## Related Pages

- [Best Practices Overview](/hermes/best-practices/)  --  All guides
- [Cron Design](cron-design.md)  --  Secure scheduled automation
- [Memory Management](memory-management.md)  --  Don't store secrets in memory
- [MCP Integration Guide](/hermes/mcp/)  --  Connector authentication
- [Troubleshooting](/hermes/troubleshooting/)  --  Fix OAuth token expiry
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
