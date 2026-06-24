---
title: trailofbits/skills — Full Setup Guide for Hermes Agents
description: Install and configure Trail of Bits security skills — 78 plugins for code auditing, vulnerability scanning, fuzzing, static analysis, and smart contract security. 243K installs.
---

# trailofbits/skills — Setup Guide

**Source:** [trailofbits/skills](https://skills.sh/trailofbits/skills) (242.7K total installs)
**Category:** Security / Code Auditing

A curated collection of 78 security-focused agent skills from Trail of Bits. Covers code auditing, vulnerability scanning, fuzzing, testing, static analysis, smart contract security, malware analysis, and development workflow hardening. Compatible with Claude Code and Codex.

---

## Installation

### Claude Code Marketplace

```bash
/plugin marketplace add trailofbits/skills
/plugin menu
```

### Codex

```bash
codex plugin marketplace add trailofbits/skills
codex plugin list
codex plugin add @trailofbits
```

### Skills.sh

```bash
npx skills add trailofbits/skills
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ |
| **Claude Code or Codex** | Plugin marketplace required for plugin install |
| **GitHub repo** | For supply-chain and workflow auditing |

---

## Key Plugin Categories

### Code Auditing

| Plugin | What It Does |
|---|---|
| **`static-analysis`** | CodeQL, Semgrep, and SARIF parsing toolkit |
| **`semgrep-rule-creator`** | Create custom Semgrep rules for vulnerability detection |
| **`insecure-defaults`** | Detect insecure configs, hardcoded credentials, fail-open patterns |
| **`supply-chain-risk-auditor`** | Audit dependency supply-chain threat landscape |
| **`differential-review`** | Security-focused diff review with git history analysis |
| **`code-maturity-assessor`** | Assess codebase security maturity level |

### Smart Contract Security

| Plugin | What It Does |
|---|---|
| **`building-secure-contracts`** | Vulnerability scanners for 6 blockchains (Solana, Cosmos, Algorand, TON, Cairo, Substrate) |
| **`entry-point-analyzer`** | Identify state-changing entry points in smart contracts |

### Testing & Fuzzing

| Plugin | What It Does |
|---|---|
| **`testing-handbook-skills`** | Fuzzers, static analysis, sanitizers, coverage from Testing Handbook |
| **`property-based-testing`** | Multi-language property-based testing guidance |
| **`mutation-testing`** | Configure mewt/muton mutation testing campaigns |

### Verification

| Plugin | What It Does |
|---|---|
| **`constant-time-analysis`** | Detect compiler-induced timing side-channels |
| **`zeroize-audit`** | Detect missing/eliminated zeroization of secrets |
| **`spec-to-code-compliance`** | Spec-to-code compliance checker |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent skill security audit** | Use `static-analysis` + `semgrep-rule-creator` to audit CorpusIQ agent skills |
| **Supply chain hardening** | Run `supply-chain-risk-auditor` on corpusiq-docs dependencies |
| **GitHub Actions security** | Use `agentic-actions-auditor` to audit CI/CD workflows |
| **Code maturity tracking** | Run `code-maturity-assessor` quarterly on core repos |
| **Secure workflow enforcement** | Use `secure-workflow-guide` as pre-commit gate |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **Plugin marketplace not found** | Upgrade Claude Code: `npm update -g @anthropic-ai/claude-code` |
| **SARIF parsing fails** | Verify SARIF v2.1.0 format — older versions not supported |
| **CodeQL database missing** | Run `codeql database create` before analysis |
| **Semgrep rules not triggering** | Check rule language matches target — use `semgrep-rule-variant-creator` to port |

## Verification

```bash
# List installed plugins
/plugin list | grep trailofbits

# Run a quick security scan
# In agent: "Run static-analysis on the current repo"

# Test semgrep
semgrep --config auto .
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
---

*
---
*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
