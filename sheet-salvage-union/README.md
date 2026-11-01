# sheet-salvage-union

A Salvage Union sheet: a pilot with a class, ability trees, HP, AP, Training Points, equipment and
details; their mech with its chassis, systems, modules, SP, EP, heat and cargo; and the Union
Crawler the pilots share. `+check` rolls the one d20 on the Core Mechanic table, where the room sees
it, and nothing is ever added to the die.

The abilities, classes, chassis, systems, modules, equipment, crawler bays and tables are the Core
Book's, generated from the Salvage Union (Unofficial) Foundry VTT system by
[`tools/salvage-union/build.mjs`](../tools/salvage-union/). Unofficial, under the Salvage Union Open
Game Licence 1.0b: see [NOTICE.md](NOTICE.md) and the in-game `+help sheet credits`.

Depends on nothing. Bridges add the rest:

| Package | Adds |
|---|---|
| [`sheet-salvage-union-help`](../sheet-salvage-union-help/) | the `+help sheet`, `mech`, `check`, `crawler` and `encounter` topics |
| [`sheet-salvage-union-config`](../sheet-salvage-union-config/) | the settings in `+config salvage` |
| [`sheet-salvage-union-chargen`](../sheet-salvage-union-chargen/) | ties sheet and mech edits to the player's `+app` application |
| [`duties-salvage-union`](../duties-salvage-union/) | a Duties roll provider called `salvage` |
| [`salvage-union-wiki`](../salvage-union-wiki/) | the rules as wiki pages |

Every sheet package answers `+sheet` and `+check`. Install one per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | The pilot, with a line for the mech |
| `+sheet/chargen [<name>]` | all | The six steps of a new pilot and mech, each marked done or not |
| `+sheet/class <class>` | unapproved player | Engineer, Hacker, Hauler, Salvager, Scout or Soldier |
| `+sheet/learn <ability or tree>` | player | Learns an ability, or a tree's next one; costs TP once approved |
| `+sheet/unlearn <ability>` | player | Forgets the last of a tree |
| `+sheet/trees [<class>]`, `/ability <ability>` | all | The trees, with what you have marked; one ability's text |
| `+sheet/take <equipment>`, `/drop` | player | The inventory; a new pilot takes two pieces of Tech 1 equipment |
| `+sheet/item <equipment>`, `/list [<tech>]` | all | One piece of equipment; the equipment of a Tech Level |
| `+sheet/use <equipment>` | player | Spends one use |
| `+sheet/hp`, `/ap` `+<n>\|-<n>\|<n>\|reset` | player | The meters |
| `+sheet/callsign`, `/background`, `/motto`, `/keepsake`, `/appearance <text>` | player | The details |
| `+sheet/downtime [<name>]` | player | HP, AP, uses and re-rolls back; the mech repaired, recharged and cool |
| `+sheet/ledger [<name>]` | all | Every entry that built the sheet |
| `+sheet/tp <name>=<n>`, `/max <name>/<hp\|ap\|slots>=<n>` | keeper | Training Points; a pilot's most |
| `+sheet/revoke <name>/<n>`, `/clear <name>` | keeper | Takes back one ledger entry, or all of them |
| `+mech [<name>]` | all | The mech |
| `+mech/chassis <chassis>`, `/install`, `/remove <part>` | player | Builds it; a new pilot uses Tech 1 parts within 20 scrap, chassis included |
| `+mech/name`, `/quirk <text>` | player | Its pattern name and quirk |
| `+mech/sp`, `/ep`, `/heat`, `/vent`, `/use <part>` | player | Play |
| `+mech/scrap <tech>=+<n>\|-<n>` | player | Scrap in the cargo |
| `+mech/part <name>`, `/list <chassis\|systems\|modules> [<tech>]` | all | The parts |
| `+check[/private\|/mech] [<what>][=<x>]` | all | The die, with an ability, system or module spending its AP or EP and adding heat |
| `+check/push`, `/reroll <background\|keepsake>`, `/motto <name>`, `/heat` | player | The re-rolls and the heat check |
| `+check/table [<table>]` | all | A roll on a table; nested tables roll on |
| `+crawler`, `/bay [<bay>]` | all | The Union Crawler and its bays |
| `+crawler/unload`, `/scrap <tech>=+<n>\|-<n>` | approved player | Scrap from the mech into the hold, or changed |
| `+crawler/name`, `/type`, `/weapon`, `/tech`, `/sp`, `/pool`, `/upkeep`, `/upgrade` | keeper | Runs it |
| `+encounter [<n>]`, `/start [<title>]`, `/join [<n>]`, `/leave [<n>]`, `/use <n>` | all | Encounters |
| `+encounter/add`, `/remove`, `/keep <name>[=<n>]`, `/end [<n>]` | GM or keeper | Runs one |

Keepers (`softcode.salvage.admin`, the **Salvage Union Sheet Keeper** role) put `<name>/` before
the argument of a build switch to change anyone's sheet at any time, without spending TP.

## The ledger

A pilot's build is a ledger: `SALVAGE`LEDGER`<n>`, each a wizard-flagged JSON entry with `kind`,
`n`, `by` (objid), `at` (secs), `phase` (`chargen`, `play` or `staff`) and `note`.

| Kind | Fields | Is |
|---|---|---|
| `set` | `leaf`, `value` | the class, a detail, the chassis, a most; the newest standing one wins |
| `grant` | `list`, `key` | an ability, equipment, system or module, in the order granted |
| `tp` | `amount` | Training Points, summed |
| `revoke` | `entry` | takes one entry back |
| `clear` | | takes back every entry before it |

The sheet's own leaves (`CLASS`, `ABILITIES`, `GEAR`, `TP`, `PATH`, `DETAIL`*`, `MECH`CHASSIS`,
`MECH`SYSTEMS`, `MECH`MODULES`, ...) are written from the ledger after every entry
(`FUN`LEDGER`REBUILD`). Before approval, choosing a `set` leaf again rewrites the chargen entry,
and taking back a chargen entry wipes it, so the ledger keeps the choices that were made. After
approval every change is a new entry.

## Encounters

An encounter keeps its own copy of the leaves in `DATA`COPY` (HP, AP, the mech's SP, EP and heat,
the re-rolls, the last check) and of every `SPENT`<kind>`<key>`, the uses spent:

```
ENC`LIST                       the encounters running, by number
ENC`NEXT                       the next number
ENC`<n>                        its title
ENC`<n>`ROOM, `GM, `START      where, who and when
ENC`<n>`MEMBERS                the members' objids
ENC`<n>`C`<dbref>`<leaf>       a member's copy
```

on the Salvage Union Store, and on the character `SALVAGE`ENCOUNTERS` (joined, in order) and
`SALVAGE`USING` (the `/use` pick). The active copy is a joined encounter running in the
character's room: the pick when it is one, else the last joined. Anywhere else the sheet itself
applies. `/keep` writes a copy onto the sheet; `/end` drops the copies. Duties and `API`CHECK`
with `live` 1 always use the sheet.

## Where the data lives

```
SALVAGE                        the root: wizard, no_command
SALVAGE`LEDGER`<n>             the ledger
SALVAGE`HP, `AP, `TP           the meters; unset is the most (TP the ledger's sum)
SALVAGE`MAX`<HP|AP|SLOTS>      a most of their own
SALVAGE`USED`<BACKGROUND|...>  a re-roll spent until downtime
SALVAGE`SPENT`<kind>`<key>     uses spent until downtime
SALVAGE`MECH`SP, `EP, `HEAT    the mech's meters
SALVAGE`MECH`SCRAP`T<n>        scrap in its cargo
SALVAGE`LAST                   the last check, for re-rolls
```

The Union Crawler is `CRAWLER`*` on the store.

## API

Called with `u()` on the sheet object, as the `duties-salvage-union` provider does: `API`TRAITS`,
`ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET`, `TIER`, `METER`, `ADJUST`, `SCRAP` and
`CHECK`. Each is described where it is defined in `package.yaml`.
