`+chargen` walks you through making your character. On this game it has these steps:

1. **Aspects.** A high concept, a trouble and the rest: `+sheet/aspect concept=<text>`. If you take a weird mode, your high concept must fit it.
2. **Modes.** Pick three and rate them Good, Fair and Average: `+mode/set <mode>=<rating>`. See [[Modes|main:atomic_robo_modes]].
3. **Skill points** (optional). Spend them with `+mode/focus <skill>`.
4. **Stunts** (optional). `+sheet/stunt <slot>=<text>`.
5. **Mega-stunt** (optional, only with a weird mode). `+mode/mega <slot>=<benefits>`. See [[Mega-stunts|main:atomic_robo_mega_stunts]].

You don't rate skills with `+sheet/set` here: the modes do that. Once every step that isn't optional is ticked, `+chargen` says your sheet has everything it needs.

For example:

`+chargen`

Output:

```
[x] Aspects
[ ] Modes
[ ] Skill points (optional)
[ ] Stunts (optional)
Next: Modes
```

---

*Rules based on the Atomic Robo RPG SRD and the Fate System Toolkit under CC BY 3.0. An unofficial fan package. See [[Atomic Robo License Notice|help:atomic_robo_license_notice]].*
