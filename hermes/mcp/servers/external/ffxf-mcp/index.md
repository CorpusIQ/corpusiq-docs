---
title: "FFxF MCP - Canadian Cloud Rented From the Chat"
description: "Rent KVM servers, managed Postgres, firewalls, load balancers and GitHub runners in Montreal, with the monthly price quoted before anything is created."
category: DevOps
stars: ★★★ (200 keyless, 71 tools verified)
added: 2026-10-28
source: "live probe of https://ffxf.net/mcp answering HTTP 200 keyless on initialize as ffxf 1.12.0 on protocol 2025-06-18 with a full tools/list of 71 tools, plus chatmcp/mcpso issue #6366 and the official registry entry net.ffxf/cloud"
relevance: ★★
tags: [cloud, vps, kvm, managed-database, postgres, load-balancer, github-runners, montreal, remote-mcp]
last_updated: "2026-10-28"
---

# FFxF MCP

**A server order usually means a console, a pricing calculator and a guess. The guess is what the invoice corrects later.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://ffxf.net/mcp
Auth:        None for catalogue reads, scoped key or OAuth for account actions
Server:      ffxf 1.12.0, protocol 2025-06-18
Tools:       71 at tools/list
Region:      Montreal, Canada, priced in CAD
Registry:    net.ffxf/cloud
```

## Why This Matters for Operators

Provisioning infrastructure is the one operational task where a wrong answer costs money immediately. An agent that can price an order before placing it, and that has to echo the hostname back to destroy anything, is a different risk profile from an agent with a console login.

This is also the first cloud provider surface in this catalogue. The infrastructure entries here cover deployment, monitoring and developer tooling around a hosting choice, not the hosting itself, so a business that wants an agent to stand up a database had no callable path.

What makes it worth an entry is the shape of the write tools. `estimate_vm` runs every check `create_vm` would run and returns the hourly and monthly price without creating anything. `reinstall_vm` and `destroy_vm` require the machine's exact current hostname as confirmation, and the descriptions say to ask the user first. `list_regions`, `list_plans` and `list_images` are public and need no key, so capacity and price can be read before an account exists.

## What It Returns, Verified

A bare `initialize` on `https://ffxf.net/mcp` returned **HTTP 200** with no credential as `ffxf` **1.12.0** on protocol `2025-06-18`. `tools/list` returned **seventy-one tools**, spanning:

- **Machines**: `list_regions`, `list_plans`, `list_images`, `list_vms`, `get_vm`, `get_vm_metrics`, `estimate_vm`, `create_vm`, `power_vm`, `rename_vm`, `reinstall_vm`, `destroy_vm`, `get_action`.
- **Network**: private networks with `create_vpc`, `connect_vpc` hot-adds a card without a restart, `move_vpc` joins the target before leaving the old one so a machine is never cut off, firewalls whose `update_firewall` replaces the whole rule list, and load balancers with pools, targets, listeners, rules and certificates.
- **Managed databases**: PostgreSQL, MySQL, MariaDB and Valkey, with `get_database_options` for engines, versions and sizes by region, `create_database`, `backup_database`, `restore_database` to any minute in the restore window, `fork_database` for a staging copy, `resize_database` upward only, `enable_extension` for pgvector, postgis and pg_trgm, per-user credentials with `reset_database_password`, and `get_slow_queries` reading pg_stat_statements with values replaced by placeholders.
- **CI**: `get_runners` and `list_runner_jobs` for GitHub Actions runners priced per minute, with the queued reason reported as credit, budget or account.
- **Account**: `get_account` returns credit balance, hourly burn rate and runway, which is the number that stops a forgotten machine from becoming a story.

## Limits Worth Recording

One region, Montreal, priced in CAD, so it is a Canadian and eastern North American option rather than a global footprint. It rents infrastructure and does not manage an application on top of it: no PaaS layer, no deploy pipeline beyond the runners. The read tools that need no key are the catalogue and price tools, and everything touching an account needs a scoped key covering `vms.read`, `vms.action`, `databases.write` or similar, so the blast radius is set at key creation rather than at call time. Powered-off machines, storage and reservations are billed by the vendor's own rules rather than explained here.

## FAQ

### Do I need an account to see prices?
No. `list_regions`, `list_plans` and `list_images` are public and keyless, and the plan prices carry both hourly and monthly figures in CAD.

### Can an agent create a server on my behalf?
It can, and it spends credit or raises an invoice when it does. `estimate_vm` prices the order first, and destroy and reinstall require the exact hostname echoed back with an instruction to ask the user first.

### Which databases are available?
Managed PostgreSQL, MySQL, MariaDB and Valkey, with backups, point-in-time restore, forks for staging copies, upward resizing and PostgreSQL extensions including pgvector, postgis and pg_trgm.

### Where do the machines run?
Montreal, Canada. One region, so latency for European or Asian users is not what this is for.

### Is there another cloud provider in this catalogue?
Not as a hosting surface. The DevOps and infrastructure entries here cover deployment, monitoring and tooling around hosting rather than renting the host itself.
