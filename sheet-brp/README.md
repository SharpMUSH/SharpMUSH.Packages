# sheet-brp

A percentile character sheet on the Basic Roleplaying rules: seven characteristics (STR, CON, SIZ,
INT, POW, DEX, CHA), hit points and power points, the six characteristic rolls, and a skill list with
base chances that the game edits. Players fill in their sheet until they are approved and keep their
own hit points and power points in play. `+check` rolls 1d100 under a skill or characteristic roll,
which the whole room sees and the game keeps as a recorded roll.

The characteristics, characteristic rolls, skill list, base chances and categories are ORC Licensed
Material from Basic Roleplaying: Universal Game Engine: see [NOTICE.md](NOTICE.md) for the ORC
notice, the attribution, the Reserved Material and what this package designates as Licensed
Material. The help and messages are this package's own wording, and the in-game
`+help sheet credits` topic carries the attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-brp-help`](../sheet-brp-help/) | the `+help sheet` and `+help check` topics |
| [`sheet-brp-config`](../sheet-brp-config/) | the settings and the skill list in `+config brp` |
| [`sheet-brp-chargen`](../sheet-brp-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-brp`](../duties-brp/) | a Duties roll provider called `brp` |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <characteristic>=<value>` | unapproved player | 1 up to `charcap` (18); unset is 10 |
| `+sheet/set <skill>=<percent>` | unapproved player | 0 up to `skillcap` (75); empty puts it back to its base |
| `+sheet/hp`, `+sheet/pp` `-<n>\|+<n>\|<n>\|full` | player | Hit points and power points left |
| `+sheet/traits` | all | The characteristics, and the skills with their base chances |
| `+check[/private] <skill>[+<n>\|-<n>][=<difficulty>]` | all | `Alice rolls Climb (55%, difficult, halved: 28%): 1d100[23] = 23: a success (roll 9)` |

Keepers (`softcode.brp.admin`, the **BRP Sheet Keeper** role) put `<name>/` before `/set` (up to 99
and 999%), and use `<name>=<n>` with `/hp` and `/pp`.

## The numbers

- A characteristic roll is five times the characteristic: Effort (STR), Stamina (CON), Idea (INT),
  Luck (POW), Agility (DEX), Charm (CHA). SIZ has none.
- A skill's base is a number or a characteristic sum such as `DEX*2` or `INT+POW`.
- Difficulty: automatic needs no roll, easy doubles the chance, average leaves it, difficult halves
  it (rounded up), impossible fails. The difficulty words map to these (`+config brp/difficulty`).
  A modifier applies after.
- Equal to or under the chance succeeds. A twentieth of the chance or less (rounded up) is
  `critical`, a fifth or less `special`; both count as success, critical as `crit-success`. A roll of
  `95 + chance/20` (rounded up, at most 100) or more is a fumble, `crit-fail`. A skill with a base of 5% or
  more succeeds on 01 to 05.
- Hit points are CON plus SIZ, halved and rounded up (`+config brp/hitpoints=total` adds them
  instead); power points equal POW.

## Where the data lives

```
BRP                     the root: wizard, no_command
BRP`CHAR`<KEY>          a characteristic; unset is 10
BRP`SKILL`<KEY>         a skill's percentage; unset is its base
BRP`HP, BRP`PP          what is left; unset is the most
```

The skill list is a `+config` table on **BRP Sheet Store**: `SKILL` (with `BASE` and `CATEGORY`).
The characteristics are `CHAR`, with `ROLL` and `ORDER`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (characteristic rolls in group `characteristic`, skills in their category; `always` for the
rolls and every skill with a base above 0), `ALWAYS`, `FIND`, `LABEL`, `RATING` (the percentage),
`TRAINED` (a skill above its base), `HAS`, `TARGET` (a difficulty word or level: the level), `TIER`
(a success level: the tier) and `CHECK` (named `roller`, `trait`, `modifier` in percent, `target`;
returns `{"tier","level","total","rating","chance","target","label","text","roll","formula"}`). BRP
adds `MOST` and `LEFT` (a character's most and remaining HP or PP), `RAISE` (adds percent to a skill,
returning the new percentage) and `HEAL` (gives back HP or PP, never past the most). `RAISE` and
`HEAL` are the ones that write.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **BRP
Sheet** object, as on the d20 sheet.
