---
title: Metamask OpenClaw Desktop Security Analysis — Setup Guide
description: Security analysis skill for evaluating Metamask OpenClaw desktop executable distributions. Detects cryptocurrency scams, impersonation, and malware red flags.
---

# Metamask OpenClaw Desktop Security Analysis — Setup Guide

⚠️ **This is a defensive security skill.** It helps agents evaluate suspicious Web3 desktop software before granting execution access.

## Prerequisites
- **Hermes Agent** or **Clawdbot** with skill execution capabilities
- **Node.js 18+** (for npx)
- Understanding of Web3/cryptocurrency security basics

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Impersonation Detection** | Identifies projects using Metamask branding without official affiliation |
| **Binary Risk Assessment** | Evaluates Windows `.exe` installers for malware indicators |
| **Brand Misuse Analysis** | Flags unauthorized use of trusted crypto brand names |
| **Scam Pattern Recognition** | Identifies common cryptocurrency scam distribution patterns |
| **Security Recommendations** | Generates actionable security guidance for users |

## Installation

```bash
npx skills add aradotso/hermes-skills/metamask-openclaw-desktop-security-analysis
```

## Quick Start

Trigger the skill with any of these natural language prompts:

- "What is Metamask Openclaw desktop?"
- "Analyze this Metamask desktop client"
- "Is this Metamask exe safe?"
- "Check Metamask Openclaw security"
- "Evaluate this Web3 desktop tool"
- "Scan this Metamask Windows installer"
- "Investigate Openclaw project"
- "Verify Metamask desktop download"

## Threat Indicators Detected

The skill evaluates projects against these red flag criteria:

### 1. Impersonation
- **Metamask** is a browser extension wallet with **no official "Openclaw" product**
- Any desktop executable claiming to be "Metamask Openclaw" is impersonating a legitimate service
- The real Metamask is available only at [metamask.io](https://metamask.io)

### 2. Distribution Patterns
- `.exe` downloads from unofficial GitHub repositories
- No code signing certificates
- No checksums or hash verification provided
- Repository lacks audit history or known maintainers

### 3. Brand Abuse
- Use of "Metamask" name and fox logo without authorization
- Misleading README screenshots showing Metamask UI
- Fake social proof (fabricated star counts, testimonials)

## CorpusIQ Use Cases

1. **Agent Security Gate:** Before any Hermes agent installs or executes a third-party tool, run this skill to evaluate the tool's security posture. Prevents agents from being tricked into installing malware.

2. **User Protection:** When CorpusIQ users ask about suspicious tools ("Is X safe to use?"), this skill provides a structured security evaluation rather than generic warnings.

3. **Security Pattern Library:** The threat indicators and detection patterns in this skill can be adapted for other crypto/Web3 security evaluations — NFT scams, fake airdrops, phishing sites.

4. **Agent Autonomy Safeguard:** As agents gain more autonomous execution capabilities (code execution, file system access, network calls), security analysis skills become mandatory pre-execution gates.

## ⚠️ CRITICAL SECURITY GUIDANCE

This project exhibits **EXTREME RED FLAGS** indicating cryptocurrency scam or malware distribution. Do NOT:

- Download any files from suspicious repositories
- Install or execute `.exe` files from unverified sources
- Enter seed phrases or private keys into any desktop application you haven't thoroughly vetted
- Trust screenshots or testimonials in the repository README

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Skill returns no analysis | Repository URL not accessible | Verify the repo exists and is public |
| False positive on legitimate tool | Overly aggressive impersonation check | Review analysis manually — skill is conservative by design |
| "Not found" error | Skill not installed | Run `npx skills add` command above |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
