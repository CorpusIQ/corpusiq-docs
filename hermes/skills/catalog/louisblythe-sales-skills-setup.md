---
title: "Sales Skills - B2B Sales Playbook Suite Setup"
description: "louisblythe/sales-skills at 51.7K combined installs: 122 B2B sales skills for prospecting, discovery, objection handling, pricing and closing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/louisblythe-sales-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "b2b sales", "revenue operations"]
---

# Sales Skills - Setup Guide

**Source:** [louisblythe/sales-skills](https://www.skills.sh/louisblythe/sales-skills) via skills.sh - 51.7K combined installs across 122 indexed listings; first seen Mar 18, 2026
**GitHub:** [louisblythe/Sales-Skills](https://github.com/louisblythe/Sales-Skills) (188 stars; no LICENSE file, GitHub reports no license while the README says MIT; pushed 2026-01-24; layout `skills/<name>/SKILL.md` for all 122 skills, plus `.claude-plugin/marketplace.json` declaring plugin `sales-skills` v5.0.0 with 122 skill paths and README grouping them as Core Sales Skills 20, Sales Process and Strategy 22, AI SDR and Bot Skills 80)
**Category:** Sales / Revenue Enablement
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub, Socket and Snyk all Pass on the three sampled skills, and the suite is pure markdown with no scripts and no network calls; held below Production by the missing LICENSE file, an MIT claim that lives only in README prose, and a single publication with no push since 2026-01-24)

Sales Skills is a 122-skill library built by Apparate, an Australian sales consultancy, for Claude Code and other agent runtimes. It splits cleanly in three: 20 core selling skills for humans, 22 process and strategy skills for building the machine, and 80 skills written for people designing an AI SDR - intent detection, objection recognition, handoff detection, sentiment analysis, conversation memory, warm transfer.

The frameworks are named and standard rather than invented: BANT, MEDDIC, SPICED, SPIN, Challenger and Gap Selling all appear in the README as the methodologies the skills encode. That makes the output reviewable by anyone who has run a sales team, which is a rarer property than it sounds in this category.

## Installation

```bash
# skills.sh install, using the source string this guide is indexed from
npx skills add louisblythe/sales-skills
```

```bash
# The README's own CLI form, which still uses the repository's original name
npx add-skill louisblythe/salesskills

# Install only the skills you want
npx add-skill louisblythe/sales-skills --skill closing objection-handling pricing-negotiation
```

Slash commands for the Claude Code plugin route, also from the README:

```text
/plugin marketplace add louisblythe/salesskills
/plugin install sales-skills
```

`louisblythe/salesskills` is the repository's original name. It still resolves - `github.com/louisblythe/salesskills` returns a 301 to `github.com/louisblythe/Sales-Skills`, and the raw README path returns 200 - so the README commands keep working even though the repo has been renamed. The suite needs no API key, no CLI binary and no Python: every skill is a single markdown file.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| appointment-booking | 882 | Designing a sales bot's calendar integration: booking, rescheduling and autonomous meeting scheduling |
| objection-handling | 616 | Turning prospect pushback into a next step without becoming defensive, with scripts per objection type |
| sales-presentations | 578 | Pitch decks, demo presentations and proposal decks: structure, design and delivery |
| outbound-prospecting | 530 | Prospecting strategy, lead sourcing, target account lists and multi-channel outreach |
| closing | 523 | Recognising buying signals, asking for the sale and moving a qualified deal to commitment |
| sales-psychology | 511 | 70+ mental models for buyer behaviour, decision making and ethical persuasion |

The remaining 116 indexed listings range from 396 to 494 installs and hold most of the library: follow-up-discipline 494, discovery 479, email-sequence 473, pricing-negotiation 472, qualifying-leads 469, pipeline-management 462, negotiation 460, all the way down to competitor-mention-handling 396. The 80 AI SDR skills live entirely in this tail, so the table above shows the human-sales half of the suite; the bot-design half is indexed but never clears 500 installs.

## Why This Matters for Hermes Agents

Sales is the domain where an agent's generic advice is most obviously generic. "Build rapport and handle objections" is not a playbook. These skills are written as operator instructions with intake questions, frameworks and worked scripts, so an agent asked to write a discovery call plan produces MEDDIC-aligned questions instead of a list of pleasantries.

The second value is the split between human and bot work. An agent helping a rep prepare a call, write a follow-up and review a lost deal needs the 42 core and process skills. An agent helping an engineer design an autonomous SDR needs the 80 bot skills, which cover the parts that break in production: how to detect a handoff moment, how to keep multi-turn context, how to avoid duplicate outreach across channels, how to score response confidence and escalate when unsure. Very few skill libraries separate those two audiences this explicitly.

The third is compliance surface. `compliance-handling` covers opt-outs, do-not-call lists and TCPA and ACMA obligations; `legal-compliance-phrase-avoidance` lists the phrasings that create liability; `message-deliverability-optimization` and `spam-bot-detection-avoidance` cover sender reputation. For teams wiring an agent into outbound, having those three as reviewable documents in the repo is more useful than a policy paragraph in a wiki.

Finally, the process skills are the ones a founder or RevOps lead can hand to an agent and get an artefact back: a qualification scoring model, a battlecard, a territory launch plan, a win-loss taxonomy. That is work a small team usually outsources, and here it is one prompt per artefact.

## Usage

| You say | What happens |
|---|---|
| "Write a cold outreach sequence for CFOs at mid-market SaaS" | outbound-prospecting frames the account list, email-sequence builds the cadence, copywriting writes the variants |
| "How do I answer 'we already have a vendor'?" | objection-recognition classifies the objection, objection-handling writes the response, competitive-positioning keeps it non-disparaging |
| "Build a battlecard against our biggest competitor" | competitor-alternatives produces the battlecard and competitive-intelligence-gathering supplies the inputs |
| "Our demo show rate is 40 percent" | meeting-conversion works the show-rate problem and meeting-confirmation-reminder-logic designs the reminder flow |
| "Design the qualification logic for our inbound bot" | lead-qualification-logic and ideal-customer-profile-matching score and route leads, budget-extraction-qualification handles budget signals without asking directly |
| "Prep the pricing conversation for this renewal" | pricing-negotiation and pricing-discussion-logic set the quote, deflect and escalation points before the call |
| "Why did we lose the last three deals?" | deal-review-win-loss and win-loss-reason-extraction produce a structured review and a reason taxonomy |

## Verification

Confirm what landed in the skills directory:

```bash
npx skills list | grep -iE "closing|objection|pricing"
```

Read the top skills before installing. All four URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/louisblythe/Sales-Skills/main/README.md
curl -sL https://raw.githubusercontent.com/louisblythe/Sales-Skills/main/skills/appointment-booking/SKILL.md
curl -sL https://raw.githubusercontent.com/louisblythe/Sales-Skills/main/skills/objection-handling/SKILL.md
curl -sL https://raw.githubusercontent.com/louisblythe/Sales-Skills/main/skills/closing/SKILL.md
```

Check the repo really is markdown-only before you trust it with a sales process:

```bash
git clone --depth 1 https://github.com/louisblythe/Sales-Skills.git
find Sales-Skills -type f ! -name '*.md' ! -name '*.json'
```

The command returns nothing: there are no scripts, no hooks and no config beyond `marketplace.json`.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| appointment-booking | Pass | Pass | Pass |
| objection-handling | Pass | Pass | Pass |
| closing | Pass | Pass | Pass |

All three verdicts are Pass, which matches the contents: 122 markdown files, no executables, no network calls, no credential handling, no MCP server and no `allowed-tools` declaration in any skill. The only file a skill can influence is the agent's own context.

The risk here is not code execution, it is behaviour. Several of the 80 bot skills describe actions a bot would take on a real person - voicemail drops, SMS and email fallback, re-engagement sequences, scarcity and urgency calibration, ghost recovery. The skills are guidance for whoever builds that system, not a running system, but if you install them into an agent that also holds outreach tooling, the agent now has written instructions for those actions. Read `compliance-handling`, `legal-compliance-phrase-avoidance` and `human-in-the-loop-training` before letting an agent act on the bot half, and check your jurisdiction's consent rules for call recording, which the core skills explicitly assume ("record a call, with permission").

## Limitations

- No LICENSE file. GitHub's metadata reports no license at all; the README ends with "MIT - Use these however you want." Treat that as documented intent rather than a verified grant, and get written confirmation before redistributing the skills inside a product.
- One publication, no maintenance trail: the repo was created and last pushed within a day (2026-01-23 to 2026-01-24) and `marketplace.json` declares v5.0.0 with no changelog. There is no evidence of fixes after launch.
- Naming drift runs in two directions: skills.sh indexes it as `louisblythe/sales-skills`, GitHub's full name is `louisblythe/Sales-Skills`, and the README plus plugin manifest still point at `louisblythe/salesskills`. The old name redirects today, but a redirect is not a guarantee.
- Only 6 of 122 listings clear 500 installs, and the whole 80-skill AI SDR group sits in the tail. Install counts here measure indexing reach more than proven quality.
- Breadth over depth: several pairs overlap (objection-handling and objection-recognition, qualifying-leads and lead-qualification and lead-qualification-logic, closing and meeting-conversion). Ask one question and the agent may load two skills with adjacent advice.
- No evals, no test cases and no examples of expected output in the repo, so skill quality has to be judged by reading the file.
- Snapshot data, verified Oct 26, 2026: 51,654 combined installs across 122 indexed listings; 188 GitHub stars; no license; last pushed 2026-01-24. Counts drift over time.

## Related

- [GTM Agents - Go-to-Market Sales Skills Setup](/hermes/skills/catalog/gtm-agents-setup) - a smaller sales methodology suite with procurement and bid libraries alongside outreach.
- [Claude GTM Plugin Skills - GTM Teams Setup](/hermes/skills/catalog/claude-gtm-plugin-setup) - marketing-side GTM skills: market research, funnel analytics, CRO and lead generation.
- [Salesforce Skills Library (sf-skills) - 330+ Agent Skills Setup](/hermes/skills/catalog/salesforce-sf-skills-setup) - the CRM-side counterpart, for work inside a Salesforce org rather than on the conversation.
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup) - deeper copywriting craft to pair with copywriting and email-sequence.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the Core 20. The 80 AI SDR skills assume you are building a system with channels, state and escalation; loaded into a normal assistant session they mostly add noise.
- Paste a real transcript into objection-handling rather than describing the call. The skill is written to work from the actual wording, and the output quality gap is large.
- Pick one of each overlapping pair. objection-handling for writing the response, objection-recognition for classifying it; do not load both for the same request.
- Install selectively. `--skill closing objection-handling pricing-negotiation` keeps the context small, which matters when 122 skill descriptions are competing to be selected.
- Before automating anything from the bot half, decide who owns the compliance review. The skills tell you what to say; they do not tell you whether you are allowed to say it in your market.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
