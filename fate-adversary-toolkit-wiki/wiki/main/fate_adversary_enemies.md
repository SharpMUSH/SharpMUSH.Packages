An **enemy** can be attacked and taken out, even if only under certain circumstances. It has skills, at least one aspect, often stunts, stress boxes, and sometimes consequences. Its numbers are set against the PCs' best skill, which the game sets with `+config adversary/peak`.

## The four kinds

- A **threat** soaks up hits and holds the PCs' attention. Its best skill is one above the PCs' best, two skills a step lower and three two steps lower. It has long stress tracks, a mild consequence, and a stunt that helps it last.
- A **hitter** deals damage and goes down fast. It has the same skills, short stress tracks, no consequences, and Weapon:2 with its best skill.
- A **boss** is the big bad. Its best skill is two above the PCs', then two, three, four skills a step lower each, down to Fair, and every other skill Average (+1). It has mild and moderate consequences, often a severe one too.
- A **filler** is a nameless goon. Average, Fair or Good: one skill at that rating (a Good filler has a second at Average), one stress box per step, no stunts and no consequences. Its name is its only aspect.

A tough threat, hitter or boss has every skill one higher and one more consequence.

## Making one

- `+adversary` lists the ready-made adversaries; `+adversary <name>` shows one.
- `+adversary/make <name>[=<new name>]` copies one into `+npc` as yours, its ratings moved to match the PCs.
- `+adversary/build <name>=<type> <skills>` builds one from the recipe above. Name its skills best first.
- `+adversary/stunts` lists quick stunts for an enemy who may not last past one fight.

For example:

`+adversary/build Bruiser=threat physique fight athletics`

Output: `[ADVERSARY] Done: You build Bruiser, a threat against PCs whose best skill is Great (+4): Physique Superb (+5), Fight Great (+4), and Athletics Great (+4); stress physical [ ] [ ] [ ] [ ] [ ] and mental [ ] [ ] [ ]; consequences mild (2). +npc/aspect and +npc/stunt finish it, and +npc Bruiser shows it.`

## Groups of fillers

Fillers are stronger together. `+adversary/mob <filler>=<how many>` brings 2 to 12 into an encounter as one NPC. The group has the filler's skills, one higher for every two fillers in it, never above Great (+4). Its stress track is every filler's boxes in a row, marked from the left, so a single hit can take out several fillers. As they go down, the group's skills drop to match.

For example:

`+adversary/mob Grunt=4`

Output: `[ADVERSARY] Gina brings in Grunt x4: 4 of 4 up, Fight Good (+3); [ ] | [ ] | [ ] | [ ].`

`+encounter/harm Grunt=2`

Output: `[SHEET] Grunt x4 takes a hit of 2 shifts. Physical stress boxes 1 and 2 take it all. 2 of 4 still up: Fight Fair (+2).`

---

*Rules based on the Fate Adversary Toolkit SRD under CC BY 3.0. An unofficial fan package. See [[Fate Adversary Toolkit License Notice|help:fate_adversary_toolkit_license_notice]].*
