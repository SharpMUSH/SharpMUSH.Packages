# PF2e feed generator

Builds `pf2e-feed/` from a checkout of the [Foundry VTT pf2e system](https://github.com/foundryvtt/pf2e). The pf2e-app
application reads the feed to fill and update a game's PF2e data.

```
git clone --depth 1 --filter=blob:none --sparse https://github.com/foundryvtt/pf2e.git foundry
git -C foundry sparse-checkout set packs/pf2e static/lang
python3 -I tools/pf2e-feed/build.py foundry pf2e-feed           # dry run: counts only
python3 -I tools/pf2e-feed/build.py foundry pf2e-feed --write   # writes the feed
```

`.github/workflows/pf2e-feed.yml` runs this every Monday and opens a pull request when the feed changed.

## What goes in

- Items from the packs listed in `books.json`, from books marked `reviewed`, whose `publication.license` is `ORC`.
  Everything else (OGL items, other books) is counted in `reports/rules.md` and left out.
- Each item as Foundry wrote it, less image paths, sort order and folder. Rule elements, predicates and formulas
  are untouched: the pf2e package interprets them.
- `lang.json`: the English text of every Foundry language key (`PF2E.…`) the items use.

## Reserved Material

The ORC License does not cover Paizo's proper nouns. `reserved.py` holds the term list (setting names plus every
deity in the Foundry deities pack), item-specific rewordings, and items dropped because the proper noun is the rule
itself. Any other description that still names a term has that sentence cut and is listed under "Cut by the
general rule" in `reports/reserved.md`. The cuts stand as they are; a rewording in `reserved.py` replaces one that
reads badly. The build fails nothing on its own; the
report's "Left in the feed" section must say "None." before a feed is merged.

## Adding a book

Review the book's items the way the first four were reviewed, add rewordings and drops to `reserved.py`, then set
`reviewed: true` in `books.json`. `default` says whether a new game starts with the book switched on.

## Feed format

| File | Holds |
| --- | --- |
| `index.json` | Format number, Foundry commit, and per book its item files with line and item counts, sizes and hashes |
| `items/<book>/<pack>-<n>.txt` | One stored attribute a line: `<_id> <hash> <leaf> <value>`, where `<leaf>` is `ITEM` (the item less its description and embedded items), `TEXT` (the description as a JSON string), ``EMBED`<ID>`` (an embedded item) or `HASH` (last, the item's hash). An item's lines may run on into the next file. Files stay under 60 KiB, so one fits in an attribute |
| `lang.json` | Language key to English text |
| `reports/reserved.md` | Every Reserved Material change |
| `reports/rules.md` | Rule element kinds by count, and what the licence filter left out |
| `corpus/predicates.txt`, `corpus/formulas.txt` | Every distinct predicate and formula, for the pf2e package's parser tests |
| `NOTICE.md` | The ORC notice for the data |

## Property runes

Foundry keeps property runes in code, not in its packs. `property_runes.py` reads them from
`src/module/item/physical/runes.ts` (with node) and writes the `DATA`RUNE`` tables on the pf2e core object:

```
git -C foundry sparse-checkout add src/module/item/physical
python3 -I tools/pf2e-feed/property_runes.py foundry pf2e/package.yaml
```
