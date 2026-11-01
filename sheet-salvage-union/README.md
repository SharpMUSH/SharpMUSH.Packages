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
| `+sheet/take <equipment>`, `/drop` | player | The inventory; a new pilot takes two pieces of Tech 1 equipment, an approved one one piece from the Armoury each downtime |
| `+sheet/item <equipment>`, `/list [<tech>]` | all | One piece of equipment; the equipment of a Tech Level |
| `+sheet/use <equipment>` | player | Spends one use |
| `+sheet/hp`, `/ap` `+<n>\|-<n>\|<n>\|reset` | player | The meters |
| `+sheet/callsign`, `/background`, `/motto`, `/keepsake`, `/appearance <text>` | player | The details |
| `+sheet/downtime [<name>]` | keeper | HP, AP, uses, re-rolls and the Armoury's pick back; the mech repaired, recharged and cool |
| `+sheet/ledger [<name>]` | all | Every entry that built the sheet |
| `+sheet/training [<name>]` | all | Every Training Point award and spend |
| `+sheet/tp <name>=+<n> [<reason>]`, `/max <name>/<hp\|ap\|slots>=<n>` | keeper | Training Points, with the reason in their ledger; a pilot's most |
| `+sheet/revoke <name>/<n>`, `/revoke <name>/T<n>`, `/clear <name>` | keeper | Takes back one build entry, one Training Point entry, or the whole build |
| `+sheet/rebuild <name>` | keeper | Writes the sheet and its TP again from the two ledgers |
| `+mech [<name>]` | all | The mech |
| `+mech/chassis <chassis>`, `/install`, `/remove <part>` | unapproved player, keeper | Builds it; a new pilot uses Tech 1 parts within 20 scrap, chassis included |
| `+mech/craft <part>[=<scrap tech>]` | approved player | A new chassis, system or module from the crawler, for its Salvage Value in scrap from the hold |
| `+mech/name`, `/quirk <text>` | player | Its pattern name and quirk |
| `+mech/install`, `/chassis <salvage>` | approved player | Fits salvage the Mech Bay has repaired |
| `+mech/breakdown <salvage>` | player | Breaks a salvaged part into its Salvage Value in scrap, for the crawler's hold |
| `+mech/sp`, `/ep`, `/heat`, `/vent`, `/use <part>` | player | Play |
| `+mech/scrap <tech>=+<n>\|-<n>` | player | Scrap in the cargo |
| `+mech/part <name>`, `/list <chassis\|systems\|modules> [<tech>]` | all | The parts |
| `+check[/private\|/mech] [<what>][=<x>]` | all | The die, with an ability, system or module spending its AP or EP and adding heat |
| `+check/push`, `/reroll <background\|keepsake>`, `/motto <name>`, `/heat` | player | The re-rolls and the heat check |
| `+check/table [<table>]` | all | A roll on a table; nested tables roll on |
| `+crawler`, `/bay [<bay>]` | all | The Union Crawler and its bays |
| `+crawler/unload`, `/trade <n> <tech>=<tech>` | approved player | Scrap from the mech into the hold; scrap traded at its value |
| `+crawler/ledger` | all | Every change to the hold, the upgrade pool and the Tech Level |
| `+crawler/rebuild` | keeper | Writes the hold, the pool and the Tech Level again from that ledger |
| `+crawler/scrap <tech>=+<n> [<reason>]`, `/name`, `/type`, `/weapon`, `/tech`, `/sp`, `/pool`, `/upkeep`, `/upgrade` | keeper | Runs it |
| `+encounter [<n>]`, `/start [<title>]`, `/join [<n>]`, `/leave [<n>]`, `/use <n>` | all | Encounters |
| `+encounter/add`, `/remove`, `/keep <name>[=<n>]`, `/end [<n>]` | GM or keeper | Runs one |
| `+encounter/bestiary [<group or npc>]`, `/stat <npc>` | all | The Core Book's NPCs; one in your encounter |
| `+encounter/npc [<count>] <npc or chassis>[=<n>]`, `/fit <npc>=<part>` | GM or keeper | Adds NPCs, or an enemy mech on a chassis, and arms it |
| `+encounter/act <npc>[/<action>][=<target>[/pilot]]`, `/heal <npc>=<n>` | GM or keeper | Rolls an NPC's action on the NPC Action table, with its damage on a hit |
| `+encounter/initiative`, `/turn [<who>]` | member or GM | Group Initiative: starts a round; marks a turn taken |
| `+encounter/hit <npc>=<n> [HP\|SP]` | member or GM | Damages an NPC |
| `+encounter/salvage <npc>[=<part>]` | member | Salvages a wrecked mech (the Mech Salvage table) or vehicle (its scrap) |
| `+encounter/spoils <name>=<n> <tech>\|<part>` | GM or keeper | Gives what a Bio-Titan or a ruin yields |

Keepers (`softcode.salvage.admin`, the **Salvage Union Sheet Keeper** role) put `<name>/` before
the argument of a build switch to change anyone's sheet at any time, without spending TP.

## The ledgers

A pilot has two ledgers, the build and the Training Points; the Union Crawler has a third, for scrap.
Each is append-only, and what the sheet shows is a cache of it, kept as a running total and written
again from the ledger by the rebuild commands.

A pilot's build is a ledger: `SALVAGE`LEDGER`<n>`, each a wizard-flagged JSON entry with `kind`,
`n`, `by` (objid), `at` (secs), `phase` (`chargen`, `play` or `staff`) and `note`.

| Kind | Fields | Is |
|---|---|---|
| `set` | `leaf`, `value` | the class, a detail, the chassis, a most; the newest standing one wins |
| `grant` | `list`, `key` | an ability, equipment, system or module, in the order granted |
| `revoke` | `entry` | takes one entry back |
| `clear` | | takes back every entry before it |

The sheet's own leaves (`CLASS`, `ABILITIES`, `GEAR`, `PATH`, `DETAIL`*`, `MECH`CHASSIS`,
`MECH`SYSTEMS`, `MECH`MODULES`, ...) are written from the ledger after every entry
(`FUN`LEDGER`REBUILD`). Before approval, choosing a `set` leaf again rewrites the chargen entry,
and taking back a chargen entry wipes it, so the ledger keeps the choices that were made. After
approval every change is a new entry.

Training Points are `SALVAGE`XP`<n>`, wizard-flagged JSON with `kind` (`tp`, or `revoke` with
`entry`), `amount`, `n`, `by`, `at`, `phase`, `note`, and `for`: the build entry a spend paid for or
a refund pays back. Each entry adds its amount to `SALVAGE`TP` (`FUN`XP`ADD`); `FUN`XP`REBUILD`
writes the sum of the entries still standing. Taking back a build entry, one at a time or with
`/clear`, pays back what was spent on it in a `tp` entry of its own; `+sheet/unlearn` pays nothing
back and costs 1 TP. A `/revoke <name>/T<n>` that would leave the pilot below 0 is refused.

## Advancement

What a pilot, their mech and the crew gain is audited:

- Training Points come only from staff (`+sheet/tp <name>=+<n> <reason>`) and from Duties, each a `tp` entry with its note in the Training Point ledger; `+sheet/learn` spends them in entries of its own, each pointing at the build entry it paid for.
- Scrap enters the Union Crawler's hold from staff (`+crawler/scrap`), a pilot's `+crawler/unload`, and Duties. `+mech/craft` spends it on chassis, systems and modules at the crawler's Tech Level or lower, `+crawler/trade` swaps it, and upkeep and upgrades move it into the pool and the Tech Level.
- Equipment comes from the Armoury, one piece each downtime, or from staff.

The crawler's ledger is `CRAWLER`LEDGER`<n>` on the store: JSON with `kind` (`scrap`, `pool` or `tech`), `n`, `by`, `at`, `for` (the pilot), `note`, and `tech` and `amount`. Amounts are the change made, and no entry is rewritten or removed. `CRAWLER`SCRAP`T<n>`, `CRAWLER`POOL` and `CRAWLER`TECH` are its cache: each entry updates them, and `FUN`CRAWLER`REBUILD` adds the entries up again in order, never below 0.

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
applies. `/keep` writes a copy onto the sheet, and the member's salvage with it; `/end` drops the copies. Duties and `API`CHECK`
with `live` 1 always use the sheet.

An encounter's NPCs are on the store too:

```
ENC`<n>`NPCS, `NNEXT            their numbers; the last used
ENC`<n>`N`<id>                  its name
ENC`<n>`N`<id>`FROM             NPC:<key> (Salvage Union Data's NPC`<key>) or CHASSIS:<key>
ENC`<n>`N`<id>`KIND, `HEALTH    npc, vehicle, bio-titan or mech; hp or sp
ENC`<n>`N`<id>`MAX, `NOW        its most; now (unset is the most)
ENC`<n>`N`<id>`TECH, `VALUE     what salvaging it gives
ENC`<n>`N`<id>`PARTS            an enemy mech's SYSTEM:<key> and MODULE:<key>
ENC`<n>`N`<id>`SBY, `SROLL, `PICKS  who salvaged it, the Mech Salvage roll, what it still allows
ENC`<n>`ROUND, `ACTED, `FIRST   the round, who has acted (objids and N<id>), the Group Initiative die
ENC`<n>`S`<dbref>               a member's salvage waiting to be kept: scrap:<tech>:<n>, part:<KIND>:<key>
```

Kept scrap goes into the crawler's hold as a ledger entry for the member. Kept parts are `grant`
entries on the `MECH`SALVAGE` list (damaged), keyed `<KIND>:<key>`. Downtime moves each one of the
crawler's Tech Level or lower to `MECH`SPARES` (repaired), where `+mech/install` and `/chassis`
take it, and `+mech/breakdown` takes either for scrap.

## Where the data lives

```
SALVAGE                        the root: wizard, no_command
SALVAGE`LEDGER`<n>             the build ledger
SALVAGE`XP`<n>                 the Training Point ledger
SALVAGE`HP, `AP                the meters; unset is the most
SALVAGE`TP                     the Training Points, a cache of SALVAGE`XP`
SALVAGE`MAX`<HP|AP|SLOTS>      a most of their own
SALVAGE`USED`<BACKGROUND|...>  a re-roll spent until downtime
SALVAGE`SPENT`<kind>`<key>     uses spent until downtime
SALVAGE`MECH`SP, `EP, `HEAT    the mech's meters
SALVAGE`MECH`SCRAP`T<n>        scrap in its cargo
SALVAGE`MECH`SALVAGE, `SPARES  salvaged parts, damaged and repaired
SALVAGE`LAST                   the last check, for re-rolls
```

The Union Crawler is `CRAWLER`*` on the store.

## API

Called with `u()` on the sheet object, as the `duties-salvage-union` provider does: `API`TRAITS`,
`ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET`, `TIER`, `METER`, `ADJUST`, `SCRAP` and
`CHECK`. Each is described where it is defined in `package.yaml`.
