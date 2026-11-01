**Scale** says how big something is: a person, a vehicle, a giant, a titan. When two things of different scale meet, each step between them helps the larger one: +1 on the roll, or two more shifts of harm when it hits, or both, as the game sets.

## Machines

A machine is a giant robot, a tank or a starship on your sheet, built at a scale. It has a name, a concept and a flaw (aspects), a Weapon rating added to the harm it deals, an Armor rating taken off the harm it takes, and stress boxes of its own.

- `+machine/set name=<name>` builds one; `/set scale=`, `concept=`, `flaw=`, `weapon=` and `armor=` fill it in.
- `+machine/check <skill>=<opposition> vs <scale>` pilots it against something of that scale: `+machine/check combat=good vs person`.
- `+machine/stress <box>` marks a stress box; `+machine/stress clear` empties them. In an encounter this marks the encounter's copy, like your own stress: see [[Encounters|main:fate_encounters]].
- `+machine/scrap` takes it off your sheet.

For example:

`+machine/check vehicles=fair vs person`

Output: `[SCIENCE] Bob pilots Little Tin: Vehicles: 4dF[-1, 1, 1, 1] + 5 = 7 (Epic) against Fair (+2): success with style, 5 shifts (roll 25) Giant against person: +2 to the roll. As an attack it hits for 5 shifts.`

---

*Rules based on the Atomic Robo RPG SRD and the Fate System Toolkit under CC BY 3.0. An unofficial fan package. See [[Atomic Robo License Notice|help:atomic_robo_license_notice]].*
