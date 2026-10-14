# pf2e-remaster

A rules reference for Pathfinder Second Edition (Remaster), installed as wiki pages: every
condition from Player Core and the difficulty class tables from GM Core. Players read them in the
portal's wiki and with `+wiki`; the tables are wiki tables other packages can look values up in.

This is a **content pack**. It carries no objects or softcode. The rules that act on these pages
(rolling checks, applying conditions to characters) belong in a separate package, which will
depend on the dice package.

Not published, endorsed or approved by Paizo. Pathfinder is a trademark of Paizo Inc.

## What it installs

| Namespace | Pages |
|---|---|
| Category | Conditions (pinned to the wiki home), its groups (Attitudes, Death and Dying, Degrees of Detection, Lowered Abilities, Senses), Difficulty Classes (pinned) |
| Main | 42 conditions, Degrees of Success |
| Table | Simple DCs, DCs by Level, Spell DCs by Rank, DC Adjustments |
| Help | ORC License Notice (wiki admins only may edit or delete it) |

Every page ends with a line linking the ORC License Notice page.

## Requirements

The `wiki:` block is manifest format 1.4, which SharpMUSH does not read yet. Until it does, a
server rejects this package at review because it has no objects. The design is in the SharpMUSH
project's content-packs plan.

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

The text was written for this pack from Player Core and GM Core, not copied from another site.

## Files

- `package.yaml`: the manifest.
- `wiki/<namespace>/<page>.md`: one Markdown file per page.
- `NOTICE.md`: the ORC notice.
