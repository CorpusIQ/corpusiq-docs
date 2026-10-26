---
title: "how.is MCP - Domain Trust and Email Auth Checks"
description: "Seventeen domain and site checks over MCP: trust verdict, DNS, WHOIS, TLS, DNSSEC, SPF and DMARC, blocklists, screenshots and page-change diffs."
category: Security / Domain Intelligence
stars: n/a (pay per call, free samples, keyless start)
added: 2026-10-25
source: "mcp.so feed card 2026-10-25T21:25:41Z + live keyless MCP session on how.is + HTTP 402 x402 payment terms + tool schemas from tools/list"
relevance: ★★★
tags: [domain-trust, dns, whois, tls, dnssec, spf, dkim, dmarc, email-deliverability, blocklists, page-monitoring, x402, security]
last_updated: "2026-10-25"
---

# how.is MCP

**The check an operator runs before the money leaves.** A domain is the one bill that never gets questioned: a new supplier, a payment portal, a recruiting agency, a reseller. Age, blocklist listings, certificate validity and email authentication answer in seconds what a phone call answers in a day.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://how.is/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        none to start, x402 v2 payment header or a Bearer key for paid calls
Tools:       17
Built by:    how.is (domain and website intelligence)
Registry:    not listed in the official MCP registry
```

## Why This Matters for Operators

Two questions sit behind most small business losses: is this counterparty real, and will my mail reach the inbox.

The first is a domain question. A supplier registered eleven days ago, on a network with abuse listings, behind a certificate that does not validate, is a different risk than a company that has held the same domain since 2014. An assistant that can state the age, the listings and the certificate state turns a gut feel into a record.

The second is also a domain question. SPF, DKIM and DMARC decide whether a quote, an invoice or an outreach email lands in an inbox or in spam. Most operators find out after a campaign has already been sent.

## What It Actually Does

The endpoint was driven in this sweep without an account. `tools/list` returned seventeen tools in 15.9 KB of schema, against protocol 2025-06-18.

| Tool | What it returns | Price |
|---|---|---|
| `domain_profile` | Bundle: DNS, WHOIS, TLS, DNSSEC, email auth, security score, blocklists, plus IP intelligence for the A record | $0.025 |
| `domain_trust` | Risk score 0-100, verdict (`likely_safe`, `caution`, `high_risk`, `inconclusive`), plain-English reasons | $0.020 |
| `domain_dns` | A, AAAA, MX, NS, TXT records with resolve timing | $0.005 |
| `domain_whois` | Registrar, creation and expiry dates, nameservers, status codes | $0.005 |
| `domain_age` | Registration date, age in days and years, and a `newly_registered` flag for the last 30 days | $0.005 |
| `domain_available` | Whether a name is free, with first-year and renewal price and the RDAP or DNS source | $0.005 |
| `domain_tls` | Validity, issuer, protocol, cipher, days until expiry, self-signed flag | $0.005 |
| `domain_dnssec` | Signed state, validation status, chain of trust, DS and DNSKEY records | $0.005 |
| `domain_email_auth` | SPF, DKIM and DMARC records with an overall score and recommendations | $0.005 |
| `domain_security_score` | Letter grade and point score with the scored items behind it | $0.005 |
| `domain_blacklist` | Whether the addresses behind a domain appear on spam and abuse blocklists | $0.005 |
| `ip_lookup` | ASN, company, geolocation, privacy flags, abuse contact | $0.005 |
| `site_status` | Live HTTP status, latency, resolve time, resolved IP, TTL, nameservers, certificate days left | $0.005 |
| `site_screenshot` | 1280-wide JPEG of any public URL, viewport or full page capped at 6000 px | $0.020 |
| `page_watch` | Whether a page changed since the last call, with a text diff at a 2 percent threshold | $0.005 |
| `bot_observatory` | Every ASN, named crawler, JA4 TLS fingerprint and firewall rule seen in the last 7 days | $0.050 |
| `add_credit` | Free. Returns a link the user opens to put card credit on the connection key | free |

Two calls were executed with real arguments. Both answers carry a receipt.

`domain_trust` on `example.com` returned `verdict: likely_safe`, `risk_score: 0`, `age_days: 11396`, `blocklist_listings: 0`, `https_valid: true` and an empty `not_checked` list, with the method stated as `Rule-based: domain age, blocklists, TLS. A heuristic, not a guarantee.` The receipt reads `rail: sample`, `charge_usd: 0.0`.

`domain_email_auth` on the same domain returned `ok: true` with `spf: {status: pass, record: "v=spf1 -all"}`, a `requestId`, and a cache block showing a stale hit at `ageSeconds: 23212`, which is the honest shape of a cached answer rather than a fresh one dressed up as live.

### The payment rail is x402, not a subscription

A call outside the free sample returns HTTP 402 with the full terms rather than a signup wall: `rail: x402`, `x402Version: 2`, `scheme: exact`, `network: eip155:8453` (Base mainnet), `asset: 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` (USDC), `amount_atomic: 20000`, `payTo: 0xa76a0E93C5af3fd43521300B0a58eF5F70fC44F6`, `maxTimeoutSeconds: 300`. Retry the same request with a `PAYMENT-SIGNATURE` header and it settles. A credit rail is offered alongside for clients that cannot sign, and `add_credit` produces a link that adds card credit from $5 without ever revealing the key.

## What It Does Not Do

- No accounts are connected and nothing is read from your systems. Every answer is about a public domain or a public URL.
- `domain_trust` is a heuristic on three signals, and the server says so in the response. It is not a credit decision and not a guarantee.
- `page_watch` needs a first call to store a baseline before any change can be reported, so a fresh connection reports `changed: false` on day one.
- Email authentication is a record check. It reads the published policy; it does not test a sending reputation or a mailbox.
- Paid calls need a funding rail. Without one, only the sample inputs answer.

## FAQ

### Can an agent use it without paying?
Yes for the sample inputs, which are the documented examples such as `example.com`. Any other domain returns HTTP 402 with x402 terms, so an unfunded connection is a demo rather than a service.

### What does the trust verdict actually measure?
Domain age, spam and abuse blocklist listings, and HTTPS certificate validity. The response lists the reasons behind the score and names any check that could not run under `not_checked`.

### Is this a monitoring product?
Partly. `page_watch` diffs a page against its own stored baseline, `site_status` checks liveness, and `bot_observatory` returns the crawler and fingerprint activity seen across networks in the last seven days, refreshed hourly.

### Where does the email authentication data come from?
The responses name the source. In this session `domain_email_auth` returned `via dns.pizza`, so the SPF, DKIM and DMARC posture is measured on the same infrastructure the vendor publishes publicly.

## The Operator Test

Ask it about the domain on the last invoice you paid that felt wrong. If the answer is a registration date in the last month, a blocklist listing, or a certificate that does not validate, the tool paid for itself before the second question.

Pairs with `dnstwist` style watchlist work and with the SEO and site-health entries in this catalog, because AI crawler access and domain trust are read by the same people.
