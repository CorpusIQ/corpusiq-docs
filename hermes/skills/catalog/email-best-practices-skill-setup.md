---
title: "Email Best Practices Skill - Deliverability for Agents"
description: "resend/email-best-practices on skills.sh: 8.2K combined installs; one skill routing eleven references on deliverability, compliance and reliability."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/email-best-practices-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "email deliverability", "spf dkim dmarc", "email compliance"]
---

# Email Best Practices Skill - Setup Guide

**Source:** [resend/email-best-practices](https://www.skills.sh/resend/email-best-practices) via skills.sh - 8,225 combined installs across 1 indexed listing; first seen 2026-11-08 (Nov 8, 2026 morning sweep)
**GitHub:** 147 stars, no licence file in the repo root, `main` branch, last pushed 2026-10-09, 1 SKILL.md at the repository root with eleven reference files under `references/`
**Category:** Deliverability for agents: sender authentication, list hygiene, sending patterns and rendering rules for transactional email
**Quality Tier:** 🟡 Use With Care - all three scanners pass and the content is substantial, but the repository has no licence file and only 147 stars against 8,225 installs.

The skill is a router plus a library. `SKILL.md` is 73 lines, and almost all of it is a quick-reference table mapping a problem to the reference file that solves it, followed by four situation-based entry paths: new app, spam issues, marketing email, and production-ready sending. The other 1,836 lines live in eleven files under `references/`, and the agent is expected to read one or two of them rather than all of them. That design is deliberate and it is the reason the skill stays useful in a long session: the routing table costs about a hundred lines of context, and the detail loads on demand.

What sits behind the routing table is the operational core of email, stated as thresholds rather than principles. DMARC rollout is a sequence: `p=none` to monitor, then `p=quarantine; pct=25`, then `p=reject`. Bounce rate targets are numeric: under 1 percent good, 1 to 3 percent acceptable, 3 to 4 percent concerning, above 4 percent critical. Hard bounces get removed immediately, soft bounces retry at 1, 4 and 24 hours and get removed after three to five failures. Complaint rate above 0.05 percent is critical. New IP warming is a four-week table from 50 to 100 messages a day to 5,000 to 10,000. Those numbers are the reason to install this rather than let an agent improvise: they are not derivable from general knowledge, and a wrong one costs inbox placement.

The skill is Resend-authored and Resend-flavoured, which is worth stating plainly. The architecture diagram, the idempotency examples and the webhook sections use the Resend API, and the homepage points at `resend.com/agent-skills`. Most of the guidance is provider-neutral, particularly the DNS, compliance and list-hygiene material, but an agent following the code samples will write Resend calls.

## Installation

The README's install is one command, and the skill is installed as a folder rather than a package:

```bash
npx skills add resend/email-best-practices
```

That places `SKILL.md` and the `references/` directory into the agent's skills path. Because it is a plain folder of markdown, copying it into any harness's skills directory also works, but the relative links inside `SKILL.md` (`./references/deliverability.md` and the rest) only resolve if the whole directory comes along. Copying `SKILL.md` alone produces a skill that points at eleven files which are not there.

There is no npm package, no plugin marketplace entry and no CLI. The frontmatter's `metadata.openclaw` block carries links to the repository and the documentation page only, so `npx skills add` is the entire install surface.

## What It Provides

The threshold for this guide is zero installs, so the single indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| email-best-practices | 8,225 | Routing an agent to the right email reference: SPF, DKIM and DMARC, transactional design, capture, compliance, retries, webhooks, list hygiene and accessibility |

One row clears the threshold, and since the threshold is zero there is no tail. No rows fall below the threshold.

The install count and the star count tell different stories, and both are in the record. 8,225 installs against 147 stars means the skill is being pulled through the skills CLI by people who never visited the repository. That is a normal pattern for a documentation skill indexed under a well-known vendor namespace, and it also means the star count is not a useful quality signal here. The tier is Yellow for the same reason the licence bullet below matters: adoption is strong, repository hygiene is thin.

The eleven references are worth naming, because the routing table is only as good as what it points at:

- `deliverability.md` covers SPF, DKIM and DMARC with `dig` verification commands, sender reputation, IP warming, bounce and complaint handling, and a spam-troubleshooting order that starts with authentication.
- `transactional-email-catalog.md` is the longest file at 418 lines and plans which emails an application needs (password reset, verification, receipts, notifications) before you write any of them.
- `transactional-emails.md` covers the design of those messages: subject lines, structure, mobile-first layout.
- `email-capture.md` covers signup forms, validation and double opt-in.
- `marketing-emails.md` covers consent, segmentation and unsubscribe.
- `compliance.md` covers CAN-SPAM, GDPR and CASL, the unsubscribe requirements, and the `List-Unsubscribe` header that Gmail and Yahoo require of bulk senders.
- `sending-reliability.md` covers idempotency keys, retry behaviour and error handling.
- `webhooks-events.md` covers event types, signature verification, idempotent processing and local testing with ngrok.
- `list-management.md` covers suppression lists, pre-send checks, list hygiene jobs, retention and transactional versus marketing lists.
- `accessibility.md` is the largest after the catalog, at 189 lines, covering `lang` and `dir`, presentational tables, heading order, alt text, `<title>` and contrast.
- `email-types.md` is the decision file: transactional versus marketing, and why the distinction changes consent and unsubscribe obligations.

Two of those details are the kind of thing an agent gets wrong by default. The idempotency section derives keys from the business event (`password-reset-${userId}-${resetRequestId}`) rather than from a random value generated per attempt, which is the difference between retrying safely and sending three password resets. And the suppression check is placed before the send in the architecture diagram, not after a bounce comes back, which is what keeps a hard-bounced address from being retried on the next campaign.

## Why This Matters for Hermes Agents

Agents write email features more often than they write email infrastructure, and the failure is rarely a bad template. It is a password reset endpoint with no idempotency key that mails twice on a timeout, a webhook handler that trusts an unsigned payload, a marketing send with no `List-Unsubscribe` header, or a DMARC record pushed to `p=reject` in one step and a week of legitimate mail rejected. Each of those has a specific, written answer in one of the references, and an agent that has read the file produces the answer instead of a plausible guess.

The routing table is the part that fits Hermes specifically. Hermes runs whole features in one session, and a skill that loads 1,836 lines up front would eat the context it needs for the work. This one loads a table, and the agent fetches the single reference that matches the task: deliverability for DNS, sending-reliability for retry logic, list-management for bounces. That is the same pattern as progressive disclosure in a well-built skill directory, and it is why one skill can cover a domain this wide.

The third fit is that the guidance is checkable. SPF, DKIM and DMARC are DNS records, and the reference gives the `dig` commands to read them back. Bounce and complaint rates are numbers with published thresholds. That turns an email review into a set of assertions an agent can run, which is a better outcome than a paragraph of best-practice prose that nobody can falsify.

The caveat is authority. This is a vendor's playbook, not a standard, and the compliance file is engineering guidance rather than legal advice. Where it disagrees with your provider's documentation or your counsel, they win.

## Usage

| You say | What happens |
|---|---|
| "Our emails are going to spam" | Routes to `deliverability.md` and checks in order: SPF, DKIM, DMARC, then `List-Unsubscribe`, then reputation, then content |
| "Set up email authentication for this domain" | Writes the SPF and DKIM records, adds DMARC at `p=none`, and gives the `dig` commands to verify each one |
| "New SaaS, we need email" | Starts from the transactional catalog to decide which emails exist, then authentication, then reliability |
| "Add a password reset endpoint" | Idempotency key from the user and request IDs, retry behaviour, and a suppression check before send |
| "Handle bounce webhooks" | Verifies signatures, suppresses hard bounces immediately, retries soft bounces at 1, 4 and 24 hours |
| "We are launching a newsletter" | Capture with double opt-in, then compliance, then segmentation and unsubscribe handling |
| "Is this signup flow GDPR compliant" | Works through consent, records, retention and the privacy policy contents for the region in question |
| "Make the receipt email accessible" | `lang` and `dir`, heading order, descriptive alt text, 4.5:1 contrast, presentational tables |

## Verification

This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/resend/email-best-practices/main/SKILL.md | head -40
```

It should open with YAML frontmatter naming `email-best-practices`, a single-sentence description that lists the triggers (spam, bounces, SPF/DKIM/DMARC, compliance, webhooks, accessibility), `license: MIT`, and a `metadata` block with `author: Resend` and `version: "1.0.2"`. Below the frontmatter you should see `# Email Best Practices`, then the ASCII architecture diagram that runs from the signup form through double opt-in, consent, suppression check, idempotent send and webhook events, and finally the `## Quick Reference` table.

Confirm the references resolve, since the skill is useless without them:

```bash
curl -fsSL https://raw.githubusercontent.com/resend/email-best-practices/main/references/deliverability.md | head -40
```

That should print `# Email Deliverability`, then `## Email Authentication` with the note that Gmail, Yahoo and Microsoft require authentication, then the SPF record, the DKIM pointer, and the DMARC block with `v=DMARC1; p=none` and the rollout line `p=none` to `p=quarantine; pct=25` to `p=reject`. A 404 here means the skill will route the agent to a file that is not installed.

After install, check the directory rather than the file:

```bash
ls -1 <skills-path>/email-best-practices/references | wc -l
```

The answer should be 11. If it is 1 or 0, only `SKILL.md` landed and the skill will fail at exactly the moment it becomes useful.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| email-best-practices | Pass | Pass | Pass |

All three scanners pass, and for this skill that verdict is narrow: the repository is markdown and test scenarios, so there is nothing executable to fail. The `tests/` directory holds five prompt scenarios and a README, not an automated suite, and nothing in the package runs on install.

The licence is the structural problem. There is no LICENSE file in the repository root, so the default position is that no rights are granted beyond viewing. The `SKILL.md` frontmatter asserts `license: MIT`, which is a statement in a metadata block rather than a licence text with a copyright holder behind it. If you plan to vendor this into a product, ship a modified copy, or redistribute it internally, treat that as unresolved and ask the maintainer rather than relying on the frontmatter line. This is not a code-safety warning; it is the reason the tier is Yellow and not Green.

The operational risk is larger than the packaging. This skill tells an agent to change DNS. An SPF record that drops a legitimate sender, or a DMARC policy that jumps to `p=reject`, takes down mail for every application on the domain, and the effect is invisible for hours because of TTLs. The reference's own rollout sequence exists to prevent exactly that, and it should be read before the agent touches a zone file. Apply changes in a staging subdomain first where possible, and keep the previous records to hand.

The second operational risk is data. Webhook handlers receive recipient addresses, delivery metadata and complaint details, and the compliance references ask you to define retention periods for them. That is personal data under GDPR and it needs a retention policy before the first webhook is stored, not after.

## Limitations

- Snapshot data, verified 2026-11-08: 8,225 installs across 1 indexed listing, 147 GitHub stars, `main` branch, last pushed 2026-10-09. The repository reports no licence, and the tree contains no LICENSE file.
- Licence status is unresolved despite the MIT claim in `SKILL.md` frontmatter. No LICENSE file means no explicit grant, so redistribution is a legal question rather than a packaging detail.
- 1 indexed listing and 1 SKILL.md at the repository root match, so there is no directory drift. There is also no second listing to cross-check the install count against.
- The content is Resend-authored. The DNS, compliance and list-hygiene advice is provider-neutral, but the architecture diagram, code samples and CLI references assume Resend, and a Postmark or SES user has to translate.
- The 1,836 lines across eleven references are the real package, and the agent must load the right ones. A harness that reads the whole directory into context will spend more on this skill than on the task.
- Compliance coverage is CAN-SPAM, GDPR and CASL plus a short note on other regions. It is engineering guidance, not legal advice, and it will not settle a jurisdiction question.
- The tests are five manual prompt scenarios plus a README describing the RED-GREEN protocol. The `results.md` that README points at is not in the tree, so there is no published comparison of baseline versus skill-loaded output.
- Version is declared as 1.0.2 in `SKILL.md` frontmatter with no release tags and no changelog, so an install cannot be pinned to a release.
- The 147 stars are a weak independent signal; almost all adoption is through the skills CLI, so there is little external review to lean on.

## Related

- [Resend Agent Skills - Setup Guide](/hermes/skills/catalog/resend-skills-setup)
- [React Email Skill - Template Authoring for Agents](/hermes/skills/catalog/react-email-skill-setup)
- [IMAP/SMTP Email - OpenClaw Email Integration Setup Guide](/hermes/skills/catalog/imap-smtp-email-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load the routing table, not the library. Ask the agent to read `SKILL.md` and then exactly one reference, and name the file yourself if you already know the problem.
- Run the `dig` checks before believing any diagnosis. `dig TXT <domain> +short`, `dig TXT <selector>._domainkey.<domain> +short` and `dig TXT _dmarc.<domain> +short` settle three of the five spam causes in seconds.
- Split transactional and marketing onto separate subdomains, which the deliverability reference recommends directly. Complaint and bounce rates then cannot contaminate the mail that must arrive.
- Keep DMARC at `p=none` for at least a reporting cycle before moving to quarantine, and read the `rua` reports rather than skipping straight to enforcement.
- Use the transactional catalog as a planning artefact before writing any code. Deciding which emails exist, and which are marketing, changes the consent and unsubscribe obligations for every one of them.
- Treat every threshold in the references as a monitoring target, not a one-time check: bounce under 1 percent, complaint under 0.05 percent, and re-read them monthly.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
