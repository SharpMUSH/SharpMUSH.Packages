Characters in Fate change through **awards** that staff give for play. Fate has no money or experience points: wealth is the Resources skill, and growth comes from milestones.

## Awards

- A **milestone** comes at the end of a session, or when something important happens. It buys one change.
- A **breakthrough** comes at the end of an arc. It gives a milestone, one skill step and a new high concept.
- A **power-up** sometimes follows a breakthrough, when the story has moved up a level. It gives a point of refresh or a second skill step.

Staff give them with `+sheet/milestone <name>[=<reason>]`, `+sheet/breakthrough <name>[=<reason>]` and `+sheet/powerup <name>/refresh` or `<name>/skill`. Every award stays on the character with who gave it, when and why, so the list is the record of how the character grew. A mistaken award is voided with `+sheet/void <name>/<n>=<reason>`: what it had not bought is taken back, and the award stays on the list marked void.

## Spending them

`+sheet/advance` shows what you have to spend and every option you can spend it on.

| Option | Costs | What it does |
|---|---|---|
| `swap <skill>=<skill>` | milestone | Switches two skills' ratings, or puts a new skill at Average in place of an Average one |
| `aspect <slot>=<aspect>` | milestone, or a new high concept | Rewrites an aspect; the high concept needs a breakthrough |
| `stunt <slot>=<stunt>` | milestone | Rewrites a stunt, or buys a new one for a point of refresh |
| `skill <skill>` | skill step | Raises one skill a step, even from Mediocre to Average |
| `refresh` | point of refresh | Adds one to your refresh |

Your refresh never goes below 1, so a stunt bought with refresh needs 2 or more. `+sheet/advances` lists every award: who gave it, why, what is left and what it bought. Packages add options of their own, such as switching modes.

For example:

`+sheet/advance swap fight=shoot`

Output: `[SHEET] Done: Alice spends a milestone from award 4: Fight is Mediocre (+0) and Shoot Average (+1).`

---

*Rules based on the Fate SRDs under CC BY 3.0. See [[Fate License Notice|help:fate_license_notice]].*
