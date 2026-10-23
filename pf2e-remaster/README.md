# Pathfinder 2e

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

The wiki collection is named **Pathfinder 2e**; its main learning article explains the Remaster scope.

Start at **Learn PF2e** in the wiki, or use `+wiki Learn PF2e`. The guides walk through
character creation, complete dwarf fighter and wizard examples, equipment, movement
and a separate two-turn adjacent encounter, defeat/recovery and worked level-2 advancement. Rules topics link to the complete option entries;
spell-rank and feat-level indexes have headings for the wiki table of contents.
This is a core learning path and reference, not an adventure, bestiary, rules engine
or automatic check that a particular character meets every prerequisite.

## What it installs

| Namespace | Pages |
|---|---|
| Category | Start here — Learn PF2e, Character Creation, Rules, Conditions and Difficulty Classes (all five pinned to the wiki home), and under them Classes, Class Features, Ancestries, Heritages (one per ancestry, plus Versatile Heritages), Backgrounds, Skills, Feats (Ancestry, Class, General, Skill and Archetype Feats, with one category per class and per ancestry), Spells (Cantrips, Rank 1 to Rank 10, Focus Spells, Rituals, and one per tradition), Actions (Basic, Specialty Basic, Skill, Exploration, Downtime, Subsystem, Other), Equipment (Weapons, Armor, Shields, Ammunition, Consumables and their kinds, Runes, Staves, Wands, Worn and Held Items, Adventuring Gear, Treasure and more), Familiar Abilities, and the condition groups |
| Main | 16 classes, 341 class features, 16 ancestries, 106 heritages, 63 backgrounds, 1,814 feats, 659 spells, 166 actions, 1,241 items, 55 familiar abilities, 17 skills, Proficiency Ranks, Character Sheet, 37 rules overviews, 42 conditions, Degrees of Success and the four DC tables, and thirteen guided-learning pages |
| Help | ORC License Notice (wiki admins only may edit or delete it) |

Each class page gives its key attribute, Hit Points, initial proficiencies, feat levels, class
features by level and its class feats; each ancestry its Hit Points, size, Speed, boosts and flaws,
languages, heritages and ancestry feats. Feats show level, traits, prerequisites and action cost;
spells their rank, traditions, casting, range, area, targets, defense, duration and heightening;
items their level, price, Bulk, traits, usage and weapon, armor or shield stats.

Every page ends with a line linking the ORC License Notice page.

It also defines six wiki fact properties, so pages can state them and be found by them:
`pf2e:level` and `pf2e:rank` (numbers), `pf2e:tradition` (arcane, divine, occult, primal; several
per page), `pf2e:class` (class pages; several per page), `pf2e:ancestry` (an ancestry page) and
`pf2e:source-book` (player core, player core 2, gm core). Uninstalling removes the properties; pages
keep the facts they state.

## Requirements

Requires a SharpMUSH server and strict PackageValidator supporting manifest format
1.17, for its `wiki_properties` ([SharpMUSH #2227](https://github.com/SharpMUSH/SharpMUSH/pull/2227)).
The validator checks the complete manifest and file-backed wiki bodies.

Version 1.3.0 adds the complete Dwarf Wizard Example, locally checked level-1/2
Wizard slot counts and advancement, actual movement practice, consistent heroic
recovery timing and currency guidance. The collection remains **Pathfinder 2e**;
its main learning article explains the Remaster scope. There are thirteen guided-learning pages. This source revision prepares the manifest/index
version; it does not itself publish a release or change an installed game.

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

The Wizard route links its complete starting sheet to the named book and casting ledger: ordinary and curriculum preparations, focus, spell attacks, basic saves, repeated preparation, Arcane Bond and daily reset. A worked level-2 update includes actual feat/book/preparation choices. Local base-slot counts cover levels 1–2; the full higher-level Wizard Spells per Day table remains an explicitly labelled external primary dependency. Source navigation checks do not certify live rendering, rules completeness or usability for every player.

Version 1.3.1 adds a pinned **Start here — Learn PF2e** category introduction
and explicit next-step/return links across the core learning path. The learning
order is authored content; category and related-page lists remain reference
navigation. The `wiki-next-step` Markdown container uses ordinary wiki links and
remains readable without the portal’s optional visual treatment.

Version 1.3.2 declares **Learn PF2e** as the collection entrance (`wiki_landing_page`,
manifest format 1.14), so the portal shows it under **Start here** on the collection page.
It also adds a first-roll primer (GM and player roles, dice notation, DC, AC, HP) to
Learn PF2e, makes the Degrees of Success ranges disjoint with boundary examples, and
explains how typed and untyped penalties stack.

Version 1.4.0 defines the PF2e wiki fact properties (`wiki_properties`, manifest format 1.17)
and names the package (`title`).
