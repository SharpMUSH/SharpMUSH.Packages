Atomic Robo characters grow through the same awards as any Fate character: milestones, breakthroughs and power-ups that staff give for play. See [[Advancement|main:fate_advancement]] for how awards work and the options every Fate sheet has. There is no money to track: gear comes from your aspects, your machine and what you invent.

Modes change what a skill step and a milestone can buy:

| Option | Costs | What it does |
|---|---|---|
| `modes <mode>=<mode>` | milestone | Switches the ratings of two of your modes |
| `point` | skill step | Gives one more skill point, which `+mode/focus <skill>` spends |
| `machine concept=<aspect>` or `machine flaw=<aspect>` | milestone | Rewrites your machine's concept or flaw |
| `upgrade weapon` or `upgrade armor` | skill step | Raises your machine's Weapon or Armor by 1, to 4 at most |

Skills come from your modes here, so `+sheet/advance swap` and `skill` are not offered: switch modes or buy a skill point instead. The machine options appear only while you have a machine. `+sheet/clear` leaves the machine as it is, so what the machine options bought stays spent; everything else the awards bought can be spent again.

For example:

`+sheet/advance modes science=action`

Output: `[SHEET] Done: Bob spends a milestone from award 1: Action (Good), Science (Fair), and Banter (Average).`

---

*Rules based on the Atomic Robo RPG SRD and the Fate System Toolkit under CC BY 3.0. An unofficial fan package. See [[Atomic Robo License Notice|help:atomic_robo_license_notice]].*
