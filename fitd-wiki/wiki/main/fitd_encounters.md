An encounter is a scene played from copies of the sheets. Stress marked, traumas taken, harm and coin spent in
it stay in it, so a score that runs over several days, or two scenes at once, never mix.

## Taking part

- `+encounter` lists the encounters in your room and the ones you are in.
- `+encounter/join` takes part with a copy of your sheet as it is now.
- While you are in the encounter's room, `+check`, `+check/resist`, stress, trauma, harm and coin use your copy
  there. Anywhere else, your sheet.
- `+encounter/use <n>` picks which copy you roll from, when you are in more than one here.
- `+encounter/leave` comes out, and your copy is gone.

## Running one

`+encounter/start <title>` starts one in your room, and you run it. You may bring someone in with
`+encounter/add <name>`, change the stress, trauma, harm and coin of anyone playing from its copies
(`+sheet/harm <name>/2=Cut`), and take someone out with `+encounter/remove <name>`.

`+encounter/end` ends it, and every copy goes. Nothing reaches the sheets unless you keep it first:
`+encounter/keep <name>` writes that character's stress, trauma, harm and coin from the copy to their sheet.

## Position and effect

The GM sets each member's position and effect: `+encounter/position Alice=risky great`. While it is set,
`+check` with no position rolls at it, and the line says the effect. Effect is limited, standard or great.

## Threats

The GM adds threats from the game's list: `+foe/bestiary` lists the kinds with their tier, clock and harm,
and `+foe/add guard=2` brings in Watch guard 1 and Watch guard 2. Each has its own clock, and they all go when
the encounter ends.

- `+foe` lists the threats in the encounter; `+foe <threat>` shows one.
- Your effect fills a threat's clock: the GM ticks it with `+foe/tick <threat>=<effect>`, limited 1 segment,
  standard 2, great 3. A full clock overcomes the threat.
- When a threat hurts someone, the GM marks its harm on their copy with `+foe/harm <threat>=<name>`. A full
  level pushes the harm up one, as `+sheet/harm` does.

Staff change the list with `+config fitd/foes`.


---

*Based on the Blades in the Dark SRD (CC BY 3.0). See [[About these pages|help:fitd_license_notice]].*
