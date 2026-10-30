---
title: Store Canary MCP - A WooCommerce Check From Outside
description: "Keyless remote MCP that audits a WooCommerce store from the outside: HTTPS, cart, checkout, payment markers, speed, products and policies in one call."
category: Commerce & Marketplace Operations
stars: n/a (new listing)
added: 2026-10-30
source: "mcpso issue #6440, io.github.erikras/store-canary"
relevance: ★★★
tags: [woocommerce, ecommerce, store-audit, checkout, https, seo, policy, remote-mcp, keyless]
last_updated: "2026-10-30"
---

# Store Canary MCP

**Most store checks happen from inside the admin, which is exactly where you cannot see what a customer sees. This one runs from the outside, unauthenticated, and never touches the store.**

Store Canary publishes an MCP endpoint at `https://mcp.storecanary.app/mcp` over Streamable HTTP. A bare `initialize` answers **HTTP 200** with `serverInfo` `store-canary` at version `1.0.0`, advertising `tools` and `prompts`.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.storecanary.app/mcp
Auth:        none (public, read-only)
Tools:       8
Prompts:     3
```

## What it does

`check_store` is the whole-store pass. Seven focused tools each look at one area: `check_ssl`, `check_exposure`, `check_seo_basics`, `check_speed`, `check_products`, `check_policies`, and `explain_finding` to turn any finding code into plain language with a fix.

The vendor's own instruction string sets the boundary: every tool runs once and sends **GET requests only**, it never logs in, adds to cart or submits forms, and nothing is monitored or saved. That sentence is what makes the surface safe to point at someone else's store during a sales conversation.

## Read from a live call, not a card

A keyless `check_store` on `https://example.com` executed and returned:

```
Store Canary checked example.com: FAIL (4 fail, 1 warn, 2 pass).
PASS Store is reachable: The homepage loaded (HTTP 200) in 5 ms to first byte.
WARN HTTPS: The certificate is accepted, but http:// serves the site (HTTP 200)
            instead of redirecting to https://.
PASS Redirect chain: No redirects on the https:// homepage.
FAIL WooCommerce detected: We found no WooCommerce markers and no Store API at
     /wp-json/wc/store/v1; this may not be a WooCommerce store.
FAIL Cart page: Cart returned 404 Not Found.
FAIL Checkout page: Checkout returned 404 Not Found.
FAIL Payment methods on checkout: We couldn't look for payment methods because
     checkout didn't load properly.
```

Two things in that output matter more than the verdict. First, the finding identifiers are stable (`reachable`, `https`, `redirects`, `woocommerce`, `cart`, `checkout`, `payment`), which means an agent can diff two audits of the same store over time instead of re-reading prose. Second, the checkout and payment findings are **causal**: payment markers were not checked because checkout did not load, and the tool says so rather than reporting a payment failure it never observed.

The typed output schema carries `status` (`checked`, `invalid_url`, `rate_limited`), `overall` (`pass`, `warn`, `fail`), a `summary`, the `findings` array and a `reportUrl`. The report is encoded in the link itself, so a shareable read-only page exists without anything being stored server-side.

## Prompts that ship with it

The three prompts are operational rather than decorative: `black_friday_audit` takes a store URL and runs all seven checks into a prioritised pre-sale fix list, `checkout_check` asks whether cart, checkout and payment methods load and explains anything that does not, and `explain_finding` takes a finding code.

## The gap it names itself

The tool output includes the limit in the vendor's words: an outside-in spot check cannot see orders or background jobs, which is why the vendor points to a WordPress.org plugin for stuck orders and failed scheduled actions, and to a paid tier for failed payments and stockouts. An agent that quotes this server as a plain "store is healthy" answer would be overstating it. The correct read is a checkout-path and exposure verdict from the customer's side, which is precisely the half an admin dashboard cannot give.

## Why it belongs in this catalogue

The catalogued WordPress and WooCommerce entries are management surfaces, and the security scanners here look at exposure or leaked keys. The nearest neighbour is the Shopify speed check, which is one platform and one dimension; this is a store-level pass across seven dimensions on a different platform, so it is a new slice rather than a duplicate. It treats cart, checkout and payment visibility as the things worth testing, and it runs before a peak trading window rather than after an incident.

## FAQ

### Does it need a key or an account?
No. The endpoint is public and read-only, and both `initialize` and `check_store` answered without a credential in this pass.

### Is it WooCommerce only?
Yes. Detection is WooCommerce markers plus the Store API at `/wp-json/wc/store/v1`, and the checks that follow assume a WooCommerce cart and checkout. A non-WooCommerce site returns a `woocommerce` fail rather than a general audit.

### Does it change anything on the store?
No. The server states GET requests only, no login and no form submission, and nothing is monitored or saved.

### What does the paid tier add?
Continuous monitoring rather than a single pass: failed payments, stockouts and an email digest, with a 30-day trial and no card required per the vendor's own links in the tool output.

## See Also

- [Shopify Speed Check MCP - Store Speed and Plan Fees](/hermes/mcp/servers/external/shopify-speed-check-mcp/) - the same outside-in instinct on Shopify, for speed and plan cost
- [ShopSynch MCP - E-Commerce Operations for AI Agents](/hermes/mcp/servers/external/shopsynch-mcp/) - operations rather than audit
- [Hustle Got Real MCP - Dropshipping in Plain Chat](/hermes/mcp/servers/external/hustle-got-real-mcp/) - the inside-out control loop this check pairs with
