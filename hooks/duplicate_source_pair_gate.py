"""Abort the docs build when two source files claim one output URL.

Why this exists
---------------
MkDocs does not fail when `X.md` and `X/index.md` both exist. It builds one and
silently drops the other. On 2026-11-03 thirteen pages were in that state: the
dead copy held unique sections in 9 of 13 pairs, and every edit made to it
published nothing. `sitemap.xml` listed each URL twice, and each copy
canonicalised to itself, so the canonical prune could not see it.

The check lives in `scripts/check_source_url_collisions.py` so the same rule
runs from the command line, from this hook, and from the tests.

Why a build hook instead of a workflow step
-------------------------------------------
The push credential for this repository has no `workflow` scope, so a
workflow-file change cannot be pushed from the agent account. An MkDocs hook is
enforced by the same `mkdocs build` that produces the deployed site, plus every
local build.

Behaviour
---------
on_config runs the gate once per build. Clean tree: the build continues. A
collision: SystemExit naming each URL and both files, so the build stops before
deploying. Fix by merging the useful sections into the published file and
deleting the shadowed one.
"""

import importlib.util
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO, "scripts", "check_source_url_collisions.py")


def _load():
    spec = importlib.util.spec_from_file_location("check_source_url_collisions", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["check_source_url_collisions"] = mod
    spec.loader.exec_module(mod)
    return mod


def on_config(config):
    if not os.path.exists(SCRIPT):
        return config
    mod = _load()
    collisions, stale = mod.scan()
    real = {url: paths for url, paths in collisions.items()
            if os.path.dirname(paths[0]) not in mod.EXEMPT_DIRS}
    if not real:
        return config

    lines = ["two or more source files claim the same output URL:", ""]
    for url, paths in sorted(real.items()):
        lines.append(f"  /{url}".rstrip("/"))
        for path in paths:
            lines.append(f"    - {path}")
    lines += [
        "",
        "MkDocs publishes only one of these and drops the rest silently, so an",
        "edit to the shadowed file publishes nothing. Merge its useful sections",
        "into the published file, then delete it.",
        "",
        "Check: python3 scripts/check_source_url_collisions.py",
    ]
    raise SystemExit("\n".join(lines))
