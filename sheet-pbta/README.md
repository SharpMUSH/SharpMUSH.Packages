# sheet-pbta

A Powered by the Apocalypse character sheet built from a ledger. Players make their character in three
guided steps (playbook, stats, moves) until they are approved, then spend XP on advances. They keep their
own forward, ongoing and hold in play, and make moves with `+check`: two six-sided dice plus a stat, which
the whole room sees and the game keeps as a recorded roll. Encounters play a scene from copies of the
sheets, so nothing that happens in one reaches the sheet or another scene unless its GM keeps it.

The rules engine is written for this package. Its example set is the Dungeon World basic and special
moves, under CC BY 3.0: see [NOTICE.md](NOTICE.md). The in-game `+help sheet credits` topic carries the
attribution. Two small playbooks, the Warden and the Wayfarer, are the package's own and show how a
playbook's moves work.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-pbta-help`](../sheet-pbta-help/) | the `+help sheet`, `+help check` and `+help encounter` topics |
| [`sheet-pbta-config`](../sheet-pbta-config/) | the settings and the stats, moves and playbooks tables in `+config pbta` |
| [`sheet-pbta-chargen`](../sheet-pbta-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-pbta`](../duties-pbta/) | a Duties roll provider called `pbta` |

Every sheet package answers `+sheet` and `+check`, and the ones with encounters `+encounter`. Install
one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/chargen [<name>]` | all | The steps of making a character: done, to do, and what comes next |
| `+sheet/playbook [<playbook>]` | unapproved player | List the playbooks, or pick one; a sheet with no stat set takes its suggested stats |
| `+sheet/set <stat>=<n>` | unapproved player | Give a stat one of the starting numbers (`array`); an empty value frees it |
| `+sheet/take <move>`, `+sheet/drop <move>` | unapproved player | Pick or give back one of your playbook's other moves, up to its `pick` |
| `+sheet/advance <stat or move>` | approved player | Spend `advance` XP (5) on +1 to a stat, up to `max` (+3), or a move from your playbook |
| `+sheet/forward <n>`, `+sheet/ongoing <n>` | player | Forward is added to the next roll and spent; ongoing to every roll; 0 clears |
| `+sheet/hold <move>=<n>` | player | Hold a move gave you; 0 clears |
| `+sheet/ledger [<name>]` | all | Every entry the sheet is built from |
| `+sheet/revoke <name>/<n>`, `+sheet/clear <name>` | keeper | Take back one entry, or the whole build so character creation starts again |
| `+sheet/xp <name>=<n> [<reason>]` | keeper | Set XP, or `=+<n>`/`=-<n>` to add or take |
| `+sheet/log [<name>]` | all | The latest 30 XP ledger entries: how much, the total after, why, and who |
| `+sheet/rebuild <name>` | keeper | Works their XP out again from their ledger |
| `+sheet/traits` | all | Every move, what it rolls with, and the stats |
| `+sheet/move <move>` | all | One move's whole text |
| `+check[/private] <move>[/<stat>][+<n>\|-<n>][=<difficulty>]` | all | Make a move: `Alice rolls Defy Danger (+Dex): 2d6[3, 5] + 1 = 9: a partial hit (roll 7)`, then what the move says for a partial hit |
| `+encounter [<n>]` | all | The encounters here and yours, or one |
| `+encounter/start [<title>]` | all | Start one in your room and run it |
| `+encounter/join [<n>]`, `/leave [<n>]`, `/use [<n>]` | all | Take part with a copy of your sheet, come out, or pick which copy you roll from here |
| `+encounter/add`, `/remove`, `/keep <name>[=<n>]`, `/end [<n>]` | its GM, keeper | Bring someone in, take them out, write their copy's forward, ongoing and hold to their sheet, end it |

`+check <stat>` rolls a stat alone. Keepers (`softcode.pbta.admin`, the **PbtA Sheet Keeper** role)
put `<name>/` before the move or stat of `/set`, `/take`, `/drop`, `/advance` and `/hold`, and `<name>=`
before the value of `/playbook`, `/forward` and `/ongoing`, to change anyone's sheet at any time. A keeper
may set a stat up to `max`, give a move from any playbook, and give an advance without XP.

## The numbers

- A roll is 2d6 plus the stat, the typed modifier, forward and ongoing, and the difficulty's modifier.
- 10 or more is `success` (a full hit), 7 to 9 `partial`, 6 or less `fail`. With `critical` on, 12 or
  more is `crit-success`.
- The difficulty words easy, standard, hard and extreme add +1, 0, -1 and -2 (`+config pbta/modifiers`).
  A trivial task is not rolled.
- A move names the stat it adds, several for the player to choose from (Defy Danger), or none (Last
  Breath; Aid or Interfere, where the player adds their bond as a modifier).

## The ledger

A character's build is their ledger, `PBTA`LEDGER`<n>`: one JSON entry per step, each with the `wizard`
attribute flag so only the sheet object or a wizard writes one; an entry without the flag is not read.

| Kind | Fields | What it does |
|---|---|---|
| `playbook` | `key` | The playbook; a later one replaces it |
| `stat` | `key`, `value` | A stat's base; empty is unassigned (+0) |
| `boost` | `key`, `value` | Added to the stat's base (an advance) |
| `move` | `key` | A move taken |
| `revoke` | `value` | Takes back entry `value` |
| `clear` | | Every entry before it stops counting |

Every entry also has `n`, `phase` (`chargen`, `play` or `staff`), `by` (an objid) and `at` (secs). Before
approval a player's change rewrites their own `chargen` entry of the same kind and key, and dropping a picked
move removes its entry; every other change is a new entry. A ledger holds at most 200 entries.

The sheet is the playbook's starting moves, every basic move (no `PLAYBOOK`), and the moves taken, with each
stat's base plus its boosts.

## The XP ledger

XP has a ledger of its own, apart from the sheet's: `PBTA`XPLEDGER`<n>`, each entry with the `wizard`
attribute flag: `n`, `delta`, `total` (the running total after it), `item` and `label` (both empty),
`reason`, `by` and `at`. A keeper's `/xp` takes a reason after the number; an advance records the XP it
spends, and `API`AWARD` (a Duties reward) records `Reward`. The ledger keeps 500 entries; past that, the
oldest goes, and the latest total always stays.

## Caches

`PBTA`XP` holds the latest entry's total, and `PBTA`MERGED` the sheet ledger's entries in force, once
something has worked them out. Only ledger writes touch a cache: a new entry rewrites its total, and a sheet
ledger entry drops `PBTA`MERGED` until the next read. `+sheet/rebuild <name>` (keepers) works every cache
out again from the ledgers.

## Encounters

An encounter is a scene played from copies of the sheets. A room may hold several, and a character may be in
several. A copy is taken when someone joins, from their sheet as it is then. While a character is in the room
of an encounter they joined, `+check`, forward, ongoing and hold use that copy: the one `/use` picked, else
the last one joined. Anywhere else the sheet applies. An encounter lasts until `/end`, over any number of days;
`/end` drops every copy, and `/keep` first writes one character's forward, ongoing and hold back to their sheet.
Nothing one encounter does touches another, or the sheet.

The Duties provider and every `API`` function always use the sheet itself.

## Where the data lives

```
PBTA                the root: wizard, no_command
PBTA`LEDGER`<n>     a ledger entry
PBTA`FORWARD        forward, spent by the next roll
PBTA`ONGOING        ongoing
PBTA`HOLD           hold, MOVE=n pairs
PBTA`MERGED         cache: the ledger entries in force
PBTA`XPLEDGER`<n>   an XP ledger entry
PBTA`XP             cache: experience
PBTA`ENCOUNTERS     the encounters they are in, in the order they joined
PBTA`USING          the encounter /use picked
```

On **PbtA Encounters**: `ENC`<n>` the title, with `ROOM`, `GM`, `STARTED` and `COPY`<dbref number>`, each
member's copy, a JSON object with `playbook`, `stats` (`STR=1 DEX=0 ...`), `moves`, `forward`, `ongoing`,
`hold` and `encounter`.

The lists are `+config` tables on **PbtA Sheet Store**: `STAT` (with `ORDER`), `MOVE` (with `STAT`,
`PLAYBOOK`, `TEXT`, `HIT`, `PARTIAL`, `MISS`, `SOURCE`, `ORDER`) and `PLAYBOOK` (with `STATS`, the
suggested `<stat>=<n>` pairs, `MOVES`, the starting moves, `PICK`, how many of its other moves a new
character picks, and `ORDER`).

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
| `` API`HAS `` | character[, key] | 1 when they have a sheet; with a key, 1 when they may roll it |
| `` API`TARGET `` | difficulty word or number | the modifier it adds, or nothing (trivial is nothing) |
| `` API`TIER `` | total | `fail`, `partial`, `success` or `crit-success` |
| `` API`MODIFIERS `` | character | their forward and ongoing together |
| `` API`SPEND `` | character | spends their forward; returns what it was |
| `` API`AWARD `` | character, XP, reason | gives (or takes) XP, never below 0, and logs it; returns the new total |
| `` API`CHECK `` | named: `roller`, `trait`, `stat`, `modifier`, `target` | `{"tier","total","target","margin","label","text","roll","formula","move","stat","outcome"}`, the roll kept with `roll(...,record)`; margin is always empty, outcome is the move's text for the result |

`API`SPEND` and `API`AWARD` are the two that write. `API`CHECK` adds nothing on its own beyond what it is
given, so a caller adds `API`MODIFIERS` and calls `API`SPEND` itself, as `+check` does.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **PbtA
Sheet** object, as on the d20 sheet.
