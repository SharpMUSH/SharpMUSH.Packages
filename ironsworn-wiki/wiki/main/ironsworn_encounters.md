An encounter is a scene played from copies of the sheets. Health, spirit, supply, momentum and companions'
health in it stay in it, so a fight that runs over several days, or two scenes at once, never mix.

## Taking part

- `+encounter` lists the encounters in your room and the ones you are in.
- `+encounter/join` takes part with a copy of your sheet as it is now.
- While you are in the encounter's room, `+check` rolls your copy's stats, and the meters and companions change
  your copy there. Anywhere else, your sheet.
- `+encounter/use <n>` picks which copy you play from, when you are in more than one here.
- `+encounter/leave` comes out, and your copy is gone.

## Running one

`+encounter/start <title>` starts one in your room, and you run it. You may bring someone in with
`+encounter/add <name>`, change the meters and companions of anyone playing from its copies
(`+sheet/health <name>=-2`), and take someone out with `+encounter/remove <name>`.

`+encounter/end` ends it, and every copy goes. Nothing reaches the sheets unless you keep it first:
`+encounter/keep <name>` writes that character's meters and companions' health from the copy to their sheet.

## Foes

The GM adds foes from the game's bestiary: `+foe/bestiary` lists the kinds with their rank and nature, and
`+foe/add wolf=2` brings in Wolf 1 and Wolf 2. Each foe has a progress track of ten boxes, as a vow does.

- `+foe` lists the foes in the encounter; `+foe <foe>` shows one, with its features, drives and tactics.
- When you strike or gain ground, `+foe/mark <foe>` marks progress by its rank, as `+vow/mark` does.
- `+foe/end <foe>` makes the progress roll to end the fight: a strong hit beats the foe, a weak hit beats it at a
  cost the GM names, and a miss turns the fight against you.
- The GM deals a foe's harm with `+foe/harm <foe>=<name>`: 1 for troublesome up to 5 for epic, off your copy's
  health. Endure it with `+check`.
- `+encounter/initiative =yes` or `=no` says whether you have the initiative; the GM sets anyone's.

| Rank | Ticks a mark fills | Harm |
|---|---|---|
| troublesome | 12 | 1 |
| dangerous | 8 | 2 |
| formidable | 4 | 3 |
| extreme | 2 | 4 |
| epic | 1 | 5 |

## Example

`+foe/end wolf 2`

Output: `[ENCOUNTER] Alice ends the fight with Wolf 2: progress 8 vs 9 and 4: a weak hit. It is beaten, at a cost the GM names. (roll 85)`

Staff change the bestiary with `+config ironsworn/foes`. The foes go when the encounter ends.


---

*Based on Ironsworn by Shawn Tomkin, under CC BY 4.0. See [[About these pages|help:ironsworn_license_notice]].*
