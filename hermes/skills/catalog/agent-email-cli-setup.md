---
title: "Agent Email CLI Skill - Setup Guide"
description: "Codex skill for the agent-email CLI: disposable inboxes, polling, reading messages and managing mailbox profiles."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-email-cli-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "email", "cli"]
---

# Agent Email CLI Skill - Setup Guide

**Source:** [zaddy6/agent-email-skill](https://github.com/zaddy6/agent-email-skill)
**Skill family:** `zaddy6/agent-email-skill` (1 installable skill)
**Combined Installs:** ~2,066 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Developer Tools
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

This single-skill family provides `agent-email-cli`, a Codex skill published by an individual maintainer that wraps the `agent-email` CLI (per the README, fetched Sep 29, 2026). The skill gives agents a workflow for creating disposable inboxes, polling and reading the latest emails, retrieving full message details, managing local mailbox profiles, and troubleshooting common CLI issues. It is the only skill in the repo, verified 1/1 by the sweep with 2,066 installs.

---

## Installation

```bash
npx skills add zaddy6/agent-email-skill
```

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Test inboxes | Create disposable inboxes to verify signup and email flows end to end. |
| Verification-code flows | Poll an inbox and read messages to complete email-based verification steps. |

## Limitations / Verification

- Verified: skills.sh indexing of Sep 29, 2026 (1/1; 2,066 installs).
- Not verified: no live install test performed. Star count not captured in the sweep. The README documents an alternative install: `npx skills add https://github.com/zaddy6/agent-email-skill --skill agent-email-cli`.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
