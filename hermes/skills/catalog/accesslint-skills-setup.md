---
title: "AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup"
description: "Setup guide for AccessLint/skills - the official agent skill set from the AccessLint web-accessibility vendor. 5 skills cover the WCAG 2.2 audit workflow end to end: automated scanning, manual keyboard/screen-reader inspection, WCAG-EM conformance auditing, remediation, and regression diffing. 5.1K+ combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/accesslint-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-15"
tags: ["hermes skill", "agent skill", "skill setup", "accessibility", "a11y", "wcag"]
---

# AccessLint Skills - Setup Guide

**Source:** [AccessLint/skills](https://github.com/AccessLint/skills) (98⭐, created Oct 2025, pushed Aug 25, 2026)
**Skill:** `AccessLint/skills` (5 installable skills; skills.sh indexes 13 listings - 5 core + 8 legacy aliases)
**Combined Installs:** ~5.1K across indexed listings (Sep 15, 2026 snapshot)
**Category:** Web Accessibility / Testing
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 15, 2026)

[AccessLint](https://accesslint.com) is an established web-accessibility vendor (npm `@accesslint/cli`, `@accesslint/core`). Its skills repo ships five Agent Skills that cover the WCAG 2.2 audit workflow end to end: automated scanning, hands-on keyboard and screen-reader checks, WCAG-EM conformance auditing, remediation, and regression diffing. Each finding is graded on two axes - severity (user impact) and evidence basis (● verified / ◐ confirm-with-a-human / ○ human-required) - making this the most audit-rigorous a11y skill set currently on skills.sh. Install is agent-agnostic via the skills CLI; a bundled MCP server (`@accesslint/mcp`) is optional.

---

## Installation

```bash
# All 5 skills (verified live Sep 15, 2026: "Found 5 skills")
npx skills add AccessLint/skills

# Optional: AccessLint MCP server (rule metadata for audit/inspect/fix)
# mcpServers entry:
#   "accesslint": { "command": "npx", "args": ["-y", "@accesslint/mcp@latest"] }
```

A Claude Code plugin variant exists (`claude plugin marketplace add accesslint/skills`), but the skills CLI path is the agent-agnostic one.

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js 18+ | `npx skills` requirement; `@accesslint/cli` is shelled out via npx on demand |
| Chrome DevTools MCP | `accessibility-inspect` drives a live page via `mcp__chrome-devtools__*` tools |
| `accesslint.config.json` | Optional: `npx @accesslint/cli init` defines named targets so skills can run without a URL |
| AccessLint MCP (optional) | `list_rules` / `explain_rule` metadata for audit/inspect/fix |

## Roster - 5 Core Skills

| Skill | Installs | Scope | Does |
|---|---|---|---|
| accessibility-audit | 576 | whole site | WCAG-EM: defines scope, samples pages/flows, runs scan+inspect per page, reports per-criterion conformance (pass/fail/undetermined) |
| accessibility-scan | 518 | one page | Automated rule engine against the live DOM; returns a worklist (selector, file:line, evidence, fix directive). Locates; doesn't edit |
| accessibility-fix | 510 | target/worklist | Baseline → edit → verify; applies mechanical fixes, leaves TODOs for visual/contextual judgment |
| accessibility-inspect | 488 | one page | Manual tier: keyboard/focus order, a11y-tree names/roles/states, reflow/zoom at 200%, reduced motion, form errors |
| accessibility-diff | 485 | a change | Diffs a page against a baseline (uncommitted changes or a branch); reports only what the change introduced/fixed |

skills.sh also indexes 8 legacy/alias listings (`audit` 654, `scan` 399, `diff` 365, `contrast-checker` 287, `refactor` 258, `use-of-color` 246, `link-purpose` 242, `audit-and-fix` 30) - the repo itself ships the 5 skills above (live-verified with `--list`).

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs-site compliance** | Run `accessibility-audit` against corpusiq.io/docs pages ahead of deploy; apply mechanical fixes with `accessibility-fix` |
| **Section 508 / enterprise client work** | WCAG-EM conformance reports for government or enterprise engagements |
| **Product UI checks** | `accessibility-inspect` keyboard/focus-order passes on new UI templates before release |
| **Regression guard** | `accessibility-diff` on docs PRs - reports only what a change introduced or fixed |
| **Help-first content** | Real a11y findings become operator-help content (real problems, real fixes) |

## Limitations / Verification

- `accessibility-scan` / `-diff` work immediately (shell out to `@accesslint/cli`); `-fix` / `-audit` / `-inspect` benefit from the optional MCP server
- The methodology draws an explicit boundary against standing in for real assistive-technology users (○ human-required findings) - don't over-claim compliance from agent runs alone
- Verify: `npx skills add AccessLint/skills --list` shows "Found 5 skills"; then `npx @accesslint/cli --version`

## Security

No skills.sh security audits published (verified Sep 15, 2026 - the publisher page renders no audit verdicts). Treat as unverified until reviewed:

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Podo Design Agent Skills - 151-Skill Design Catalog Setup](/docs/hermes/skills/catalog/podo-design-agent-skills-setup)
- [OWL Listener Designer Skills - 107-Skill Design Suite Setup](/docs/hermes/skills/catalog/owl-listener-designer-skills-setup)
- [Hallmark - Anti-AI-Slop Design Skill Setup](/docs/hermes/skills/catalog/hallmark-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
