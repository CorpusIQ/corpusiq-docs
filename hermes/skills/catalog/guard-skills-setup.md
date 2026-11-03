---
title: "Guard Skills - Code Safety Review Pack"
description: "amelnagdy/guard-skills: 18.1K combined installs. Five second-pass review guards for AI-written code, tests, docs, WordPress and WooCommerce."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/guard-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "wordpress", "woocommerce", "quality gates"]
---

# Guard Skills - Setup Guide

**Source:** [amelnagdy/guard-skills](https://www.skills.sh/amelnagdy/guard-skills) via skills.sh - 18.1K combined installs across 5 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [amelnagdy/guard-skills](https://github.com/amelnagdy/guard-skills) - 1,301 stars, MIT, branch master, last pushed 2026-07-04; 5 `SKILL.md` directories under `skills/`, one per guard, each with an `agents/openai.yaml` metadata file and a `references/` folder

**Category:** Guardrail review for agents: destructive-command checks, secret handling and safe-change discipline

**Quality Tier:** 🟢 Green - all five sampled verdicts are Pass on Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE

This is a deliberately narrow pack: five review gates that run after an agent has produced work, not five skills that teach an agent how to build. The README states the intended order plainly, let your agent do the work and then invoke the relevant guard on the diff before you present, commit or merge it, and says the guards can guide writing when explicitly asked but are strongest as reactive review passes.

The division of labour is clean. `clean-code-guard` covers production code in any language and targets LLM-specific smells: over-abstraction, broad error swallowing, bad names, and SOLID, DRY, KISS and YAGNI violations. `test-guard` covers test code and targets mock abuse, duplicated tests, implementation-detail assertions and tests that catch nothing. `docs-guard` treats documentation as a list of claims and verifies each against the codebase. `wp-guard` and `woo-guard` are the platform pair: WordPress escaping, sanitization, nonces, capabilities and prepared queries, and on top of that WooCommerce order access, HPOS compatibility, checkout validation and money handling.

What makes the set usable is the routing rather than the rules. Every guard names its own boundary and the skill to use instead, so `clean-code-guard` points at `test-guard` for test review, `wp-guard` points at `woo-guard` when WooCommerce APIs appear, and `woo-guard` points back at `wp-guard` for WordPress code without Woo APIs. An agent that loads one guard gets told when it has loaded the wrong one.

## Installation

The README documents the skills CLI, starting with a listing pass that shows what the package contains:

```bash
npx skills add amElnagdy/guard-skills --list
```

Then the package, all five guards:

```bash
npx skills add amElnagdy/guard-skills
```

Or one guard at a time, which is the sensible route when only one review pass is wanted:

```bash
npx skills add amElnagdy/guard-skills --skill clean-code-guard
npx skills add amElnagdy/guard-skills --skill docs-guard
```

The README also documents an agent-specific form and a global install:

```bash
npx skills add amElnagdy/guard-skills --skill clean-code-guard --agent codex
npx skills add amElnagdy/guard-skills --skill '*' --agent cursor
npx skills add amElnagdy/guard-skills --global
```

Because skills install as a copy, the README is explicit that updates do not arrive on their own, and documents the refresh commands:

```bash
npx skills update
npx skills update clean-code-guard
```

The manual route is a flat copy, since all five skills sit one level under `skills/` and share one shape:

```bash
git clone --depth 1 https://github.com/amelnagdy/guard-skills.git /tmp/guard-skills
cp -r /tmp/guard-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Each skill directory holds `SKILL.md`, `agents/openai.yaml` and a `references/` folder. The README says the `SKILL.md` stays small so it loads cheaply and the deeper guidance loads only when the task needs it, which means the `references/` folder has to travel with the skill or the guard loses most of its rules.

There are no runtime dependencies and no configuration step. The package is markdown plus `agents/openai.yaml`, and the README states there are no executable scripts, network calls, MCP server dependencies or credentials.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| clean-code-guard | 4,746 | Production code in any language, reviewed after an agent writes or refactors it: LLM code smells, over-abstraction, broad error swallowing, bad names, and SOLID, DRY, KISS and YAGNI violations. |
| test-guard | 4,215 | Test code in pytest, PHPUnit or Pest, Jest or Vitest, Go and WordPress: mock abuse, duplicate tests, implementation-detail assertions and tests that catch nothing, with a nine-rule core set. |
| docs-guard | 4,013 | READMEs, API references, docstrings, PHPDoc and JSDoc, changelogs and tutorials: hallucinated symbols, broken samples, docs-versus-code drift, and unverifiable claims such as performance adjectives. |
| wp-guard | 2,606 | WordPress plugins, themes, blocks, REST routes, AJAX handlers, shortcodes, queries and WP-CLI code: escaping and sanitization, nonce plus capability checks, prepared queries, core APIs first, translatable strings and query caching. |
| woo-guard | 2,542 | WooCommerce extensions, gateways, shipping, checkout and order or product logic: HPOS-safe order access, CRUD over direct meta, truthful feature-compatibility declarations, server-side checkout validation and money handling. |

All 5 indexed listings clear the 0-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

The failure modes these guards target are the ones that survive a passing test suite. An agent that wraps everything in `try/catch` and returns a success object produces green tests and a service that hides its errors; an agent that mocks its own state objects produces tests that assert the mock; an agent that writes a README from memory produces documentation for functions it never checked. A general code review prompt catches some of this. A guard with nine named rules, a fixed output shape and a boundary against the adjacent skill catches more, because it is looking for specific patterns rather than assessing quality in the abstract.

The WordPress pair is the strongest part of the pack for a specific reason: WordPress review is where generic advice fails hardest. `wp-guard` enforces the layer that clean-code guidance misses, escaping and sanitization, a real permission callback on a writing REST route, prepared queries, translation-ready strings, and not handing a million-row site `posts_per_page => -1`. `woo-guard` then adds the WooCommerce-specific rules that break shops silently, HPOS-safe order access, CRUD over direct meta, and a truthful compatibility declaration.

For a Hermes profile, the practical gain is a repeatable second pass. The guards are cheap to load, the deeper references only come in when a framework-specific case appears, and the review is read-only by design, so the guard cannot make the change it is reviewing. That is the right shape for an automated review step in a delivery pipeline.

## Usage

| You say | What happens |
|---|---|
| "Review the diff you just produced" | `clean-code-guard` runs the LLM smell checks against production code and returns rule-by-rule fixes rather than a general impression. |
| "Check these tests before I merge them" | `test-guard` flags mock abuse, duplicated test bodies, implementation-detail assertions and tests that would pass with the code broken. |
| "Is this README accurate" | `docs-guard` treats each statement as a claim, checks referenced functions, flags, config keys and samples against the source, and strips unverifiable claims. |
| "Review this WordPress plugin before we ship it" | `wp-guard` checks escaping, nonces, capability checks, prepared queries, i18n and query caching, and hands off to `woo-guard` if WooCommerce APIs appear. |
| "Is this checkout change HPOS compatible" | `woo-guard` checks order access against HPOS, direct meta usage, compatibility declarations and server-side validation. |
| "Use wp-guard while you implement this REST endpoint" | The guard runs as a writing constraint rather than a review pass, with a self-check before delivery. |

## Verification

The raw path for `clean-code-guard` returned HTTP 200 on branch master when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} clean-code-guard\n" \
  https://raw.githubusercontent.com/amelnagdy/guard-skills/master/skills/clean-code-guard/SKILL.md
```

Expect `200`. After the copy lands, confirm all five guards arrived with their references:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/*-guard/ | wc -l
head -5 ~/.hermes/profiles/corpusiq/skills/clean-code-guard/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/wp-guard
```

The count should print 5, the header should show `name: clean-code-guard`, and the `wp-guard` listing should show `SKILL.md`, `agents` and `references`.

## Security

Every sampled skill passes every verdict, which is why this pack is Green rather than Yellow.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| clean-code-guard | Pass | Pass | Pass |
| test-guard | Pass | Pass | Pass |
| docs-guard | Pass | Pass | Pass |
| wp-guard | Pass | Pass | Pass |
| woo-guard | Pass | Pass | Pass |

The repository is inspectable in a way that is rare for a skill pack, and the README says so: skill content is Markdown plus lightweight `agents/openai.yaml` metadata, there are no executable scripts, network calls, MCP server dependencies or credentials, and the only external URLs sit in each skill's `references/sources.md`. That is 35 files across the five skills, all readable, with nothing to execute and nothing to install beyond the copy.

The license is MIT under a named copyright holder, which is the permissive end of the range and the reason the tier carries no license caveat. Keep the `LICENSE` file with any redistribution.

The remaining risk is behavioural rather than technical. These guards advise and do not enforce: they cannot block a merge, and their verdicts are text an agent can ignore. Pair them with a real linter and CI gate where the rules matter, and use the guards for the judgement-shaped part of review that linters do not cover.

## Limitations

- Snapshot data, verified 2026-10-31: 18,122 combined installs across 5 indexed listings; 1,301 GitHub stars; MIT; last pushed 2026-07-04. Counts drift over time.
- The pack is small and unevenly weighted. Two of the five guards are WordPress-specific and one is WooCommerce-specific, so a profile that does not ship PHP gets three of five.
- The last push is 2026-07-04, roughly four months before this sweep, so the WordPress and WooCommerce rules reflect that snapshot rather than the current release cycle.
- Guards are review prompts, not enforcement. Nothing here fails a build, blocks a commit or rewrites code, and the README frames them as second-pass gates that a human or a pipeline still has to act on.
- Coverage stops at the four domains named. There is no guard for infrastructure code, SQL migrations or frontend component libraries, so the pack complements a general review process rather than replacing it.
- The install index and the tree agree here, all five listings map to five directories, which also means there are no unindexed skills to discover in the current tree.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Asyraf Hussin Skills - Clean Code Suite](/hermes/skills/catalog/asyrafhussin-agent-skills-setup)
- [OrchestKit - Orchestration and DevOps Skills](/hermes/skills/catalog/orchestkit-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the guard on the diff, not on the plan. The README's framing is that these catch failure modes in work already produced, and reviewing a diff gives the guard something concrete to check.
- Install all five even if two are WordPress only. The boundary rules matter: `clean-code-guard` sends test review to `test-guard` and `wp-guard` sends WooCommerce work to `woo-guard`, so the routing only works when both ends are present.
- Copy the whole skill directory. `SKILL.md` is intentionally short and the framework rules live in `references/`, so a bare file copy removes the progressive disclosure that keeps the load cheap.
- Use `docs-guard` before publishing anything public. It verifies claimed functions, flags and config keys against the source and removes unverifiable claims, which is cheaper than a correction later.
- Refresh with `npx skills update` on a schedule. Skills install as a copy, so a fix in the repository never reaches the profile on its own.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
