---
title: "Setup Guide: cantinaxyz/clawdstrike — Agent Red-Team Security Testing (486 Installs)"
description: "Complete setup guide for clawdstrike: automated vulnerability scanning and security testing for Hermes/OpenClaw agent deployments."
---

# Setup Guide: cantinaxyz/clawdstrike

**Red-team security testing for agent deployments — automated vulnerability scanning.**

## Quick Install

```bash
npx skills add cantinaxyz/clawdstrike/clawdstrike
```

## Prerequisites

- Hermes Agent or OpenClaw installed
- Node.js 18+ (for `npx skills`)
- Security testing mindset — this skill actively probes for vulnerabilities
- **Important**: Run only on systems you own or have explicit permission to test

## What It Does

Clawdstrike performs automated security assessments of agent deployments:

- **Permission Audit**: Checks agent file system, network, and tool access scopes
- **Token Exposure Scan**: Identifies accidentally exposed API keys and credentials
- **Command Injection Tests**: Probes for unsafe command execution patterns
- **Configuration Hardening**: Validates agent config against security best practices
- **Network Exposure**: Checks for unintentionally exposed services and ports

## Configuration

```yaml
# ~/.hermes/config.yaml
skills:
  clawdstrike:
    scan_depth: "standard"      # standard | deep | full
    report_format: "markdown"    # markdown | json | html
    auto_fix: false              # Set true to auto-apply fixes (careful!)
    exclude_paths:
      - "/proc/*"
      - "/sys/*"
    notify_on_critical: true
```

## Scan Levels

| Level | Duration | Checks |
|-------|:--------:|--------|
| **standard** | ~30s | Permission audit, token scan, basic config check |
| **deep** | ~2min | Standard + command injection tests, network scan |
| **full** | ~5min | Deep + dependency audit, file permission crawl |

## Use Cases

1. **Pre-deployment audit**: Run before deploying agent to production
2. **Periodic security scan**: Weekly automated scans with report to admin
3. **Post-incident review**: After a security event, assess what was exposed
4. **Configuration drift detection**: Compare current config against known-good baseline

## Sample Output

```
🔴 CRITICAL: API key found in session logs
  File: ~/.hermes/sessions/session-1234.json
  Key: sk-*** (OpenAI)
  Fix: Rotate key immediately, enable session log sanitization

🟡 WARNING: Agent has write access to ~/.ssh/
  Risk: SSH key exfiltration
  Fix: Restrict file tool to specific directories

🟢 PASS: All tool permissions properly scoped
🟢 PASS: No open network ports detected
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Scan hangs | Large file system | Use `standard` depth, add exclusions |
| False positives on token scan | Legitimate config patterns | Add to `token_scan_exclusions` |
| Network scan blocked | No `nmap` installed | Install nmap or use basic scan only |
| Auto-fix broke config | Overly aggressive fixes | Restore from backup, disable `auto_fix` |

## CorpusIQ Integration

- **Governance gate**: Run clawdstrike as part of the CorpusIQ governance preflight checks
- **Cron integration**: Weekly automated scan → Telegram alert on findings
- **Compliance**: Report output feeds into security audit trail

---

*← [Clawdirect Setup](/hermes/skills/catalog/clawdirect-setup/) | [Marketplace Home →](/hermes/skills/marketplace/)*

*↑ [Skills Catalog](/hermes/skills/catalog/)*
