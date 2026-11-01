# sheet-fitd

A Forged in the Dark character sheet: twelve actions rated 0 to 4 under Insight, Prowess and
Resolve, stress, trauma, harm and coin, plus the game's progress clocks. Players rate their actions
until they are approved and keep their own stress, trauma, harm and coin in play. `+check` rolls
one six-sided die per point of an action and reads the highest against a position, which the whole
room sees and the game keeps as a recorded roll.

Based on the Blades in the Dark SRD under CC BY 3.0: see [NOTICE.md](NOTICE.md). The help and
messages are this package's own wording, and the in-game `+help sheet credits` topic carries the
attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-fitd-help`](../sheet-fitd-help/) | the `+help sheet`, `+help check` and `+help clock` topics |
| [`sheet-fitd-config`](../sheet-fitd-config/) | the settings and the action and attribute lists in `+config fitd` |
| [`sheet-fitd-chargen`](../sheet-fitd-chargen/) | ties rating changes to the player's `+app` application |
| [`duties-fitd`](../duties-fitd/) | a Duties roll provider called `fitd` |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <action>=<rating>` | unapproved player | 0 up to `cap` (2) |
| `+sheet/stress +<n>\|-<n>\|<n>\|clear` | player | Past the most (9) stress clears and a trauma is due |
| `+sheet/trauma <trauma>` | player | Mark a trauma; at the fourth the character retires |
| `+sheet/harm <level>=<harm>` | player | Level 1 to 3; a full level pushes harm up one. Empty clears the level |
| `+sheet/coin -<n>` | player | Spend coin |
| `+sheet/traits` | all | The actions and their attributes |
| `+check[/private] <action>[+<n>\|-<n>][=<position>]` | all | `Alice rolls Skirmish (risky): 2d6kh1[(3), 6] = 6: a full success (roll 42)` |
| `+check/resist <attribute>` | all | Rolls the attribute and marks 6 less the highest die in stress; two 6s clear 1 |
| `+clock`, `+clock <name>` | all | The game's clocks |
| `+clock/new <name>=<segments>` | all | 4, 6, 8 or 12 segments |
| `+clock/tick <name>[=<n>]`, `+clock/remove <name>` | who started it, keepers | Fill (or empty) segments; take it away |

Keepers (`softcode.fitd.admin`, the **FitD Sheet Keeper** role) put `<name>/` before `/set`,
`/trauma` and `/harm`, use `<name>=<n>` with `/stress` and `/coin`, and take traumas off with
`+sheet/trauma <name>/<trauma>=remove`.

## The numbers

- One die per rating; a rating of 0 rolls two dice and keeps the lower.
- The highest die: 6 is `success`, 4 or 5 `partial`, 1 to 3 `fail`. Two 6s or more (from one die
  or more) are `crit-success`.
- An attribute's rating is how many of its actions are rated 1 or more.
- The difficulty words map to positions (`+config fitd/positions`) and dice (`+config fitd/dice`).
  `none` means no roll: it succeeds.

## Where the data lives

```
FITD                    the root: wizard, no_command
FITD`ACTION`<KEY>       an action's rating; unset is 0
FITD`STRESS             stress marked; unset is 0
FITD`TRAUMA             traumas, a |-list
FITD`HARM`<SLOT>        harm in slot 1A, 1B, 2A, 2B or 3A
FITD`COIN               coin; unset is 0
```

The lists are `+config` tables on **FitD Sheet Store**: `ACTION` (with `ATTRIBUTE` and `ORDER`) and
`ATTRIBUTE`. Clocks are on the store too: `` CLOCK`<KEY> `` with `SIZE`, `FILLED` and `OWNER`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every action `always`, its attribute as `group`), `ALWAYS`, `FIND`, `LABEL`, `RATING`,
`HAS`, `TARGET` (a position or difficulty word: the position), `TIER` (highest die, sixes) and
`CHECK` (named `roller`, `trait`, `modifier` in dice, `target`; returns
`{"tier","total","sixes","dice","target","label","text","roll","formula"}`). FitD adds `ATTRIBUTE`
(a character's dice in an attribute), `STRESSED` (stress marked), `STRESS` (marks or clears stress and
returns `{"stress","trauma"}`, trauma 1 when one is due), `COIN` and `AWARD` (gives or takes coin,
never below 0, returning the new count). `STRESS` and `AWARD` are the ones that write.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **FitD
Sheet** object, as on the d20 sheet.
