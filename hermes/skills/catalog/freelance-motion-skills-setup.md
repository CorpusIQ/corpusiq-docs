---
title: "Freelance Motion Skills - Brief, Price, Deliver Setup"
description: "iart-ai/freelance-motion-skills: 4.8K combined installs across 5 listings, the business side of motion design: briefs, quotes, revisions, delivery specs"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/freelance-motion-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "motion design", "freelance", "pricing"]
---

# Freelance Motion Skills - Setup Guide

**Source:** [iart-ai/freelance-motion-skills](https://www.skills.sh/iart-ai/freelance-motion-skills) via skills.sh - 4.8K combined installs across 5 indexed listings; first seen Nov 2, 2026
**GitHub:** 7 stars, MIT license, `main` branch, last pushed 2026-11-11, 5 `SKILL.md` files under `skills/`, 36 files in total
**Category:** Freelance operations for motion designers and small studios
**Quality Tier:** 🟡 Established - five focused skills with a near-identical install band, a clean MIT license and a fresh push, held back by a young repository, a small star count and one Snyk Warn on the revisions skill.

Every other motion skill in this catalog is about making the animation. This one is about the paperwork around it, which is where freelance motion work actually leaks money. Five skills, one per stage: scope the ask into a brief, price it defensibly, cap revisions, export correctly, and document the brand's motion language.

The install band is the tell. All five listings sit between 950 and 966 installs, a spread of 16 across the set. That is the signature of a pack installed as a unit rather than five skills found separately, and it means the numbers describe the pack rather than any one skill's merit.

The skills read as written by someone who has argued about revision rounds. `client-revisions` handles the three parts of the problem: capping the rounds in the contract, writing the SOW language, and converting out-of-scope feedback into a change order instead of an argument. `motion-pricing` runs day-rate math, names the cost drivers (style complexity, revisions, usage rights, turnaround) and outputs a line-itemed quote.

Two of the five are delivery-side and useful even if you never quote a project: `video-delivery-specs` carries per-platform spec sheets, a cutdown matrix from one master to the short social versions, caption and accessibility notes, and a pre-delivery QC checklist. `brand-motion-guidelines` builds the token set (easing, duration, logo rules) that keeps a brand's animation consistent across vendors.

## Installation

The README documents the Skills CLI and the Claude Code plugin marketplace:

```bash
npx skills add iart-ai/freelance-motion-skills
```

```text
/plugin marketplace add iart-ai/freelance-motion-skills
/plugin install freelance-motion-skills
```

The pack is one of 19 in the publisher's open collection. Installing this repo gets only these five skills; the sibling packs install separately, which keeps the instruction surface small.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| video-delivery-specs | 966 | Per-platform export specs, a cutdown matrix, caption and accessibility notes, and a pre-delivery QC list. |
| brand-motion-guidelines | 961 | A brand motion system: easing and duration tokens, a motion library, logo rules and accessibility standards. |
| motion-pricing | 958 | Pricing model choice, day-rate math, cost drivers and a line-itemed quote. |
| creative-brief | 957 | Turning a vague client ask into a structured brief plus the clarifying questions to send back. |
| client-revisions | 950 | Revision caps, SOW language, vague feedback translated into requests, and out-of-scope work as a change order. |

No indexed listings fall below the threshold; all 5 appear above it.

## Why This Matters for Hermes Agents

The failure mode in creative freelance work is not bad animation. It is work that was never scoped, priced against an unclear brief, extended through free revisions and delivered in a format the client rejects. Each of those is a small negotiation, and small negotiations are where an operator sounds least confident.

That makes them a good fit for an agent, because the agent is not embarrassed to send the clarifying questions, not tempted to accept an eighth revision, and not flattering when the client says "make it pop". The brief skill asks the six or seven questions a senior designer would ask and hands them back as a single message rather than a drip of follow-ups.

The pricing skill is the one with a hard number in it. Day-rate math plus named cost drivers plus usage rights produces a quote an operator can defend line by line, which is a different posture from a number that felt right.

The delivery specs skill generalises past freelance work. Any team that ships one master video to several platforms needs the same cutdown matrix and QC list, whether or not anyone is invoicing for it.

## Usage

| You say | What happens |
|---|---|
| "The client said they want something cool for a product launch, turn that into a brief" | Runs `creative-brief` and returns a structured brief plus the questions to send back for sign-off. |
| "Quote a 30-second 2D explainer with two revision rounds and paid social usage" | Runs `motion-pricing` and returns a line-itemed quote with the drivers named. |
| "They keep asking for small tweaks and we are past the agreed rounds" | Runs `client-revisions` and drafts the change-order message. |
| "What are the export specs for Reels, TikTok and broadcast?" | Runs `video-delivery-specs` and returns the per-platform sheet. |
| "We need one master cut into vertical and square versions" | Runs `video-delivery-specs` and returns the cutdown matrix with safe areas. |
| "Write the motion guidelines for this brand" | Runs `brand-motion-guidelines` and returns named easing and duration tokens plus logo animation rules. |
| "Run the pre-delivery check on these files" | Runs `video-delivery-specs` through the QC list and reports what fails. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/iart-ai/freelance-motion-skills/main/skills/creative-brief/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/iart-ai/freelance-motion-skills/main/skills/motion-pricing/SKILL.md
```

After installation, confirm five folders with one `SKILL.md` each. The pack has no scripts and no dependencies, so a missing file is a copy problem rather than an install problem.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| video-delivery-specs | Pass | Pass | Pass |
| brand-motion-guidelines | Pass | Pass | Pass |
| motion-pricing | Pass | Pass | Pass |
| creative-brief | Pass | Pass | Pass |
| client-revisions | Pass | Pass | Warn |

Five instruction files with no executables. The Snyk Warn on `client-revisions` sits on text that writes contract language, which is the closest thing here to a risk: what the skill drafts is not legal advice, and SOW wording should be reviewed by whoever signs it.

## Limitations

- Snapshot data, verified 2026-11-12: 4,792 combined installs across 5 indexed listings; 7 GitHub stars; MIT license; last pushed 2026-11-11. Counts drift over time.
- Five skills is the whole pack. There is no client management, no contract template beyond the SOW language in `client-revisions`, and no invoicing or tax coverage.
- The pricing math is day-rate based. Studios that price on value or on deliverable complexity will use the structure but replace the arithmetic.
- The star count is tiny next to the install count, so the pack is being installed through the skills CLI far more than it is being discussed or reviewed in public.
- The README links to a commercial product (iart.ai) alongside the open skills. The five skills here are the free part.
- Delivery specs for platforms age quickly. Two of the named formats change their encoding recommendations most years, so re-check the sheet against the platform's current guidance before a delivery.

## Related

- [IART Web Animation Skills - GSAP and SVG Suite](/hermes/skills/catalog/iart-web-animation-skills-setup)
- [Explainer Video Skills - Script to Render Setup](/hermes/skills/catalog/explainer-video-skills-setup)
- [Motion Graphics Skills - B-roll and Explainer Video](/hermes/skills/catalog/barty-motion-graphics-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `creative-brief` on the client's own words, pasted verbatim. The skill's job is to surface what is missing, and it can only do that against what was actually said.
- Send the brief and the quote together. A price without the brief it is based on invites a negotiation about the number instead of the scope.
- Put the revision cap in the first email. `client-revisions` writes the language, and the cheapest change order is the one the client already agreed to.
- Use the cutdown matrix before animating. Designing for the vertical crop after the fact is the most common cause of a second round of work on a finished piece.
- Keep `brand-motion-guidelines` output as versioned files. Easing tokens that live in a chat history are not tokens.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
