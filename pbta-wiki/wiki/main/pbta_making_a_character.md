`+sheet/chargen` shows every step, which are done, and the command for the next one. Until your character is
approved you can change any choice; each change replaces the one before.

## 1. Pick a playbook

`+sheet/playbook` lists them, with their suggested stats and moves. `+sheet/playbook <playbook>` picks one,
and if you have not set any stat yet you get its suggested stats. See [[Playbooks|main:pbta_playbooks]].

## 2. Give out your stats

You have the numbers +2, +1, +1, 0, 0 and -1, one for each stat. `+sheet/set <stat>=<number>` gives a stat
one of the numbers still free; `+sheet/set <stat>=` frees it again, so to swap two stats free one first.

## 3. Pick your moves

You have every basic move and your playbook's starting moves. Each playbook also lets you pick one or more of
its other moves: `+sheet/take <move>`, and `+sheet/drop <move>` to change your mind. Changing your playbook
gives back the moves you picked from the old one.

## Example

```
+sheet/playbook warden
+sheet/set str=2
+sheet/set con=1
+sheet/take stand fast
+sheet/chargen
```

When every step shows done, your sheet is complete. If the game uses applications, `+app/submit` sends it to
staff with yours.

Everything you choose is kept on your sheet's ledger, `+sheet/ledger`.
