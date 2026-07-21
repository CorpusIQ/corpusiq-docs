---
title: Skill Vetter — Security Audit for Hermes Skills (useai-pro)
description: Security-first vetting for OpenClaw/Hermes skills before installation. Checks for red flags, permission scope, and suspicious patterns. 20.5K+ installs.
---

# Skill Vetter — Setup Guide

**Source:** [useai-pro/openclaw-skills-security](https://skills.sh/useai-pro/openclaw-skills-security/skill-vetter) (20,500+ installs)
**Category:** Security / Governance
**Quality Tier:** 🟡 Beta
**Trust Score:** 97/100 (last audited: 2026-02-01)

A security auditor for OpenClaw and Hermes skills. Before installing any skill from ClawHub, GitHub, or other community sources, the skill-vetter runs a structured red-flag checklist focused on permissions, patterns, and suspicious instructions. Produces a conservative manual review output for install-or-block decisions.

---

## Installation

```bash
npx skills add useai-pro/openclaw-skills-security --skill skill-vetter
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes/OpenClaw** | Any version |
| **Node.js 18+** | Required for `npx skills` CLI |

---

## Key Capabilities

### Vetting Protocol

The skill-vetter follows a four-stage protocol:

#### Step 1: Metadata Check
- Verify `name` matches expected skill name (no typosquatting)
- Check `version` follows semver
- Confirm `description` is clear and matches what the skill does
- Ensure `author` is identifiable (not anonymous)

#### Step 2: Permission Scope Analysis

| Permission | Risk Level | Justification Required |
|---|---|---|
| `fileRead` | Low | Almost always legitimate |
| `fileWrite` | Medium | Must justify what files and why |
| `network` | Medium-High | Must specify endpoints and data sent |
| `shell` | High | Requires strong justification and sandboxing |

#### Step 3: Pattern Analysis
- Command injection vectors (eval, exec, system calls)
- Obfuscated code or base64-encoded payloads
- Hardcoded URLs/IPs (potential data exfiltration)
- Excessive permission requests relative to stated functionality

#### Step 4: Recommendation
- **INSTALL** — No red flags, permissions justified
- **REVIEW** — Minor concerns, install with monitoring
- **BLOCK** — Critical red flags, do not install

---

## Quick Start

```bash
# Vet a skill before installing
npx skills use useai-pro/openclaw-skills-security@skill-vetter --skill <skill-name>

# Or: manually invoke the vetting checklist when reviewing a SKILL.md
```

### Manual Vetting (for Hermes agents)

When reviewing a skill manually, apply these checks:

1. Read the SKILL.md frontmatter — verify `name`, `version`, `description`, `author`
2. Check `allowed-tools` or `permissions` section — assess risk level per tool
3. Scan for suspicious patterns: `eval()`, `exec()`, base64 strings, hardcoded URLs
4. Compare stated functionality against requested permissions — they should align
5. Document your decision: INSTALL / REVIEW / BLOCK with justification

---

## Hermes Integration

For CorpusIQ Hermes agents, integrate skill-vetter into the governance pipeline:

1. **Pre-install gate**: Run vetting before any `npx skills add` command
2. **Weekly re-audit**: Re-vet all installed skills every Sunday
3. **Audit log**: Write vetting results to `~/.hermes/profiles/corpusiq/skill-audits/YYYY-MM-DD.md`
4. **Block escalation**: BLOCK results → notify Telegram Topic 2 immediately

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Unknown skill format | Ensure the skill has a SKILL.md with proper frontmatter |
| Missing author info | Flag as REVIEW — anonymous skills require extra scrutiny |
| Permission mismatch | If a skill requests `shell` but only needs `fileRead`, flag as BLOCK |

---

## See Also

- [[skill-vetting-setup]] — NVIDIA SkillSpector-based alternative vetting system
- [[openclaw-audit-watchdog-setup]] — Runtime audit monitoring for installed skills
- [ClawHub](https://clawhub.ai) — Official OpenClaw skill marketplace
