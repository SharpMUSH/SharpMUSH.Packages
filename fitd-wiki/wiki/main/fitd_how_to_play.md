Say what your character does. When it is risky and the outcome is in doubt, the GM names an action and a
position, and you roll.

## Rolling an action

`+check <action>` rolls one die for each point of the action's rating and reads the highest die:

| Highest die | Result |
|---|---|
| 6 | A full success: you do it. |
| 4 or 5 | A partial success: you do it, with a cost or a complication. |
| 1, 2 or 3 | A bad outcome: things go wrong. |

Two or more 6s are a critical: you do it with an extra edge. An action rated 0 rolls two dice and reads the
lower, and never counts as a critical.

## Position

`+check skirmish=risky` names the position. Controlled is the safest, risky the usual, desperate the
most dangerous: the worse the position, the worse a bad outcome is. The GM may give a difficulty word instead,
which stands for a position and sometimes takes a die away, unless your game changed them:

| Difficulty | Position | Dice |
|---|---|---|
| trivial | none | - |
| easy | controlled | - |
| standard | risky | - |
| hard | desperate | - |
| extreme | desperate | -1 |

`none` means there is no roll: it simply happens.

## More dice

`+check wreck+1=risky` adds a die, for help from a friend or for pushing yourself. `-1` takes one away.
`/private` rolls where only you see it.

## Resisting

When a consequence lands, you may resist it. `+check/resist <attribute>` rolls one die for each action under
that attribute rated 1 or more. The consequence is lessened or avoided, and it costs 6 less the highest die in
stress. Two 6s clear 1 stress instead.

## Example

`+check skirmish=risky`

Output: `[SHEET] Alice rolls Skirmish (risky): 2d6kh1[(3), 6] = 6: a full success (roll 42)`


---

*Based on the Blades in the Dark SRD (CC BY 3.0). See [[About these pages|help:fitd_license_notice]].*
