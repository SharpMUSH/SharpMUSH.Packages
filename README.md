# SharpMUSH Packages

**Give your world new things to do.**

Official softcode packages for [SharpMUSH](https://github.com/SharpMUSH/SharpMUSH): connected starter rooms, player directories, bulletin boards, roll tables and reference content.

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

| Package | Version | Description |
|---|---|---|
| [`hello-world/`](hello-world/) | 1.0.0 | Minimal example: one object, one `+hello` command |
| [`who-where/`](who-where/) | 1.2.0 | `+who` and `+where` commands with a shared formatting object |
| [`starter-area/`](starter-area/) | 1.0.0 | Two rooms and linked exits |
| [`bbs-lite/`](bbs-lite/) | 0.9.0-beta | Tiny bulletin board; dependencies, typed configure params, cross-package refs |
| [`http-handler/`](http-handler/) | 1.0.0 | Inbound HTTP verb routers using existing handler objects |
| [`profile-handler/`](profile-handler/) | 1.0.0 | Read-only character directory and profile API; depends on HTTP Handler |
| [`roll-tables/`](roll-tables/) | 1.0.0 | Random tables as softcode data: `+table/roll` tells the room, table keepers edit them by command, and a table can be published to a wiki page |
| [`pf2e-remaster/`](pf2e-remaster/) | 1.4.0 | Pathfinder Second Edition (Remaster) core rules as wiki pages: classes, ancestries, heritages, backgrounds, feats, spells, actions, equipment, skills, conditions and DC tables; a content pack under the ORC License |
| [`sheet-d20/`](sheet-d20/) | 2.2.1 | d20 character sheet built from a ledger: six abilities, a skill list the game edits, training, level, hit points, coin and gear, guided character creation and XP advances; `+check` against a DC or a foe; `+encounter` plays scenes from copies of the sheets, with a bestiary of foes, initiative, turns and conditions |
| [`sheet-d20-help/`](sheet-d20-help/) | 1.0.1 | Bridge: the D20 sheet's topics in `+help` |
| [`sheet-d20-config/`](sheet-d20-config/) | 1.0.2 | Bridge: the D20 sheet's settings, trait table and bestiary in `+config` |
| [`sheet-d20-chargen/`](sheet-d20-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-fate/`](sheet-fate/) | 1.6.0 | Fate character sheet: skills or approaches on the ladder, aspects, stunts, stress, consequences and fate points; `+check` on four Fate dice; a grant ledger, guided `+chargen`, encounters that keep their own sheet copies with NPCs from `+npc`, exchanges, harm, concessions, scene aspects and the GM's pool, and milestones and breakthroughs from staff on an award ledger of their own, which players spend with `+sheet/advance`. Fate SRD text under CC BY 3.0 (see its NOTICE) |
| [`sheet-fate-help/`](sheet-fate-help/) | 1.0.0 | Bridge: the Fate sheet's topics in `+help` |
| [`sheet-fate-config/`](sheet-fate-config/) | 1.0.0 | Bridge: the Fate sheet's settings and tables in `+config` |
| [`sheet-fate-chargen/`](sheet-fate-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-fate-wiki/`](sheet-fate-wiki/) | 1.1.0 | Fate rules reference as wiki pages: the ladder, aspects, skills, stunts, actions, stress and consequences, `+chargen`, advancement and encounters. Fate SRD text under CC BY 3.0 |
| [`atomic-robo/`](atomic-robo/) | 1.1.0 | Unofficial Atomic Robo pack: pulp action science and giant robots on the Fate sheet: modes that rate skills, mega-stunts, invention with catches and flaws, brainstorms, and machines and enemy robots whose scale counts. Atomic Robo RPG SRD and Fate System Toolkit under CC BY 3.0 (see its NOTICE) |
| [`atomic-robo-help/`](atomic-robo-help/) | 1.0.0 | Bridge: the Atomic Robo topics in `+help` |
| [`atomic-robo-config/`](atomic-robo-config/) | 1.0.0 | Bridge: the Atomic Robo settings and tables in `+config` |
| [`atomic-robo-wiki/`](atomic-robo-wiki/) | 1.1.0 | Unofficial Atomic Robo rules reference as wiki pages: modes, chargen, mega-stunts, invention, brainstorms, scale and machines, advancement |
| [`fate-adversary-toolkit/`](fate-adversary-toolkit/) | 1.0.0 | Unofficial Fate Adversary Toolkit pack: opposition for the Fate sheet: ready adversaries scaled to the game, adversaries built by type, filler mobs that thin as they fall, hazards, blocks, distractions, countdowns, limitations and resistances. Fate Adversary Toolkit SRD under CC BY 3.0 (see its NOTICE) |
| [`fate-adversary-toolkit-help/`](fate-adversary-toolkit-help/) | 1.0.0 | Bridge: the Fate Adversary Toolkit topics in `+help` |
| [`fate-adversary-toolkit-config/`](fate-adversary-toolkit-config/) | 1.0.0 | Bridge: the Fate Adversary Toolkit settings and libraries in `+config` |
| [`fate-adversary-toolkit-wiki/`](fate-adversary-toolkit-wiki/) | 1.0.0 | Unofficial Fate Adversary Toolkit rules reference as wiki pages: enemies, obstacles, constraints |
| [`fate-system-toolkit/`](fate-system-toolkit/) | 1.1.0 | Unofficial Fate System Toolkit pack for the Fate sheet: conditions that soak stress, a Wealth track for money that staff refill with audited parcels, Stormcallers, magic from five storms with barriers, super skills with fate-point bids between powers, gadgets and magic items, and cyberware on a cyber-heart with surgery in play. Fate System Toolkit SRD under CC BY 3.0 (see its NOTICE) |
| [`fate-system-toolkit-help/`](fate-system-toolkit-help/) | 1.1.0 | Bridge: the Fate System Toolkit topics in `+help` |
| [`fate-system-toolkit-config/`](fate-system-toolkit-config/) | 1.1.0 | Bridge: the Fate System Toolkit settings, conditions, storms and augs in `+config` |
| [`fate-system-toolkit-wiki/`](fate-system-toolkit-wiki/) | 1.1.0 | Unofficial Fate System Toolkit rules reference as wiki pages: conditions, Wealth, Stormcallers, supers, gadgets, cyberware |
| [`sheet-pbta/`](sheet-pbta/) | 2.3.1 | Powered by the Apocalypse character sheet built from a ledger: playbooks, stats and moves the game edits, guided character creation, advances, forward, ongoing, hold, harm and XP; `+check` on 2d6; `+encounter` plays scenes from copies of the sheets, with foes from a bestiary and GM moves. Dungeon World moves under CC BY 3.0 (see its NOTICE) |
| [`sheet-pbta-help/`](sheet-pbta-help/) | 1.0.1 | Bridge: the PbtA sheet's topics in `+help` |
| [`sheet-pbta-config/`](sheet-pbta-config/) | 1.0.2 | Bridge: the PbtA sheet's settings and tables, the bestiary and GM moves among them, in `+config` |
| [`sheet-pbta-chargen/`](sheet-pbta-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`duties-d20/`](duties-d20/) | 1.0.1 | Duties roll provider `d20` on the D20 sheet |
| [`duties-pf2e/`](duties-pf2e/) | 1.0.0 | Duties roll provider `pf2e` on the Pathfinder 2e sheet: skills, Perception and saves against the roller's level DC, Aid, XP and money as rewards |
| [`d20-wiki/`](d20-wiki/) | 1.1.0 | Wiki pages for the d20 sheet: checks and DCs, making a character, abilities and skills, hit points, gear and advancement, and encounters with foes and turns |
| [`duties-fate/`](duties-fate/) | 1.0.0 | Duties roll provider `fate` on the Fate sheet: teamwork, paid invokes, fate points as rewards |
| [`duties-pbta/`](duties-pbta/) | 1.0.2 | Duties roll provider `pbta` on the PbtA sheet: aid, forward and ongoing, XP as a reward |
| [`pbta-wiki/`](pbta-wiki/) | 1.1.0 | Wiki pages for the PbtA sheet: how to play, making a character, the playbooks, the basic and special moves, advancement, and encounters with foes and harm. Dungeon World moves under CC BY 3.0 |
| [`sheet-fitd/`](sheet-fitd/) | 2.2.1 | Forged in the Dark character sheet: twelve actions under three attributes built from a ledger, XP for each attribute spent on advances, stress, trauma, harm, coin, an audited log of XP and coin, encounters played from copies of the sheets, with threats that each have a clock, positions and effect, and progress clocks; `+check` on a d6 pool against a position. Blades in the Dark SRD under CC BY 3.0 (see its NOTICE) |
| [`sheet-fitd-help/`](sheet-fitd-help/) | 1.0.1 | Bridge: the FitD sheet's topics in `+help` |
| [`sheet-fitd-config/`](sheet-fitd-config/) | 1.0.2 | Bridge: the FitD sheet's settings and lists, the threats among them, in `+config` |
| [`sheet-fitd-chargen/`](sheet-fitd-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-brp/`](sheet-brp/) | 2.3.0 | Percentile character sheet on Basic Roleplaying: characteristics and a skill list with base chances built from a ledger, point-buy character creation, experience checks that raise skills, hit points, power points, coin, an audited log of coin and skill gains, and encounters played from copies of the sheets, with creatures from a bestiary, hit locations and an order of play by DEX or strike rank; `+check` on 1d100. ORC Licensed Material (see its NOTICE) |
| [`sheet-brp-help/`](sheet-brp-help/) | 1.0.1 | Bridge: the BRP sheet's topics in `+help` |
| [`sheet-brp-config/`](sheet-brp-config/) | 1.0.2 | Bridge: the BRP sheet's settings, skill list and bestiary in `+config` |
| [`sheet-brp-chargen/`](sheet-brp-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-ironsworn/`](sheet-ironsworn/) | 2.2.1 | Ironsworn character sheet: five stats and assets built from a ledger, guided character creation, experience spent on new assets and abilities with an audited log, meters, momentum, companion health, iron vows with progress, and encounters that play from copies of the sheets, with foes from a bestiary fought on progress tracks; `+check` action rolls and `+vow`. Ironsworn SRD under CC BY 4.0 (see its NOTICE) |
| [`sheet-ironsworn-help/`](sheet-ironsworn-help/) | 1.0.1 | Bridge: the Ironsworn sheet's topics in `+help` |
| [`sheet-ironsworn-config/`](sheet-ironsworn-config/) | 1.0.2 | Bridge: the Ironsworn sheet's settings, stat and asset lists and bestiary in `+config` |
| [`sheet-ironsworn-chargen/`](sheet-ironsworn-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`duties-fitd/`](duties-fitd/) | 1.0.1 | Duties roll provider `fitd` on the FitD sheet: assists and pushes paid in stress, coin and stress relief as rewards |
| [`fitd-wiki/`](fitd-wiki/) | 1.1.0 | Wiki pages for the FitD sheet: how to play, making a character, actions and attributes, stress, harm and advancement, encounters with threats, and clocks. Based on the Blades in the Dark SRD under CC BY 3.0 |
| [`duties-brp/`](duties-brp/) | 1.0.2 | Duties roll provider `brp` on the BRP sheet: help as an augment, skill increases and healing as rewards |
| [`brp-wiki/`](brp-wiki/) | 1.1.0 | Wiki pages for the BRP sheet: how to play, making a character, characteristics and skills, hit points, coin and experience, and encounters with creatures. ORC Licensed Material |
| [`ironsworn-wiki/`](ironsworn-wiki/) | 1.1.0 | Wiki pages for the Ironsworn sheet: action rolls, making a character, assets and experience, meters and momentum, iron vows, and encounters with foes. Ironsworn SRD under CC BY 4.0 |
| [`duties-ironsworn/`](duties-ironsworn/) | 1.1.0 | Duties roll provider `ironsworn` on the Ironsworn sheet: help adds 1, experience (logged) and momentum as rewards |
| [`sheet-fabula/`](sheet-fabula/) | 1.2.0 | JRPG character sheet compatible with Fabula Ultima: four attribute dice, the Core Rulebook's and the Atlases' classes and skill levels, HP, MP, IP, Fabula Points, experience and zenit on a ledger, status effects, bonds and encounters, with conflicts in turns against a bestiary of foes on a battle screen with pictures; `+check` rolls two attribute dice against a Difficulty Level. Requires the Fabula Ultima Core Rulebook (see its NOTICE) |
| [`sheet-fabula-help/`](sheet-fabula-help/) | 1.0.0 | Bridge: the JRPG sheet's topics in `+help` |
| [`sheet-fabula-config/`](sheet-fabula-config/) | 1.0.0 | Bridge: the JRPG sheet's settings and class list in `+config` |
| [`sheet-fabula-chargen/`](sheet-fabula-chargen/) | 1.0.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`fabula-wiki/`](fabula-wiki/) | 1.2.0 | JRPG rules as wiki pages: character creation, checks, Fabula Points and bonds, resources, levels and zenit, status effects, conflicts, classes and the commands on this game. Requires the Fabula Ultima Core Rulebook (see its NOTICE) |
| [`duties-fabula/`](duties-fabula/) | 1.0.0 | Duties roll provider `fabula` on the JRPG sheet: help and bonds add to the total, Fabula Points pay for rerolls, experience, zenit and Fabula Points as rewards |
| [`sheet-salvage-union/`](sheet-salvage-union/) | 1.3.0 | Salvage Union pilots, mechs and the Union Crawler: class ability trees, chassis, systems and modules, scrap by tech level, heat; `+check` rolls the d20 on the Core Mechanic table. Unofficial, under the Salvage Union Open Game Licence 1.0b (see its NOTICE) |
| [`sheet-salvage-union-help/`](sheet-salvage-union-help/) | 1.0.0 | Bridge: the Salvage Union sheet's topics in `+help` |
| [`sheet-salvage-union-config/`](sheet-salvage-union-config/) | 1.0.0 | Bridge: the Salvage Union sheet's settings in `+config` |
| [`sheet-salvage-union-chargen/`](sheet-salvage-union-chargen/) | 1.0.0 | Bridge: sheet and mech edits follow the player's `+app` application; reviewers read the sheets they review |
| [`duties-salvage-union/`](duties-salvage-union/) | 1.0.2 | Duties roll provider `salvage` on the Salvage Union sheet: abilities and mech parts as traits, Training Points and crawler scrap as rewards |
| [`salvage-union-wiki/`](salvage-union-wiki/) | 1.0.3 | Salvage Union rules as wiki pages: the core rules, Pilot Bay, Mech Workshop, every chassis blueprint, the Union Crawler, salvaging, the denizens of the wasteland, and a page for every ability, system, module, piece of equipment and table. Unofficial, under the Salvage Union Open Game Licence 1.0b (see its NOTICE) |
| [`sheet-charge/`](sheet-charge/) | 1.2.2 | Charge character sheet: details, twelve actions in dots, momentum, a stress clock and condition, milestones and talents on a ledger, encounters with their own sheet copies, threats and consequences, and clocks; `+check` on a d6 pool against a risk, with assists, pushes, determination and fortune rolls. Charge SRD under CC BY 4.0 (see its NOTICE) |
| [`sheet-charge-help/`](sheet-charge-help/) | 1.0.0 | Bridge: the Charge sheet's topics in `+help` |
| [`sheet-charge-config/`](sheet-charge-config/) | 1.0.0 | Bridge: the Charge sheet's settings and lists in `+config` |
| [`sheet-charge-chargen/`](sheet-charge-chargen/) | 1.0.0 | Bridge: giving out action dots follows the player's `+app` application; reviewers read the sheets they review |
| [`charge-wiki/`](charge-wiki/) | 1.0.2 | Charge rules as wiki pages: the game, character creation, action rolls, momentum, teamwork, consequences, stress, clocks, progression, fortune rolls and the commands that play them; a content pack under CC BY 4.0 (see its NOTICE) |
| [`duties-charge/`](duties-charge/) | 1.0.0 | Duties roll provider `charge` on the Charge sheet: assists and pushes paid in momentum, momentum, milestones and stress recovery as rewards |

These currently double as the reference implementations for package authors —
each README explains which manifest features it demonstrates. The curated
default softcode experience (scene-system, bboard, chargen, events, finger,
http-hooks) will land here as those systems mature.

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
`who-where/v1.2.0`. The admin panel's version list is the tag list; installing
a version checks out its tag; `main` is the development channel. Release tags
are **immutable**: never move or delete one — publish a fix as a new version.
Installers record the exact commit they applied and warn loudly if a release
tag later points elsewhere.

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
5. Once merged, a maintainer tags the release `<package>/v<version>`.

Package ids are first-come within this repo, must not collide with an
existing id even with punctuation stripped (`who-where` blocks `whowhere`),
and released versions are never rewritten — bump the version instead.

## License

Same license as SharpMUSH unless a package declares otherwise in its
manifest. `pf2e-remaster/` is one that does: its rules text is under the ORC
License, with the notice in [`pf2e-remaster/NOTICE.md`](pf2e-remaster/NOTICE.md). So is the data in
`pf2e-feed/`, with its notice in [`pf2e-feed/NOTICE.md`](pf2e-feed/NOTICE.md). `charge-wiki/` is under CC BY 4.0,
with its notice in [`charge-wiki/NOTICE.md`](charge-wiki/NOTICE.md).
Package manifests are softcode — inspect anything you install; the admin panel's review screen flags dangerous patterns (`@force`, `@toad`, …)
to help.
