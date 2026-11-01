An encounter is a scene played from copies of the sheets. Hit points lost, coin spent and gear used in it stay
in it, so a fight that runs over several days, or two scenes at once, never mix.

## Taking part

- `+encounter` lists the encounters in your room and the ones you are in.
- `+encounter/join` takes part with a copy of your sheet as it is now.
- While you are in the encounter's room, `+check`, damage, healing, coin and gear use your copy there.
  Anywhere else, your sheet.
- `+encounter/use <n>` picks which copy you roll from, when you are in more than one here.
- `+encounter/leave` comes out, and your copy is gone.

## Running one

`+encounter/start <title>` starts one in your room, and you run it. You may bring someone in with
`+encounter/add <name>`, change the hit points, coin and gear of anyone playing from its copies
(`+sheet/damage <name>=<n>`), and take someone out with `+encounter/remove <name>`.

`+encounter/end` ends it, and every copy goes. Nothing reaches the sheets unless you keep it first:
`+encounter/keep <name>` writes that character's damage, coin and gear from the copy to their sheet.


---

*Written for SharpMUSH. See [[About these pages|help:d20_license_notice]].*
