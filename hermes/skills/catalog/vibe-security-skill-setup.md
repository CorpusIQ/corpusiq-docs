---
title: "Vibe Security - Security Audit for Vibe-Coded"
description: "raroque/vibe-security-skill - 3.9K combined installs across 1 indexed listing: security references loaded by stack to catch vulnerability patterns."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vibe-security-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "security", "vibe coding"]
---

# Vibe Security - Setup Guide

**Source:** [raroque/vibe-security-skill](https://www.skills.sh/raroque/vibe-security-skill) via skills.sh - 3.9K combined installs across 1 indexed listing; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 1,235 stars, MIT license, `main` branch, last pushed 2026-03-15, `vibe-security/SKILL.md`
**Category:** Security review for vibe-coded and AI-built applications
**Quality Tier:** 🟢 Green - the sampled skill passes all three auditors.

Vibe Security is a single-skill publisher built by Chris Raroque with colleagues at Aloa. The one indexed skill is a set of security reference files that the agent loads by stack, so checks apply only to the technologies a project actually uses.

The rules target the patterns AI assistants keep introducing: hardcoded secrets, disabled Supabase row-level security, trusted client-submitted prices, and tokens stored in localStorage. Supabase checks cover RLS policies, Stripe checks cover payment flows, and React Native checks look for secrets in the JS bundle.

## Installation

```bash
npx skills add https://github.com/raroque/vibe-security-skill --skill vibe-security
```

The same command works for Claude Code and OpenAI Codex; select the platform when prompted. Manual install copies the `vibe-security/` folder into `.claude/skills/` (project) or `~/.claude/skills/` (global).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| vibe-security | 3,869 | Security reference files loaded by stack: Supabase row-level security, Stripe payment flows, React Native bundle secrets, auth, rate limiting and AI output checks. |

No indexed listings fall below the threshold; the one indexed listing appears above.

## Why This Matters for Hermes Agents

AI assistants are fast at shipping features and consistently wrong on security: hardcoding secrets, skipping row-level security, trusting client-submitted prices. This skill catches those patterns before they ship.

Its stack-based loading is the differentiator. A project on Supabase gets RLS checks; a project on Stripe gets payment-flow checks; a React Native app gets bundle-secret checks. No context is spent on irrelevant rules, which matters for agents with limited working memory.

The checks are reference material plus a trigger prompt, not a scanner, so the value scales with how often the agent is asked to audit rather than write. That fits a Hermes workflow where review runs after generation.

## Usage

| You say | What happens |
|---|---|
| "Check my code for security issues" | The agent loads the reference files and audits the project for the listed patterns. |
| "Audit this project before we ship" | It runs a full security pass over the codebase against the applicable stack rules. |
| "Check my Supabase RLS policies" | It loads the database rules and reviews row-level security coverage. |
| "Review this Stripe integration" | It checks payment flows for client-submitted prices and missing webhook verification. |
| "Is this React Native bundle leaking secrets?" | It inspects for API keys and tokens shipped in the JS bundle. |
| "Review this for vulnerabilities" | It applies the auth, rate limiting and AI/LLM checks to the code at hand. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/raroque/vibe-security-skill/main/vibe-security/SKILL.md | head -40
npx skills add https://github.com/raroque/vibe-security-skill --skill vibe-security
```

The SKILL.md sits under `vibe-security/` in the repository; fetching it shows the reference files the skill will load.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| vibe-security | Pass | Pass | Pass |

The skill is Markdown reference material with no runtime dependencies or network calls, and all three auditors pass it.

## Limitations

- Snapshot data, verified 2026-11-15: 3,869 combined installs across 1 indexed listing; 1,235 GitHub stars; MIT; last pushed 2026-03-15. Counts drift over time.
- The last push predates this snapshot by more than eight months, so coverage lags newer framework and provider defaults.
- It is reference files plus a prompt, not a scanner: the host agent applies the rules during review.
- One skill means a single broad security surface rather than per-domain specialists.

## Related

- [Bagelhole DevOps Security Skills Setup](/hermes/skills/catalog/bagelhole-devops-security-skills-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)
- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Trigger the audit as part of the release flow so security checks run after generation, not only when prompted.
- Ask for the stack-specific check by name (Supabase RLS, Stripe, React Native) to avoid wasted context on irrelevant rules.
- Keep the skill installed globally if you work across several vibe-coded projects.
- Treat a passing review as a point-in-time check; re-run it after dependency or framework upgrades.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
