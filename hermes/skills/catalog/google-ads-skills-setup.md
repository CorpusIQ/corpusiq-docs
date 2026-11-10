---
title: "Google Ads Skills - Paid Search Playbooks for Agents"
description: "eliasmalmsandberg/google-ads-skills on skills.sh: 4.9K combined installs; Google Ads audit, bidding and ad copy playbooks for agents"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/google-ads-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "google ads", "paid search", "ppc", "advertising"]
---

# Google Ads Skills - Setup Guide

**Source:** [eliasmalmsandberg/google-ads-skills](https://www.skills.sh/eliasmalmsandberg/google-ads-skills) via skills.sh - 4.9K combined installs across 20 indexed listings; sampled 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 14 stars, MIT licensed, `main` branch, last pushed 2026-07-27, 21 `SKILL.md` files in a compact repository of 28 blobs, one directory per skill under `skills/google-ads-*/`
**Category:** Paid media: Google Ads account structure, bidding, ad copy, keyword and search term analysis
**Quality Tier:** 🟡 Solid with caveats - MIT licensed and mostly Pass verdicts, but the publisher repository is small and the sample carries one Snyk Warning.

This is a small, single-purpose repository: 21 Google Ads playbooks written for agents, one per job, with no runtime code and no bundled connector. The README is direct about the division of labour. A data connector gives the agent access to live account data, and these skills give it the domain expertise to do something with that data. The connector is a separate decision, and the README compares three routes: Windsor MCP for the fastest setup with no API tokens, Supermetrics MCP if the team already pays for it, and the official Google Ads MCP for full GAQL control at the cost of a longer setup.

The skills are written as task playbooks rather than campaign overviews, and they are deliberately interconnected. Search term mining feeds negative keyword work, conversion tracking is described as a prerequisite for bidding decisions, and attribution is treated as something that changes how Smart Bidding performs rather than a reporting curiosity. The README frames the whole set around four questions an operator actually asks: what to fix after an audit, which search terms spend without converting, why CPA moved this week, and what belongs on a negative list.

The repository is small in every sense. Fourteen stars, 21 skill directories, 28 blobs in total, and a last push of 2026-07-27. That is not a reason to skip it, but it does mean the material reflects Google Ads as of that date and has not been maintained through the platform's more recent changes.

## Installation

The README's install line adds the whole set:

```bash
npx skills add eliasmalmsandberg/google-ads-skills
```

Individual skills can be taken one at a time, which is what the skills.sh pages show:

```bash
npx skills add https://github.com/eliasmalmsandberg/google-ads-skills --skill google-ads-account-audit
```

There is no plugin, no CLI and no MCP server in this repository. The second half of a working setup is the data connection, chosen and configured outside the skill install:

- Windsor MCP, described in the README as the fastest route, with no API tokens and coverage of 325+ platforms, estimated at 10 to 15 minutes.
- Supermetrics MCP, for teams already on Supermetrics, covering 200+ platforms, estimated at 10 to 20 minutes.
- The official Google Ads MCP, for full GAQL control with no third-party cost, estimated at 30 to 60 minutes.

The README keeps setup notes for each under `setup/`, and a `getting-started.md` walkthrough covers the three options with screenshots and troubleshooting. Whichever connector you choose, the agent needs it available in the same session as the skills, or the playbooks have no account data to work from.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear in the table:

| Skill | Installs | Use For |
|---|---|---|
| google-ads-ad-copy | 422 | RSA headlines and descriptions, headline frameworks, value propositions and copy matched to search intent |
| google-ads-quality-score | 375 | Diagnosing Quality Score by component (Expected CTR, Ad Relevance, Landing Page Experience) and reducing CPCs |
| google-ads-search-term-mining | 364 | Mining search term reports for keyword opportunities, intent signals and structural insights |
| google-ads-bidding | 357 | Smart Bidding strategy choice (tCPA, tROAS, maximise conversions), manual CPC and portfolio strategies |
| google-ads-account-audit | 352 | Full account audit with fixes ranked by financial impact and a first-30-days takeover plan |
| google-ads-audiences | 338 | RLSA, Customer Match, in-market and lookalike audiences, plus exclusions and bid layering |
| google-ads-anomaly-detection | 335 | Diagnosing CPA spikes, conversion rate drops and spend surges, and setting up proactive monitoring |
| google-ads-budget-management | 334 | Budget pacing, allocation, shared budgets and fixing underspend or overspend |
| google-ads-segmentation | 328 | Device, geo and dayparting analysis with bid adjustments and campaign splits |
| google-ads-ad-extension-audit | 326 | Extension coverage matrix, sitelink and callout quality checks and a prioritised fix list |
| google-ads-conversion-tracking | 168 | Google Tag, Tag Manager, enhanced conversions, offline conversion import and conversion action audits |
| google-ads-keywords | 167 | Keyword research, match type strategy, intent classification and keyword architecture |
| google-ads-negative-keywords | 163 | Building negative lists from search terms to cut wasted spend and prevent cannibalisation |
| google-ads-audit-leadgen | 145 | CPL, lead volume and quality, form conversion, offline imports and B2B targeting |
| google-ads-audit-ecommerce | 131 | ROAS, product feed health, Shopping and Performance Max structure, cart abandonment and seasonality |
| google-ads-attribution | 123 | Attribution models, data-driven attribution, windows and their effect on Smart Bidding |
| google-ads-ad-extensions | 120 | Sitelinks, callouts, snippets, call, lead form, image, price, promotion, location and app assets |
| google-ads-utm-generator | 119 | UTM templates, dynamic values, naming conventions and GA4 channel grouping |
| google-ads-scripts | 118 | JavaScript automation for budget monitoring, keyword pausing, Quality Score tracking and reporting |
| google-ads-keyword-cannibalization | 115 | Finding campaigns competing in the same auction, costing the overlap and routing queries |

No indexed listings fall below the threshold; all 20 appear above.

The table is a snapshot of a 21-skill repository: `google-ads-experiments` exists in the tree at `skills/google-ads-experiments/` but is not among the 20 listings rendered on the skills.sh source page, so its installs are not counted here. Within the rendered set, ten skills sit between 326 and 422 installs and ten between 115 and 168, which is a remarkably flat distribution. There is no flagship skill; the set is used as a set.

## Why This Matters for Hermes Agents

Paid search is a domain where a general model produces confident, generic advice. "Improve ad relevance" and "review your bids" are true and useless. These skills replace that with procedures: which components make up Quality Score and what to change for each, how to build a negative list from a search term report, which Smart Bidding strategy fits a conversion volume, what an extension coverage matrix should contain. That specificity is the value, and it is why the set is worth installing whole rather than cherry-picking.

The interconnection is the second reason. An agent asked to "reduce wasted spend" will usually jump to negatives. The chain that actually works starts at search term mining, moves to intent classification, then to negatives, then to cannibalisation checks so the new list does not starve a campaign that was legitimately bidding. Having all four playbooks present means the agent can follow that chain instead of stopping at the first plausible action.

The audit skills are the ones to reach for first on an unfamiliar account. The account audit, the ecommerce audit and the lead gen audit each rank findings by financial impact, which is the right output for a human who has to decide what to fix on Monday.

The limitation is structural rather than editorial: these are markdown playbooks with no data access of their own. Without a connector the agent can still explain the method, but it cannot audit anything, and it will fill the gap with assumptions if you let it. Wire the connector first, then ask for the audit.

## Usage

| You say | What happens |
|---|---|
| "Audit this account and tell me the top five fixes" | `google-ads-account-audit` reviews structure, targeting, bids and budgets, ranks findings by financial impact and returns a first-30-days plan |
| "Which search terms spent money with no conversions last month?" | `google-ads-search-term-mining` pulls the report, classifies intent and surfaces the zero-conversion spenders, then hands candidates to negative keyword work |
| "Build a negative keyword list from last month" | `google-ads-negative-keywords` turns the mined terms into a list, checks for cannibalisation risk and explains the match types used |
| "My CPA went up 40 percent this week" | `google-ads-anomaly-detection` checks the usual causes (budget, bidding, competition, tracking) before recommending a change |
| "Why is my Quality Score stuck at 4?" | `google-ads-quality-score` separates Expected CTR, Ad Relevance and Landing Page Experience, then points at the matching playbook for the weak component |
| "Write RSA headlines for this ad group" | `google-ads-ad-copy` produces headlines and descriptions from intent-matched frameworks, with character counts that fit the limits |
| "Is our ecommerce account structured properly?" | `google-ads-audit-ecommerce` reviews ROAS, feed health, Shopping and Performance Max structure, and cart abandonment retargeting |

## Verification

The raw skill file sits one level down in `skills/`, and this URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/eliasmalmsandberg/google-ads-skills/main/skills/google-ads-ad-copy/SKILL.md | head -6
```

The frontmatter should declare `name: google-ads-ad-copy` and a description that starts "When the user wants help writing, improving, or auditing Google Ads ad copy", and the body should open with the copy frameworks and trigger phrases. Every other listing follows the same `skills/<name>/SKILL.md` layout, so the path pattern is safe to reuse.

After install, confirm the skill landed as a directory containing `SKILL.md`:

```bash
test -f ~/.claude/skills/google-ads-ad-copy/SKILL.md && echo ok
```

If your agent reads the Hermes profile directory instead, check `~/.hermes/profiles/corpusiq/skills/google-ads-ad-copy/SKILL.md`. Note that this repository has no plugin or CLI of its own, so the skills directory is the only install artifact and there is nothing else to verify.

The setup that does need verification is the connector. Before trusting any audit output, ask the agent one question that requires live data, for example "how many conversions did the account record yesterday", and check that the answer cites the account rather than the model's priors.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| google-ads-ad-copy | Pass | Pass | Pass |
| google-ads-quality-score | Pass | Pass | Pass |
| google-ads-search-term-mining | Pass | Pass | Warn |
| google-ads-bidding | Pass | Pass | Pass |
| google-ads-account-audit | Pass | Pass | Pass |
| google-ads-audiences | Pass | Pass | Pass |
| google-ads-anomaly-detection | Pass | Pass | Pass |
| google-ads-budget-management | Pass | Pass | Pass |
| google-ads-segmentation | Pass | Pass | Pass |
| google-ads-ad-extension-audit | Pass | Pass | Pass |
| google-ads-conversion-tracking | Pass | Pass | Pass |
| google-ads-keywords | Pass | Pass | Pass |
| google-ads-negative-keywords | Pass | Pass | Pass |
| google-ads-audit-leadgen | Pass | Pass | Pass |
| google-ads-audit-ecommerce | Pass | Pass | Pass |
| google-ads-attribution | Pass | Pass | Pass |
| google-ads-ad-extensions | Pass | Pass | Pass |
| google-ads-utm-generator | Pass | Pass | Pass |
| google-ads-scripts | Pass | Pass | Pass |
| google-ads-keyword-cannibalization | Pass | Pass | Pass |

Nineteen listings are a clean Pass on all three scanners. The single exception is a Snyk Warning on `google-ads-search-term-mining`, which is also the skill that reads a report and derives negative keyword candidates, so read its Snyk page and its instruction text before using it on a live account.

The real exposure is not in the markdown. It is the connector you attach. A Google Ads MCP server sees campaign structure, spend, conversion data and, depending on the scopes you grant, the ability to change bids and budgets. Grant read access first, keep the connector credential in the agent's secret store rather than a prompt, and decide explicitly whether the agent may mutate the account. None of the three scanners evaluates that decision, and the skills are written to recommend changes, not to enforce your approval boundary.

There is one more practical control: these playbooks are persuasive. An agent that has read the bidding skill will confidently recommend a strategy switch, and the skill has no view of your margin, contract terms or seasonality. Treat every recommendation as a hypothesis with a date and a metric attached, and change one thing at a time.

## Limitations

- Snapshot data, verified 2026-11-09: 4,900 combined installs across 20 indexed listings; 14 GitHub stars; MIT license; last pushed 2026-07-27. Counts drift over time.
- The skills.sh source page renders at most 20 listings while the repository holds 21 skills. `google-ads-experiments` is in the tree but not in the rendered page, so neither its installs nor its row appear above.
- No data connector is bundled. The skills are playbooks that describe what to analyse; they read live data only through a Windsor, Supermetrics or official Google Ads MCP server that you configure separately.
- The last push was 2026-07-27, roughly three and a half months before this snapshot. Google Ads surfaces change often, so verify field names, bidding options and interface paths against the current product before running a procedure.
- Fourteen stars is a thin adoption signal for a 21-skill suite. The install counts are real, but there is little community review behind the playbooks and no test suite or eval set in the repository.
- The account audits produce prioritised recommendations, not executed changes. Nothing in the repository validates that a recommendation is permitted by your account, contract or approval process.

## Related

- [Claude Ads - Paid Media Skill Suite Setup](/hermes/skills/catalog/claude-ads-setup)
- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the full set, not one skill. The value is in the chain from search term mining to negatives to cannibalisation checks, and a single playbook leaves the agent with a plausible first step and no second one.
- Connect the data source before the skills. Otherwise the agent will audit from memory, and the output will read well and be wrong.
- Ask for the top five fixes by financial impact rather than a full audit. The account audit skill already ranks that way, and the shorter output is the one a human will act on.
- Use `google-ads-anomaly-detection` before changing bids. Most CPA spikes are budget, tracking or competition, and the skill checks those before it recommends a bidding change.
- Check the character counts on generated RSA copy yourself. The skill writes to the limits, but the limits and the asset requirements change, and a rejected asset wastes the ad group's learning period.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
