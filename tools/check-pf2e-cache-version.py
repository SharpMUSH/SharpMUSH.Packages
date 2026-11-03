#!/usr/bin/env python3
"""pf2e keys its derived-sheet cache on DATA`CACHE`VERSION, so a new version of the package works
every sheet out again. The value has to follow the package's version.

Run from the package repository: python3 tools/check-pf2e-cache-version.py
"""
from pathlib import Path
import re
import sys

text = (Path(__file__).resolve().parents[1] / "pf2e" / "package.yaml").read_text(encoding="utf-8")
version = re.search(r'^version: "([^"]+)"', text, re.M)
cache = re.search(r'^\s+DATA`CACHE`VERSION: "([^"]+)"', text, re.M)
if not version or not cache:
    print("pf2e/package.yaml: version or DATA`CACHE`VERSION missing", file=sys.stderr)
    raise SystemExit(1)
if version[1] != cache[1]:
    print(f"pf2e/package.yaml: DATA`CACHE`VERSION is {cache[1]}, the package is {version[1]}; set it to {version[1]}", file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: pf2e cache version {cache[1]}")
