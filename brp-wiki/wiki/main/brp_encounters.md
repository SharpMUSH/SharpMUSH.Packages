An encounter is a scene played from copies of the sheets. Hit points lost, power points and coin spent, and
experience checks marked in it stay in it, so an adventure that runs over several days, or two scenes at once,
never mix.

## Taking part

- `+encounter` lists the encounters in your room and the ones you are in.
- `+encounter/join` takes part with a copy of your sheet as it is now.
- While you are in the encounter's room, hit points, power points, coin and the checks your rolls mark use your
  copy there. Anywhere else, your sheet.
- `+encounter/use <n>` picks which copy you play from, when you are in more than one here.
- `+encounter/leave` comes out, and your copy is gone.

## Running one

`+encounter/start <title>` starts one in your room, and you run it. You may bring someone in with
`+encounter/add <name>`, change the hit points, power points, coin and marks of anyone playing from its copies
(`+sheet/hp <name>=-3`), and take someone out with `+encounter/remove <name>`.

`+encounter/end` ends it, and every copy goes. Nothing reaches the sheets unless you keep it first:
`+encounter/keep <name>` writes that character's hit points, power points and coin from the copy to their
sheet, and adds the copy's experience checks.


---

*Contains ORC Licensed Material from Basic Roleplaying: Universal Game Engine. See [[About these pages|help:brp_license_notice]].*
