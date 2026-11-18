---
title: "OpenCode Skills - Interface Design and Review Suite Setup"
description: "osmontero/opencode-skills: 5.7K combined installs across 35 listings; interface design and review skills plus engineering rigor workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/opencode-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "interface design", "code review", "opencode"]
---

# OpenCode Skills - Setup Guide

**Source:** [osmontero/opencode-skills](https://www.skills.sh/osmontero/opencode-skills) via skills.sh - 5.7K combined installs across 35 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 18 stars, MIT license, `main` branch, last pushed 2026-11-17, 33 skills under `skills/` plus 11 agents under `agents/`
**Category:** Interface design and review / agent engineering workflows
**Quality Tier:** 🟡 Yellow - 55 Pass and 5 Warn across the 20 sampled listings; no Fail.

osmontero/opencode-skills adapts skills and agents for the OpenCode agent ecosystem. The most-installed skills are interface design and review: designing-frontend-interfaces (776) and designing-user-experience (575) lead, with reviewing-interface-quality and building-accessible-interfaces close behind. The engineering side covers debugging, testing, security review, performance investigation, schema evolution, and plan execution.

The repository is MIT, but individual skills carry separate attribution. Several are Apache 2.0 adaptations from Anthropic's Claude skills, others are MIT adaptations of obra/superpowers, and the remainder are original MIT, each with its own `LICENSE.txt`. Eleven agents run implementation, review, and evaluation roles, including `interface-reviewer` and `security-reviewer`.

## Installation

The README installs the whole suite with a shell script:

```bash
git clone https://github.com/osmontero/opencode-skills.git
./install.sh
```

Or install manually:

```bash
cp -r skills/* ~/.config/opencode/skills/
cp agents/* ~/.config/opencode/agents/
```

A PowerShell installer (`install.ps1`) ships alongside the shell script. Skills land in `~/.config/opencode/skills/`, agents in `~/.config/opencode/agents/`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| designing-frontend-interfaces | 776 | Design and restyle web interfaces: landing pages, dashboards, marketing sites, with tokens, type, color, and motion. |
| designing-user-experience | 575 | Design interface behavior: user flows, navigation, forms, data tables, and loading/empty/error states. |
| reviewing-interface-quality | 450 | Audit and critique existing UIs as the final gate before shipping frontend work. |
| building-accessible-interfaces | 438 | Build or audit web UIs for WCAG 2.2 AA accessibility: keyboard, screen readers, ARIA, contrast. |
| systematic-debugging | 200 | Investigate bugs and test failures with root-cause tracing before proposing fixes. |
| testing-webapps | 191 | Test local web apps with Playwright: verify frontend behavior, capture screenshots, view browser logs. |
| verifying-before-completion | 185 | Run verification commands and confirm output before claiming work is complete or creating PRs. |
| reviewing-security | 183 | Review code for security before merge: traced exploit paths, secrets, auth, SQL, outbound requests. |

The remaining 27 indexed listings range from 28 to 150 installs.

## Why This Matters for Hermes Agents

The design cluster is the reason this suite is notable. Four skills compose into a full interface workflow: designing-frontend-interfaces handles visual craft with tokens, type, color, and motion; designing-user-experience handles behavior with flows, forms, and the empty/loading/error state matrix; building-accessible-interfaces applies WCAG 2.2 AA; and reviewing-interface-quality ties them together as a critique rubric with an evidence requirement and severity grading. That gives an agent a repeatable path from a blank page to a shipped, reviewed, accessible interface instead of a one-shot "make it look better" prompt.

The same discipline extends past design. reviewing-security refuses a finding without a traced path from attacker-controlled input to impact, and investigating-performance refuses an optimization without a measurement that names the bottleneck. For an agent that tends to claim completion early, verifying-before-completion requires running the verification commands and confirming their output before any success claim.

## Usage

| You say | What happens |
|---|---|
| "Design a landing page for our launch" | designing-frontend-interfaces applies tokens, type, color, and motion to produce a polished, distinctive page. |
| "Review this dashboard before we ship" | reviewing-interface-quality audits visual, UX, and accessibility with an evidence requirement and severity grading. |
| "Make this form accessible" | building-accessible-interfaces checks keyboard, screen readers, ARIA, and contrast against WCAG 2.2 AA. |
| "This page loads slowly" | investigating-performance requires a measurement naming the bottleneck before any optimization. |
| "Test this web app" | testing-webapps drives Playwright to verify behavior and capture screenshots. |
| "Review this code for security" | reviewing-security traces a path from attacker-controlled input to impact before accepting a finding. |

## Verification

Confirm the two highest-install skills exist on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/osmontero/opencode-skills/main/skills/designing-frontend-interfaces/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/osmontero/opencode-skills/main/skills/reviewing-interface-quality/SKILL.md
```

Skills live at `skills/<name>/SKILL.md`; agents live at `agents/<name>.md`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| designing-frontend-interfaces | Pass | Pass | Pass |
| designing-user-experience | Pass | Pass | Pass |
| reviewing-interface-quality | Pass | Pass | Pass |
| building-accessible-interfaces | Pass | Pass | Warn |
| systematic-debugging | Pass | Pass | Pass |
| testing-webapps | Pass | Warn | Warn |
| verifying-before-completion | Pass | Pass | Pass |
| reviewing-security | Pass | Pass | Warn |
| test-driven-development | Pass | Pass | Pass |
| investigating-performance | Pass | Pass | Pass |
| applying-themes | Pass | Pass | Pass |
| writing-plans | Pass | Pass | Pass |
| brainstorming | Pass | Pass | Pass |
| dispatching-parallel-agents | Pass | Pass | Pass |
| evolving-apis-and-schemas | Pass | Pass | Pass |
| requesting-code-review | Pass | Pass | Pass |
| executing-plans | Pass | Pass | Pass |
| receiving-code-review | Pass | Pass | Warn |
| subagent-driven-development | Pass | Pass | Pass |
| building-mcp-servers | Pass | Pass | Pass |

The sample covers 20 of the 35 indexed listings; five of the sixty verdict cells are Warn (Socket or Snyk), the rest Pass, and no skill fails.

## Limitations

- Snapshot data, verified 2026-11-17: 5,739 combined installs across 35 indexed listings; 18 GitHub stars; MIT; last pushed 2026-11-17. Counts drift over time.
- The install index lists 35 listings, but the current tree ships 33 SKILL.md directories. Two indexed listings, creating-slack-gifs and configuring-opencode, have no matching skill directory in the tree.
- The skills target the OpenCode agent ecosystem; the installer copies into `~/.config/opencode/`, so other agent runtimes need manual wiring.
- Skills mix licenses: the repository is MIT, but individual skills carry Apache 2.0 or third-party MIT attribution in per-skill `LICENSE.txt` files.
- skills.sh sampled 20 of 35 listings for verdicts; the other 15 carry no verdicts here.

## Related

- [OpenCode Workflows - Command and Agent Template Suite Setup](/hermes/skills/catalog/opencode-workflows-setup)
- [Codex - Delegate Coding Tasks to OpenAI Codex CLI](/hermes/skills/catalog/codex-setup)
- [Awesome Cursor Skills - Cursor Agent Setup](/hermes/skills/catalog/awesome-cursor-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Compose the design cluster in order: designing-frontend-interfaces for look, designing-user-experience for behavior, building-accessible-interfaces for a11y, then reviewing-interface-quality as the ship gate.
- Use the interface-reviewer and security-reviewer agents to run their rubrics instead of reviewing inline.
- Run `./install.sh`, or copy `skills/*` and `agents/*` manually; both target `~/.config/opencode/`.
- Check each skill's `LICENSE.txt` before redistributing; several are Apache 2.0 or third-party MIT adaptations.
- Reach for verifying-before-completion before any "done" claim; it requires running the verification commands and showing output.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
