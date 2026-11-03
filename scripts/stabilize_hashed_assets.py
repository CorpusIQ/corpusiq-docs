#!/usr/bin/env python3
"""Stabilize hashed MkDocs asset names and hard-verify references.

MkDocs Material emits content-hashed CSS and JavaScript asset names and
removes older hashes on each build. If cached HTML remains at the edge after
deploy, that HTML can still reference older hashes that no longer exist,
causing site-wide broken CSS or JavaScript reports. This script writes stable
unhashed sibling files and rewrites hashed references to use `?v=<hash>` so
cached HTML keeps loading resolvable assets.

Usage:
    python scripts/stabilize_hashed_assets.py [site_dir] [--check]

Exit 0 = stable
Exit 1 = change required in --check mode, missing hashed HTML reference, or
         processing failure
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import posixpath
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


HASHED_FILENAME_RE = re.compile(
    r"^(?P<stem>.+)\.(?P<hash>[0-9a-f]{6,32})(?P<min>\.min)?\.(?P<ext>css|js|woff2|woff|ttf)$"
)

HASHED_REF_VALUE_RE = re.compile(
    r"^(?P<prefix>.+?)\.(?P<hash>[0-9a-f]{6,32})(?P<min>\.min)?\.(?P<ext>css|js)"
    r"(?:\?[^#]*)?(?P<fragment>#.*)?$"
)

STABLE_PATH_RE = re.compile(r"\.[0-9a-f]{6,32}(?P<min>\.min)?\.(?P<ext>css|js)$")
QUOTED_REF_RE = re.compile(r"(?P<quote>['\"])(?P<ref>[^'\"]+)(?P=quote)")
URL_REF_RE = re.compile(r"url\((?P<quote>['\"]?)(?P<ref>[^)'\"]+)(?P=quote)\)")

TEXT_SUFFIXES = {".html", ".css", ".js", ".json", ".xml", ".webmanifest", ".txt"}
LOCAL_HOSTS = {"www.corpusiq.io", "docs.corpusiq.io", "corpusiq.github.io"}


@dataclass(frozen=True)
class AssetRecord:
    hashed_rel: str
    stable_rel: str
    hash_value: str


@dataclass
class AssetMetrics:
    copies_written: int = 0
    references_rewritten: int = 0


@dataclass
class Summary:
    stable_copies_written: int
    references_rewritten: int
    files_touched: int
    metrics: dict[str, AssetMetrics]


class MissingHashedAssetReference(Exception):
    def __init__(self, file_rel: str, reference: str):
        super().__init__(f"{file_rel}: {reference}")
        self.file_rel = file_rel
        self.reference = reference


def _to_posix(path: Path) -> str:
    return path.as_posix()


def _split_ref(ref: str) -> tuple[str, str]:
    fragment = ""
    without_fragment = ref
    if "#" in ref:
        without_fragment, frag = ref.split("#", 1)
        fragment = f"#{frag}"
    path_only = without_fragment.split("?", 1)[0]
    return path_only, fragment


def _is_local_reference(path_only: str) -> bool:
    if path_only.startswith("//"):
        return False
    if path_only.startswith(("http://", "https://")):
        host = urlsplit(path_only).hostname or ""
        return host.lower() in LOCAL_HOSTS
    return True


def _resolve_site_rel(ref_path: str, source_rel: str) -> str | None:
    path_value = ref_path
    if ref_path.startswith(("http://", "https://")):
        path_value = urlsplit(ref_path).path
    if not path_value:
        return None

    if path_value.startswith("/docs/"):
        rel = path_value[len("/docs/") :]
    elif path_value.startswith("/"):
        rel = path_value[1:]
    else:
        base = posixpath.dirname(source_rel)
        rel = posixpath.normpath(posixpath.join(base, path_value))

    if rel in {"", "."}:
        return None
    rel = posixpath.normpath(rel)
    if rel.startswith("../") or rel == "..":
        return None
    return rel


def _stable_rel_from_hashed_rel(hashed_rel: str) -> str:
    match = STABLE_PATH_RE.search(hashed_rel)
    if not match:
        return hashed_rel
    min_part = match.group("min") or ""
    ext = match.group("ext")
    return f"{hashed_rel[:match.start()]}{min_part}.{ext}"


def _discover_assets(site_dir: Path) -> list[AssetRecord]:
    assets: list[AssetRecord] = []
    for path in sorted(site_dir.rglob("*")):
        if not path.is_file():
            continue
        rel_path = path.relative_to(site_dir)
        if "assets" not in rel_path.parts:
            continue
        match = HASHED_FILENAME_RE.match(path.name)
        if not match:
            continue
        min_part = match.group("min") or ""
        stable_name = f"{match.group('stem')}{min_part}.{match.group('ext')}"
        assets.append(
            AssetRecord(
                hashed_rel=_to_posix(rel_path),
                stable_rel=_to_posix(rel_path.with_name(stable_name)),
                hash_value=match.group("hash"),
            )
        )
    return assets


def _write_stable_copies(
    site_dir: Path,
    assets: list[AssetRecord],
    metrics: dict[str, AssetMetrics],
    *,
    check: bool,
) -> tuple[int, set[str]]:
    written = 0
    written_or_would_write: set[str] = set()
    for asset in assets:
        source = site_dir / asset.hashed_rel
        target = site_dir / asset.stable_rel
        source_bytes = source.read_bytes()
        same = target.exists() and target.read_bytes() == source_bytes
        if same:
            continue
        written += 1
        written_or_would_write.add(asset.stable_rel)
        metrics[asset.hashed_rel].copies_written += 1
        if not check:
            target.write_bytes(source_bytes)
    return written, written_or_would_write


def _read_text(path: Path, site_dir: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # pragma: no cover - exercised by integration failures.
        rel = _to_posix(path.relative_to(site_dir))
        raise RuntimeError(f"Failed to read {rel}: {exc}") from exc


def _rewrite_references(
    site_dir: Path,
    assets: list[AssetRecord],
    metrics: dict[str, AssetMetrics],
    stable_written_or_would_write: set[str],
    *,
    check: bool,
) -> tuple[int, int]:
    refs_rewritten = 0
    files_touched = 0

    assets_by_hashed = {asset.hashed_rel: asset for asset in assets}
    assets_by_stable: dict[str, list[AssetRecord]] = {}
    for asset in assets:
        assets_by_stable.setdefault(asset.stable_rel, []).append(asset)

    for path in sorted(site_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel_file = _to_posix(path.relative_to(site_dir))
        original = _read_text(path, site_dir)

        file_refs = 0

        def rewrite_one_reference(ref: str) -> str:
            nonlocal refs_rewritten, file_refs
            match = HASHED_REF_VALUE_RE.match(ref)
            if not match:
                return ref

            prefix = match.group("prefix")
            hash_value = match.group("hash")
            min_part = match.group("min") or ""
            ext = match.group("ext")
            fragment = match.group("fragment") or ""
            path_only, _ = _split_ref(ref)

            if not _is_local_reference(path_only):
                return ref

            resolved_hashed_rel = _resolve_site_rel(path_only, rel_file)
            if not resolved_hashed_rel:
                return ref
            if "assets/" not in f"{resolved_hashed_rel}/" and not resolved_hashed_rel.startswith("assets"):
                return ref

            stable_ref = f"{prefix}{min_part}.{ext}?v={hash_value}{fragment}"
            resolved_stable_rel = _stable_rel_from_hashed_rel(resolved_hashed_rel)
            hashed_exists = (site_dir / resolved_hashed_rel).exists()
            stable_written_now = resolved_stable_rel in stable_written_or_would_write

            if rel_file.endswith(".html") and not hashed_exists and not stable_written_now:
                raise MissingHashedAssetReference(rel_file, ref)

            asset = assets_by_hashed.get(resolved_hashed_rel)
            if asset is None:
                stable_candidates = assets_by_stable.get(resolved_stable_rel, [])
                if stable_candidates:
                    asset = stable_candidates[0]
            if asset is not None and stable_ref != ref:
                metrics[asset.hashed_rel].references_rewritten += 1

            if stable_ref != ref:
                refs_rewritten += 1
                file_refs += 1

            return stable_ref

        def replace_quoted(match: re.Match[str]) -> str:
            quote = match.group("quote")
            ref = match.group("ref")
            return f"{quote}{rewrite_one_reference(ref)}{quote}"

        def replace_url(match: re.Match[str]) -> str:
            quote = match.group("quote")
            ref = match.group("ref")
            return f"url({quote}{rewrite_one_reference(ref)}{quote})"

        updated = QUOTED_REF_RE.sub(replace_quoted, original)
        updated = URL_REF_RE.sub(replace_url, updated)
        if updated != original:
            files_touched += 1
            if not check:
                path.write_text(updated, encoding="utf-8")

    return refs_rewritten, files_touched


def stabilize_hashed_assets(site_dir: Path, *, check: bool) -> Summary:
    if not site_dir.exists() or not site_dir.is_dir():
        raise RuntimeError(f"Site directory not found: {site_dir}")

    assets = _discover_assets(site_dir)
    metrics = {asset.hashed_rel: AssetMetrics() for asset in assets}

    copies_written, stable_written_or_would_write = _write_stable_copies(
        site_dir,
        assets,
        metrics,
        check=check,
    )
    refs_rewritten, files_touched = _rewrite_references(
        site_dir,
        assets,
        metrics,
        stable_written_or_would_write,
        check=check,
    )

    return Summary(
        stable_copies_written=copies_written,
        references_rewritten=refs_rewritten,
        files_touched=files_touched,
        metrics=metrics,
    )


def _print_summary(summary: Summary, *, check: bool) -> None:
    copies_label = "Stable copies to write" if check else "Stable copies written"
    refs_label = "References to rewrite" if check else "References rewritten"
    files_label = "Files to touch" if check else "Files touched"

    print(f"{copies_label}: {summary.stable_copies_written}")
    print(f"{refs_label}: {summary.references_rewritten}")
    print(f"{files_label}: {summary.files_touched}")
    print("Per-asset:")

    for hashed_rel in sorted(summary.metrics):
        metric = summary.metrics[hashed_rel]
        stable_rel = _stable_rel_from_hashed_rel(hashed_rel)
        hash_match = HASHED_FILENAME_RE.match(Path(hashed_rel).name)
        hash_value = hash_match.group("hash") if hash_match else "unknown"
        print(
            "  {} -> {} | hash={} | copies={} | refs={}".format(
                hashed_rel,
                stable_rel,
                hash_value,
                metric.copies_written,
                metric.references_rewritten,
            )
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", nargs="?", default="site")
    parser.add_argument("--check", action="store_true", help="Report drift without modifying files")
    args = parser.parse_args(argv)

    site_dir = Path(args.site_dir)
    try:
        summary = stabilize_hashed_assets(site_dir, check=args.check)
    except MissingHashedAssetReference as exc:
        print(
            f"ERROR: missing hashed asset reference in {exc.file_rel}: {exc.reference}",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    _print_summary(summary, check=args.check)
    has_changes = summary.stable_copies_written > 0 or summary.references_rewritten > 0
    if args.check and has_changes:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

