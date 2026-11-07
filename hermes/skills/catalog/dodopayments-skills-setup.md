---
title: "Dodo Payments Skills - Billing and Checkout"
description: "dodopayments/skills on skills.sh: 9.0K combined installs; 18 official skills for checkout, subscriptions, credits, webhooks and billing UI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dodopayments-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "payments", "billing", "subscriptions"]
---

# Dodo Payments Skills - Setup Guide

**Source:** [dodopayments/skills](https://www.skills.sh/dodopayments/skills) via skills.sh - 9.0K combined installs across 18 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 13 stars, MIT, last pushed 2026-11-02, 18 SKILL.md directories under dodo-payments/, each with an optional references/ folder
**Category:** Payments for agents: checkout, subscriptions, credit billing, discounts, customer management and MCP usage patterns
**Quality Tier:** 🟡 Review - an official vendor catalogue with uniform Trust Hub and Socket passes and one sampled Snyk pass, held back by a small star count, four Snyk warnings in the sample and no community track record yet.

Eighteen skills from the payments company itself, not a community wrapper. They cover the whole integration surface of Dodo Payments, which is a Merchant of Record: Dodo is the legal seller on every transaction, registers and calculates sales tax across jurisdictions, remits it, and handles card-network disputes and chargebacks. What you build is the checkout session, the webhook handler and the access grant on payment success. The skills are written to that division of labour, which is why several of them spend their first section telling you what the platform already does so you do not build it twice.

The catalogue is grouped by job. Getting started: `dodo-best-practices`, `framework-adapters`, `testing-and-go-live`. Accepting payments: `checkout-integration`, `subscription-integration`, `mobile-checkout`, `webhook-integration`, `dodo-mcp-usage`. Billing models: `credit-based-billing`, `usage-based-billing`, `license-keys`. Catalogue and pricing, customers and operations, and UI round it out with `product-catalog-management`, `discounts-and-promotions`, `localized-pricing`, `customer-management`, `refunds-and-disputes`, `billing-sdk` and `better-auth-integration`.

The repository is tooled like a product rather than a prompt dump. `package.json` is version 2.0.0 and declares itself tooling only, with the skills being the `SKILL.md` files. Four CI checks run over them, and the validation pass is unusually specific: real API hostnames, correct test and live key formats, no hand-rolled webhook HMAC, no deprecated SDK calls, no type suppression, and agreement between each skill's directory name, its frontmatter, the marketplace manifest and the README table.

## Installation

The README's primary route installs all 18 skills with the skills CLI:

```bash
npx skills add dodopayments/skills
```

Individual skills are addressable by their path inside the repository, which is what most projects want, because nobody needs the whole catalogue in one context:

```bash
npx skills add dodopayments/skills/dodo-payments/dodo-best-practices
npx skills add dodopayments/skills/dodo-payments/webhook-integration
npx skills add dodopayments/skills/dodo-payments/subscription-integration
```

For Claude Code, the README documents the plugin marketplace route. Add the marketplace once:

```text
/plugin marketplace add dodopayments/skills
```

Then install the plugin you need:

```text
/plugin install dodo-best-practices
/plugin install webhook-integration
/plugin install subscription-integration
```

OpenCode picks the skills up automatically once they are configured in its settings. There is no install step beyond that.

If you are working on the repository itself rather than consuming it, the tooling has dependencies and a full check:

```bash
npm install
npm run check
```

`npm run check` chains `validate`, `typecheck`, `typecheck:go` and `typecheck:python`. The typecheck step compiles every TypeScript block in every `SKILL.md` and `references/*.md` against the real `dodopayments` types and the `@dodopayments/*` adapter packages, which is what catches wrong field and parameter names before an agent pastes them into your codebase.

## What It Provides

Eight listings clear the 500-install threshold, and they are the ones with real adoption:

| Skill | Installs | Use For |
|---|---|---|
| webhook-integration | 1,122 | Receiving and verifying webhooks with the Standard Webhooks specification, including idempotency on the webhook-id header |
| subscription-integration | 1,044 | Subscription lifecycle, trials, plan changes, proration and on-demand charging |
| checkout-integration | 1,016 | Hosted checkout sessions, static payment links, overlay and inline checkout for one-time and subscription products |
| dodo-best-practices | 1,011 | The orientation skill: Merchant of Record basics, SDK setup, environments, API keys and the canonical checkout-to-webhook flow |
| billing-sdk | 828 | BillingSDK React and shadcn components for pricing tables, billing pages, usage meters and credit balances |
| usage-based-billing | 801 | Metered billing with meters, event ingestion and per-unit pricing |
| license-keys | 694 | License key activation, validation and instance management |
| credit-based-billing | 670 | Credit entitlements, grants, balances, ledger deductions, rollover, expiry and overage |

The remaining 10 indexed listings range from 43 to 217 installs.

The tail is not filler. `testing-and-go-live` covers test mode, test payment methods, webhook testing and the production launch checklist, which is the skill that stops a live key reaching a staging build. `refunds-and-disputes` and `product-catalog-management` both sit at 206. `framework-adapters` carries ten reference files, one per adapter, covering Next.js, Express, Hono, Astro, Remix, SvelteKit, Nuxt, Fastify, TanStack, Bun and Convex. `mobile-checkout` carries four, covering React Native, Flutter, iOS and Android. `dodo-mcp-usage` sits at the bottom on 43 and explains when to use the dodo-knowledge docs MCP rather than the dodopayments-api MCP in Code Mode, plus the test-mode safety rules around each.

Across the 18 skill directories there are 44 markdown files, and the split matters: `webhook-integration` has three references, `checkout-integration` and `credit-based-billing` have two each, and nine skills have none at all. A skill with no references is meant to be read whole and applied directly.

## Why This Matters for Hermes Agents

Payments is the domain where a plausible-sounding agent answer costs the most. A wrong field name in a checkout session is a failed payment; a hand-rolled signature check is a forged webhook that grants access; a live key in a test harness is a real charge. These skills are written against that risk, and the webhook skill leads with the three concepts that go wrong most often: signature verification on the raw body before parsing, idempotency keyed on the `webhook-id` header, and the fact that retries are normal rather than exceptional.

The reference density is the useful part for an agent. `framework-adapters` does not describe Next.js adapters in prose; it carries a file per framework, so a Next.js project gets Next.js code and not a generic Express example that has to be translated. `billing-sdk` carries `pricing-page.md` beside the main skill. That structure matches how a coding agent actually consumes context: whole files it can copy, not summaries it has to re-derive.

The `dodo-best-practices` skill is a good first install even if you never read the other 17. It states the division of labour, names the canonical flow from checkout to webhook, and covers environments and key formats. An agent that has read it stops inventing tax logic, which is the single most expensive misunderstanding in a payments build.

The maintenance story is stronger than most skill repositories. The CI typechecks examples in TypeScript, Go and Python against the real SDKs, so an example that no longer compiles fails the build rather than reaching your agent. Deliberate counter-examples are skipped only when explicitly labelled, so a "wrong way" block cannot silently remove coverage.

## Usage

| You say | What happens |
|---|---|
| "Add a checkout button for our pro plan" | `checkout-integration` builds a hosted checkout session with the right product and return URL, or an overlay if you ask for one |
| "Verify these webhooks properly" | `webhook-integration` sets up Standard Webhooks signature verification on the raw body and idempotent handling keyed on the webhook-id header |
| "We need usage-based billing for API calls" | `usage-based-billing` wires meters and event ingestion, with per-unit pricing |
| "Let users buy credit packs and see their balance" | `credit-based-billing` models entitlements, grants, ledger deductions and low-balance alerts |
| "Build the billing page" | `billing-sdk` supplies BillingSDK React and shadcn components for pricing tables, invoices and cancel or upgrade flows |
| "What do we still need before going live" | `testing-and-go-live` walks test mode, test payment methods, webhook testing and the production checklist |
| "Should the agent use the Dodo MCP here" | `dodo-mcp-usage` picks between the docs MCP and the API MCP and states the test-mode safety rules |

## Verification

Read one skill before installing the set. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/dodopayments/skills/main/dodo-payments/checkout-integration/SKILL.md | head -30
```

It should open with frontmatter naming `checkout-integration` and a description covering hosted Checkout Sessions, static payment links, and overlay or inline checkout, with a pointer to `subscription-integration` for post-checkout lifecycle.

After install, confirm you got the full catalogue and the references that come with it. The clone route puts the repository wherever you cloned it, and the skill directories are one level down:

```bash
ls dodo-payments | wc -l
ls dodo-payments/framework-adapters/references | wc -l
ls ~/.claude/skills | grep -i dodo
```

The first command should print 18, the second 10, and the third should list whichever skills the installer placed for your agent. If you installed a single skill rather than the repository, only the third check applies.

To confirm the examples in a checkout are current, the repository's own validation is the check that matters. It enforces key formats (`dodo_test_` and `dodo_live_`), rejects deprecated SDK calls and hand-rolled HMAC, and keeps each `SKILL.md` within the 500-line Agent Skills limit:

```bash
npm run validate
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| webhook-integration | Pass | Pass | Warn |
| billing-sdk | Pass | Pass | Pass |
| refunds-and-disputes | Pass | Pass | Warn |
| discounts-and-promotions | Pass | Pass | Warn |
| dodo-mcp-usage | Pass | Pass | Warn |

Five of 18 skills sampled, with Trust Hub and Socket clean across all five and one Snyk pass. The warnings cluster on the skills that touch money movement and discounts, which is where a scanner has the most to say and where you should read the detail rather than the letter.

The credential surface is the serious one. These skills assume a Dodo API key in the environment, and the key format itself distinguishes test from live (`dodo_test_` and `dodo_live_`). Keep the two in separate environment files, never in a prompt, and treat any instruction that asks an agent to paste a live key into a request body as a stop condition. The validation script checks key formats precisely because a live key in a test path is the failure that costs real money.

One genuinely good sign: the repository explicitly forbids hand-rolled webhook HMAC in its own validation rules. Signature verification done by hand is the most common way a payments integration becomes forgeable, and a vendor that refuses to ship an example of it is doing the right thing.

The remaining caveat is that these skills are vendor documentation with executable examples. They describe Dodo's API as of the last push, and no skill can verify that your account, plan or region supports a given feature. Confirm entitlement in the dashboard before you promise a billing model to a customer.

## Limitations

- Snapshot data, verified 2026-11-06: 9,036 combined installs across 18 indexed listings; 13 GitHub stars; MIT; last pushed 2026-11-02. Counts drift over time.
- Small community footprint. 13 stars and a first documentation date of 2026-11-06 mean the install counts are the only adoption signal, and they are new.
- Vendor scope. Everything here is Dodo Payments; it is not a general billing design guide, and it assumes Dodo is the merchant of record.
- A live integration still needs a Dodo account, API keys, and a webhook endpoint you control. Nothing in the skills provisions an account, and test mode is not a substitute for a go-live check.
- Four of the five sampled skills carry a Snyk warning, and only five of 18 were sampled at all, so most of the catalogue has no published scanner verdict.
- The examples are typechecked against the SDK at the last push, not against the version you have installed. Pin your SDK and re-run `npm run validate` if you are working inside the repository.

## Related

- [Stripe Link CLI Skills - Agent Payments Setup](/hermes/skills/catalog/stripe-link-cli-setup)
- [Better Auth Skills - Setup Guide](/hermes/skills/catalog/better-auth-skills-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `dodo-best-practices` first and alone. It names the canonical flow, and an agent that knows the flow asks for the right skill next instead of guessing at an endpoint.
- Ask for the framework by name. `framework-adapters` carries a separate reference file per framework, so "Next.js" gets you code and "web framework" gets you a translation exercise.
- Make the agent read `webhook-integration` before it writes a handler. Signature verification on the raw body plus idempotency on `webhook-id` is the pair that separates a working endpoint from one that double-grants access on retry.
- Keep test and live keys in different files and say which one is loaded in every session. The skill formats the key prefix into its examples for exactly this reason.
- Run `testing-and-go-live` as a checklist, not a read. It is the only skill in the set written to be executed step by step against a real account.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
