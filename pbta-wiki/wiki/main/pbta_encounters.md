An encounter is a scene played from copies of the sheets. When you join one, it takes a copy of your sheet as
it is then, and while you are in its room your rolls, forward, ongoing and hold use that copy. Nothing that
happens there reaches your sheet or any other scene, however many days the encounter runs.

## Taking part

- `+encounter` lists the encounters in your room and the ones you are in; `+encounter <n>` shows one.
- `+encounter/join <n>` takes part. `+encounter/leave <n>` comes out, and the copy is gone.
- In more than one encounter in the same room? `+encounter/use <n>` picks which copy you roll from.

## Running one

`+encounter/start <title>` starts one in your room, and you run it. You can bring people in with
`+encounter/add <name>=<n>`, take them out with `/remove`, and end it with `+encounter/end <n>`. Ending it
drops every copy. To let something last, such as forward or hold a character earned, `+encounter/keep
<name>=<n>` writes their copy's forward, ongoing and hold to their sheet first.
