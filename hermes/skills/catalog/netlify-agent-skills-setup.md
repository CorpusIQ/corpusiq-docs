---
title: "Netlify Agent Skills — Serverless deployment, edge"
description: 6 deployment-focused skills from Netlify covering functions, config, frameworks, edge functions, and forms. 7.9K+ combined installs. Essential for Hermes agents managing Netlify deployments.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/netlify-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Netlify Agent Skills — Setup Guide

**Source:** [netlify/context-and-tools](https://github.com/netlify/context-and-tools) (7,900+ combined installs)
**Category:** Infrastructure & DevOps
**Quality Tier:** 🟢 Production

Netlify's official agent skills provide authoritative guidance for building, deploying, and managing applications on the Netlify platform. These skills cover serverless functions, edge functions, framework-specific deployment config, forms handling, and platform configuration — giving Hermes agents the full Netlify operations toolkit.

---

## Installation

```bash
npx skills add netlify/context-and-tools --skill netlify-functions
npx skills add netlify/context-and-tools --skill netlify-config
npx skills add netlify/context-and-tools --skill netlify-deploy
npx skills add netlify/context-and-tools --skill netlify-frameworks
npx skills add netlify/context-and-tools --skill netlify-edge-functions
npx skills add netlify/context-and-tools --skill netlify-forms
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **netlify-functions** | 1.4K | Write serverless functions with modern syntax (default export + Config). Covers TypeScript, path routing, background functions, scheduled functions, streaming, and method routing |
| **netlify-config** | 1.3K | Configure `netlify.toml` with redirects, headers, build settings, and environment variables |
| **netlify-deploy** | 1.3K | Deploy via Git, CLI, or API. Covers branch deploys, deploy previews, rollbacks, and split testing |
| **netlify-frameworks** | 1.3K | Framework-specific deployment guidance: Next.js, Remix, Astro, SvelteKit, Nuxt, and more |
| **netlify-edge-functions** | 1.3K | Edge Functions using Deno runtime — location-based personalization, auth at the edge, A/B testing, geolocation |
| **netlify-forms** | 1.3K | Built-in form handling without server-side code — spam filtering, notifications, webhooks, file uploads |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Netlify account** | Free tier available at [netlify.com](https://netlify.com) |
| **Netlify CLI** | `npm install -g netlify-cli` |
| **Git** | Required for Git-based deploys |

---

## Key Capabilities

### Serverless Functions
Build API endpoints, background jobs, and scheduled tasks directly in your repo. Netlify Functions auto-scale and use standard Web API `Request`/`Response` objects. Modern syntax uses default export + Config pattern — no legacy `exports.handler`.

### Edge Functions
Run code at the edge on Deno runtime for ultra-low-latency personalization, auth gates, geolocation routing, and A/B testing before the request hits origin.

### Framework-Aware Deployments
Automatic detection and optimization for Next.js, Remix, Astro, SvelteKit, and other frameworks. Essential runtime configs, SSR support, image optimization, and ISR are handled automatically.

### Git-Centric Workflow
Push to Git → auto-deploy. Preview deploys for every PR. Instant rollbacks. Branch-based environments.

---

## Quick Start

```bash
# Deploy a site from the current directory
netlify deploy --prod

# Create a serverless function
mkdir -p netlify/functions
cat > netlify/functions/hello.ts << 'EOF'
import type { Context, Config } from "@netlify/functions";
export default async (req: Request, context: Context) => {
  return new Response(JSON.stringify({ message: "Hello from Hermes" }), {
    headers: { "Content-Type": "application/json" },
  });
};
export const config: Config = { path: "/api/hello" };
EOF

# Deploy
git add . && git commit -m "Add hello function" && git push
```

---

## Verification

```bash
npx skills list | grep netlify
```

---

## Notes

- All skills use the official Netlify documentation as their knowledge base — no guesswork
- Edge Functions require the `@netlify/edge-functions` types package for TypeScript
- Functions auto-detect TypeScript — no build step needed
- Form handling is built into Netlify's edge — enable with `netlify` attribute on HTML forms
- Hermes agents can use these skills to provision full-stack apps, set up API endpoints, and manage CI/CD on Netlify
