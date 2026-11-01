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

## Creatures

The GM adds creatures from the game's bestiary: `+foe/bestiary` lists the kinds with their hit points,
armour and attack, and `+foe/add wolf=2` brings in Wolf 1 and Wolf 2. Their hit points and damage bonus come
from their characteristics, as yours do, and they all go when the encounter ends.

- `+foe` lists the creatures in the encounter; `+foe <creature>` shows one.
- When you hit one, roll your weapon's damage and tell the GM, who takes it off with
  `+foe/damage <creature>=<n>`, less its armour. A blow of half its hit points or more is a major wound.
- The GM rolls a creature's attack with `+foe/attack <creature>=<name>/<armour>`. A hit comes off your copy's
  hit points, less your armour. A special hit rolls the weapon's dice twice; a critical does too, and ignores
  armour. Parry or dodge with your own `+check` first.
- With the game's `locations` setting, each blow says where it lands: legs, abdomen, chest, arms or head.

## The order of play

`+encounter/initiative` puts everyone in order, highest DEX first. With the game's `strikeranks` setting,
lowest strike rank goes first: DEX and SIZ each give part of it. `+encounter/next` passes the turn on, and
`+encounter/order` shows the round and whose turn it is. `+encounter/condition <name>=prone 1` marks a
condition for a number of rounds.

Staff change the bestiary with `+config brp/foes`.


---

*Contains ORC Licensed Material from Basic Roleplaying: Universal Game Engine. See [[About these pages|help:brp_license_notice]].*
