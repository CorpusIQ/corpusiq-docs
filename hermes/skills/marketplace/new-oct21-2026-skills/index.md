---
title: "New Skills - October 21, 2026"
description: "Skills.sh sweep (Oct 21): 887 skills checked, 106 new. One guide added - Dontbesilent dbskill, a 35-skill Chinese business toolkit at 725.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct21-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 21, 2026 (Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The 20-query window (15 Hermes-focused plus the 5-query generic pass) served 887 unique skills in both passes with 0 failed queries: 106 NEW, 271 PARTIAL.

The fire produced one above-floor find, and it is the largest single publisher added to this catalog in months: [dontbesilent2025/dbskill](https://www.skills.sh/dontbesilent2025/dbskill) at 725,537 combined installs across 44 indexed listings, with a flagship skill alone at 29,768. It is a 35-skill Chinese business-diagnosis and content toolkit built from a 4,176-atom knowledge base, fronted by a router skill that decides which skills to run and in what order. The sweep itself read it as two rows (dbs-bridge 8,982 and dbs-install-skill 7,748); the publisher follow-up sized it 81x larger than that first reading, which is why the follow-up is mandatory before any guide decision.

One above-floor find was rejected on security grounds. [cyxzdev/uncodixfy](https://www.skills.sh/cyxzdev/uncodixfy/uncodixfy) carries 5,589 installs and 2.7K GitHub stars, and Snyk rates it CRITICAL under E004: prompt injection detected in the skill instructions, with an explicit directive telling the agent to hide content from its own reasoning. It gets no guide and no install recommendation here; the verdict is published so a reader who finds the repo elsewhere knows what to check.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 887 (pass 1 and pass 2, identical; 0 failed) |
| NEW (not in catalog) | 106 across 78 sources |
| PARTIAL (source known, skill not cataloged) | 271 |
| New publisher guides | 1 (725,537 combined installs) |
| Above-floor finds rejected | 1 (Snyk CRITICAL prompt injection) |
| Zero-catalog audit | 48 sources at 100+; 0 uncovered in catalog/; 0 converts |
| Marketplace count | 1,136+ to 1,137+ |

## New Publisher Guides

### 1. Dontbesilent dbskill - 35-Skill Business Toolkit (725.5K)

**Source:** [dontbesilent2025/dbskill](https://www.skills.sh/dontbesilent2025/dbskill) (725,537 combined across 44 indexed listings; 10,831 stars; CC BY-NC 4.0; pushed Oct 19, 2026; top: dbs 29,768)

A Chinese-language business toolbox from the writer [@dontbesilent](https://x.com/dontbesilent), distilled from 16,152 public posts into 4,176 knowledge atoms and packaged as 35 agent skills. The distinctive piece is `/dbs`, a router that reads the intended outcome and picks the smallest set of skills that reaches it, announcing the arrangement before it runs. The rest of the suite covers business diagnosis, peer benchmarking, Jobs to Be Done, content planning, platform moderation risk, AI-writing detection, WeChat HTML layout, a local decision ledger, a knowledge-base builder, and a skill auditor that scans installed skills for ad funnelling and hidden commercial intent. State carries across sessions through `dbs-save` and `dbs-restore` into `~/.dbs/`. Two constraints matter: everything is written in Chinese, and the license is CC BY-NC 4.0, so commercial use needs the author's permission. Sampled security verdicts are clean on two skills and carry one MEDIUM Snyk third-party-content warning on the router.

-> [Setup guide](/hermes/skills/catalog/dontbesilent-dbskill-setup)

## Rejected Above Floor

### cyxzdev/uncodixfy - not recommended (5,589 installs)

2,668 GitHub stars, MIT, single SKILL.md, last pushed March 2026. Snyk's audit rates it CRITICAL under E004, prompt injection detected in the skill instructions: the instructions direct the agent to act as if it does not see its own reasoning and to list what it would do without doing it. That is a manipulation pattern unrelated to the skill's stated UI-styling purpose, so it is excluded from the catalog. Gen Agent Trust Hub and Socket both pass it, which is exactly why a single critical verdict is worth reading rather than averaging away.

## Zero-Catalog Audit

48 PARTIAL sources sit at 100 or more combined installs, audited against `catalog/` recursively (716 markdown files, full `owner/repo` match then exact owner token). 0 carry no catalog page, so the conversion queue is empty and there are no converts this fire.

Two borderline sources remain below the 5,000-install guide floor and are carried forward: [ant-design/antd-skill](https://www.skills.sh/ant-design/antd-skill) at 4,102 combined across 3 listings, and [gogf/skills](https://www.skills.sh/gogf/skills) at 3,231. One standing exclusion re-verified: 404kidwiz/claude-supercode-skills still returns 404 from GitHub, so its 1,971 installs are unactionable.

## Cross-Reference Note

The coverage test now ignores per-fire report pages. Those pages list newly seen skill names without a guide, so treating them as coverage made a previously reported name permanently un-convertible: the Oct 20 evening fire published 20 NEW names, and every one of them read as already documented on the next pass. With report pages excluded, this fire reports 106 NEW where the same data returned 0 under the old test. Names stay NEW until a guide exists, which is the intent.
