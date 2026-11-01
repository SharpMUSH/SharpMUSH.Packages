# sheet-fate

A Fate character sheet: skills on the ladder (or the six approaches), aspects, stress tracks,
consequences, fate points and refresh. Players fill in their skills and aspects until they are
approved, keep their own stress, consequences and fate points in play, and roll four Fate dice
against an opposition with `+check`, which the whole room sees and the game keeps as a recorded roll.

Based on the Fate Core, Fate Accelerated and Fate Condensed SRDs under CC BY 3.0: see
[NOTICE.md](NOTICE.md). The help and messages are this package's own wording, and the in-game
`+help sheet credits` topic carries the attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-fate-help`](../sheet-fate-help/) | the `+help sheet` and `+help check` topics |
| [`sheet-fate-config`](../sheet-fate-config/) | the settings and the four lists in `+config fate` |
| [`sheet-fate-chargen`](../sheet-fate-chargen/) | ties rating and aspect changes to the player's `+app` application |
| [`duties-fate`](../duties-fate/) | a Duties roll provider called `fate` |

`sheet-fate` and `sheet-d20` both answer `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <skill>=<rating>` | unapproved player | A number from -2 up to `cap`, or a ladder word: `fight=3`, `notice=fair` |
| `+sheet/aspect <slot>=<aspect>` | unapproved player | `concept`, `trouble`, or a number |
| `+sheet/stress <track>=<box>` | player | Mark a box; `=clear` empties the track |
| `+sheet/recover` | player | Clear every stress box |
| `+sheet/consequence <slot>=<aspect>` | player | Take a consequence; empty clears it |
| `+sheet/spend [<what for>]` | player | Spend a fate point where the room sees it |
| `+sheet/award <name>[=<n>]` | keeper | Give fate points, or take them with a number below 0 |
| `+sheet/refresh <name>[=<n>\|default]` | keeper | Bring their points up to their refresh, or set it |
| `+sheet/traits` | all | The skills or approaches, and the ladder |
| `+check[/private] <skill>[+<n>\|-<n>][=<opposition>]` | all | Roll 4dF plus the rating: `Bob rolls Fight: 4dF[-1, 0, 1, 0] + 4 = 4 (Great) against Fair (+2): success, 2 shifts (roll 20)` |

Keepers (`softcode.fate.admin`, the **Fate Sheet Keeper** role) put `<name>/` before the slot of
`/set`, `/aspect`, `/stress` and `/consequence` to change anyone's sheet at any time.

## The numbers

- Shifts are the total less the opposition. Below 0 is `fail`, 0 is `partial` (a tie), 1 or 2
  `success`, 3 or more `crit-success` (success with style).
- The difficulty words are oppositions +0 to +4 (`+config fate/opposition`). A ladder word or a
  number works too.
- In `skills` mode the sheet warns when more skills sit at a rating than at the one below it
  (`pyramid`).

## Where the data lives

```
FATE                        the root: wizard, no_command
FATE`RATING`<KEY>           a skill's or approach's rating; unset is Mediocre (+0)
FATE`ASPECT`<SLOT>          CONCEPT, TROUBLE, 1, 2, ...
FATE`STRESS`<TRACK>         the marked boxes, a space list
FATE`CONSEQUENCE`<SLOT>     a consequence
FATE`POINTS                 fate points; unset is the refresh
FATE`REFRESH                a refresh of their own; unset is the game's
```

The lists are `+config` tables on **Fate Sheet Store**: `SKILL`, `APPROACH`, `TRACK` (with `BOXES`)
and `CONSEQUENCE` (with `SHIFTS`).

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every one `always`), `ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET` (difficulty,
ladder word or number), `TIER` (from the shifts) and `CHECK` (named `roller`, `trait`, `modifier`,
`target`; returns `{"tier","total","shifts","target","margin","label","text","roll","formula"}`).
Fate adds `LADDER` (a rating's word), `POINTS` (a character's fate points) and `AWARD` (gives or
takes fate points, never below 0, and returns the new count): the one API attribute that writes.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **Fate
Sheet** object, as on the d20 sheet.
