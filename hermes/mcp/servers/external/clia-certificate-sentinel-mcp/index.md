---
title: "CLIA Sentinel MCP - US Lab Certificate Expiry Dates"
description: "A US clinical laboratory's CLIA certificate expiry, the 9-to-12-month renewal window and the days left, read from the quarterly CMS file."
category: "Compliance"
stars: n/a (vendor-hosted)
added: 2026-11-22
source: "chatmcp/mcpso submission #7835 filed 2026-11-22T16:55:24Z; keyless initialize and tools/list, clia_certificate_example driven, clia_certificate_lookup returned an x402 payment challenge, all on 2026-11-22"
relevance: ★★★★
tags: [compliance, healthcare, licensing, deadlines, cms, x402, remote-mcp]
last_updated: "2026-11-22"
---

# CLIA Certificate Renewal Sentinel MCP

**Remote MCP server (Streamable HTTP)** - two tools over the quarterly CMS Provider of Services File for clinical laboratories. It answers whether a US laboratory's CLIA certificate is close to expiry, when the regulatory renewal window opens, and how many days are left, without returning a laboratory name or address.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://clia.amacunia.fr/mcp
Server:      CLIA Certificate Renewal Sentinel 0.1.0, protocol 2025-06-18
Tools:       2 (one free sample, one paid per lookup)
Payment:     x402, 0.01 USDC on Base, plus a free-trial allowance
Citation:    42 U.S.C. 263a, 42 CFR part 493
```

## Why This Matters for Operators

Every laboratory that examines human specimens in the United States needs a CLIA certificate in effect, and every certificate expires. A certificate that lapses is not paperwork: the statute prohibits examining specimens without one, and the enforcement ladder runs from civil money penalties to revocation with a two-year ownership ban.

This server answers the date question in the form an operator needs it: not "expires" but *expires on this date, the renewal window opened here and closes there, and you are inside it*. That is an expiry watch built on a public quarterly file rather than on a vendor's memory of a customer.

## Measured Behaviour

Both tools were called on 2026-11-22. The free sample returned a complete answer; the paid tool returned a payment challenge instead of data, which is itself the measurement.

### The free sample is a real answer

`clia_certificate_example` returned one laboratory record in full. Quoted:

```json
{
  "clia_number": "01D0726657",
  "found": true,
  "state": "in_force_on_file",
  "state_code": "AL",
  "certificate_type": "waiver",
  "termination_reason": "ACTIVE PROVIDER",
  "certificate_effective_date": "2025-10-20",
  "certificate_expiration_date": "2027-10-19",
  "days_to_expiration": 332,
  "renewal_rule": { "kind": "window", "citation": "42 CFR 493.37(f)(1)" },
  "regulatory_renewal_window": {
    "opens": "2026-10-19", "closes": "2027-01-19",
    "status": "open", "days_until_close": 59
  },
  "cms_billing": {
    "invoice_expected_around": "2027-04-19",
    "certificate_expected_around": "2027-09-19"
  },
  "conflicts": ["renewal_timing", "waiver_alternative_sanctions"],
  "as_of": "2026-11-21",
  "time_zone": "America/Chicago"
}
```

Three things make that record useful. The **window is open right now** (2026-10-19 to 2027-01-19, 59 days to close), so the answer is actionable rather than academic. The **332 days** is dated to the server's `as_of` of 2026-11-21 and reproduces: 2026-11-21 to 2027-10-19. And the record **declares its own conflicts**: `renewal_timing` plus `waiver_alternative_sanctions`, which flags that a waiver certificate has an alternative enforcement path rather than the standard renewal only.

### The penalty block refuses to invent a number

The same response carries a `penalties` object that states the citations and then explicitly declines to price them:

> References only: no amount is returned, because the civil money penalty ranges are adjusted every year.

with citations to 42 U.S.C. 263a(b) for the certificate requirement, 263a(h) for intermediate sanctions, and 263a(i) for suspension, revocation and limitation, including the two-year ownership ban that follows a revocation. An agent quoting a dollar penalty here would be inventing it; the server declines to, and says why.

### The paid tool answers with a payment challenge

`clia_certificate_lookup` returned an x402 challenge in band rather than an error:

```json
{ "x402Version": 2, "error": "Payment Required",
  "accepts": [{ "scheme": "exact", "network": "eip155:8453",
                "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
                "amount": "10000", "payTo": "0xa1caaece13804f600df4affd88455395422d5eac",
                "maxTimeoutSeconds": 300 }]}
```

`amount` 10000 at six decimals is **0.01 USDC**, on Base. The response also documents the alternative in plain text: call the same tool again with `free_trial: true` to get the answer without paying, **3 calls per day per caller** shared with the web route, while the service's daily allowance of 50 lasts.

That free-trial line is the difference between a walled tool and a metered one, and it is stated to the client inside the refusal.

## What It Cannot Do

- It does not name laboratories or return addresses. The response says so: no laboratory names, no addresses.
- It is not affiliated with or endorsed by CMS, and the server says that in its own instructions.
- Coverage is only as fresh as the quarterly file. The record carries `as_of` and a `time_zone` of America/Chicago, so a stale file is visible in the payload rather than assumed current.
- The paid path needs a wallet with USDC on Base. Without one, use the free sample or the three-a-day trial.

## Frequently Asked Questions

### Can an agent check a lab's CLIA certificate without paying?

Yes, within limits. The free sample tool returns one complete record at no cost, and the paid lookup accepts `free_trial: true` for three calls a day per caller. The 0.01 USDC charge applies beyond that allowance while the daily service allowance lasts.

### What exactly is the 9-to-12-month renewal window?

It is the period the regulation defines for renewal against the certificate's expiry date. For the record measured here the certificate expires 2027-10-19 and the window runs 2026-10-19 to 2027-01-19, with the status field reporting it as open and 59 days left to close.

### Does it return the penalty amount for operating without a certificate?

No, deliberately. It returns the statutory citations and explains that the civil money penalty ranges are adjusted every year, so no fixed amount is published.

## See Also

- [Compliance and filing data sources in the external catalogue](/hermes/mcp/servers/external/)
