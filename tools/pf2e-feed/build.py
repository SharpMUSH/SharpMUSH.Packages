"""Builds the PF2e feed from a checkout of the Foundry VTT pf2e system.

	python3 -I build.py <foundry-pf2e-checkout> <feed-dir> [--write]

Without --write it reads everything and prints what it would write. The feed holds every item of the
reviewed books in books.json whose publication licence is ORC, as Foundry wrote it, less image paths
and sort order, with Reserved Material reworded, cut or dropped (reserved.py). Everything read is data.

Feed layout:
	index.json                     Foundry commit, books, the files of each book with item counts and hashes
	items/<book>/<pack>-<n>.txt    one item per line: <_id> <hash> <json>, at most MAX_FILE bytes a file
	reports/reserved.md            what the Reserved Material screening did, item by item
	reports/rules.md               rule element kinds and the items carrying them; what the licence filter left out
	corpus/predicates.txt          every distinct rule element predicate, one JSON value a line
	corpus/formulas.txt            every distinct rule element formula string
"""
import collections
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # python3 -I leaves the script's own folder off the path

import reserved  # noqa: E402
MAX_FILE = 256 * 1024
STRIP = {"img", "sort", "folder", "ownership", "_stats"}
PROSE = {"publicNotes", "privateNotes", "blurb", "description", "disable", "reset", "routine"}
LANG_KEY = re.compile(r"^PF2E\.[A-Za-z0-9_.-]+$")
LANG_FILES = ["en.json", "action-en.json", "re-en.json"]


def canonical(value):
	return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=False)


def publication(item):
	system = item.get("system") or {}
	return system.get("publication") or (system.get("details") or {}).get("publication") or {}


def strip(value):
	if isinstance(value, dict):
		return {k: strip(v) for k, v in value.items() if k not in STRIP}
	if isinstance(value, list):
		return [strip(v) for v in value]
	return value


def pack_items(foundry, pack):
	root = os.path.join(foundry, "packs", "pf2e", pack)
	for path in sorted(glob.glob(os.path.join(root, "**", "*.json"), recursive=True)):
		if os.path.basename(path) == "_folders.json":
			continue
		with open(path, encoding="utf-8") as f:
			data = json.load(f)
		if isinstance(data, dict) and "_id" in data:
			yield data


def deity_names(foundry):
	return sorted({d["name"] for d in pack_items(foundry, "deities")})


class Screen:
	"""Applies reserved.py to an item and every item embedded in it, and records what it did."""

	def __init__(self):
		self.rows = []

	def prose(self, owner, node, path=()):
		"""Rewords every description and note under node, in place."""
		if isinstance(node, dict):
			for key, value in node.items():
				if key == "description" and isinstance(value, dict) and isinstance(value.get("value"), str):
					value["value"], how = reserved.reword(owner, value["value"])
					if how:
						self.rows.append((owner, "/".join(path + (key,)), how))
				elif key in PROSE and isinstance(value, str):
					node[key], how = reserved.reword(owner, value)
					if how:
						self.rows.append((owner, "/".join(path + (key,)), how))
				elif isinstance(value, str):
					node[key] = reserved.text(value)
				elif key != "publication":
					self.prose(owner, value, path + (key,))
		elif isinstance(node, list):
			for i, value in enumerate(node):
				if isinstance(value, str):
					node[i] = reserved.text(value)
				else:
					self.prose(owner, value, path + (str(i),))

	def item(self, item):
		"""The screened item, or None when it is dropped."""
		name = item["name"]
		if name in reserved.DROP:
			self.rows.append((name, "", [f"dropped: {reserved.DROP[name]}"]))
			return None
		if reserved.hits(name):
			self.rows.append((name, "", [f"dropped: named for {', '.join(reserved.hits(name))}"]))
			return None
		kept = []
		for embedded in item.get("items") or []:
			if isinstance(embedded.get("name"), str):
				embedded["name"] = reserved.text(embedded["name"])
			if reserved.hits(embedded.get("name", "")) or embedded.get("name") in reserved.DROP:
				self.rows.append((name, f"items/{embedded.get('name')}", ["embedded item dropped: named for a reserved term"]))
				continue
			kept.append(embedded)
		if "items" in item:
			item["items"] = kept
		self.prose(name, item)
		return item


def without_publication(value):
	if isinstance(value, dict):
		return {k: without_publication(v) for k, v in value.items() if k != "publication"}
	if isinstance(value, list):
		return [without_publication(v) for v in value]
	return value


def strings(value):
	if isinstance(value, dict):
		for v in value.values():
			yield from strings(v)
	elif isinstance(value, list):
		for v in value:
			yield from strings(v)
	elif isinstance(value, str):
		yield value


def left_over(item):
	"""Reserved terms still in the item outside its publication records and language keys."""
	return reserved.hits("\n".join(s for s in strings(without_publication(item)) if not LANG_KEY.match(s)))


def load_lang(foundry):
	"""Foundry's English strings, flattened to dotted keys; later files win, as the system loads them."""
	flat = {}

	def walk(node, prefix):
		for k, v in node.items():
			key = f"{prefix}.{k}" if prefix else k
			if isinstance(v, dict):
				walk(v, key)
			elif isinstance(v, str):
				flat[key] = v
	for name in LANG_FILES:
		with open(os.path.join(foundry, "static", "lang", name), encoding="utf-8") as f:
			walk(json.load(f), "")
	return flat


def walk_rules(item):
	for rule in (item.get("system") or {}).get("rules") or []:
		if isinstance(rule, dict):
			yield rule
	for embedded in item.get("items") or []:
		yield from walk_rules(embedded)


FORMULA = re.compile(r"@|\b(?:floor|ceil|max|min|ternary|lte|gte|lt|gt|eq)\(")


def formulas(value):
	if isinstance(value, str):
		if FORMULA.search(value):
			yield value
	elif isinstance(value, dict):
		for k, v in value.items():
			if k != "predicate":
				yield from formulas(v)
	elif isinstance(value, list):
		for v in value:
			yield from formulas(v)


def build(foundry, books_file):
	with open(books_file, encoding="utf-8") as f:
		config = json.load(f)
	books = {b["title"]: b for b in config["books"] if b["reviewed"]}
	reserved.configure(deity_names(foundry))
	screen = Screen()
	kept = collections.defaultdict(list)
	excluded = collections.Counter()
	rule_kinds = collections.Counter()
	rule_items = collections.Counter()
	predicates, formula_set, left, keys = set(), set(), [], set()
	for pack in config["packs"]:
		for item in pack_items(foundry, pack):
			pub = publication(item)
			book = books.get(pub.get("title"))
			if pub.get("license") != "ORC" or book is None:
				excluded[(pub.get("license") or "none", pub.get("title") or "no book")] += 1
				continue
			item = screen.item(strip(item))
			if item is None:
				continue
			keys.update(s for s in strings(item) if LANG_KEY.match(s))
			found = left_over(item)
			if found:
				left.append((item["name"], found))
			seen = set()
			for rule in walk_rules(item):
				kind = rule.get("key", "?")
				rule_kinds[kind] += 1
				seen.add(kind)
				if "predicate" in rule:
					predicates.add(canonical(rule["predicate"]))
				formula_set.update(formulas(rule))
			for kind in seen:
				rule_items[kind] += 1
			kept[(book["slug"], pack)].append(item)
	strings_en = load_lang(foundry)
	lang, missing = {}, []
	for key in sorted(keys):
		if key not in strings_en:
			missing.append(key)
			continue
		value = reserved.text(strings_en[key])
		if reserved.hits(value):
			left.append((key, reserved.hits(value)))
		lang[key] = value
	return config, kept, excluded, rule_kinds, rule_items, predicates, formula_set, screen.rows, left, lang, missing


def item_line(item):
	body = canonical(item)
	digest = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
	return f"{item['_id']} {digest} {body}\n"


def chunks(lines):
	"""Lines grouped into files of at most MAX_FILE bytes (a longer line gets a file of its own)."""
	group, size = [], 0
	for line in lines:
		n = len(line.encode("utf-8"))
		if group and size + n > MAX_FILE:
			yield group
			group, size = [], 0
		group.append(line)
		size += n
	if group:
		yield group


def commit_of(foundry):
	run = lambda *a: subprocess.run(["git", "-C", foundry, *a], capture_output=True, text=True, check=True).stdout.strip()
	return run("rev-parse", "HEAD"), run("log", "-1", "--format=%cI")


def write(out, foundry, result):
	config, kept, excluded, rule_kinds, rule_items, predicates, formula_set, rows, left, lang, missing = result
	commit, committed = commit_of(foundry)
	for sub in ("items", "reports", "corpus"):
		shutil.rmtree(os.path.join(out, sub), ignore_errors=True)
	index_books = []
	for book in config["books"]:
		if not book["reviewed"]:
			continue
		files = []
		for pack in config["packs"]:
			items = sorted(kept.get((book["slug"], pack), []), key=lambda i: i["_id"])
			for n, group in enumerate(chunks(item_line(i) for i in items), start=1):
				rel = f"items/{book['slug']}/{pack}-{n}.txt"
				path = os.path.join(out, rel)
				os.makedirs(os.path.dirname(path), exist_ok=True)
				data = "".join(group)
				with open(path, "w", encoding="utf-8", newline="\n") as f:
					f.write(data)
				files.append({"path": rel, "pack": pack, "items": len(group),
					"bytes": len(data.encode("utf-8")), "hash": hashlib.sha256(data.encode("utf-8")).hexdigest()[:16]})
		index_books.append({"slug": book["slug"], "name": book["name"], "title": book["title"], "default": book["default"],
			"items": sum(f["items"] for f in files), "files": files})
	index = {"format": 1, "foundry": {"repository": "https://github.com/foundryvtt/pf2e", "commit": commit, "committed": committed},
		"licence": "ORC", "books": index_books}
	with open(os.path.join(out, "lang.json"), "w", encoding="utf-8", newline="\n") as f:
		f.write(json.dumps(lang, indent="\t", ensure_ascii=False, sort_keys=True) + "\n")
	with open(os.path.join(out, "index.json"), "w", encoding="utf-8", newline="\n") as f:
		f.write(json.dumps(index, indent="\t", ensure_ascii=False) + "\n")
	os.makedirs(os.path.join(out, "reports"), exist_ok=True)
	os.makedirs(os.path.join(out, "corpus"), exist_ok=True)
	with open(os.path.join(out, "corpus", "predicates.txt"), "w", encoding="utf-8", newline="\n") as f:
		f.write("".join(p + "\n" for p in sorted(predicates)))
	with open(os.path.join(out, "corpus", "formulas.txt"), "w", encoding="utf-8", newline="\n") as f:
		f.write("".join(s.replace("\n", " ") + "\n" for s in sorted(formula_set)))
	write_reserved(os.path.join(out, "reports", "reserved.md"), commit, rows, left)
	write_rules(os.path.join(out, "reports", "rules.md"), commit, rule_kinds, rule_items, excluded)
	return index


def write_reserved(path, commit, rows, left):
	dropped = [r for r in rows if r[2][0].startswith("dropped")]
	embedded = [r for r in rows if r[2][0].startswith("embedded")]
	unreviewed = [r for r in rows if any("not yet reviewed" in h for h in r[2])]
	other = [r for r in rows if r not in dropped and r not in embedded and r not in unreviewed]
	lines = ["# Reserved Material report", "", f"Foundry pf2e commit `{commit}`.", "",
		"The ORC License does not license Paizo's proper nouns: deities, places, organizations, planes, named characters.",
		"Terms matched: every deity in the Foundry deities pack (less a few ordinary words) and the setting list in",
		"`tools/pf2e-feed/reserved.py`. Items under \"Not yet reviewed\" had sentences cut by the general rule; a reviewer",
		"either accepts the cut or adds a rewording to `reserved.py`.", "",
		f"## Dropped ({len(dropped)})", ""]
	lines += [f"- **{n}**: {h[0][len('dropped: '):]}" for n, _, h in dropped]
	lines += ["", f"## Embedded items dropped ({len(embedded)})", ""]
	lines += [f"- **{n}**, {p}" for n, p, _ in embedded]
	lines += ["", f"## Reworded ({len(other)})", ""]
	lines += [f"- **{n}** `{p}`: {'; '.join(h)}" for n, p, h in other]
	lines += ["", f"## Not yet reviewed ({len(unreviewed)})", ""]
	lines += [f"- **{n}** `{p}`: {'; '.join(h)}" for n, p, h in unreviewed]
	lines += ["", "## Left in the feed", ""]
	lines += [f"- **{n}**: {', '.join(found)}" for n, found in left] or ["None."]
	with open(path, "w", encoding="utf-8", newline="\n") as f:
		f.write("\n".join(lines) + "\n")


def write_rules(path, commit, kinds, items, excluded):
	lines = ["# Rule elements and licence filter", "", f"Foundry pf2e commit `{commit}`.", "",
		"Every rule element kind in the feed, with how often it appears and on how many items. The pf2e package",
		"applies the kinds it has a handler for and shows the others as unsupported on the sheet.", "",
		"| Kind | Rule elements | Items |", "| --- | --- | --- |"]
	lines += [f"| {k} | {kinds[k]} | {items[k]} |" for k in sorted(kinds, key=lambda k: (-kinds[k], k))]
	lines += ["", "## Left out by the licence and book filter", "", "| Licence | Book | Items |", "| --- | --- | --- |"]
	lines += [f"| {lic} | {title} | {n} |" for (lic, title), n in sorted(excluded.items(), key=lambda kv: (-kv[1], kv[0]))]
	with open(path, "w", encoding="utf-8", newline="\n") as f:
		f.write("\n".join(lines) + "\n")


def main(argv):
	args = [a for a in argv if not a.startswith("--")]
	if len(args) != 2:
		raise SystemExit(__doc__)
	foundry, out = args
	result = build(foundry, os.path.join(HERE, "books.json"))
	config, kept, excluded, rule_kinds, rule_items, predicates, formula_set, rows, left, lang, missing = result
	total = sum(len(v) for v in kept.values())
	print(f"items kept: {total}; left out by licence or book: {sum(excluded.values())}")
	for book in config["books"]:
		if book["reviewed"]:
			print(f"  {book['slug']}: {sum(len(v) for (b, _), v in kept.items() if b == book['slug'])}")
	print(f"rule element kinds: {len(rule_kinds)}; predicates: {len(predicates)}; formulas: {len(formula_set)}")
	print(f"reserved: {len(rows)} actions; terms left in the feed: {len(left)}")
	print(f"language keys: {len(lang)}; not found in Foundry's English files: {len(missing)}")
	if "--write" in argv:
		os.makedirs(out, exist_ok=True)
		index = write(out, foundry, result)
		print(f"wrote {sum(len(b['files']) for b in index['books'])} item files to {out}")
	else:
		print("dry run; pass --write to write the feed")


if __name__ == "__main__":
	main(sys.argv[1:])
