An encounter is a fight, a chase or any scene where the GM wants what happens kept apart from your sheet until it is over. It keeps its own copy of each player's fate points, stress and consequences. Nothing reaches your sheet unless the GM keeps it.

## Taking part

- `+encounter` lists the encounters in the room, or shows the one there is.
- `+encounter/join [<number>]` takes part. The copy is taken from your sheet at that moment.
- While you stand in that room, `+sheet/stress`, `/consequence`, `/spend` and `/recover` change the copy, and `+sheet` shows it with a warning line. Anywhere else, you play on your sheet itself.
- `+encounter/leave [<number>]` takes you out and drops your copy.

A room can hold several encounters and you can be in several. Your play goes to the one you picked with `+encounter/use <number>`, or the last one you joined. An encounter lasts until the GM ends it, so it can run over several days while you play other scenes on your sheet.

## Turns, aspects and conceding

A fight runs in exchanges. In each one, everyone still in it acts once: an attack, an overcome or creating an advantage. Defending is free.

- `+encounter/act` takes your turn. Then `+encounter/act <name>` hands the turn to someone who has not acted yet, a player or an NPC.
- `+encounter/aspect <aspect>[=<free invokes>]` puts an aspect on the scene, such as the one you just created an advantage for. `+encounter/boost <aspect>` puts a boost there: one free invoke, gone once used.
- `+encounter/invoke <number>[=<what for>]` invokes one for +2 or a reroll. A free invoke goes first; otherwise it costs a fate point from your copy.
- `+encounter/concede` gives in before a roll goes against you. You get a fate point, plus one for each consequence you took in this fight, and you say how you get out of it.

When the GM hits you, you are told how many shifts to take: each stress box you mark takes one, and a consequence takes 2, 4 or 6. Whatever you cannot take takes you out.

## Running one

Whoever starts an encounter runs it, and sheet keepers run every encounter.

- `+encounter/start [<title>]` begins one in the room.
- `+encounter/add <name>[=<number>]` and `/remove <name>[=<number>]` bring someone in or take them out.
- `+encounter/exchange` starts the next exchange. At the first, the GM gets a fate point for each player.
- `+encounter/pool` shows the GM's fate points; `+encounter/pool +1=compel` changes them. `+encounter/point <name>` gives a player a fate point, such as for a compel.
- `+encounter/victory <name>[=<n>]` counts victories in a contest: 1, or 2 for success with style. Three wins.
- `+encounter/keep <name>[=<number>]` writes their copy back onto their sheet.
- `+encounter/end [<number>]` ends it. Every copy not kept is dropped.

## Opposition

The GM builds NPCs with `+npc` and brings them in. A **minor** NPC, a thug or a guard dog, has one stress box and no consequences, so a solid hit takes it out. A **major** NPC, a rival or a villain, has every stress track and consequence a player has.

- `+npc/create <name>[=minor|major]` makes one, and `+npc/skill`, `/aspect`, `/stunt`, `/stress` and `/consequences` fill it in. `+npc/share <name>` lets other GMs use it.
- `+encounter/npc <name>[=<how many>]` brings copies into the encounter: `+encounter/npc thug=3` brings Thug 1, Thug 2 and Thug 3.
- `+encounter/roll <npc>/<skill>[=<opposition>]` rolls for one where the room sees it.
- `+encounter/harm <name>=<shifts>` lands a hit. An NPC marks its stress boxes first and is taken out when what is left is more than its consequences take. `+encounter/consequence <npc>/<slot>=<aspect>` takes what is left as a consequence.
- `+encounter/out <name>=<what happens>` says what happens to someone taken out. `+encounter/concede <npc>` concedes for an NPC. A major one banks fate points, which go to the GM's pool the next time it turns up.

For example:

`+encounter/harm thug 3=4`

Output: `[SHEET] Thug 3 takes a hit of 4 shifts. Physical stress box 1 takes 1, and the 3 shifts left are more than it can take: taken out.`

---

*Rules based on the Fate SRDs under CC BY 3.0. See [[Fate License Notice|help:fate_license_notice]].*
