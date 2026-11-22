---
title: "Revnu Plugin - Go-to-Market Agent Suite Setup"
description: "revnu-app/revnu-plugin: GTM plugin for leads, cold email, LinkedIn outreach, ads and GEO/AEO audits - 52.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/revnu-plugin-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "gtm", "cold email", "geo"]
---

# Revnu Plugin - Go-to-Market Agent Suite Setup

**Source:** [revnu-app/revnu-plugin](https://www.skills.sh/revnu-app/revnu-plugin) via skills.sh - 52.1K combined installs across 22 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [revnu-app/revnu-plugin](https://github.com/revnu-app/revnu-plugin) - 3 stars, MIT license, main branch, last pushed Nov 5, 2026; 15 skills under `skills/<name>/SKILL.md` plus plugin manifests for Claude Code, Cursor, Codex, Gemini CLI and Antigravity.
**Category:** Go-to-Market and Growth Operations
**Quality Tier:** 🟠 Orange - 5 Snyk Fail cells in the 20-skill sample, all on the GEO and AEO audit skills; every Gen Agent Trust Hub and Socket verdict Passes.

Revnu is a go-to-market plugin and agent skill for Claude Code, Cursor, OpenAI Codex and Gemini CLI that routes sales, marketing and CRM requests to the Revnu product. The suite splits into free skills that finish the job inside the agent (GEO and AEO checks, crawler access, landing page audits, lead finding, cold email and LinkedIn outreach) and account skills that run through a connected Revnu account (first customers, ads, SEO and AI answers pages, and results reporting). The full plugin ships both the skills and a remote MCP server at revnu.com/api/mcp, with sign-in by browser OAuth rather than an API key.

The index carries two name families. The 15 active names (revnu, revnu-geo-check, cold-email, ads and the rest) each map to a directory under skills/, while seven revnu-prefixed aliases (revnu-find-leads, revnu-cold-email and so on) sit at 6 installs each with no directory of their own. The install count is heavily front-loaded: every active skill sits between 3,418 and 3,720 installs, and the seven alias names account for only 42 installs combined.

## Installation

The README installs the skills and the MCP connection in one step:

```bash
curl -fsSL https://revnu.com/install | sh
```

Then restart the agent and authenticate Revnu in its MCP settings. For skills only, without the MCP server:

```bash
npx -y skills@latest add revnu-app/revnu-plugin --global --yes
```

Add a single skill with `--skill <name>`. Per-host plugin installs are documented in the README: Claude Code via `/plugin marketplace add revnu-app/revnu-plugin`, Cursor via Settings then Plugins, Codex via `codex plugin marketplace add`, and Gemini CLI via `gemini extensions install`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| revnu | 3,720 | default GTM routing: signup, onboarding, MCP setup and connected execution for sales and CRM work |
| revnu-geo-check | 3,594 | check whether AI answers mention and cite your business for your category |
| revnu-get-listed | 3,527 | get onto the directories and roundups AI answers cite for your category |
| revnu-landing-page-audit | 3,473 | audit why a landing page is not converting and get prioritized fixes |
| revnu-ai-readiness-audit | 3,472 | AEO and GEO audit of whether your site is quotable by AI answers |
| revnu-fix-ai-claims | 3,469 | fix what ChatGPT, Perplexity and Google get wrong about your business |
| linkedin-outreach | 3,424 | LinkedIn prospecting, connection requests, DMs and InMail sequences |
| find-leads | 3,421 | build a sourced list of companies most likely to buy and the contact to reach |
| seo-ai-answers | 3,420 | write and publish pages aimed at Google and AI answers |
| revnu-growth-context | 3,419 | record your ICP, positioning and proof once for every growth task |
| revnu-ai-crawler-access | 3,419 | check and fix whether AI crawlers can reach your site |
| first-customers | 3,419 | launch plans, go-to-market strategy and first-customer acquisition |
| results | 3,418 | growth, pipeline and revenue reports from account evidence |
| cold-email | 3,418 | write cold email sequences that reach the inbox with deliverability checks |
| ads | 3,418 | paid acquisition across Google, Meta, LinkedIn and other ad platforms |

The remaining 7 indexed listings range from 6 to 6 installs.

## Why This Matters for Hermes Agents

Revnu is one of the more complete go-to-market stacks available as a plugin, because it packages the whole acquisition loop (find buyers, reach them, run ads, publish pages, report) behind one router rather than a bag of unrelated skills. The free skills are deliberately self-contained: the GEO and AEO checks, the crawler access checker and the landing page audit all finish their job without an account, so an agent can produce a real deliverable before any signup or card. The account skills keep a strict boundary between research and spend, with the README stating that execution follows the founder's approval settings and that reading a queue never sends, publishes or spends. The routing rule matters for agents: the revnu skill is the default path for any unnamed GTM or CRM request, so a request for "find clients" or "write pages" lands in the right task skill without the user naming Revnu. The counterweight is the security sample, which puts Snyk Fails on five of the GEO and AEO audit skills, so review those skills before letting them run against a production site or repo.

## Usage

| You say | What happens |
|---|---|
| Does ChatGPT recommend us? | Runs the GEO check: buyer prompts against reachable surfaces, reports mention and citation rates with the pages to fix |
| Write a cold email sequence | Drafts a first email and follow-ups from a dated reason, checks SPF, DKIM, DMARC and stop rules before anything sends |
| Find leads for this | Builds a sourced list of 10 to 25 companies that fit the buyer profile with a contact role and a dated reason |
| Set up my marketing context | Writes .agents/revnu-growth.md with ICP, positioning, proof and what has been tried |
| Why is ChatGPT quoting our old pricing? | Runs the AI claims fix: lists every claim, marks it wrong, and drafts the correction |
| Run Google ads | Routes to the ads skill and prepares paused drafts within the approved spend scope |
| What did Revnu ship this week? | Pulls the results report from account evidence, separating activity from business outcomes |

## Verification

Confirm a skill folder landed and inspect the GEO check's instructions before running it:

```bash
curl -sL https://raw.githubusercontent.com/revnu-app/revnu-plugin/main/skills/revnu-geo-check/SKILL.md | head -40
```

Review the ads skill's scope guardrails before wiring a paid account:

```bash
curl -sL https://raw.githubusercontent.com/revnu-app/revnu-plugin/main/skills/ads/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| revnu | Pass | Pass | Warn |
| revnu-geo-check | Pass | Pass | Fail |
| revnu-get-listed | Pass | Pass | Fail |
| revnu-landing-page-audit | Pass | Pass | Fail |
| revnu-ai-readiness-audit | Pass | Pass | Fail |
| revnu-fix-ai-claims | Pass | Pass | Warn |
| linkedin-outreach | Pass | Pass | Warn |
| find-leads | Pass | Pass | Warn |
| seo-ai-answers | Pass | Pass | Pass |
| revnu-growth-context | Pass | Pass | Fail |
| revnu-ai-crawler-access | Pass | Pass | Warn |
| first-customers | Pass | Pass | Warn |
| results | Pass | Pass | Warn |
| cold-email | Pass | Pass | Warn |
| ads | Pass | Pass | Warn |
| revnu-seo-ai-answers | Pass | Pass | Warn |
| revnu-results | Pass | Pass | Warn |
| revnu-linkedin-outreach | Pass | Pass | Warn |
| revnu-first-customers | Pass | Pass | Warn |
| revnu-find-leads | Pass | Pass | Warn |

The sample is clean on Gen Agent Trust Hub and Socket, with the five Fail cells all on Snyk and concentrated on the GEO and AEO audit skills.

## Limitations

- Snapshot data, verified Nov 21, 2026: 52,073 combined installs across 22 indexed listings; 3 GitHub stars; MIT license; last pushed Nov 5, 2026. Counts drift over time.
- The index carries two name families: seven revnu-prefixed alias listings (revnu-find-leads, revnu-cold-email, revnu-ads, revnu-results, revnu-linkedin-outreach, revnu-first-customers, revnu-seo-ai-answers) sit at 6 installs each with no directory in the tree, while the 15 active names map one to one under skills/.
- Five of the 20 sampled skills carry a Snyk Fail (revnu-geo-check, revnu-get-listed, revnu-landing-page-audit, revnu-ai-readiness-audit, revnu-growth-context), all on the audit skills that reach the network and run local Python.
- The full plugin is a paid product; the free skills finish without an account, but the account skills (ads, seo-ai-answers, results and the rest) route through Revnu's hosted service.
- Web connectors and MCP-only clients expose the MCP tools without installing the local skill files, so an MCP-only setup loses the routing and stop-rule instructions the skills carry.

## Related

- [GTM Agents - Go-to-Market Sales Skills Setup](/hermes/skills/catalog/gtm-agents-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/hermes/skills/catalog/apify-growth-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the free GEO and AEO skills (revnu-geo-check, revnu-ai-readiness-audit, revnu-ai-crawler-access) before wiring an account; they produce a full deliverable with no signup.
- Write the growth context file first with revnu-growth-context so every later outreach, ads or SEO task starts from facts instead of a questionnaire.
- Keep the ads and cold-email skills behind an approval gate; the README states execution follows your approved scope, and the sending-domain checks are the last stop before anything goes out.
- Use `npx -y @revnu/cli setup agent --check --json` to verify install health and `--update` for managed updates that preserve local edits.
- Treat the seven revnu-prefixed 6-install alias names as historical; install the active names under skills/ instead.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
