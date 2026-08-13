---
title: Anthropic Cybersecurity Skills Setup Guide
description: Install and configure mukul975/Anthropic-Cybersecurity-Skills — 750+ MITRE-mapped security skills for AI agents including threat detection, incident response, and vulnerability assessment.
category: security
publisher: mukul975
skills_count: 750+
maturity: production
source: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anthropic-cybersecurity-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Anthropic Cybersecurity Skills — Setup Guide

750+ MITRE-mapped cybersecurity skills for AI agents by [mukul975](https://github.com/mukul975/Anthropic-Cybersecurity-Skills). The largest domain-specific skill pack discovered — production-grade threat detection, incident response, vulnerability assessment, and security operations workflows. All skills mapped to the MITRE ATT&CK framework.

## What It Provides

- **Threat Detection** — 200+ skills for identifying active threats across network, endpoint, and cloud
- **Incident Response** — 150+ skills for triage, containment, eradication, and recovery
- **Vulnerability Assessment** — 120+ skills for scanning, prioritizing, and validating vulnerabilities
- **Security Operations** — 100+ skills for SIEM, SOAR, log analysis, and alert triage
- **Compliance & Audit** — 80+ skills for SOC 2, ISO 27001, HIPAA, PCI-DSS
- **Cloud Security** — 50+ skills for AWS, GCP, Azure security posture
- **MITRE ATT&CK Mapping** — every skill tagged with MITRE technique ID

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/mukul975/Anthropic-Cybersecurity-Skills

# Or manually — clone the full repo (large: 750+ skills)
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git ~/.hermes/skills/cybersecurity

# Install specific skill categories only (recommended for smaller footprint)
npx skills add https://github.com/mukul975/Anthropic-Cybersecurity-Skills --skill threat-detection
npx skills add https://github.com/mukul975/Anthropic-Cybersecurity-Skills --skill incident-response
```

## Skill Categories

| Category | Count | MITRE Coverage |
|----------|-------|---------------|
| Threat Detection | 200+ | TA0001-TA0011 |
| Incident Response | 150+ | IR phases 1-4 |
| Vulnerability Assessment | 120+ | CVE/CWE mapped |
| Security Operations | 100+ | SOC workflows |
| Compliance & Audit | 80+ | Framework-specific |
| Cloud Security | 50+ | CSPM/CWPP |

## Configuration

```yaml
cybersecurity:
  enabled_categories:
    - threat-detection
    - incident-response
    - vulnerability-assessment
  mitre_framework_version: "v15"
  severity_threshold: "medium"     # only load skills for medium+ severity
  scan_frequency: "daily"
  alert_destination: "siem"        # or "slack", "email", "pagerduty"
```

## Key Workflows

### Run a threat scan

```
Run a threat detection scan on our AWS environment. Check for:
- Exposed S3 buckets
- Unused IAM access keys
- Security groups with 0.0.0.0/0
```

### Incident triage

```
A suspicious login was detected from an unusual location.
Run the incident-response/triage skill to analyze the event
and recommend containment actions.
```

### Vulnerability prioritization

```
Scan our dependency tree for known CVEs.
Prioritize by CVSS score and exploitability.
```

## Verification

```bash
# List installed cybersecurity skills
hermes skills list | grep -i "threat\|incident\|vulnerability"

# Test a basic scan
hermes chat -q "Run a quick security posture check on this environment"
```

## Pitfalls

- **⚠️ Production systems**: These skills can run destructive actions (blocking IPs, revoking keys, terminating instances). Always run in `--dry-run` mode first on production environments.
- **⚠️ API scope**: Cloud security skills need broad read permissions. Use read-only IAM roles where possible. Never use admin credentials for automated scanning.
- **Large install size**: The full pack is 750+ skills. Install only the categories you need. Use the `--skill` flag for selective install.
- **False positives**: Automated threat detection can generate noise. Tune the `severity_threshold` and always review findings before automated remediation.
- **MITRE version**: Skills are mapped to MITRE ATT&CK v15. If your org uses a different version, verify mapping accuracy.

## See Also

- [mukul975/Anthropic-Cybersecurity-Skills repo](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Trail of Bits Security Setup](/hermes/skills/catalog/trailofbits-security-setup/)
- [OpenClaw Security Hardening](/hermes/skills/catalog/openclaw-security-hardening-setup/)

---

*Setup guide by CorpusIQ. Source: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills).*
