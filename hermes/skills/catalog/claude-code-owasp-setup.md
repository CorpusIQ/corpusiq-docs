---
title: "Claude Code OWASP Security - Secure Review Setup"
description: "agamm/claude-code-owasp: 2.9K combined installs. OWASP security skill for Claude Code covering Top 10:2025, ASVS 5.0 and agentic AI security."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-code-owasp-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "owasp", "security", "appsec"]
---

# Claude Code OWASP Security - Setup Guide

**Source:** [agamm/claude-code-owasp](https://www.skills.sh/agamm/claude-code-owasp) via skills.sh - 2.9K combined installs across 1 indexed listing; first documented 2026-11-27 (evening sweep)

**GitHub:** [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) - 463 stars, MIT, branch main, last pushed 2026-11-03; the skill lives under `.claude/skills/owasp-security/SKILL.md` with on-demand `reference/` files.

**Category:** Application security, OWASP standards and secure code review for agent runtimes

**Quality Tier:** 🟢 Green - all three samplers pass the single sampled listing.

claude-code-owasp is a single-skill Claude Code plugin from agamm that turns the current OWASP standards into review guidance an agent can apply. The skill covers the OWASP Top 10:2025, ASVS 5.0, the OWASP Top 10 for LLM Applications (2026) and the Agentic Top 10 (2026), with a five-step review workflow, a finding-triage rubric to cut false positives and a fixed reporting format. It is intended for authorised review of code you own or are permitted to test, not as an offensive toolkit.

The accuracy note is the notable part: category names, ASVS chapter structure and requirement IDs are verified directly against owasp.org and the ASVS repository rather than paraphrased, because ASVS 5.0 renumbered every chapter and three Top 10 categories were renamed in 2025. On-demand reference files add a coverage checklist, language-specific quirks for 20+ languages and a config-and-supply-chain deep dive, kept out of the main SKILL.md per Claude Code progressive-disclosure practice.

## Installation

The README offers three install paths. As a Claude Code plugin:

```text
/plugin marketplace add agamm/claude-code-owasp
/plugin install owasp-security@agamm
```

Third-party marketplaces do not auto-update by default. Update by hand:

```bash
claude plugin marketplace update agamm
claude plugin update owasp-security@agamm
```

Or turn on auto-update once: run `/plugin`, open the Marketplaces tab, select `agamm` and choose Enable auto-update, then `/reload-plugins`. To install as a plain skill instead, copy the whole directory with degit:

```bash
npx degit agamm/claude-code-owasp/.claude/skills/owasp-security .claude/skills/owasp-security
```

Use the `~/.claude/skills/owasp-security` target for a global install, or clone the full repository and copy the directory manually.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| owasp-security | 2,911 | Authorised review of code and diffs against OWASP Top 10:2025, ASVS 5.0, the LLM Top 10 (2026) and the Agentic Top 10 (2026), plus secure implementation of auth, cryptography, input handling and AI agent features. |

The single indexed listing appears above.

## Why This Matters for Hermes Agents

The skill is a compact model of how to carry a fast-moving standard into an agent. OWASP renamed three Top 10 categories in 2025, ASVS 5.0 renumbered every chapter, and the LLM Top 10 2026 reordered eight of its ten entries, so a skill that pins the current IDs and names keeps an agent from citing stale ones. The README asserts that accuracy by checking every name and ID against the primary sources rather than paraphrasing.

The finding-triage rubric is the transferable discipline: before reporting, confirm attacker-controlled input, sink reachability and blast radius. That is what keeps a review skill from flooding a pull request with false positives, which is the usual reason reviewers stop trusting an agent's security output.

The progressive-disclosure split is also worth copying. SKILL.md holds the workflow, rubric and quick-reference tables; the reference directory carries the per-language quirks and the config and supply-chain detail, loaded only when the task needs them. For a router, that means the skill is cheap to keep resident and the expensive material is fetched on demand.

One caveat for builders: the skill reviews and guides, it does not scan. It points the agent at the right OWASP requirement and severity logic, but it is not a substitute for a real scanner or an authorised manual review before shipping.

## Usage

| You say | What happens |
|---|---|
| "Review this diff for security issues" | Loads the review workflow and walks entry points to report, rating severity by exploitability. |
| "Is this authentication implementation secure?" | Applies the auth and session guidance from ASVS 5.0 with requirement IDs and levels. |
| "What are the security risks in this Python code?" | Pulls the language quirks reference for unsafe and safe Python patterns. |
| "Help me implement secure session management" | Guides session, cookie and token handling with the Top 10:2025 and ASVS requirements. |
| "Check this AI agent for OWASP agentic risks" | Maps the agent against the OWASP Agentic Top 10 (2026) ASI01-ASI10 risks. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/agamm/claude-code-owasp/main/.claude/skills/owasp-security/SKILL.md
```

After a clone, confirm the skill layout and its reference set:

```bash
git clone --depth 1 https://github.com/agamm/claude-code-owasp.git /tmp/claude-code-owasp
ls /tmp/claude-code-owasp/.claude/skills/owasp-security/
ls /tmp/claude-code-owasp/.claude/skills/owasp-security/reference/
head -3 /tmp/claude-code-owasp/.claude/skills/owasp-security/SKILL.md
```

The first listing should show SKILL.md alongside the reference directory, the second should show review-checklist.md, languages.md, config-and-supply-chain.md and owasp-report.md, and head should show the SKILL.md frontmatter.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| owasp-security | Pass | Pass | Pass |

This guide is Green because all three samplers pass the single sampled listing. The repository is Markdown skills plus an eval suite and a test-graders script under scripts/, with no executable payload beyond the evals. It is a review and guidance skill for authorised security review of your own code, not an offensive toolkit; apply it only to code you are permitted to test.

## Limitations

- Snapshot data, verified 2026-11-27: 2,911 combined installs across 1 indexed listing; 463 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- It is a single skill and a single indexed listing; there is no suite to route between, so coverage is bounded by what the one SKILL.md and its reference files carry.
- Claude Code first: updates arrive cleanly through the plugin marketplace, while a plain degit install is a manual copy that does not auto-update, and third-party marketplaces do not auto-update by default either.
- The evals run real model calls billed to your account, so run them deliberately rather than in every CI cycle.
- The skill reviews and guides; it is not a scanner and does not replace an authorised manual review or a real SAST/DAST tool before shipping.

## Related

- [Awesome Security Skills - SecLists Testing Toolkit Setup](/hermes/skills/catalog/awesome-skills-security-setup)
- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install as a plugin and turn on auto-update once, or update by hand with the two update commands; the README warns third-party marketplaces do not auto-update by default.
- Apply the triage rubric before reporting anything: confirm attacker-controlled input, sink reachability and blast radius, or the review floods the pull request with false positives.
- Keep SKILL.md lean and let the reference files load on demand; do not inline the whole language and config reference into the main skill.
- Scope reviews to code you own or are authorised to test; this is a defensive review skill, not an offensive toolkit.
- Pin the reporting format: location, input-to-sink path, impact, fix and confidence keeps every finding comparable across runs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
