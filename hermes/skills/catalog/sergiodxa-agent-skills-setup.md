---
title: "Sergiodxa Agent Skills - Frontend Practice Setup"
description: "Setup guide for sergiodxa/agent-skills - 7.9K combined installs. Frontend testing, React, accessibility, and security best-practices skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sergiodxa-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "frontend", "react", "accessibility"]
---

# Sergiodxa Agent Skills - Setup Guide

**Source:** [sergiodxa/agent-skills](https://www.skills.sh/sergiodxa/agent-skills) via skills.sh - 7.9K combined installs across 11 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [sergiodxa/agent-skills](https://github.com/sergiodxa/agent-skills) (90 stars, MIT; pushed 2026-02-01; `skills/<name>/SKILL.md` layout)
**Category:** Frontend Engineering / Best Practices
**Quality Tier:** 🟡 Beta - independent (Sergio Xalambri); MIT; last pushed Feb 2026; all sampled verdicts Pass

Sergio Xalambri, an independent developer from the Remix and React ecosystem, publishes the agent skills he uses himself. The set skews frontend professional: testing best practices at the top of the index, an OWASP security check, React and React Router patterns, accessibility, Tailwind, async and internationalization guidance, plus two wildcards (Ruby on Rails, and a skill about writing skills). Each skill lives at `skills/<name>/SKILL.md` and installs independently.

Read the collection as a review layer rather than a generator: these skills give an agent checklists to press against real code, so the highest-value use is running them over diffs and pages before a human reviews. Install is one command through the skills CLI with Bun, and the README keeps it minimal: choose the ones you want as you go.

---

## Installation

Prerequisites: Bun, since the README installs through `bunx`; the same skills CLI also runs through `npx` in Node-only environments.

```bash
bunx skills add sergiodxa/agent-skills
```

The install prompt lets you choose which skills to add: pick what matches your stack and skip the rest.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| frontend-testing-best-practices | 2,175 | Testing best practices for frontend code and test suites |
| owasp-security-check | 1,649 | OWASP security check pass over an application |
| frontend-react-best-practices | 1,192 | React component, state, and code-organization practices |
| frontend-accessibility-best-practices | 822 | Accessibility practices for frontend interfaces |
| frontend-tailwind-best-practices | 460 | Tailwind CSS usage and structure practices |
| frontend-react-router-best-practices | 401 | React Router routing and data-loading patterns |

The remaining 5 indexed listings range from 173 to 329 installs.

## Why This Matters for Hermes Agents

Best-practice skills are the cheapest way to raise an agent's baseline, because they encode what to check rather than what to generate. This set is unusually cohesive: testing, security, React, accessibility, Tailwind, and routing are exactly the surfaces a frontend change touches, so an agent can load the relevant pair and review its own diff before a human ever sees it. Several of these skills come from an ecosystem author's working practice (Sergio Xalambri, who built in the Remix and React world), which tends to produce sharper checklists than generic advice. For Hermes agents, the practical pattern is a per-change review stack: frontend-testing-best-practices plus owasp-security-check on every pull request, with the accessibility and framework skills loaded when the diff touches UI or routing. Note the maintenance signal: the last push was Feb 2026, so recent framework conventions may lag, and the set is best treated as durable review heuristics rather than version-specific guidance.

## Usage

| You say | What happens |
|---|---|
| "Review this PR before I merge it" | frontend-testing-best-practices and owasp-security-check press their checklists against the diff |
| "Does this checkout flow have security holes?" | owasp-security-check runs an OWASP-style review over the app |
| "Check this component for React anti-patterns" | frontend-react-best-practices reviews component and state structure |
| "Audit the new settings page for accessibility" | frontend-accessibility-best-practices checks the interface against accessibility practices |
| "Is this Tailwind class soup salvageable?" | frontend-tailwind-best-practices suggests structure and usage fixes |
| "Review our router loaders before a refactor" | frontend-react-router-best-practices checks routing and data-loading patterns |

## Verification

```bash
# Confirm the install through the skills CLI
bunx skills list | grep -i frontend

# Or check the skills directory your agent scans
ls ~/.claude/skills/ | grep -E 'frontend-testing|owasp'

# Review the flagship skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/sergiodxa/agent-skills/main/skills/frontend-testing-best-practices/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frontend-testing-best-practices | Pass | Pass | Pass |
| frontend-react-best-practices | Pass | Pass | Pass |
| remix | - | - | - |

Both scored skills pass on all three engines; coverage is partial, so re-check the security pages on skills.sh before production use.

## Limitations

- Maintenance signal: last pushed Feb 2026, so newer framework conventions may not be reflected.
- Independent single-author collection; the scope is frontend practices, not tooling or automation.
- The below-threshold listings (Ruby on Rails, internationalization, and friends) carry less install pressure than the core set.
- Verdict coverage is partial; only two skills were scored.
- Snapshot data, verified Oct 10, 2026: 7,893 combined installs across 11 indexed listings; 90 GitHub stars; MIT; last pushed 2026-02-01. Counts drift over time.

## Related

- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup) - router and server-state patterns for React apps
- [Meticulous Agent Skills - Visual Regression Testing Setup](/hermes/skills/catalog/meticulous-agent-skills-setup) - visual regression testing to complement the testing skill
- [VueJS AI Skills - Vue Best Practices Suite Setup](/hermes/skills/catalog/vuejs-ai-skills-setup) - the same best-practices idea for Vue stacks
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load the review pair per diff: testing plus OWASP security on any pull request, then stack the framework skills that match the change.
- These skills are strongest as pre-commit or pre-review passes; run them on real diffs rather than asking for abstract advice.
- For accessibility, audit a rendered page with interactive states open (menus, dialogs), not just static markup.
- Treat version-sensitive advice with care: with a Feb 2026 last push, cross-check against current React, Tailwind, and Router docs.
- In a Bun environment, use the README's `bunx` command; the same skills CLI also runs through `npx` in Node-only setups.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
