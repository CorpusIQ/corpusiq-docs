---
title: "Pandus MCP - WCAG 2.2 Accessibility for Commerce Sites"
description: "Finds what is actually wrong on a page for accessibility, why it matters and how to fix it on Shopify, WooCommerce or PrestaShop."
category: Compliance / Web Accessibility
stars: ★★ (3 keyless tools, 10 documented, OAuth site checks)
added: 2026-10-28
source: "live probe of https://pandus.online/mcp returning HTTP 200 keyless on initialize with a tools/list of 3 tools, plus the mcpservers.org listing at mcpservers.org/servers/pandus-online-en-accessibility-mcp-server documenting 10 tools, 2 prompts and the OAuth site audit path"
relevance: ★★
tags: [accessibility, wcag, axe-core, eaa, ada, shopify, woocommerce, prestashop, compliance, mcp]
last_updated: "2026-10-28"
---

# Pandus MCP

**Accessibility fails quietly: the customer who cannot complete checkout does not complain, they leave, and the law that covers them does not care that the site looked fine.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://pandus.online/mcp
Auth:        none for the rule library, OAuth or token for sites
Tools:       3 keyless, 10 documented at the vendor
Prompts:     2 (fix the problems, write an owner update)
Covers:      WCAG 2.2 A and AA, axe-core rules
Platforms:   Shopify, WooCommerce, PrestaShop, Shoptet
```

## Why This Matters for Operators

The European Accessibility Act now puts an accessibility obligation on consumer-facing commerce in the EU, the ADA has done the same in the United States for years, and most store owners have no idea which of their pages fail. The failure mode is not dramatic. It is a contrast ratio, an unlabelled form field, an image with no alternative text, a modal that traps a keyboard.

The useful part of this server is not that it finds problems. It is that each finding is tied to the WCAG criterion it breaks and to a fix written for the platform the store actually runs on, so the agent can find the template that renders the problem rather than describing it.

## What It Returns, Verified

The endpoint is live and open on its public half: a bare `POST initialize` on `https://pandus.online/mcp` returned **HTTP 200**, and `tools/list` returned **3 tools** keyless: `search_rules`, `explain_rule` and `explain_wcag_criterion`.

The vendor documents **10 tools** in total, with seven needing a sign-in or token:

- `search_rules` and `explain_rule` and `explain_wcag_criterion` need nothing: rule cards by words, axe-core rule id or WCAG criterion, with fixes in code and on Shopify, WooCommerce, PrestaShop and Shoptet
- `list_sites`, `what_to_fix`, `get_problem`, `get_report`, `compare_checks` and `check_status` need sign-in or a token
- `start_check` starts a new check within the plan, allowed at sign-in or with a write-scoped token
- `compare_checks` reports what was fixed, what is new and what is still open between the two latest checks

Two prompts ship with it: fix the most important problems in the codebase, and write an update for the site owner in their own language.

## Limits Worth Recording

The vendor states plainly that results come from an automated check, not a full audit, and are not legal advice, which is the correct way to read any axe-core-derived result: automated tooling catches perhaps a third of real WCAG failures and misses the ones that need a person. The keyless surface is the rule library, so measuring an actual site requires signing in from the assistant or holding a token. Cross-reference the catalogue's existing accessibility entries before treating any single scanner as coverage.

## FAQ

### Do I need an account to use it?
No. `search_rules`, `explain_rule` and `explain_wcag_criterion` answer without one. Checking your own sites needs a sign-in or a token.

### Which platforms does the fix guidance cover?
Shopify, WooCommerce, PrestaShop and Shoptet are named for platform-specific fixes, and each finding also carries the WCAG clause and a code-level fix.

### Is an automated check enough for compliance?
No, and the vendor says so: it is an automated check, not a full audit, and not legal advice. Use it to find and fix the mechanical failures, then test the flows by hand.

### How do I know a fix worked?
Run a new check with `start_check` and read `compare_checks`, which separates what was fixed, what is new and what is still open between the two latest checks.
