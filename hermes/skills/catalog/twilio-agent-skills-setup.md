---
title: "Twilio Agent Skills - SMS, Voice and Messaging APIs"
description: "twilio/ai on skills.sh: 5.5K combined installs; official Twilio skills for SMS, WhatsApp, voice, Verify, SendGrid and compliance"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/twilio-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "twilio", "sms", "voice", "sendgrid"]
---

# Twilio Agent Skills - Setup Guide

**Source:** [twilio/ai](https://www.skills.sh/twilio/ai) via skills.sh - 5.5K combined installs across 20 indexed listings; sampled 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 40 stars, MIT licensed, `main` branch, last pushed 2026-10-22, 57 `SKILL.md` files in 236 blobs, split between `skills/twilio/` and `skills/sendgrid/` and grouped by the README into setup, planner, product and guardrail categories
**Category:** Communications: SMS, WhatsApp, voice, email and conversation APIs for customer messaging
**Quality Tier:** 🟡 Solid with caveats - MIT licensed official Twilio skills, mostly Pass verdicts with two Snyk Warnings in the sample.

Twilio's AI repository is the official skill and MCP distribution for the company's communications APIs, published as a public beta. The README states plainly that beta features can change and are not covered by Twilio's support terms or service level agreement, which is the right frame for everything below: the material is authoritative about the products, and the packaging is still moving. It ships two things. The MCP server at `https://mcp.twilio.com/docs` exposes two tools, `twilio__search` for natural language search over Twilio documentation and API operations, and `twilio__retrieve` for the full parameter schema of a named operation. The skills are `SKILL.md` packages covering SMS, MMS, WhatsApp, RCS, Voice, Verify, SendGrid, Conversations, Messaging Services and the compliance programmes that gate traffic.

The suite is organised by intent rather than by product catalogue. Setup skills handle account, credentials and numbers; planner skills qualify a use case before any code exists; product skills cover one API done correctly; guardrail skills carry the operational patterns that prevent outages and policy violations. The publisher page claims 58 skills and the tree holds 57 `SKILL.md` files, so the counts are close but not identical. The skills.sh source page renders 20 listings, and those are the ones counted below.

## Installation

The skills CLI installs one skill at a time, and the command names it:

```bash
npx skills add https://github.com/twilio/ai --skill twilio-send-message
```

Swap the skill name for any entry in the table. This is the lightest route and it does not register the MCP server, so the agent gets the procedure but not live documentation search.

Claude Code users get skills and MCP together from the plugin marketplace:

```text
/plugin marketplace add twilio/ai
/plugin install twilio-developer-kit@twilio
```

Skills activate when a prompt matches a covered use case, and they can also be invoked directly, for example `/twilio-verify-send-otp` or `/twilio-sms-send-message`.

Cursor reads the open Agent Skills layout from `.agents/skills/`, so the README's route is a clone and a copy:

```bash
git clone https://github.com/twilio/ai.git .twilio-ai
cp -r .twilio-ai/skills/ .agents/skills/
```

For Codex, the README adds the MCP server and copies the skills to the user-level directory:

```bash
codex mcp add twilio-docs --url https://mcp.twilio.com/docs
git clone https://github.com/twilio/ai.git
cp -r ai/skills/ ~/.agents/skills/
```

Other hosts that support the Agent Skills standard can load the `skills/` directory directly, and any MCP client can use the streamable HTTP endpoint.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear in the table:

| Skill | Installs | Use For |
|---|---|---|
| twilio-sms-send-message | 927 | SMS and MMS deep dive: SMS error codes, message filtering diagnostics, MMS media limits and SMS pumping indicators; the file itself says to use twilio-send-message for sending |
| twilio-send-message | 785 | Sending SMS, MMS, RCS and WhatsApp through the Messages API, including media, rich cards and carousels, templates, Messaging Services and status callbacks |
| twilio-sendgrid-email-send | 290 | Transactional and bulk email through the SendGrid v3 Mail Send API, with batch sends, dynamic templates, scheduling and sandbox mode |
| twilio-webhook-architecture | 284 | Designing and hardening webhook endpoints: inbound events, status callbacks, signature validation, retry and timeout tuning |
| twilio-security-hardening | 236 | Credential management, webhook signature checks, PCI and HIPAA requirements, SMS pumping defence and account isolation |
| twilio-messaging-overview | 220 | Channel overview and the onboarding sequence across SMS, WhatsApp, RCS and Messenger, before choosing a specific channel |
| twilio-account-setup | 215 | Account creation, trial limits, credentials, number purchase, SDK install and the first API call |
| twilio-compliance-traffic | 215 | TCPA, GDPR, PCI DSS, HIPAA, FDCPA, CAN-SPAM and WhatsApp policy rules for live messaging and voice traffic |
| twilio-reliability-patterns | 212 | 429 backoff with jitter, per-number throughput, StatusCallback resilience, the thin receiver pattern and fallback chains |
| twilio-messaging-webhooks | 211 | Receiving inbound messages and tracking delivery across SMS, MMS, WhatsApp and RCS, including TwiML replies and signature checks |
| twilio-sendgrid-email-settings | 207 | SendGrid dynamic templates, open and click tracking, link branding and HTML, plain text or AMP content types |
| twilio-sendgrid-deliverability-advisor | 202 | Diagnosing spam placement, blocks and bounces: SPF, DKIM, DMARC, BIMI, IP warmup and reputation thresholds |
| twilio-sendgrid-account-setup | 202 | SendGrid API keys, domain authentication, Single Sender Verification and the credential split from Twilio |
| twilio-numbers-senders | 198 | Choosing number and sender types (local, toll-free, short code, alphanumeric, WhatsApp, RCS) before building |
| twilio-cli-reference | 194 | Terminal operations: profiles, number provisioning, sending, webhooks, tunnels, logs and serverless deploys |
| twilio-verify-send-otp | 187 | Verify service setup and OTP send and check over SMS, voice, email or WhatsApp, including fallback behaviour |
| twilio-voice-twiml | 185 | Call logic in TwiML: Say, Play, Gather, Dial, Record and Conference, with a complete inbound IVR example |
| twilio-messaging-channel-advisor | 185 | Picking SMS, MMS, RCS or WhatsApp by content type, geography, use case, cost model and brand presence |
| twilio-compliance-onboarding | 185 | Pre-traffic registrations: A2P 10DLC, toll-free verification, WhatsApp WABA, RCS, short code and voice trust programmes |
| twilio-debugging-observability | 184 | Console Debugger, Monitor Alerts, Event Streams, status callbacks, error codes and a systematic debugging workflow |

No indexed listings fall below the threshold; all 20 appear above.

The distribution is unusual for a vendor suite. The single most installed entry, `twilio-sms-send-message` at 927, is a diagnostic reference that explicitly defers to `twilio-send-message` for actual sends. That second skill sits at 785. Together they dominate the set, and everything else falls below 300. The compliance pair matters more than its install count suggests: registration blocks traffic on every number type, so an agent that skips `twilio-compliance-onboarding` will produce working code that fails at the carrier.

## Why This Matters for Hermes Agents

Twilio is one of the few APIs where a correct-looking integration can be illegal. Consent rules, quiet hours, opt-out handling and registration programmes are not edge cases; they are preconditions for the message to be delivered at all. The guardrail skills carry those rules in a form an agent can apply, which is more reliable than hoping the model remembers TCPA when it writes a cron job that texts customers at 2am.

The second gain is product selection. A model asked to "send a verification code" will reach for SMS by default, and the channel advisor plus the numbers skill ask the questions that change the answer: which country, what content, which sender type, what registration. That ordering prevents the expensive version of the mistake, where the number is bought and the campaign built before anyone checks whether the sender type is available.

Webhooks are the third. Inbound message handling fails on signature validation and status callback parsing far more often than it fails on the send call, and both webhook skills treat validation as part of the procedure rather than an optional hardening step.

The counterweight is that this is a public beta with a thin install record. Forty GitHub stars and 5.5K combined installs across 20 listings means the skills have not been through a large amount of community use. Treat them as vendor documentation with procedure attached, verify each API call against the current Twilio docs, and do not assume a beta surface will keep its shape.

## Usage

| You say | What happens |
|---|---|
| "Send an SMS confirming the appointment" | `twilio-send-message` builds the Messages API call with the right sender and status callback, after `twilio-numbers-senders` confirms the number type is usable |
| "Which channel should I use for order updates in Brazil?" | `twilio-messaging-channel-advisor` qualifies content type, geography, use case and cost, then recommends SMS, RCS or WhatsApp |
| "Set up OTP login" | `twilio-verify-send-otp` creates a Verify service, sends and checks tokens, and documents the WhatsApp to SMS fallback |
| "Our messages are being filtered" | `twilio-sms-send-message` runs the filtering diagnostic checklist and points at error codes and SMS pumping indicators |
| "Build an IVR for inbound calls" | `twilio-voice-twiml` assembles Say, Gather, Dial and Record verbs into an inbound call flow with SDK examples |
| "Why did our emails start going to spam?" | `twilio-sendgrid-deliverability-advisor` checks SPF, DKIM and DMARC, IP warmup, list hygiene and bounce thresholds |
| "Is this integration secure enough for production?" | `twilio-security-hardening` and `twilio-webhook-architecture` review credentials, signature validation and account isolation |

## Verification

The raw skill file sits under the `twilio` product folder, and this URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/twilio/ai/main/skills/twilio/twilio-sms-send-message/SKILL.md | head -6
```

The frontmatter should declare `name: twilio-sms-send-message` and a description that begins "SMS and MMS deep-dive reference", and the body should open with its filtering and error-code sections. SendGrid skills take the other folder, for example `https://raw.githubusercontent.com/twilio/ai/main/skills/sendgrid/twilio-sendgrid-email-send/SKILL.md`.

After a skills CLI install, confirm the skill landed as a directory containing `SKILL.md`:

```bash
test -f ~/.claude/skills/twilio-send-message/SKILL.md && echo ok
```

For the clone route the layout keeps the product folder, so the check is one level deeper: `~/.agents/skills/twilio/twilio-sms-send-message/SKILL.md`. If your agent reads the Hermes profile directory, use the same relative path under `~/.hermes/profiles/corpusiq/skills/`.

The MCP server has its own smoke test from the README: after setup, ask the agent "How do I send an SMS with Twilio?" and check that the answer covers Messaging Services, A2P compliance and error handling rather than generic training-data advice.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| twilio-sms-send-message | Pass | Pass | Pass |
| twilio-send-message | Pass | Pass | Pass |
| twilio-sendgrid-email-send | Pass | Pass | Pass |
| twilio-webhook-architecture | Pass | Pass | Pass |
| twilio-security-hardening | Pass | Pass | Pass |
| twilio-messaging-overview | Pass | Pass | Pass |
| twilio-account-setup | Pass | Pass | Pass |
| twilio-compliance-traffic | Pass | Pass | Pass |
| twilio-reliability-patterns | Pass | Pass | Pass |
| twilio-messaging-webhooks | Pass | Pass | Warn |
| twilio-sendgrid-email-settings | Pass | Pass | Pass |
| twilio-sendgrid-deliverability-advisor | Pass | Pass | Pass |
| twilio-sendgrid-account-setup | Pass | Pass | Pass |
| twilio-numbers-senders | Pass | Pass | Pass |
| twilio-cli-reference | Pass | Pass | Pass |
| twilio-verify-send-otp | Pass | Pass | Pass |
| twilio-voice-twiml | Pass | Pass | Warn |
| twilio-messaging-channel-advisor | Pass | Pass | Pass |
| twilio-compliance-onboarding | Pass | Pass | Pass |
| twilio-debugging-observability | Pass | Pass | Pass |

The sample is clean apart from two Snyk Warnings, on `twilio-messaging-webhooks` and `twilio-voice-twiml`. Both are skills that build request handlers, so a warning there is worth a look rather than a dismissal: read the Snyk page, then read the skill's code samples, which are the part a scanner can actually evaluate.

The larger risk is credential handling, and the skills are explicit about it. `twilio-security-hardening` prefers API keys over the account auth token, requires webhook signature validation and covers SMS pumping. An agent following the setup skill will still put an Account SID and Auth Token in a `.env` file, so scope the credentials and keep them out of the repository. For SendGrid, the split matters: the SendGrid skills require an `SG.` key and state that they do not apply to the Twilio Email API at `comms.twilio.com`, which uses different credentials.

Finally, every one of these skills can move money and send messages to real people. Nothing in the scanners covers that. Keep a test account and test numbers for development, and gate any production send behind a human check until you have watched the workflow behave.

## Limitations

- Snapshot data, verified 2026-11-09: 5,524 combined installs across 20 indexed listings; 40 GitHub stars; MIT license; last pushed 2026-10-22. Counts drift over time.
- The skills.sh source page renders at most 20 listings, while the repository carries 57 `SKILL.md` files and the publisher page claims 58. The 20 rows and the combined figure cover only the rendered page, so the total understates the suite.
- Twilio MCP and Twilio Skills are public beta. The README says features may change before general availability and that the beta is outside the support terms and the SLA.
- The skills are documentation-shaped, not executable tooling. They describe API calls and compliance rules; they do not call Twilio for you, and they do not validate that your account is provisioned for the channel they recommend.
- `twilio-sms-send-message` is the most installed listing but is a diagnostic reference that defers to `twilio-send-message` for sends. Installing only the former gives an agent error-code knowledge and no send procedure.
- The install routes differ in what they deliver: the CLI takes one skill, the Claude Code plugin adds the MCP server, and the Codex route adds a user-level MCP entry. The MCP server is a documentation search surface, not an account-operations API.

## Related

- [COSS Skills - One API for Email, SMS and Inboxes](/hermes/skills/catalog/coss-skills-setup)
- [n8n Skills - Workflow Automation for Business](/hermes/skills/catalog/n8n-skills-setup)
- [Zapier Agent Skills - Automation and App Actions](/hermes/skills/catalog/zapier-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `twilio-numbers-senders` and `twilio-compliance-onboarding` before writing any code. The number type and registration programme constrain everything downstream, and both are expensive to change after launch.
- Install `twilio-send-message` alongside `twilio-sms-send-message`. The first is the send procedure, the second is the debugging reference, and the second one says so in its own description.
- Treat the SendGrid folder as a separate product. Its skills need an `SG.` API key and explicitly exclude the Twilio Email API, so an agent that mixes the two will produce calls that fail authentication.
- Ask for the webhook signature check by name. Both webhook skills document validation, and agents routinely skip it when the request "already works" in a tunnel.
- Keep a status callback URL wired from the first test send. Delivery failures on SMS and WhatsApp surface there, not in the API response.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
