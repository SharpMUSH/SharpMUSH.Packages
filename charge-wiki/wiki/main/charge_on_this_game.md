This game keeps your Charge character sheet for you. `+help sheet`, `+help check` and `+help encounter` explain each command in full.

## Your sheet

- `+sheet` shows your sheet; `+sheet/traits` lists the actions.
- `+sheet/detail <detail>=<text>` writes your concept, appearance or ties.
- `+sheet/set <action>=<dots>` gives out your starting dots (7 by default, at most 2 in one action) until staff approve your character.
- `+sheet/momentum`, `+sheet/stress` and `+sheet/condition` keep count in play.
- `+sheet/advance <action>` and `+sheet/talent <talent>` spend a milestone.
- `+sheet/ledger` lists every entry that built your sheet: the dots you gave out, each milestone and why it was given, each advance and talent. A sheet keeper can undo one entry without touching the rest.

## Rolling

- `+check <action>=<risk> <effect>` makes an action roll for the room, and gains momentum.
- `/push` and `/tension` add a die; `+check/assist <name>` helps someone else.
- `+check/determination <momentum>` resists a consequence, and `+check/fortune` leaves something to luck.
- `+clock` tracks progress and danger clocks.

## Encounters

A fight, chase or other scene can be an encounter with its own copy of each member's sheet. `+encounter/start <title>` starts one and makes you its GM; `+encounter/join` takes a copy of your sheet into it. While you are in the room where it runs, your rolls, momentum, stress and condition use that copy, so an encounter that runs for days never touches another scene or another encounter. The copy's stress and condition reach your sheet only when the GM or a keeper uses `+encounter/keep`, at any time during the encounter. Details, milestones, advances and talents always change your sheet, not the copy. When it ends, its copies are dropped.

## Duties

Automated Duties roll on your own sheet, never on an encounter's copy.


---

*Based on the Charge SRD by Fari RPGs, under CC BY 4.0. See [[Charge License Notice|help:charge_license_notice]].*
