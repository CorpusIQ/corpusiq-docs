---
title: "NemoClaw User Guide — Security Setup"
description: Install and use the NemoClaw security user guide from nvidia/skills (99 installs). Enterprise-grade security best practices for autonomous Hermes agent deployments.
---

# NemoClaw User Guide — Setup Guide

**Source:** [nvidia/skills](https://skills.sh/nvidia/skills) (99 installs)
**Category:** Security & Governance

A security-focused user guide for NemoClaw — a hardened OpenClaw variant providing permission models, audit logging, and secure execution boundaries for Hermes agents. Published by NVIDIA, signaling enterprise validation of the Hermes/OpenClaw agent ecosystem. Covers security best practices for deploying autonomous agents in production environments.

---

## Installation

```bash
npx skills add nvidia/skills --skill nemoclaw-user-guide
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ with OpenClaw runtime support |
| **NemoClaw Runtime** | Installed alongside the skill — provides the hardened execution layer |
| **Audit Log Storage** | Local directory or S3 bucket for agent audit trails |

---

## Key Capabilities

### Security Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Permission gates | Configured in `~/.hermes/config.yaml` | Fine-grained tool access control |
| Audit logging | Automatic — all agent actions logged | JSONL format, S3-compatible storage |
| Execution sandboxing | Enabled by default | Prevents unauthorized filesystem/network access |
| Security policy review | "Review my agent security policy" | Hardening recommendations |
| Threat detection | "Scan for security misconfigurations" | Checks permission model, env exposure, credential hygiene |

### CLI Command Reference

```bash
# Run security audit on current agent config
hermes nemoclaw audit

# View recent security events
hermes nemoclaw events --last 24h

# Apply recommended hardening
hermes nemoclaw harden --apply
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Production Agent Security** | Apply NemoClaw permission gates to CorpusIQ growth agents before production deployment |
| **Compliance Auditing** | Use audit logs for SOC 2 / security review evidence |
| **Credential Hygiene** | Automated scanning prevents credential leakage in agent output |
| **Permission Hardening** | Restrict agent tool access to minimum required for each workflow |
| **Incident Response** | Audit trails enable forensic analysis of agent actions |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "Permission denied" on legitimate tool | Check `~/.hermes/config.yaml` nemoclaw rules — add explicit allow |
| Audit log grows too large | Configure log rotation: `nemoclaw config set --log-rotation 7d` |
| "NemoClaw runtime not found" | Reinstall: `npx skills add nvidia/skills --skill nemoclaw-user-guide --force` |

## Verification

```bash
# Verify skill installed
hermes skills list | grep nemoclaw-user-guide

# Run security audit
hermes nemoclaw audit

# Check audit logging is active
hermes nemoclaw status
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 28 Discovery](/hermes/skills/marketplace/new-june28-2026/) →*
*Powered by CorpusIQ*
