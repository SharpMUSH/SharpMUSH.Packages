# sheet-fitd

A Forged in the Dark character sheet: twelve actions rated 0 to 4 under Insight, Prowess and
Resolve, built from a ledger, with XP for each attribute, stress, trauma, harm and coin, an audited
log of XP and coin, encounters that play from copies of the sheets, and the game's progress clocks.
Players share out their starting dots until they are approved, then spend XP on advances, and keep
their own stress, trauma, harm and coin in play. `+check` rolls one six-sided die per point of an
action and reads the highest against a position, which the whole room sees and the game keeps as a
recorded roll.

Based on the Blades in the Dark SRD under CC BY 3.0: see [NOTICE.md](NOTICE.md). The help and
messages are this package's own wording, and the in-game `+help sheet credits` topic carries the
attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-fitd-help`](../sheet-fitd-help/) | the `+help sheet`, `+help check`, `+help encounter` and `+help clock` topics |
| [`sheet-fitd-config`](../sheet-fitd-config/) | the settings and the action and attribute lists in `+config fitd` |
| [`sheet-fitd-chargen`](../sheet-fitd-chargen/) | ties rating changes to the player's `+app` application |
| [`duties-fitd`](../duties-fitd/) | a Duties roll provider called `fitd` |
| [`fitd-wiki`](../fitd-wiki/) | wiki pages on playing with the sheet |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/chargen [<name>]` | all | The steps of making a character, and what to do next |
| `+sheet/set <action>=<rating>` | unapproved player | Shares out the starting dots (`dots`, 7), at most `cap` (2) in one action |
| `+sheet/advance <action>` | approved player | Spends `advance` (6) XP of the action's attribute on +1, up to 4 |
| `+sheet/ledger [<name>]` | all | Every entry the ratings are built from |
| `+sheet/log [<name>]` | all | Every change to XP and coin, who made it and why |
| `+sheet/stress +<n>\|-<n>\|<n>\|clear` | player | Past the most (9) stress clears and a trauma is due |
| `+sheet/trauma <trauma>` | player | Mark a trauma; at the fourth the character retires |
| `+sheet/harm <level>=<harm>` | player | Level 1 to 3; a full level pushes harm up one. Empty clears the level |
| `+sheet/coin -<n> [<reason>]` | player | Spend coin |
| `+sheet/traits` | all | The actions and their attributes |
| `+check[/private] <action>[+<n>\|-<n>][=<position>]` | all | `Alice rolls Skirmish (risky): 2d6kh1[(3), 6] = 6: a full success (roll 42)` |
| `+check/resist <attribute>` | all | Rolls the attribute and marks 6 less the highest die in stress; two 6s clear 1 |
| `+encounter [<n>]` | all | The encounters here and yours, or one |
| `+encounter/start [<title>]`, `/join [<n>]`, `/leave [<n>]`, `/use <n>` | all | Start, join, leave, pick which copy you roll from |
| `+encounter/add <name>[=<n>]`, `/remove`, `/keep`, `/end [<n>]` | its GM, keepers | Run it; `/keep` writes a copy back to the sheet |
| `+clock`, `+clock <name>` | all | The game's clocks |
| `+clock/new <name>=<segments>` | all | 4, 6, 8 or 12 segments |
| `+clock/tick <name>[=<n>]`, `+clock/remove <name>` | who started it, keepers | Fill (or empty) segments; take it away |

Keepers (`softcode.fitd.admin`, the **FitD Sheet Keeper** role) put `<name>/` before `/set`,
`/advance`, `/trauma` and `/harm`, use `<name>=<n>` with `/stress` and `/coin`, and take traumas off
with `+sheet/trauma <name>/<trauma>=remove`. They rate any action up to 4, give advances without
XP, and have three more switches:

| Command | What |
|---|---|
| `+sheet/xp <name>/<attribute>=+<n> [<reason>]` | Gives XP in that attribute; `-<n>` takes, `<n>` sets |
| `+sheet/revoke <name>/<n>` | Takes back one ledger entry |
| `+sheet/clear <name>` | Revokes every entry; character creation starts again. XP, stress, trauma, harm and coin stay |

The GM of an encounter changes the stress, trauma, harm and coin of anyone playing from its copies.

## The numbers

- One die per rating; a rating of 0 rolls two dice and keeps the lower.
- The highest die: 6 is `success`, 4 or 5 `partial`, 1 to 3 `fail`. Two 6s or more (from one die
  or more) are `crit-success`.
- An attribute's rating is how many of its actions are rated 1 or more.
- The difficulty words map to positions (`+config fitd/positions`) and dice (`+config fitd/dice`).
  `none` means no roll: it succeeds.

## The ledger

A character's ratings are their ledger, `FITD`LEDGER`<n>`: one JSON entry per step, each with the
`wizard` attribute flag so only the sheet object or a wizard writes one; an entry without the flag is
not read.

| Kind | Fields | What it does |
|---|---|---|
| `rating` | `key`, `value` | An action's rating, 0 to 4; a later one replaces it |
| `revoke` | `value` | Takes back entry `value` |
| `clear` | | Every entry before it stops counting |

Every entry also has `n`, `phase` (`chargen`, `play` or `staff`), `by` (an objid) and `at` (secs).
Before approval a player's change rewrites their own `chargen` entry for that action; every other
change is a new entry. A ledger holds at most 200 entries.

## The log

Every change to XP, and to the coin on the sheet itself, is an entry in the character's log,
`FITD`LOG`<n>`, with the `wizard` attribute flag: `kind` (`xp` or `coin`), `delta`, `total` after,
`item` (the attribute, for XP), `reason`, `by` and `at`. A keeper's `/xp` and `/coin` take a reason
after the number; an advance logs the XP it spends, `API`AWARD` (Duties rewards) logs `Reward`, and
`/keep` logs how the copy's coin differs from the sheet's. Changes to an encounter's copy are not
logged until they are kept. A log keeps the latest 500 entries.

## Encounters

An encounter is a scene played from copies of the sheets. A room may hold several, and a character
may be in several. A copy is taken when someone joins, from their sheet as it is then. While a
character is in the room of an encounter they joined, `+check`, `+check/resist`, stress, trauma, harm
and coin use that copy: the one `/use` picked, else the last one joined. Anywhere else the sheet
applies. An encounter lasts until `/end`, over any number of days; `/end` drops every copy, and
`/keep` first writes one character's stress, trauma, harm and coin back to their sheet. Nothing one
encounter does touches another, or the sheet.

The Duties provider and every `API`` function always use the sheet itself.

## Where the data lives

```
FITD                    the root: wizard, no_command
FITD`LEDGER`<n>         a ledger entry
FITD`XP`<ATTRIBUTE>     an attribute's XP; unset is 0
FITD`STRESS             stress marked; unset is 0
FITD`TRAUMA             traumas, a |-list
FITD`HARM`<SLOT>        harm in slot 1A, 1B, 2A, 2B or 3A
FITD`COIN               coin; unset is 0
FITD`LOG`<n>            a log entry
FITD`ENCOUNTERS         the encounters they are in, in the order they joined
FITD`USING              the encounter /use picked
```

On **FitD Encounters**: `ENC`<n>` the title, with `ROOM`, `GM`, `STARTED` and `COPY`<dbref number>`,
each member's copy, with `STRESS`, `TRAUMA`, `COIN`, `HARM`<SLOT>` and `RATINGS` (`SKIRMISH=2 HUNT=1
...`, or `none`) beneath.

The lists are `+config` tables on **FitD Sheet Store**: `ACTION` (with `ATTRIBUTE` and `ORDER`) and
`ATTRIBUTE`. Clocks are on the store too: `` CLOCK`<KEY> `` with `SIZE`, `FILLED` and `OWNER`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every action `always`, its attribute as `group`), `ALWAYS`, `FIND`, `LABEL`, `RATING`,
`HAS`, `TARGET` (a position or difficulty word: the position), `TIER` (highest die, sixes) and
`CHECK` (named `roller`, `trait`, `modifier` in dice, `target`; returns
`{"tier","total","sixes","dice","target","label","text","roll","formula"}`). FitD adds `ATTRIBUTE`
(a character's dice in an attribute), `STRESSED` (stress marked), `STRESS` (marks or clears stress and
returns `{"stress","trauma"}`, trauma 1 when one is due), `COIN` and `AWARD` (`%0` a character, `%1`
coin to give or take, `%2` why, `Reward` when empty: never below 0, logged, returns the new count).
`STRESS` and `AWARD` are the ones that write.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **FitD
Sheet** object, as on the d20 sheet.
