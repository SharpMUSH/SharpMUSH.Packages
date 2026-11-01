When an attack lands, its shifts of harm have to go somewhere.

## Stress

Stress is the minor harm that goes away after a scene: bruises, fatigue, frayed nerves. Each character has a **physical** and a **mental** track. Each box you mark takes one shift of harm, and you may mark as many boxes as you have left. `+sheet/stress physical=2` marks box 2, and `+sheet/recover` clears every box once the scene is over.

## Consequences

Consequences are aspects for lasting harm. Each slot takes a set number of shifts:

| Consequence | Shifts |
|---|---|
| Mild | 2 |
| Moderate | 4 |
| Severe | 6 |

`+sheet/consequence mild=Bruised ribs` takes one. Like any aspect, others may invoke it against you, and the first invocation is free for whoever caused it.

## Taken out and conceding

If you can't absorb all the shifts of a hit with stress and consequences, you are **taken out**: the attacker decides what happens to you. Before a roll is made, you may **concede** instead: you lose, but you choose how, and you get a fate point, plus one for each consequence you took in the conflict.

## Recovering

A consequence clears once someone has started your recovery with a roll that suits it, and enough time has passed: a mild one after a whole scene, a moderate one after a whole session, and a severe one after a scenario. Clear it with `+sheet/consequence mild=`.

In an encounter, stress and consequences go on the encounter's copy of your sheet: see [[Encounters|main:fate_encounters]].

---

*Rules based on the Fate SRDs under CC BY 3.0. See [[Fate License Notice|help:fate_license_notice]].*
