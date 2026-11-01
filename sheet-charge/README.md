# sheet-charge

A Charge character sheet: details, twelve actions rated in dots, momentum, a stress clock with a
condition, and milestones spent on dots and situational talents, plus the game's clocks. Players give
out their starting dots until they are approved and keep their own details, momentum, stress and
condition in play. `+check` rolls one six-sided die per dot and reads the highest against a risk,
which the whole room sees and the game keeps as a recorded roll, and the roll gains momentum.

Based on the Charge SRD under CC BY 4.0, which is based on Blades in the Dark under CC BY 3.0: see
[NOTICE.md](NOTICE.md). The action descriptions are the SRD's; the help and messages are this
package's own wording, and the in-game `+help sheet credits` topic carries both attributions.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-charge-help`](../sheet-charge-help/) | the `+help sheet`, `+help check` and `+help clock` topics |
| [`sheet-charge-config`](../sheet-charge-config/) | the settings and the action and detail lists in `+config charge` |
| [`sheet-charge-chargen`](../sheet-charge-chargen/) | ties giving out dots to the player's `+app` application |
| [`duties-charge`](../duties-charge/) | a Duties roll provider called `charge` |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <action>=<dots>` | unapproved player | `dots` (7) to give out, at most `cap` (2) in one action |
| `+sheet/detail <detail>=<text>` | player | Concept, appearance, ties; empty clears |
| `+sheet/momentum +<n>\|-<n>\|<n>\|session` | player | `session` sets it to `momentum` (2) |
| `+sheet/stress +<n>\|-<n>\|<n>\|clear` | player | When the clock (4) fills, taken out for the scene, and it clears |
| `+sheet/condition <condition>` | player | Empty clears |
| `+sheet/advance <action>` | player | Spend a milestone on a dot, up to 4 |
| `+sheet/talent <talent>` | player | Spend a milestone on a situational talent |
| `+sheet/traits` | all | The actions and what each is for |
| `+check[/push\|/tension][/private] <action>[+<n>\|-<n>][=<risk> <effect>]` | all | `Alice rolls Muscle (high risk, standard effect): 2d6kh1[(3), 6] = 6: a full success. +2 momentum (4). (roll 42)` |
| `+check/assist <name>` | all | 1 momentum: +1 die on their next action roll |
| `+check/determination <momentum>` | all | Resist a consequence, one die per momentum spent; `/resist` too |
| `+check/fortune <dice>\|<action>` | all | A roll for luck: no momentum, no consequence |
| `+clock`, `+clock <name>` | all | The game's clocks |
| `+clock/new <name>=<segments>` | all | 4, 6 or 8 segments |
| `+clock/tick <name>[=<n>]`, `+clock/remove <name>` | who started it, keepers | Fill (or empty) segments; take it away |

Keepers (`softcode.charge.admin`, the **Charge Sheet Keeper** role) put `<name>/` before `/set`,
`/detail`, `/advance` and `/talent`, use `<name>=<value>` with `/momentum`, `/stress` and
`/condition`, give milestones with `+sheet/milestone <name>=<n>`, and take talents off with
`+sheet/talent <name>/<talent>=remove`.

## The numbers

- One die per dot; an action with no dots rolls two dice and keeps the lower, and can't be a critical.
- The highest die: 6 is `success`, 4 or 5 `partial`, 1 to 3 `fail`. Two 6s or more are
  `crit-success`.
- Risk is low, moderate (the default) or high; a partial success or a bad outcome names the
  consequence rating, 1, 2 or 3. Effect is limited, standard (the default) or great.
- An action roll gains momentum from the `gain` dial (`1 2 3`: partial, success, critical), unless
  momentum was spent on it: a push (2 of the roller's) or an assist (1 of the helper's). Tension adds a
  die and spends nothing.
- A character who never had momentum holds `momentum` (2).
- The difficulty words map to risks (`+config charge/risks`) and dice (`+config charge/dice`). `none`
  means no roll: it succeeds.

## Where the data lives

```
CHARGE                    the root: wizard, no_command
CHARGE`ACTION`<KEY>       an action's dots; unset is 0
CHARGE`DETAIL`<KEY>       a detail
CHARGE`MOMENTUM           momentum held; unset is the session's start
CHARGE`STRESS             stress clock segments filled; unset is 0
CHARGE`CONDITION          the condition
CHARGE`MILESTONES         milestones to spend; unset is 0
CHARGE`TALENT             situational talents, a |-list
CHARGE`ASSIST             who spent momentum to help the next action roll
```

The lists are `+config` tables on **Charge Sheet Store**: `ACTION` (with `SUMMARY` and `ORDER`) and
`DETAIL` (with `ORDER`). Clocks are on the store too: `` CLOCK`<KEY> `` with `SIZE`, `FILLED` and
`OWNER`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every action `always`), `ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET` (a risk or
difficulty word: the risk), `TIER` (highest die, sixes) and `CHECK` (named `roller`, `trait`,
`modifier` in dice, `target` the risk, `effect`; returns
`{"tier","total","sixes","dice","target","effect","label","text","roll","formula"}`, and never
touches momentum). Charge adds `DOTS` (a character's dots in all), `GAIN` (the momentum a tier gains),
`CHARGES` (momentum held), `MOMENTUM` (gives or spends momentum, never below 0, returning the new
count), `STRESSED`, `STRESS` (takes or recovers stress and returns `{"stress","out"}`, out 1 when the
clock filled), `MILESTONES` and `MILESTONE` (gives or takes milestones, returning the new count).
`MOMENTUM`, `STRESS` and `MILESTONE` are the ones that write.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **Charge
Sheet** object, as on the d20 sheet.
