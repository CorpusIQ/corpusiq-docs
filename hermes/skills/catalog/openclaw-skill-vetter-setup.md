---
title: openclaw-skill-vetter — Setup Guide
description: Automated skill quality validation for Hermes agents. Scan installed skills for missing dependencies, trigger conflicts, security anti-patterns, and structural issues.
---

# openclaw-skill-vetter — Setup Guide

## Prerequisites
- **Hermes Agent** installed
- **Node.js 18+** with `npx` available
- At least one skill installed (to vet)

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Dependency Validation** | Checks all required tools are available before skill activation |
| **Trigger Conflict Detection** | Identifies multiple skills competing for the same keyword trigger |
| **Tool Compatibility Matrix** | Verifies skill tool requirements against available Hermes tools |
| **Security Scanning** | Flags skills with sensitive operations (file write, network, shell) |
| **Structure Validation** | Ensures YAML frontmatter and required sections are present |
| **Version Compatibility** | v1.0.0 adds stricter validation rules and semantic version checking |

## Installation

```bash
# Standard version (168 installs)
npx skills add skills.volces.com/openclaw-skill-vetter

# Stricter v1.0.0 version (171 installs)
npx skills add skills.volces.com/openclaw-skill-vetter-1-0-0
```

## Quick Start

```bash
# Vet all installed skills
hermes skills vet --all

# Vet a specific skill
hermes skills vet --name "corpusiq-email-standards"

# Vet with security deep scan
hermes skills vet --all --security-deep

# Generate a vetting report
hermes skills vet --all --output report.md
```

## What Gets Checked

### 1. Dependency Validation
```
✅ corpusiq-email-standards: all 3 dependencies available (himalaya, terminal, memory)
❌ seo-audit: missing dependency 'web_extract' — web tools not configured
⚠️  browser-automation: optional dependency 'playwright' not installed
```

### 2. Trigger Conflict Detection
```
⚠️  CONFLICT: 'email' keyword triggered by 5 skills:
   - corpusiq-email-standards
   - corpusiq-email-operating-rules
   - corpusiq-email-send-checklist
   - himalaya
   - imap-smtp-email-setup
   → First-match wins: corpusiq-email-standards
```

### 3. Security Anti-Pattern Scan
```
🔴 CRITICAL: skill 'metamask-openclaw-security' — executes downloaded binaries
🟡 WARNING: skill 'browser-automation' — spawns headless browser with network access
🟢 SAFE: skill 'memory-hygiene' — file operations on LanceDB only, no network
```

### 4. Structure Validation
```
❌ skill 'untitled-skill': missing YAML frontmatter
❌ skill 'draft-skill': missing 'description' field
⚠️  skill 'old-skill': no verification gates defined
✅ skill 'corpusiq-email-standards': all structural requirements met
```

## Configuration

Add to `~/.hermes/config.yaml`:

```yaml
skill_vetter:
  version: "1.0.0"                   # Which vetter version to use
  auto_vet_on_install: true          # Vet skills immediately after install
  security_scan_depth: "standard"    # standard | deep
  blocked_patterns:
    - "rm -rf"                       # Block skills containing destructive commands
    - "curl | bash"                  # Block pipe-to-bash patterns
    - "eval("                        # Block dynamic code execution
  warning_patterns:
    - "sudo"                         # Warn on privilege escalation
    - "chmod 777"                    # Warn on permissive file permissions
  ignore_skills:
    - "corpusiq-system-tools"        # Trusted internal skills to skip
```

## CorpusIQ Use Cases

1. **Marketplace Quality Gate:** Before adding a new marketplace skill to the CorpusIQ docs, run vetting to ensure it meets quality standards.

2. **Production Agent Safety:** CorpusIQ's 133+ skills need continuous validation — this prevents a broken dependency from silently failing in production.

3. **Security Compliance:** Automated scanning for dangerous patterns keeps CorpusIQ agents compliant with security best practices.

4. **Onboarding Audit:** When onboarding new team members, vet their skill installation to ensure all required tools are configured.

5. **CI/CD Integration:** Add `hermes skills vet --all --ci` to your CI pipeline to catch skill issues before deployment.

## Integration with Hermes Session Start

Add to your Hermes session start hook:

```bash
#!/bin/bash
# ~/.hermes/hooks/session-start.sh
echo "Vetting installed skills..."
hermes skills vet --all --quiet || echo "⚠️  Skill vetting found issues — check logs"
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "No skills found to vet" | Skills directory empty or misconfigured | Check `~/.hermes/skills/` path |
| False positive on dependency | Tool installed under different name | Add alias to skill config |
| Security scan too aggressive | Legitimate skill flagged | Add to `ignore_skills` list |
| v1.0.0 stricter than expected | Version mismatch | Use standard version for initial adoption |
| "Permission denied" on vet | Hermes can't read skill files | Check file permissions: `chmod -R 644 ~/.hermes/skills/` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
