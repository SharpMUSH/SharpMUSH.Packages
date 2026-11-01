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


---

*Based on Ironsworn by Shawn Tomkin, under CC BY 4.0. See [[About these pages|help:ironsworn_license_notice]].*
