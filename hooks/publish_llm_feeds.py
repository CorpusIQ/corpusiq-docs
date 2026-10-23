"""Publish the LLM feeds and a build marker into the built site.

Why this exists
---------------
``llms.txt`` and ``llms-full.txt`` live at the repository root and are written by
``scripts/generate_llms_txt.py``. They are not inside ``docs/``, so MkDocs never
copies them into the built site on its own.

Two publishers compensated for that with an explicit ``cp llms.txt llms-full.txt
site/``: the ``vercel-deploy`` workflow and ``scripts/deploy_docs.py``.

Production, however, is served by the Vercel Git integration, which runs
``mkdocs build`` on every push to main and nothing else. That path never ran
either copy, so the live site answered 404 for ``/llms.txt`` and
``/llms-full.txt`` while the repository held both files, and
``/build-info.json`` was absent, which left the hourly freshness check unable to
prove which commit production was serving.

Emitting the files from a build hook fixes every publisher at once, including
any future one, because the output is produced by ``mkdocs build`` itself rather
than by a step someone has to remember to add.

Scope
-----
Writes exactly three files into ``site_dir``: ``llms.txt``, ``llms-full.txt`` and
``build-info.json``. It never edits source content and never touches the
repository root copies.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

FEEDS = ("llms.txt", "llms-full.txt")


def _git_head(repo_root: Path) -> str:
    """Best effort commit id for the build marker.

    Vercel exports VERCEL_GIT_COMMIT_SHA for the commit it is building, which is
    the authoritative value there. Everywhere else fall back to the checkout.
    """
    sha = os.environ.get("VERCEL_GIT_COMMIT_SHA", "").strip()
    if sha:
        return sha
    try:
        done = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            timeout=20,
        )
        if done.returncode == 0:
            return done.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return ""


def on_post_build(config, **kwargs) -> None:
    repo_root = Path(config.config_file_path).resolve().parent
    site_dir = Path(config.site_dir)
    site_dir.mkdir(parents=True, exist_ok=True)

    published = []
    for name in FEEDS:
        src = repo_root / name
        if not src.is_file():
            continue
        shutil.copy2(src, site_dir / name)
        published.append(name)

    commit = _git_head(repo_root)
    marker = {
        "commit": commit,
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "mkdocs-post-build-hook",
        "feeds": published,
    }
    (site_dir / "build-info.json").write_text(
        json.dumps(marker, indent=2) + "\n", encoding="utf-8"
    )
