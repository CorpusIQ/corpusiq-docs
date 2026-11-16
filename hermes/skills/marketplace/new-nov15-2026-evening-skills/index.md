---
title: "New Skills - November 15, 2026 Evening"
description: "Skills.sh sweep (Nov 15 evening): 9 publisher guides for 79,728 combined installs across 143 indexed listings, from engineering loops to YouTube and design"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov15-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 15, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. This is the evening fire that follows the November 14 double header, and it also closes a publishing gap: the sixteen guides from that November 14 evening batch had been committed to a branch and never opened as a pull request, so they reached the site in this fire rather than the last one. A commit is not a publication, and nothing in the pipeline was watching for the difference.

The standing 20-query window came back to life in a way it had not in weeks. It returned 883 listings, 80 NEW and 250 PARTIAL rows, and its top NEW row sat at 4,724 installs rather than the 300 to 350 band that the previous fires had to clear. That single row, `oil-oil/oil-ui`, became one of the nine guides below.

The topic probe ran 174 lanes at 2.7-second pacing through `curl`, returning 13,115 rows across 3,829 distinct sources with zero failed queries. Cross-referencing against the docs tree left 3,200 uncovered sources, of which 7 sat above 3,000 installs. The probe band was thin, so the fire sized 78 candidates by their own source filter instead of by their probe rows, and that step is what carried the batch: three of the nine publishers below read more than twice their probe figure once exact-source rows were summed.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 883 listings / 831 names / 289 sources |
| NEW (standing window) | 80 rows |
| PARTIAL (standing window) | 250 rows |
| Top NEW row in the standing window | 4,724 (`oil-oil/oil-ui` / `oil-ui`) |
| Topic lanes completed | 174 |
| Probe rows / distinct sources | 13,115 / 3,829 |
| Failed queries | 0 |
| Uncovered sources after cross-reference | 3,200 |
| Uncovered above 3,000 combined | 7 |
| Candidates sized by exact source | 78 |
| Guides published this fire | 9 |
| Combined installs documented | 79,728 |
| Indexed listings covered | 143 |
| Tier mix | 1 Green, 8 Yellow |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|---|--:|--:|---|
| Pwguler Skills - Triple Debt Engineering Suite | pwguler/skills | 15,161 | 47 | Yellow |
| Pandoscope Skills - Agentic Engineering Library | pandoscope/skills | 14,554 | 14 | Yellow |
| YouTube Agent Skills - Eleven Channel Skills | jakeschincariol/youtube-agent-skill | 12,226 | 11 | Yellow |
| Learn AI Basics - Devpost Learner Curriculum | challengepost/learn-ai-basics | 11,061 | 9 | Green |
| GitLab CLI Skills - glab Command Reference | vince-winkintel/gitlab-cli-skills | 7,673 | 53 | Yellow |
| Reelary Skills - Local Footage Search for Agents | reelary/skills | 6,787 | 6 | Yellow |
| Oil UI - Interface Design Skill for Agents | oil-oil/oil-ui | 4,724 | 1 | Yellow |
| Vibe Security - Security Audit for Vibe-Coded | raroque/vibe-security-skill | 3,869 | 1 | Yellow |
| Solid Skills - SOLID and TDD Coding Standards | ramziddin/solid-skills | 3,673 | 1 | Yellow |

The eight Yellow tiers are not a decline in quality so much as a decline in luck: seven of the nine carry a Snyk or Socket warn on at least one sampled skill, and two repositories ship no licence file at all. The one Green page covers the smallest repository in the batch by stars and the cleanest one by audit, which is the pattern this catalog keeps finding.

## Carried forward, not published

- **el4cteo/roblox-skills** (25,089 across 23 listings, 119 stars, MIT): the largest single find of the fire, but this family already has a page for `sentinelcore/roblox-skills`, and the two repositories publish the same skill names. Held until the identity question is settled rather than publishing a second page for one project.
- **szkocot/andrej-karpathy-skills** (3,950 across 1 listing, 3 stars, no licence): the same skill is documented from `multica-ai/andrej-karpathy-skills`, so this is a mirror until proven otherwise.
- **ctsstc/get-shit-done-skills** (3,769 across 69 listings, 8 stars, no licence): listing names carry colons and near-duplicates of each other, so the row set cannot be grounded or counted honestly yet.
- **dexhunter/seedance2-skill** (3,588 across 2 listings, 4,496 stars, MIT): the top listing fails the Gen Agent Trust Hub outright. Held for a re-probe before any page is written.
- **challengepost** and **vince-winkintel** neighbours, plus 69 further candidates sized in this fire, remain queued with their exact figures recorded.

## New pitfalls found this fire

- **The standing window can go quiet for weeks and then produce the batch on its own.** Fifty-two consecutive fires read a top NEW row between 300 and 350 before one fire broke 3,300 and this one broke 4,700. A window that looks structurally dead is still worth running, because the alternative reading hides a real publisher.
- **Probe rows undercount large publishers by 2x to 16x, and the error is not uniform.** `challengepost/learn-ai-basics` read 1,842 in the probe against 11,061 by exact source, `vince-winkintel/gitlab-cli-skills` read 1,939 against 7,673, and `pwguler/skills` read 1,034 against 15,161. Ranking candidates by probe figure would have ordered this batch backwards.
- **A committed batch is not a published batch.** The November 14 evening guides were written, gated and committed to a branch with no pull request opened and no check registered, so they sat unreachable while the site's own freshness checks stayed green. Recovering them cost a rebase over three moving branches, and the lesson is to verify the merge, not the commit.
- **skills.sh listing names can contain colons.** A name like `gsd:verify-work` breaks the table parser in the drafting gates and collapses a 69-listing publisher into a single readable row, so any publisher whose names carry a colon needs its rows counted by script before a page is attempted.

## Live verification

Deploy ran after the push to main. Each new guide page returns 200 with its own title on `docs.corpusiq.io` and through the `www.corpusiq.io/docs` proxy, the batch page returns 200 on both hosts, the catalog index renders the new sweep heading with all nine links, the marketplace index carries the updated stamp and links this page, and the new URLs appear in `sitemap.xml`.

## Integration

Nine guides into `hermes/skills/catalog/`, one `### New - November 15, 2026 Evening Sweep (9 publisher guides)` block prepended to the sweep sections in `catalog/index.md`, this batch page, a Recent Sweeps entry at the top of `marketplace/index.md`, and PROGRESS counts resynced from the staged tree.

## Next-fire note

Start from the 78 exact-source sizes in this fire's cache rather than re-probing: the top unpublished entries are `el4cteo/roblox-skills` (25,089 / 23, pending identity), `pwguler` neighbours, `pandoscope` derivations and 69 sized candidates. Settle the roblox identity question first, because it is worth more than the rest of the queue combined, and re-probe `dexhunter/seedance2-skill` for its trust verdict.
