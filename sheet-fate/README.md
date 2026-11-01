# sheet-fate

A Fate character sheet: skills on the ladder (or the six approaches), aspects, stunts, stress tracks,
consequences, fate points and refresh. Players fill in their skills and aspects until they are
approved, with `+chargen` showing what is left to do. They keep their own stress, consequences and
fate points in play, and roll four Fate dice against an opposition with `+check`, which the whole room
sees and the game keeps as a recorded roll. Ratings, stress boxes and refresh are built from a ledger
of grants, so a staff bonus or a package's grant survives the player's own changes. An encounter keeps
its own copy of each player's fate points, stress and consequences until the GM keeps it or ends the
encounter. The GM brings in opposition built with `+npc`, from mooks to villains, and runs the
conflict with exchanges, harm, concessions, aspects on the scene and a pool of fate points. Keepers give milestones, breakthroughs and power-ups, which stay on the character as a log
of who gave what and why, and players spend them with `+sheet/advance`.

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
| `+sheet/stunt <slot>=<stunt>` | unapproved player | A stunt in slot 1 to `stunts`; empty clears it |
| `+sheet/stress <track>=<box>` | player | Mark a box; `=clear` empties the track |
| `+sheet/recover` | player | Clear every stress box |
| `+sheet/consequence <slot>=<aspect>` | player | Take a consequence; empty clears it |
| `+sheet/spend [<what for>]` | player | Spend a fate point where the room sees it |
| `+sheet/award <name>[=<n>]` | keeper | Give fate points, or take them with a number below 0 |
| `+sheet/refresh <name>[=<n>\|default]` | keeper | Bring their points up to their refresh, or set it |
| `+sheet/boxes <name>/<track>=<n>\|default` | keeper | Give one character a stress track of their own length |
| `+sheet/traits` | all | The skills or approaches, and the ladder |
| `+sheet/ledger [<name>]` | all | The grants a sheet is built from, numbered |
| `+sheet/grant <name>/<what>=<n>\|+<n>\|-<n>` | keeper | A grant of its own for a skill, a track or `refresh`: a number sets it, `+`/`-` adds |
| `+sheet/revoke <name>/<n>` | keeper | Take away grant `<n>` of their ledger |
| `+sheet/clear <name>` | keeper | Take away their whole build so they make the character again |
| `+sheet/milestone <name>[=<reason>]` | keeper | Give a milestone |
| `+sheet/breakthrough <name>[=<reason>]` | keeper | Give a breakthrough: a milestone, a skill step and a new high concept |
| `+sheet/powerup <name>/refresh\|skill[=<reason>]` | keeper | Give a point of refresh or a second skill step |
| `+sheet/void <name>/<n>=<reason>` | keeper | Take back what award `<n>` has not spent; it stays on the log, marked void |
| `+sheet/advance [[<name>/]<option> <what>[=<value>]]` | player | What there is to spend and on what, or spend one; keepers for anyone |
| `+sheet/advances [<name>]` | all | Every award: who gave it, when, why, what is left and what it bought |
| `+chargen [<name>]` | all | The steps of making a character, which are done, and what to do next |
| `+encounter [<n>]` | all | The encounters in the room, or one of them |
| `+encounter/start [<title>]` | all | Begin an encounter here and run it as its GM |
| `+encounter/join [<n>]` | player | Take part; the copy is taken now |
| `+encounter/use <n>` | player | Which of your encounters in this room your play goes to |
| `+encounter/leave [<n>]` | player | Leave; the copy is dropped |
| `+encounter/add <name>[=<n>]` | GM | Bring in someone in the room |
| `+encounter/remove <name>[=<n>]` | GM | Take someone out; their copy is dropped |
| `+encounter/keep <name>[=<n>]` | GM | Write their copy back onto their sheet |
| `+encounter/end [<n>]` | GM | End it; every copy not kept is dropped |
| `+encounter/npc <opposition>[=<count>]` | GM | Bring in NPCs from `+npc`, numbered when several |
| `+encounter/stats <npc>` | GM | One NPC in full |
| `+encounter/roll <npc>/<skill>[+<n>][=<opposition>]` | GM | Roll for an NPC, for the room |
| `+encounter/harm <name>[/<track>]=<shifts>` | GM | A hit: an NPC marks its boxes and is taken out past its consequences; a player is told what to mark |
| `+encounter/stress <npc>/<track>=<box>\|clear` | GM | Mark or clear an NPC's box, or its track |
| `+encounter/consequence <npc>/<slot>=<aspect>` | GM | An NPC's consequence; empty clears it |
| `+encounter/out <name>[=<what happens>]` | GM | Take someone out, or say what happened; again bare brings them back |
| `+encounter/concede [<npc>]` | player, GM | Concede: a fate point and one per consequence taken here; a major NPC banks them |
| `+encounter/exchange` | GM | The next exchange; the first gives the GM a fate point per player |
| `+encounter/act [<name>]` | player, GM | Take your turn, or hand it to someone who has not acted |
| `+encounter/aspect <aspect>[=<free invokes>]` | player, GM | An aspect on the scene |
| `+encounter/boost <aspect>` | player, GM | A boost: one free invoke, gone once used |
| `+encounter/invoke <n>[=<why>]` | player, GM | +2 or a reroll: a free invoke, else a fate point from your copy or the GM's pool |
| `+encounter/unaspect <n>` | GM, whoever placed it | Take an aspect off |
| `+encounter/pool [<n>\|+<n>\|-<n>][=<why>]` | all, GM | The GM's fate points; the GM changes them |
| `+encounter/point <name>[=<why>]` | GM | A fate point on a player's copy, such as for a compel |
| `+encounter/victory <name>[=<n>]` | GM | A victory in a contest, 2 for success with style; three win |
| `+npc [<name>]` | all | The NPCs you may use, or one in full |
| `+npc/create <name>[=minor\|major]` | all | A minor NPC has one stress box and no consequences, a major one the full set |
| `+npc/skill <npc>/<skill>=<rating>` | maker, keeper | A rating; every other skill is Mediocre |
| `+npc/aspect <npc>/<n>=<aspect>`, `/stunt <npc>/<n>=<stunt>` | maker, keeper | Slots 1 to 5; empty clears one |
| `+npc/stress <npc>/<track>=<boxes>` | maker, keeper | 0 to 10 boxes |
| `+npc/consequences <npc>=<slots>\|all\|none` | maker, keeper | Its consequence slots |
| `+npc/set <npc>/<field>=<value>` | maker, keeper | A field a package adds, such as Atomic Robo's scale |
| `+npc/share <npc>` | maker, keeper | Let every GM use it, or only its maker again |
| `+npc/destroy <npc>` | maker, keeper | Remove it; running encounters keep their copies |
| `+check[/private] <skill>[+<n>\|-<n>][=<opposition>]` | all | Roll 4dF plus the rating: `Bob rolls Fight: 4dF[-1, 0, 1, 0] + 4 = 4 (Great) against Fair (+2): success, 2 shifts (roll 20)` |

Keepers (`softcode.fate.admin`, the **Fate Sheet Keeper** role) put `<name>/` before the slot of
`/set`, `/aspect`, `/stunt`, `/stress` and `/consequence` to change anyone's sheet at any time.

## Encounters

An encounter has a number, a room and a GM: whoever started it, and every keeper. A room holds any
number of them and a character may be in several. While a character stands in the room of an
encounter they joined, `+sheet/stress`, `/consequence`, `/spend`, `/recover` and `+sheet` use that
encounter's copy: the one they picked with `+encounter/use`, else the last they joined. Everywhere
else they use the sheet. An encounter lasts until the GM ends it, across any number of days. Duties
and every other reader of the sheet API use the sheet itself.

A GM's commands without a number go to the encounter picked with `+encounter/use`, else the one their
play goes to, else the only one they run in the room.

Opposition is built with `+npc` and kept on **Fate Opposition**, each player's own until they share
it; a player may keep `npcs` of them (50), a keeper any number. `+encounter/npc` copies one into the
encounter, so later changes never reach a running one. Harm follows Fate Condensed: each stress box
takes one shift, each consequence its shifts, and what is left takes the character out. A conflict
runs in exchanges: `+encounter/act` marks who has acted and who acts now, and whoever acts hands the
turn on. The GM's pool starts each encounter with a fate point per player at the first exchange,
plus what a major NPC banked by conceding in an earlier one.

## The ledger

A grant is `` FATE`GRANT`<SOURCE>`<TARGET>`<KEY> ``, holding `base <n>` or `add <n>`. `TARGET` is
`RATING` (a skill or approach), `BOXES` (a stress track) or `REFRESH` (key `ALL`). A value is the
highest base, or the game's own when there is none, plus every add. `+sheet/set` writes the `SHEET`
source, `+sheet/boxes` and `+sheet/refresh` the `STAFF` source, and each `+sheet/grant` a new
`STAFF_<n>`. Packages write their own sources, such as `ROBO_MODE_SCIENCE`. `` FATE`RATING ``,
`` FATE`BOXES `` and `` FATE`REFRESH `` are rebuilt from the ledger after every change.

## Advancement

Awards have a ledger of their own, apart from the build ledger, and it is only ever added to. An award
is `` FATE`ADV`<n> `` on the character, holding its kind (`milestone`, `breakthrough`, `refresh` or
`skill`), with `BY` (the keeper's objid), `AT` (`secs()`), `WHY` and `GAVE` (its letters) beneath. The
letters are `M` (milestone), `S` (skill step), `H` (new high concept) and `R` (point of refresh). Each
spend adds `` USED`<m> `` (its letter and the advance as typed) with `BY` and `AT`. `+sheet/clear` adds
`BACK` (who, when) to each spend it gives back, and `+sheet/void` adds `VOID` (who, when, why).

What is left to spend is a cache: `` FATE`UNSPENT `` holds every letter not spent and
`` FATE`UNSPENT`<n> `` award `<n>`'s. It is worked out again from the ledger after every award, spend,
void and clear: an award's letters, less those of its spends not given back, and none once void. What
a spend buys goes into the build ledger as grants from the `ADVANCE` source.

Each option is `` ADVANCE`<KEY> `` on the **Fate Sheet** object, holding its description, with
`TOKEN` (the letter it costs; `%0` the character, `%1` what was typed after the option, `%2` the value
after `=`), `USAGE`, `SKIP` (`%0`: 1 when it is not offered) and `RUN` (`%0`, `%1`, `%2`: makes the
change and returns what happened, or `#-1` and why, before it changes anything). A package adds its
own the same way. An option with `KEEPS` set buys something `+sheet/clear` does not take away; the
clear gives every other spend back. `swap` exchanges the two skills' grants from every source.

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
FATE`GRANT`<SOURCE>`<TARGET>`<KEY>   a grant: base <n> or add <n>
FATE`RATING`<KEY>           a skill's or approach's rating, from the ledger; unset is Mediocre (+0)
FATE`ASPECT`<SLOT>          CONCEPT, TROUBLE, 1, 2, ...
FATE`STUNT`<n>              a stunt, 1 to the stunts setting
FATE`STRESS`<TRACK>         the marked boxes, a space list
FATE`BOXES`<TRACK>          a track length of their own; unset is the track's
FATE`CONSEQUENCE`<SLOT>     a consequence
FATE`POINTS                 fate points; unset is the refresh
FATE`REFRESH                a refresh from the ledger; unset is the game's
FATE`ENCOUNTERS             the encounters they are in, in the order they joined
FATE`USING                  the one +encounter/use picked
FATE`ADV`<n>                an award, with BY, AT, WHY, GAVE, USED`<m> (BY, AT, BACK) and VOID beneath
FATE`UNSPENT`<n>            the cache of what each award has left; FATE`UNSPENT all of it
```

Encounters live on **Fate Encounters**:

```
ENC`<n>                     the room's objid
ENC`<n>`TITLE               the title, if any
ENC`<n>`LEAD                the GM who started it
ENC`<n>`PEOPLE              who takes part, objids
ENC`<n>`C`<char key>`<leaf> their copy of each leaf PLAY` names, and POINTS
ENC`<n>`S`<char key>        their standing: HAD (consequences they came in with), OUT, VICTORIES
ENC`<n>`N`<k>               an NPC's name: FROM (its template), a copy of the template's leaves, OUT,
                            VICTORIES
ENC`<n>`A`<k>               an aspect on the scene: INVOKES, BOOST, BY
ENC`<n>`EXCHANGE            the exchange; ACTED who has acted in it, CURRENT who acts now
ENC`<n>`POOL                the GM's fate points
NEXT                        the last number given out
```

Opposition lives on **Fate Opposition**:

```
NPC`<n>                     the name
NPC`<n>`KIND                minor or major
NPC`<n>`OWNER               who made it; SHARED 1 when every GM may use it
NPC`<n>`ASPECT`<k>          aspects 1 to 5; STUNT`<k> stunts 1 to 5
NPC`<n>`SKILL`<KEY>         a rating
NPC`<n>`BOXES`<TRACK>       stress boxes; SLOTS its consequence slots
NPC`<n>`FIELD`<NAME>        a field a package adds
NPC`<n>`POINTS              fate points a major NPC banked by conceding
NEXT                        the last number given out
```

A package adds an NPC field with `` NPCFIELD`<NAME> `` on the Fate Sheet (%0 the value typed: the value
to keep, or `#-1` and why), shown through `` NPCFIELD`<NAME>`SHOW ``. `` NPC`ROLL `` (%0 the NPC's
object/attribute, %1 what followed ` vs `: what to add to the roll, or `#-1` and why), `` NPC`HIT `` (%0,
%1, %2 the check: words after the roll) and `` NPC`HARM `` (%0, %1 the shifts: what gets through, then
why) change how it rolls and takes harm. Atomic Robo uses them for scale, Weapon and Armor.
Any number of `` AFTER`NPC`<NAME> `` hooks (%0 the copy's object/attribute) run after an NPC's
stress changes in an encounter; what each returns is added to the message. The Adversary Toolkit
pack uses one to thin a filler mob as its members go down.
Any number of `` SOAK`<NAME> `` hooks (%0 the player, %1 their encounter copy's object/attribute)
return more shifts a player can take before a hit takes them out, and `` SOAK`<NAME>`TEXT `` how,
which `+encounter/harm` adds to what it tells the player. The System Toolkit pack's conditions use one.
Any number of `` RATE`<NAME> `` hooks (%0 the roller, %1 the skill or approach key, upper case) return
a number that `API`CHECK` adds to the rating in every roll. The System Toolkit pack's super skills use one
for a skill stepped back after its power is used.

The lists are `+config` tables on **Fate Sheet Store**: `SKILL`, `APPROACH`, `TRACK` (with `BOXES`)
and `CONSEQUENCE` (with `SHIFTS`).

## The sheet API

The same `API` tree as every sheet package (see [sheet-d20](../sheet-d20/README.md#the-sheet-api)):
`TRAITS` (every one `always`), `ALWAYS`, `FIND`, `LABEL`, `RATING`, `HAS`, `TARGET` (difficulty,
ladder word or number), `TIER` (from the shifts) and `CHECK` (named `roller`, `trait`, `modifier`,
`target`; returns `{"tier","total","shifts","target","margin","label","text","roll","formula"}`).
Fate adds `LADDER` (a rating's word), `POINTS` (a character's fate points) and `AWARD` (gives or
takes fate points, never below 0, and returns the new count). `POINTS` and `AWARD` always read and
write the sheet itself, never an encounter's copy.

A package that builds part of the sheet uses the ledger:

- `GRANT` (named `who`, `source`, `target`, `key`, `kind` `base` or `add`, `value`; an empty value
  takes the grant away) writes one grant. `#-1` and why when it is wrong.
- `REVOKE` (named `who`, `source` a source or a pattern such as `ROBO_*`) takes away every grant from it.
- `REBUILD` (`%0` a character) works the ratings, tracks and refresh out again. Call it after grants.
- `PLAY` (`%0`, `%1` a leaf under `FATE`) and `PLAYSET` (`%0`, `%1`, `%2` the value; empty clears)
  read and write play state where play goes: an encounter's copy while the character is in one, else
  the sheet. For a package's own `PLAY` leaves, such as a machine's stress.

Bridges may set `` HINT`<message> ``, `` GATE`EDIT `` and `` ALLOW`VIEW`<name> `` on the **Fate
Sheet** object, as on the d20 sheet, and two more:

- `` GATE`SET `` (`%0` the player): a reason nobody, keepers included, sets ratings with `+sheet/set`,
  for a package that works them out itself, such as [`atomic-robo`](../atomic-robo/)'s modes.
  While it is set the sheet gives no `pyramid` warning, since its ratings are not the player's to arrange.
- `` SECTION`<name> `` (`%0` the character, `%1` the reader): a part of the `+sheet` screen, drawn after
  the consequences under a rule titled by its `` SECTION`<name>`TITLE `` leaf, in the order of its
  `` SECTION`<name>`ORDER `` (50 when unset). A section that gives nothing is left out.
- `` PLAY`<name> ``: a leaf under `FATE` that an encounter copies, `*` for every one beneath it
  (`` STRESS`* ``). The sheet names `` STRESS`* ``, `` CONSEQUENCE`* `` and `POINTS`.
- `` BUILD`<name> ``: leaves under `FATE` that `+sheet/clear` takes away along with the grants,
  aspects and stunts, such as `MODE FOCUS`.
- `` CHARGEN`<KEY> ``: a `+chargen` step, holding its name, with `ORDER` (lowest first; the sheet's
  own are `ASPECTS` 10, `SKILLS` 20 and `STUNTS` 30), `DONE` (`%0` the character: 1 when done),
  `TEXT` (`%0`: what to do), `SKIP` (`%0`: 1 when the step does not apply) and `OPTIONAL` (1 when the
  character is complete without it). `` HINT`CHARGEN `` ends the screen once every step is done.
