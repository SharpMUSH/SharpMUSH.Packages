A character with a weird mode may turn any stunt into a **mega-stunt**: a stunt with more than one benefit, such as a robot body that is armoured, strong and never needs to breathe.

## The cost

Your stunt slots pay for one benefit each. Every benefit beyond them adds a fate point to the GM's **reserve** while you are in the scene: points the GM spends on the opposition. Each weakness or cost you choose to take on, such as a robot that can't swim, takes one benefit off that bill.

## Commands

- `+sheet/stunt <slot>=<text>` writes the stunt first.
- `+mode/mega <slot>=<benefits>` makes it a mega-stunt with that many benefits, 1 to 10. Leave the number out to make it a plain stunt again.
- `+mode/weakness <slot>=<number>` counts the weaknesses and costs it takes on.
- `+mode/reserve` adds up what everyone in the room puts into the GM's reserve.

For example:

`+mode/mega 1=2`

Output: `[SCIENCE] Done: Stunt 1 on Bob's sheet is a mega-stunt with 2 benefits. Their stunts add nothing to the GM's fate point reserve.`

---

*Rules based on the Atomic Robo RPG SRD and the Fate System Toolkit under CC BY 3.0. An unofficial fan package. See [[Atomic Robo License Notice|help:atomic_robo_license_notice]].*
