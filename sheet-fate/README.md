# sheet-fate

A Fate character sheet: skills on the ladder (or the six approaches), aspects, stunts, stress tracks,
consequences, fate points and refresh. Players fill in their skills and aspects until they are
approved, with `+chargen` showing what is left to do. They keep their own stress, consequences and
fate points in play, and roll four Fate dice against an opposition with `+check`, which the whole room
sees and the game keeps as a recorded roll. Ratings, stress boxes and refresh are built from a ledger
of grants, so a staff bonus or a package's grant survives the player's own changes. An encounter keeps
its own copy of each player's fate points, stress and consequences until the GM keeps it or ends the
encounter. Keepers give milestones, breakthroughs and power-ups, which stay on the character as a log
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
NEXT                        the last number given out
```

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
