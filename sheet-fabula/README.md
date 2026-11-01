# sheet-fabula

A JRPG character sheet, compatible with Fabula Ultima: four attributes (Dexterity, Insight, Might,
Willpower), each a die from d6 to d12; classes and the skill levels spent in them; identity, theme and
origin; HP, MP, IP, Fabula Points, experience and zenit; status effects; and bonds. The build, experience
and zenit are a ledger of entries, each with where it came from. `+check` rolls the dice of two attributes against a Difficulty
Level for the room, keeps the roll, and lets the roller spend Fabula Points to reroll or to add a bond.
`+encounter` keeps an encounter's own copy of each member's HP, MP, IP and status effects, and runs a
conflict in turns against foes from a bestiary of the package's own creatures.

Requires the Fabula Ultima Core Rulebook. See [NOTICE.md](NOTICE.md) for the licence notice; the
in-game `+help sheet credits` topic carries it too. The help and messages are this package's own
wording, and the sheet keeps skills by name and level, not their text.

Depends on nothing. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`sheet-fabula-help`](../sheet-fabula-help/) | the `+help sheet` and `+help check` topics |
| [`sheet-fabula-config`](../sheet-fabula-config/) | the settings and the class list in `+config fabula` |
| [`sheet-fabula-chargen`](../sheet-fabula-chargen/) | ties sheet changes to the player's `+app` application |
| [`duties-fabula`](../duties-fabula/) | a Duties roll provider called `fabula` |

[`fabula-wiki`](../fabula-wiki/) puts the rules on the wiki; neither package needs the other.

Every sheet package answers `+sheet` and `+check`. Install one sheet package per game.

## Commands

| Command | Who | What |
|---|---|---|
| `+sheet [<name>]` | all | Your sheet, or another character's when you may read it |
| `+sheet/set <attribute>=<die>` | unapproved player | `d6`, `d8`, `d10` or `d12`; unset is d8 |
| `+sheet/class <class>=<levels>` | unapproved player | 0 to 10; the classes share `start` (5) levels, at most 3 below level 10 |
| `+sheet/skill <class>:<skill>=<level>` | player | One skill level per class level; `heroic:<skill>=1` for each class at 10. Approved players only raise |
| `+sheet/levelup <class>` | approved player | 10 experience for one more class level, as a ledger entry |
| `+sheet/raise <attribute>` | player | One die size larger, at level 20 and at 40 |
| `+sheet/bonus <hp\|mp\|ip>=<n> [<source>]` | player | A ledger entry: what a skill adds to the maximum HP, MP or IP. Approved players only add |
| `+sheet/bonus <def\|mdef\|init\|martial>=<n> [<source>]` | player | A ledger entry: what equipment adds to Defense, Magic Defense and Initiative; `martial` is martial armour's Defense, the largest counting |
| `+sheet/ledger [<name>][=<page>]` | all | The build ledger, and 50 entries a page of the experience and zenit ledgers, newest first, when you may read the sheet |
| `+sheet/revoke <entry>` | player | Takes an entry off: equipment at any time, anything until approved, as long as the rest adds up |
| `+sheet/award <name>=<xp\|zenit> <n> <reason>` | keeper | Experience or zenit as a ledger entry with the reason; `-<n>` takes some back. The character is told |
| `+sheet/buy <item>=<cost>` | player | Spends zenit, as a ledger entry with the item |
| `+sheet/clear <name>=confirm` | keeper | The build's entries and the experience levels cost off, so the build starts over, and out of every encounter; awards and zenit stay |
| `+sheet/identity`, `/theme`, `/origin` | player | The three traits |
| `+sheet/hp`, `/mp`, `/ip`, `/fp` | player | `+<n>`, `-<n>`, `<n>` or `reset` |
| `+sheet/status [<effect>\|clear]` | player | Toggles dazed, enraged, poisoned, shaken, slow or weak |
| `+sheet/rest` | player | HP and MP full, status effects gone |
| `+sheet/bond <who>=<emotions>` | player | Up to six bonds; nothing after `=` takes one off |
| `+sheet/traits` | all | The attributes, classes, difficulties, status effects and emotions |
| `+check[/private] <attr>+<attr>[+<n>\|-<n>][=<difficulty>]` | all | `Alice rolls Dexterity + Insight: d10[7] + d8[4] = 11 vs 10: a success, high roll 7 (roll 42)` |
| `+check/invoke <identity\|theme\|origin>[=first\|second]` | all | A Fabula Point to reroll the last check's dice (both when not given) |
| `+check/bond <bond>` | all | A Fabula Point to add a bond's strength to the last check, once |
| `+check init` | all | Dexterity + Insight with the Initiative bonus |
| `+check/support <leader>=<attr>+<attr>` | all | A check against 10 that helps the leader's next group check |
| `+check/group <attr>+<attr>[=<difficulty>]` | all | The leader's check: +1 for each supporter who succeeded, and the strongest of their bonds with the leader |
| `+encounter [<n>]` | all | The encounter you are in, or the one here, with each member's copy |
| `+encounter/start [<title>]` | all | A new encounter in this room, with you as its GM |
| `+encounter/join [<n>]`, `/leave [<n>]` | all | Take part with a copy of your HP, MP, IP and status effects, or drop it |
| `+encounter/use [<n>]` | all | Which of your encounters in this room your commands use; nothing for the last joined |
| `+encounter/add <name>[=<n>]` | keeper | Bring a character in |
| `+encounter/remove`, `/keep <name>[=<n>]` | GM | Take a member out, or write their copy onto their sheet |
| `+encounter/end [<n>]` | GM | Ends it; every copy goes |
| `+foe [<foe>]` | all | The bestiary, or one foe with its numbers worked out; for a GM, a foe in their encounter as it stands |
| `+encounter/foe [<count>] <foe>` | GM | Bring 1 to 10 copies of a bestiary foe in, lettered A, B, C |
| `+encounter/initiative` | member | Before the conflict: Dexterity + Insight plus Initiative against the foes' best Initiative picks the side that acts first |
| `+encounter/begin [characters\|foes]` | GM | Round 1, with that side first |
| `+attack <target>=<attr>+<attr>[+<n>]`, `/magic` | member | A check against the target's Defense or Magic Defense; it is the last check, so the invokes work on it |
| `+attack/damage <n> [<type>]` | member | The last hit's high roll plus `<n>`, after the target's affinities |
| `+encounter/turn [<who>]`, `/guard [<who>]` | member, GM for others | End a turn, or guard |
| `+encounter/undo <who>`, `/round` | GM | Give a turn back; start the next round |
| `+encounter/damage <who>=<n> [<type>]` | GM | Damage by hand, after affinities |
| `+encounter/surrender` | member | At 0 HP, leave the conflict for Fabula Points (`+config fabula/surrender`) |
| `+encounter/entrance <foe>` | GM | A villain's entrance: a Fabula Point for each character still in |
| `+encounter/reward <xp\|zenit> <n> <reason>` | keeper | An award for each member, on the experience or zenit ledger |
| `+foe/attack <foe>=<target>[/<attack>]` | GM | One of the foe's attacks, rolled, with its damage on a hit |
| `+foe/hp`, `/mp <foe>=<+n\|-n\|n>`, `/status <foe>=<effect>\|clear`, `/remove <foe>` | GM | Change a foe's copy, or take it out |
| `+foe/ultima <foe>=escape\|recover\|invoke` | GM | Spend a villain's Ultima Point |
| `+sheet/affinity [<name>/]<type>=<vu\|rs\|im\|ab> [<source>]` | all, keeper for others | A build entry for a vulnerability, resistance, immunity or absorption |

Keepers (`softcode.fabula.admin`, the **JRPG Sheet Keeper** role) put `<name>/` before the
`/set`, `/class`, `/skill`, `/levelup`, `/raise`, `/bonus`, `/buy`, `/revoke` and `/bond` arguments, and use
`<name>=<value>` with the resources, traits and `/status`. A keeper runs any encounter as its GM. The GM
changes a member's copy with `+sheet/hp <name>=<value>`, and `/mp`, `/ip`, `/status` and `/rest`, while
that encounter is the one the member uses.

## The numbers

- A check is the two dice, as status effects leave them, plus any adds. It succeeds when the total
  reaches the Difficulty Level. The difficulty words are `5 7 10 13 16` (`+config fabula/dls`);
  `normal` is standard and `very hard` extreme.
- Both dice the same and 6 or more is `crit-success`; both 1 is `crit-fail`, a fumble, which gives
  the roller a Fabula Point. Invokes cannot change a fumble. They work for `window` (600) seconds
  after the check.
- Each status effect makes its attributes one die smaller, down to d6: dazed Insight, slow
  Dexterity, weak Might, shaken Willpower, enraged Dexterity and Insight, poisoned Might and
  Willpower.
- Maximum HP is 5 times the base Might die plus the level, maximum MP the same with Willpower, maximum IP 6.
  Each class that gives HP or MP adds 5, IP 2; `+sheet/bonus` adds the rest. Crisis is half HP or less.
- Defense is the Dexterity die now, or martial armour's Defense, plus the `def` bonus; Magic Defense the
  Insight die now plus `mdef`; Initiative the `init` bonus.
- A character has at most 3 classes below level 10 at once.
- The build is the ledger: a die sets an attribute's base, a raise adds one size, class levels, skill
  levels and bonuses add up, and the largest martial armour counts. Until approval, changing an
  attribute, class or skill rewrites its character creation entry; after it each change is an entry of
  its own. A sheet holds at most 200 build entries.
- Experience and zenit each have a ledger of their own, apart from the build's, of at most 1000 entries: a
  keeper's `+sheet/award`, a duty's reward, a level-up's 10 experience and `+sheet/buy`. Both start at 0,
  and the total is a cache rebuilt from the ledger. Only a keeper takes one of these entries off.
- An encounter copies a member's HP, MP, IP and status effects when they join. While the member is in
  the room where it runs, the commands use that copy: the one `+encounter/use` picked, else the last
  joined. Anywhere else, and for the API that Duties calls, the sheet is used. Ending an encounter
  drops every copy, so the sheet has only what the GM kept with `/keep`.
- A conflict alternates the sides one creature at a time; when one side has no turns left the other
  takes the rest, and the round ends when everyone has acted. A soldier has one turn a round, an elite
  two, a champion its number. A character's action on their side's turn takes that turn; one out of turn
  takes none.
- A foe's HP is 5 times its Might die plus twice its level, plus its `hp` bonus, times 1 for a soldier,
  2 for an elite and the number for a champion. MP is 5 times Willpower plus the level, plus `mp`,
  doubled for a champion. Initiative is half of Dexterity plus Insight, plus `init`, plus the soldier
  count of an elite or champion. Defense is Dexterity plus `def`, Magic Defense Insight plus `mdef`, with
  status effects shrinking the dice. Its attacks add a tenth of its level to the check and 5 damage for
  every 20 levels. A role (brute, hunter, mage, saboteur, sentinel, support) sets the four dice for the
  level, changing at 20, 40 and 60.
- A minor villain starts with 5 Ultima Points, a major one 10 and a supreme one 15. The encounter counts
  those spent, for the session's experience.
- Vulnerable doubles damage, resistant halves it, rounded down, immune stops it and absorbent heals it.
  Resistance and vulnerability cancel. Guarding is resistance to every type until the next turn.
- A bond holds one to three emotions, one from each pair at most (admiration or inferiority,
  loyalty or mistrust, affection or hatred). Its strength is how many.

## Where the data lives

```
FABULA                        the root: wizard, no_command
FABULA`LEDGER`<n>             the build: JSON with kind (die raise class skill bonus), key, n,
                              phase (chargen play staff), source, by, at, class, name; wizard-flagged
FABULA`LEDGER`NEXT            the next entry's number, for all three ledgers
FABULA`EXPERIENCE`<n>         the experience ledger: JSON with kind xp and the same fields; wizard-flagged
FABULA`MONEY`<n>              the zenit ledger: JSON with kind zenit and the same fields; wizard-flagged
FABULA`ATTR`<KEY>             DEX INS MIG WLP: the base die size; unset is 8
FABULA`RAISES                 attributes raised at levels 20 and 40
FABULA`CLASS`<KEY>            a class's level
FABULA`SKILL`<KEY>            a skill's name, with CLASS (a class key or HEROIC) and LEVEL beneath
FABULA`TRAIT`<KEY>            IDENTITY, THEME, ORIGIN
FABULA`METER`<KEY>            HP MP IP FP; unset is its start
FABULA`WALLET`<KEY>           XP ZENIT: the total of that ledger, a wizard-flagged cache
FABULA`BONUS`<KEY>            HP MP IP from skills; DEF MDEF INIT MARTIAL from equipment
FABULA`STATUS                 the status effects on the character
FABULA`BOND`<KEY>             a bond's name, with EMOTIONS beneath
FABULA`LAST                   the last check, for the invokes
FABULA`ATTACK                 the last attack: JSON with at, enc and target
FABULA`AFFINITY`<TYPE>        vu rs im ab, rebuilt from the build ledger's affinity entries
FABULA`SUPPORTS               the supporters of their next group check
FABULA`ENCOUNTERS             the encounters they are in, last joined last
FABULA`USING                  the one +encounter/use picked
```

`ATTR`, `RAISES`, `CLASS`, `SKILL` and `BONUS` are rebuilt from `LEDGER` after every change. `WALLET` moves
with each new experience or zenit entry and is added up again from its ledger when one is taken off.

**JRPG Encounters** holds the encounters: `` ENC`<n> `` a title, with `ROOM`, `GM`, `AT`, `MEMBERS`
and each member's `` COPY`<number> `` (their HP, MP, IP and status effects) beneath, and
`` ROOM`<number> `` the encounters in a room. A conflict adds `ROUND`, `FIRST` and `SIDE` (heroes or
foes), `TAKEN` (one id per turn taken this round), `GUARD`, `OUT` (who surrendered), `UPSPENT`, and
`` FOE`<k> ``: a foe's label, with `KEY`, `LEVEL`, `RANK`, `SOLDIERS`, `VILLAIN`, the dice, `HPMAX`,
`MPMAX`, `HP`, `MP`, `DEFB`, `MDEFB`, `INIT`, `UP`, `AFF`, `IMMUNE`, `ATTACKS`, `STATUS` and `STATE`
(escaped) beneath. A character's id is their objid, a foe's `F<k>`.

The bestiary is a `+config` table on **JRPG Sheet Store**, `` FOE`<KEY> `` with `LEVEL`, `RANK`,
`CHAMPION`, `VILLAIN`, `SPECIES`, `ROLE`, `DEX` `INS` `MIG` `WLP`, the `HP` `MP` `DEF` `MDEF` `INIT`
bonuses, `AFFINITIES` (`<type>:<vu|rs|im|ab>`), `IMMUNE` (status effects), `ATTACKS` and `NOTES`.
An attack is `<name>: <attr>+<attr> <accuracy> <damage> <type>`, with `magic` at the end for one
against Magic Defense, and attacks are separated by `;`. The seventeen foes it ships, from level 5 to
55, are this package's own.

The class list is a `+config` table on **JRPG Sheet Store**: `CLASS` (with `BENEFIT` hp, mp, ip
or none, `MARTIAL`, `RITUALS` and `ORDER`). It holds the Core Rulebook's fifteen classes; a game
adds the classes of other books with `+config/add fabula/classes/<key>=<label>`.

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)),
where a trait is a pair of attributes:

- `TRAITS` the ten pairs (`dex+ins`, label `Dexterity + Insight`, group `check`, all `always`),
  `ALWAYS`, `FIND` (`dex+ins`, `dex ins`, or `mig` for `mig+mig`), `LABEL`, `RATING` (the dice now,
  `d10 + d8`), `HAS`, `TARGET` (a difficulty word or a number from 1 to 40: the Difficulty Level),
  `TIER` (total, the two dice, the Difficulty Level).
- `CHECK` (named `roller`, `trait`, `modifier`, `target`) rolls and keeps the roll, and returns
  `{"tier","total","hr","dice","sizes","pair","modifier","target","crit","fumble","label","text","roll"}`.
  It gives no Fabula Point for a fumble: the caller does.
- `REROLL` and `PUSH` change a check's JSON: dice rolled again, or a bond's strength added.
- `LEVEL`, `METER`, `START`, `MAX` and `DEFENSE` (character, `DEF`, `MDEF` or `INIT`) read a character; `BOND` (holder, someone) is the strongest bond
  the holder has named for them. `ADJUST` (character, meter, amount, and for `XP` or `ZENIT` the
  reason) is the one that writes; experience and zenit go on the ledger.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the
**JRPG Sheet** object, as on the d20 sheet.
