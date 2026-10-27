---
title: "New Skills - October 26, 2026 Evening"
description: "Skills.sh sweep (Oct 26 evening): a widened 25-query topic probe found 24 qualifying publishers, 8 guides shipped here for 1.02M combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/marketplace/new-oct26-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 26, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 91 NEW, 269 PARTIAL. It was the sixteenth consecutive fire with nothing new above the 1,000-install trigger, and its top row was `zzci/skills` at 364. The trending board served 506 entries across 53 sources and every one of the 53 was already in the catalog.

The productive lane stays the topic probe, widened this fire from eleven lanes to twenty-five: the eleven that converted in the previous sweep plus fourteen new ones covering logistics, supply chain, HR, legal, healthcare, construction, real estate, education, finance operations, accounting, procurement, customer support and ecommerce. That probe collected 2,142 unique skills with 0 failed queries and left 415 sources with no catalog coverage.

Sizing is what turned it into guides. Every source whose best window row reached 1,000 installs was queried by its publisher, and **24 of them cleared the 5,000-install combined floor**. Eight are documented below; the other sixteen are sized and queued for the next fire.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 885 (0 failed queries) |
| NEW (not in catalog) | 91 |
| PARTIAL (source known, skill not cataloged) | 269 |
| Topic probe (25 queries) | 2,142 unique, 0 failed, 415 uncovered sources |
| Sources sized by publisher | 33 with a window row at 1,000+ |
| Above-floor finds | 24 (16 queued for the next fire) |
| New publisher guides | 8 (364 indexed listings, 1,015,632 combined installs) |
| Above-floor finds rejected | 0 |
| Board | Trending 506 entries / 53 sources; all 53 covered |
| Marketplace count | 1,174+ to 1,182+ |

## New Publisher Guides

### 1. Yaklang Hack Skills (373,468 combined)

**Source:** [yaklang/hack-skills](https://www.skills.sh/yaklang/hack-skills), 104 indexed listings, top skill `hackskill-playbook` class rows in the 3.6K to 4.3K band; 2,551 stars; MIT; pushed 2026-09-13.

The largest source in this sweep: 103 offensive-security playbooks, one per class of finding, from injection and deserialization to Active Directory, mobile SSL pinning, kernel and browser exploitation, plus engagement-level skills for recon, attack-surface mapping and bug bounty. Each is a `SKILL.md` under `skills/<name>/`, so an agent can load one technique at a time instead of a generic pentest prompt.

Beta tier. Gen Agent Trust Hub and Snyk pass on all three sampled listings, Socket warns on all three, and the content is offensive-security material that only belongs in an authorized engagement.

### 2. Dev Event Organizer Skills (340,513 combined)

**Source:** [samber/dev-event-organizer-skills](https://www.skills.sh/samber/dev-event-organizer-skills), 65 indexed listings in a 5,154 to 5,410 band; 4 stars; MIT; pushed 2026-10-26.

Seventy-five skills for conferences, meetups, hackathons and the community programs around them: portfolio strategy, market fit, first edition, budget, venue and vendor sourcing, CFP design, speaker sourcing, sponsor prospectus and fulfillment, run of show, accessibility, code of conduct, no-show management, feedback and content repurposing. Every skill is tool-agnostic and the repo ships a per-skill `evals/` folder plus Claude, Codex and Cursor manifests.

Beta tier. All three auditors pass on the three sampled skills and the repo carries real evals, but 4 GitHub stars against 340.5K installs and a 256-install spread across 65 listings reads as bundle adoption rather than 65 individually used skills.

### 3. Aaron Marketing Skills (130,549 combined)

**Source:** [aaron-he-zhu/aaron-marketing-skills](https://www.skills.sh/aaron-he-zhu/aaron-marketing-skills), 134 indexed listings, top skill `keyword-research` at 1,925; 3,000 stars; Apache-2.0; pushed 2026-10-27.

A marketing department laid out as discipline, phase and skill: SEO and GEO, content, social, email, paid ads, influencer, launch and analytics, 120 skills in total with typed auditors, per-skill evals, eight commands and a documented install path for more than seventy hosts. It is versioned like software (20.1.0) and the tree is organised so a router can pick one phase rather than loading the whole suite.

Beta tier. Snyk warns on all three sampled skills, Gen Agent Trust Hub also warns on `keyword-research`, and the install index carries 134 listings against 120 skill directories.

### 4. Markdown Viewer Skills (50,975 combined)

**Source:** [markdown-viewer/skills](https://www.skills.sh/markdown-viewer/skills), 21 indexed listings, top skill `canvas` at 3,866; 3,378 stars; CC-BY-4.0 for the skill package with the `documd` CLI and rendering engines under GPL-3.0-only; pushed 2026-10-06.

Diagrams, architecture, charts, cards and wireframes written as text in Markdown and rendered live: mermaid, drawio, floor plans, engineering drawings and the `documd-visuals` package that replaced the older per-skill layout in September. The practical value is that an agent produces a visual answer as text, which diffs, reviews and version-controls like code.

Beta tier. All three auditors pass on the three sampled skills; the guide is held below Production because 21 installs-indexed names map to one in-tree package and most of the install volume predates the consolidation.

### 5. Reddit Research Skills (46,849 combined)

**Source:** [lignertys/reddit-research-skills](https://www.skills.sh/lignertys/reddit-research-skills), 4 indexed listings from `reddapi` 13,535 down to `reddit-search-api` 10,659; 15 stars; MIT; pushed 2026-09-15.

Semantic search over 50K+ subreddits, 20M+ posts and 40M+ comments through reddapi.dev, with playbooks for competitor research, niche validation and trend tracking, plus `reddit-leads` which finds buying-intent posts, scores them 0 to 100 and classifies them by lead type. No Reddit OAuth or app registration is needed.

Beta tier. It is a third-party paid service with plan-based rate limits and no API access on Free plans, and Snyk warns on all three sampled listings.

### 6. Indexion Skills (44,603 combined)

**Source:** [trkbt10/indexion-skills](https://www.skills.sh/trkbt10/indexion-skills), 19 indexed listings, nine of them clustered at 4,915 to 5,100; 2 stars; Apache-2.0; pushed 2026-09-22.

Source-code exploration behind the `indexion` CLI: agent orientation on an unfamiliar repo, search, segmentation, knowledge-graph facts, spec-driven development, refactoring and README and wiki generation. Ten skills in the tree, with a plugin manifest at 0.19.0.

Community tier. The install counts are high but the repo has 2 stars, nine indexed listings have no directory in the current tree, and the required binary arrives through a curl-to-shell installer.

### 7. Superagent Security Skills (17,532 combined)

**Source:** [superagent-ai/skills](https://www.skills.sh/superagent-ai/skills), 16 indexed listings, top skills `skill-security` 8,008 and `ci-cd-security` 7,956; 79 stars; MIT; pushed 2026-08-15.

Security work encoded as rules and offline scanners rather than a service: skill and supply-chain scanning, GitHub Actions review, repository security posture, IDOR and authz review, secrets handling, infrastructure security, disclosure triage and vulnerability triage, plus an instruction-only offensive engagement orchestrator and a bounded red-team loop that writes guardrail training data.

Beta tier. Gen Agent Trust Hub and Socket pass on all three sampled skills, Snyk fails `ci-cd-security` and warns on the other two, and the offensive-skills entry has neither a README entry nor a directory in the tree.

### 8. Darwin Skill (11,143 combined)

**Source:** [alchaincyf/darwin-skill](https://www.skills.sh/alchaincyf/darwin-skill), 1 indexed listing; 6,628 stars; MIT; pushed 2026-09-18.

A single skill that improves other skills: evaluate a `SKILL.md` on a nine-dimension rubric, make one conservative edit at a time, test it, and keep or revert the change through a git ratchet, with a paired same-judge comparison deciding each keep or revert. It is the closest thing in the ecosystem to a skill-quality loop an agent can run on its own library.

Beta tier. Two of three scanners warn because the skill edits files and drives git, the operational instructions are Chinese-first, and the rubric's own evidence puts judge accuracy well below human review.

## Queued For The Next Fire

Sixteen further sources cleared the floor and are sized, not yet documented: Cap Go 45,261; Mblode 32,174; Anthropic Financial Services 31,116; Senclaw 31,105; Ship Shit Dev 27,426; Iart AI Motion Design 26,459; Astronomer 25,523; Sumsub 24,593; Enzed R3F 22,525; LangChain Deepagents 21,754; Qodex AI Agent Skills 21,316; Pydantic Skills 21,182; Qdrant Skills 14,361; Customware AI 14,308; Benjamin Sehl Liquid 9,343; Laguagu 8,664. The remaining 382 uncovered sources from the probe have not been sized yet, which is deliberate: the row-versus-publisher gap that surfaced this batch has ranged from 2.7x to 652x.

## Method Notes

- Standing window and topic probe both ran against the live skills.sh API at 30 requests per minute; 0 queries failed across 45 queries.
- Coverage is tested against every markdown file under `hermes/skills/`, with per-fire report pages excluded, so a name reported last fire is not mistaken for a documented one.
- Every guide is cross-checked against its pack by three gates: format, pack-integer reconciliation, and a non-ASCII audit. All 8 passed all three on the first attempt after the pack parser was widened to accept comma-grouped integers.
