---
title: "Slavingia Skills - Minimalist Entrepreneur Business Suite"
description: "Sahil Lavingia's 10 book-based business skills: 26.3K combined installs for idea validation, MVPs, pricing, first customers and sustainable growth."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/slavingia-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "business", "founder"]
---

# Slavingia Skills - Setup Guide

Sahil Lavingia, the founder of Gumroad, published these 10 skills as the operating system for his book The Minimalist Entrepreneur. Each skill is a single Markdown file that tells the agent to act as a business advisor working one stage of the book's journey, from finding a community through pricing, selling, growing and reviewing decisions. There are no scripts, no CLI and no API keys.

The suite is unusually clean for a personal publisher: all 10 indexed listings map one to one onto a `skills/<name>/SKILL.md` directory in the current tree, so there is no index-versus-tree drift, and the whole repo is 10 skill files, a README and two Claude Code plugin manifests in `.claude-plugin/`.

**Source:** [slavingia/skills](https://www.skills.sh/slavingia/skills) via skills.sh - 26.3K combined installs across 10 indexed listings; first seen Mar 23, 2026
**GitHub:** [slavingia/skills](https://github.com/slavingia/skills) (10,983 stars; no LICENSE file, GitHub reports no license; branch main, pushed 2026-04-14; layout `skills/<name>/SKILL.md` for all 10 skills, plus `.claude-plugin/plugin.json` and `marketplace.json` registering the `minimalist-entrepreneur` plugin)
**Category:** Business / Founder Playbook
**Quality Tier:** 🟡 Beta - 10,983 stars and 26.3K installs, all 10 listings resolve to a real directory, and three sampled skills return Pass on all three scanners, but the repo carries no LICENSE file (the plugin manifest says MIT while GitHub reports none), the content is advisory prompt text with no scripts, evals or tests, and the last push was 2026-04-14

## Installation

```bash
# Install all 10 skills with the skills CLI
npx skills add slavingia/skills

# Or use the repo README's own Claude Code plugin path
/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur
```

```bash
# Alternative from the README: register a local clone as the marketplace
git clone https://github.com/slavingia/skills.git ~/.claude/plugins/skills
/plugin marketplace add ~/.claude/plugins/skills
/plugin install minimalist-entrepreneur
```

The only prerequisite is an agent that reads the Agent Skills format. There is no CLI, API key, environment variable or runtime to install, and no bundled dependency to update later.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| validate-idea | 2,992 | Test whether an idea is worth pursuing by selling a manual version first instead of building, with the book's validation checklist |
| mvp | 2,776 | Scope a minimum viable product through the book's three stages (manual, processized, productized) and cut scope when the build grows |
| first-customers | 2,640 | Build a plan for the first 100 customers with direct selling in concentric circles, instead of waiting for a launch |
| minimalist-review | 2,638 | Gut-check any decision, plan or strategy against the minimalist principles; accepts a free-text description of the situation |
| marketing-plan | 2,596 | Write a content-first marketing plan for a product with early traction, spending time before money |
| pricing | 2,574 | Set or change a price, covering the two pricing models and why charging from day one matters |
| find-community | 2,563 | Identify and evaluate the communities a business could be built around, starting from communities the founder already belongs to |
| grow-sustainably | 2,534 | Evaluate spending, hiring, fundraising and scaling decisions through profitability and runway |
| company-values | 2,496 | Define company values and culture before the first hire, in specific rather than generic language |
| processize | 2,488 | Turn a product idea into a manual service that can be delivered today, before any code is written |

No indexed listings fall below the threshold; all 10 appear above. Every listing name matches a directory in the current tree, so the install index and the repo agree exactly.

## Why This Matters for Hermes Agents

Business questions are where agents default to generic advice. Ask a bare model whether to raise money or raise prices and it will produce a balanced list of considerations. These skills replace that with a fixed procedure: state the principle, walk the framework, and end on a recommendation. The output is opinionated and traceable to a step, which is what an operator actually needs to act on.

The suite is also sequenced. The 10 skills follow the book's order (community, validate, build, processize, sell, price, market, grow, culture, review), and each skill's description names the moment it applies. That lets a router pick one stage instead of blending five, and it means a session can say plainly that a founder is trying to price a product before they have sold anything, which is a real ordering error the skills catch.

Operationally they are free to carry. Ten Markdown files, no shell calls, no network requests, no credentials in scope. Nothing runs until a prompt matches a description, so a global install costs context only when a business question is actually asked. For an agent that also holds production credentials and write access to a codebase, a skill family that cannot touch either is a safe default.

The honest caveat is that this is one operator's playbook, not market data. It will argue for profitability, direct sales and small scope even when a specific business has a reason to do otherwise. Treat it as a decision scaffold that forces a defensible answer, not as evidence about a market.

## Usage

| You say | What happens |
|---|---|
| "Is this idea worth building?" | Loads validate-idea, asks what has already been sold and to whom, and pushes for a manual sale before a build |
| "We keep adding scope to the MVP" | Loads mvp, walks the manual, processized and productized stages, and names what to cut for this release |
| "How should I price this at launch?" | Loads pricing, covers the two pricing models and argues for charging something from day one |
| "I have a product and no customers" | Loads first-customers, replaces the launch plan with a direct selling sequence for the first 100 |
| "Should we hire a second engineer?" | Loads grow-sustainably, tests the hire against runway and profitability rather than growth targets |
| "Gut-check this decision" | Loads minimalist-review with the situation as its argument and scores the decision against the book's principles |
| "What should our values be?" | Loads company-values and drafts specific values instead of two-word slogans, tied to how the team will actually work |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -iE "validate-idea|minimalist-review|processize"
```

Read the skills before installing. The five URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/slavingia/skills/main/README.md
curl -sL https://raw.githubusercontent.com/slavingia/skills/main/skills/validate-idea/SKILL.md
curl -sL https://raw.githubusercontent.com/slavingia/skills/main/skills/mvp/SKILL.md
curl -sL https://raw.githubusercontent.com/slavingia/skills/main/skills/processize/SKILL.md
curl -sL https://raw.githubusercontent.com/slavingia/skills/main/skills/minimalist-review/SKILL.md
```

The directory listing behind the install index also returned 200 on the same date:

```bash
curl -s https://api.github.com/repos/slavingia/skills/contents/skills | grep '"name"'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| validate-idea | Pass | Pass | Pass |
| mvp | Pass | Pass | Pass |
| minimalist-review | Pass | Pass | Pass |

The security surface here is close to zero, which is worth stating precisely. No SKILL.md declares an `allowed-tools` field, so no skill asks the host for shell, write or network permission of its own. The repo contains no scripts and no `references/` payloads; its only files are the 10 Markdown skills, a README and the two plugin manifests, so there is nothing executable to review. None of the skills read files, call an API or handle credentials; they instruct the model to reason about a business situation and reply in prose.

The one real gap is legal rather than technical. `.claude-plugin/plugin.json` declares `"license": "MIT"`, but the repository has no LICENSE file and GitHub reports no license for it, so the terms under which the text may be copied or redistributed are not actually stated. Treat the content as all rights reserved until the author adds a license, and do not republish the skill text or a derivative of it.

## Limitations

- No LICENSE file. The plugin manifest claims MIT, GitHub reports no license, and there is no license text in the repo, so the grant is unconfirmed.
- Advisory only. No skill in the suite reads data, queries a market, checks a competitor or writes a file, so every answer rests on what the operator tells it in the prompt.
- One book, one point of view. The frameworks argue for community first, manual delivery, profitability and small scope; a funded or capital-intensive business will get advice that does not fit.
- No test or eval suite. There is nothing in the repo that measures whether a skill produces a good answer, so quality is judged per conversation.
- The suite is static. Last push 2026-04-14, about six months before this snapshot, so no skill has been revised against newer model behaviour.
- Snapshot data, verified Oct 26, 2026: 26,297 combined installs across 10 indexed listings; 10,983 GitHub stars; no LICENSE file (GitHub reports no license); last pushed 2026-04-14. Counts drift over time.

## Related

- [Ognjen Founder Skills - Setup Guide](/hermes/skills/catalog/ognjengt-founder-skills-setup) - another small founder-playbook suite, useful as a second opinion on early-stage decisions.
- [Marketing Mindset - B2B Marketing OS for AI Agents Setup](/hermes/skills/catalog/marketing-mindset-setup) - deeper marketing machinery once the marketing-plan skill says there is traction.
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - the content planning layer that the marketing-plan skill only sketches.
- [A Smart Bear Skills - Positioning & PMF Suite Setup](/hermes/skills/catalog/asmartbear-skills-setup) - positioning and product-market-fit frameworks that pair with validate-idea and pricing.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install once globally. Ten Markdown files that never touch the network are the cheapest possible always-on advisor set, and they cost context only when matched.
- Say which stage you are at in the prompt. "I have 12 paying customers" routes to first-customers and pricing; leaving it out lets the agent pick the wrong stage.
- Use minimalist-review as the final gate on a plan the other skills produced. It is the only skill in the suite built to disagree with the rest.
- Treat the tier as Beta for a reason: quote the advice internally, but do not paste the skill text into a product or a public page while the license is unstated.
- Ask for the counter-argument explicitly. These skills are opinionated by design, and asking what would have to be true for the opposite choice is where they are most useful.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
