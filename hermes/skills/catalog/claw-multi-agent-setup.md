---
title: "Claw Multi-Agent Skill - Setup Guide"
description: "OpenClaw multi-agent skill: parallel sub-agents, auto-routing and hybrid research-pipeline modes with 50-78% time savings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claw-multi-agent-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent", "openclaw"]
---

# Claw Multi-Agent Skill - Setup Guide

**Source:** [zcyynl/claw-multi-agent](https://github.com/zcyynl/claw-multi-agent)
**Skill family:** `zcyynl/claw-multi-agent` (1 installable skill)
**Combined Installs:** ~168 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Automation
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

A single OpenClaw skill published by an individual maintainer that assembles an AI sub-agent squad — researcher, analyst, writer — with different roles and models working in parallel. Per the README (fetched Sep 29, 2026; Chinese, translated here), it offers three modes: commander (parallel web-search agents aggregated into one report), pipeline (lightweight tool-free agents for multi-angle analysis), and hybrid (research then multi-draft output), with auto-routing between modes. The sweep verified it 1/1 with 168 installs.

---

## Installation

```bash
npx skills add zcyynl/claw-multi-agent
```

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Parallel research sweeps | Run commander mode to search several topics at once and merge results into one report. |
| Multi-angle analysis | Use pipeline mode to analyze one problem from technical, product, and beginner perspectives. |
| Multi-draft reports | Generate several draft variants in hybrid mode after a research phase. |

## Limitations / Verification

- Verified: skills.sh indexing of Sep 29, 2026 (1/1; 168 installs).
- Not verified: no live install test performed. Star count not captured in the sweep. The README documents an alternative install: `npx clawhub@latest install claw-multi-agent`, with zero-config reuse of existing OpenClaw models.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
