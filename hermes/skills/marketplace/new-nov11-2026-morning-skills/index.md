---
title: "New Skills - November 11, 2026 Morning"
description: "Skills.sh sweep (Nov 11 morning): 7 publisher guides for 48,013 combined installs across 288 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov11-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 11, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills across 0 failed queries: 83 NEW rows and 249 PARTIAL, with the top NEW row at 339 installs and nothing above the 1,000-install trigger. That is the forty-seventh consecutive silent window.

The previous fire left a probe debt rather than a queue, so this one paid it. Fifty-seven domain queries ran at the 2.7-second pacing the API requires, returning 3,803 rows across 1,745 distinct sources with zero failed queries. Those queries deliberately covered territory the last two queues never touched: hardware and robotics, logistics and fleet, legal and compliance operations, healthcare administration, education back office, local services, and procurement and accounting. Cross-referencing the 1,745 sources against the docs tree left 1,520 uncovered, but only 2 of them above 3,000 combined installs, which says the domain space is mostly mapped and the remaining finds sit in the 700 to 2,500 band.

Twenty-four candidates were sized from their own source pages rather than from the probe rows, and the difference mattered again: `gasserane/personal-skills` read 1,432 in the probe and sizes to 22,098 across 52 listings, while `snailsploit/claude-red` read 1,471 and sizes to 10,049. Fourteen of the twenty-four changed by more than 50 percent once sized, and four changed by a factor of six or more. Five were held with a measured reason each, one is an excluded class and one is the standing dangling-publisher re-check. The seven published guides all came from the sized set.

Every guide was built from a pre-verified pack holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree, and the live security verdicts from skills.sh. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit. All 21 gate runs are green.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 83 rows |
| PARTIAL (source known, skill not cataloged) | 249 |
| Above-floor finds in the standing window | 0 (top row 339) |
| Fresh topic probe | 57 queries, 3,803 rows, 1,745 sources, 0 failed |
| Uncovered sources from the probe | 1,520 |
| Uncovered above 3,000 combined | 2 |
| Candidates sized from source | 24 |
| Held, excluded or dangling | 7 |
| Guides published this fire | 7 |
| Combined installs documented | 48,013 |
| Indexed listings covered | 288 |
| Tier mix | 1 Green, 6 Yellow |

## New Setup Guides

- [Anthropic Healthcare Skills - Clinical Workflow Suite Setup](/hermes/skills/catalog/anthropic-healthcare-skills-setup) - anthropics/healthcare, 2,256 combined, 10 listings, 443 stars, no LICENSE file, Healthcare operations: clinical data extraction, coding, claims review, FHIR integration and contract questions, with seven connected MCP servers
- [MATLAB Agentic Toolkit - Engineering Agent Skills Setup](/hermes/skills/catalog/matlab-agentic-toolkit-setup) - matlab/matlab-agentic-toolkit, 6,814 combined, 96 listings, 1,290 stars, NOASSERTION, Engineering and scientific computing: 158 skills that drive the MATLAB MCP server so an agent runs code instead of guessing toolbox signatures
- [KiCad Happy - Electronics Design Review Skills Setup](/hermes/skills/catalog/kicad-happy-setup) - aklofas/kicad-happy, 8,216 combined, 12 listings, 1,644 stars, MIT, Hardware design: schematic and layout parsing, power tree computation, ESD audits, EMC pre-checks, SPICE and distributor sourcing
- [GRC Skills - Governance, Risk and Compliance Suite](/hermes/skills/catalog/grc-skills-setup) - sushegaad/claude-skills-governance-risk-and-compliance, 9,363 combined, 36 listings, 1,060 stars, MIT, Compliance: one skill per framework across ISO 27001, SOC 2, FedRAMP, GDPR, HIPAA, EU AI Act, NIST 800-53 and 28 more
- [Claude Patent Creator - USPTO Patent Drafting Setup](/hermes/skills/catalog/claude-patent-creator-setup) - robthepcguy/claude-patent-creator, 2,710 combined, 17 listings, 211 stars, MIT, Intellectual property: hybrid RAG over MPEP, 35 USC and 37 CFR, prior-art search across patents and papers, 112(a) and 112(b) checks
- [Apple Skills - iOS and macOS Development Suite Setup](/hermes/skills/catalog/apple-skills-setup) - rshankras/claude-code-apple-skills, 13,116 combined, 96 listings, 882 stars, MIT, Apple platform: 165 skills across 23 categories covering iOS, macOS, watchOS, visionOS, App Store optimization and release review
- [Agent Stuff - Agent Skill Toolkit for Builders](/hermes/skills/catalog/agent-stuff-setup) - mitsuhiko/agent-stuff, 5,538 combined, 21 listings, 3,212 stars, Apache-2.0, Builder utilities: OpenSCAD modelling, Chrome DevTools browser control, headless Ghidra, tmux session control and gh workflows

## Held, with the reason measured

- **snailsploit/claude-red** (10,049 across 51 listings, 10,588 stars): offensive security and red-team suite. Standing exclusion class since the Nov 6 evening fire.
- **gasserane/personal-skills** (22,098 across 52 listings, 3 stars): no LICENSE file and no public signal. The second-largest figure in the probe and the least verifiable.
- **whawkinsiv/solo-founder-skills** (2,899 across 71 listings, 262 stars): seventy-one indexed listings against 21 `SKILL.md` files, so a guide would document entries with no directory behind them. Index shape, not size.
- **qfeius/make-platform-skills** (4,662 across 18 listings): AGPL-3.0 and 0 stars. Licence class plus no public signal.
- **diodeinc/pcb** (8,554 across 12 listings, 501 stars): twelve indexed listings against five `SKILL.md` files, a 2.4 drift ratio, on a repository whose tree is 2,621 files of mostly application code. First in line if a PCB guide is wanted and the drift is explained.
- **freightcognition/linehaulai-claude-marketplace** (1,034 across 46 listings, 4 stars): no public signal and a 46 against 35 drift.
- **404kidwiz/claude-supercode-skills**: re-probed as the standing dangling-publisher check. GitHub still returns 404 for the repository and the account while skills.sh serves 96 listings, unchanged since the Nov 10 evening fire.

## New pitfalls found this fire

- **The probe-versus-source gap is not a rounding error, it is a different number.** Six of twenty-four candidates changed by more than 50 percent once sized from their own source page, and one changed by a factor of 15 (`gasserane/personal-skills`, 1,432 in the row, 22,098 from the source). Any candidate sized from a probe row is unsized.
- **Domain probes return domain-agnostic publishers.** Hardware, logistics, legal and healthcare queries all returned 96 rows at the cap, but the cross-ref showed the same platform-wide publishers (`sickn33`, `pproenca`, `garrytan/gbrain`) surfacing under every vertical term. The vertical space is thin at the publisher level, which is why only 2 uncovered sources cleared 3,000.
- **A repository description and its own README can disagree on the same fact.** The patent creator's description cites 76M+ patents while its BigQuery skill row says 100M+. Both are carried in the guide rather than one being picked.
- **Index drift appears in official publishers too.** The MATLAB toolkit indexes `matlab-debugging` while the tree carries `matlab-debug-code`, and nine further listings have no same-named directory. An official publisher is not a guarantee that the index matches the tree.

## Integration and deploy

Seven guides into `hermes/skills/catalog/`, a `### New - November 11, 2026 Morning Sweep (7 publisher guides)` block appended to `catalog/index.md`, this batch page, a Recent Sweeps entry at the top of `marketplace/index.md`, stamps 1,559+ to 1,566+, PROGRESS setup guides 1,024 to 1,031 and total Markdown 3,757 to 3,764.
