---
title: "New Skills - November 12, 2026 Evening"
description: "Skills.sh sweep (Nov 12 evening): 6 publisher guides for 34,003 combined installs across 287 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov12-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 12, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills across 0 failed queries: 82 NEW rows and 248 PARTIAL, with the top NEW row at 346 installs (`sjy051/music-composition`). That is the fiftieth consecutive silent window on the standing board.

The morning fire's next-fire note asked for the generic business-process lane to stay in the probe and for the ten pre-sized candidates to be drained. This fire did both: 87 generic business-process queries at the 2.7-second pacing the API requires, and five of the six published guides came off that queue.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 82 rows |
| PARTIAL (source known, skill not cataloged) | 248 |
| Above-floor finds in the standing window | 0 (top row 346) |
| Fresh topic probe | 87 queries, 5,892 rows, 2,226 sources, 0 failed |
| Uncovered sources from the probe | 1,962 |
| Uncovered above 3,000 combined | 2 |
| Uncovered above 2,000 combined | 5 |
| Uncovered above 1,500 combined | 10 |
| Uncovered above 1,000 combined | 21 |
| Queue candidates sized from source | 12 |
| Candidates taken to a full tree check | 7 |
| Guides published this fire | 6 |
| Combined installs documented | 34,003 |
| Indexed listings covered | 287 |
| Tier mix | 1 Green, 5 Yellow |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|--:|--:|---|
| Awesome AI Agent Skills | seb1n/awesome-ai-agent-skills | 13,145 | 96 | Green |
| Freelance Motion Skills | iart-ai/freelance-motion-skills | 4,792 | 5 | Yellow |
| Claude for Financial Services CN | jwangkun/claude-for-financial-services-cn | 4,610 | 59 | Yellow |
| AI Business Skills | minhnv0807/ai-business-skills | 4,442 | 96 | Yellow |
| 60s Skills | vikiboss/60s-skills | 3,742 | 7 | Yellow |
| Codex Claude Academic Skills | zlanqing/codex-claude-academic-skills | 3,272 | 24 | Yellow |

Per-guide thresholds were set from each distribution: 150 for seb1n where a long low band needed a top slice, 900 for the five-skill motion pack where every listing clears 950, 85 for jwangkun where the tail drops off after eleven rows, 78 for minhnv0807 where twenty rows cluster at the top, 70 for the seven-skill 60s pack and 500 for zlanqing where three skills carry the installs and 21 nested references sit at 21 to 24. All 18 gate runs were green on the first pass apart from one draft that carried a Chinese placeholder string into the body, which the frontmatter audit caught and the draft fixed before the push.

Three of the six are large multi-skill families with a real publisher behind them: 103 skills from seb1n, 147 marketing skills from minhnv0807, and 188 `SKILL.md` files from jwangkun. The other three are narrow: a five-skill freelance motion pack, a seven-skill wrapper over one free Chinese API, and a three-skill academic suite that carries the highest star count in the batch.

## Held, with the reason measured

- **qfeius/make-platform-skills** (4,732 across 18 listings, 0 stars, AGPL-3.0): re-sized this fire and still held. Every one of the 18 indexed names maps to a real directory and the repository was pushed on 2026-11-11, so the content is coherent; the hold is on the publisher signal, which is what the Nov 11 fire measured and this one did not overturn.
- **geoffjay/claude-plugins** (3,514 across 25 listings, 8 stars, MIT): clean shape, last pushed 2025-11-04. A repository a year without a push against a current install count is a queue item, not a rejection; it stays in the next-fire list.
- **wispbit-ai/skills** (3,587 across 5 listings, 9 stars, no LICENSE file): five skills from February 2026 with no licence. Standing queue, unpublished.
- **sylphxai/skills** (4,841 across 95 listings against 14 `SKILL.md`): the drift review the last two notes asked for. The probe row for one of its skills (`market-research-synthesis`, 66 installs) confirms the listings resolve, but 95 listings over 14 files is index shape rather than content, and the hold stands.
- **workos/skills** (3,603 across 1 listing) and **gasserane/personal-skills** (2,210 across 9 listings): both standing holds. A single listing is a note, and gasserane still ships no LICENSE and surfaced on Nov 12 morning at 22,149 combined, which is 10x what this probe's rows suggest.
- **sales-skills/sales** (1,557 in the probe): still serves rows in the probe and still returns 404 from GitHub. Dangling publisher, recorded again so the next fire does not re-size it.
- **Single-listing discoveries with four-figure installs**: `alibaba-flyai/flyai-skill` (3,454), `juliobsz/skills` (2,428), `muxuuu/serenity-skill` (2,407) and `nashsu/llm_wiki_skill` (1,870). One listing each. The rule that has held for six fires is that a single skill is a note rather than a guide, and 3,454 installs on one listing does not change the shape.

## New pitfalls found this fire

- **The probe row understates a family by an order of magnitude, again.** `seb1n/awesome-ai-agent-skills` appeared in this probe at 1,534 combined across 12 listings and sizes to 13,145 across 96. The ratio is 8.6x. Any selection rule that reads probe rows as sizes will pick the wrong six guides, and this is the fifth consecutive fire where the distortion moved the outcome.
- **A four-figure single listing is still one skill.** The temptation to publish `alibaba-flyai/flyai-skill` at 3,454 installs is real and the answer is no: there is no family to describe, no roster to reconcile and no second Use For cell to write.
- **Python `urllib` is wrong for this API and `curl` is right.** The standing window ran 20 queries in 72 seconds at 2.7-second pacing through `curl`; the same code path through `urllib` averaged around 60 seconds per query in the Nov 11 evening fire. Time the first three queries and switch client rather than rewriting the query list.
- **A placeholder username in a README reaches the guide.** `zlanqing/codex-claude-academic-skills` documents its install commands with a Chinese placeholder repo path, and the first draft quoted it verbatim. The frontmatter audit flags any non-ASCII outside the tier emoji and the footer arrows, which is what caught it before publication.

## Next fire

The queue below is sized from source, or scheduled for a shape check:

- `geoffjay/claude-plugins` (3,514 across 25 listings) needs a decision on age rather than shape: MIT, 102 files, 25 skills, one year since the last push.
- `wispbit-ai/skills` (3,587 across 5) and `dexhunter/seedance2-skill` (3,569 across 2) are both still unpublished; the first has no licence, the second is two skills.
- `qfeius/make-platform-skills` (4,732 across 18) is publishable on content and held on publisher signal. If the next fire wants it, the guide writes itself; if not, drop it from the queue rather than re-sizing it a third time.
- `sylphxai/skills` is a drift review, not a guide, until 95 listings resolve to more than 14 files.
- Keep at least one generic business-process lane in the probe. It carried this fire and the two before it, and the uncovered mass sits below 3,000 installs per source, which means volume now comes from more queries rather than from taller rows.

Every guide was built from a pre-verified manifest holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree, and the live security verdicts from skills.sh. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
