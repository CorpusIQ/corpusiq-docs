---
title: "Dev Event Organizer Skills - Conferences and Meetups Setup"
description: "Samber's 65 dev event skills: 340.5K combined installs for conference, meetup and hackathon planning, from budget and sponsors to run of show."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dev-event-organizer-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "events", "community operations"]
---

# Dev Event Organizer Skills - Setup Guide

Samuel Berthe publishes this suite as one operator's manual for technical event operations: conferences, meetups, hackathons and the community programs around them. It is 75 skills in the current tree, each a single `SKILL.md`, covering the whole arc from picking a date and pricing tickets through sponsor rate cards, call for papers review, run of show and the post-event debrief. Nothing is tied to one vendor's ticketing console: the skills teach the decision, not a product.

The suite is deliberately atomic and cross-referenced. `dev-event-kickoff` is a router that sends any event task to exactly one sibling skill or names the gap when none fits, and the SKILL.md files point at each other by name (the budget skill, for example, refuses to set prices and hands off to `event-ticket-pricing` and `event-sponsor-pricing`). The README's install section says to install the whole repo for that reason, and the install counts back it up: all 65 indexed listings sit in a narrow band between 5,154 and 5,410, which is the shape of whole-suite adoption rather than per-skill demand.

**Source:** [samber/dev-event-organizer-skills](https://www.skills.sh/samber/dev-event-organizer-skills) via skills.sh - 340.5K combined installs across 65 indexed listings; first seen Sep 13, 2026
**GitHub:** [samber/dev-event-organizer-skills](https://github.com/samber/dev-event-organizer-skills) (4 stars; MIT License; branch main, pushed 2026-10-26; layout `skills/<name>/SKILL.md` for 75 skill directories, plus `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/` and `gemini-extension.json` manifests and a per-skill `evals/` tree)
**Category:** Events / Conference and Community Operations
**Quality Tier:** 🟡 Beta - MIT, pushed the day of this snapshot, 65 of 75 tree directories indexed with no listing missing a directory, per-skill eval folders and four host manifests, and Pass from all three auditors on the three sampled skills, but the repo has only 4 GitHub stars against 340.5K installs and every listing sits within 256 installs of every other, so the counts read as bundle adoption rather than proven per-skill demand

## Installation

```bash
# Install the whole suite: the README explicitly warns against installing one skill
npx skills add samber/dev-event-organizer-skills
```

```bash
# Claude Code, from the README's own plugin path
/plugin marketplace add samber/dev-event-organizer-skills
/plugin install dev-event-organizer-skills@dev-event-organizer-skills

# Codex
codex plugin add github:samber/dev-event-organizer-skills

# Gemini CLI
gemini extensions install https://github.com/samber/dev-event-organizer-skills
```

Cursor users clone the repo into `~/.cursor/skills/dev-event-organizer-skills`, which the README names as an auto-discovered path. Claude.ai installs it as a plugin marketplace from the repository URL and then syncs. There is no CLI, API key or environment variable: the only executable file in the tree is one Python script inside `event-registration-forecast`, which forecasts registrations from a pace curve you supply.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| tech-podcast-youtube-channel | 5,410 | Decide whether an organizer's standing podcast or video channel should exist at all, then set guest sourcing, cadence and a wind-down |
| dev-event-hiring | 5,372 | Build the hiring side of an event role: scorecard, posting, interview loop, sourcing channels and a ramp plan |
| event-landing-page | 5,368 | Shape the event's public front door and the small site around it: page structure, the dominant call to action and per-section reveal timing |
| event-date-selection | 5,363 | Pick the date by checking audience calendars, observances and competing events before anything is announced |
| event-talk-selection | 5,362 | Run proposal review: committee shape, rubric, anonymization, conflict recusal, the cut rule and decline messages |
| event-budget | 5,359 | Build one edition's money model: fixed and per-head costs, break-even, and the sponsor and ticket targets it hands downstream |
| hackathon-brief-design | 5,356 | Write the challenge document teams read before building: problem statements, tracks, rules, eligibility and submission checklist |
| event-social-media | 5,351 | Run the event's own social presence: platform set, hashtag split, post calendar, amplification asks and staffed live coverage |
| event-format-selection | 5,351 | Choose the event's structure: shape, track count, session-format mix, delivery mode and hackathon demo and judging structure |
| event-ticket-pricing | 5,349 | Price attendee tickets: free-to-commercial posture, tier ladder, gating rules, scholarships, group discounts and refund policy |
| event-sponsor-pricing | 5,349 | Build the sponsorship rate card: revenue target first, then tiers, add-ons, exclusivity premiums, in-kind valuation and discount policy |
| event-debrief | 5,348 | Run the organizing team's retrospective: timeline, reconciliations against risk, budget and schedule, and owned action items |
| dev-event-career | 5,343 | Guide a practitioner into and up the event-organizing ladder: role fit, portfolio audit, interview prep and offer evaluation |
| dev-event-kickoff | 5,341 | Route any event-organizing task to exactly one skill in the collection, or name the gap when none fits |
| event-media-partnerships | 5,333 | Set up barter media and community partnerships: exchange formats, partner scoring, a no-cash agreement and a two-direction delivery ledger |
| corporate-event-strategy | 5,332 | Decide what a company-run event is funded to accomplish: goal mix, budget ownership and the measurement commitment written upfront |
| event-growth-strategy | 5,323 | Grow an established edition through one deliberate lever per edition, and treat capping or shrinking as a valid strategy |
| event-portfolio-strategy | 5,319 | Shape several event properties into one set where each feeds the others, with a written kill criterion per property |
| event-comms-channels | 5,319 | Design the attendee-facing channel architecture: which channels exist, who is on each, message routing and wind-down |
| workshop-program-design | 5,317 | Run the hands-on session itself: facilitator coverage, prerequisites, capacity ceilings, session length, materials and the room's network posture |

The remaining 45 indexed listings range from 5,154 to 5,298 installs.

## Why This Matters for Hermes Agents

Event organizing is a scheduling and sequencing problem disguised as a content problem, which is exactly where a general model gives confident but unordered advice. These skills impose an order: a budget skill that refuses to price tickets and hands off, a date skill that runs before anything is announced, a run-of-show skill that consumes the schedule rather than inventing it. An agent holding the suite has to answer "which decision is this, and what does it depend on" before it writes anything.

The router is the part that matters most in practice. `dev-event-kickoff` is a single entry point that either lands on one skill or says plainly that the collection does not cover the task, which is a rare and useful refusal for an agent that otherwise improvises. Because siblings name each other in their own descriptions, a handoff is written into the text rather than left to the model to infer.

It is also cheap to carry. Seventy-five Markdown files, no network calls, no credentials in scope and one optional Python script, so a global install costs context only when an event question is actually asked. For an agent that also holds production credentials, a skill family that cannot touch them is a safe default.

Finally, the repo ships evals. Each skill directory under `evals/` carries trigger queries and scenario summaries; `event-budget`, for example, reports 9 scenarios with a 90.7 percent pass rate with the skill against 33.1 percent without it, a delta of 57.6 percentage points. That is the author's own instrument, not an outside audit, but it is more than most prompt suites offer and it flags a real weakness: trigger accuracy on that skill was 78.9 percent, with several positive queries firing in one run out of two.

## Usage

| You say | What happens |
|---|---|
| "/dev-event-kickoff I'm running a 200-person developer conference in March and the call for papers still isn't open." | Routes to the call for papers and timeline skills, or names the gap, instead of drafting a generic plan |
| "We sold 340 tickets but only 210 showed up last year" | Loads `event-no-show-management` for the show-up expectation, an overbooking ceiling and a waitlist design |
| "Sponsors keep asking what the gold tier includes" | Loads `event-sponsor-prospectus` and `event-sponsor-pricing` to rebuild the tier table and rate card from a revenue target |
| "Should we run a hackathon track this year?" | Loads `event-format-selection`, then `hackathon-brief-design` and `hackathon-judging` if the answer is yes |
| "Give me the minute-by-minute for the two main days" | Loads `event-run-of-show` for the cue sheet, transitions, comms channels and on-duty rotation |
| "How much should we spend on the venue versus the food?" | Loads `event-budget` to split fixed and per-head costs and find break-even, handing prices back to the pricing skills |
| "What did we learn from this edition?" | Loads `event-debrief` for the retrospective, then `event-continuous-improvement` to turn it into one change |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -iE "dev-event-kickoff|event-budget|event-sponsor-pricing"
```

Read the skills before installing. All five URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/samber/dev-event-organizer-skills/main/README.md
curl -sL https://raw.githubusercontent.com/samber/dev-event-organizer-skills/main/skills/dev-event-kickoff/SKILL.md
curl -sL https://raw.githubusercontent.com/samber/dev-event-organizer-skills/main/skills/event-budget/SKILL.md
curl -sL https://raw.githubusercontent.com/samber/dev-event-organizer-skills/main/skills/tech-podcast-youtube-channel/SKILL.md
curl -sL https://raw.githubusercontent.com/samber/dev-event-organizer-skills/main/skills/hackathon-brief-design/SKILL.md
```

The directory listing behind the install index also returned 200 on the same date, and is the fastest way to see which skills exist today:

```bash
curl -s https://api.github.com/repos/samber/dev-event-organizer-skills/contents/skills | grep '"name"'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tech-podcast-youtube-channel | Pass | Pass | Pass |
| dev-event-hiring | Pass | Pass | Pass |
| event-landing-page | Pass | Pass | Pass |

The surface is close to zero and worth stating precisely. No `SKILL.md` in the tree declares an `allowed-tools` field, so no skill asks the host for shell, write or network permission of its own. There is exactly one executable file in the whole repository, `skills/event-registration-forecast/scripts/forecast-registrations.py`, a registration forecast helper; every other file is Markdown or the plugin and Gemini manifests. The skills do not read files, call an API or handle credentials. They instruct the model to walk a decision procedure and reply in prose.

The one caveat is scope rather than safety: several skills produce material that ends up in public or legal documents, including sponsor agreements, codes of conduct, press releases and code of conduct enforcement ladders. The `event-sponsor-agreement` skill explicitly frames its output as a term sheet for counsel. Have a lawyer review anything binding before it goes out.

## Limitations

- Only 4 GitHub stars against 340.5K installs. The listing counts do not correlate with stars, and all 65 sit between 5,154 and 5,410, so treat the number as evidence of whole-suite installs, not of 65 independently popular skills.
- The install index and the tree disagree by 10 directories. `event-accessibility-inclusion`, `event-attendee-experience`, `event-continuous-improvement`, `event-production`, `event-registration-forecast`, `event-speaker-coaching`, `event-speaker-experience`, `event-sponsor-renewal`, `event-sustainability-plan` and `hackathon-judging` exist in `skills/` but are not indexed on skills.sh, so they install with the suite but carry no install count.
- Advisory only. No skill reads a calendar, queries a venue, checks a competitor's dates or writes a file; every answer rests on what the operator supplies, which makes the quality of the input the ceiling on the output.
- Evals are the author's own and are not uniformly strong. The `event-budget` summary reports 90.7 percent with the skill against 33.1 percent without, but also 78.9 percent trigger accuracy, and several positive trigger queries fire at a 0.5 rate, so routing between siblings can miss.
- The suite is one publisher's method, aimed at technical and developer events. Community, cultural and academic events will need the community-flavoured skills padded with local practice.
- Snapshot data, verified Oct 26, 2026: 340,513 combined installs across 65 indexed listings; 4 GitHub stars; MIT License; last pushed 2026-10-26. Counts drift over time.

## Related

- [Samber DevRel Skills - Open Source Growth Suite Setup](/hermes/skills/catalog/samber-devrel-skills-setup) - the same publisher's developer-relations suite, listed as a related collection in the README and aimed at the audience the event sells to.
- [Samber Developer Platform Skills - API & DX Setup](/hermes/skills/catalog/samber-developer-platform-skills-setup) - the third collection in the same family, for the platform and developer-experience side of a conference programme.
- [Marketing Mindset - B2B Marketing OS for AI Agents Setup](/hermes/skills/catalog/marketing-mindset-setup) - deeper campaign machinery for the attendee-acquisition work that `event-marketing-plan` only sketches.
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - the planning layer behind the talk and content work that `event-content-repurposing` turns into derivatives.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole suite, as the README insists. The siblings cross-reference each other by name, and a single skill's handoff instructions point at skills you will not have.
- Start every event task with `dev-event-kickoff`. It is the only skill written to refuse, and a refusal tells you the collection does not cover the problem before you spend a session on it.
- Feed the budget skill real quotes. It consumes prices and refuses to derive them, so placeholder numbers produce a break-even figure that will not survive a vendor conversation.
- Run the eval queries in `evals/<skill>/trigger-evals.json` against your own router before relying on automatic routing; the shipped `event-budget` summary reports 78.9 percent trigger accuracy, which is good but not a guarantee.
- Treat anything legal that the suite drafts, from the sponsor term sheet to the code of conduct sanctions ladder, as a first draft for counsel, not as advice.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
