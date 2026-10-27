---
title: "Yaklang Hack Skills - Offensive Security Toolkit Setup"
description: "Yaklang Hack Skills: 373.5K combined installs of 104 offensive-security playbooks for authorized pentests, CTF and security research."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hack-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "offensive security", "pentest"]
---

# Yaklang Hack Skills - Setup Guide

Yaklang publishes hack-skills as a knowledge base for agents doing security work: one master entry (`hack`), six category routers (`recon-for-sec`, `api-sec`, `auth-sec`, `injection-checking`, `file-access-vuln`, `business-logic-vuln`) and a large set of deep topic skills arranged across web, API, authentication, operating system privilege escalation, Active Directory, mobile, binary exploitation, reverse engineering, cryptography, blockchain, AI and ML, network protocols and forensics. The stated audience is bug bounty, penetration testing, CTF competitions and authorized security research, and the repository describes its own output as generic methodology for educational use rather than a mirror of external payload collections.

The design goal is loader discipline rather than breadth. Each skill is a single `SKILL.md` with a semantic name, and the README prescribes an order: expose the master entry first, route through a category entry by attack surface, and drill into a deep topic only when the engagement reaches it. That is the same shape as a hierarchical router in front of a large reference library, which is why the install index shows 104 listings at 373.5K combined installs while the content stays readable one skill at a time.

Treat everything here as offensive security material. It documents how vulnerabilities are found and proven, including remote code execution, privilege escalation and lateral movement, and it is written for engagements where the operator has written authorization. Nothing in the skills establishes or checks authorization, so that condition sits entirely with whoever runs the agent.

**Source:** [yaklang/hack-skills](https://www.skills.sh/yaklang/hack-skills) via skills.sh - 373.5K combined installs across 104 indexed listings; first seen Apr 8, 2026 (Oct 26, 2026 sweep)
**GitHub:** [yaklang/hack-skills](https://github.com/yaklang/hack-skills) (2,551 stars; MIT LICENSE in-repo; branch main, pushed 2026-09-13; layout is `skills/<name>/SKILL.md` for 103 skills alongside `assets/`, `site/`, `scripts/`, `README.md` and a Chinese mirror in `README_CN.md`)
**Category:** Security / Offensive Testing
**Quality Tier:** 🟡 Beta - 373.5K installs and 103 of 104 listings resolving to a directory in the current tree, MIT licensed with a push on 2026-09-13, and Gen Agent Trust Hub and Snyk Pass on all three sampled skills; held below Production by Socket returning Warn on every sampled skill and by the content being offensive-security material that only belongs in authorized engagements

## Installation

```bash
# Install the whole knowledge base with the skills CLI
npx skills add yaklang/hack-skills
```

```bash
# Fetch the master entry on its own, as the README documents
curl -fsSL https://raw.githubusercontent.com/yaklang/hack-skills/main/skills/hack/SKILL.md
```

```bash
# Work from a local clone instead
git clone https://github.com/yaklang/hack-skills.git
cd hack-skills
```

The README also publishes an AES-256 ZIP of all the Markdown for air-gapped use, with a public constant password of `hack-skills`. The repository is explicit that this is not access control: the password is printed openly in the README, the website and the CI workflow, and it exists only to stop AV and browser scanners from quarantining plain offensive-security Markdown in transit.

```bash
curl -fsSLO https://oss-qn.yaklang.com/hack-skills/latest/hack-skills.zip
7z x -phack-skills hack-skills.zip
```

There is no runtime, API key or build step. The skills are Markdown, `npx skills add` copies or links them into the agent's skills directory, and nothing executes at install time.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hack | 4,344 | Master entry: global routing, operating doctrine, phase assessment, test matrix and evidence standard |
| android-pentesting-tricks | 4,077 | APK analysis and reverse engineering, Frida hooking, intent exploitation, root detection bypass |
| sqli-sql-injection | 4,027 | SQL injection per database engine, WAF bypass matrix, CTF techniques such as handler and innodb tricks |
| code-obfuscation-deobfuscation | 4,023 | Control flow flattening, opaque predicates, string encryption, OLLVM and Themida analysis |
| recon-and-methodology | 4,022 | Recon methodology framework, Java middleware fingerprint matrix, leak detection checklist |
| xss-cross-site-scripting | 3,956 | Polyglot payloads, WAF bypass by vendor, CSP bypass, DOM clobbering, CSS injection data exfiltration |
| api-sec | 3,934 | Category router for REST, GraphQL and mobile backend routing |
| business-logic-vulnerabilities | 3,889 | Payment manipulation matrix, state machine bypass, coupon and stock race conditions |
| ssrf-server-side-request-forgery | 3,875 | Cloud metadata matrix across six platforms, DNS rebinding, Gopher and Redis RCE chains |
| authbypass-authentication-flaws | 3,811 | Password reset pattern matrix, captcha bypass methods, insecure randomness in tokens and IDs |
| jwt-oauth-token-attacks | 3,796 | JWT algorithm and key confusion, claim tampering, JWKS abuse |
| idor-broken-object-authorization | 3,796 | Systematic IDOR testing and ORM filter chain leaks in Django, Prisma and Ransack |
| api-recon-and-docs | 3,796 | API discovery, OpenAPI and Swagger documents, hidden endpoint enumeration |
| 401-403-bypass-techniques | 3,789 | Path normalization tricks, verb tampering, header-based bypass, proxy misconfiguration |
| waf-bypass-techniques | 3,788 | Encoding chains, chunked transfer tricks, vendor bypass matrices for Cloudflare, AWS WAF, Akamai and ModSecurity |
| api-auth-and-jwt-abuse | 3,787 | JWT attacks, API key abuse and token manipulation |
| websocket-security | 3,769 | Cross-site WebSocket hijacking, origin validation gaps, wsrepl and ws-harness tooling |
| vm-and-bytecode-reverse | 3,747 | Custom VM and bytecode analysis, Python, Java and .NET decompilation, opcode mapping |
| api-authorization-and-bola | 3,743 | BOLA and BFLA, mass assignment, object-level authorization testing |
| auth-sec | 3,738 | Category router for authentication, sessions, OAuth, JWT and object-level authorization |
| kubernetes-pentesting | 3,730 | RBAC abuse, ServiceAccount token theft, etcd access, kubelet API and pod security bypass |
| cors-cross-origin-misconfiguration | 3,726 | Origin reflection, null origin, subdomain trust abuse |
| injection-checking | 3,725 | Category router that separates XSS, SQLi, SSRF, XXE, SSTI, CMDi and NoSQL before testing |
| ios-pentesting-tricks | 3,723 | IPA analysis, Objective-C runtime manipulation, jailbreak detection bypass, Keychain access |
| recon-for-sec | 3,714 | Recon category router: asset discovery and technology identification at the start of an engagement |
| llm-prompt-injection | 3,703 | Direct and indirect injection, RAG poisoning, tool and function abuse, MCP security risks |

The remaining 78 indexed listings range from 1 to 3,699 installs, and they are not a lesser tier of content: heap exploitation, kernel exploitation, request smuggling, deserialization, Active Directory certificate services, tunneling and pivoting and reverse shells all sit just under the threshold, at 3,400 to 3,699 installs each.

## Why This Matters for Hermes Agents

Security work is where an agent's failure mode is most expensive. A generic model asked to test an API will produce a plausible checklist; these skills instead impose an order: assess the attack surface, route to one category, establish the injection point, prove impact without destroying the target, then record evidence. The `hack` master entry even carries a quality gate and an evidence standard, which is the part most security prompting leaves out.

The loader priority is what makes a 104-listing suite usable in a working context window. Route first, drill second: an agent handling a JWT question opens `auth-sec`, then `jwt-oauth-token-attacks`, and never loads the binary exploitation or cryptography families. That keeps a large offensive library at a few hundred lines of active context per turn instead of flooding the window with payload tables that do not apply.

The repository also takes a defensible position on destructive payloads, which matters when an agent is the one typing. Its documented policy replaces irreversible operations with non-destructive proofs of the same primitive: a stacked `DROP TABLE` becomes a time delay, a `FLUSHALL` chain is dropped, an actuator shutdown endpoint becomes an environment or heap dump read. The injection point is still proven and the target still stands, which is exactly the trade an autonomous agent should be making.

Used from the defensive side, the same content reads as a review checklist. The CSP, CORS, JWT, OAuth, request smuggling and prompt injection skills describe the misconfigurations that a code review or a hardened deployment should be checked against, and they are specific enough to name the header or the flow rather than gesturing at best practice.

## Usage

| You say | What happens |
|---|---|
| "Start a test on this staging app, we have written authorization" | Loads `hack` for routing and sequencing, then `recon-for-sec` for asset and technology discovery |
| "There is a JWT in the login response, can it be abused?" | Routes through `auth-sec` into `jwt-oauth-token-attacks` for algorithm confusion, claim tampering and JWKS abuse |
| "The WAF is blocking our SQLi payloads" | Routes to `waf-bypass-techniques` for encoding chains and vendor matrices, then back to `sqli-sql-injection` for engine specifics |
| "Review this API for broken object level authorization" | Loads `api-authorization-and-bola` and `idor-broken-object-authorization` for the object-level test pattern |
| "Our chatbot reads untrusted documents" | Loads `llm-prompt-injection` for indirect injection, RAG poisoning and tool abuse paths |
| "Analyse this PCAP from the incident" | Loads `traffic-analysis-pcap` for protocol dissection and stream reconstruction, a forensics skill rather than an attack one |
| "Can we escalate from this container?" | Loads `container-escape-techniques`, which covers Docker socket abuse, privileged containers and cgroup breakouts |

## Verification

Confirm what the skills CLI installed, and that it installed the routers rather than a single deep topic:

```bash
npx skills list | grep -iE "hack|api-sec|auth-sec|injection-checking"
```

Read the master entry before installing anything. The five URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/yaklang/hack-skills/main/README.md
curl -sL https://raw.githubusercontent.com/yaklang/hack-skills/main/skills/hack/SKILL.md
curl -sL https://raw.githubusercontent.com/yaklang/hack-skills/main/skills/sqli-sql-injection/SKILL.md
curl -sL https://raw.githubusercontent.com/yaklang/hack-skills/main/skills/xss-cross-site-scripting/SKILL.md
curl -sL https://raw.githubusercontent.com/yaklang/hack-skills/main/skills/llm-prompt-injection/SKILL.md
```

The directory listing behind the install index also returned 200 on the same date, and it is the quickest way to see which listed skills actually exist in the tree:

```bash
curl -s https://api.github.com/repos/yaklang/hack-skills/contents/skills | grep '"name"'
```

This is offensive-security content. Verify the skills in a lab or a scoped engagement target before pointing them at anything that matters, and read the master entry's own operating doctrine rather than skipping to a deep topic.

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hack | Pass | Warn | Pass |
| android-pentesting-tricks | Pass | Warn | Pass |
| sqli-sql-injection | Pass | Warn | Pass |

The verdicts describe packaging, not intent. Gen Agent Trust Hub and Snyk pass all three sampled skills while Socket returns Warn, which is the expected signature of a repository full of offensive tooling: the scanner recognises dual-use content even when the files themselves are inert Markdown. Nothing here executes at install time, no skill declares an `allowed-tools` field, and the repository ships no installed runtime of its own.

The risk is entirely in what the content instructs an agent to do. These files document how to obtain command execution, escalate privileges, move laterally and exfiltrate data, and they assume an authorized engagement. Run them only against targets you own or have written permission to test, keep the agent's scope bounded to that target, and treat any output that touches a third-party system as out of scope. For defensive use, prefer the review-shaped skills (CSP, CORS, JWT, OAuth, request smuggling, prompt injection) and read the playbooks as checklists rather than actions.

The licence is MIT with a LICENSE file in the repository, so the text can be reused with the usual attribution and warranty terms.

## Limitations

- Authorized testing only. Every skill assumes written permission for the target, and nothing in the suite checks or records that permission; the operator carries it entirely.
- One listing has no directory. `hackskills-bugbounty-hunter` shows 1 install in the index but has no counterpart in the current `skills/` tree, so it cannot be installed from this repo.
- Verdicts are sampled. skills.sh security verdicts were read for 3 of the 104 listings, and Socket returns Warn on all three, so the remaining listings are unaudited here.
- Volume is the point, not a defect to fix. Roughly a hundred deep topic playbooks across 14 domains, several of them long (deserialization and ghost bits alone run to many hundreds of lines), so an unpinned agent can load far more context than the task needs.
- Router and playbook names overlap. `api-sec`, `auth-sec`, `injection-checking`, `file-access-vuln` and `business-logic-vuln` are routers while `api-authorization-and-bola`, `authbypass-authentication-flaws` and `business-logic-vulnerabilities` are the playbooks, and picking the wrong one wastes a turn.
- Snapshot data, verified Oct 26, 2026: 373,468 combined installs across 104 indexed listings; 2,551 GitHub stars; MIT License; last pushed 2026-09-13. Counts drift over time.

## Related

- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup) - the competition-oriented counterpart, useful when the target is a challenge binary rather than a live application.
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup) - agents that run the engagement themselves, where this repo supplies the methodology they read.
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup) - the defensive side of the same material, oriented to reviewing an application rather than attacking it.
- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup) - a curated research-firm suite that pairs well as a second opinion on audit findings.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the suite, then expose only `hack` by name in your agent's configuration. The master entry routes correctly and costs a fraction of what a preloaded deep topic does.
- Give the agent a bounded scope in the prompt, not just a target. "Staging environment at this host, authorized, do not touch production" changes behaviour more than any skill file will.
- Use the router names as verbs in your own requests. Saying "route this through auth-sec" gets a category decision first, which is the sequence the repository was designed around.
- Prefer the non-destructive proof pattern even when a damaging payload exists. A time delay or a read proves the injection point and leaves the target intact for the next test.
- Keep a copy in the repo of record you are auditing. A pinned clone makes findings reproducible, where a moving `main` does not.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
