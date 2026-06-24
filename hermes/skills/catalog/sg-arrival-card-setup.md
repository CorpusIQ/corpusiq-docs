---
title: SG Arrival Card (SGAC) Automation Setup Guide
description: Install and configure Freakingnolife/sg-arrival-card-skill — automated Singapore Arrival Card submission via browser, covering all three residency pathways with CAPTCHA handling and Angular SPA quirks
---

# SG Arrival Card — Browser Automation Setup

**Source:** [Freakingnolife/sg-arrival-card-skill](https://github.com/Freakingnolife/sg-arrival-card-skill)
**Stars:** 2 ⭐ | **License:** MIT
**Created:** June 24, 2026
**Category:** Browser Automation / Government Forms

---

## 1. What It Is

A browser-automation skill for submitting Singapore Arrival Cards (SGAC) via the ICA e-Services portal. Handles the Angular SPA's specific browser-automation quirks — reactive form validation, custom toggle buttons, CAPTCHA routing.

**Key design principle:** Capability-first and portable across agents (Hermes Agent, Claude Code, OpenClaw, Codex CLI). Maps abstract capabilities (Open, Click, Type, PageJS) to concrete agent tools via `references/portability.md`.

### Supported Pathways

| Pathway | Button Label | ID Field | Format |
|---------|-------------|----------|--------|
| Singapore Citizen / PR | "Singapore Citizen / Permanent Resident" | NRIC | S/T + 7 digits + letter |
| LTVP / DP / EP / SP | "Long-Term Pass Holder" | FIN | G/F/M + 7 digits + letter |
| Foreign Visitor (no pass) | "Foreign Visitor / IPA Holder" | Passport No + Nationality | varies |

## 2. Prerequisites

- Hermes Agent with browser automation tools enabled
- Python 3.8+ (for CAPTCHA extraction scripts)
- ICA e-Services portal access (no special account needed)

## 3. Installation

```bash
git clone https://github.com/Freakingnolife/sg-arrival-card-skill.git
cp -r sg-arrival-card-skill ~/.hermes/skills/sg-arrival-card
```

### Verify

```bash
ls ~/.hermes/skills/sg-arrival-card/
# Should show: SKILL.md  references/  scripts/
```

## 4. Configuration

### Tool Bindings

The skill uses abstract capabilities that must be bound to your agent's tools. The default Hermes bindings are:

| Capability | Hermes Tool |
|------------|-------------|
| `Open(url)` | `browser_navigate` |
| `Click(target)` | `browser_click` |
| `Type(text)` | `browser_type` then `browser_press(key="Tab")` |
| `Commit` | `browser_press(key="Tab")` |
| `PageJS(script)` | `browser_console(script)` or `execute_code` |
| `RunCode(script)` | `execute_code` |
| `ReadDoc(image)` | `vision_analyze` |
| `AskUser(question)` | `clarify` or `send_message` |
| `SendFile(path)` | File delivery via agent platform |

### CAPTCHA Handling

The skill includes two scripts for CAPTCHA extraction:

```bash
# On the browser page:
# Run: scripts/extract_captcha.js  (via browser_console)
# Then: scripts/save_captcha.py     (via execute_code)
```

CAPTCHA images are extracted and **routed to the user for solving** — the skill intentionally does not attempt automated CAPTCHA solving.

## 5. Usage

### Quick Reference

```bash
# Start an SGAC submission
hermes -s sg-arrival-card "Submit SGAC for John Tan, Singapore Citizen, arriving 2026-06-25 from Tokyo, staying at 10 Orchard Rd"

# The skill will:
# 1. Navigate to https://eservices.ica.gov.sg/sgarrivalcard/
# 2. Select pathway (SC/PR in this case)
# 3. Enter NRIC and personal details
# 4. Handle health declaration toggles
# 5. Extract and route CAPTCHA to user
# 6. Review and submit
```

### Golden Rule

**Every input:** Click → Type → **Commit (Tab)**
Setting `.value` via JavaScript does NOT trigger Angular validation. Always use Tab to blur the field.

## 6. Included Scripts

| Script | Purpose | Called Via |
|--------|---------|------------|
| `scripts/js_click_by_text.js` | Click Angular button by visible text | PageJS |
| `scripts/set_health_no.js` | Set health toggles to NO | PageJS |
| `scripts/check_declaration.js` | Tick review-page declaration checkbox | PageJS |
| `scripts/extract_captcha.js` | Pull CAPTCHA image, chunked | PageJS |
| `scripts/save_captcha.py` | Decode + save CAPTCHA PNG | RunCode |

## 7. CorpusIQ Use Cases

| Use Case | Application |
|----------|-------------|
| **Reference patterns** | Angular SPA quirks (click→type→commit cycle) apply to any government portal automation |
| **CAPTCHA workflow** | User-in-the-loop CAPTCHA routing pattern is reusable for any form automation |
| **Group submission** | Multiple travellers in one submission — pattern for batch form filling |
| **Portability layer** | The `references/portability.md` pattern is a template for any multi-agent cross-platform skill |

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Form fields not updating | Angular not detecting input | Ensure `Tab` is pressed after each Type |
| CAPTCHA not appearing | Rate limiting or session expiry | Navigate back and retry from step 1 |
| Browser navigation fails | Portal URL changed | Check `https://eservices.ica.gov.sg/sgarrivalcard/` is still live |
| Button click does nothing | Angular button not yet enabled | Wait for page load; some buttons are disabled until previous field is validated |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Discovery](/hermes/skills/marketplace/new-june24-2026/) →*
