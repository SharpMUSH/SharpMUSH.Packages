On this game your skills come from three **modes** instead of a skill list you rate one by one. A mode is a group of skills, such as Action, Banter, Intrigue or Science. Your three modes are rated Good (+3), Fair (+2) and Average (+1), one each.

## How a skill is rated

- A skill in one of your modes is **trained**: it takes the rating of the best mode that holds it.
- A skill in two of your modes is **focused**: one step higher.
- A skill in all three is **specialized**: two steps higher.
- A skill in none of your modes stays Mediocre (+0).

**Skill points** raise single skills: one point makes a trained skill focused, two more make it specialized. Two steps above its mode is the most a skill gets.

## Weird modes

Some modes make a character more than human: a robot, a pilot bonded to their machine, a secret agent, a soldier of fortune. A weird mode must fit your high concept, and it lets your stunts be [[mega-stunts|main:atomic_robo_mega_stunts]].

## Stress

A Fair or Good mode whose skills include Athletics or Physique adds physical stress boxes; one with Provoke or Will adds mental ones. Fair adds one box, Good two. When a mode's skills fit both, `+mode/stress <mode>=physical`, `mental` or `split` chooses.

## Commands

- `+mode` shows your modes, skill points and stress boxes. `+mode/list` lists every mode and its skills.
- `+mode/set <mode>=<rating>` chooses a mode: `+mode/set science=good`. Leave the rating out to drop it.
- `+mode/focus <skill>` spends skill points; `+mode/unfocus <skill>` takes a step back.
- `+sheet/ledger` shows what each mode grants. A staff grant stays when your modes change.

For example:

`+mode/set science=fair`

Output: `[SCIENCE] Done: Bob's Science mode is Fair (+2): Will, Chemistry, Engineering, Exobiology, Mechanics, Physics, Robotics, and Other sciences.`

---

*Rules based on the Atomic Robo RPG SRD and the Fate System Toolkit under CC BY 3.0. An unofficial fan package. See [[Atomic Robo License Notice|help:atomic_robo_license_notice]].*
