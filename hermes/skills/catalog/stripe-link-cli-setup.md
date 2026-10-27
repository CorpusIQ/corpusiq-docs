---
title: "Stripe Link CLI Skills - Agent Payments Setup"
description: "Stripe Link CLI: 49.0K combined installs. Four skills for agent payments, wallet credentials, spending insights and identity claims."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/stripe-link-cli-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "payments", "stripe", "agent commerce"]
---

# Stripe Link CLI Skills - Setup Guide

**Source:** [stripe/link-cli](https://www.skills.sh/stripe/link-cli) via skills.sh - 49.0K combined installs across 4 indexed listings; new to this catalog in the Oct 23, 2026 sweep

**GitHub:** [stripe/link-cli](https://github.com/stripe/link-cli) - 869 stars, MIT license, last pushed 2026-10-23, branch main, three skills under `skills/` plus two plugin skills under `plugins/cursor-link/skills/`

**Category:** Commerce / Agent Payments

**Quality Tier:** 🟡 Beta - official Stripe repository under MIT with same-day activity and clean identity and financial skills, but Socket and Snyk both warn on the payment credential skill because it gives an agent the ability to spend

Link CLI is Stripe's agent payments surface. An agent asks for a payment credential, the user approves the spend in the Link app, and the agent receives a credential that works at checkout without the user's real card number ever reaching the agent or the merchant. The repository ships three agent skills for that flow plus a fourth indexed listing for the CLI itself.

The repository is current, official and small in surface area: three skill directories, a CLI, and SDKs for TypeScript, Python and Go. The reason this guide says Beta rather than Production is the one no vendor can design away. A skill whose job is to spend money takes warnings from auditors that read instruction files for exactly that capability.

## Installation

```bash
# The CLI
npm i -g @stripe/link-cli

# Or run it without installing
npx @stripe/link-cli

# The skills
npx skills add stripe/link-cli
```

For Hermes, install the three skills from the repo's `skills/` directory:

```bash
hermes skills install stripe/link-cli/create-payment-credential --yes
hermes skills install stripe/link-cli/financial-insights --yes
hermes skills install stripe/link-cli/use-link-identity --yes
```

Sign in once, and name the agent so the approval screen is readable:

```bash
link-cli auth login --client-name "Hermes Agent"
```

With `--client-name`, the Link app shows the connecting agent on the approval screen instead of the generic CLI name. `--interval 5 --timeout 300` polls for the approval inside the same call, which is what an agent wants when it cannot hold a session open.

The CLI ships a local MCP server. It binds to `127.0.0.1` by default and answers `POST /mcp`, with skill discovery at `/.well-known/skills/index.json` and `/.well-known/skills/{skill-name}/SKILL.md`. Do not raise `--host` unless the network is trusted and isolated: anyone who reaches the port can use the CLI's authenticated Link session.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| create-payment-credential | 19,627 | Gets payment credentials from a Link wallet for one-time purchases and recurring payments, and walks an agent through checkout on a merchant site. Covers the three credential types: a virtual card (PAN) for a standard web form, a Link Pay Token for Stripe surfaces that accept WebMCP, and a Shared Payment Token for sellers on Machine Payment Protocols. Also covers connecting a Link account. |
| financial-insights | 18,587 | Reads Link financial data so an agent can answer questions about spending: transactions, balances and connected wallet sources, with pagination and amount interpretation handled. Covers "check my balance", "how much did I spend", "show my transactions" and summaries of recent purchases. |
| use-link-identity | 7,938 | Link identity commands for services that ask for a Link Agent Attestation Token or signed user claims such as a verified email. Covers acquiring and managing attestations and presenting selected claims to a verifier through an HTTP client or browser automation, rather than handing over the whole profile. |
| link-cli | 2,895 | The CLI surface behind the three skills. This listing has no matching directory in the repository's `skills/` tree; its written form is `docs/link-cli-skill.md`, and the installable variants under `plugins/cursor-link/skills/` are check-link-wallet and complete-link-purchase. |

All 4 indexed listings clear the 2,000-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Agent commerce has been blocked on one question: how does an agent pay without holding a card number. Handing a card to an agent means the credential sits in a config file or an environment variable, which is the same exposure as pasting it into a chat. Link inverts that. The agent requests a credential for a specific spend, the human approves it in an app they already trust, and the agent receives something that is scoped to that purchase.

That shape is what makes the difference between an agent that can research a purchase and an agent that can complete one. For a Hermes workflow the useful pattern is a task that ends in a transaction: buy the part, renew the subscription, pay the invoice. Each of those needs a payment step, an approval, and a record. Link supplies all three, and the skills teach the agent which credential type each merchant surface accepts.

The identity skill is the piece most teams overlook. Services increasingly ask an agent to prove a claim about the user, an email or an account, before acting. Presenting a signed attestation of one claim is a narrower grant than logging in as the user, and it is the difference between an agent a service will accept and one it will block.

## Usage

| You say | What happens |
|---|---|
| "Buy the enclosure I was looking at, up to 40 dollars" | The agent requests a credential with a spend limit, you approve it in the Link app, and the agent completes checkout on the merchant site. |
| "How much did I spend on tools this month?" | financial-insights pages the transaction list, groups it and sums it, rather than estimating from memory. |
| "Which card is behind my Link wallet?" | The agent reports connected sources and balances, without ever printing a full card number. |
| "Sign me up for this service, it wants an email verification" | use-link-identity acquires an attestation for the email claim and presents the single claim to the verifier. |
| "Set this up as a monthly subscription" | The agent uses the recurring path, which the credential skill documents separately from one-time checkout. |
| "Why did the purchase stop at a challenge?" | The skill covers step-ups and 402 challenges, so the agent returns to you for the approval instead of retrying blind. |

## Verification

Confirm the three skill paths exist on main, then read the credential rules before granting anything:

```bash
for s in create-payment-credential financial-insights use-link-identity; do
  curl -sL -o /dev/null -w "%{http_code} $s\n" \
    "https://raw.githubusercontent.com/stripe/link-cli/main/skills/$s/SKILL.md"
done
```

The credential skill is the one to read in full:

- https://raw.githubusercontent.com/stripe/link-cli/main/skills/create-payment-credential/SKILL.md
- https://raw.githubusercontent.com/stripe/link-cli/main/skills/financial-insights/SKILL.md

Two local checks after install: `link-cli --version` should report the CLI the skills expect, and `link-cli --help` should list the commands the skill names. Identity commands need a Link Agent Wallet version that supports them, and they are deliberately excluded from the MCP surface, so an agent that only has the MCP server connected will not see them.

## Security

skills.sh verdicts for sampled skills (verified October 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| create-payment-credential | Pass | Warn | Warn |
| financial-insights | Pass | Pass | Warn |
| use-link-identity | Pass | Pass | Pass |
| link-cli | Pass | Warn | Warn |

The warnings are the honest reading of what these skills do. Snyk raises W009, direct money access, on the credential skill, and W011, third-party content exposure, because the workflow browses merchant pages, product catalogues and API responses the skill does not control. Socket warns on the same skill for the same class of capability. None of that is a defect in the files; it is a description of an agent that can spend.

Treat the Link session as the most sensitive credential on the machine. The local MCP server lets anyone who can reach its port use the authenticated session, which is why it binds to loopback. Keep spend limits on every request, approve each purchase rather than pre-authorizing a category, and review the transaction list before pointing an agent at a new merchant.

## Limitations

- Snapshot data, verified October 23, 2026: 49,047 combined installs across 4 indexed listings; 869 GitHub stars; license MIT; last pushed 2026-10-23. Counts drift over time.
- Link CLI is available to US and Canadian Link accounts only. Everything else in this guide depends on that prerequisite.
- 869 stars is a young repository. It is official Stripe code with same-day pushes, but treat version drift as normal: the skills carry a version field, and the CLI is at 0.28.0 in this snapshot.
- The `link-cli` listing has no counterpart directory in `skills/`. Its documented form is `docs/link-cli-skill.md`, so an install-by-name of `link-cli` may not resolve.
- Identity commands require a Link Agent Wallet version that supports attestations, are absent from MCP, and are newer than the payment path. Verify with `link-cli --help` before designing a flow around them.
- The skills assume a human can approve a spend in the Link app. Fully unattended purchasing is not what this repository documents.

## Related

- [stripe Skills](/hermes/skills/catalog/stripe)
- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)

## Pro Tips

- Start with `link-cli auth login --client-name "Hermes Agent"`. The name on the approval screen is the only thing that tells you which agent is spending.
- Set a spend limit on the request, not in the prompt. A limit the agent states in prose is a preference; a limit in the request is enforced.
- Use `financial-insights` before and after a purchase run. It is the cheapest way to catch a duplicate charge from a retried step-up.
- Read the three credential types before choosing: a virtual card works anywhere, a Link Pay Token needs a Stripe surface with WebMCP, and a Shared Payment Token needs a seller on Machine Payment Protocols.
- Keep identity attestations narrow. Request the single claim the verifier asked for rather than a bundle.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
