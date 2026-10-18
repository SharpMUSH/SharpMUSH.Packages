# pf2e-remaster

A rules reference for Pathfinder Second Edition (Remaster), installed as wiki pages: the classes,
ancestries, heritages, backgrounds, feats, spells, actions, equipment and familiar abilities of
Player Core, Player Core 2 and GM Core, a page for every skill, a character sheet overview, every
condition, the difficulty class tables and rules overviews. Players read them in the portal's wiki
and with `+wiki`.

This is a **content pack**: documentation only, with no objects or softcode. Softcode never reads
these pages. The rules themselves, with the DC tables as game data, belong in a separate
implementation package that depends on the dice package; that package may write its tables to the
wiki, but never the other way round.

Not published, endorsed or approved by Paizo. Pathfinder is a trademark of Paizo Inc.

## Learn and play

Start at **Learn PF2e** in the wiki, or use `+wiki Learn PF2e`. The guides walk through
character creation, an exact-budget dwarf fighter, equipment, a two-turn encounter,
defeat/recovery and advancement. Rules topics link to the complete option entries;
spell-rank and feat-level indexes have headings for the wiki table of contents.
This is a core learning path and reference, not an adventure, bestiary, rules engine
or automatic check that a particular character meets every prerequisite.

## What it installs

| Namespace | Pages |
|---|---|
| Category | Character Creation, Rules, Conditions and Difficulty Classes (all four pinned to the wiki home), and under them Classes, Class Features, Ancestries, Heritages (one per ancestry, plus Versatile Heritages), Backgrounds, Skills, Feats (Ancestry, Class, General, Skill and Archetype Feats, with one category per class and per ancestry), Spells (Cantrips, Rank 1 to Rank 10, Focus Spells, Rituals, and one per tradition), Actions (Basic, Specialty Basic, Skill, Exploration, Downtime, Subsystem, Other), Equipment (Weapons, Armor, Shields, Ammunition, Consumables and their kinds, Runes, Staves, Wands, Worn and Held Items, Adventuring Gear, Treasure and more), Familiar Abilities, and the condition groups |
| Main | 16 classes, 341 class features, 16 ancestries, 106 heritages, 63 backgrounds, 1,814 feats, 659 spells, 166 actions, 1,241 items, 55 familiar abilities, 17 skills, Proficiency Ranks, Character Sheet, 37 rules overviews, 42 conditions, Degrees of Success and the four DC tables, and twelve guided-learning pages |
| Help | ORC License Notice (wiki admins only may edit or delete it) |

Each class page gives its key attribute, Hit Points, initial proficiencies, feat levels, class
features by level and its class feats; each ancestry its Hit Points, size, Speed, boosts and flaws,
languages, heritages and ancestry feats. Feats show level, traits, prerequisites and action cost;
spells their rank, traditions, casting, range, area, targets, defense, duration and heightening;
items their level, price, Bulk, traits, usage and weapon, armor or shield stats.

Every page ends with a line linking the ORC License Notice page.

## Requirements

The `wiki:` block uses manifest format 1.4. Current SharpMUSH supports file-backed wiki
packages; its strict PackageValidator reads the complete manifest and bodies. Use a
current server with content-pack support rather than a release predating that format.

Version 1.2.0 adds twelve guided-learning pages and linked corrections to the existing
reference. Its manifest/index version is prepared for review; it does not itself
publish a package release or change an installed game.

## Editing and upgrades

The pages are yours once installed. Edit them as you would any wiki page. On an upgrade, edits
that don't overlap the new version's changes are kept and merged; an edit that clashes with one is
shown on the review screen, and keeping your text is the default. Uninstalling deletes the pages
nobody changed and leaves the ones your staff edited.

## Licence

The rules text in `wiki/` is Adapted Licensed Material under the ORC License, not the licence of
the rest of this repository. The full notice, with the attribution the licence requires, is in
[NOTICE.md](NOTICE.md) and installs as the `Help:ORC License Notice` page.

When you change a page:

- keep the footer line that links the notice;
- don't add Reserved Material: proper nouns (deities, places, named characters and
  organizations), Paizo artwork, trade dress or setting lore;
- don't add material from Paizo's Fan Content Policy or Community Use Policy; those can't be
  mixed with ORC rules content.

The learning guides and original worked examples, conditions, DC tables, skill pages, Proficiency Ranks and Character Sheet were written for this
pack from Player Core and GM Core. Everything else was transcribed from the Foundry VTT pf2e game
system, taking only items it marks as ORC-licensed from Player Core, Player Core 2 and GM Core;
pages that name a deity, place, organization or other setting term were reworded to leave it out,
or left out where the name is the rule.

## Files

- `package.yaml`: the manifest.
- `wiki/<namespace>/<page>.md`: one Markdown file per page.
- `NOTICE.md`: the ORC notice.

The Wizard learning route separately covers a level-1 casting ledger: book choices, ordinary and curriculum preparations, focus, spell attacks, basic saves, repeated preparation, Arcane Bond and daily reset. It assumes an explicitly stated Intelligence/proficiency input; it is not a complete alternate character build. The full higher-level Wizard Spells per Day table is an explicitly labelled external primary dependency.
