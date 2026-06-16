---
title: Troubleshooting
description: Common issues and fixes for Hermes agent deployment. Browser, OAuth, cron, model routing, Playwright, SSH.
---

# Troubleshooting

## Browser Automation

| Symptom | Cause | Fix |
|---------|-------|-----|
| `agent-browser` won't install Chrome | DGX Spark is aarch64 | Use Playwright chromium-1223 + `~/.agent-browser/config.json` with `executablePath` |
| Chrome window visible during automation | Not headless | Add `--headless=new` to browser args |
| `browser_navigate` times out on dynamic pages | Page not fully loaded | Use `browser_snapshot` + retry, or bump timeout |

## OAuth & Authentication

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gmail connector returns 401 | Token expired | Run `reset_connector_token` for google_workspace, re-auth |
| OAuth link opens wrong account | Browser cached session | Open link in incognito/private window |
| Headless OAuth fails | Google detects automation | Use Playwright with persistent profile (`userDataDir`) |

## Cron & Scheduling

| Symptom | Cause | Fix |
|---------|-------|-----|
| Job says `last_status: ok` but didn't deliver | Cron tracked execution, not outcome | Run job manually with `cronjob run`, verify output |
| Job skipped silently | Rate limit or concurrency cap | Check `cronjob list` for `last_error` |
| `context_from` chain broken | Upstream job failed | Run upstream first, then chain job |

## Model Routing

| Symptom | Cause | Fix |
|---------|-------|-----|
| Opus used for simple task | No routing rule matched | Add explicit routing rule in config |
| Model not found | Provider mismatch | Check `hermes config list models` |
| High token costs | Sonnet not default | Set `default_model: claude-sonnet-4` in config |

## SSH & Mac Mini

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Connection refused` | SSH not running or firewall | `sudo systemctl enable ssh --now` on Mac Mini |
| `Permission denied` | Key not in authorized_keys | `ssh-copy-id user@worker-node.local` |
| `Host key verification failed` | Machine reimaged | `ssh-keygen -R worker-node.local` |

## Playwright

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Executable doesn't exist` | Wrong chromium path | Set `executablePath` in config or use `npx playwright install chromium` |
| Browser hangs on navigation | Network slow or blocked | Add 30s timeout, check DNS |
| `Target closed` mid-operation | Page navigated away | Re-navigate and snapshot before interacting |

---

*↑ [Home](/hermes/)*
