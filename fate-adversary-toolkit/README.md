# fate-adversary-toolkit

An unofficial Fate Adversary Toolkit pack: opposition for the [Fate sheet](../sheet-fate/). A library
of ready adversaries copied into `+npc` at the game's power level, adversaries built by type from the
toolkit's recipes, filler mobs that thin as they take stress, hazards, blocks and distractions in an
encounter, countdowns, and resistances and limitations on any NPC.

Based on the Fate Adversary Toolkit SRD under CC BY 3.0: see [NOTICE.md](NOTICE.md). The library's
Forward Scout, Baron von Darkness, obstacles and resistance examples are the SRD's; the other
adversaries are this package's own. The in-game `+help adversary credits` topic carries the
attribution. It is an unofficial fan package, not affiliated with or endorsed by Evil Hat Productions.

Depends on [`sheet-fate`](../sheet-fate/) 1.4 or later, whose `` AFTER`NPC` `` hooks thin a mob as its
members go down. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`fate-adversary-toolkit-help`](../fate-adversary-toolkit-help/) | the `+help adversary`, `+help obstacle` and `+help countdown` topics |
| [`fate-adversary-toolkit-config`](../fate-adversary-toolkit-config/) | the settings and the `adversaries` and `obstacles` libraries in `+config adversary` |
| [`fate-adversary-toolkit-wiki`](../fate-adversary-toolkit-wiki/) | wiki pages on enemies, obstacles and constraints |

## Commands

| Command | Who | What |
|---|---|---|
| `+adversary [<name>]` | all | The library, or one adversary in full |
| `+adversary/make <name>[/<peak>][=<new name>]` | all | Copy one into `+npc` as yours, its ratings moved to the PCs' best skill |
| `+adversary/build <name>=<type> [tough] [<quality>] <skills>[/<peak>]` | all | Build a threat, hitter, boss or average/fair/good filler by the toolkit's recipe, skills best first |
| `+adversary/mob <filler>[=<2 to 12>]` | GM | Bring a group of fillers into the encounter you run as one NPC |
| `+adversary/stunts` | all | Quick enemy stunts |
| `+obstacle [<name>]` | in the encounter | The obstacles in it, or one |
| `+obstacle/list [<name>]` | all | The obstacle library |
| `+obstacle/add <obstacle>[/<peak>][=<name>]` | GM | One from the library; one with a countdown starts it |
| `+obstacle/hazard <name>=<rating>[/<weapon>]`, `/block` | GM | Make one |
| `+obstacle/distraction <name>=<choice>[/<opposition>]` | GM | Make one; `/repercussion <obstacle>=<text>` adds what leaving it costs |
| `+obstacle/lock <obstacle>=<lock>[/<key>]` | GM | A resistance; empty clears it |
| `+obstacle/roll <hazard>[+<n>][=<opposition>]` | GM | A hazard's turn |
| `+obstacle/overcome <obstacle>=<skill>[+<n>]`, `/disable` | in the encounter | Get past one, or take it out of play (a block's rating plus two) |
| `+obstacle/remove <obstacle>` | GM | Take one out |
| `+countdown [<name>]` | all | The countdowns you can see here, or one |
| `+countdown/start <name>=<boxes>[/<outcome>]` | all | Start one; `+countdown/start <adversary or obstacle>` starts the library's |
| `+countdown/trigger <name>=<text>`, `/outcome` | starter, keeper | What marks a box; what happens at the end |
| `+countdown/tick <name>[=<why>]`, `/untick` | starter, keeper | Mark a box, or take one back |
| `+countdown/hide <name>` | starter, keeper | Keep it to the starter and keepers; again shows it |
| `+countdown/stop <name>` | starter, keeper | End it |

GM is whoever runs the encounter, and sheet keepers (`softcode.fate.admin`). `+npc/set <npc>/type=`,
`lock=`, `key=` and `limit=` set an NPC's type, resistance and limitation.

## The numbers

- `peak` is the PCs' best skill (0 takes the Fate sheet's cap). A library entry carries the peak it
  was written for, and `/make` moves every rating by the difference, within -2 to 8.
- Threats and hitters: peak+1, two at peak, three at peak-1. Bosses: peak+2, then two, three, four
  skills a step lower each down to Fair, every other skill Average. Tough adds one to each and a
  consequence.
- A built threat or boss gets the sheet's boxes plus one for an Average or Fair `track_skills` skill
  and two for Good or better; hitters keep the base. Fillers get one box per quality step.
- A mob of fillers adds +1 for every two members to each skill, to `mob_cap`; its track is the
  members' boxes in a row, and its skills fall as members go down.
- An obstacle's library rating is written for peak 4 and moves by the difference too.

## Where the data lives

```
Fate Adversary Store   TPL`<KEY> adversaries, OBS`<KEY> obstacles; +config tables
Fate Encounters        ENC`<n>`OBS`<k> an encounter's obstacles (TYPE RATING WEAPON CHOICE REP`<j> LOCK KEY DISABLED)
Fate Opposition        NPC`<n>`FIELD`TYPE/LOCK/KEY/LIMIT; a mob's MOB`SIZE/EACH/LEFT/TRACK/BASE`<KEY>
Fate Countdowns        CD`<n> (BOXES MARKED OUTCOME TRIG`<j> OWNER ROOM ENC HIDDEN)
```
