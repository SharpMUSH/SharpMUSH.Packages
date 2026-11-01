# sheet-ironsworn

An Ironsworn character sheet: five stats (Edge, Heart, Iron, Shadow, Wits) and assets built from a
ledger, health, spirit, supply and momentum, experience spent on new assets and their abilities with
an audited log, companion health, iron vows with progress tracks, and encounters that play from
copies of the sheets. Players give out their starting stats and take their starting assets until they
are approved, then spend experience, and keep their own meters and vows in play. `+check` makes an
action roll, a six-sided die plus a stat against two ten-sided challenge dice, which the whole room
sees and the game keeps as a recorded roll; `+vow/fulfil` makes a vow's progress roll.

Based on the Ironsworn SRD under CC BY 4.0: see [NOTICE.md](NOTICE.md). The help, the messages and
the starting assets are this package's own wording, and the in-game `+help sheet credits` topic
carries the attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-ironsworn-help`](../sheet-ironsworn-help/) | the `+help sheet`, `+help check`, `+help vow` and `+help encounter` topics |
| [`sheet-ironsworn-config`](../sheet-ironsworn-config/) | the settings and the stat and asset lists in `+config ironsworn` |
| [`sheet-ironsworn-chargen`](../sheet-ironsworn-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-ironsworn`](../duties-ironsworn/) | a Duties roll provider called `ironsworn` |
| [`ironsworn-wiki`](../ironsworn-wiki/) | wiki pages on playing with the sheet |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/chargen [<name>]` | all | The steps of making a character, and what to do next |
| `+sheet/set <stat>=<value>` | unapproved player | Gives a stat one of the starting values (`array`, `3 2 2 1 1`); empty frees it |
| `+sheet/asset <asset>[=remove]` | player | Unapproved: takes one of the starting assets (`starting`, 3) or gives it back. Approved: a new asset for `newasset` (3) experience |
| `+sheet/upgrade <asset>` | approved player | Marks the asset's next ability for `upgrade` (2) experience |
| `+sheet/assets [<asset>]` | all | The assets, or one asset's three abilities |
| `+sheet/ledger [<name>]` | all | Every entry the stats and assets are built from |
| `+sheet/log [<name>]` | all | Every change to experience, who made it and why |
| `+sheet/health`, `/spirit`, `/supply` | player | 0 to 5, starting at 5 |
| `+sheet/momentum` | player | -6 to +10, starting at +2 |
| `+sheet/companion <asset>=<n>` | player | A companion's health, 0 up to its most |
| `+sheet/traits` | all | The stats, difficulties and vow ranks |
| `+check[/private] <stat>[+<n>\|-<n>][=<difficulty>]` | all | `Alice rolls Iron: 1d6[3] + 3 = 6 vs 8 and 5: a weak hit (roll 68)` |
| `+vow [<name>]` | all | Your vows, or another character's when you may read them |
| `+vow/swear <vow>=<rank>` | player | troublesome, dangerous, formidable, extreme or epic |
| `+vow/mark <vow>[=<n>]` | player | Mark progress n times (1 when none); below 0 takes it off |
| `+vow/fulfil <vow>` | player | The progress roll; a hit fulfils the vow and marks experience |
| `+vow/forsake <vow>` | player | Take a vow off |
| `+encounter [<n>]` | all | The encounters here and yours, or one |
| `+encounter/start [<title>]`, `/join [<n>]`, `/leave [<n>]`, `/use <n>` | all | Start, join, leave, pick which copy you roll from |
| `+encounter/add <name>[=<n>]`, `/remove`, `/keep`, `/end [<n>]` | its GM, keepers | Run it; `/keep` writes a copy back to the sheet |

The meter and companion switches take `+<n>`, `-<n>`, `<n>` or `reset`. Keepers
(`softcode.ironsworn.admin`, the **Ironsworn Sheet Keeper** role) put `<name>/` before `/set`,
`/asset`, `/upgrade`, `/companion` and the vow, and use `<name>=<n>` with the meters. They set any stat
from 1 to 5, give assets and abilities without experience, take an asset away with `=remove`, and have
three more switches:

| Command | What |
|---|---|
| `+sheet/xp <name>=+<n> [<reason>]` | Gives experience; `-<n>` takes, `<n>` sets |
| `+sheet/revoke <name>/<n>` | Takes back one ledger entry |
| `+sheet/clear <name>` | Revokes every entry; character creation starts again. Experience, meters and vows stay |

The GM of an encounter changes the meters and companions of anyone playing from its copies.

## The numbers

- The action score is the die plus the stat and any adds, at most 10. The difficulty words add
  `2 1 0 -1 -2` (`+config ironsworn/adds`). An unassigned stat counts as 1.
- Beating both challenge dice is `success` (a strong hit), one `partial` (a weak hit), neither `fail`
  (a miss); a tie goes to the die. When the challenge dice match, a strong hit is `crit-success` and a
  miss `crit-fail`.
- A vow's track is ten boxes of four ticks. One mark fills 12 ticks for troublesome, 8 dangerous,
  4 formidable, 2 extreme, 1 epic. The progress score is the full boxes; its roll has no action die.
- Fulfilling marks experience by rank, 1 for troublesome to 5 for epic, one less on a weak hit.

## Character creation

`+sheet/chargen` shows three steps: give every stat one of the starting values, take the starting
assets, and swear a background vow. A new asset comes with its first ability marked.

## The ledger

A character's stats and assets are their ledger, `IRONSWORN`LEDGER`<n>`: one JSON entry per step, each
with the `wizard` attribute flag so only the sheet object or a wizard writes one; an entry without the
flag is not read.

| Kind | Fields | What it does |
|---|---|---|
| `stat` | `key`, `value` | A stat, 1 to 5, or empty for unassigned; a later one replaces it |
| `asset` | `key`, `value` | An asset's abilities marked, 1 to 3, or 0 for given back; a later one replaces it |
| `revoke` | `value` | Takes back entry `value` |
| `clear` | | Every entry before it stops counting |

Every entry also has `n`, `phase` (`chargen`, `play` or `staff`), `by` (an objid) and `at` (secs).
Before approval a player's change rewrites their own `chargen` entry for that stat or asset; every
other change is a new entry. A ledger holds at most 200 entries.

## The log

Every change to experience is an entry in the character's log, `IRONSWORN`LOG`<n>`, with the `wizard`
attribute flag: `kind` (`xp`), `delta`, `total` after, `reason`, `by` and `at`. A keeper's `/xp` takes a
reason after the number; spending logs the asset or ability bought, fulfilling a vow logs the vow,
and `API`AWARD` (Duties rewards) logs its reason. A log keeps the latest 500 entries.

## Encounters

An encounter is a scene played from copies of the sheets. A room may hold several, and a character
may be in several. A copy is taken when someone joins, from their sheet as it is then. While a
character is in the room of an encounter they joined, `+check`, the meters and `+sheet/companion` use
that copy: the one `/use` picked, else the last one joined. Anywhere else the sheet applies. An
encounter lasts until `/end`, over any number of days; `/end` drops every copy, and `/keep` first
writes one character's meters and companions' health back to their sheet. Nothing one encounter does
touches another, or the sheet. Vows and experience stay on the sheet.

The Duties provider and every `API`` function always use the sheet itself.

## Where the data lives

```
IRONSWORN                       the root: wizard, no_command
IRONSWORN`LEDGER`<n>            a ledger entry
IRONSWORN`METER`<KEY>           HEALTH, SPIRIT, SUPPLY or MOMENTUM; unset is its start
IRONSWORN`COMPANION`<ASSET>     a companion's health; unset is its most
IRONSWORN`XP                    experience to spend; unset is 0
IRONSWORN`LOG`<n>               a log entry
IRONSWORN`VOW`<KEY>             a vow's name, with RANK and TICKS beneath
IRONSWORN`ENCOUNTERS            the encounters they are in, in the order they joined
IRONSWORN`USING                 the encounter /use picked
```

On **Ironsworn Encounters**: `ENC`<n>` the title, with `ROOM`, `GM`, `STARTED` and `COPY`<dbref
number>`, each member's copy, with `STATS` (`IRON=3 HEART=2 ...`, or `none`), `ASSETS` (`HOUND=2 ...`,
or `none`), `METER`<KEY>` and `COMPANION`<ASSET>` beneath.

The lists are `+config` tables on **Ironsworn Sheet Store**: `STAT` (with `ORDER`) and `ASSET` (with
`TYPE`, `HEALTH`, `FIRST`, `SECOND`, `THIRD` and `ORDER`). The twelve starting assets are a sample in
this package's own words; staff add the rest with `+config ironsworn/assets`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every stat `always`, group `stat`), `ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET`
(a difficulty word or a number from -5 to 5: the adds), `TIER` (score and the two challenge dice) and
`CHECK` (named `roller`, `trait`, `modifier` in adds, `target`; returns
`{"tier","action","challenge","match","stat","target","label","text","roll","formula"}`). Ironsworn
adds `ASSET` (the abilities a character has marked on an asset), `METER` (a character's meter),
`ADJUST` (adds to a meter within its range and returns the new value; `XP` gives experience as
`AWARD` does), `XP` (experience to spend) and `AWARD` (`%0` a character, `%1` experience to give or
take, `%2` why, `Reward` when empty: never below 0, logged, returns the new count). `ADJUST` and
`AWARD` are the ones that write.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the
**Ironsworn Sheet** object, as on the d20 sheet.
