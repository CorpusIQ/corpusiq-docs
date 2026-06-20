---
title: frontend-development
description: Pattern for a Next.js + Tailwind frontend that serves BOTH a public marketing site and an authenticated customer dashboard from the same repo. Vercel auto-deploy, the canonical-constant rule for shared values, npm build's public/ writeback gotcha, and the deploy-verification boundary.
---

# Frontend Development (Next.js + Vercel)

When a single Next.js repo serves BOTH the public marketing site (`www.<domain>/*`) AND the authenticated customer dashboard (`/dashboard/*`), the discipline shifts compared to either alone. This skill covers the patterns that bite once you have both surfaces in one codebase.

## The single-repo, two-surface architecture

- Marketing routes: `/`, `/pricing`, `/connectors`, `/blog`, etc. — public, SEO-critical, indexed by Google
- Dashboard routes: `/dashboard/*` — authenticated, behind a session cookie, the actual product UX
- The BFF layer (`/api/*` Next.js routes) wraps your backend API and handles cookie-based session state — the API itself never sets cookies, the frontend does
- Vercel auto-deploys every push to main — one push, both surfaces redeploy

The trap: a copy-edit to a pricing page on the marketing side and a UX change to the dashboard land in the same Vercel deploy. If either breaks, both go down. Watch deploy status after EVERY push, not just dashboard PRs.

## The canonical-constant rule

A real failure mode: someone added a connector to the connector substrate, also added it to the dashboard's connector list (good), but the marketing site's `/connectors` page is generated from a separate constant file (bad). Customers visit the marketing page, see the connector listed, try to connect from the dashboard — and the dashboard shows it as Connected (because the marketing page wasn't the source of truth). Or worse, the marketing page does NOT show the connector, customers don't know it exists, the dashboard offers it but nobody knows.

**The rule:** any value that appears on BOTH surfaces (connector count, pricing, feature lists, plan tiers) has exactly ONE source of truth, imported by both surfaces. If you find yourself updating the same string in two files, you've found a canonical-constant violation.

Audit pattern: grep your repo for the value before changing it, confirm it appears in only one place.

## npm build's `public/` writeback gotcha

If your build script writes generated files into `public/` (e.g. sitemap.xml, OG images, schema.json), AND those generated files are committed to git, you'll get a recurring "uncommitted changes after build" problem on local dev.

Solutions, in order of preference:
1. Add the generated files to `.gitignore` and regenerate on deploy (preferred)
2. Build into a separate directory, copy to `public/` only in CI
3. If they MUST be committed, run the build once after every change and commit the artifact along with the source

The third option drifts silently — the build's output and the committed artifact eventually diverge and the deployed site shows stale generated content.

## Deploy verification — the marketing-site-specific check

After any push that touches a customer-visible marketing surface (new connector, pricing change, new page):

```bash
# 1. Wait for Vercel to finish (typically 90s-3min)
# 2. Fetch the live page directly
curl -s https://www.<your-domain>/<page> | grep <new-thing>

# 3. If the marketing site's CMS / data layer is in a different repo, ALSO check there
# Common pattern: MCP server ships a connector → marketing site (separate repo) needs a
# matching entry. The MCP merge does NOT update the marketing site repo.
```

The MCP-server-changes-don't-update-marketing-site trap bites hard. Customer reads marketing site, sees old connector list, tries new connector, hits "connector not found." You shipped the platform change but the marketing site is wrong.

## Author email mapping (Vercel auto-deploy quirk)

If your Vercel project is configured to auto-deploy on push from specific authors, a contributor's commit may NOT trigger auto-deploy under their identity. The fix is usually manual: someone with the Vercel admin role hits "Redeploy" in the dashboard.

When you (the agent) push a fix to the frontend repo and the deploy doesn't fire automatically, the honest framing in your status update is: "PR merged at <SHA>. Vercel auto-deploy may not have fired because of author-email mapping; please click Redeploy in the Vercel dashboard if you don't see it deploying within 2 minutes." Don't claim "deployed" without verifying the deploy actually happened.

## Cross-repo boundary

If your marketing copy lives in this repo but your blog posts, knowledge base, or product docs live in a DIFFERENT repo (common when the docs site is a separate Vercel project), the boundaries:

- Changes to marketing routes (homepage, /pricing, /features) — this repo
- Changes to /blog or /docs — usually the other repo
- Connector listings: depends on the project — some teams put the canonical list in the docs repo and import it here; some put it here and link from docs. Confirm before editing

When in doubt, grep the deployed page for a unique string and see which repo's git log mentions it most recently.

## Related

- [mcp-architecture](../mcp-architecture/#marketing-site-is-a-separate-repo-verification-trap) — the MCP-server-side view of the same cross-repo boundary
- [api-development](../api-development/) — the BFF layer's backend dependency

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
