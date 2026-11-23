---
title: "Sinch Agent Skills - Communication APIs Setup"
description: "Sinch agent skills for communication APIs: SMS, voice, email, numbers, verification and fax guidance inside AI agents - 5.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sinch-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "cpaas", "sms", "email"]
---

# Sinch Agent Skills - Communication APIs Setup

**Source:** [sinch/skills](https://www.skills.sh/sinch/skills) via skills.sh - 5.3K combined installs across 28 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [sinch/skills](https://github.com/sinch/skills) - 11 stars, Apache-2.0, main branch, last pushed Oct 3, 2026; one SKILL.md per product directory under skills/ with references/, scripts/ and assets/ alongside.
**Category:** Communication APIs and Messaging Development
**Quality Tier:** 🟡 Yellow - 10 Warn cells (all Snyk) and no Fail cells across the 20-skill sample.

Sinch publishes AI agent skills for its communication APIs, giving an agent expert guidance on getting started, best practices and gotchas right inside the coding assistant. The suite spans the Sinch product line: Conversation API for omnichannel messaging, SMS, MMS, RCS and WhatsApp channels, the Voice API, Elastic SIP Trunking, the Mailgun email product, number search and porting, verification, and the beta Functions runtime. Every skill lives in its own folder under skills/ with a SKILL.md that carries YAML frontmatter plus Overview, Getting Started, Key Concepts, Common Patterns, and Gotchas and Best Practices sections.

The distribution is notable for its breadth and flatness. The top 19 skills sit in a tight band of 192 to 274 installs, with authentication, the Conversation API and Fax at the head, and the channel-specific and Functions skills trailing behind. The README states that every example uses curl or the Node.js SDK (@sinch/sdk-core) except the Mailgun skills, which use mailgun.js, and that use of Sinch services requires a valid Sinch account under the Sinch Terms of Service.

## Installation

Install the full set through the skills CLI:

```bash
npx skills add sinch/skills
```

The skills can also be installed through the Sinch Plugins repository, which packages them for supported agents.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sinch-authentication | 274 | OAuth2, API keys and application signing for any Sinch product |
| sinch-conversation-api | 268 | omnichannel messaging across SMS, MMS, RCS, WhatsApp and more |
| sinch-fax-api | 259 | sending and receiving faxes programmatically |
| sinch-mailgun | 253 | Mailgun email sending, receiving and tracking |
| sinch-numbers-api | 234 | searching, renting, managing and releasing phone numbers |
| sinch-provisioning-api | 231 | provisioning WhatsApp, RCS and KakaoTalk senders and templates |
| sinch-10dlc | 230 | US 10DLC brand and campaign registration for A2P SMS |
| sinch-voice-api | 229 | building voice apps with SVAML, IVR, TTS and conferencing |
| sinch-number-lookup-api | 229 | carrier, line type and fraud-signal lookups |
| sinch-verification-api | 226 | phone verification via SMS, flashcall, call or WhatsApp |
| sinch-elastic-sip-trunking | 226 | provisioning SIP trunks, endpoints, ACLs and credentials |
| sinch-mailgun-validate | 225 | email address validation and list hygiene |
| sinch-mailgun-inspect | 225 | previewing email rendering and accessibility before send |
| sinch-mailgun-optimize | 221 | deliverability monitoring via InboxReady |
| sinch-in-app-calling | 220 | voice and video calling in Android, iOS and web apps |
| sinch-number-order-api | 218 | number ordering with KYC compliance |
| sinch-imported-numbers-hosting-orders | 217 | importing, hosting and text-enabling non-Sinch numbers |
| sinch-sdks | 212 | SDK install and client init for Node, Python, Java and .NET |
| sinch-porting-api | 192 | porting numbers into Sinch with LOA and order tracking |

The remaining 9 indexed listings range from 56 to 128 installs.

## Why This Matters for Hermes Agents

An agent that integrates with a communications platform without these skills will reach for wrong endpoints, skip authentication setup and mis-handle channel-specific rules such as WhatsApp's 24-hour window, 10DLC registration, or SMS opt-out handling. The highest-value skills are sinch-authentication, which configures OAuth2, Basic auth, API keys and signing once so every later call works, and sinch-conversation-api, which owns the omnichannel layer including message types, templates, batch sending and channel fallback. The channel skills (sinch-sms, sinch-mms, sinch-rcs, sinch-whatsapp) carry the encoding, sender-ID and opt-out details that differ per channel, while the Mailgun trio separates sending, inspection and deliverability so an agent does not conflate them. For an operator the suite reads as a self-contained handbook where each SKILL.md documents its own gotchas, so an agent can resolve an integration problem by loading the one skill that matches the failing product.

## Usage

| You say | What happens |
|---|---|
| Install Sinch skills | Adds sinch/skills through the skills CLI to the agent's skills directory |
| Set up Sinch API credentials | Uses sinch-authentication for OAuth2, API keys and signing |
| Send an SMS and handle STOP replies | Routes to sinch-sms for sender IDs, encoding and opt-out handling |
| Register a 10DLC campaign | Uses sinch-10dlc for brand and campaign registration workflow |
| Why are my emails landing in spam? | Uses sinch-mailgun-optimize for deliverability and blocklist monitoring |
| Verify a phone number on signup | Uses sinch-verification-api for SMS or silent verification flows |
| Port a number into Sinch | Uses sinch-porting-api for portability checks and LOA upload |

## Verification

Confirm the repository README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/sinch/skills/main/README.md | head -30
```

Confirm the omnichannel messaging skill body is present before relying on it for a messaging integration:

```bash
curl -sL https://raw.githubusercontent.com/sinch/skills/main/skills/sinch-conversation-api/SKILL.md | head -30
```

Confirm the SMS channel skill body is present before using it for sender-ID and encoding decisions:

```bash
curl -sL https://raw.githubusercontent.com/sinch/skills/main/skills/sinch-sms/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sinch-authentication | Pass | Pass | Warn |
| sinch-conversation-api | Pass | Pass | Warn |
| sinch-fax-api | Pass | Pass | Warn |
| sinch-mailgun | Pass | Pass | Warn |
| sinch-numbers-api | Pass | Pass | Pass |
| sinch-provisioning-api | Pass | Pass | Warn |
| sinch-10dlc | Pass | Pass | Pass |
| sinch-voice-api | Pass | Pass | Warn |
| sinch-number-lookup-api | Pass | Pass | Pass |
| sinch-verification-api | Pass | Pass | Pass |
| sinch-elastic-sip-trunking | Pass | Pass | Pass |
| sinch-mailgun-validate | Pass | Pass | Warn |
| sinch-mailgun-inspect | Pass | Pass | Pass |
| sinch-mailgun-optimize | Pass | Pass | Pass |
| sinch-in-app-calling | Pass | Pass | Pass |
| sinch-number-order-api | Pass | Pass | Warn |
| sinch-imported-numbers-hosting-orders | Pass | Pass | Warn |
| sinch-sdks | Pass | Pass | Pass |
| sinch-porting-api | Pass | Pass | Warn |
| sinch-sms | Pass | Pass | Pass |

Ten of the 20 sampled skills carry a Snyk Warn, all other cells are Pass, and no sampled skill Fails; eight of the 28 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 5,273 combined installs across 28 indexed listings; 11 GitHub stars; Apache-2.0; last pushed Oct 3, 2026. Counts drift over time.
- The install counts form a flat band: the top 19 skills range only from 192 to 274 installs, so rankings within the table are not a strong quality signal.
- Eight of the 28 indexed listings (the Functions trio, sinch-cli, sinch-mms, sinch-rcs, sinch-whatsapp and sinch-voice-api-v2 among them) carry no published security verdict in the sampled set.
- The skills.sh index and the repository tree agree on all 28 listing names, so there is no name drift to resolve here.
- Using Sinch services requires a valid Sinch account and is subject to the Sinch Terms of Service, which the README links.

## Related

- [Twilio Agent Skills - SMS, Voice and Messaging APIs](/hermes/skills/catalog/twilio-agent-skills-setup)
- [Resend Agent Skills - Setup Guide](/hermes/skills/catalog/resend-skills-setup)
- [Email Best Practices Skill - Deliverability for Agents](/hermes/skills/catalog/email-best-practices-skill-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Configure sinch-authentication first: every other skill assumes valid OAuth2 or Basic auth, and 401 and 403 errors route back to it.
- Use sinch-conversation-api for the omnichannel layer and drop to the channel-specific skills only for encoding, sender-ID and opt-out details.
- Treat the Mailgun trio as three separate jobs: validate cleans the list, inspect previews rendering, optimize monitors deliverability.
- Run the 10DLC registration workflow before sending US SMS on long codes, and do not use it for non-US or toll-free and short-code messaging.
- Pin to the Node.js SDK examples the README recommends, except for Mailgun work, which uses mailgun.js.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
