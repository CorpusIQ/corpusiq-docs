---
title: Security Scanning — Automated Skill Vulnerability Detection
description: Automated security scanning for Hermes Agent skills using NVIDIA SkillSpector. Vulnerability categories, scan methodology, and how to interpret results for your own skill corpus.
category: best-practices
tags: [hermes-agent, security, skillspector, vulnerability-scanning, credentials, supply-chain]
last_updated: 2026-06-20
---

# Security Scanning — Automated Skill Vulnerability Detection

Your Hermes Agent's skills are code — and code needs security review. [NVIDIA SkillSpector](https://github.com/NVIDIA/skillspector) scans AI agent skill files for vulnerability patterns across multiple categories. Running it on your skill corpus catches credential leaks, dangerous code patterns, and excessive permissions before they become breaches.

## What SkillSpector Scans

SkillSpector analyzes every file in a skill corpus — markdown documentation, Python scripts, shell scripts, configuration files — against a library of vulnerability patterns:

| Category | What It Detects |
|----------|----------------|
| **Data Exfiltration** | Patterns that could leak data to external endpoints, hardcoded URLs in scripts, unrestricted network access |
| **Privilege Escalation** | Sudo usage, root-level file writes, permission changes without approval gates |
| **Supply Chain** | Unpinned dependencies, `curl | bash` patterns, unsigned package sources |
| **Rogue Agent** | Unsupervised execution loops, self-modifying code, agent autonomy beyond declared bounds |
| **Excessive Agency** | Write permissions without confirmation gates, destructive operations without guardrails |
| **Tool Misuse** | Dangerous flag combinations, chained tools that could amplify damage |
| **Output Handling** | Unsanitized output used as input, log injection patterns, unsanitized HTML |
| **Dangerous Code Execution** | `eval()`, `exec()`, unchecked subprocess calls, shell injection vectors |
| **Prompt Injection** | Unsanitized user input in prompt templates, missing input validation |
| **Memory Poisoning** | Unvalidated writes to persistent memory stores |

## Typical Scan Results

A production Hermes Agent deployment with an extensive skill library will typically produce findings in these ranges:

| Severity | Range | Primary Sources |
|----------|-------|-----------------|
| **HIGH** | Several hundred findings | Privilege Escalation patterns in reference docs, Supply Chain in archived examples |
| **MEDIUM** | Larger volume | Documentation describing dangerous patterns, example scripts showing insecure defaults |
| **LOW** | Minimal | Known-safe patterns flagged for review, style-level concerns |

**Important context:** Static-only scans (without LLM analysis) flag documentation that *describes* dangerous patterns alongside actual dangerous code. A SKILL.md documenting "never hardcode API keys" will trigger the same finding as code that actually hardcodes API keys. Run with LLM-enhanced analysis for production safety scoring that distinguishes documentation from executable code.

## Running a Scan

```bash
# Docker-based scan (works on any Python version)
docker run --rm \
  -v /path/to/skills:/scan/skills:ro \
  -v /tmp:/output:rw \
  skillspector scan /scan/skills \
  --no-llm \
  --format json \
  --output /tmp/report.json

# LLM-enhanced scan for accurate scoring
docker run --rm \
  -v /path/to/skills:/scan/skills:ro \
  -v /tmp:/output:rw \
  -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
  -e SKILLSPECTOR_PROVIDER=anthropic \
  skillspector scan /scan/skills \
  --format json \
  --output /tmp/report.json
```

## Interpreting Your Results

1. **Start with static scan** (`--no-llm`). This gives you a broad inventory of potential issues.
2. **Filter by file type.** Markdown files (.md) flagged as HIGH are likely documentation references, not executable vulnerabilities.
3. **Focus on scripts.** Python (.py) and shell (.sh) files with HIGH findings need immediate review.
4. **Run LLM-enhanced scan** for accurate per-skill risk scores before publishing to marketplaces or sharing with teams.
5. **Set a cadence.** Run scans weekly or before major skill releases.

## Fixing Common Findings

Most HIGH findings in skill documentation are resolved by:

- **Removing sensitive patterns from docs:** Replace real API key examples with `"your-key-here"` placeholders
- **Adding approval gates:** Document that write operations require `approval_required: true`
- **Pinning dependencies:** Replace `pip install package` with `pip install package==1.2.3`
- **Validating inputs:** Add input sanitization examples to scripts that handle user data

---

*Scans run with SkillSpector. Your own results will vary based on skill corpus size, code-to-documentation ratio, and security practices in your skills.*
