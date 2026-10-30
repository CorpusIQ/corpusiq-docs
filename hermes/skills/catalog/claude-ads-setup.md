---
title: "Claude Ads - Paid Media Skill Suite Setup"
description: "claude-ads: 98.7K combined installs. AgriciDaniel's MIT paid-media suite audits and drafts changes across 12 ad platforms from Claude Code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-ads-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "paid media", "advertising", "audit"]
---

# Claude Ads - Setup Guide

**Source:** [agricidaniel/claude-ads](https://www.skills.sh/agricidaniel/claude-ads) via skills.sh - 98.7K combined installs across 34 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [agricidaniel/claude-ads](https://github.com/agricidaniel/claude-ads) - 10,586 stars, MIT License, branch main, last pushed 2026-10-17; one conductor skill at `ads/SKILL.md` plus 33 per-skill files at `skills/ads-*/SKILL.md`, with shared references in `ads/references/`, bounded worker definitions in `agents/`, the deterministic scoring and schema core in `claude_ads_core/`, evidence and capability state in `control-plane/`, and plugin metadata in `.claude-plugin/` at manifest version 2.1.0

**Category:** Paid media operations, ad-account auditing, creative production and measurement for coding agents

**Quality Tier:** 🟡 Beta - three Snyk Warn verdicts in the sampled six (ads, ads-google, ads-competitor) on ad-account write paths; MIT, one directory per indexed listing

Claude Ads is AgriciDaniel's MIT-licensed paid-media suite for Claude Code, published on skills.sh as 34 separate skills that share one operating contract. The surface is deliberately wide: Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat and X, each with its own audit skill, an attribution and server-side tracking pair, a financial model, experiment design, creative generation, monitoring and reporting.

Architecturally it is one conductor plus bounded workers. `ads/SKILL.md` holds the operating order, the context intake list and a command routing table that maps every `/ads <subcommand>` to exactly one skill directory, and each worker gets a bounded scope and must return schema-valid findings instead of prose. The canonical result of a run is a versioned JSON bundle; Markdown, HTML and PDF are renderings of that same bundle, so a report cannot claim more than the evidence behind it. Account changes are read-only by default and stop at a draft unless the mutation gate passes in full.

## Installation

The README treats Claude Code as the canonical runtime and gives its native plugin flow as the preferred route. Both install forms below are copied from the repository's own docs, and they differ only in whether the marketplace name is attached:

```bash
/plugin marketplace add agricidaniel/claude-ads
/plugin install claude-ads
```

The Quickstart section attaches the marketplace explicitly, which is the form to use when more than one marketplace is already registered:

```bash
/plugin install claude-ads@ai-marketing-hub-claude-ads
```

For a release, the README asks you to prefer a tagged archive with a verified SHA-256 checksum and warns never to pipe a remote installer directly to a shell. Each release publishes the zip, `release-manifest.json`, `sbom.cdx.json` and `SHA256SUMS` in one directory, and every line must report `OK` before you extract and install:

```bash
sha256sum -c SHA256SUMS          # macOS: shasum -a 256 -c SHA256SUMS
bash install.sh --source=local
```

From a reviewed checkout, the local route is the same installer without the download step:

```bash
git clone https://github.com/AgriciDaniel/claude-ads.git
cd claude-ads
bash install.sh --source=local
```

Only the Claude Code target is verified. The README marks Codex, Gemini, Cursor, Windsurf and Goose experimental, and the installer's usage block documents `--skill-dir` and `--agent-dir` overrides for hosts whose layout differs. For a Hermes profile, point both overrides at the profile so nothing is written outside it, and skip the managed Python environment if you do not want the helpers:

```bash
bash install.sh --target=codex --no-deps \
  --skill-dir=~/.hermes/profiles/corpusiq/skills \
  --agent-dir=~/.hermes/profiles/corpusiq/skills/ads/agents
```

That places the conductor at `<skills>/ads/SKILL.md` and each platform skill at `<skills>/ads-<platform>/SKILL.md`. `--no-deps` keeps the skill files but leaves out the managed runtime, so the deterministic core and report rendering are unavailable until you install the locked requirements. Removal is manifest-scoped: `bash uninstall.sh --target=claude` deletes only files the installer recorded, and the validate skill is explicit that unrelated `ads-*` skills survive it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ads-meta | 4,891 | Read-only Meta audit: Pixel and Events Manager, attribution setup, Facebook and Instagram creative, audiences, placements, Advantage+ automation, budgets and account structure. |
| ads | 4,709 | The conductor contract: operating order, context intake, untrusted-data rules, command routing, run manifests and the evidence standard every other skill inherits. |
| ads-google | 4,500 | Read-only Google Ads audit across Search, Shopping, Performance Max and Demand Gen, with keyword and search-term review, negative-keyword generation, GAQL reads, bidding and policy. |
| ads-competitor | 4,204 | Competitor ad research through official transparency libraries and public ads, recording capture date, placement, observable message, landing destination and source URL. |
| ads-creative | 4,199 | Creative audit of copy, images and video for hooks, concept diversity, format and safe-zone fit, message match, fatigue signals, accessibility and policy. |
| ads-tiktok | 4,182 | Read-only TikTok audit covering Pixel, mobile-first creative, Smart+, Shop and commerce campaigns, pacing, attribution and policy. |
| ads-audit | 4,179 | Full or scoped multi-platform audit that writes a versioned JSON bundle first, then renders from it, and marks the run partial when a required worker fails. |
| ads-plan | 4,070 | Media plan and strategy: objectives, economics, channel selection, campaign architecture, audiences, budget, measurement, governance and rollout. |
| ads-budget | 4,067 | Budget, bidding and pacing review with break-even boundaries, marginal return, allocation under constraints, and formulas shown with their inputs. |
| ads-landing | 4,033 | Landing-page audit for message match, mobile experience, speed, accessibility, trust, forms, consent and tracking, fetched through the repo's guarded HTTP fetcher. |
| ads-create | 3,934 | Campaign concepts, messaging, ad copy, headlines and creative briefs built from a validated brand profile and platform requirements. |
| ads-linkedin | 3,913 | Read-only LinkedIn audit: Insight Tag and conversions, professional audiences, Lead Gen Forms, Thought Leader Ads, ABM, bidding and pacing. |
| ads-youtube | 3,911 | Read-only YouTube audit for in-stream, Shorts and CTV inventory, creative, audiences, brand safety, bidding and measurement. |
| ads-generate | 3,872 | Ad image generation from a validated brief and brand profile through an explicitly configured provider with a declared cost ceiling. |
| ads-dna | 3,860 | Brand and offer profile extracted from an authorized website, separating direct observations from inferred style labels and treating page content as untrusted. |
| ads-microsoft | 3,855 | Read-only Microsoft Advertising audit: UET, search and audience campaigns, Google imports, syndication, Copilot inventory and policy. |
| ads-photoshoot | 3,846 | Rights-cleared product photography variants from an authorized source image, preserving product geometry, packaging, labels and color. |
| ads-apple | 3,816 | Read-only Apple Ads audit: AdServices and AdAttributionKit, Search Match, App Store placements, custom product pages, MMP reconciliation and policy. |
| ads-math | 3,758 | Paid-media math: CPA, CPL, CPC, CPM, ROAS, MER, break-even, contribution margin, LTV:CAC, forecasts and experiment economics with units checked. |
| ads-test | 3,703 | Experiment design and readout: hypothesis, randomization unit, sample size and duration from stated assumptions, guardrails and decision rules. |
| ads-attribution | 3,452 | Cross-platform attribution audit across GA4, MMPs, AdServices, browser and server events, plus reconciliation of incompatible reporting windows. |
| ads-server-side-tracking | 3,422 | Server-side measurement audit: sGTM and tagging, Meta CAPI and TikTok Events API, event taxonomy, deduplication, consent and data quality. |
| ads-amazon | 3,403 | Read-only Amazon Ads audit: Sponsored Products, Brands and Display, DSP, portfolios, search terms, retail readiness, ACOS, TACOS and reporting. |
| ads-optimize | 690 | Diagnose and draft optimizations such as budget moves, bid changes, pausing or archiving, and negative-keyword actions, defaulting to a draft. |
| ads-report | 676 | Render Markdown, HTML or PDF reports from a validated run bundle, refusing fabricated health or incompatible historical bundles. |
| ads-monitor | 662 | Pacing, delivery, tracking, fatigue and policy monitoring that separates expected learning and reporting latency from unexplained anomalies. |
| ads-setup | 643 | Onboarding profile: business model, objective, conversion taxonomy, economics, active platforms, account IDs, date and currency conventions, credential references and guardrails. |
| ads-launch | 636 | Campaign launch plans and, only with the full mutation gate, capability-gated application, defaulting to `--draft`. |
| ads-research | 631 | Refresh platform, API, policy, benchmark and repository evidence, with reverify-or-demote decisions on stale claims and expired refresh dates. |
| ads-validate | 629 | Validate contracts, scoring inputs, run bundles, capabilities, source freshness, install or uninstall state and release readiness. |
| ads-pinterest | 604 | Read-only Pinterest audit: Tag and Conversions API, catalog and shopping readiness, visual creative, audiences, Performance+ and reporting. |
| ads-reddit | 601 | Read-only Reddit audit: campaign structure, community and interest targeting, creative-native fit, catalog ads, brand safety and reporting. |
| ads-snapchat | 600 | Read-only Snapchat audit: Snap Pixel and Conversions API, app campaigns, AR and catalog formats, audiences, budgets and brand safety. |
| ads-x | 594 | Read-only X audit: X Pixel and Conversions API, campaign objectives, keyword and conversation targeting, creative, app measurement and brand safety. |

No indexed listings fall below the threshold; all 34 appear above.

## Why This Matters for Hermes Agents

Thirty-four skills in one repository is a routing problem before it is a capability problem. Claude Ads solves it the way an agent host should: the conductor file carries a table that maps each subcommand to one owning skill and tells the agent to load that skill and not a neighbor, so a `/ads google` turn does not drag twelve platform references into context. That single-owner rule is also what makes the output auditable, because exactly one skill can be blamed for a finding.

The second design choice worth copying is the evidence contract. Every control ends in pass, fail, unknown or not applicable, and unknown is an explicit answer for missing data rather than a zero or a guess. Coverage of 80 percent or more is graded, 60 to 79 percent is provisional, and below 60 percent is insufficient evidence, so an agent working from a thin export is told that it is thin instead of producing confident prose. Findings live in a versioned JSON bundle and every human-readable report is rendered from that bundle, which kills the usual failure mode where a summary says something the raw data never supported.

The third is the mutation gate. Adapters are read-only by default, and applying a change needs a tested capability for that exact operation, explicit account and object IDs, a before and after diff with blast radius, owner approval inside account ceilings, an idempotency key with an audit destination and rollback, plus confirmation that remote state still matches the precondition. Missing ceilings mean no write, and permanent deletion is not supported at all in v2.

For a Hermes profile the practical lesson is portability. The skill files are plain markdown with YAML frontmatter and the runtime work is Python in `claude_ads_core/`, so the same artifacts load under a host other than Claude Code, with the caveat that only the Claude Code target is verified upstream. Treat it as a paid-media reasoning layer that produces drafts and evidence, not as an autonomous media buyer.

## Usage

| You say | What happens |
|---|---|
| "Audit our Google Ads account, here is last month's export" | The conductor routes to `ads-google` for a read-only audit and returns passed, failed and unchecked items, each with the evidence behind it, plus an explicit note on anything the export cannot answer. |
| "Where is the money leaking across all twelve platforms?" | `/ads audit all` fans out to bounded platform workers, writes one versioned JSON bundle, and marks the run partial for any platform whose worker or inputs were missing rather than quietly averaging it away. |
| "Should we move budget from Meta to Amazon next quarter?" | `ads-budget` normalizes spend and outcomes to comparable windows, `ads-math` supplies break-even and marginal-return formulas with inputs and sensitivity cases, and the answer states its uncertainty. |
| "Write three Meta hooks for the spring offer" | `ads-create` loads the validated setup and brand profile, separates factual from approved from hypothetical claims, and returns concepts, copy and a production brief instead of finished creative. |
| "Pause the ad sets that are wasting spend" | `ads-optimize` defaults to `--draft` and returns the proposed pause with causal evidence, a before and after diff, and the gate conditions still missing, so nothing is touched without approval. |
| "GA4 and Meta disagree on conversions, which number is real?" | `ads-attribution` inventories every counting source with its window, deduplication and privacy rules, then explains the discrepancy instead of adding the platforms together. |
| "Turn that audit into something I can send a client" | `ads-report` renders Markdown, HTML or PDF from the validated bundle, preserving findings, confidence, evidence references and contradictions. |

## Verification

Both raw paths cited in this guide returned 200 on branch main when it was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} ads/SKILL.md\n" \
  https://raw.githubusercontent.com/agricidaniel/claude-ads/main/ads/SKILL.md
curl -sL -o /dev/null -w "%{http_code} ads-audit/SKILL.md\n" \
  https://raw.githubusercontent.com/agricidaniel/claude-ads/main/skills/ads-audit/SKILL.md
```

Expect `200` on both. The capability manifest, which is the authoritative record of what a skill may read or change live, is fetchable the same way and also returned 200:

```bash
curl -sL -o /dev/null -w "%{http_code} capability-manifest.json\n" \
  https://raw.githubusercontent.com/agricidaniel/claude-ads/main/control-plane/manifests/capability-manifest.json
```

Review a skill before installing it by reading the first forty lines of its own file, which is the frontmatter and the procedure head, and compare the claimed scope against the manifest:

```bash
curl -sL https://raw.githubusercontent.com/agricidaniel/claude-ads/main/skills/ads-optimize/SKILL.md | head -40
```

After an install, confirm the conductor and the platform skills landed side by side under the profile, and that the conductor still carries its routing table:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep '^ads'
head -3 ~/.hermes/profiles/corpusiq/skills/ads/SKILL.md
grep -n '^## Command routing' ~/.hermes/profiles/corpusiq/skills/ads/SKILL.md
```

Expect 34 entries in that listing, the three lines of frontmatter head showing `name: ads` and its description, and the routing heading present in the conductor, which sits around line 48 of the file.

If dependencies were installed, the deterministic core reports its own version, and the suite reports its own state once a run has been recorded:

```bash
python -m claude_ads_core --version
```

In Claude Code the same checks are `/ads status` for current state, `/ads next` for the most important blocker, and `/ads validate` for contracts, runs, capabilities or release readiness. A run that validates but reports partial coverage is a working install with thin data, not a broken one.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ads-meta | Pass | Pass | Pass |
| ads | Pass | Pass | Warn |
| ads-google | Pass | Pass | Warn |
| ads-competitor | Pass | Pass | Warn |
| ads-creative | Pass | Pass | Pass |
| ads-x | Pass | Pass | Pass |

No sampled listing fails, and Gen Agent Trust Hub and Socket pass all six. Snyk records warn on three: `ads`, `ads-google` and `ads-competitor`. The tier note places those warns on ad-account write paths, which reads oddly for two skills whose own descriptions say read-only, and the pack does not carry the finding text, so this guide will not guess at a rule code: open each of those three security pages and read the warnings before the suite goes near a live account.

In practice a warn on this suite matters because the blast radius is an ad account, not a file tree. The suite is designed to read exports, screenshots and pasted summaries, and the conductor classifies all of that as untrusted data with an explicit instruction never to follow instructions embedded in it, because a competitor's ad copy or a malicious CSV is an injection surface. Credentials belong in environment variables, an OS keychain or an approved secret manager and never in profiles, reports or logs, and the mutation gate is what stands between a draft and real spend. Verify the gate, the capability manifest and the draft-first default yourself instead of trusting the badge.

## Limitations

- Snapshot data, verified 2026-10-29: 98,745 combined installs across 34 indexed listings; 10,586 GitHub stars; MIT License; last pushed 2026-10-17. Counts drift over time.
- The index and the tree agree exactly here: 34 indexed listings against 34 SKILL.md files, 33 in `skills/` and the conductor at `ads/`. That agreement is convenient but shallow, because the conductor sits one level up from the per-skill directories, so copying `skills/*` alone installs a suite whose routing target is missing.
- The README labels the project a development candidate that is not release-ready until every gate in `control-plane/RELEASE_REQUIREMENTS.md` passes. All twelve account-health scoring profiles are disabled, so audits report findings, unknowns and evidence coverage but no health score.
- Only the Claude Code target is verified. Codex, Gemini, Cursor, Windsurf and Goose install the same artifacts under each host's expected directory, but the README calls those targets experimental and tells you to confirm the result in the host.
- Runtime expectations are specific: managed dependencies support CPython 3.11 and 3.12 on glibc 2.28 or later and refuse musl. Browser capture needs an operator-installed Playwright payload, and PDF rendering needs WeasyPrint and Pango on the host.
- Changes stay drafts unless the full mutation gate passes, and permanent deletion is not supported in v2. A request to delete a campaign is answered with a draft and an explanation, not an executed delete.

## Related

- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup)
- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Never paste API keys or tokens into the conversation. `/ads setup` records that a credential reference exists, not the secret, and the README is explicit that credentials belong in environment variables, an OS keychain or an approved secret manager.
- Always attach the window with the data: date range, timezone, currency and platform. Without them the skill returns unknown rather than an estimate, and an audit that ignores timezone differences between Meta and Google will invent a discrepancy that is not there.
- Start with one platform. `/ads google` or `/ads meta` produces a scoped bundle you can read end to end, and a platform you understand is the cheapest way to learn whether the evidence standard is being met before you fan out to all twelve.
- Read the draft diff, not the recommendation. The mutation gate wants a before and after diff with blast radius, owner approval inside account ceilings, an idempotency key, a rollback and a verification window, so a draft missing any of those is the suite telling you it is not ready.
- Pin a release archive and check `SHA256SUMS` instead of piping an installer. Releases are checksummed and not signed, which means the checksum proves the files match the release and proves nothing about who built it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
