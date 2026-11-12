---
title: "Vetto MCP - Fake Signup Checks Before the Account"
description: "Keyless signup-email checks driven live: a typo rescued, a disposable blocked, a Gmail alias proven the same inbox, and the role rule"
category: "Growth and Revenue Operations"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the mcpservers.org listing carrying a lastmod inside the 2026-11-12 window, the mcp.so feed card stamped 2026-11-12 08:40Z, the submission queue entry #7190, the vendor site and its pricing block read the same day, and a live session on this host: initialize, tools/list and six tools/call requests against https://usevetto.com/mcp"
relevance: ★★★
tags: [signup, fraud, email-validation, trial-abuse, growth, saas, keyless, mcp, remote]
last_updated: "2026-11-12"
---

# Vetto MCP

**Every signup form accepts an address it cannot deliver to, and the bill arrives a month later as an unpaid trial.** The address is the cheapest thing a person types and the most expensive thing to get wrong: a typo locks out a real buyer, a throwaway domain fills the trials, and one Gmail account becomes seven registrations because dots and plus tags are free. Vetto turns that judgement into four read-only tools on a public endpoint with no account and no key.

```text
Server type:  remote Streamable HTTP, keyless
Endpoint:     https://usevetto.com/mcp
Server:       vetto 1.0.0 (serverInfo), title "Vetto: fake signup checks", protocol 2025-03-26
Capabilities: tools only (no resources, no prompts)
Tools:        4 measured, all annotated readOnlyHint: true
Registry:     no record found under this name (the search returns si.vettoz/vettoz, a different product)
Probe:        initialize, tools/list and six tools/call requests in one session
```

## What the server answered

`initialize` returned **200** with no credential and an instruction block that states the product's four questions in its own words: disposable and throwaway domains, domains that cannot receive mail, typos such as `gmial.com`, privacy relays (allowed, because they reach a real inbox), and Gmail aliases of the same inbox. `tools/list` returned four:

```text
check_email     one address, judged the way a signup form judges it
check_domains   up to 50 domains at once, for the domains behind recent signups
same_inbox      two addresses compared after Gmail normalisation
how_to_block    setup steps for a given stack
```

## Driven: a typo, a throwaway and an alias

Six calls were made, and the first two show why the verdict is more useful than a boolean.

`check_email` on `jdoe@gmail.co` returned **BLOCK**, `reasons: ["typo", "dead"]`, `suggestion: "jdoe@gmail.com"`, `domainStatus: "null_mx"` and an empty `mx` array. The suggestion is the part that saves the customer: an assistant can answer *did you mean jdoe@gmail.com* inside the signup conversation rather than showing a validation error.

`check_email` on `billing@mailinator.com` returned **BLOCK** with `reasons: ["role", "disposable"]` and `domainStatus: "skipped"`. `check_email` on `team+1@googlemail.com` returned **ALLOW** with `reasons: ["freemail", "role"]`.

Read together, those two answers define the rule precisely: **a role address alone does not block**. A role address on a freemail domain is allowed with the tag recorded; the same role shape on a disposable domain is blocked because the disposable signal carries the verdict. A tool that blocked on `role` as a flag would have rejected a real team inbox, and one that ignored it would have let the throwaway through with no note. The response keeps both signals and ranks them.

`same_inbox` on `john.doe+promo@gmail.com` and `johndoe@googlemail.com` returned `same: true` with both normalising to `johndoe@gmail.com`; the control pair `john@gmail.com` and `jane@gmail.com` returned `same: false`. That is the trial-abuser check stated as arithmetic rather than as a claim.

`check_domains` on four domains returned a summary of `checked: 4, flagged: 2`: `gmail.com` ok, `mailinator.com` disposable, `gmial.com` disposable, `acme-supply.com` ok. Note that `gmial.com` is flagged as a disposable domain, not as a typo, and the vendor's own page makes the distinction worth knowing: `gmai.com` carries a live mail server, so an MX-only check passes it, while `gmial.com` resolves to something the vendor already classifies. Two different lookalike domains, two different signals.

`how_to_block` on `next.js` returned a server-side recipe rather than a marketing page: POST to `https://usevetto.com/v1/audit` with the domain list, reject when `results[domain].disposable` is true or the status is `nxdomain`, `null_mx` or `no_mail`, and **fail open on timeout**. That last clause is the operational decision most form guards get wrong in the other direction, and it is stated in the tool output.

## What the vendor states, and what it does not

From the vendor site read on 2026-11-12: one script tag (`/v.js` with a site key) on the signup form, free on one site with no card, free for Next.js, Supabase, Webflow, Framer and WordPress, failing open after **800 ms**, and eight signals folded into one verdict per signup. The headline claim is that Stripe saw **6.2x** more abusive free trials between November 2025 and February 2026, sourced to Stripe, alongside a **~10 percent** figure for registrants who typed their email wrong, sourced to Discourse Meta. There is a Founding offer of Pro for life at **69 USD** once for the first 100 buyers until November 27.

Two honest limits. The server's own instruction block says nothing sent to these tools is stored; that is the vendor's statement about its own endpoint, quoted as such and not a claim about an account you connect. And no official MCP registry record was found under this product name, so the endpoint evidence above is the whole of the technical record: keyless, four tools, six driven calls.

## Where it sits

This is the first signup-integrity entry in this catalog. [Vibe Shield MCP](/hermes/mcp/servers/external/vibe-shield-mcp/) scans the code that accepts the form; this judges the value typed into it. [Emailchaser MCP](/hermes/mcp/servers/external/emailchaser-mcp/) owns the outbound side, where a bad address costs a send rather than a trial.

### Does Vetto need an API key to answer a check?

No. `initialize` and `tools/list` answered **200** with no credential, and all six `tools/call` requests returned verdicts. Whether an account changes rate limits or coverage is not published on the endpoint and was not measured here.

### Can it tell two Gmail addresses apart from the same person?

Not apart - together. `same_inbox` normalises dots, `+tags` and `googlemail.com`, so `john.doe+promo@gmail.com` and `johndoe@googlemail.com` are reported as one inbox, which is how a seventh trial from the same person is detected.

### What happens when the check times out?

The vendor's own recipe tells the caller to fail open, so a slow check lets a real customer through rather than blocking a signup. That is a product decision to verify against your own form before switching the script on.
