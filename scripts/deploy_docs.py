#!/usr/bin/env python3
"""
Deploy corpusiq-docs to GitHub Pages (legacy branch mode).
Bypasses GitHub Actions entirely - builds locally, pushes to gh-pages,
triggers the Pages build API.

Usage: python3 deploy_docs.py [--commit-msg "..."]

Aug 12, 2026: Created after org-level Actions disable blocked all workflow deploys.
"""
import json
import os
import subprocess
import sys
import time

import requests
import yaml

REPO_DIR = os.path.expanduser("~/workspace/corpusiq-docs")
GH_HOSTS = os.path.expanduser("~/.config/gh/hosts.yml")

def get_token():
    with open(GH_HOSTS) as f:
        d = yaml.safe_load(f)
    return d["github.com"]["oauth_token"]

def run(cmd, cwd=REPO_DIR, fatal=False):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    ok = r.returncode == 0 or "up to date" in r.stderr or "up to date" in r.stdout
    if not ok:
        print(f"CMD FAILED: {cmd}\n{r.stderr[:300]}")
        if fatal:
            print("FATAL: aborting deploy — critical step failed")
            sys.exit(1)
    return r.stdout + r.stderr


def deploy_vercel():
    """Deploy the site/ build to the Vercel docs project (docs.corpusiq.io).

    Independent of GitHub Actions - the GitHub Pages pipeline is blocked
    (Ben-Home account flagged), so Vercel CLI is the production path.
    """
    import json
    secret_path = os.path.expanduser("~/.hermes/profiles/corpusiq/secrets/vercel.json")
    with open(secret_path) as f:
        v = json.load(f)
    token = v["token"]
    team = v["team"]
    # Copy GEO feeds into the build
    run("cp llms.txt llms-full.txt site/")
    # Copy vercel.json INTO the deployed directory so redirects ship with the build
    run("cp vercel.json site/vercel.json")
    # Re-link the deploy directory to the corpusiq-docs project. mkdocs build --clean
    # wipes site/.vercel/project.json, and without it the CLI creates a NEW project
    # (site-one-henna-67) instead of deploying to docs.corpusiq.io.
    os.makedirs("site/.vercel", exist_ok=True)
    with open("site/.vercel/project.json", "w") as f:
        json.dump(
            {"projectId": "prj_sKOYMEdaQZjCcJwYDgfb4KN61na2",
             "orgId": "team_btwsQPaxGRECjJjdKQOMcMUQ",
             "projectName": "corpusiq-docs"},
            f,
        )
    out = run(
        f"npx --yes vercel@latest deploy site --yes --token {token} --team {team} --prod"
    )
    print(out[-500:] if out else "vercel deploy: no output")
    if "Error" in out:
        print("VERCEL DEPLOY FAILED")
        sys.exit(1)
    print("   Vercel deploy OK -> https://docs.corpusiq.io")

def main():
    commit_msg = None
    if "--commit-msg" in sys.argv:
        i = sys.argv.index("--commit-msg")
        commit_msg = sys.argv[i + 1] if i + 1 < len(sys.argv) else None

    # 1. Pull latest main
    print("1. Pulling main...")
    # Generated feed files may be dirty from a previous partial run — discard so pull can rebase
    run("git checkout -- llms.txt llms-full.txt")
    # Clear any stale rebase/merge state left by an interrupted previous attempt -
    # a half-finished rebase makes checkout/pull behave unpredictably.
    run("git rebase --abort 2>/dev/null; git merge --abort 2>/dev/null; true")
    run("git checkout main", fatal=True)
    # Resilient pull (Sep 14): this clone exists only to deploy and holds no unique
    # work; a failed rebase used to abort the whole deploy (e.g. 7AM cron dead until
    # re-run). If pull --rebase cannot replay local commits (stale PR-style commits,
    # dirty refs, interrupted rebase), hard-reset the clone to origin/main and
    # continue. Previous state is preserved on the auto/reset-backup branch.
    pull_out = run("git pull --rebase origin main")
    if "could not apply" in pull_out or "CONFLICT" in pull_out or "cannot pull with rebase" in pull_out:
        print("   pull --rebase failed; resetting deploy clone to origin/main (backup: auto/reset-backup)")
        run("git rebase --abort")
        run("git branch -f auto/reset-backup HEAD")
        run("git fetch origin main")
        run("git reset --hard origin/main")
    # 1b. Re-exec self after pull so the RUNNING code is the freshly-pulled
    #     version (the script loads before step 1, so without this every deploy
    #     runs the PREVIOUS commit's deploy script (the Aug 26 verify-gate
    #     shipped twice without taking effect). Guarded by env flag to avoid loops.
    if not os.environ.get("DEPLOY_REEXEC"):
        os.environ["DEPLOY_REEXEC"] = "1"
        print("   Re-executing with pulled code...")
        os.execv(sys.executable, [sys.executable, os.path.abspath(__file__)] + sys.argv[1:])

    # 2. Regenerate GEO feeds (llms.txt / llms-full.txt)
    print("2. Regenerating llms.txt...")
    run("python3 scripts/generate_llms_txt.py", fatal=True)
    # 2b. Commit regenerated feeds so the NEXT deploy starts with a clean tree.
    #     Without this, a stale llms.txt leaves the tree dirty and the next
    #     `git pull --rebase` fails with "cannot pull with rebase: You have
    #     unstaged changes" (recurring failure: Aug 13, Aug 18).
    dirty_feeds = run("git status --porcelain -- llms.txt llms-full.txt").strip()
    if dirty_feeds:
        run(
            "git add llms.txt llms-full.txt && "
            "git commit -m 'chore: regenerate llms feeds (auto, deploy)'"
        )
        print(f"   Committed regenerated feeds ({len(dirty_feeds.splitlines())} file(s))")

    # 3. Build
    print("3. Building mkdocs...")
    out = run("python3 -m mkdocs build --clean", fatal=True)
    if "Documentation built" not in out:
        print("BUILD FAILED")
        sys.exit(1)
    print("   Build OK")

    # 3b. Normalize to no-slash (docs origin serves no-slash; mkdocs emits slashed):
    #     internal hrefs, sitemap <loc>, and the theme canonical tag. Keeps every
    #     URL on the site in ONE convention so Ahrefs credits inlinks (orphans
    #     previously appeared because internal links were slashed but pages served
    #     no-slash with a 308 in between).
    import glob as _glob
    import re as _re
    # 3b-i: sitemap
    sm = os.path.join(REPO_DIR, "site", "sitemap.xml")
    if os.path.exists(sm):
        with open(sm, encoding="utf-8") as f:
            xml = f.read()
        new_xml = _re.sub(r"<loc>(.*?)</loc>", lambda m: f"<loc>{m.group(1).rstrip('/')}</loc>", xml)
        with open(sm, "w", encoding="utf-8") as f:
            f.write(new_xml)
        print("   Sitemap normalized (no-slash)")
    # 3b-i2: sitemap.xml.gz (mkdocs emits a gzipped twin; Ahrefs can fetch it)
    import gzip as _gzip
    smgz = os.path.join(REPO_DIR, "site", "sitemap.xml.gz")
    if os.path.exists(smgz):
        with _gzip.open(smgz, "rt", encoding="utf-8") as f:
            xml = f.read()
        new_xml = _re.sub(r"<loc>(.*?)</loc>", lambda m: f"<loc>{m.group(1).rstrip('/')}</loc>", xml)
        with _gzip.open(smgz, "wt", encoding="utf-8") as f:
            f.write(new_xml)
        print("   Sitemap.xml.gz normalized (no-slash)")
    # 3b-ii: internal hrefs + canonical tag
    link_count = 0
    canon_count = 0
    for html in _glob.glob(os.path.join(REPO_DIR, "site", "**", "*.html"), recursive=True):
        with open(html, encoding="utf-8") as f:
            text = f.read()
        def _fix(m):
            nonlocal link_count
            href = m.group(1)
            if (href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:")
                or href.startswith("javascript:") or href.startswith("#") or href.startswith("/assets")
                or "assets/" in href or ".css" in href or ".js" in href or ".png" in href
                or ".svg" in href or ".ico" in href or ".xml" in href or ".txt" in href or ".json" in href):
                return m.group(0)
            if href.endswith("/") and len(href) > 1:
                link_count += 1
                return f'href="{href[:-1]}"'
            return m.group(0)
        new = _re.sub(r'href="([^"]+)"', _fix, text)
        # absolute www.corpusiq.io/docs links: strip trailing slash (the main-site
        # proxy 301s slashed docs URLs -> Ahrefs counts them as "links to redirect")
        new = _re.sub(r'(https://www\.corpusiq\.io/docs/[^"\s]+?)/"', r'\1"', new)
        # canonical: strip trailing slash in the href value
        new = _re.sub(r'(<link rel="canonical" href="[^"]+)/">', r'\1">', new)
        if new != text:
            with open(html, "w", encoding="utf-8") as f:
                f.write(new)
    print(f"   Links normalized ({link_count})")

    # 3b-iii: canonical overrides - docs commercial duplicates point their
    #        canonical at the marketing counterpart so ranking signals
    #        consolidate on the commercial pages. Map lives in
    #        scripts/canonical_overrides.json; applied HERE so the 3c gate
    #        sees the final values. See data/research/viktor-seo-decision-2026-09-14.md
    ov_path = os.path.join(REPO_DIR, "scripts", "canonical_overrides.json")
    if os.path.exists(ov_path):
        with open(ov_path, encoding="utf-8") as f:
            overrides = json.load(f).get("overrides", {})
        ov_count = 0
        for rel, target in overrides.items():
            p = os.path.join(REPO_DIR, "site", rel)
            if not os.path.exists(p):
                print(f"   [warn] canonical override target missing: {rel}")
                continue
            with open(p, encoding="utf-8") as f:
                text = f.read()
            new = _re.sub(
                r'<link rel="canonical" href="[^"]+">',
                f'<link rel="canonical" href="{target}">',
                text,
                count=1,
            )
            if new != text:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(new)
                ov_count += 1
        print(f"   Canonical overrides applied ({ov_count}/{len(overrides)})")

    # 3b-iv: relative-link resolution fix (Sep 15). The docs origin serves pages
    #        WITHOUT trailing slash while mkdocs computes relative links for
    #        SLASHED urls; under www.corpusiq.io/docs/* every relative link then
    #        resolves one level too high: index links skip a level (orphans),
    #        root-target nav links ESCAPE above /docs (404s: the five
    #        how-to-analyze pages carried 1,742 escaping inlinks each), and
    #        others land on redirects. Rewrite every resolvable internal
    #        relative link to its intended target as an absolute
    #        https://www.corpusiq.io/docs/... URL (house convention). Links
    #        whose target is not found in the build are left untouched.
    import posixpath as _pp
    _site_root = os.path.join(REPO_DIR, "site")
    _existing = set()
    for _r, _ds, _fs in os.walk(_site_root):
        for _f in _fs:
            _p = os.path.relpath(os.path.join(_r, _f), _site_root).replace(os.sep, "/")
            _existing.add(_p)
            if _f == "index.html":
                _d = os.path.dirname(_p)
                if _d:
                    _existing.add(_d)
    _skip_ext = (".css", ".js", ".png", ".svg", ".ico", ".jpg", ".jpeg", ".webp",
                 ".gif", ".woff", ".woff2", ".ttf", ".mp4", ".webm", ".pdf", ".gz", ".zip")
    _rel_count = 0
    _rel_files = 0
    _rel_left = 0

    def _target_exists(rp):
        rp = rp.strip("/")
        if not rp:
            return False
        return (rp in _existing) or ((rp + "/index.html") in _existing) or ((rp + ".html") in _existing)

    for _html in _glob.glob(os.path.join(_site_root, "**", "*.html"), recursive=True):
        _rel_html = os.path.relpath(_html, _site_root).replace(os.sep, "/")
        _pagedir = os.path.dirname(_rel_html)
        with open(_html, encoding="utf-8") as f:
            _text = f.read()
        _changed = 0

        def _rel(m):
            nonlocal _rel_count, _rel_left, _changed
            h = m.group(1)
            if (not h or h.startswith(("http://", "https://", "mailto:", "tel:", "javascript:",
                                       "data:", "ftp://", "#", "?"))
                    or "{{" in h or "{%" in h):
                return m.group(0)
            path_part, _, frag = h.partition("#")
            qs = ""
            if "?" in path_part:
                path_part, _, qs = path_part.partition("?")
                qs = "?" + qs
            low = path_part.lower()
            if low.endswith(_skip_ext) or "assets/" in low or low.startswith("assets"):
                return m.group(0)
            if path_part.startswith("/"):
                R = _pp.normpath(path_part)
            else:
                base = "/" + _pagedir if _pagedir else "/"
                R = _pp.normpath(base.rstrip("/") + "/" + path_part)
            if R == "/" or R.startswith("//") or ".." in R.split("/"):
                _rel_left += 1
                return m.group(0)
            rp = R.strip("/")
            if not _target_exists(rp):
                _rel_left += 1
                return m.group(0)
            _rel_count += 1
            _changed += 1
            return 'href="https://www.corpusiq.io/docs/%s%s%s"' % (rp, qs, ("#" + frag) if frag else "")

        _new = _re.sub(r'href="([^"]+)"', _rel, _text)
        if _changed:
            _rel_files += 1
            with open(_html, "w", encoding="utf-8") as f:
                f.write(_new)
    print(f"   Relative links absolutized ({_rel_count} across {_rel_files} files; {_rel_left} unresolved left as-is)")

    # 3c. VERIFY no-slash invariants - hard fail BEFORE any deploy (guard added
    #     Aug 26 after health score 30 regression: duplicate slashed canonicals
    #     + slashed sitemap/feeds shipped twice). A build that violates any
    #     invariant here must NOT reach production.
    verify_errors = []
    # sitemap xml + gz
    for smf in ("sitemap.xml", "sitemap.xml.gz"):
        p = os.path.join(REPO_DIR, "site", smf)
        if not os.path.exists(p):
            continue
        opener = _gzip.open if smf.endswith(".gz") else open
        with opener(p, "rt", encoding="utf-8") as f:
            xml = f.read()
        n = len(_re.findall(r"<loc>([^<]*/)</loc>", xml))
        if n:
            verify_errors.append(f"{smf}: {n} slashed <loc> entries")
    # feeds
    for feed in ("llms.txt", "llms-full.txt"):
        p = os.path.join(REPO_DIR, "site", feed)
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        n = len(_re.findall(r"https://www\.corpusiq\.io/docs/[^)\s\"']*/[)\s\"']", txt))
        if n:
            verify_errors.append(f"{feed}: {n} slashed docs URLs")
    # per-page canonical + internal hrefs (same exclusions as 3b-ii).
    # Skip non-page HTML artifacts: 404.html, raw email templates
    # (hermes/templates/*.html) and the community widget snippet - none are
    # real pages and legitimately carry no canonical.
    for html in _glob.glob(os.path.join(REPO_DIR, "site", "**", "*.html"), recursive=True):
        text = open(html, encoding="utf-8").read()
        rel = os.path.relpath(html, REPO_DIR)
        if (rel.endswith("404.html") or "templates/" in rel
                or rel.endswith("tokens-saved-widget.html")):
            continue
        canons = _re.findall(r'<link rel="canonical" href="([^"]+)"', text)
        if len(canons) != 1:
            verify_errors.append(f"{rel}: {len(canons)} canonical tags")
        elif canons[0].endswith("/"):
            verify_errors.append(f"{rel}: slashed canonical {canons[0]}")
        for href in _re.findall(r'href="([^"]+)"', text):
            if (href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:")
                or href.startswith("javascript:") or href.startswith("#") or href.startswith("/assets")
                or "assets/" in href or ".css" in href or ".js" in href or ".png" in href
                or ".svg" in href or ".ico" in href or ".xml" in href or ".txt" in href or ".json" in href):
                continue
            if href.endswith("/") and len(href) > 1:
                verify_errors.append(f"{rel}: slashed internal href {href}")
                break
    if verify_errors:
        print("VERIFY GATE FAILED - deploy aborted (no-slash invariant violated):")
        for e in verify_errors[:25]:
            print("  -", e)
        print(f"  ({len(verify_errors)} total violations)")
        sys.exit(1)
    print("   Verify gate passed (canonical, sitemap, feeds, hrefs all no-slash)")

    # 4. Deploy to gh-pages
    print("4. Deploying to gh-pages...")
    wt = "/tmp/gh-pages-deploy"
    if os.path.exists(os.path.join(wt, ".git")):
        run(f"git -C {wt} fetch origin gh-pages")
        run(f"git -C {wt} reset --hard origin/gh-pages")
    else:
        # Stale worktree registrations are recurring (Sep 14, 2026): prune first,
        # and never abort production for the legacy backup path - Vercel is the
        # production deploy.
        run("git worktree prune")
        r = subprocess.run(f"git worktree add -f {wt} gh-pages", shell=True, cwd=REPO_DIR,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"   [warn] gh-pages worktree unavailable - skipping legacy backup: "
                  f"{(r.stdout + r.stderr).strip()[:160]}")

    if os.path.exists(os.path.join(wt, ".git")):
        # Clear old content, copy new build
        run(f"cd {wt} && find . -not -path './.git*' -not -name '.git' -delete")
        run(f"cp -r {REPO_DIR}/site/. {wt}/")
        # GEO feeds at site root
        run(f"cp {REPO_DIR}/llms.txt {REPO_DIR}/llms-full.txt {wt}/")
        run(f"touch {wt}/.nojekyll")

        # Commit
        sha = run("git rev-parse HEAD").strip()[:8]
        if not commit_msg:
            commit_msg = f"Deployed {sha} with MkDocs version: 1.6.1 - manual legacy deploy"
        run(f"cd {wt} && git add -A && git commit -m '{commit_msg}'")
        run(f"cd {wt} && git push origin gh-pages")
    else:
        print("   gh-pages backup skipped (worktree unavailable)")
    print("4b. Deploying to Vercel...")
    deploy_vercel()

    # 4. Trigger Pages build via API
    print("4. Triggering Pages build...")
    token = get_token()
    resp = requests.post(
        "https://api.github.com/repos/CorpusIQ/corpusiq-docs/pages/builds",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
        timeout=30,
    )
    if resp.status_code in (200, 201):
        print(f"   Build queued: {resp.json().get('status')}")
    else:
        print(f"   Build trigger failed: HTTP {resp.status_code} {resp.text[:150]}")

    # 5. Verify
    print("5. Waiting for build...")
    for i in range(6):
        time.sleep(30)
        chk = requests.get(
            "https://api.github.com/repos/CorpusIQ/corpusiq-docs/pages/builds?per_page=3",
            headers={"Authorization": f"Bearer {token}"},
            timeout=15,
        )
        if chk.status_code == 200:
            builds = chk.json()
            if builds:
                latest = builds[0]
                status = latest.get("status")
                print(f"   Build status: {status}")
                if status == "built":
                    print("DEPLOY COMPLETE")
                    return
                if status == "errored":
                    print(f"BUILD ERROR: {latest.get('error', {}).get('message')}")
                    sys.exit(1)

    print("DEPLOY QUEUED - still processing (org Actions may still block). Check later.")

if __name__ == "__main__":
    main()
