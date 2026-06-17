---
title: June 12, 2026 (Update) — OpenClaw Security Suite
description: "Afternoon sweep: 13-skill OpenClaw security suite discovered from useai-pro (UseClawPro). Flagship skill-vetter at 19,340 installs."
---

# June 12, 2026 (Update) — OpenClaw Security Suite

Afternoon sweep surfaced the **`useai-pro/openclaw-skills-security`** repository from **UseClawPro** (UseAI.pro): a complete 13-skill security suite for the OpenClaw ecosystem. The flagship `skill-vetter` has **19,340 installs** — one of the highest-install Hermes/OpenClaw skills discovered to date.

All 13 skills are instruction modules (`SKILL.md`) — they don't run on their own. Load them into a host agent (Hermes Agent / Claude Code / Codex CLI / OpenClaw) or paste into any LLM chat. Trust scores range from 93–98. All skills audited Feb–Mar 2026. AGPL-3.0-or-later licensed.

*Previously cataloged: 337 total (89 native + 248 marketplace). This update adds 13 → 350 total.*

---

## useai-pro/openclaw-skills-security — Security Suite (13 skills)

Security-first instruction modules maintained by UseClawPro. Each skill is a focused module covering one security domain. Load individually or chain them together for a full security pipeline.

**Homepage:** https://useclaw.pro/
**Pillar guide:** https://useclaw.pro/guides/openclaw-security/
**Verified Skills catalog:** https://useclaw.pro/verified-skills/
**Skill Verifier (browser):** https://useclaw.pro/verifier/

---

### 🔍 skill-vetter (19,340 installs)

Legacy deep-vetting checklist for manual-first OpenClaw skill review. Structured red-flag checklist focused on permissions, patterns, and suspicious instructions. Conservative review path for operators who want manual audit before automated tools.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill skill-vetter -a hermes-agent -y
```

**Key features:**
- Manual-first red-flag checklist
- Permission scope analysis
- Suspicious pattern detection
- Conservative install-or-block verdict
- Trust score: 97 | Audited: Feb 1, 2026

---

### 🛡️ skill-auditor (590 installs) — **Recommended Primary Auditor**

Comprehensive six-step security review for OpenClaw skills. Checks for typosquatting, dangerous permissions, prompt injection, supply chain risks, and data exfiltration patterns. Produces a structured SKILL AUDIT REPORT with severity-based verdicts and safe-run plans.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill skill-auditor -a hermes-agent -y
```

**Six-step protocol:**
1. **Identity check** — typosquatting, impersonation, source verification
2. **Permission analysis** — file-read, file-write, network, shell, env access
3. **Dependency review** — npm/pip/Go package safety, hooks, typosquatting
4. **Prompt injection scan** — hidden instructions, context manipulation
5. **Exfiltration risk** — network calls, file reads, data egress patterns
6. **Supply chain check** — repo provenance, maintainer trust, update history

**Version:** 2.0.0 | Trust score: 97 | Audited: Feb 5, 2026

---

### 🟢 skill-guard (489 installs)

Runtime security monitor for active OpenClaw skills. Watches file access, network calls, and shell commands during execution. Flags anomalous behavior and enforces permission boundaries. Permission-boundary checks + suspicious-behavior signals.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill skill-guard -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 96 | Audited: Feb 3, 2026

---

### 🚫 prompt-guard (453 installs)

Detect and neutralize prompt injection attacks in skill content, user inputs, and external data sources. Uses pattern detection, normalization, and severity tiers (critical vs warning). Prevents hidden instructions from overriding agent behavior.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill prompt-guard -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 97 | Audited: Feb 3, 2026

---

### 🔑 credential-scanner (433 installs)

Pre-flight workspace scan for exposed credentials, API keys, and secrets before any skill gets file-read access. Path-aware regex checks with skip rules and sanitized reporting — never prints raw secrets.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill credential-scanner -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 98 | Audited: Feb 1, 2026

---

### 📦 dependency-auditor (423 installs)

Audit npm, pip, and Go dependencies that skills try to install. Checks for typosquatting, install hooks, malicious packages, recency, reputation, and known vulnerabilities.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill dependency-auditor -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 93 | Audited: Feb 3, 2026

---

### 🔒 permission-auditor (396 installs)

Analyze skill permissions and explain exactly what each allows. Identifies over-privileged skills, flags dangerous combinations, and suggests minimal permission sets. Permission-by-permission review with least-privilege guidance.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill permission-auditor -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 96 | Audited: Feb 1, 2026

---

### 🧹 output-sanitizer (392 installs)

Sanitize agent output before display. Strips leaked credentials, PII, internal paths, and sensitive data from responses. Pattern-based detection with masking rules — never emits raw sensitive values.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill output-sanitizer -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 94 | Audited: Feb 3, 2026

---

### 🏖️ sandbox-guard (390 installs)

Generate Docker sandbox configurations for safely running untrusted skills. Isolates filesystem, network, and process access. Pre-baked profiles for read-only and read-write execution modes with explicit security flags.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill sandbox-guard -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 95 | Audited: Feb 1, 2026

---

### ⚙️ config-hardener (387 installs)

Audit and harden OpenClaw/Hermes configuration. Checks AGENTS.md, gateway settings, sandbox config, and permission policies for security weaknesses. Produces a prioritized hardening plan.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill config-hardener -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 95 | Audited: Feb 1, 2026

---

### 🏠 setup-auditor (384 installs) — **Recommended Environment Audit**

Wizard-style four-step environment audit. Covers credentials, config hardening, sandbox readiness, and persistence checks. Collects operator answers and produces a SETUP AUDIT REPORT with readiness verdict, findings, and concrete remediation steps.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill setup-auditor -a hermes-agent -y
```

**Four-step review:**
1. Credential exposure — secrets in environment, config files, logs
2. Configuration hardening — gateway, AGENTS.md, permission defaults
3. Sandbox readiness — isolation, filesystem, network containment
4. Persistence checks — cron, autostart, SSH keys, startup scripts

**Version:** 2.0.0 | Trust score: not yet audited (new release)

---

### 🌐 network-watcher (376 installs)

Audit and monitor network requests made by skills. Detects data exfiltration, unauthorized API calls, and suspicious outbound connections. Endpoint scrutiny + exfiltration heuristics + safe-pattern whitelist.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill network-watcher -a hermes-agent -y
```

**Version:** 1.0.0 | Trust score: 95 | Audited: Feb 3, 2026

---

### 🚨 incident-responder (374 installs)

Step-by-step incident response playbook for OpenClaw security breaches. Guides through containment, investigation, credential rotation, and recovery. Structured checkpoints for operator decision-making at each phase.

**Install:**
```bash
npx skills add useai-pro/openclaw-skills-security --skill incident-responder -a hermes-agent -y
```

**Response phases:**
1. **Containment** — isolate affected skills, revoke tokens, stop processes
2. **Investigation** — audit logs, check file access, trace network calls
3. **Credential rotation** — systematically rotate all potentially exposed secrets
4. **Recovery** — restore from known-good state, verify integrity, document findings

**Version:** 1.0.0 | Trust score: 96 | Audited: Feb 3, 2026

---

## Recommended Security Pipeline

Chain these skills in order for a complete security workflow:

```
Before install:  skill-vetter OR skill-auditor → permission-auditor → dependency-auditor
Before first run: credential-scanner → config-hardener → setup-auditor → sandbox-guard
During execution: skill-guard → network-watcher → prompt-guard
After execution:  output-sanitizer
If compromised:   incident-responder
```

For minimal setup, start with the two recommended auditors:
```bash
npx skills add useai-pro/openclaw-skills-security --skill skill-auditor -a hermes-agent -y
npx skills add useai-pro/openclaw-skills-security --skill setup-auditor -a hermes-agent -y
```

---

## Summary

| Skill | Installs | Kind | Trust Score |
|-------|----------|------|-------------|
| `skill-vetter` | 19,340 | Auditor (legacy) | 97 |
| `skill-auditor` ⭐ | 590 | Auditor (primary) | 97 |
| `skill-guard` | 489 | Module | 96 |
| `prompt-guard` | 453 | Module | 97 |
| `credential-scanner` | 433 | Module | 98 |
| `dependency-auditor` | 423 | Module | 93 |
| `permission-auditor` | 396 | Module | 96 |
| `output-sanitizer` | 392 | Module | 94 |
| `sandbox-guard` | 390 | Module | 95 |
| `config-hardener` | 387 | Module | 95 |
| `setup-auditor` ⭐ | 384 | Auditor (env) | — |
| `network-watcher` | 376 | Module | 95 |
| `incident-responder` | 374 | Module | 96 |

**New this update:** 13 skills
**Marketplace subtotal before:** 248 → **After:** 261
**Total skills:** 337 → **350**

---

*← [June 12 Discoveries](/hermes/skills/marketplace/new-june12-2026/) | [Skills Catalog](/hermes/skills/catalog/) →*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
