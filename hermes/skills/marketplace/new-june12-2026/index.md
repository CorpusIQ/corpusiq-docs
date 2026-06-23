---
title: June 12, 2026  --  New Hermes Security & UI Skills
description: "Overnight sweep: 3 new Hermes-specific skills discovered  --  security attestation, traffic monitoring, and a Hermes-themed UI deck. From ClawSec and nexu-io."
---

# June 12, 2026  --  New Hermes Security & UI Skills

Overnight sweep found **3 new Hermes-specific skills** not in any existing catalog page. Key finds: ClawSec's security attestation/traffic monitoring suite from `prompt-security/clawsec` and a Hermes-themed cyber UI deck.

*Previously cataloged: 334 total (89 native + 245 marketplace). This update adds 3 → 337 total.*

---

## prompt-security/clawsec  --  Hermes Security Suite (2 skills)

ClawSec by Prompt Security provides Hermes-first runtime security attestation and traffic monitoring. Both skills use signed release verification with reproducible checksum validation. AGPL-3.0-or-later licensed.

### hermes-attestation-guardian (54 installs) 🛡️

Runtime security attestation and drift detection for operator-managed Hermes infrastructure. Generates deterministic posture attestations, verifies them with fail-closed integrity checks, and compares baseline drift using stable severity mapping. Includes advisory feed integration with signed verification.

**Install:**
```bash
npx skills add prompt-security/clawsec --skill hermes-attestation-guardian -a hermes-agent -y
```

**Key features:**
- **Posture attestation**: gateway flags, risky toggles, feed verification status
- **File integrity**: watched files + trust anchors with SHA-256 verification
- **Canonical digest**: stable JSON representation with deterministic hashing
- **Advisory feed**: signed feed verification with NVD CVEs and community advisories
- **Cron scheduling**: managed attestation + advisory check schedule blocks
- **Fail-closed**: exits non-zero on schema/digest/signature mismatch
- **Signed releases**: reproducible checksum verification with ClawSec release key

**Requires:** `node`
**Output:** `~/.hermes/security/attestations/current.json`
**Homepage:** https://clawsec.prompt.security
**Version:** 0.1.4

**Quick start:**
```bash
# Generate attestation
node scripts/generate_attestation.mjs

# Verify schema + canonical digest
node scripts/verify_attestation.mjs --input ~/.hermes/security/attestations/current.json

# Verify with baseline diff (fail on high severity)
node scripts/verify_attestation.mjs \
  --input ~/.hermes/security/attestations/current.json \
  --baseline ~/.hermes/security/attestations/baseline.json \
  --baseline-expected-sha256 <trusted-sha256> \
  --fail-on-severity high

# Schedule automatic attestation every 6 hours
node scripts/setup_attestation_cron.mjs --every 6h --apply
```

**Advisory feed overrides (optional):**
| Variable | Purpose |
|----------|---------|
| `HERMES_ADVISORY_FEED_SOURCE` | `auto`, `remote`, or `local` |
| `HERMES_ADVISORY_FEED_URL` | Remote feed URL |
| `HERMES_ADVISORY_FEED_PUBLIC_KEY` | Pinned key override |

---

### hermes-traffic-guardian (24 installs) 🔍

Runtime traffic monitoring baseline for opt-in proxy inspection, egress detection, and attestation-aware traffic posture. **Baseline specification skill**  --  intentionally does not ship a proxy or runtime implementation yet (v0.0.1-beta3). Builders use this as the landing zone for implementing Hermes traffic monitoring.

**Install:**
```bash
npx skills add prompt-security/clawsec --skill hermes-traffic-guardian -a hermes-agent -y
```

**Key features:**
- Opt-in HTTP proxy inspection (operator-scoped)
- Optional HTTPS inspection with per-process CA trust
- Outbound exfiltration detection + inbound injection detection
- Redacted local threat logs (JSONL format)
- Status export for `hermes-attestation-guardian` integration
- Safety-first: detect-and-log by default, no automatic CA installation

**Requires:** `node`, `python3`
**Version:** 0.0.1-beta3
**State dir:** `$HERMES_HOME/security/traffic-guardian`

**Safety contract:**
- Opt-in only  --  no global proxy changes
- Detect-and-log by default  --  no blocking in v0.0.1
- Secrets redacted before logs/attestation exports
- No automatic system trust-store mutation
- No full request/response body collection
- No sending traffic to external services

**Builder entry points:**
| Path | Use |
|------|-----|
| `lib/` | Detector rules, redaction, posture export, report formatting |
| `scripts/` | Start, stop, status, config validation, log query, attestation export helpers |
| `test/` | Unit tests, proxy fixture tests, redaction tests, attestation export tests |
| `SPEC.md` | Full specification  --  read before implementing |

**Required first implementation behavior:**
1. Validate config without starting the proxy
2. Start monitor in foreground or explicit background mode
3. Scope proxy env vars to target Hermes service or CLI process
4. Inspect HTTP request/response text up to bounded byte limit
5. Support optional HTTPS MITM only with per-process trust config
6. Emit JSONL findings with redacted snippets
7. Export posture JSON for `hermes-attestation-guardian` integration

---

## nexu-io/html-anything  --  Hermes Theme (1 skill)

### deck-hermes-cyber (29 installs) 🎨

Hermes-themed cyber UI deck from the `nexu-io/html-anything` collection. Minimal documentation  --  SKILL.md not publicly accessible on GitHub. Part of a themed-deck collection alongside invoice, meeting-notes, live-dashboard, and doc-kami-parchment decks. Primarily cosmetic/aesthetic.

**Install:**
```bash
npx skills add nexu-io/html-anything --skill deck-hermes-cyber
```

---

## Summary

| Skill | Installs | Source | Category |
|-------|----------|--------|----------|
| `hermes-attestation-guardian` | 54 | prompt-security/clawsec | Security |
| `hermes-traffic-guardian` | 24 | prompt-security/clawsec | Security |
| `deck-hermes-cyber` | 29 | nexu-io/html-anything | UI/Theme |

**New this update:** 3 skills
**Marketplace subtotal before:** 245 → **After:** 248
**Total skills:** 334 → **337**
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
