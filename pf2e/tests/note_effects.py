"""Contract test for DATA`NOTEFX, the table of who each effect a roll's note links is for.

	python3 -I note_effects.py <pf2e-feed> <pf2e/package.yaml>

Checks, against the feed:
- every effect a Note rule links (through @UUID[Compendium.pf2e.<pack>-effects.Item.<id or name>]) that the feed
  carries has a row, and every row names one;
- a row is target, self or none, with auto after target or self;
- an auto effect is linked only from notes that name their outcomes, as only those put it on;
- each ChoiceSet of an auto effect has one choice that holds for each outcome its notes name, from the parent:
  options FUN`ITEM`PARENT and FUN`FX`ORIGIN give it, as FUN`FX`AUTOCHOICE takes it;
- a TempHP of an auto effect that reads @actor.flags.system.<x> has an effect in the feed that sets that flag.
"""
import glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from predicates import test

LINK = re.compile(r"@UUID\[Compendium\.pf2e\.([a-z-]+-effects)\.Item\.([^\]]+)\]")
OUTCOMES = ["criticalFailure", "failure", "success", "criticalSuccess"]

def sluggify(name):
	return re.sub(r"[^a-z0-9]+", "-", re.sub(r"['’]", "", name.lower())).strip("-")

def slug(item):
	return item["system"].get("slug") or sluggify(item["name"])

def selectors(values):
	return [sluggify(v) for v in values or []]

def load(feed):
	items, names = {}, {}
	for path in glob.glob(os.path.join(feed, "items", "*", "*.txt")):
		pack = re.sub(r"-\d+\.txt$", "", os.path.basename(path))
		with open(path, encoding="utf-8") as f:
			for line in f:
				parts = line.rstrip("\n").split(" ", 3)
				if len(parts) == 4 and parts[2] == "ITEM":
					item = json.loads(parts[3])
					items[(pack, item["_id"])] = item
					names[(pack, item["name"])] = item["_id"]
	with open(os.path.join(feed, "lang.json"), encoding="utf-8") as f:
		lang = json.load(f)
	return items, names, lang

def origin(item):
	"""FUN`FX`ORIGIN of the note's item, without the roller's level and traits."""
	sysd = item["system"]
	opts = ["item", "item:id:" + item["_id"], "item:slug:" + slug(item), "item:type:" + item["type"]]
	level = (sysd.get("level") or {}).get("value")
	if isinstance(level, int):
		opts.append(f"item:level:{level}")
	traits = sysd.get("traits") or {}
	opts += ["item:trait:" + t for t in selectors(traits.get("value"))]
	opts += ["item:tag:" + t for t in selectors(traits.get("otherTags"))]
	return opts

def parent(effect, origin_opts, outcome):
	"""FUN`ITEM`PARENT of the effect with its _origin, each with parent: in front."""
	sysd = effect["system"]
	opts = ["id:" + effect["_id"], "slug:" + slug(effect), "type:" + effect["type"]]
	level = (sysd.get("level") or {}).get("value")
	if isinstance(level, int):
		opts.append(f"level:{level}")
	traits = sysd.get("traits") or {}
	opts += ["trait:" + t for t in selectors(traits.get("value"))]
	opts += ["tag:" + t for t in selectors(traits.get("otherTags"))]
	opts += ["origin:" + o for o in origin_opts]
	opts.append(f"context:check:outcome:{outcome}")
	return {"parent:" + o for o in opts}

def main(argv):
	feed, package = argv
	items, names, lang = load(feed)
	with open(package, encoding="utf-8") as f:
		text = f.read()
	rows = {k.upper(): v.split() for k, v in re.findall(r"^\s+DATA`NOTEFX`([A-Z0-9]+): (.+)$", text, re.M)}
	fails = []
	links = {}
	for (pack, _), item in items.items():
		for rule in item["system"].get("rules") or []:
			if rule.get("key") != "Note":
				continue
			note_text = str(rule.get("text", ""))
			note_text = lang.get(note_text, note_text)
			for fx_pack, ref in LINK.findall(note_text):
				fx_id = ref if (fx_pack, ref) in items else names.get((fx_pack, ref))
				if fx_id:
					links.setdefault((fx_pack, fx_id), []).append((item, rule))
	ids = {fx_id.upper(): key for key in links for fx_id in [key[1]]}
	for up, key in sorted(ids.items()):
		if up not in rows:
			fails.append(f"no DATA`NOTEFX`{up} for {items[key]['name']}")
	for up, row in sorted(rows.items()):
		if up not in ids:
			fails.append(f"DATA`NOTEFX`{up} names no effect a note links")
			continue
		if row[0] not in ("target", "self", "none") or row[1:] not in ([], ["auto"]) or (row[0] == "none" and row[1:]):
			fails.append(f"DATA`NOTEFX`{up}: {' '.join(row)} is not target, self or none, with auto after target or self")
			continue
		if row[1:] != ["auto"]:
			continue
		key = ids[up]
		effect = items[key]
		rules = effect["system"].get("rules") or []
		for item, rule in links[key]:
			named = rule.get("outcome") or []
			if not named:
				fails.append(f"{effect['name']} is auto, but {item['name']}'s note names no outcome")
			for name in named:
				opts = parent(effect, origin(item), OUTCOMES.index(name))
				for i, choice_set in enumerate(rules):
					if choice_set.get("key") != "ChoiceSet":
						continue
					choices = choice_set.get("choices")
					if not isinstance(choices, list) or "parent:" not in json.dumps(choices):
						fails.append(f"{effect['name']} is auto, but its ChoiceSet {i} asks the player")
						continue
					fit = [c for c in choices if test(c.get("predicate") or [], opts)]
					if len(fit) != 1:
						fails.append(f"{effect['name']} from {item['name']} on {name}: ChoiceSet {i} fits {len(fit)} choices")
		for rule in rules:
			value = str(rule.get("value", "")) if rule.get("key") == "TempHP" else ""
			if value.startswith("@actor.flags.system."):
				path = value[len("@actor."):]
				if not any(r.get("key") == "ActiveEffectLike" and r.get("path") == path for it in items.values() for r in it["system"].get("rules") or []):
					fails.append(f"{effect['name']}'s temporary Hit Points read {path}, which no effect sets")
	for line in fails:
		print("FAIL", line)
	auto = sum(1 for r in rows.values() if r[1:] == ["auto"])
	print(f"{len(links)} linked effects, {len(rows)} rows, {auto} auto: {'FAIL' if fails else 'PASS'}")
	return 1 if fails else 0

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
