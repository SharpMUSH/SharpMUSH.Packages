`+chargen` walks you through making your character. It lists the steps, ticks the ones you have done, and explains the next one. Run it again after each step.

## The steps

1. **Aspects.** Write a high concept, a trouble and the rest of your aspects: `+sheet/aspect concept=<text>`, `+sheet/aspect trouble=<text>`, `+sheet/aspect 1=<text>`. See [[Aspects and Fate Points|main:fate_aspects_and_fate_points]].
2. **Ratings.** Rate your skills or approaches with `+sheet/set <skill>=<rating>`. See [[Skills and Approaches|main:fate_skills_and_approaches]].
3. **Stunts** (optional). Write up to the game's number of stunts with `+sheet/stunt <slot>=<text>`. See [[Stunts|main:fate_stunts]].

A setting package can add steps of its own, or replace one: in Atomic Robo, for example, modes rate your skills instead of `+sheet/set`. Optional steps can stay undone. Once every other step is ticked, `+chargen` says your sheet has everything it needs, and how to send it to staff if the game uses applications.

## After approval

Once your character is approved, staff change your ratings and aspects. Staff can also add a grant of their own with `+sheet/grant`, which stays when anything else changes, or clear the whole build with `+sheet/clear` so you make the character again.

For example:

`+chargen`

Output:

```
[x] Aspects
[ ] Ratings
[ ] Stunts (optional)
Next: Ratings
```

---

*Rules based on the Fate SRDs under CC BY 3.0. See [[Fate License Notice|help:fate_license_notice]].*
