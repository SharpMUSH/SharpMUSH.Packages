# sheet-charge

A Charge character sheet: details, twelve actions rated in dots, momentum, a stress clock with a
condition, and milestones spent on dots and situational talents, plus the game's clocks. Players give
out their starting dots until they are approved and keep their own details, momentum, stress and
condition in play. `+check` rolls one six-sided die per dot and reads the highest against a risk,
which the whole room sees and the game keeps as a recorded roll, and the roll gains momentum.

The sheet keeps two ledgers. The build ledger holds every change to dots, advances and talents. The
milestones ledger holds every milestone given or taken, with the reason. The sheet adds the two up and
caches the totals, so staff can see how a character was built and where its milestones came from, and
undo one step. During chargen, changing an action's dots
rewrites that action's entry instead of adding one, so the ledger keeps one entry per action from chargen. Encounters keep their own
copy of each member's sheet, so a fight that runs for days changes nothing outside it until the GM
keeps its stress and condition.

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
| `+sheet/ledger [<name>]` | all | The entries that build the sheet, oldest first |
| `+sheet/milestones [<name>]` | all | The milestones given and taken, with what is earned, spent and left |
| `+check[/push\|/tension][/private] <action>[+<n>\|-<n>][=<risk> <effect>]` | all | `Alice rolls Muscle (high risk, standard effect): 2d6kh1[(3), 6] = 6: a full success. +2 momentum (4). (roll 42)` |
| `+check/assist <name>` | all | 1 momentum: +1 die on their next action roll |
| `+check/determination <momentum>` | all | Resist a consequence, one die per momentum spent; `/resist` too |
| `+check/fortune <dice>\|<action>` | all | A roll for luck: no momentum, no consequence |
| `+encounter [<n>]` | all | The encounter you are in here, one by number, or every open one |
| `+encounter/start [<title>]` | all | Starts one here, with you as its GM; a room may hold several |
| `+encounter/join [<n>]`, `/leave [<n>]` | all | Takes a copy of your sheet into it, or drops it |
| `+encounter/use <n>` | all | Which of your encounters here your rolls and changes go to |
| `+encounter/add\|remove\|keep <name>[=<n>]` | the GM, keepers | Brings someone in, drops their copy, or writes their copy's stress and condition back to their sheet |
| `+encounter/threat <threat>`, `+encounter/threat <name>=<segments> <risk> <effect>` | the GM, keepers | Brings in a copy of a library threat, or makes one for this encounter |
| `+encounter/danger <name>=<segments>`, `/tick <name>[=<n>]`, `/dismiss <name>` | the GM, keepers | A danger clock; fill or empty a clock by hand; take one out |
| `+encounter/consequence <name>=<kind> [<danger>]` | the GM, keepers | The consequence of a member's last roll there: `stress`, `complication`, `effect`, `risk` or `lost` |
| `+encounter/accept`, `/protect <name>` | members | Take your consequence, or a friend's |
| `+encounter/return <name>` | the GM, keepers | Brings back a member who was taken out |
| `+encounter/milestone [<reason>]` | keepers | A milestone for everyone in it, on their milestones ledgers |
| `+encounter/end [<n>]` | the GM, keepers | Ends it, says which threats were overcome, and drops every copy |
| `+threat`, `+threat <name>` | all | The game's threats, or one with its description and moves |
| `+threat/new <name>=<segments> <risk> <effect>`, `/desc <name>=<text>`, `/moves <name>=<move>\|<move>`, `/remove <name>` | keepers | Keeps the list |
| `+clock`, `+clock <name>` | all | The game's clocks |
| `+clock/new <name>=<segments>` | all | 4, 6 or 8 segments |
| `+clock/tick <name>[=<n>]`, `+clock/remove <name>` | who started it, keepers | Fill (or empty) segments; take it away |

Keepers (`softcode.charge.admin`, the **Charge Sheet Keeper** role) start the argument of `/set`,
`/detail`, `/advance` and `/talent` with `<name>/` (`+sheet/set <name>/<action>=<dots>`), use `<name>=<value>` with `/momentum`, `/stress` and
`/condition`, give milestones with `+sheet/milestone <name>=<n>/<reason>` (the reason goes on the milestones ledger; a negative grant corrects one), take talents off with
`+sheet/talent <name>/<talent>=remove`, undo a ledger entry with `+sheet/revoke <name>/<entry>`, and
start a sheet over with `+sheet/clear <name>=confirm` (the milestones ledger stays).

## Encounters

Joining an encounter copies the member's dots, talents, momentum, stress and condition into it.
While they are in the room where it runs, `+sheet`, `+check` and the momentum, stress and condition
switches use that copy: the encounter they picked with `/use`, else the one they joined last.
Anywhere else, and for milestones, the ledger and Duties, the sheet is used. Each encounter has its
own copies, so encounters never touch each other. Ending one drops its copies; only what the GM kept
with `/keep` (stress and condition) is on the sheet. Momentum and the build never carry back.

NPCs never roll. A threat is a clock the members fill to overcome it, with the risk and effect of
acting against it; a danger clock is filled by complications. `+check <action>=vs <threat>` rolls
with the threat's risk and effect unless others are named before `vs`, and a partial or full success
ticks it 1, 2 or 3 for the effect, one more on a critical. The encounter keeps its own copy of each
threat, so the `+threat` list never changes a running encounter.

After a partial success or a bad outcome the GM picks the consequence, rated by the roll's risk (1
to 3): `stress` (that much stress; a full clock takes the member out until `/return`), `complication`
(a danger clock ticks that much), `effect` (the threat loses one segment of the roll's progress),
`risk` (the threat's risk goes up one) or `lost` (that action won't do it). It waits on the member's
copy until they `/accept` it, resist it with `+check/determination` (4 or 5 takes one off a stress or
complication, a 6 avoids it, two 6s also lower the risk of their next roll there), or a friend takes
it with `/protect`.

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
CHARGE`LEDGER`<n>         a build entry, JSON, wizard-flagged; an entry without the flag is not read
CHARGE`XP`<n>             a milestones entry, JSON, wizard-flagged likewise
CHARGE`TOTALS             the cached totals, JSON, wizard-flagged; worked out from the ledgers when missing
CHARGE`DETAIL`<KEY>       a detail
CHARGE`MOMENTUM           momentum held; unset is the session's start
CHARGE`STRESS             stress clock segments filled; unset is 0
CHARGE`CONDITION          the condition
CHARGE`ASSIST             who spent momentum to help the next action roll
CHARGE`ENCOUNTERS         the encounters the character is in, last joined last
CHARGE`USING              the one picked with +encounter/use
```

A build entry is `{"kind","n","by","phase",...}`: `dots` (`action`, `dots` before advances),
`advance` (`action`), `talent` (`text`), `revoke` (`entry`) and `clear`. `phase` is `chargen`
before approval, `staff` for a keeper, else `play`. Revoked entries and everything before the last
`clear` do not count. A milestones entry is `{"kind":"milestone","n","count","reason","by","phase"}`;
nothing revokes or clears it, and a negative `count` takes milestones.

`CHARGE`TOTALS` is `{"ratings","advanced","talents","given","earned","spent","milestones"}`:
`ratings` and `advanced` are `KEY:n` lists, `talents` a `|`-list, `given` the starting dots handed
out, `earned` the milestones ledger's sum, `spent` one per live advance and talent. Every write to
either ledger rewrites it.

The lists are `+config` tables on **Charge Sheet Store**: `ACTION` (with `SUMMARY` and `ORDER`) and
`DETAIL` (with `ORDER`). Clocks are on the store too: `` CLOCK`<KEY> `` with `SIZE`, `FILLED` and
`OWNER`. So are encounters: `` ENC`<n> `` the title, with `ROOM`, `GM`, `` COPY`<key> `` per member
holding `DOTS`, `TALENTS`, `MOMENTUM`, `STRESS`, `CONDITION`, `LAST` (their last roll there, JSON),
`PENDING` (a consequence waiting, JSON), `OUT` (taken out) and `EASE` (the next roll's risk is
lowered), and `` FOE`<key> `` per threat or danger, the name with `KIND`, `SIZE`, `FILLED`, `RISK`,
`EFFECT`, `DESC` and `MOVES`; `` ENCOUNTER`OPEN `` lists them. The threat list is `` THREAT`<KEY> ``,
the name with `SIZE`, `RISK`, `EFFECT`, `DESC` and `MOVES`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every action `always`), `ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET` (a risk or
difficulty word: the risk), `TIER` (highest die, sixes) and `CHECK` (named `roller`, `trait`,
`modifier` in dice, `target` the risk, `effect`; returns
`{"tier","total","sixes","dice","target","effect","label","text","roll","formula"}`, and never
touches momentum; `live` 1 rolls the sheet even in an encounter). Charge adds `DOTS` (a character's dots in all), `GAIN` (the momentum a tier gains),
`CHARGES` (momentum held), `MOMENTUM` (gives or spends momentum, never below 0, returning the new
count), `STRESSED`, `STRESS` (takes or recovers stress and returns `{"stress","out"}`, out 1 when the
clock filled), `MILESTONES` and `MILESTONE` (gives or takes milestones with a reason, returning the new count).
`RECORD` (writes a ledger entry and returns its number). `RECORD`, `MOMENTUM`, `STRESS` and
`MILESTONE` are the ones that write. `RATING`, `DOTS`, `CHARGES`, `MOMENTUM`, `STRESSED` and `STRESS`
take a last argument, 1 for the character's sheet even when they are in an encounter; without it they
use the encounter's copy there.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **Charge
Sheet** object, as on the d20 sheet.
