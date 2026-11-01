An encounter is a scene played from copies of the sheets. When you join one, it takes a copy of your sheet as
it is then, and while you are in its room your rolls, forward, ongoing and hold use that copy. Nothing that
happens there reaches your sheet or any other scene, however many days the encounter runs.

## Taking part

- `+encounter` lists the encounters in your room and the ones you are in; `+encounter <n>` shows one.
- `+encounter/join <n>` takes part. `+encounter/leave <n>` comes out, and the copy is gone.
- In more than one encounter in the same room? `+encounter/use <n>` picks which copy you roll from.

## Running one

`+encounter/start <title>` starts one in your room, and you run it. You can bring people in with
`+encounter/add <name>=<n>`, take them out with `/remove`, and end it with `+encounter/end <n>`. Ending it
drops every copy. To let something last, such as forward or hold a character earned, `+encounter/keep
<name>=<n>` writes their copy's forward, ongoing, hold and harm to their sheet first.

## Harm

Your sheet counts the harm you have taken, up to the most your game allows (6 unless it changed that); at the
most you are out of action, and Last Breath is near. `+sheet/harm <n>` marks harm and `+sheet/heal <n>` or
`all` takes it off. In an encounter they change your copy there, and its GM can change them for you.

## Foes

The GM adds foes from the game's bestiary: `+foe/bestiary` lists the kinds with their hit points, armour and
damage, and `+foe/add goblin=3` brings in Goblin 1, Goblin 2 and Goblin 3. Each has its own hit points, and
they all go when the encounter ends.

- `+foe` lists the foes in the encounter; `+foe <foe>` shows one, with its tags.
- When you deal harm, the GM takes it off with `+foe/harm <foe>=<harm>`, less the foe's armour. Harm that
  ignores armour, or pierces some of it, says so: `+foe/harm ogre 1=5 piercing 2`.
- When a foe hurts someone, the GM rolls its damage with `+foe/deal <foe>=<name>/<armour>`, and it goes on
  that member's harm, less their armour.
- `+foe/move` shows the GM a GM move picked at random, and `+foe/move <foe>` one of that foe's own moves.

Staff change the bestiary with `+config pbta/foes` and the GM moves with `+config pbta/gmmoves`.
