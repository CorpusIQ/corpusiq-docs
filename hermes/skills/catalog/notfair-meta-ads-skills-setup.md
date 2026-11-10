---
title: "NotFair Plugin - Meta Ads Audit and Automation Skills"
description: "nowork-studio/notfair-plugin on skills.sh: 4.4K combined installs; Meta and Google Ads audit, SEO and GEO skills for marketing agents"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/notfair-meta-ads-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "meta ads", "paid social", "seo", "marketing"]
---

# NotFair Plugin - Setup Guide

**Source:** [nowork-studio/notfair-plugin](https://www.skills.sh/nowork-studio/notfair-plugin) via skills.sh - 4.4K combined installs across 20 indexed listings; sampled 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 4,133 stars, MIT licensed, `main` branch, last pushed 2026-11-10, 45 `SKILL.md` files in 222 blobs, one directory per skill under `skills/<name>/` plus category folders for the shared workflow notes
**Category:** Paid social: Meta Ads auditing, campaign structure, creative testing and ad account diagnostics
**Quality Tier:** 🟡 Solid with caveats - MIT licensed with 4,000+ stars, but ten Warn verdicts across nine sampled skills.

NotFair is an open-source marketing skill suite with a serious following: 4,133 stars for a plugin that ships 45 skills across SEO, GEO, paid media, analytics, WordPress and CRM. The README describes the design goal well. Each skill is a focused procedure with defined inputs, decision rules and an output format, and live-data work goes through one OAuth-connected NotFair MCP server rather than a pile of platform-specific connectors. That single-server design is the reason the plugin can cover Meta, Google, X, LinkedIn, Reddit and TikTok ads without hardcoding tool names: skills use placeholders such as `~~meta-ads` and the agent resolves them against whatever the live session exposes.

This guide's slug points at Meta Ads, and the repository does carry a coherent paid social story: `meta-ads` for account management, `meta-ads-audit` for the health check and business context, and a `meta-ads-creative` skill in the tree for creative fatigue and briefs. But the rendered listing page is broader than the slug suggests. Of the 20 indexed listings, two are Meta skills, four are Google Ads skills, and the rest are SEO, content, GEO and site health procedures. Read the table as the top of the whole marketing suite rather than as a Meta-only set.

Two counts need care. The README says the plugin ships 45 skills and the tree agrees with 45 `SKILL.md` files, while the publisher page claims 53 and skills.sh renders 20. Those are three different numbers, and only the first two describe the current release.

## Installation

The skills CLI route takes one skill at a time:

```bash
npx skills add https://github.com/nowork-studio/notfair-plugin --skill meta-ads-audit
```

Claude Code users install the plugin from its marketplace, which brings the skills and the MCP connection together:

```text
/plugin marketplace add nowork-studio/notfair-plugin
/plugin install notfair@nowork-studio
```

Skills are then reachable as namespaced commands, for example `/notfair:seo-analysis`, `/notfair:google-ads-audit` or `/notfair:meta-ads-creative`, and plain language works as well.

Gemini CLI installs the repository as an extension and authenticates the MCP server when prompted:

```bash
gemini extensions install https://github.com/nowork-studio/notfair-plugin
```

Codex takes the plugin and opens the OAuth flow in one sequence:

```bash
codex plugin marketplace add nowork-studio/notfair-plugin --json && codex plugin add notfair@nowork-studio --json && codex mcp login NotFair
```

If the marketplace is already configured, the README's refresh form is `codex plugin marketplace upgrade nowork-studio --json` followed by the same add and login calls. Cursor users can clone into the local plugin directory while the public listing is pending:

```bash
git clone https://github.com/nowork-studio/notfair-plugin.git ~/.cursor/plugins/local/notfair
```

For any host that reads instructions rather than plugins, the repository ships `INSTALL_FOR_AGENTS.md`, and the README suggests pointing the agent at its raw URL so it can follow the setup itself.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear in the table:

| Skill | Installs | Use For |
|---|---|---|
| seo-analysis | 284 | Site-wide SEO audit from Search Console data and page inspection: traffic drops, indexing, metadata, schema, content gaps and Core Web Vitals |
| meta-ads-audit | 261 | Meta (Facebook and Instagram) account health audit and business context setup |
| meta-tags-optimizer | 261 | Title tags, meta descriptions, Open Graph and Twitter cards with A/B variants and a SERP preview |
| keyword-research | 260 | Seed-driven keyword discovery, clustering and prioritisation for SEO and GEO content |
| schema-markup-generator | 256 | JSON-LD for FAQ, HowTo, Article, Product and LocalBusiness rich results, validated against Google requirements |
| content-writer | 249 | SEO blog posts and landing pages written to E-E-A-T and Helpful Content guidance |
| seo-page | 241 | Single-page audit covering intent, content quality, E-E-A-T, metadata, schema, links and technical SEO |
| setup-cms | 238 | No directory in the current tree; the README release note says local CMS setup was removed from the shared release |
| geo-optimizer | 236 | Generative Engine Optimization: auditing and rewriting content for citation in ChatGPT, Claude, Perplexity, Gemini and AI Overviews |
| gemini | 234 | No directory in the current tree; the README release note says the Gemini CLI review skill was removed |
| google-ads-audit | 230 | Google Ads account health audit and business context setup |
| broken-link-checker | 229 | Broken link and redirect checks from a supplied crawl report or page inspection, with coverage limits stated |
| google-ads-landing | 227 | Landing page scoring and diagnosis, including the Landing Page Experience component of Quality Score |
| google-ads-copy | 225 | RSA copy generation and A/B testing of headlines and descriptions |
| google-ads | 223 | Google Ads management: performance, keywords, bids, budgets, negatives, campaigns and search terms |
| meta-ads | 221 | Meta Ads management: ROAS, CPM, frequency, audience overlap, learning phase and creative fatigue |
| content-planner | 176 | Dated editorial calendar from Search Console data, prioritising striking-distance queries and content gaps |
| upgrade | 151 | No directory in the current tree; the README release note says shell update and reminder helpers were removed |
| sitemap-audit | 89 | XML sitemap validation, crawl budget waste, indexable pages missing from the sitemap and lastmod accuracy |
| ecommerce-seo | 87 | Store SEO audit across category and product pages, faceted navigation, canonicals, pagination and product schema |

No indexed listings fall below the threshold; all 20 appear above.

Three listings in this table have no counterpart in the current tree. `setup-cms`, `gemini` and `upgrade` carry install counts but no `skills/<name>/` directory, and the README's release note explains why: local CMS setup, the Gemini CLI review skill, and shell update or reminder helpers were removed from the shared release. They are historical listings, and the honest description of each is the removal notice rather than a guessed capability.

## Why This Matters for Hermes Agents

Meta Ads work is mostly diagnosis, and diagnosis is where agents improvise. A model asked why ROAS fell will offer a list of generic causes: creative fatigue, audience saturation, learning phase, auction pressure. All are plausible, none is checked. The NotFair skills are built the other way round. `meta-ads-audit` sets up business context and runs an account health pass, and `meta-ads` covers the specific metrics that move: ROAS, CPM, frequency, audience overlap, learning phase, creative fatigue, budgets and ad set structure. That gives the agent a measurement frame before it offers a cause.

The audit skill is also the one that asks for context first. Meta performance is meaningless without a conversion definition and a target, and a skill that requires business context before auditing prevents the most common failure, which is a confident report against the wrong objective.

The broader suite matters because marketing questions rarely stay inside one platform. A drop in Meta ROAS often traces to a landing page, a tracking change or an organic traffic shift, and the same plugin carries page audits, sitemap checks, conversion-adjacent Google Ads workflows and GEO optimisation. Having those in one install means the agent can follow the evidence instead of declaring the platform guilty.

The caveat is quality signal. Ten of the twenty sampled skills carry at least one Warn, and three listings are historical entries with no code behind them. The star count reflects the repository's SEO and GEO reputation as much as its paid ads material, so judge the Meta skills on their own files rather than on the repository's popularity.

## Usage

| You say | What happens |
|---|---|
| "Audit my Meta ads account" | `meta-ads-audit` collects business context, then reviews account structure, audiences, creative and delivery before producing a prioritised health report |
| "Why did ROAS drop last week?" | `meta-ads` compares ROAS, CPM, frequency and audience overlap across periods, and checks learning phase and creative fatigue before naming a cause |
| "Which Meta campaigns are wasting spend?" | The audit workflow ranks ad sets by spend against result, and separates structural waste from creative wear |
| "Write a creative brief from last month's data" | `meta-ads-creative`, present in the tree though not in the rendered top 20, turns performance evidence into a brief rather than a generic prompt |
| "Why is organic traffic down at the same time?" | `seo-analysis` pulls Search Console evidence and checks indexing, metadata and Core Web Vitals, so platform and organic causes can be compared |
| "Is this landing page hurting my Quality Score?" | `google-ads-landing` scores the page and compares its message against the ad group's promise |
| "Give me next month's content calendar" | `content-planner` builds a dated plan from striking-distance queries and content gaps in Search Console data |

## Verification

The raw skill file sits at `skills/meta-ads-audit/SKILL.md`, and this URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/nowork-studio/notfair-plugin/main/skills/meta-ads-audit/SKILL.md | head -6
```

The frontmatter should declare `name: meta-ads-audit` and a description beginning "Meta Ads (Facebook + Instagram) account audit and business context setup", with trigger phrases listed below it. The `meta-ads` skill follows the same pattern at `skills/meta-ads/SKILL.md`.

After install, confirm the skill landed as a directory containing `SKILL.md`:

```bash
test -f ~/.claude/skills/meta-ads-audit/SKILL.md && echo ok
```

If your agent reads the Hermes profile directory, use the same relative path under `~/.hermes/profiles/corpusiq/skills/`. For a Cursor local plugin install, the skills stay inside the clone at `~/.cursor/plugins/local/notfair/skills/meta-ads-audit/SKILL.md`.

The MCP connection is separate from the skills and needs its own check. The plugin registers one server named NotFair and opens a browser OAuth flow; after authenticating, ask a question that requires account data, for example "how many Meta campaigns are active in this account", and confirm the answer comes from the connected workspace rather than from general knowledge.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| seo-analysis | Pass | Warn | Warn |
| meta-ads-audit | Pass | Pass | Pass |
| meta-tags-optimizer | Pass | Pass | Pass |
| keyword-research | Pass | Pass | Pass |
| schema-markup-generator | Pass | Pass | Pass |
| content-writer | Pass | Pass | Warn |
| seo-page | Pass | Pass | Warn |
| setup-cms | Pass | Warn | Pass |
| geo-optimizer | Pass | Pass | Pass |
| gemini | Warn | Pass | Pass |
| google-ads-audit | Pass | Pass | Pass |
| broken-link-checker | Pass | Pass | Warn |
| google-ads-landing | Pass | Pass | Warn |
| google-ads-copy | Pass | Pass | Pass |
| google-ads | Pass | Pass | Pass |
| meta-ads | Pass | Pass | Pass |
| content-planner | Pass | Pass | Pass |
| upgrade | Pass | Pass | Pass |
| sitemap-audit | Pass | Pass | Warn |
| ecommerce-seo | Pass | Pass | Warn |

Ten Warn cells spread across nine skills, which matches the tier note. The pattern is worth reading rather than counting: Snyk warnings cluster on skills that fetch and parse pages (`seo-analysis`, `seo-page`, `broken-link-checker`, `sitemap-audit`, `ecommerce-seo`, `google-ads-landing`) and on content generation (`content-writer`). Socket warns on `seo-analysis` and the removed `setup-cms`, and Gen Agent Trust Hub warns on the removed `gemini` listing. The two skills this guide is named for, `meta-ads-audit` and `meta-ads`, are clean Passes on all three scanners.

The current release is defensible on the supply-chain axis. The README states that the shared release on `main` contains declarative skills and one remote OAuth MCP connection, with no local helper programs, credential-file readers, automatic hooks, package installs or local servers. That is a strong claim, and it is checkable: the tree contains markdown and manifests rather than executables. Note that the same README says the scripted crawler and shell helpers were removed, which is consistent with the missing `setup-cms`, `gemini` and `upgrade` directories.

The exposure that remains is account access. One NotFair MCP server holds OAuth grants for Meta, Google Ads, Search Console, Analytics and the rest, so the blast radius of a bad instruction is every connected platform at once. Connect only the workspaces and platforms you intend to use, prefer read-only scopes where the skill only audits, and keep mutating operations behind an explicit confirmation. The README's own boundary is that changes must stay inside the user's authorization and be verified against the resulting account state, which is a policy the agent follows, not a technical control you can rely on.

## Limitations

- Snapshot data, verified 2026-11-09: 4,378 combined installs across 20 indexed listings; 4,133 GitHub stars; MIT license; last pushed 2026-11-10. Counts drift over time.
- The last push reads 2026-11-10T00:12:57Z, one day after this snapshot date, which is consistent with a UTC timestamp landing after a local-day cut-off rather than with a future commit.
- The skills.sh source page renders at most 20 listings. The tree holds 45 `SKILL.md` files and the publisher page claims 53, so the table covers less than half of the suite and the combined figure understates it.
- Three indexed listings, `setup-cms`, `gemini` and `upgrade`, have no directory in the current tree. The README's release note says local CMS setup, the Gemini CLI review skill and shell update or reminder helpers were removed, so those installs point at retired capabilities.
- Ten Warn cells across nine skills, concentrated on page-fetching and content-generation procedures. `meta-ads-audit` and `meta-ads` are clean, but the SEO side of the suite needs review before production use.
- The plugin depends on one hosted OAuth MCP server at `notfair.co`. Without that connection, live account work has no data source, and the skills state coverage limits rather than substituting estimates.
- The README notes that Amazon and ChatGPT Ads remain planning or export-review workflows unless the session exposes a verified connector, so cross-platform coverage is uneven despite the breadth of the platform table.

## Related

- [Claude Ads - Paid Media Skill Suite Setup](/hermes/skills/catalog/claude-ads-setup)
- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [Apify Growth Skills - Lead Gen, Brand Monitoring, Ultimate Scraper Setup](/hermes/skills/catalog/apify-growth-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `meta-ads-audit` before `meta-ads` on any new account. The audit collects business context and establishes the baseline; the management skill is far more useful once the objective and conversion definition are written down.
- Ask for the evidence behind each finding. These skills are built to state coverage limits, and a report that names the period, the metric and the comparison is the one worth acting on.
- Keep Meta and Google separate in one session. Both audits use business context, and mixing them produces recommendations that quietly assume the other platform's attribution.
- Check the tree before installing a listing with no directory. `setup-cms`, `gemini` and `upgrade` still carry install counts but were removed from the shared release, so the install buys a notice rather than a workflow.
- Connect read-only first. The single NotFair MCP server reaches every platform you authorise, so scope the OAuth grant to what the audit needs before you let an agent near budget or bid changes.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
