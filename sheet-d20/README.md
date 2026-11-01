# sheet-d20

A d20 character sheet built from a ledger: six ability scores, a level, hit points, coin, gear, and a
skill list the game edits, each skill untrained, trained or expert. Players make their character in two
guided steps (abilities, skills) until they are approved, then spend XP on advances. They keep their own
hit points, coin and gear in play, and roll against the sheet with `+check`, which the whole room sees and
the game keeps as a recorded roll. Encounters play a scene from copies of the sheets, so nothing that
happens in one reaches the sheet or another scene unless its GM keeps it.

The rules are generic d20 mechanics written for this package; no rulebook text is used.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-d20-help`](../sheet-d20-help/) | the `+help sheet`, `+help check` and `+help encounter` topics |
| [`sheet-d20-config`](../sheet-d20-config/) | the settings and the trait table in `+config d20` |
| [`sheet-d20-chargen`](../sheet-d20-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-d20`](../duties-d20/) | a Duties roll provider called `d20` |
| [`d20-wiki`](../d20-wiki/) | wiki pages on playing, making a character, advancing and encounters |

Every sheet package answers `+sheet` and `+check`, and the ones with encounters `+encounter`. Install
one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/chargen [<name>]` | all | The steps of making a character: done, to do, and what comes next |
| `+sheet/set <ability>=<score>` | unapproved player | Give an ability one of the starting scores (`array`); an empty value frees it |
| `+sheet/set <skill>=trained` | unapproved player | Train a skill, up to `trained` (4) skills; `untrained` takes it back |
| `+sheet/advance <level, ability or skill>` | approved player | Spend `advance` XP (10) on a level, +1 to a score up to `score-max` (20), or a step of training |
| `+sheet/damage <n>`, `+sheet/heal <n\|all>` | player | Take hit points, down to 0, or give them back |
| `+sheet/coin <n> [<reason>]` | unapproved player | Set coin; `+<n>` adds. `-<n>` spends, at any time |
| `+sheet/gear <item>=<count> [<reason>]` | unapproved player | List an item (`Rope=1`); a count of 0 takes it off |
| `+sheet/use <item>` | player | Spend one of an item |
| `+sheet/ledger [<name>]` | all | Every entry the sheet is built from |
| `+sheet/revoke <name>/<n>`, `+sheet/clear <name>` | keeper | Take back one entry, or the whole build so character creation starts again |
| `+sheet/xp <name>=<n> [<reason>]` | keeper | Set XP, or `=+<n>`/`=-<n>` to add or take |
| `+sheet/log [<name>]` | all | The latest 30 changes to XP, coin and gear: how much, the total after, why, and who |
| `+sheet/traits` | all | Every trait, its key, and what it adds |
| `+check[/private][/advantage\|/disadvantage] <trait>[+<n>\|-<n>][=<DC or difficulty>]` | all | Roll 1d20 plus the trait for the room: `Alice checks Athletics: 1d20[13] + 6 = 19 vs DC 15: success (roll 13)` |
| `+encounter [<n>]` | all | The encounters here and yours, or one |
| `+encounter/start [<title>]` | all | Start one in your room and run it |
| `+encounter/join [<n>]`, `/leave [<n>]`, `/use [<n>]` | all | Take part with a copy of your sheet, come out, or pick which copy you roll from here |
| `+encounter/add`, `/remove`, `/keep <name>[=<n>]`, `/end [<n>]` | its GM, keeper | Bring someone in, take them out, write their copy's damage, coin and gear to their sheet, end it |

Keepers (`softcode.d20.admin`, the **D20 Sheet Keeper** role) put `<name>/` before the trait or item of
`/set`, `/advance`, `/gear` and `/use`, and `<name>=` before the value of `/damage`, `/heal` and `/coin`,
to change anyone's sheet at any time. A keeper may set any score up to 30, any training, a level
(`+sheet/set <name>/level=<n>`), and give an advance without XP. An encounter's GM does the same for the
hit points, coin and gear of a member playing from that encounter's copy.

A character reads their own sheet; keepers read every sheet; `+config d20/public=yes` lets anyone read
anyone's.

## The numbers

- An ability adds `(score - 10) / 2`, rounded down. A score not yet set is `score-default` (10).
- A skill adds its ability's modifier, plus the training bonus when trained, twice it when expert.
- The training bonus is `bonus-base` (2) at level 1 and grows by 1 every `bonus-every` (4) levels.
- The most hit points are `hp-level` (8) plus the `hp-ability` (con) modifier for each level, at least 1
  a level.
- A check meets its DC to succeed. With `crits` on, a natural 20 is `crit-success` and a natural 1
  `crit-fail`, whatever the total.
- The difficulty words trivial, easy, standard, hard and extreme are DC 5, 10, 15, 20 and 25
  (`+config d20/dcs`).

## The ledger

A character's build is their ledger, `D20`LEDGER`<n>`: one JSON entry per step, each with the `wizard`
attribute flag so only the sheet object or a wizard writes one; an entry without the flag is not read.

| Kind | Fields | What it does |
|---|---|---|
| `score` | `key`, `value` | An ability's base score; empty is unassigned |
| `boost` | `key`, `value` | Added to the ability's base (an advance) |
| `train` | `key`, `value` | A skill's training, 0, 1 or 2; a later one replaces it |
| `level` | `value` | The level; a later one replaces it |
| `revoke` | `value` | Takes back entry `value` |
| `clear` | | Every entry before it stops counting |

Every entry also has `n`, `phase` (`chargen`, `play` or `staff`), `by` (an objid) and `at` (secs). Before
approval a player's change rewrites their own `chargen` entry of the same kind and key; every other change
is a new entry. A ledger holds at most 200 entries.

## The log

Every change to XP, and to the coin and gear on the sheet itself, is an entry in the character's log,
`D20`LOG`<n>`, with the `wizard` attribute flag: `kind` (`xp`, `coin` or `gear`), `delta`, `total` after,
`item` (gear's name), `reason`, `by` and `at`. A keeper's `/xp`, `/coin` and `/gear` take a reason after the
number; an advance logs the XP it spends, `API`COIN` and `API`GEAR` (Duties rewards) log `Reward`, and
`/keep` logs how the encounter's copy differs from the sheet. Changes to an encounter's copy are not logged
until they are kept. A log keeps the latest 500 entries.

## Encounters

An encounter is a scene played from copies of the sheets. A room may hold several, and a character may be in
several. A copy is taken when someone joins, from their sheet as it is then. While a character is in the room
of an encounter they joined, `+check`, damage, healing, coin and gear use that copy: the one `/use` picked,
else the last one joined. Anywhere else the sheet applies. An encounter lasts until `/end`, over any number of
days; `/end` drops every copy, and `/keep` first writes one character's damage, coin and gear back to their
sheet. Nothing one encounter does touches another, or the sheet.

The Duties provider and every `API`` function always use the sheet itself.

## Where the data lives

```
D20                 the root: wizard, no_command
D20`LEDGER`<n>      a ledger entry
D20`DAMAGE          hit points lost
D20`COIN            the coin
D20`GEAR`<KEY>      an item: <count>|<name>, the key its name in upper case
D20`XP              experience
D20`LOG`<n>         a log entry
D20`ENCOUNTERS      the encounters they are in, in the order they joined
D20`USING           the encounter /use picked
```

On **D20 Encounters**: `ENC`<n>` the title, with `ROOM`, `GM`, `STARTED` and `COPY`<dbref number>`, each
member's copy, a JSON object with `level`, `scores` (`STR=15 DEX=14 ...`), `training` (`ATHLETICS=1 ...`),
`hp`, `damage`, `coin`, `gear` (`<count>~<KEY>~<name>` items between `|`) and `encounter`.

The traits are a `+config` table on **D20 Sheet Store**: `TRAIT`<KEY>` holds the label, with `KIND`
(ability or skill), `ABILITY` (a skill's ability key) and `ORDER` beneath.

## The sheet API

Every sheet package (`sheet-d20`, `sheet-fate`, and the ones that follow) has the same `API` tree on
its sheet object, so a bridge such as a Duties provider is written the same way for each. The
attributes are VISUAL on a WIZARD object, so only code at least that privileged calls them
(`safer_ufun`). They read the sheet itself, never an encounter's copy, and roll; only `API`COIN` and `API`GEAR` write.

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
| `` API`COIN `` | character, amount, reason | adds coin (less than 0 takes it), returns the new total; a write, logged |
| `` API`GEAR `` | character, item, amount, reason | adds that many of an item, returns how many now; a write, logged |
| `` API`CHECK `` | named: `roller`, `trait`, `modifier`, `target`, `dice` (`1d20`, `2d20kh`, `2d20kl`) | `{"tier","total","natural","target","margin","label","text","roll","formula"}`, the roll kept with `roll(...,record)` |

## What a bridge may set

On the **D20 Sheet** object:

- `` HINT`<message> `` adds a line to one of the sheet's messages (`SWITCHES`, `FOOTER`, `CHARGEN`).
- `` GATE`EDIT `` (`%0` the player) gives a reason a player may not change their own sheet now, or nothing.
- `` ALLOW`VIEW`<name> `` (`%0` who asks, `%1` whose sheet) lets more people read a sheet.
