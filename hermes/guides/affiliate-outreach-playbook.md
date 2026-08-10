# Affiliate Outreach Playbook

The exact process used to send 42 affiliate promotion emails across 4 target categories on August 10, 2026. Repeatable. Measurable. Designed to scale.

## Target Categories

### 1. Connector Partnerships (7 targets)
Companies with pre-built integration libraries. The pitch: their connectors power the data layer, CorpusIQ adds the AI intelligence layer. Combined value proposition for business owners.

Targets: Merge.dev, Composio, Airbyte, Paragon, Apideck, Kombo, Pandium.

### 2. AI Directory Listings (19 targets)
Platforms that list AI tools and SaaS products. The ask: list CorpusIQ, include the affiliate program mention.

Targets: Toolify, AlternativeTo, Top AI Tools, Insidr.ai, Dang.ai, SaaS AI Tools, GPTForWork, AI Tool Guru, WhatTheAI.tech, Favird, TopAI.tools, BetaList, SaaS Hub, Launching Next, KillerStartups, BetaPage, StartupBase, 10words, SideProjectors.

### 3. Newsletter and Creator Platforms (8 targets)
AI-focused newsletters and creator platforms with large subscriber bases. The ask: feature the affiliate program to their audience.

Targets: There's An AI For That, Futurepedia, The Rundown AI, SuperTools, Ben's Bites, AI Valley, Every.to, Toolify (partnerships).

### 4. International and French/EU (8 targets)
Non-US platforms for global distribution. The pitch: French-founded company seeks international partners.

Targets: FrenchWeb, Startups.ch, French Tech Journal, Tech.eu, TechInAsia, TechNode, EU-Startups, Startup Digest.

## Email Template

```
Subject: [specific angle based on category]

Body:
- One-line intro: what CorpusIQ does
- The ask: specific to their platform
- The incentive: 25% recurring for 3 years, no cap
- The math: $891 per referral lifetime
- Call to action: would you be open to [specific next step]

Signature:
Ben
Founder, CorpusIQ
(877) 51-CORPUSIQ
corpusiq.io
```

## Follow-Up Cadence

- Initial outreach: Day 0
- First follow-up: Day 2
- Second follow-up: Day 7
- Final follow-up: Day 14
- After 14 days with no reply: archive, move to quarterly re-engagement

## Bounce Handling

When a delivery notification arrives:
1. Identify the bounced address from the email body
2. Remove from active outreach list
3. Search for alternative contact (LinkedIn, company website)
4. If no alternative found, mark as dead in tracker

## Metrics

Track per category:
- Emails sent
- Bounces
- Replies (positive, negative, needs more info)
- Conversions (affiliate signup, directory listing, partnership call)

## Automation Path

This playbook is designed to be automated by Hermes:
1. Pull target list from outreach-tracker
2. Generate personalized email from template
3. Send via Gmail API
4. Log to activity-log.jsonl
5. Monitor inbox for replies
6. Update tracker with response status

The human touch: personalization in the first line, category-specific angle in the subject, and the signature from Ben.
