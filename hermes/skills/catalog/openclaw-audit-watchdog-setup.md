---
title: "OpenClaw Audit Watchdog — Setup Guide"
description: "Install and configure the openclaw-audit-watchdog from prompt-security/clawsec — security auditing and misconfiguration detection for Hermes/OpenClaw agent deployments."
last_updated: 2026-07-08
---

# OpenClaw Audit Watchdog — Setup Guide

Security auditing and monitoring skill for Hermes and OpenClaw agent deployments. Detects misconfigurations, monitors for suspicious activity, and generates security reports — keeping your agent infrastructure secure.

**Publisher:** [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | **Installs:** 665 | **Source:** [skills.sh](https://skills.sh/prompt-security/clawsec/openclaw-audit-watchdog)

## 1. Prerequisites

- Hermes Agent or OpenClaw installed
- Node.js 18+ (for `npx skills` CLI)
- Skills CLI: `npm install -g skills` or use `npx skills`
- Access to agent configuration files (read-only for audit)

## 2. Installation

```bash
# Install from the clawsec security suite
npx skills add prompt-security/clawsec --skill openclaw-audit-watchdog
```

Verify installation:
```bash
npx skills list | grep audit-watchdog
```

## 3. Capabilities

The watchdog provides continuous security monitoring for agent deployments:

- **Misconfiguration Detection** — Scans agent configs for insecure settings (exposed ports, weak auth, debug mode in production)
- **Suspicious Activity Monitoring** — Detects unusual agent behavior patterns (unexpected network calls, excessive filesystem access)
- **Security Reports** — Generates human-readable security audit reports
- **Remediation Suggestions** — Provides specific fixes for each finding
- **Compliance Checks** — Validates against security best practices for AI agent deployments

## 4. Usage Examples

### Run a Full Audit
```
> audit my agent deployment for security issues
```

### Check Specific Config
```
> check if any agent configs have debug mode enabled or expose ports to 0.0.0.0
```

### Generate Report
```
> generate a security audit report for the last 7 days of agent activity
```

## 5. CorpusIQ Use Cases

This skill is critical for CorpusIQ's multi-agent infrastructure:

- **Agent fleet security** — Audit all 15+ CorpusIQ agents for misconfigurations
- **Pre-deployment checks** — Run before deploying new agent skills or connectors
- **Compliance validation** — Ensure agent deployments meet security standards before client onboarding
- **Incident response** — Detect unusual agent behavior that could indicate a compromise

## 6. Related Skills

- [OpenClaw Security Hardening](/hermes/skills/catalog/openclaw-security-hardening-setup/) — Hardening configurations (874 installs)
- [OpenClaw Audit Watchdog](/hermes/skills/catalog/openclaw-audit-watchdog-setup/) — Security auditing and misconfiguration detection (665 installs)
- [Hermes Flight Recorder](/hermes/skills/catalog/hermes-flight-recorder-setup/) — Agent activity logging

## 7. Troubleshooting

| Issue | Fix |
|-------|-----|
| `npx skills` not found | `npm install -g skills` or use `npx -y skills` |
| Audit returns no results | Ensure agent config files are accessible (check file permissions) |
| False positives on dev configs | The skill distinguishes prod vs dev — tag your configs appropriately |

---

*Part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered in the [June 28, 2026 evening sweep](/hermes/skills/marketplace/new-june28-2026-update2/).*

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
