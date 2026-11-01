# sheet-brp

A percentile character sheet on the Basic Roleplaying rules: seven characteristics (STR, CON, SIZ,
INT, POW, DEX, CHA), hit points, power points and coin, the six characteristic rolls, and a skill list
with base chances that the game edits. The sheet is built from a ledger. Players share out
characteristic and skill points until they are approved, then raise skills with experience checks, and
keep their own hit points, power points and coin in play. Coin has an audited ledger of its own, every skill gain is
an entry on the sheet's ledger, and encounters play from copies of the sheets. `+check` rolls 1d100 under a skill or characteristic roll,
which the whole room sees and the game keeps as a recorded roll.

The characteristics, characteristic rolls, skill list, base chances and categories are ORC Licensed
Material from Basic Roleplaying: Universal Game Engine: see [NOTICE.md](NOTICE.md) for the ORC
notice, the attribution, the Reserved Material and what this package designates as Licensed
Material. The help and messages are this package's own wording, and the in-game
`+help sheet credits` topic carries the attribution.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-brp-help`](../sheet-brp-help/) | the `+help sheet`, `+help check` and `+help encounter` topics |
| [`sheet-brp-config`](../sheet-brp-config/) | the settings and the skill list in `+config brp` |
| [`sheet-brp-chargen`](../sheet-brp-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-brp`](../duties-brp/) | a Duties roll provider called `brp` |
| [`brp-wiki`](../brp-wiki/) | wiki pages on playing with the sheet |

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/chargen [<name>]` | all | The steps of making a character, and what to do next |
| `+sheet/set <characteristic>=<value>` | unapproved player | Shares out `charpoints` (75), each 3 up to `charcap` (18); empty unassigns it (10) |
| `+sheet/set <skill>=<percent>` | unapproved player | Spends `skillpoints` (300) above the base, up to `skillcap` (75%); empty puts it back to its base |
| `+sheet/improve` | approved player | Rolls the marked experience checks: over the percentage adds 1d`improve` (1d6) |
| `+sheet/ledger [<name>]` | all | Every entry the sheet is built from |
| `+sheet/log [<name>]` | all | The latest 30 coin ledger entries, who made them and why |
| `+sheet/hp`, `+sheet/pp` `-<n>\|+<n>\|<n>\|full` | player | Hit points and power points left |
| `+sheet/coin -<n> [<reason>]` | player | Spend coin |
| `+sheet/traits` | all | The characteristics, and the skills with their base chances |
| `+check[/private] <skill>[+<n>\|-<n>][=<difficulty>]` | all | `Alice rolls Climb (55%, difficult, halved: 28%): 1d100[23] = 23: a success (roll 9)`; a success on a skill marks its experience check |
| `+encounter [<n>]` | all | The encounters here and yours, or one |
| `+encounter/start [<title>]`, `/join [<n>]`, `/leave [<n>]`, `/use <n>` | all | Start, join, leave, pick which copy you play from |
| `+encounter/add <name>[=<n>]`, `/remove`, `/keep`, `/end [<n>]` | its GM, keepers | Run it; `/keep` writes a copy back to the sheet |

Keepers (`softcode.brp.admin`, the **BRP Sheet Keeper** role) put `<name>/` before `/set` (up to 99
and 999%, without points) and use `<name>=<n>` with `/hp`, `/pp` and `/coin`. They also have:

| Command | What |
|---|---|
| `+sheet/coin <name>=+<n> [<reason>]` | Gives coin; `-<n>` takes, `<n>` sets |
| `+sheet/mark <name>/<skill>[=remove]` | Marks an experience check by hand, or takes one off |
| `+sheet/improve <name>` | Rolls their experience checks, approved or not |
| `+sheet/revoke <name>/<n>` | Takes back one ledger entry |
| `+sheet/rebuild <name>` | Works their coin out again from their ledger |
| `+sheet/clear <name>` | Revokes every entry; character creation starts again. Hit points, power points, coin and checks stay |

The GM of an encounter changes the hit points, power points, coin and marks of anyone playing from its
copies.

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

## The ledger

A character's characteristics and skills are their ledger, `BRP`LEDGER`<n>`: one JSON entry per step,
each with the `wizard` attribute flag so only the sheet object or a wizard writes one; an entry without
the flag is not read.

| Kind | Fields | What it does |
|---|---|---|
| `char` | `key`, `value` | A characteristic; empty is unassigned (10). A later one replaces it |
| `skill` | `key`, `value` | The points put into a skill above its base chance; a later one replaces it |
| `improve` | `key`, `value` | Percent added to a skill by an experience check or `API`RAISE` |
| `revoke` | `value` | Takes back entry `value` |
| `clear` | | Every entry before it stops counting |

Every entry also has `n`, `phase` (`chargen`, `play` or `staff`), `by` (an objid) and `at` (secs).
Before approval a player's change rewrites their own `chargen` entry of the same kind and key; every
other change is a new entry. A ledger holds at most 200 entries. A skill's percentage is its base
chance from the characteristics in force, plus its points, plus every `improve`.

## The coin ledger

Coin has a ledger of its own, apart from the sheet's: `BRP`MONEYLEDGER`<n>`, each entry with the `wizard`
attribute flag: `n`, `delta`, `total` (the running total after it), `item` and `label` (both empty),
`reason`, `by` and `at`. A keeper's `/coin` takes a reason after the number, `API`AWARD` (Duties rewards)
records `Reward`, and `/keep` records how the copy's coin differs from the sheet's. Skill gains, from
`/improve` or `API`RAISE`, are `improve` entries on the sheet's ledger. Changes to an encounter's copy are
entered only when they are kept. The ledger keeps 500 entries; past that, the oldest goes, and the latest
total always stays.

## Caches

`BRP`COIN` holds the latest entry's total, and `BRP`MERGED` the sheet ledger's entries in force, once
something has worked them out. Only ledger writes touch a cache: a new entry rewrites its total, and a sheet
ledger entry drops `BRP`MERGED` until the next read. `+sheet/rebuild <name>` (keepers) works every cache out
again from the ledgers.

## Encounters

An encounter is a scene played from copies of the sheets. A room may hold several, and a character
may be in several. A copy is taken when someone joins: their hit points, power points and coin as
they are then, and no experience checks. While a character is in the room of an encounter they
joined, hit points, power points, coin and the checks their rolls mark use that copy: the one `/use`
picked, else the last one joined. Anywhere else the sheet applies. Rolls use the sheet's percentages.
An encounter lasts until `/end`, over any number of days; `/end` drops every copy, and `/keep` first
writes one character's hit points, power points and coin back to their sheet and adds the copy's
checks to the sheet's. Nothing one encounter does touches another, or the sheet.

The Duties provider and every `API`` function always use the sheet itself.

## Where the data lives

```
BRP                     the root: wizard, no_command
BRP`LEDGER`<n>          a ledger entry
BRP`HP, BRP`PP          what is left; unset is the most
BRP`MERGED              cache: the ledger entries in force
BRP`MONEYLEDGER`<n>     a coin ledger entry
BRP`COIN                cache: coin; unset is 0
BRP`MARKS               the skills marked for an experience check
BRP`ENCOUNTERS          the encounters they are in, in the order they joined
BRP`USING               the encounter /use picked
```

On **BRP Encounters**: `ENC`<n>` the title, with `ROOM`, `GM`, `STARTED` and `COPY`<dbref number>`,
each member's copy, with `HP`, `PP`, `COIN` and `MARKS` beneath.

The skill list is a `+config` table on **BRP Sheet Store**: `SKILL` (with `BASE` and `CATEGORY`).
The characteristics are `CHAR`, with `ROLL` and `ORDER`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (characteristic rolls in group `characteristic`, skills in their category; `always` for the
rolls and every skill with a base above 0), `ALWAYS`, `FIND`, `LABEL`, `RATING` (the percentage),
`TRAINED` (a skill above its base), `HAS`, `TARGET` (a difficulty word or level: the level), `TIER`
(a success level: the tier) and `CHECK` (named `roller`, `trait`, `modifier` in percent, `target`;
returns `{"tier","level","total","rating","chance","target","label","text","roll","formula"}`). BRP
adds `MOST` and `LEFT` (a character's most and remaining HP or PP), `RAISE` (`%0` a character, `%1`
a skill, `%2` percent to add, `%3` why: an `improve` entry, returning the new percentage),
`HEAL` (gives back HP or PP, never past the most), `COIN` and `AWARD` (`%0` a character, `%1` coin to
give or take, `%2` why: never below 0, a coin ledger entry, returning the new count). `RAISE`, `HEAL` and `AWARD`
are the ones that write.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **BRP
Sheet** object, as on the d20 sheet.
