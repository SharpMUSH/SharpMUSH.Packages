Say what your character does. When the outcome is in doubt, the GM asks for a check on an ability or a skill.

## Making a check

`+check <trait>` rolls 1d20 and adds what the trait adds. The room sees the roll, and the game keeps it.

`+check athletics=15` rolls against DC 15. Meeting the DC is a success; falling short is a failure.

The difficulty words stand for these DCs, unless your game changed them:

| Difficulty | DC |
|---|---|
| trivial | 5 |
| easy | 10 |
| standard | 15 |
| hard | 20 |
| extreme | 25 |

`+check stealth=hard` uses the word. `+check stealth+2=hard` adds 2 for this roll, and `-2` takes 2 away.

## Advantage and disadvantage

`+check/advantage` rolls two dice and keeps the higher; `+check/disadvantage` keeps the lower. The GM says
when a situation gives either. `/private` rolls where only you see it.

## Natural 20 and natural 1

A 20 on the die is a critical success and a 1 a critical failure, whatever the total, unless your game turns
that off.

## Example

`+check/advantage perception=15`

Output: `[SHEET] Alice checks Perception: 2d20kh[17, (4)] + 2 = 19 vs DC 15: success (roll 42)`


---

*Written for SharpMUSH. See [[About these pages|help:d20_license_notice]].*
