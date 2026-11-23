---
title: "RelayShield Scam Checks MCP - Keyless Fraud Screening"
description: "Four free, keyless checks for links, wallets, emails and breach exposure that answer unknown rather than safe, and say why."
category: "Security & Risk"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-23
source: "The mcp.so submission queue entry #7908 filed 2026-11-23T14:54:51Z; a keyless initialize and tools/list on `https://relayshieldadmin-relayshield-free-mcp.hf.space/mcp` that answered 200 with four tools; nine tools/call requests across all four tools; and the registry records for the publisher's three servers, `io.github.nzdsf2-gif/relayshield-free-mcp` 1.30.1, `relayshield-firewall` 0.3.0 and `relayshield-mcp` 0.2.11"
relevance: "★★★★"
tags: [fraud, phishing, breach-check, threat-intelligence, due-diligence, keyless, email-security, remote-mcp]
last_updated: "2026-11-23"
---

# RelayShield Scam Checks MCP

**The worst answer a security check can give is "safe".** A clean verdict from a wrong database is worse than no verdict, because it ends the question. RelayShield's free server is built around that one idea: every tool answers **unknown** when it has nothing, states which signals it actually consulted, and never promotes absence of evidence into clearance. Four tools, no key, no signup.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://relayshieldadmin-relayshield-free-mcp.hf.space/mcp
Server:      relayshield-free (version string empty)
Auth:        none for the link, wallet and email checks
Tools:       4 (check_link, check_wallet, check_email, check_breach)
Hosted on:   Hugging Face Spaces
Registry:    io.github.nzdsf2-gif/relayshield-free-mcp 1.30.1
Family:      relayshield-firewall 0.3.0 (50 free calls, then $49/month),
             relayshield-mcp 0.2.11 (subscription)
```

## Four tools, each answering one question

| Tool | The question it answers |
| --- | --- |
| `check_link` | Is this URL in the known-phishing corpus or the threat feeds? One URL, or up to 25 in one call |
| `check_email` | Does this set of parsed email fields carry phishing signals - claimed sender, display name, reply-to, links, attachments |
| `check_breach` | Does this address appear in known breaches, and in which ones |
| `check_wallet` | Is this crypto address flagged, read-only, and does it ever move funds itself |

The submission describes the corpus as threat intelligence from **115 monitored Telegram marketplaces**. The server cannot be checked against that claim from outside; what can be checked is what it returns, which is what follows.

## What "unknown" actually looks like

`check_link` on our own domain:

```
[UNKNOWN] https://corpusiq.io
Signals: IOC corpus=False | threat feeds=False | domain age=Noned
Note: the best verdict this check returns is 'unknown' - absence of
evidence is not evidence of absence.
```

Three things are right and one is broken. Right: the verdict is `UNKNOWN` rather than `CLEAN`, the tool prints the two signals it consulted and both their values, and the note says the quiet part out loud. Broken: **`domain age=Noned`** - the string is a template that appends `d` to a null value, so "domain age" is both unavailable and unreadable. A signal the tool advertises and cannot fill is a defect, not a flourish.

`check_wallet` on the zero address returns the same discipline for crypto:

```
Address: 0x0000000000000000000000000000000000000000
Chain: evm | Risk: LOW
- No flags: nothing known against this address (verdict 'unknown', not 'safe').
```

"Risk: LOW" on an all-zero address would be alarming if the qualifier were missing. It is not missing, and the tool says which verdict it is giving.

## Where the batch path misbehaves

`check_link` accepts 25 URLs in one call. Two were passed:

```
Checked 1 link(s): 0 flagged, 1 incomplete.
- [UNKNOWN] http://paypa1-secure-login.example
- [UNKNOWN] https://example.com - example.com is an IANA-reserved documentation
  name (example.com); it is never a real-world target, so no threat signals were checked.
- [NOT CHECKED - retry] http://paypa1-secure-login.example
```

The count says **one** checked, **one** incomplete. The lookalike domain was checked and then printed again as not checked, while `example.com` was correctly skipped with its reason. A reader cannot tell which of the two links actually went to the corpus. **Recorded as a defect: the batch result set and the batch count disagree, and one input appears twice with opposite dispositions.** The single-URL path does not exhibit it, and every guide fact below comes from single calls.

Bad input is refused cleanly and in band:

```
Error executing tool check_link: {"ok": false, "status_code": 400,
 "body": "{\"ok\": false, \"error\": \"url is required and must start with
 http:// or https://, or pass urls[] to check several at once\"}"}
```

That is a specific rule with the remedy attached, which is what an agent needs to correct itself.

## Breach exposure, and what a test address teaches

`check_breach` on `test@example.com` returned **275 breaches** with names and dates - Adobe (2013-10-04), Stratfor (2011-12-24), Yahoo (2012-07-11), Gawker (2010-12-11), MailRu (2014-09-10), LinkedIn (2012-05-05), Dropbox (2012-07-01), MySpace (2008-07-01), Tumblr (2013-02-28), VK (2012-01-01) and 265 more. A throwaway address on a reserved domain returning 275 breaches looks like a wildcard.

It is not. A unique address on our own domain returned **0**. `test@example.com` is one of the most-used test addresses in existence and appears in exactly the kinds of dumps this tool indexes, so 275 is a plausible reading rather than a bug. **The lesson is the operational one:** test a security tool with an address you know the history of, or the tool's output teaches you nothing. Any address on a real domain that returns dozens of hits deserves a look at the names and dates before it is treated as a customer problem.

## Email scoring, and the limit that matters

A made-up business email fraud, deliberately shaped like the classic invoice scam - claimed sender `ceo@corpusiq.io`, subject "Invoice overdue - urgent payment", body asking to open the attachment and pay:

```
Claimed sender: ceo@corpusiq.io
Risk: low | Score: 0
Note: heuristic verdict over the fields you supplied - it never answers
'safe', and a 'low' score on a vague forward is 'unknown', not 'legitimate'.
```

A score of **0** on that message is the single most useful thing in this guide. The tool scores **the fields you give it** - sender, display name, reply-to, links, attachment names - and a subject and body that read like a scam carry no weight on their own. An operator who forwards "is this email safe" and receives `Risk: low` will read it as clearance unless they understand the tool's scope. **Feed it the reply-to, the links and the attachment names; a bare body is not a check.**

The vendor says this in the note, which is why the tool deserves the four stars rather than two. The failure is in how a score reads to a human, not in what the tool claimed.

## FAQ

### Does RelayShield need an API key or an account?

No. The link, wallet and email checks are keyless, and the endpoints answered a keyless `initialize` with four tools. The submission says no signup and no key, and the probe agrees.

### Is a clean result from this tool a safety guarantee?

No, and the tool refuses to pretend otherwise. Every clean answer reads `[UNKNOWN]` or a `LOW` risk with the qualifier that the verdict is unknown rather than safe. Treat it as a tripwire for known-bad, not as a scanner.

### What is the difference between the free server and the paid ones?

The publisher runs three servers in the official registry: the free scam checks measured here (**1.30.1**), an MCP proxy firewall that screens every tool call (**0.3.0**, 50 free calls then **$49 a month**), and a subscription server covering breach detection, SIM swap, domain lookalikes, an OAuth watchlist and prompt-injection detection (**0.2.11**). The free server is the front door to a paid family, and this guide measures only the door.

### Why did two URLs come back as one checked?

The batch path prints the count and the list from different places: one line reports 1 checked and 1 incomplete, and a URL appears both as `[UNKNOWN]` and as `[NOT CHECKED - retry]`. Use single-URL calls until that is fixed, and record the discrepancy if you report on it.

## Verdict

**The best-behaved security surface in this catalog on the question of honesty, and it is free.** Four stars because it is drivable, keyless and refuses to overclaim, with two defects recorded rather than smoothed - the `domain age=Noned` template, and the batch path that disagrees with its own count. For an operator the practical use is narrow and real: check a payment-change link or a supplier's attachment name before the wire goes out, and check a customer address against the breach list before promising confidentiality. Do not hand it a bare email body and read the zero.
