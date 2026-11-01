This game runs Pathfinder Second Edition in softcode, through the `pf2e` package. The rules are those of Player Core, Player Core 2, GM Core and Monster Core as Foundry VTT's pf2e system has them. These pages are the rules; this one is the commands. In the game, `+help pf2e` lists the same commands.

## Make your character

`+build` shows every step of character creation, what is done, and what to type next. Work down the list:

1. `+build/ancestry`, `+build/heritage`, `+build/background` and `+build/class`, each with a name. The start of a name is enough when only one fits.
2. `+build/boost ancestry`, `+build/boost background`, `+build/boost class` and `+build/boost 1`, each followed by `=` and the attributes. Type a set without attributes to see what it asks for.
3. `+build/skills` with every skill you choose, then `+build/language` with your extra languages.
4. `+build/feat` for each feat slot, such as `+build/feat class-1=Sudden Charge`. `+build/list feats class-1` lists only the feats whose prerequisites you meet.
5. `+build/choose` for each choice a feature asks for, such as a barbarian's instinct: `+build/choose instinct=giant`.
6. Buy your starting gear from 15 gp with `+build/buy`, then `+build/equip` your weapon as held and your armor as worn.
7. `+build/done` finishes the sheet.

`+build/info <name>` describes anything, and `+build/undo <step>` takes a step back with everything that came with it.

For example, a human barbarian:

```
+build/ancestry Human
+build/heritage Skilled Human
+build/background Warrior
+build/class Barbarian
+build/boost ancestry=str con
+build/boost background=str wis
+build/boost class=str
+build/boost 1=str dex con wis
+build/skills acrobatics survival stealth
+build/language goblin
+build/choose skill=medicine
+build/choose instinct=giant
+build/feat ancestry-1=Natural Ambition
+build/feat class-1=Sudden Charge
+build/choose energy=fire
+build/choose natural ambition=adrenaline rush
+build/buy greataxe
+build/equip greataxe=held
+build/buy hide armor
+build/equip hide armor=worn
+build/done
```

Output of the class step:

```
[PF2E] Done: Class: Barbarian.
[PF2E] Next: Ancestry boosts. Type +build/boost ancestry. +build shows every step.
```

## Your sheet and checks

`+sheet` shows the finished character: attributes, hit points, AC, every skill and save with its modifier, Strikes, gear, feats and features. `+check athletics=15` rolls a check against a DC and says the degree of success:

```
[PF2E] Amiri rolls Athletics: 1d20[16] + 7 = 23 vs DC 15: Success (roll 178)
Strength +4, Trained +3
```

Your sheet is a ledger. Every choice, award and purchase is an entry, and nothing is overwritten, so staff can always see how a character came to be.

## Encounters

The GM starts a fight with `+enc/start`; you take part with `+enc/join`. `+enc/init` rolls initiative and `+enc/next` moves through the turns, handling persistent damage, frightened, timed conditions and recovery checks. On your turn, `+enc/strike <target>` attacks with the multiple attack penalty counted, and `+enc/use <item>` uses a consumable.

An encounter keeps its own copy of everyone in it. Hit points, conditions, dying and the potions you drink stay in the encounter and never change your sheet, so an encounter can last several sessions and two encounters never affect each other. When it ends, the GM decides what carries on.

See [[Encounter Mode|main:encounter_mode]] and [[Dying and Recovery|main:dying_and_recovery]] for the rules these follow.

## Exploration, skill challenges and Recall Knowledge

- `+explore/set <activity>` chooses what you do while exploring. Avoid Notice rolls Stealth for initiative, and Scout gives everyone +1 to initiative.
- `+challenge` shows a skill challenge the GM runs, and `+challenge/roll <skill>` is your check for the round.
- `+recall <creature>` tries to remember what you know about a creature, with the skill its traits call for or a Lore that fits.
- `+dc <level> [difficulty]` gives the DC for a task, such as `+dc 5 hard` for DC 24.

## Experience, money and levels

Staff award experience and money with a reason, and each award is an entry in your ledger. You spend them yourself:

- `+build/level` raises your level for 1,000 XP. `+build` then lists what the new level brings. See [[Leveling Up|main:leveling_up]].
- `+build/upgrade <item>=<rune>` etches a fundamental rune: `+1`, `+2` or `+3` potency, striking on a weapon, resilient on armor. You pay the new rune's price less the old one's.
- `+build/buy` and `+build/sell` keep working after creation. Selling then gives half the price.

`+sheet` shows your experience beside your level.

---

*Rules text under the ORC License. See [[ORC License Notice|help:orc_license_notice]].*
