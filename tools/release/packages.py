#!/usr/bin/env python3
"""Release tooling for the package repository.

A package is a top-level directory holding a package.yaml. Its release tag is
<directory>/v<version>, the name SharpMUSH's Git package source looks for.

  check-bumps BASE HEAD   Fail when a package changed between BASE and HEAD
                          (merge-base diff, as a pull request shows it) without
                          a higher version, or when its new version is already tagged.
  pending-tags            Print "<tag> <commit>" for every package version on HEAD
                          that has no tag yet. The commit is the last one that
                          touched the package's directory, so a version is tagged
                          where its content was last changed. Exits 1 when a tagged
                          version's directory changed after its tag.

Run from the repository root with the tags fetched (git fetch --tags).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

VERSION_LINE = re.compile(r'^version:\s*["\']?([^"\'\s#]+)', re.M)
VERSION = re.compile(r"^([0-9]+)(?:\.([0-9]+))?(?:\.([0-9]+))?(?:-(.+))?$")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def parse(text: str) -> tuple[int, int, int, str | None] | None:
    """The engine's PackageVersion: 1-3 numeric components, optional -prerelease."""
    match = VERSION.match(text.strip())
    if not match:
        return None
    return int(match[1]), int(match[2] or 0), int(match[3] or 0), match[4]


def normalized(version: tuple[int, int, int, str | None]) -> str:
    major, minor, patch, pre = version
    return f"{major}.{minor}.{patch}" + (f"-{pre}" if pre else "")


def compare(a: tuple[int, int, int, str | None], b: tuple[int, int, int, str | None]) -> int:
    """SemVer 2.0.0 precedence, matching PackageVersion.CompareTo."""
    if a[:3] != b[:3]:
        return -1 if a[:3] < b[:3] else 1
    pa, pb = a[3], b[3]
    if pa == pb:
        return 0
    if pa is None:
        return 1
    if pb is None:
        return -1
    for x, y in zip(pa.split("."), pb.split(".")):
        if x == y:
            continue
        xn, yn = x.isascii() and x.isdigit(), y.isascii() and y.isdigit()
        if xn and yn:
            return -1 if int(x) < int(y) else 1
        if xn != yn:
            return -1 if xn else 1
        return -1 if x < y else 1
    la, lb = len(pa.split(".")), len(pb.split("."))
    return (la > lb) - (la < lb)


def version_at(ref: str, directory: str) -> str | None:
    """The raw version string in <directory>/package.yaml at ref, or None when there is no manifest."""
    try:
        text = git("show", f"{ref}:{directory}/package.yaml")
    except subprocess.CalledProcessError:
        return None
    match = VERSION_LINE.search(text)
    return match[1] if match else ""


def tags() -> set[str]:
    return set(git("tag", "--list", "*/v*").split())


def check_bumps(base: str, head: str) -> int:
    # --no-renames: a file moved out of a package changes that package too.
    changed = [p for p in git("diff", "--name-only", "--no-renames", "-z", f"{base}...{head}").split("\0") if p]
    directories = sorted({path.split("/", 1)[0] for path in changed if "/" in path})
    merge_base = git("merge-base", base, head).strip()
    existing = tags()
    failures = []
    checked = 0
    for directory in directories:
        after_text = version_at(head, directory)
        if after_text is None:
            continue  # not a package on HEAD (removed, or not a package directory)
        checked += 1
        after = parse(after_text)
        if after is None:
            failures.append(f"{directory}: version '{after_text}' is not a package version")
            continue
        tag = f"{directory}/v{normalized(after)}"
        before_text = version_at(merge_base, directory)
        if before_text is None:
            if tag in existing:
                failures.append(f"{directory}: new package, but {tag} already exists")
            else:
                print(f"OK    {directory}: new package at {normalized(after)}")
            continue
        before = parse(before_text)
        if before is not None and compare(after, before) <= 0:
            failures.append(
                f"{directory}: files changed but the version is still {before_text}; "
                f"raise version in {directory}/package.yaml and index.yaml")
        elif tag in existing:
            failures.append(f"{directory}: {tag} already exists; choose a version above every released one")
        else:
            print(f"OK    {directory}: {before_text} -> {normalized(after)}")
    for failure in failures:
        print(f"ERROR {failure}")
        print(f"::error::{failure}")
    print(f"{checked} changed package(s), {len(failures)} without a new version.")
    return 1 if failures else 0


def pending_tags() -> int:
    existing = tags()
    drift = 0
    for manifest in sorted(Path(".").glob("*/package.yaml")):
        directory = manifest.parent.name
        match = VERSION_LINE.search(manifest.read_text(encoding="utf-8"))
        version = parse(match[1]) if match else None
        if version is None:
            print(f"::warning::{directory}: no package version; not tagged", file=sys.stderr)
            continue
        tag = f"{directory}/v{normalized(version)}"
        last = git("log", "-1", "--format=%H", "--", directory).strip()
        if tag not in existing:
            print(f"{tag} {last}")
        elif git("rev-parse", f"{tag}:{directory}") != git("rev-parse", f"HEAD:{directory}"):
            print(f"::error::{directory} changed after {tag} without a new version; raise its version", file=sys.stderr)
            drift += 1
    return 1 if drift else 0


def main(argv: list[str]) -> int:
    match argv:
        case ["check-bumps", base, head]:
            return check_bumps(base, head)
        case ["pending-tags"]:
            return pending_tags()
        case _:
            print(__doc__, file=sys.stderr)
            return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
