#!/usr/bin/env python3
"""Writes the README's package table from index.yaml.

The table sits between the two marker comments in README.md. index.yaml is the
source: add, bump or describe a package there and run this script.

    python3 tools/readme-packages-table.py          # rewrite README.md
    python3 tools/readme-packages-table.py --check  # fail if README.md is out of date
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
INDEX = ROOT / "index.yaml"
BEGIN = "<!-- packages-table:begin (generated from index.yaml by tools/readme-packages-table.py) -->"
END = "<!-- packages-table:end -->"


def cell(text):
	return " ".join(str(text).split()).replace("|", "\\|")


def table():
	index = yaml.safe_load(INDEX.read_text(encoding="utf-8"))
	rows = ["| Package | Version | Description |", "|---|---|---|"]
	for entry in index["packages"]:
		path = entry["path"]
		rows.append(f"| [`{path}`]({path}) | {cell(entry['version'])} | {cell(entry['description'])} |")
	return "\n".join(rows)


def render(readme):
	start = readme.find(BEGIN)
	stop = readme.find(END)
	if start < 0 or stop < start:
		sys.exit(f"README.md: the markers {BEGIN!r} and {END!r} are missing or out of order.")
	return readme[: start + len(BEGIN)] + "\n" + table() + "\n" + readme[stop:]


def main():
	current = README.read_text(encoding="utf-8")
	wanted = render(current)
	if "--check" in sys.argv[1:]:
		if current != wanted:
			print("::error file=README.md::The package table is out of date. Run: python3 tools/readme-packages-table.py")
			return 1
		print("README package table matches index.yaml.")
		return 0
	if current != wanted:
		README.write_text(wanted, encoding="utf-8")
		print("README.md updated.")
	return 0


if __name__ == "__main__":
	sys.exit(main())
