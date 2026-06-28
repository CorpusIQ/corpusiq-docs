---
title: OpenClaw Security Hardening — Security Suite Setup Guide
description: Setup guide for the openclaw-security-hardening skill — lock down your OpenClaw agent with automated security audits, file permission hardening, and network restriction profiles.
last_updated: 2026-06-28
---

# OpenClaw Security Hardening — Security Suite

**Publisher:** [aradotso/security-skills](https://skills.sh/aradotso/security-skills) | **Installs:** 874 | **Category:** Security

Automated security hardening for OpenClaw agents. Audits file permissions, network exposure, environment variables, and skill configurations — then applies security best practices. Ships with companion [openclaw-security-watchdog](https://skills.sh/aradotso/security-skills/openclaw-security-watchdog) (761 installs) for continuous monitoring.

## Prerequisites

- OpenClaw installed and running
- macOS or Linux (file permission hardening is OS-specific)
- Node.js 18+
- `npx` available

## Installation

Install both the hardening tool and watchdog together:

```bash
npx skills add aradotso/security-skills/openclaw-security-hardening
npx skills add aradotso/security-skills/openclaw-security-watchdog
```

## Configuration

```json
{
  "security": {
    "hardening": {
      "filePermissions": true,
      "envScanning": true,
      "networkRestriction": true,
      "skillAudit": true,
      "strictMode": false
    },
    "watchdog": {
      "enabled": true,
      "scanInterval": "1h",
      "alertOnViolation": true,
      "autoFix": false
    }
  }
}
```

| Setting | Default | Description |
|---------|---------|-------------|
| `filePermissions` | `true` | Lock down config files to owner-only |
| `envScanning` | `true` | Scan environment for hardcoded secrets |
| `networkRestriction` | `true` | Audit outbound network access |
| `skillAudit` | `true` | Review installed skills for known vulnerabilities |
| `strictMode` | `false` | Enforce all findings (may break some integrations) |
| `watchdog.autoFix` | `false` | Auto-apply fixes (set `true` for production) |

## Capabilities

### File Permission Hardening

- Scans `~/.openclaw/`, skill directories, and config files
- Sets owner-only permissions (600/700) on sensitive files
- Detects world-readable tokens, keys, and secrets
- Flags config files with group/other read access

### Environment Scanning

- Checks for hardcoded API keys in environment variables
- Flags passwords and tokens in shell config files
- Detects `.env` files with world-readable permissions
- Recommends migration to secret managers

### Network Restriction

- Audits which domains the agent connects to
- Flags connections to untrusted/unexpected hosts
- Recommends allowlisting for production agents
- Detects plaintext (non-TLS) connections

### Skill Audit

- Scans installed skills for known vulnerability patterns
- Checks skill permissions and access scopes
- Flags skills with excessive filesystem/network access

## CLI Reference

```
Command                           Description
──────────────────────────────────────────────────
security-hardening audit          Run full security audit
security-hardening apply          Apply hardening recommendations
security-hardening permissions    Audit file permissions only
security-hardening env-scan       Scan for hardcoded secrets
security-hardening network        Audit network access

security-watchdog start           Start continuous monitoring
security-watchdog status          Show current security posture
security-watchdog alerts          View recent alerts
```

## CorpusIQ Use Cases

- **Production agent deployment:** Run hardening audit before deploying any agent to production
- **Compliance preparation:** Generate security posture reports for SOC 2 / ISO 27001 audits
- **Multi-tenant environments:** Ensure agent boundaries between customer data partitions
- **Incident response:** Watchdog alerts on unexpected file modifications or network connections

## Troubleshooting

### Audit found too many issues

```bash
# Start without strict mode
security-hardening audit --strict=false

# Apply only critical findings first
security-hardening apply --severity=critical

# Review each finding interactively
security-hardening audit --interactive
```

### Permission hardening broke a skill

```bash
# Check which file was locked down
security-hardening permissions --verbose

# Restore permissions on specific path
chmod 755 ~/.openclaw/skills/<skill-name>

# Add exception to config
```

### Watchdog false positives

```bash
# Add allowed domains
security-watchdog allowlist --add api.trusted-service.com

# Tune scan sensitivity
security-watchdog config --sensitivity=medium
```

---

*← [Security Hardening Setup Guide](/hermes/skills/catalog/openclaw-security-hardening-setup/) | [Discovery Page](/hermes/skills/marketplace/new-june28-2026/) →*

*↑ [Skills Catalog](/hermes/skills/catalog/)*

---

*Part of the Hermes Skills Library — curated by CorpusIQ. Content remains attributed to original authors and repositories. [CorpusIQ](https://corpusiq.io) — one MCP endpoint, all your business tools.*
