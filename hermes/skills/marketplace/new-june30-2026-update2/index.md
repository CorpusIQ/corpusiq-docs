---
title: "🆕 June 30, 2026 (Update 2) — xurl X/Twitter, TimesFM Forecasting, ClawSec Security Suite"
description: "12 additional Hermes-relevant skills discovered June 30, 2026 evening sweep: xurl (X/Twitter from Nous Research), TimesFM forecasting (Google), and 10 ClawSec security skills for the OpenClaw ecosystem."
---

# 🆕 June 30, 2026 — Update 2: 12 Additional Skills

**Date:** June 30, 2026 (Update to [June 30 sweep](/hermes/skills/marketplace/new-june30-2026/) and [Update 1](/hermes/skills/marketplace/new-june30-2026-update/))
**New Repos:** 2 | **New Skills:** 12 | **Combined Installs:** 3,478

Evening sweep across skills.sh surfaced 12 additional skills missed in the morning and midday passes. The headline find is **xurl** — Nous Research's official X/Twitter integration that was inexplicably absent from the catalog despite 171 installs. Google's **TimesFM** brings zero-shot forecasting to Hermes agents. The remaining 10 skills form the **ClawSec security suite** from prompt-security — the first comprehensive security toolkit for the OpenClaw/Clawbot agent ecosystem.

---

## New Skills at a Glance

| # | Skill | Installs | Category | Source |
|---|-------|:--------:|----------|--------|
| 1 | **xurl** | 171 | Social Media | nousresearch/hermes-agent |
| 2 | **timesfm-forecasting** | 699 | Data Science | k-dense-ai/scientific-agent-skills |
| 3 | **clawsec-suite** | 731 | Security | prompt-security/clawsec |
| 4 | **soul-guardian** | 233 | Agent Identity | prompt-security/clawsec |
| 5 | **clawsec-clawhub-checker** | 221 | Security | prompt-security/clawsec |
| 6 | **clawsec-feed** | 220 | Security Intelligence | prompt-security/clawsec |
| 7 | **clawtributor** | 186 | Supply Chain | prompt-security/clawsec |
| 8 | **claw-release** | 174 | Release Mgmt | prompt-security/clawsec |
| 9 | **clawsec-scanner** | 167 | Security Scanning | prompt-security/clawsec |
| 10 | **clawsec-nanoclaw** | 166 | Security | prompt-security/clawsec |
| 11 | **prompt-agent** | 140 | Prompt Security | prompt-security/clawsec |
| 12 | **openclaw-traffic-guardian** | 31 | Network Security | prompt-security/clawsec |

---

## Category Breakdown

### Social Media (1 skill)

#### xurl (171 installs) ⭐ Setup Guide Available
**Repo:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)

Full X/Twitter API v2 integration from the Hermes creator. Post tweets, search, send DMs, upload media — everything a growth agent needs for social presence management. Previously missing from the catalog despite being an official Nous Research skill.

**Setup Guide:** [xurl — Full Setup Guide](/hermes/skills/catalog/xurl-setup/)

```bash
npx skills add nousresearch/hermes-agent --skill xurl
```

---

### Data Science (1 skill)

#### timesfm-forecasting (699 installs) ⭐ Setup Guide Available
**Repo:** [k-dense-ai/scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills)

Google Research's TimesFM foundation model for zero-shot time series forecasting. No training required — feed historical data and get predictions with confidence intervals. Useful for revenue forecasting, usage growth prediction, and anomaly detection from agent-generated metrics.

Also available from: google-research/timesfm (153 installs), eturkes/claude-scientific-skills (23).

**Setup Guide:** [TimesFM Forecasting — Full Setup Guide](/hermes/skills/catalog/timesfm-forecasting-setup/)

```bash
npx skills add k-dense-ai/scientific-agent-skills --skill timesfm-forecasting
```

---

### Security — ClawSec Suite (10 skills)

The [prompt-security/clawsec](https://github.com/prompt-security/clawsec) repo provides a comprehensive security toolkit for the OpenClaw/Clawbot agent ecosystem. While most skills target Claw/OpenClaw specifically, several are directly applicable to Hermes agent security auditing.

#### clawsec-suite (731 installs)
Umbrella security suite — vulnerability scanning, prompt injection detection, and security posture assessment for agent deployments. The entry point for the entire ClawSec toolkit.

```bash
npx skills add prompt-security/clawsec --skill clawsec-suite
```

#### soul-guardian (233 installs)
Guards agent personality/identity ("soul") against prompt injection, role confusion, and identity drift. Relevant to any agent with a defined persona — including Hermes profiles.

```bash
npx skills add prompt-security/clawsec --skill soul-guardian
```

#### clawsec-clawhub-checker (221 installs)
Validates ClawHub marketplace submissions for security issues. Supply-chain security for the agent skill ecosystem.

```bash
npx skills add prompt-security/clawsec --skill clawsec-clawhub-checker
```

#### clawsec-feed (220 installs)
Real-time security intelligence feed for agent vulnerabilities, prompt injection CVEs, and MCP server CVEs.

```bash
npx skills add prompt-security/clawsec --skill clawsec-feed
```

#### clawtributor (186 installs)
Verifies contributor identity and commit provenance. Supply-chain trust for agent ecosystems with multiple contributors.

```bash
npx skills add prompt-security/clawsec --skill clawtributor
```

#### claw-release (174 installs)
Secure release management — verifies artifact integrity, checksums, and signing before deployment.

```bash
npx skills add prompt-security/clawsec --skill claw-release
```

#### clawsec-scanner (167 installs)
Active vulnerability scanner for agent configurations, MCP server endpoints, and skill dependencies.

```bash
npx skills add prompt-security/clawsec --skill clawsec-scanner
```

#### clawsec-nanoclaw (166 installs)
Lightweight security agent for resource-constrained environments (Raspberry Pi, edge devices running agent workloads).

```bash
npx skills add prompt-security/clawsec --skill clawsec-nanoclaw
```

#### prompt-agent (140 installs)
Prompt-level security agent — analyzes every prompt for injection attempts before it reaches the LLM.

```bash
npx skills add prompt-security/clawsec --skill prompt-agent
```

#### openclaw-traffic-guardian (31 installs)
Network traffic monitoring for OpenClaw agents — detects anomalous outbound connections, data exfiltration patterns.

```bash
npx skills add prompt-security/clawsec --skill openclaw-traffic-guardian
```

---

## Setup Guides Added

This sweep produced two new setup guides:
- **[xurl (X/Twitter) Setup Guide](/hermes/skills/catalog/xurl-setup/)** — API credentials, CLI commands, 5 CorpusIQ use cases
- **[TimesFM Forecasting Setup Guide](/hermes/skills/catalog/timesfm-forecasting-setup/)** — Installation, forecasting modes, anomaly detection

---

*← [June 30 Update 1](/hermes/skills/marketplace/new-june30-2026-update/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
