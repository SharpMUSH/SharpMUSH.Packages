"""Contract test for FUN`PREDICATE`TEST against every predicate in pf2e-feed/corpus/predicates.txt.

	python3 -I predicates.py <corpus> <out-dir> [--cases N] [--seed S]

Writes <out-dir>/commands.txt (lines to send to a game holding the pf2e core at CORE and an object
CASES to hold the predicates) and
<out-dir>/expected.txt (what Foundry's Predicate.test gives for each case, ported below). After the
commands have run, compare the game's "PRED <n> <result>" lines with expected.txt.

An option holding an injected property such as {item|id} is left out: the pf2e core resolves those before
it tests a predicate, as Foundry does.
"""
import json, random, re, sys

def values(operand, domain):
	try:
		return [float(operand)]
	except (TypeError, ValueError):
		pass
	pat = re.compile(r"^" + re.escape(str(operand)) + r":([^:]+)$")
	found = []
	for s in domain:
		m = pat.match(s)
		if m:
			try:
				found.append(float(m.group(1)))
			except ValueError:
				pass
	return found

def true(st, domain):
	if isinstance(st, str):
		return st in domain
	if not isinstance(st, dict):
		return False
	keys = set(st)
	if keys == {"if", "then"}:
		return not (true(st["if"], domain) and not true(st["then"], domain))
	(op, arg), = st.items()
	if op == "and": return all(true(s, domain) for s in arg)
	if op == "or": return any(true(s, domain) for s in arg)
	if op == "nand": return not all(true(s, domain) for s in arg)
	if op == "nor": return not any(true(s, domain) for s in arg)
	if op == "xor": return sum(true(s, domain) for s in arg) == 1
	if op == "not": return not true(arg, domain)
	if op == "iff": return all(true(s, domain) for s in arg) or not any(true(s, domain) for s in arg)
	if op == "eq":
		return arg[0] == arg[1] if isinstance(arg[1], str) else f"{arg[0]}:{arg[1]}" in domain
	left, right = values(arg[0], domain), values(arg[1], domain)
	if not left or not right: return False
	cmp = {"gt": lambda l, r: l > r, "gte": lambda l, r: l >= r, "lt": lambda l, r: l < r, "lte": lambda l, r: l <= r}[op]
	return any(all(cmp(l, r) for r in right) for l in left)

def test(pred, domain):
	return isinstance(pred, list) and all(true(s, domain) for s in pred)

def atoms(st, out):
	if isinstance(st, str):
		out.add(st)
	elif isinstance(st, list):
		for s in st: atoms(s, out)
	elif isinstance(st, dict):
		for k, v in st.items():
			if k in ("gt", "gte", "lt", "lte", "eq"):
				for side in v:
					if isinstance(side, str): out.add(("num", side))
			else:
				atoms(v, out)

def domain_for(pred, rng):
	found = set()
	atoms(pred, found)
	dom = set()
	for a in sorted(found, key=str):
		if isinstance(a, tuple):
			if rng.random() < 0.8:
				dom.add(f"{a[1]}:{rng.randint(0, 20)}")
		elif rng.random() < 0.5:
			dom.add(a)
	return sorted(dom)

def main(argv):
	args = [a for a in argv if not a.startswith("--")]
	corpus, out = args
	opts = dict(a[2:].split("=", 1) for a in argv if a.startswith("--") and "=" in a)
	cases, rng = int(opts.get("cases", 3)), random.Random(int(opts.get("seed", 1)))
	with open(corpus, encoding="utf-8") as f:
		preds = [json.loads(l) for l in f if l.strip()]
	cmds, expected = [], []
	n = 0
	for i, pred in enumerate(preds):
		raw = json.dumps(pred, ensure_ascii=True, separators=(",", ":"))
		if any(c in raw for c in "%;\\"):
			continue
		cmds.append(f"&P`{i} CASES={raw}")
		for _ in range(cases):
			dom = domain_for(pred, rng)
			if any(c in d for d in dom for c in " ,[]{}%"):
				continue
			n += 1
			cmds.append(f"think PRED {n} [u(CORE/FUN`PREDICATE`TEST,get(CASES/P`{i}),{' '.join(dom)})]")
			expected.append(f"PRED {n} {int(test(pred, set(dom)))}")
	for name, lines in (("commands.txt", cmds), ("expected.txt", expected)):
		with open(f"{out}/{name}", "w", encoding="utf-8", newline="\n") as f:
			f.write("\n".join(lines) + "\n")
	print(f"{len(preds)} predicates, {n} cases")

if __name__ == "__main__":
	main(sys.argv[1:])
