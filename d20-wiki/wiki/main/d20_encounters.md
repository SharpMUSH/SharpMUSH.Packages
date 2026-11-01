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

## Foes

The GM adds foes from the game's bestiary: `+foe/bestiary` lists the kinds, with their level, AC, hit points
and attack, and `+foe/add goblin=3` brings in Goblin 1, Goblin 2 and Goblin 3. Each keeps its own hit points
and conditions, and they all go when the encounter ends.

- `+foe` lists the foes in the encounter; `+foe <foe>` shows one.
- `+check <trait>=<foe>` rolls against that foe's AC.
- The GM rolls a foe's attack with `+foe/attack <foe>=<name>/<AC>`. A hit takes the damage off that member's
  copy. A natural 20 always hits and doubles the damage dice.
- `+foe/damage <foe>=<n>` and `+foe/heal <foe>=<n>` change a foe's hit points; at 0 it is down.

Staff change the bestiary with `+config d20/foes`.

## Turns

`+encounter/initiative` rolls 1d20 for everyone: members add Dexterity from their copy, foes their
initiative. `+encounter/next` passes the turn on, skipping foes that are down, and starts a new round after
the last. The GM passes any turn, and a member passes their own. `+encounter/order` shows the round, the
order, hit points and conditions.

`+encounter/condition <name or foe>=prone 1` marks a condition for a number of rounds, counted down at the
start of each of its holder's turns. Without rounds it stays until `=!prone` takes it off.


---

*Written for SharpMUSH. See [[About these pages|help:d20_license_notice]].*
