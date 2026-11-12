---
title: "New Skills - November 12, 2026 Morning"
description: "Skills.sh sweep (Nov 12 morning): 6 publisher guides for 40,413 combined installs across 391 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov12-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 12, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills across 0 failed queries: 82 NEW rows and 249 PARTIAL, with the top NEW row at 342 installs. That is the forty-ninth consecutive silent window, and the standing board again produced nothing above the 1,000-install floor.

The Nov 11 evening note asked the next fire to keep a generic business-process lane in the probe, because vertical terms mostly rediscover publishers the catalog already covers. This fire ran 78 generic queries at the 2.7-second pacing the API requires, and the result matched that reasoning: 6,055 rows across 2,054 distinct sources with zero failed queries.

Cross-referencing those 2,054 sources against the docs tree left 1,408 uncovered, of which 6 sit above 3,000 combined installs, 10 above 2,000, 34 above 1,000 and 55 above 700. The distribution is flatter than the Nov 11 evening probe, which found 548 uncovered sources but 11 above 3,000: the generic lanes keep reaching new publishers, and the mass sits lower each time.

Twenty-three candidates were sized from their own source pages rather than from probe rows. Nineteen of them appeared in the probe, and fourteen changed by more than 50 percent once sized. The largest distortions were the ones that decided the fire: `okou-ai/okou-skills` read 1,743 in its probe row and sizes to 16,320, `glebis/claude-skills` read 1,978 and sizes to 14,683, `pawbytes/skill-suites` read 2,474 and sizes to 10,105, and `seb1n/awesome-ai-agent-skills` read 1,885 and sizes to 13,036. A probe row remains a sample of one listing's traffic, never the family size.

Selection used the same rule as the last fire, restated for a lower band: sized at 3,000 combined or above, plus a quality signal (an official or vendor publisher, a release inside the last quarter, a multi-skill family), minus anything held on a measured property. Six sources cleared it. Two large ones did not, on evidence rather than on size, and their reasons are recorded below.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 82 rows |
| PARTIAL (source known, skill not cataloged) | 249 |
| Above-floor finds in the standing window | 0 (top row 342) |
| Fresh topic probe | 78 queries, 6,055 rows, 2,054 sources, 0 failed |
| Uncovered sources from the probe | 1,408 |
| Uncovered above 3,000 combined | 6 |
| Candidates sized from source | 23 |
| Changed by more than 50 percent once sized | 14 |
| Held, excluded or duplicate | 6 |
| Guides published this fire | 6 |
| Combined installs documented | 40,413 |
| Indexed listings covered | 391 |
| Tier mix | 1 Green, 5 Yellow |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|--:|--:|---|
| Glebis Claude Skills | glebis/claude-skills | 14,683 | 96 | Yellow |
| Pawbytes Skill Suites | pawbytes/skill-suites | 10,105 | 76 | Yellow |
| Asgard Skills | asgard-ai-platform/skills | 4,981 | 96 | Yellow |
| Privacy and Data Protection Skills | mukul975/privacy-data-protection-skills | 4,267 | 96 | Yellow |
| Looker Skills | looker-open-source/looker-skills | 3,277 | 26 | Green |
| Dataverse Skills | microsoft/dataverse-skills | 3,100 | 11 | Yellow |

Per-guide thresholds were set from each distribution rather than fixed: 250 for glebis, 175 for pawbytes, 100 for looker and 300 for dataverse, with 60 for asgard and 47 for mukul975 where the whole install band sits low. All 18 gate runs were green on the first pass: the format gate, the pack cross-check at each guide's own threshold and the frontmatter audit, zero fix cycles.

Three of the six are first-party or vendor code: Looker's open source organization, Microsoft, and an Apache-2.0 privacy database. The other three are individual authors with real install volume and active pushes, and each guide states what the scanners found rather than smoothing it.

## Held, with the reason measured

- **okou-ai/okou-skills** (16,320 across 96 listings, 81 stars, no LICENSE file): the largest uncovered source in the sweep and the one that took the most time to reject. The repository carries 94 `SKILL.md` files, but only 2 of the top 19 indexed listings have a matching directory. The rest are connector skills (`google-sheets`, `strava`, `line`, `apify`, `lark`, `firecrawl`, `gmail`, `slack-webhook`) whose bodies live in `okou-ai/okou-connectors`, and that repository returns 404. An index-only guide would have guessed a Use For cell for 17 rows.
- **lawve-ai/awesome-legal-skills** (4,422 across 96 listings, 947 stars): 281 `SKILL.md` files, but 17 of the top 21 indexed names match neither a directory nor an entry in the 97KB README catalog. The index renames skills on the way in, and no naming map was published. Held until the mapping can be derived or the publisher documents it.
- **gasserane/personal-skills** (22,149 across 52 listings, 3 stars): no LICENSE file and no public signal. Standing hold, fourth fire.
- **workos/skills** (4,824 across 45 listings) and **streamlit/agent-skills** (3,618 across 19 listings against 1 `SKILL.md`): both are index shape rather than content, the same disposition as earlier fires for workos.
- **sylphxai/skills** (4,841 across 95 listings against 14 `SKILL.md`) and **seb1n/awesome-ai-agent-skills** (13,036 across 96 listings): sized, not yet drafted. The first has a 7x index-to-tree ratio; the second is large enough to be worth a tree check before any draft. Both are queued for the next fire rather than rejected.
- **sales-skills/sales** (3,636 in the probe): `skills.sh` serves 99 listings under this source while `/api/search` filtered to the exact source returns zero rows and GitHub returns 404 for the repository. A dangling publisher, recorded so the next fire does not re-size it.
- **boristane/agent-skills** (4,964 across 1 listing): one skill. A note rather than a guide.

## New pitfalls found this fire

- **A source can be visible in the probe and invisible to the sizing pass.** `sales-skills/sales` returned rows during the probe and zero rows from the exact-source filter minutes later. Size a candidate twice, or treat a zero as a dangling publisher rather than as a small family.
- **The marker assert in the one-pass cross-ref must fall back to a standalone probe.** The probe's own name list does not contain `hermes-agent`, so the sanity check that catches a broken `rg` construction fails for every probe pass that does not include the standing queries. Fall back to a single-pattern `rg` before concluding the construction is broken.
- **A repository can index skills it does not ship.** okou's connector skills are listed under `okou-ai/okou-skills` and live in a second repository that is not public. Check the tree ratio and the top-row mapping, not just the SKILL.md count: 94 files against 96 listings looked clean and was not.
- **Rename-on-index is a distinct drift from rename-in-tree.** Lawve's tree and its own README agree with each other, and the skills.sh names match neither. A guide built from the index names would have invented descriptions for 17 rows.
- **Capping at 96 is common at the top of the band.** Three of the six published sources returned exactly 96 rows, the API ceiling. For those, both the listing count and the combined install total are floors, and each guide says so.

## Next fire

The queue below is sized from source, or scheduled for a tree check first:

- `seb1n/awesome-ai-agent-skills` (13,036 across 96 listings) needs a tree check before drafting; 103 `SKILL.md` files against 96 listings suggests a real family rather than an aggregator, but it has not been verified.
- `iart-ai/freelance-motion-skills` (4,690 across 5 listings, 7 stars) and `jwangkun/claude-for-financial-services-cn` (4,554 across 59, 890 stars) are both above the floor with clean shapes.
- `minhnv0807/ai-business-skills` (4,225 across 96 listings, 661 stars) and `zlanqing/codex-claude-academic-skills` (3,257 across 24, 5,911 stars) are the next multi-skill families in the band.
- `sylphxai/skills` (4,841 against 14 `SKILL.md`) is a drift review: confirm the 95 listings resolve before sizing a guide.
- `wispbit-ai/skills` (3,579 across 5), `vikiboss/60s-skills` (3,742 across 7), `geoffjay/claude-plugins` (3,514 across 25) and `dexhunter/seedance2-skill` (3,559 across 2) are still clean and still unpublished.
- Keep the generic business-process lane in the probe. It carried this fire, as it carried the last one.

Every guide was built from a pre-verified manifest holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree, and the live security verdicts from skills.sh. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
