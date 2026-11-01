An encounter is a fight, a chase or any scene where the GM wants what happens kept apart from your sheet until it is over. It keeps its own copy of each player's fate points, stress and consequences. Nothing reaches your sheet unless the GM keeps it.

## Taking part

- `+encounter` lists the encounters in the room, or shows the one there is.
- `+encounter/join [<number>]` takes part. The copy is taken from your sheet at that moment.
- While you stand in that room, `+sheet/stress`, `/consequence`, `/spend` and `/recover` change the copy, and `+sheet` shows it with a warning line. Anywhere else, you play on your sheet itself.
- `+encounter/leave [<number>]` takes you out and drops your copy.

A room can hold several encounters and you can be in several. Your play goes to the one you picked with `+encounter/use <number>`, or the last one you joined. An encounter lasts until the GM ends it, so it can run over several days while you play other scenes on your sheet.

## Running one

Whoever starts an encounter runs it, and sheet keepers run every encounter.

- `+encounter/start [<title>]` begins one in the room.
- `+encounter/add <name>[=<number>]` and `/remove <name>[=<number>]` bring someone in or take them out.
- `+encounter/keep <name>[=<number>]` writes their copy back onto their sheet.
- `+encounter/end [<number>]` ends it. Every copy not kept is dropped.

For example:

`+encounter/start Warehouse brawl`

Output: `[SHEET] Alice starts Warehouse brawl (encounter 1). +encounter/join 1 takes part with a copy of your fate points, stress and consequences.`

---

*Rules based on the Fate SRDs under CC BY 3.0. See [[Fate License Notice|help:fate_license_notice]].*
