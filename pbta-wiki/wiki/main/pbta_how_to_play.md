You describe what your character does. When what you do matches a move's trigger ("When you attack an enemy
in melee..."), you make that move with `+check <move>`: two six-sided dice plus the stat the move names.

| Total | Result |
|---|---|
| 10 or more | A full hit: you get what you wanted. |
| 7 to 9 | A partial hit: you get it, with a cost, a choice or a complication. |
| 6 or less | A miss: the GM says what happens, and it is rarely good. |

Under the roll you see what the move says for your result.

## Choosing the stat

Most moves name one stat. Some let you choose by how you act: Defy Danger takes Str when you power through and
Dex when you get out of the way, so you type `+check defy danger/dex`. A few add no stat at all.

## Adding to a roll

- `+check <move>+1` adds a number for this roll only, such as your bond when you aid someone.
- `+check <move>=hard` adds the difficulty's modifier: easy +1, standard +0, hard -1, extreme -2. A trivial task needs no roll.
- **Forward** is added to your next roll, then spent. **Ongoing** is added to every roll until it is cleared.
- **Hold** is a count a move gives you to spend later, such as Defend's hold.

`+sheet/forward`, `+sheet/ongoing` and `+sheet/hold` keep track of them.

## The stats

Str, Dex, Con, Int, Wis, Cha. Each runs from -1 to +2 for a new character, and advances raise
them to +3.
