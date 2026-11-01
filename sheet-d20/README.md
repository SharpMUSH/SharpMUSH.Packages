# sheet-d20

A d20 character sheet: six ability scores, a level, and a skill list the game edits, each skill
untrained, trained or expert. Players fill in their own sheet until they are approved, and roll
against it with `+check`, which the whole room sees and the game keeps as a recorded roll.

The rules are generic d20 mechanics written for this package; no rulebook text is used.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-d20-help`](../sheet-d20-help/) | the `+help sheet` and `+help check` topics |
| [`sheet-d20-config`](../sheet-d20-config/) | the settings and the trait table in `+config d20` |
| [`sheet-d20-chargen`](../sheet-d20-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-d20`](../duties-d20/) | a Duties roll provider called `d20` |

`sheet-d20` and `sheet-fate` both answer `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <trait>=<value>` | unapproved player | Set a score (`str=14`), a skill's training (`athletics=trained`) or `level=3`; an empty value clears it |
| `+sheet/set <name>/<trait>=<value>` | keeper | The same on anyone's sheet, at any time; scores up to 30 |
| `+sheet/traits` | all | Every trait, its key, and what it adds |
| `+check[/private][/advantage\|/disadvantage] <trait>[+<n>\|-<n>][=<DC or difficulty>]` | all | Roll 1d20 plus the trait for the room: `Alice checks Athletics: 1d20[13] + 6 = 19 vs DC 15: success (roll 13)` |

A keeper holds `softcode.d20.admin`, which the **D20 Sheet Keeper** role grants. A character reads
their own sheet; keepers read every sheet; `+config d20/public=yes` lets anyone read anyone's.

## The numbers

- An ability adds `(score - 10) / 2`, rounded down.
- A skill adds its ability's modifier, plus the training bonus when trained, twice it when expert.
- The training bonus is `bonus-base` (2) at level 1 and grows by 1 every `bonus-every` (4) levels.
- A check meets its DC to succeed. With `crits` on, a natural 20 is `crit-success` and a natural 1
  `crit-fail`, whatever the total.
- The difficulty words trivial, easy, standard, hard and extreme are DC 5, 10, 15, 20 and 25
  (`+config d20/dcs`).

## Where the data lives

A character's sheet is their own attributes, wizard-flagged so only the sheet object writes them:

```
D20                 the root: wizard, no_command
D20`<TRAIT>         an ability's score, or a skill's training (0, 1 or 2)
D20`LEVEL           the level
```

The traits are a `+config` table on **D20 Sheet Store**: `TRAIT`<KEY>` holds the label, with `KIND`
(ability or skill), `ABILITY` (a skill's ability key) and `ORDER` beneath.

## The sheet API

Every sheet package (`sheet-d20`, `sheet-fate`, and the ones that follow) has the same `API` tree on
its sheet object, so a bridge such as a Duties provider is written the same way for each. The
attributes are VISUAL on a WIZARD object, so only code at least that privileged calls them
(`safer_ufun`). They read and roll, and write nothing.

| Attribute | Arguments | Returns |
|---|---|---|
| `` API`TRAITS `` | | `[{"key","label","group","always"}]`; always is true for the abilities |
| `` API`ALWAYS `` | | the keys anyone can roll, a space list |
| `` API`FIND `` | typed text | the key it names, or nothing |
| `` API`LABEL `` | key | its label |
| `` API`RATING `` | character, key | what it adds to a roll |
| `` API`TRAINED `` | character, key | 1 when trained (abilities always) |
| `` API`HAS `` | character | 1 when anything is set on their sheet |
| `` API`TARGET `` | DC or difficulty word | the DC, or nothing |
| `` API`TIER `` | total, natural die, DC | `crit-fail`, `fail`, `success`, `crit-success`, or nothing without a DC |
| `` API`CHECK `` | named: `roller`, `trait`, `modifier`, `target`, `dice` (`1d20`, `2d20kh`, `2d20kl`) | `{"tier","total","natural","target","margin","label","text","roll","formula"}`, the roll kept with `roll(...,record)` |

## What a bridge may set

On the **D20 Sheet** object:

- `` HINT`<message> `` adds a line to one of the sheet's messages (`SWITCHES`, `SET`, `FOOTER`).
- `` GATE`EDIT `` (`%0` the player) gives a reason a player may not change their own sheet now, or nothing.
- `` ALLOW`VIEW`<name> `` (`%0` who asks, `%1` whose sheet) lets more people read a sheet.
