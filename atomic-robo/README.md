# atomic-robo

An unofficial Atomic Robo pack: pulp action science and giant robots on the [Fate sheet](../sheet-fate/). Characters pick three
modes that rate their skills, take mega-stunts, invent gadgets with catches and flaws, brainstorm a
hypothesis together, and pilot machines whose scale counts in a fight.

Based on the Atomic Robo RPG SRD and the Fate System Toolkit, both under CC BY 3.0: see
[NOTICE.md](NOTICE.md). The help and messages are this package's own wording, and the in-game
`+help mode credits` topic carries the attribution. It is an unofficial fan package, not affiliated with or endorsed by Evil Hat Productions or the creators of Atomic Robo, and uses none of the comic's characters or art.

Depends on [`sheet-fate`](../sheet-fate/) 1.1 or later. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`atomic-robo-help`](../atomic-robo-help/) | the `+help atomic-robo`, `+help mode`, `+help machine`, `+help invent` and `+help brainstorm` topics |
| [`atomic-robo-config`](../atomic-robo-config/) | the settings and the `modes` and `scales` tables in `+config atomic-robo` |

The Fate sheet's own bridges keep working: [`sheet-fate-chargen`](../sheet-fate-chargen/) ties mode,
focus and mega-stunt changes to the player's `+app` application, and [`duties-fate`](../duties-fate/)
rolls the ratings the modes write.

## Commands

| Command | Who | What |
|---|---|---|
| `+mode [<name>]` | all | Modes, skill points and stress boxes |
| `+mode/list` | all | The modes and their skills; weird modes allow mega-stunts |
| `+mode/set <mode>=<rating>` | unapproved player | Choose a mode at one of the `ratings`; empty drops it |
| `+mode/focus <skill>` | unapproved player | Spend 1 point to focus a skill in a mode, 2 more to specialize it |
| `+mode/unfocus <skill>` | unapproved player | Take back a step bought |
| `+mode/stress <mode>=physical\|mental\|split` | unapproved player | Where a mode's extra stress boxes go |
| `+mode/mega <slot>=<benefits>` | unapproved player | Make a written stunt a mega-stunt (needs a weird mode); empty makes it plain |
| `+mode/weakness <slot>=<n>` | unapproved player | Voluntary weaknesses and costs on a mega-stunt |
| `+mode/reserve` | all | What the people in the room add to the GM's fate point reserve |
| `+mode/points <name>=<n>\|default` | keeper | A skill point total of their own |
| `+machine [<name>]` | all | The machine: name, scale, concept, flaw, weapon, armor, stress |
| `+machine/set <field>=<value>` | unapproved player | `name` builds it; `scale`, `concept`, `flaw`, `weapon`, `armor` |
| `+machine/check <skill>[=<opposition>] [vs <scale>]` | player | Pilot it: `Bob pilots Little Tin: Vehicles: 4dF[-1, 1, 1, 1] + 5 = 7 (Epic) against Fair (+2): success with style, 5 shifts (roll 25) Giant against person: +2 to the roll. As an attack it hits for 5 shifts.` |
| `+machine/stress <box>\|clear` | player | Mark or clear the machine's stress |
| `+machine/scrap` | unapproved player | Take it off the sheet |
| `+invent <skill>=<benefits> <function>` | player | Roll against twice the benefits; the outcome says who chooses the catches |
| `+invent[/list] [<name>]` | all | Inventions with their catches and flaws |
| `+invent/catch <n>=<catch>` | player | One catch per benefit |
| `+invent/flaw <n>=<flaw>` | player | The flaw the GM names |
| `+invent/drop <n>` | player | Let one go |
| `+brainstorm/start <question>` | player | One brainstorm per room |
| `+brainstorm/join <aspect>` | player | Take part, compelling an aspect (a fate point when `brainstorm_point`) |
| `+brainstorm <skill>[+<n>]` | player | This round's roll, once each |
| `+brainstorm/next` | lead, keeper | Close the round |
| `+brainstorm/fact <fact>` | round winner | State the fact won |
| `+brainstorm/hypothesis <aspect>` | hypothesis winner | Name what is going on |
| `+brainstorm[/stop]` | all; lead, keeper | Show it; end it |

Keepers (`softcode.fate.admin`, the **Fate Sheet Keeper** role) put `<name>/` before the slot or
field of `/set`, `/focus`, `/unfocus`, `/stress`, `/mega`, `/weakness`, `+machine/set`,
`+invent/catch`, `/flaw` and `/drop` to change anyone's at any time.

## The numbers

- A skill takes the rating of the best mode that holds it, one step more for each other held mode
  that has it too, and the steps bought with `/focus`, at most two steps over the mode.
- Stress tracks start at `stress` boxes. A Fair mode adds one box and a Good mode two, physical
  for `physical` skills (Athletics, Physique) and mental for `mental` ones (Provoke, Will).
- Stunt slots (`+config fate/stunts`) cover one benefit each. Each mega-stunt benefit beyond them,
  less voluntary weaknesses, adds one to the GM's fate point reserve.
- An invention's difficulty is twice its benefits. Fail: the GM chooses every catch. Tie: the GM
  and the inventor take turns, the GM first. Success: the GM one, the inventor the rest. Success
  with style: the inventor all of them.
- A brainstorm's first fact is against `brainstorm_difficulty`, each after it against the last
  winning total. A lone winner gains 1 victory (at a cost on a tie), 2 with 3 shifts or more;
  several winners at the same total gain 1 between them. Three victories or more after three facts
  open the hypothesis roll: free invocations 0 at 3, 1 at 4 or 5, 2 at 6 or more.
- Each step of scale between a machine and its foe gives the larger +1 on the roll (`roll`), 2
  shifts of harm (`harm`), or both (`both`).

## Where the data lives

On each character, beside the sheet's own leaves:

```
FATE`MODE`<KEY>                 a mode's rating
FATE`FOCUS`<SKILL>              steps bought for a skill
FATE`SKILLPOINTS                a keeper's skill point total; unset is the game's
FATE`MODESTRESS`<KEY>           physical, mental or split
FATE`MEGA`<n>                   a mega-stunt's benefits; WEAK beneath: chosen weaknesses and costs
FATE`MACHINE                    the machine's name; SCALE, CONCEPT, FLAW, WEAPON, ARMOR, STRESS beneath
FATE`INVENTION`<n>              an invention's function; BENEFITS, SKILL, OUTCOME, ROLL, FLAW, CATCH`<n> beneath
```

The modes go into the sheet's ledger after every change: a skill's highest mode sets its rating
(source `ROBO_MODE_<mode>`), each other mode that has it adds one, and bought steps add under
`ROBO_FOCUS`; the tracks get `ROBO_STRESS` and what each mode adds. Only `ROBO_` grants are replaced, so
a keeper's `+sheet/grant` stays. `+sheet`, `+check` and Duties read the ratings the sheet builds.

On the **Fate Sheet** it sets `` GATE`SET `` (turns `+sheet/set` off), four `` SECTION` `` hooks (the
modes, mega-stunts, machine and inventions on `+sheet`), `` PLAY`MACHINE `` (an encounter copies the
machine's stress, and `+machine/stress` marks the copy), `` BUILD`ROBO `` (`+sheet/clear` takes the
modes, bought steps and mega-stunts too) and three `+chargen` steps: Modes, Skill points (optional)
and Mega-stunt (optional, for a weird mode only). The sheet's own Ratings step is skipped.

The modes and scales are `+config` tables on **Atomic Robo Store**: `MODE` (with `SKILLS`,
`WEIRD`, `ORDER`) and `SCALE` (with `STEP`). It adds Combat, Vehicles and the sciences to the Fate
sheet's skill list. Live brainstorms are on **Fate Brainstorms**, one branch per room.
