# SharpMUSH Packages

**Give your world new things to do.**

Official softcode packages for [SharpMUSH](https://github.com/SharpMUSH/SharpMUSH): character sheets for tabletop systems, rules references as wiki pages, roll tables and the bridges that join them.

**[Browse packages](#packages)** · **[Install a package](#using-this-repo)** · **[Write your own](#contributing-a-package)**

<p align="center">
  <img src="assets/branding/sharpie/marketing/sharpie-package-workbench.png" width="320" alt="Sharpie connects reusable room and conversation modules on a small workbench." />
</p>

A **package** is a declarative description of softcode: the objects that
should exist on a MUSH and the attributes, flags, locks, and parent
relationships they carry. Packages are installed, upgraded, and authored
through SharpMUSH's web admin panel (`/admin/packages`) using a plan/apply
model — the server computes a changeset against the live database, a wizard
reviews it, and only then is anything written. Upgrades three-way-merge
against stored baselines so your local customizations survive, every apply is
recorded as a revision, and installs can be rolled back.

Packages use symbolic object references instead of hardcoded dbrefs.

## Using this repo

Add it as a remote in the SharpMUSH admin panel
(**Admin → Packages → Remotes**):

```
https://github.com/SharpMUSH/SharpMUSH.Packages
```

Then browse, pick a package and version, review the changeset, and apply.
Dependencies are resolved against your installed packages, with version
constraints checked before anything is planned.

## Packages

The table is generated from [`index.yaml`](index.yaml); edit that file, then run
`python3 tools/readme-packages-table.py`.

<!-- packages-table:begin (generated from index.yaml by tools/readme-packages-table.py) -->
| Package | Version | Description |
|---|---|---|
| [`roll-tables/`](roll-tables/) | 1.1.0 | Random tables as softcode data, rolled in the room with +table/roll and publishable to the wiki |
| [`roll-tables-help/`](roll-tables-help/) | 1.0.0 | Puts the roll table topics into +help |
| [`pf2e-remaster/`](pf2e-remaster/) | 1.6.4 | Pathfinder Second Edition (Remaster) core rules as wiki pages (classes, ancestries, feats, spells, equipment, skills, conditions, DC tables; ORC License) |
| [`sheet-d20/`](sheet-d20/) | 2.2.4 | d20 character sheet built from a ledger (abilities, skills, training, level, hit points, coin, gear), guided character creation, +check against a DC or a foe, and encounters with their own sheet copies, foes from a bestiary, initiative and conditions |
| [`sheet-d20-help/`](sheet-d20-help/) | 1.0.3 | Puts the D20 sheet topics into +help |
| [`sheet-d20-config/`](sheet-d20-config/) | 1.0.4 | Puts the D20 sheet settings, trait table and bestiary into +config |
| [`sheet-d20-chargen/`](sheet-d20-chargen/) | 1.1.2 | Joins the D20 sheet to +app character applications |
| [`sheet-fate/`](sheet-fate/) | 1.6.3 | Fate character sheet (skills or approaches, aspects, stunts, stress, consequences, fate points) with +check on four Fate dice, a grant ledger, guided +chargen, encounters with their own sheet copies, NPC opposition from +npc and the commands to run a conflict, and audited milestones and breakthroughs that players spend with +sheet/advance; Fate SRD text under CC BY 3.0 |
| [`sheet-fate-help/`](sheet-fate-help/) | 1.0.2 | Puts the Fate sheet topics into +help |
| [`sheet-fate-config/`](sheet-fate-config/) | 1.0.2 | Puts the Fate sheet settings and its skill, approach, stress and consequence tables into +config |
| [`sheet-fate-chargen/`](sheet-fate-chargen/) | 1.1.2 | Joins the Fate sheet to +app character applications |
| [`sheet-fate-wiki/`](sheet-fate-wiki/) | 1.1.2 | Fate rules reference as wiki pages; Fate SRD text under CC BY 3.0 |
| [`atomic-robo/`](atomic-robo/) | 1.1.2 | Unofficial Atomic Robo pack, pulp action science and giant robots on the Fate sheet (modes, mega-stunts, invention, brainstorms, machines and enemy robots at scale); Atomic Robo RPG SRD and Fate System Toolkit text under CC BY 3.0 |
| [`atomic-robo-help/`](atomic-robo-help/) | 1.0.2 | Puts the Atomic Robo topics into +help |
| [`atomic-robo-config/`](atomic-robo-config/) | 1.0.2 | Puts the Atomic Robo settings and its modes and scales tables into +config |
| [`atomic-robo-wiki/`](atomic-robo-wiki/) | 1.1.2 | Unofficial Atomic Robo rules reference as wiki pages; Atomic Robo RPG SRD and Fate System Toolkit text under CC BY 3.0 |
| [`fate-adversary-toolkit/`](fate-adversary-toolkit/) | 1.0.2 | Unofficial Fate Adversary Toolkit pack, opposition for the Fate sheet (ready adversaries scaled to your game, adversaries built by type, filler mobs, hazards, blocks, distractions, countdowns, limitations and resistances); Fate Adversary Toolkit SRD text under CC BY 3.0 |
| [`fate-adversary-toolkit-help/`](fate-adversary-toolkit-help/) | 1.0.2 | Puts the Fate Adversary Toolkit topics into +help |
| [`fate-adversary-toolkit-config/`](fate-adversary-toolkit-config/) | 1.0.2 | Puts the Fate Adversary Toolkit settings and its adversary and obstacle libraries into +config |
| [`fate-adversary-toolkit-wiki/`](fate-adversary-toolkit-wiki/) | 1.0.2 | Unofficial Fate Adversary Toolkit rules reference as wiki pages; Fate Adversary Toolkit SRD text under CC BY 3.0 |
| [`fate-system-toolkit/`](fate-system-toolkit/) | 1.1.2 | Unofficial Fate System Toolkit pack for the Fate sheet (conditions that soak stress, a Wealth track for money on an audited ledger, Stormcallers' storm magic with barriers, super skills with fate-point bids between powers, gadgets and magic items, and cyberware with surgery); Fate System Toolkit SRD text under CC BY 3.0 |
| [`fate-system-toolkit-help/`](fate-system-toolkit-help/) | 1.1.2 | Puts the Fate System Toolkit topics into +help |
| [`fate-system-toolkit-config/`](fate-system-toolkit-config/) | 1.1.2 | Puts the Fate System Toolkit settings, conditions, storms and augs into +config |
| [`fate-system-toolkit-wiki/`](fate-system-toolkit-wiki/) | 1.1.2 | Unofficial Fate System Toolkit rules reference as wiki pages; Fate System Toolkit SRD text under CC BY 3.0 |
| [`duties/`](duties/) | 1.3.2 | +duty — short adventures a party plays from challenge to challenge, written by players, approved by duty reviewers and put on a seasonal roster; rolls come from a sheet system bridge |
| [`duties-help/`](duties-help/) | 1.0.2 | Registers the duties topics with +help (requires duties and plus-help) |
| [`duties-config/`](duties-config/) | 1.0.2 | Registers the duties settings and active roster with +config (requires duties and plus-config) |
| [`duties-app/`](duties-app/) | 1.1.1 | Application package — registers duties as a portal page at /apps/duties, with a map editor for a duty's steps, the review of submitted duties and the active roster (requires duties) |
| [`duties-scene/`](duties-scene/) | 1.0.3 | +duty/start/scene and +duty/scene — a party plays its duty in a scene, and setting out, each step, roll and outcome go into it as narration (requires duties and scene) |
| [`duties-d20/`](duties-d20/) | 1.0.3 | Duties roll provider "d20" on the D20 sheet |
| [`duties-pf2e/`](duties-pf2e/) | 1.0.2 | Duties roll provider "pf2e" on the Pathfinder 2e sheet |
| [`duties-fate/`](duties-fate/) | 1.0.2 | Duties roll provider "fate" on the Fate sheet |
| [`sheet-pbta/`](sheet-pbta/) | 2.3.4 | Powered by the Apocalypse character sheet built from a ledger (playbooks, stats, moves, guided character creation, advances, forward, ongoing, hold, harm, XP), +check on 2d6 and encounters on sheet copies with foes and GM moves; Dungeon World moves under CC BY 3.0 |
| [`sheet-pbta-help/`](sheet-pbta-help/) | 1.0.3 | Puts the PbtA sheet topics into +help |
| [`sheet-pbta-config/`](sheet-pbta-config/) | 1.0.4 | Puts the PbtA sheet settings and its stats, moves, playbooks, foes and GM moves tables into +config |
| [`sheet-pbta-chargen/`](sheet-pbta-chargen/) | 1.1.2 | Joins the PbtA sheet to +app character applications |
| [`duties-pbta/`](duties-pbta/) | 1.0.4 | Duties roll provider "pbta" on the PbtA sheet |
| [`pbta-wiki/`](pbta-wiki/) | 1.1.2 | Wiki pages for the PbtA sheet (how to play, making a character, playbooks, moves, advancement, encounters, foes); Dungeon World moves under CC BY 3.0 |
| [`d20-wiki/`](d20-wiki/) | 1.1.2 | Wiki pages for the d20 sheet (checks and DCs, making a character, abilities and skills, hit points, gear and advancement, encounters) |
| [`fitd-wiki/`](fitd-wiki/) | 1.1.2 | Wiki pages for the FitD sheet (how to play, making a character, actions and attributes, stress, harm and advancement, encounters, threats, clocks); based on the Blades in the Dark SRD under CC BY 3.0 |
| [`brp-wiki/`](brp-wiki/) | 1.1.2 | Wiki pages for the BRP sheet (how to play, making a character, characteristics and skills, hit points, coin and experience, encounters, creatures); ORC Licensed Material |
| [`ironsworn-wiki/`](ironsworn-wiki/) | 1.1.2 | Wiki pages for the Ironsworn sheet (how to play, making a character, assets and experience, meters and momentum, vows, encounters, foes); based on the Ironsworn SRD under CC BY 4.0 |
| [`pf2e/`](pf2e/) | 0.10.19 | Pathfinder Second Edition rules read the way Foundry VTT's pf2e system reads them, with ledger character sheets, a character builder, spellcasting, a deity table the game fills, alchemy, encounters with a bestiary, hazards, effects and GM tools, exploration, skill challenges, downtime, loot and shops with unidentified items, audited awards and levels (ORC License) |
| [`pf2e-portal/`](pf2e-portal/) | 1.0.1 | Joins the Pathfinder 2e rules to the HTTP handler, for the pf2e-app sheet page |
| [`pf2e-app/`](pf2e-app/) | 1.0.1 | The Pathfinder 2e sheet as a portal page at /apps/pf2e |
| [`pf2e-help/`](pf2e-help/) | 1.0.2 | Puts the Pathfinder 2e topics into +help |
| [`pf2e-config/`](pf2e-config/) | 1.0.2 | Puts the Pathfinder 2e settings into +config |
| [`sheet-fitd/`](sheet-fitd/) | 2.2.4 | Forged in the Dark character sheet (ledger-built actions, XP advances, stress, trauma, harm, coin, audited log, encounters with threats and positions, clocks) with +check on a d6 pool; Blades in the Dark SRD under CC BY 3.0 |
| [`sheet-fitd-help/`](sheet-fitd-help/) | 1.0.3 | Puts the FitD sheet topics into +help |
| [`sheet-fitd-config/`](sheet-fitd-config/) | 1.0.4 | Puts the FitD sheet settings and action, attribute and threat tables into +config |
| [`sheet-fitd-chargen/`](sheet-fitd-chargen/) | 1.1.2 | Joins the FitD sheet to +app character applications |
| [`sheet-brp/`](sheet-brp/) | 2.3.3 | Percentile character sheet on Basic Roleplaying (ledger-built characteristics and skills, point-buy chargen, experience checks, hit points, power points, coin, audited log, encounters with creatures, hit locations and strike ranks) with +check on 1d100; ORC Licensed Material |
| [`sheet-brp-help/`](sheet-brp-help/) | 1.0.3 | Puts the BRP sheet topics into +help |
| [`sheet-brp-config/`](sheet-brp-config/) | 1.0.4 | Puts the BRP sheet settings, skill table and bestiary into +config |
| [`sheet-brp-chargen/`](sheet-brp-chargen/) | 1.1.2 | Joins the BRP sheet to +app character applications |
| [`sheet-ironsworn/`](sheet-ironsworn/) | 2.2.4 | Ironsworn character sheet (stats and assets built from a ledger, meters, experience spent on assets with an audited log, companion health, iron vows, encounters with their own copies, foes on progress tracks) with +check action rolls and +vow; Ironsworn SRD under CC BY 4.0 |
| [`sheet-ironsworn-help/`](sheet-ironsworn-help/) | 1.0.3 | Puts the Ironsworn sheet topics into +help |
| [`sheet-ironsworn-config/`](sheet-ironsworn-config/) | 1.0.4 | Puts the Ironsworn sheet settings, stat and asset tables and bestiary into +config |
| [`sheet-ironsworn-chargen/`](sheet-ironsworn-chargen/) | 1.1.2 | Joins the Ironsworn sheet to +app character applications |
| [`duties-fitd/`](duties-fitd/) | 1.0.3 | Duties roll provider "fitd" on the FitD sheet |
| [`duties-brp/`](duties-brp/) | 1.0.4 | Duties roll provider "brp" on the BRP sheet |
| [`duties-ironsworn/`](duties-ironsworn/) | 1.1.2 | Duties roll provider "ironsworn" on the Ironsworn sheet |
| [`sheet-fabula/`](sheet-fabula/) | 1.2.3 | JRPG character sheet compatible with Fabula Ultima (four attribute dice, the Core Rulebook's and the Atlases' classes, HP/MP/IP, Fabula Points, status effects, bonds) with +check against a Difficulty Level, and conflicts in turns against a bestiary of foes on a battle screen with pictures; requires the Fabula Ultima Core Rulebook |
| [`sheet-fabula-help/`](sheet-fabula-help/) | 1.0.2 | Puts the JRPG sheet topics into +help |
| [`sheet-fabula-config/`](sheet-fabula-config/) | 1.0.2 | Puts the JRPG sheet settings and class table into +config |
| [`sheet-fabula-chargen/`](sheet-fabula-chargen/) | 1.0.2 | Joins the JRPG sheet to +app character applications |
| [`duties-fabula/`](duties-fabula/) | 1.0.2 | Duties roll provider "fabula" on the JRPG sheet |
| [`fabula-wiki/`](fabula-wiki/) | 1.2.2 | JRPG sheet rules as wiki pages (checks, Fabula Points, bonds, resources, statuses, conflicts, classes); requires the Fabula Ultima Core Rulebook |
| [`sheet-salvage-union/`](sheet-salvage-union/) | 1.3.3 | Salvage Union pilots, mechs and the Union Crawler (class ability trees, chassis, systems, modules, scrap, heat) with d20 +check on the Core Mechanic table; Salvage Union Open Game Licence 1.0b, unofficial |
| [`sheet-salvage-union-help/`](sheet-salvage-union-help/) | 1.0.2 | Puts the Salvage Union sheet topics into +help |
| [`sheet-salvage-union-config/`](sheet-salvage-union-config/) | 1.0.2 | Puts the Salvage Union sheet settings into +config |
| [`sheet-salvage-union-chargen/`](sheet-salvage-union-chargen/) | 1.0.2 | Joins the Salvage Union sheet to +app character applications |
| [`duties-salvage-union/`](duties-salvage-union/) | 1.0.4 | Duties roll provider "salvage" on the Salvage Union sheet |
| [`salvage-union-wiki/`](salvage-union-wiki/) | 1.0.5 | Salvage Union rules as wiki pages (core rules, Pilot Bay, Mech Workshop, chassis, Union Crawler, salvaging, denizens, and every ability, system, module, equipment and table); Salvage Union Open Game Licence 1.0b, unofficial |
| [`sheet-charge/`](sheet-charge/) | 1.2.4 | Charge character sheet (details, action dots, momentum, stress clock, milestones and talents) with +check action rolls, assists, determination and fortune rolls, encounters with threats and consequences, and clocks; Charge SRD under CC BY 4.0 |
| [`sheet-charge-help/`](sheet-charge-help/) | 1.0.2 | Puts the Charge sheet topics into +help |
| [`sheet-charge-config/`](sheet-charge-config/) | 1.0.2 | Puts the Charge sheet settings and action and detail tables into +config |
| [`sheet-charge-chargen/`](sheet-charge-chargen/) | 1.0.2 | Joins the Charge sheet to +app character applications |
| [`charge-wiki/`](charge-wiki/) | 1.0.4 | Charge rules as wiki pages (action rolls, momentum, consequences, stress, clocks, progression; CC BY 4.0) |
| [`duties-charge/`](duties-charge/) | 1.0.2 | Duties roll provider "charge" on the Charge sheet |
| [`radio/`](radio/) | 1.8.1 | +radio — frequencies to tune in to, speak on and recall, with moderators, admins and locks; the worked example of a system built on @feed |
| [`radio-help/`](radio-help/) | 1.1.1 | Registers the radio topics with +help (requires radio and plus-help) |
| [`radio-config/`](radio-config/) | 1.0.1 | Registers the radio settings with +config (requires radio and plus-config) |
| [`radio-scene/`](radio-scene/) | 1.4.3 | +radio/log — what a listener hears on a frequency goes into their scene, through a tap on the radio feed kind (requires radio and scene) |
| [`scene-verse/`](scene-verse/) | 2.0.0 | Verse and canon on scenes, and +scene/verses (requires scene) |
<!-- packages-table:end -->

Packages bundled with SharpMUSH (`+who`/`+where`, the HTTP handler, the
character profile API, bulletin boards and others) ship inside the server and
are not in this repo; some install on a new game, the rest from the admin
panel. Small teaching examples for package authors are in the
SharpMUSH Guide.

## PF2e feed

[`pf2e-feed/`](pf2e-feed/) is game data, not a package: every ORC item of Player Core, Player Core 2, GM Core
and Monster Core from the Foundry VTT pf2e system, one item a line, with an index the PF2e app reads to fill
and update a game. [`tools/pf2e-feed/`](tools/pf2e-feed/) builds it, and a weekly workflow opens a pull request
when Foundry's data changes.

## Community repos

[`community/`](community/) is the curated directory of accepted
**community package repos**. Games ping it from the admin panel to discover
sources beyond this repo, with the community trust tier and rendered READMEs.
Want yours listed? See [community/README.md](community/README.md) — it's a
one-file pull request.

## Repo structure & releases

A package is a directory containing a `package.yaml` manifest; the root
[`index.yaml`](index.yaml) lists every package with its id, latest version,
and description.

**Releases are git tags** named `<package-dir>/v<version>` — e.g.
`roll-tables/v1.0.0`. The admin panel's version list is the tag list; installing
a version checks out its tag; `main` is the development channel. Release tags
are **immutable**: never move or delete one — publish a fix as a new version.
Installers record the exact commit they applied and warn loudly if a release
tag later points elsewhere.

Tags are made by CI. A pull request that changes anything in a package's
directory fails unless it raises that package's `version` (in `package.yaml`
and `index.yaml`) above the last one. Once it merges, the release job tags
`<package-dir>/v<version>` at the last commit that touched the directory.
Every manifest is validated against SharpMUSH `main` and, once SharpMUSH has
a release, against its latest one; the behaviour tests in [`tests/`](tests/)
run on both, when that SharpMUSH has their runner. To check a branch by hand:

```
git fetch --tags origin
python3 tools/release/packages.py check-bumps origin/main HEAD
python3 tools/release/packages.py pending-tags
```

## The manifest format, in brief

Manifests are **desired state**, not command scripts — and they never contain
dbrefs. Object identity is symbolic, resolved at install time:

```yaml
format: 1
package: who-where              # id slug
version: 1.2.0                  # semver
description: "+who and +where commands."
license: MIT

depends:
  - package: some-dependency    # optional, with version constraints
    version: ">=1.0 <2.0"
    source:                     # where to find it if not installed
      repo: https://github.com/SharpMUSH/SharpMUSH.Packages
      path: some-dependency/

configure:
  storage:
    label: "Object that stores data"
    type: dbref                 # dbref | string | number | boolean

objects:
  - ref: ww_global              # abstract name — never a dbref
    type: thing                 # thing | room | exit | player
    name: Who-Where Global Object
    parent: "{{ww_functions}}"
    attributes:
      CMD_+WHO: |-
        $+who:@pemit %#=[u({{ww_functions}}/WW_FN_HEADER,Who)]...
```

Ref tokens (case-insensitive; every token must resolve or the manifest is
rejected; escape a literal `{{` as `{{{{`):

| Syntax | Resolved from |
|---|---|
| `{{name}}` | Another object defined in the same package |
| `{{pkg/name}}` | An object owned by `pkg` (must be listed under `depends:`) |
| `{{$name}}` | Server configuration (`room_zero`, `master_room`, `player_start`, `god`, `package_manager`) |
| `{{?name}}` | The installing admin, prompted during review (declare under `configure:`) |

**Write all MUSHcode as block scalars (`|-`)** — YAML plain and double-quoted
strings corrupt softcode (`\` escapes, ` #` comment truncation, `&token`
anchors). Exits declare `location:` and `destination:`; rooms declare
neither.

The full format reference lives in the SharpMUSH repo:
[`examples/packages/README.md`](https://github.com/SharpMUSH/SharpMUSH/blob/main/examples/packages/README.md).
Every manifest here is validated by CI (`tools/PackageValidator`, strict
mode: warnings fail).

## Contributing a package

1. Author your package — by hand or with the admin panel's authoring tools
   (object picker, dbref-to-ref resolution, export).
2. Add a directory with `package.yaml` and a `README.md`; declare a
   `license`.
3. Add the directory to `index.yaml` (path, id, version, description).
4. Open a pull request. Keep attribute namespaces behind a
   `convention_prefix`, never hardcode dbrefs, declare every `{{?configure}}`
   ref with a label and type, and use block scalars for all code.
5. Raise the package's version in the same pull request; once it merges, CI
   tags the release `<package>/v<version>`.
6. Add a behaviour test under `tests/<package>/`: a YAML file of commands
   played by test characters and the output each must show. CI runs it on a
   test game. See [`tests/README.md`](tests/README.md).

Package ids are first-come within this repo, must not collide with an
existing id even with punctuation stripped (`roll-tables` blocks `rolltables`),
and released versions are never rewritten — bump the version instead.

## License

Same license as SharpMUSH unless a package declares otherwise in its
manifest. `pf2e-remaster/` is one that does: its rules text is under the ORC
License, with the notice in [`pf2e-remaster/NOTICE.md`](pf2e-remaster/NOTICE.md). So is the data in
`pf2e-feed/`, with its notice in [`pf2e-feed/NOTICE.md`](pf2e-feed/NOTICE.md). `charge-wiki/` is under CC BY 4.0,
with its notice in [`charge-wiki/NOTICE.md`](charge-wiki/NOTICE.md).
Package manifests are softcode — inspect anything you install; the admin panel's review screen flags dangerous patterns (`@force`, `@toad`, …)
to help.
