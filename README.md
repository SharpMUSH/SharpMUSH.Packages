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
| [`sheet-d20/`](sheet-d20/) | 2.0.0 | d20 character sheet built from a ledger: six abilities, a skill list the game edits, training, level, hit points, coin and gear, guided character creation and XP advances; `+check` against a DC; `+encounter` plays scenes from copies of the sheets |
| [`sheet-d20-help/`](sheet-d20-help/) | 1.0.1 | Bridge: the D20 sheet's topics in `+help` |
| [`sheet-d20-config/`](sheet-d20-config/) | 1.0.1 | Bridge: the D20 sheet's settings and trait table in `+config` |
| [`sheet-d20-chargen/`](sheet-d20-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-fate/`](sheet-fate/) | 1.0.1 | Fate character sheet: skills or approaches on the ladder, aspects, stress, consequences and fate points; `+check` on four Fate dice. Fate SRD text under CC BY 3.0 (see its NOTICE) |
| [`sheet-fate-help/`](sheet-fate-help/) | 1.0.0 | Bridge: the Fate sheet's topics in `+help` |
| [`sheet-fate-config/`](sheet-fate-config/) | 1.0.0 | Bridge: the Fate sheet's settings and tables in `+config` |
| [`sheet-fate-chargen/`](sheet-fate-chargen/) | 1.0.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-pbta/`](sheet-pbta/) | 2.1.0 | Powered by the Apocalypse character sheet built from a ledger: playbooks, stats and moves the game edits, guided character creation, advances, forward, ongoing, hold and XP; `+check` on 2d6; `+encounter` plays scenes from copies of the sheets. Dungeon World moves under CC BY 3.0 (see its NOTICE) |
| [`sheet-pbta-help/`](sheet-pbta-help/) | 1.0.1 | Bridge: the PbtA sheet's topics in `+help` |
| [`sheet-pbta-config/`](sheet-pbta-config/) | 1.0.1 | Bridge: the PbtA sheet's settings and tables in `+config` |
| [`sheet-pbta-chargen/`](sheet-pbta-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`duties-d20/`](duties-d20/) | 1.0.1 | Duties roll provider `d20` on the D20 sheet |
| [`d20-wiki/`](d20-wiki/) | 1.0.0 | Wiki pages for the d20 sheet: checks and DCs, making a character, abilities and skills, hit points, gear and advancement, and encounters |
| [`duties-fate/`](duties-fate/) | 1.0.0 | Duties roll provider `fate` on the Fate sheet: teamwork, paid invokes, fate points as rewards |
| [`duties-pbta/`](duties-pbta/) | 1.0.1 | Duties roll provider `pbta` on the PbtA sheet: aid, forward and ongoing, XP as a reward |
| [`pbta-wiki/`](pbta-wiki/) | 1.0.1 | Wiki pages for the PbtA sheet: how to play, making a character, the playbooks, the basic and special moves, advancement and encounters. Dungeon World moves under CC BY 3.0 |
| [`sheet-fitd/`](sheet-fitd/) | 2.0.0 | Forged in the Dark character sheet: twelve actions under three attributes built from a ledger, XP for each attribute spent on advances, stress, trauma, harm, coin, an audited log of XP and coin, encounters played from copies of the sheets, and progress clocks; `+check` on a d6 pool against a position. Blades in the Dark SRD under CC BY 3.0 (see its NOTICE) |
| [`sheet-fitd-help/`](sheet-fitd-help/) | 1.0.1 | Bridge: the FitD sheet's topics in `+help` |
| [`sheet-fitd-config/`](sheet-fitd-config/) | 1.0.1 | Bridge: the FitD sheet's settings and lists in `+config` |
| [`sheet-fitd-chargen/`](sheet-fitd-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-brp/`](sheet-brp/) | 2.0.0 | Percentile character sheet on Basic Roleplaying: characteristics and a skill list with base chances built from a ledger, point-buy character creation, experience checks that raise skills, hit points, power points, coin, an audited log of coin and skill gains, and encounters played from copies of the sheets; `+check` on 1d100. ORC Licensed Material (see its NOTICE) |
| [`sheet-brp-help/`](sheet-brp-help/) | 1.0.1 | Bridge: the BRP sheet's topics in `+help` |
| [`sheet-brp-config/`](sheet-brp-config/) | 1.0.1 | Bridge: the BRP sheet's settings and skill list in `+config` |
| [`sheet-brp-chargen/`](sheet-brp-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`sheet-ironsworn/`](sheet-ironsworn/) | 2.0.0 | Ironsworn character sheet: five stats and assets built from a ledger, guided character creation, experience spent on new assets and abilities with an audited log, meters, momentum, companion health, iron vows with progress, and encounters that play from copies of the sheets; `+check` action rolls and `+vow`. Ironsworn SRD under CC BY 4.0 (see its NOTICE) |
| [`sheet-ironsworn-help/`](sheet-ironsworn-help/) | 1.0.1 | Bridge: the Ironsworn sheet's topics in `+help` |
| [`sheet-ironsworn-config/`](sheet-ironsworn-config/) | 1.0.1 | Bridge: the Ironsworn sheet's settings and its stat and asset lists in `+config` |
| [`sheet-ironsworn-chargen/`](sheet-ironsworn-chargen/) | 1.1.0 | Bridge: sheet edits follow the player's `+app` application; reviewers read the sheets they review |
| [`duties-fitd/`](duties-fitd/) | 1.0.1 | Duties roll provider `fitd` on the FitD sheet: assists and pushes paid in stress, coin and stress relief as rewards |
| [`fitd-wiki/`](fitd-wiki/) | 1.0.0 | Wiki pages for the FitD sheet: how to play, making a character, actions and attributes, stress, harm and advancement, encounters and clocks. Based on the Blades in the Dark SRD under CC BY 3.0 |
| [`duties-brp/`](duties-brp/) | 1.0.1 | Duties roll provider `brp` on the BRP sheet: help as an augment, skill increases and healing as rewards |
| [`brp-wiki/`](brp-wiki/) | 1.0.0 | Wiki pages for the BRP sheet: how to play, making a character, characteristics and skills, hit points, coin and experience, and encounters. ORC Licensed Material |
| [`ironsworn-wiki/`](ironsworn-wiki/) | 1.0.0 | Wiki pages for the Ironsworn sheet: action rolls, making a character, assets and experience, meters and momentum, iron vows, and encounters. Ironsworn SRD under CC BY 4.0 |
| [`duties-ironsworn/`](duties-ironsworn/) | 1.1.0 | Duties roll provider `ironsworn` on the Ironsworn sheet: help adds 1, experience (logged) and momentum as rewards |
| [`sheet-salvage-union/`](sheet-salvage-union/) | 1.1.0 | Salvage Union pilots, mechs and the Union Crawler: class ability trees, chassis, systems and modules, scrap by tech level, heat; `+check` rolls the d20 on the Core Mechanic table. Unofficial, under the Salvage Union Open Game Licence 1.0b (see its NOTICE) |
| [`sheet-salvage-union-help/`](sheet-salvage-union-help/) | 1.0.0 | Bridge: the Salvage Union sheet's topics in `+help` |
| [`sheet-salvage-union-config/`](sheet-salvage-union-config/) | 1.0.0 | Bridge: the Salvage Union sheet's settings in `+config` |
| [`sheet-salvage-union-chargen/`](sheet-salvage-union-chargen/) | 1.0.0 | Bridge: sheet and mech edits follow the player's `+app` application; reviewers read the sheets they review |
| [`duties-salvage-union/`](duties-salvage-union/) | 1.0.1 | Duties roll provider `salvage` on the Salvage Union sheet: abilities and mech parts as traits, Training Points and crawler scrap as rewards |
| [`salvage-union-wiki/`](salvage-union-wiki/) | 1.0.1 | Salvage Union rules as wiki pages: the core rules, Pilot Bay, Mech Workshop, every chassis blueprint, the Union Crawler, salvaging, the denizens of the wasteland, and a page for every ability, system, module, piece of equipment and table. Unofficial, under the Salvage Union Open Game Licence 1.0b (see its NOTICE) |

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
`pf2e-feed/`, with its notice in [`pf2e-feed/NOTICE.md`](pf2e-feed/NOTICE.md).
Package manifests are softcode — inspect anything you install; the admin panel's review screen flags dangerous patterns (`@force`, `@toad`, …)
to help.
