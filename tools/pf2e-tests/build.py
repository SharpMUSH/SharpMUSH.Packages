"""Writes the pf2e behaviour tests, tests/pf2e/<name>.yaml, from the scenarios in tools/pf2e-tests/scenarios.

	python3 -I tools/pf2e-tests/build.py [--check]

A pf2e test needs Foundry's items, which a game reads from pf2e-feed with the updater: thousands of items,
minutes of work. A test reads only the items it names instead. A scenario is a test file with one more
top-level key, `feed`, a list of items as `<pack>/<name>` (`classes/Cleric`, `heritages/Dhampir`), or
`<pack>/*` for a whole pack, written `feed: [a, b]`. Each is put in with what it brings: the items its rules
grant or offer by uuid (a self effect too), and a class's or ancestry's features up to `feed_level` (default 1). The conditions
pack always comes, and the language lines (labels such as PF2E.SpecificRule...) the items name.

The test written has `install` with pf2e first, and steps before the scenario's own that hand each item's
feed lines to the updater's INC`IMPORT`LINE, as a run of the updater does. A test whose scenario is gone is removed.
With --check nothing is written, and the exit status is 1 when a test is not what its scenario gives, or has no scenario.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FEED = os.path.join(ROOT, "pf2e-feed")
OUT = os.path.join(ROOT, "tests", "pf2e")

# Foundry's pack ids, as uuids name them, to the feed's pack names (the core's DATA`UUID).
UUID_PACKS = {
	"feats-srd": "feats", "classfeatures": "class-features", "ancestryfeatures": "ancestry-features",
	"actionspf2e": "actions", "spells-srd": "spells", "equipment-srd": "equipment", "conditionitems": "conditions",
	"feat-effects": "feat-effects", "spell-effects": "spell-effects", "equipment-effects": "equipment-effects",
	"other-effects": "other-effects", "ancestries": "ancestries", "heritages": "heritages", "backgrounds": "backgrounds",
	"classes": "classes", "familiar-abilities": "familiar-abilities",
}
UUID = re.compile(r"Compendium\.pf2e\.([a-z0-9-]+)\.Item\.([^\]\"}]+)")


LANG_KEY = re.compile(r"PF2E\.[A-Za-z0-9.]+")


def read_lang():
	"""The feed's language lines: key -> (file, line)."""
	index = json.load(open(os.path.join(FEED, "index.json"), encoding="utf-8"))
	lang = {}
	for entry in index["lang"]:
		with open(os.path.join(FEED, entry["path"]), encoding="utf-8") as feed:
			for line in feed:
				line = line.rstrip("\n")
				if line:
					lang[line.split(" ", 1)[0]] = (entry["path"], line)
	return lang


def read_feed():
	"""Every item line of the feed: (pack, id) -> {file, book, lines: {leaf: line}, item: the parsed ITEM}."""
	index = json.load(open(os.path.join(FEED, "index.json"), encoding="utf-8"))
	items, names = {}, {}
	for book in index["books"]:
		for entry in book["files"]:
			with open(os.path.join(FEED, entry["path"]), encoding="utf-8") as feed:
				for line in feed:
					line = line.rstrip("\n")
					if not line:
						continue
					item_id, _hash, leaf, value = line.split(" ", 3)
					key = (entry["pack"], item_id)
					record = items.setdefault(key, {"file": entry["path"], "book": book["slug"], "lines": {}})
					record["lines"][leaf] = line
					if leaf == "ITEM":
						record["item"] = json.loads(value)
						names.setdefault((entry["pack"], record["item"]["name"].lower()), item_id)
	return items, names


def find(items, names, pack, name):
	if (pack, name) in items:
		return name
	found = names.get((pack, name.lower()))
	if not found:
		raise SystemExit(f"The feed has no {pack} item called {name}.")
	return found


def closure(items, names, seeds, level):
	"""The items the seeds name, with what each brings by uuid, oldest first."""
	wanted, queue = [], list(seeds)
	while queue:
		pack, item_id = queue.pop(0)
		if (pack, item_id) in wanted:
			continue
		wanted.append((pack, item_id))
		item = items[(pack, item_id)].get("item", {})
		system = item.get("system", {})
		refs = []
		# A class's or ancestry's own features, up to the level the test reaches.
		for feature in (system.get("items") or {}).values():
			if feature.get("level", 0) <= level and feature.get("uuid"):
				refs.append(feature["uuid"])
		refs += UUID.findall(json.dumps([system.get("rules", []), system.get("selfEffect")]))
		for ref in refs:
			if isinstance(ref, str):
				match = UUID.search(ref)
				if not match:
					continue
				ref = match.groups()
			ref_pack, ref_name = UUID_PACKS.get(ref[0]), ref[1]
			if not ref_pack or "{" in ref_name:
				continue
			ref_id = ref_name if (ref_pack, ref_name) in items else names.get((ref_pack, ref_name.lower()))
			if ref_id:
				queue.append((ref_pack, ref_id))
	return wanted


def yaml_string(text):
	return json.dumps(text, ensure_ascii=False)


def load_steps(items, wanted, lang):
	steps = []
	keys = sorted({key for pack, item_id in wanted for key in LANG_KEY.findall(items[(pack, item_id)]["lines"].get("ITEM", "")) if key in lang})
	for key in keys:
		path, line = lang[key]
		steps.append(f"  - god: {yaml_string('&FEED`CURRENT ${object:pf2e/updater}=' + '|'.join([path, 'lang', 'lang', 'test']))}")
		steps.append(f"  - god: {yaml_string('&FEED`BODY ${object:pf2e/updater}=' + line)}")
		steps.append("  - god: \"@trigger ${object:pf2e/updater}/INC`IMPORT`LINE=1\"")
	for pack, item_id in wanted:
		record = items[(pack, item_id)]
		steps.append(f"  - god: {yaml_string('&FEED`CURRENT ${object:pf2e/updater}=' + '|'.join([record['file'], pack, record['book'], 'test']))}")
		# Every leaf in feed order (ITEM, TEXT, each EMBED`<ID>), less HASH, which marks a finished import.
		for leaf, line in record["lines"].items():
			if leaf != "HASH":
				steps.append(f"  - god: {yaml_string('&FEED`BODY ${object:pf2e/updater}=' + line)}")
				steps.append("  - god: \"@trigger ${object:pf2e/updater}/INC`IMPORT`LINE=1\"")
	return steps


def build(path, items, names, lang):
	text = open(path, encoding="utf-8").read()
	feed = re.search(r"^feed: *\[(.*)\] *$", text, re.M)
	level = re.search(r"^feed_level: *(\d+) *$", text, re.M)
	level = int(level[1]) if level else 1
	seeds = []
	for spec in ["conditions/*"] + ([part.strip().strip('"') for part in feed[1].split(",") if part.strip()] if feed else []):
		pack, name = spec.split("/", 1)
		if name == "*":
			seeds += [key for key in items if key[0] == pack]
		else:
			seeds.append((pack, find(items, names, pack, name)))
	wanted = closure(items, names, seeds, level)
	# The scenario's own lines, without feed and feed_level, with the loading steps first.
	kept = []
	for line in text.splitlines():
		if re.match(r"^(feed|feed_level):", line):
			continue
		kept.append(line)
		if line.rstrip() == "steps:":
			kept.append(f"  # Generated by tools/pf2e-tests/build.py: the {len(wanted)} feed items this test reads.")
			kept += load_steps(items, wanted, lang)
			kept.append("  # The scenario.")
	header = f"# Generated from tools/pf2e-tests/scenarios/{os.path.basename(path)}; edit that and run build.py.\n"
	return header + "\n".join(kept) + "\n"


def main():
	check = "--check" in sys.argv
	items, names = read_feed()
	lang = read_lang()
	scenarios = os.path.join(HERE, "scenarios")
	os.makedirs(OUT, exist_ok=True)
	stale, orphans = [], False
	for name in sorted(os.listdir(scenarios)):
		if not name.endswith(".yaml"):
			continue
		written = build(os.path.join(scenarios, name), items, names, lang)
		target = os.path.join(OUT, name)
		current = open(target, encoding="utf-8").read() if os.path.exists(target) else None
		if current != written:
			stale.append(name)
			if not check:
				with open(target, "w", encoding="utf-8", newline="\n") as out:
					out.write(written)
	# A test whose scenario is gone.
	for name in sorted(os.listdir(OUT)):
		if name.endswith(".yaml") and not os.path.exists(os.path.join(scenarios, name)):
			print(("orphan: " if check else "removed: ") + os.path.join("tests", "pf2e", name))
			orphans = True
			if not check:
				os.remove(os.path.join(OUT, name))
	for name in stale:
		print(("stale: " if check else "wrote: ") + os.path.join("tests", "pf2e", name))
	sys.exit(1 if check and (stale or orphans) else 0)


if __name__ == "__main__":
	main()
