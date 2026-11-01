# sheet-pbta

A Powered by the Apocalypse character sheet: stats, moves and playbooks the game edits, forward,
ongoing, hold and XP. Players pick a playbook, set their stats and take moves until they are approved,
keep their own forward, ongoing and hold in play, and make moves with `+check`: two six-sided dice plus
a stat, which the whole room sees and the game keeps as a recorded roll.

The rules engine is written for this package. Its example set is the Dungeon World basic and special
moves, under CC BY 3.0: see [NOTICE.md](NOTICE.md). The in-game `+help sheet credits` topic carries the
attribution. Two small playbooks, the Warden and the Wayfarer, are the package's own and show how a
playbook's moves work.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-pbta-help`](../sheet-pbta-help/) | the `+help sheet` and `+help check` topics |
| [`sheet-pbta-config`](../sheet-pbta-config/) | the settings and the stats, moves and playbooks tables in `+config pbta` |
| [`sheet-pbta-chargen`](../sheet-pbta-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-pbta`](../duties-pbta/) | a Duties roll provider called `pbta` |

`sheet-pbta`, `sheet-d20` and `sheet-fate` all answer `+sheet` and `+check`. Install one sheet package
per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/playbook [<playbook>]` | unapproved player | List the playbooks, or pick one; a sheet with no stat set takes its suggested stats |
| `+sheet/set <stat>=<n>` | unapproved player | A stat from -3 up to `cap` (+2); an empty value clears it |
| `+sheet/take <move>`, `+sheet/drop <move>` | unapproved player | Take or give back a move from your playbook |
| `+sheet/forward <n>`, `+sheet/ongoing <n>` | player | Forward is added to the next roll and spent; ongoing to every roll; 0 clears |
| `+sheet/hold <move>=<n>` | player | Hold a move gave you; 0 clears |
| `+sheet/xp <name>=<n>` | keeper | Set XP, or `=+<n>`/`=-<n>` to add or take |
| `+sheet/traits` | all | Every move, what it rolls with, and the stats |
| `+sheet/move <move>` | all | One move's whole text |
| `+check[/private] <move>[/<stat>][+<n>\|-<n>][=<difficulty>]` | all | Make a move: `Alice rolls Defy Danger (+Dex): 2d6[3, 5] + 1 = 9: a partial hit (roll 7)`, then what the move says for a partial hit |

`+check <stat>` rolls a stat alone. Keepers (`softcode.pbta.admin`, the **PbtA Sheet Keeper** role)
put `<name>/` before the move or stat of `/set`, `/take`, `/drop` and `/hold`, and `<name>=` before
the value of `/playbook`, `/forward` and `/ongoing`, to change anyone's sheet at any time. A keeper may
give a move from any playbook.

## The numbers

- A roll is 2d6 plus the stat, the typed modifier, forward and ongoing, and the difficulty's modifier.
- 10 or more is `success` (a full hit), 7 to 9 `partial`, 6 or less `fail`. With `critical` on, 12 or
  more is `crit-success`.
- The difficulty words easy, standard, hard and extreme add +1, 0, -1 and -2 (`+config pbta/modifiers`).
  A trivial task is not rolled.
- A move names the stat it adds, several for the player to choose from (Defy Danger), or none (Last
  Breath; Aid or Interfere, where the player adds their bond as a modifier).

## Where the data lives

```
PBTA                the root: wizard, no_command
PBTA`STAT`<KEY>     a stat; unset is +0
PBTA`PLAYBOOK       the playbook's key
PBTA`MOVES          moves taken beyond the playbook's starting ones, a space list of keys
PBTA`FORWARD        forward, spent by the next roll
PBTA`ONGOING        ongoing
PBTA`HOLD`<MOVE>    hold on a move
PBTA`XP             experience
```

The lists are `+config` tables on **PbtA Sheet Store**: `STAT` (with `ORDER`), `MOVE` (with `STAT`,
`PLAYBOOK`, `TEXT`, `HIT`, `PARTIAL`, `MISS`, `SOURCE`, `ORDER`) and `PLAYBOOK` (with `STATS`, the
suggested `<stat>=<n>` pairs, `MOVES`, the starting moves, and `ORDER`). A character has every basic
move (no `PLAYBOOK`), their playbook's starting moves, and the moves they took.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)).
A trait key is a stat's key (`str`) or `move-<key>` for a move (`move-defy-danger`).

| Attribute | Arguments | Returns |
|---|---|---|
| `` API`TRAITS `` | | `[{"key","label","group","always"}]`, group `stat` or `move`; every stat and every basic move is always |
| `` API`ALWAYS `` | | the stats and basic moves, a space list |
| `` API`FIND `` | typed text | the key it names, or nothing |
| `` API`LABEL `` | key | its label |
| `` API`RATING `` | character, key | what it adds: the stat, or for a move its stat (the best of several) |
| `` API`HAS `` | character[, key] | 1 when anything is set on their sheet; with a key, 1 when they may roll it |
| `` API`TARGET `` | difficulty word or number | the modifier it adds, or nothing (trivial is nothing) |
| `` API`TIER `` | total | `fail`, `partial`, `success` or `crit-success` |
| `` API`MODIFIERS `` | character | their forward and ongoing together |
| `` API`SPEND `` | character | spends their forward; returns what it was |
| `` API`AWARD `` | character, XP | gives (or takes) XP, never below 0; returns the new total |
| `` API`CHECK `` | named: `roller`, `trait`, `stat`, `modifier`, `target` | `{"tier","total","target","margin","label","text","roll","formula","move","stat","outcome"}`, the roll kept with `roll(...,record)`; margin is always empty, outcome is the move's text for the result |

`API`SPEND` and `API`AWARD` are the two that write. `API`CHECK` adds nothing on its own beyond what it is
given, so a caller adds `API`MODIFIERS` and calls `API`SPEND` itself, as `+check` does.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **PbtA
Sheet** object, as on the d20 sheet.
