# sheet-ironsworn

An Ironsworn character sheet: five stats (Edge, Heart, Iron, Shadow, Wits), health, spirit, supply,
momentum and experience, and iron vows with progress tracks. Players set their stats until they are
approved and keep their own meters and vows in play. `+check` makes an action roll, a six-sided die
plus a stat against two ten-sided challenge dice, which the whole room sees and the game keeps as a
recorded roll; `+vow/fulfil` makes a vow's progress roll.

Based on the Ironsworn SRD under CC BY 4.0: see [NOTICE.md](NOTICE.md). The help and messages are
this package's own wording, and the in-game `+help sheet credits` topic carries the attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-ironsworn-help`](../sheet-ironsworn-help/) | the `+help sheet`, `+help check` and `+help vow` topics |
| [`sheet-ironsworn-config`](../sheet-ironsworn-config/) | the settings and the stat list in `+config ironsworn` |
| [`sheet-ironsworn-chargen`](../sheet-ironsworn-chargen/) | ties stat changes to the player's `+app` application |
| [`duties-ironsworn`](../duties-ironsworn/) | a Duties roll provider called `ironsworn` |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <stat>=<value>` | unapproved player | 1 up to `cap` (3); unset is 1 |
| `+sheet/health`, `/spirit`, `/supply` | player | 0 to 5, starting at 5 |
| `+sheet/momentum` | player | -6 to +10, starting at +2 |
| `+sheet/xp` | player | Experience marked |
| `+sheet/traits` | all | The stats, difficulties and vow ranks |
| `+check[/private] <stat>[+<n>\|-<n>][=<difficulty>]` | all | `Alice rolls Iron: 1d6[3] + 3 = 6 vs 8 and 5: a weak hit (roll 68)` |
| `+vow [<name>]` | all | Your vows, or another character's when you may read them |
| `+vow/swear <vow>=<rank>` | player | troublesome, dangerous, formidable, extreme or epic |
| `+vow/mark <vow>[=<n>]` | player | Mark progress n times (1 when none); below 0 takes it off |
| `+vow/fulfil <vow>` | player | The progress roll; a hit fulfils the vow and marks experience |
| `+vow/forsake <vow>` | player | Take a vow off |

The meter switches take `+<n>`, `-<n>`, `<n>` or `reset`. Keepers (`softcode.ironsworn.admin`, the
**Ironsworn Sheet Keeper** role) put `<name>/` before `/set` (up to 5) and the vow, and use
`<name>=<n>` with the meters.

## The numbers

- The action score is the die plus the stat and any adds, at most 10. The difficulty words add
  `2 1 0 -1 -2` (`+config ironsworn/adds`).
- Beating both challenge dice is `success` (a strong hit), one `partial` (a weak hit), neither `fail`
  (a miss); a tie goes to the die. When the challenge dice match, a strong hit is `crit-success` and a
  miss `crit-fail`.
- A vow's track is ten boxes of four ticks. One mark fills 12 ticks for troublesome, 8 dangerous,
  4 formidable, 2 extreme, 1 epic. The progress score is the full boxes; its roll has no action die.
- Fulfilling marks experience by rank, 1 for troublesome to 5 for epic, one less on a weak hit.

## Where the data lives

```
IRONSWORN                       the root: wizard, no_command
IRONSWORN`STAT`<KEY>            a stat; unset is 1
IRONSWORN`METER`<KEY>           HEALTH, SPIRIT, SUPPLY, MOMENTUM or XP; unset is its start
IRONSWORN`VOW`<KEY>             a vow's name, with RANK and TICKS beneath
```

The stat list is a `+config` table on **Ironsworn Sheet Store**: `STAT` (with `ORDER`).

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every stat `always`, group `stat`), `ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET`
(a difficulty word or a number from -5 to 5: the adds), `TIER` (score and the two challenge dice) and
`CHECK` (named `roller`, `trait`, `modifier` in adds, `target`; returns
`{"tier","action","challenge","match","stat","target","label","text","roll","formula"}`). Ironsworn
adds `METER` (a character's meter) and `ADJUST` (adds to a meter within its range and returns the
new value), the one that writes.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the
**Ironsworn Sheet** object, as on the d20 sheet.
