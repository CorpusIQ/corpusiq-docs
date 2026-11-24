---
title: "WeChat Pay Skills - Chinese Payments Setup"
description: "wechatpay-apiv3/wechatpay-skills - 6.3K combined installs: WeChat Pay integration skills for Chinese payments and product coupons."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wechatpay-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "wechat pay", "payments", "fintech"]
---

# WeChat Pay Skills - Chinese Payments Setup

**Source:** [wechatpay-apiv3/wechatpay-skills](https://www.skills.sh/wechatpay-apiv3/wechatpay-skills) via skills.sh - 6.3K combined installs across 7 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) - 379 stars, MIT, main branch, last pushed Nov 19, 2026; one in-tree skill, wechatpay-payment-integration, with Chinese-language references and sign-and-extract scripts alongside.
**Category:** Payments and Fintech Integration
**Quality Tier:** 🟠 Orange - one Fail cell (wechatpay-payment-integration, Snyk) and seven Warn cells, named in Security.

WeChat Pay ships an official skill collection that teaches a coding agent how to integrate its domestic payment products. The entry skill, wechatpay-payment-integration, is the unified front door for every scenario: product selection, official sample code, in-repo coding, pre-launch quality review and troubleshooting. The README and skill bodies are written in Chinese, and every interface, field, error code and sample answer must trace to the official documentation knowledge base rather than to model memory.

Six further indexed listings cover specific products, product coupons, basic payment, medical insurance payment, Pay Score and deduction service, but only the entry skill has a SKILL.md in the current tree. This collection moves money, so the Security section below leads with the verdicts before any install guidance is applied to a live merchant account.

## Installation

Add the skills with the Agent Skills installer:

```bash
npx skills add wechatpay-apiv3/wechatpay-skills
```

The entry skill loads resources on demand and expects a one-time sync of its documentation bundle:

```bash
python3 <SKILL_DIR>/scripts/wechatpay-resource-sync.py update
```

The skill also references wechatpay-dev-cli for local signing and order-status queries, so the APIv3 private key stays on the local machine. For any live API call, the skill is required to confirm scope and consent with the user first, and it must not retain signing credentials.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| wechatpay-payment-integration | 2,855 | the unified entry: product selection, sample code, coding integration, quality review and troubleshooting |
| wechatpay-product-coupon | 1,145 | product coupon and voucher workflows |
| wechatpay-basic-payment | 883 | JSAPI, Native, APP, H5 and Mini Program payment integration |
| wechatpay-medical-insurance-payment | 495 | medical insurance payment integration |
| wechatpay-payscore | 491 | WeChat Pay Score integration |
| wechatpay-deduction-service | 392 | authorized deduction and recurring payment integration |

The remaining 1 indexed listing is wxpay-product-coupon (1 install), with no counterpart in the current tree.

## Why This Matters for Hermes Agents

Payments integration is the class of task where a wrong assumption costs real money, and WeChat Pay is a large enough surface that most agents get the details wrong from memory: APIv2 versus APIv3, the merchant role, the signature algorithm and the platform versus merchant certificate split. The entry skill is built to force the opposite behaviour, confirm the product and role, retrieve the official document for every field and error code, and only then write code.

The quality-review capability is the highest-value part for a builder. Before launch it walks the payment module the way a financial systems reviewer would, checking signature and verification, key handling, amount precision, idempotency, timeout and retry, and active order lookup, and it reports each item as pass, issue, unverified or not applicable with file and line references. A checklist-driven review with evidence is exactly what a pre-launch audit needs.

The operational discipline also matters: the skill confirms scope and consent before calling a live interface and keeps the signing private key local, using wechatpay-dev-cli for verification. The tradeoff is that this is a credential-bearing, documentation-heavy suite whose non-entry listings carry no in-tree files, so the entry skill is the one to audit first.

## Usage

| You say | What happens |
|---|---|
| Which product should my mini program use | Uses wechatpay-payment-integration for product selection with reasons |
| Give me JSAPI order plus callback signature code | Uses wechatpay-payment-integration for official sample code |
| Add JSAPI payment to this Spring Boot project | Uses wechatpay-payment-integration to confirm role and version, then code |
| Review my payment module before launch | Uses wechatpay-payment-integration for a checklist-based quality review |
| My callback keeps returning SIGN_ERROR | Uses wechatpay-payment-integration to trace the error code and cause |
| Did this order actually pay | Uses wechatpay-payment-integration with wechatpay-dev-cli to query status |
| Explain platform versus API certificate | Uses wechatpay-payment-integration to answer from the knowledge base |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/wechatpay-apiv3/wechatpay-skills/main/README.md | head -40
```

Confirm the entry skill body is present before integration work:

```bash
curl -sL https://raw.githubusercontent.com/wechatpay-apiv3/wechatpay-skills/main/wechatpay-payment-integration/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use. This publisher moves money, so review each verdict page before wiring any skill into a live merchant account:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wechatpay-payment-integration | Warn | Pass | Fail |
| wechatpay-product-coupon | Pass | Pass | Warn |
| wechatpay-basic-payment | Pass | Pass | Warn |
| wechatpay-medical-insurance-payment | Pass | Pass | Warn |
| wechatpay-payscore | Pass | Pass | Warn |
| wechatpay-deduction-service | Pass | Pass | Warn |
| wxpay-product-coupon | Pass | None | Warn |

The single Fail cell sits on wechatpay-payment-integration (Snyk). The seven Warn cells sit on wechatpay-payment-integration (Gen Agent Trust Hub) and on the Snyk column for wechatpay-product-coupon, wechatpay-basic-payment, wechatpay-medical-insurance-payment, wechatpay-payscore, wechatpay-deduction-service and wxpay-product-coupon. wxpay-product-coupon also carries no Socket verdict (None). Do not treat these as safe for production without reading the linked security pages.

## Limitations

- Snapshot data, verified Nov 23, 2026: 6,262 combined installs across 7 indexed listings; 379 GitHub stars; MIT licence; last pushed Nov 19, 2026. Counts drift over time.
- Only wechatpay-payment-integration has a SKILL.md in the current tree; the other six listings carry install counts and verdict cells but no directory in this repo.
- The README and skill bodies are in Chinese, and the entry skill's routing and reference documents assume Chinese-language intent.
- Answers are constrained to the official knowledge base, and questions outside it are answered as out of scope rather than from model memory.
- Live interface calls require user consent, and the skill must not retain signing credentials, but the extract_and_sign scripts in the tree handle keys locally and need operator review.
- The one Fail and seven Warn verdict cells across a money-moving publisher make independent security review mandatory before any production use.

## Related

- [Dodo Payments Skills - Payments API Setup](/hermes/skills/catalog/dodopayments-skills-setup)
- [Stripe Link CLI Skills](/hermes/skills/catalog/stripe-link-cli-setup)
- [Stripe Skills](/hermes/skills/catalog/stripe)
- [Skills Catalog](/hermes/skills/catalog)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read the entry skill's precondition section first: it requires domain allowlisting and a resource sync before any question is answered.
- Treat APIv2 versus APIv3 as the first question to settle, since the signature, certificate and endpoint paths differ entirely.
- Keep the signing private key local and use wechatpay-dev-cli for order queries instead of pasting keys into the agent.
- Run the quality-review flow before every launch, not after, and keep its pass, issue, unverified and not applicable output as the audit trail.
- For the six non-entry listings, verify their own pages on skills.sh and the product documentation before relying on a name-only install.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
