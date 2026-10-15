# roll-tables

Random tables kept as softcode data: the weather on the road, who is at the inn, what the storm
brings. Players read them with `+table` and roll them in the room with `+table/roll`; table keepers
make and change them with commands, so nobody has to set attributes by hand (though they can).
A table can be written to a wiki page for the portal; the page is output, and the package never
reads it back.

Requires [`plus-help`](https://github.com/SharpMUSH/SharpMUSH/tree/main/examples/packages/plus-help)
for its `+help tables` topics. Manifest format 1.3 (objects and attributes, plus a permission and a
role).

## Commands

| Command | Who | What |
|---|---|---|
| `+table/list` | all | The tables the player may read; `+table/list/2` for the next page |
| `+table <name>` | all | One table, fifty rows to a page: `+table/2 <name>` |
| `+table/roll <name>[=<times>]` | all | Roll once, or up to 20 times, and tell the room: `Ash rolls 14 on Weather on the coast road: Overcast, ...` |
| `+table/roll/private <name>[=<times>]` | all | The same, told only to the roller (`+table/private <name>` too) |
| `+table/lookup <name>=<number or key>` | all | The row a number falls in, or the row with that key, without rolling |
| `+table/create <name>=<die>` | keeper | A new table: the die is a `roll()` formula (`d20`, `2d6`, `d100`), `weight`, or `none` |
| `+table/row <name>=<key>\|<result>` | keeper | Add a row; `+table/row <name>/<n>=...` replaces row n |
| `+table/delrow <name>/<n>` | keeper | Remove a row |
| `+table/die <name>=<die>` | keeper | Roll it another way; every row must fit the new die |
| `+table/title <name>=<title>` | keeper | Its title |
| `+table/lock <name>=<lock key>` | keeper | Who may read, roll and look it up (`role^gm`); `=` alone opens it |
| `+table/delete <name>[=yes]` | keeper | Say what would go; with `=yes`, remove it |
| `+table/publish <name>=<namespace:page>` | keeper with `wiki.create` and `wiki.edit` | Write the table to a wiki page |

A keeper holds `softcode.tables.admin`, which the package's **Table Keeper** role grants. Keepers
read every table, locked or not.

`+table` is added with `@command/add/noparse` and hooked to the command object (its `STARTUP`, run
by `AINSTALL` and at every boot), so a row typed as `Storm: [u(FN`TABLE`ROLL,squall)]` is stored as
code and runs at each roll rather than when it is typed. Uninstalling leaves the added command until
the next restart, as with any `@command/add`.

## How a table rolls

- **A die table** rolls its formula with `roll()`. Each row holds a number or a range (`11-16`);
  ranges may not overlap and must fit inside what the die can roll. A number no row holds gives no
  result.
- **A weight table** picks a row with one `rand()` over the summed weights.
- **A `none` table** makes every row equally likely, and its keys are names for `+table/lookup`.
  Rolling it several times deals different rows with `shuffle()`; dice and weights roll each time
  afresh, so they can repeat.

A row's result is evaluated when it is rolled, as the data object, so a row can roll another table
with `[u(FN`TABLE`ROLL,<name>)]`. Rolls nest at most five deep.

For other code there are two functions on **Roll Tables Functions**, both checking that the enactor
may read the table:

- `` u(<functions>/FN`TABLE`ROLL,<name>) `` gives one roll's result.
- `` u(<functions>/FN`TABLE`LOOKUP,<name>,<key>) `` gives the row a number falls in or whose key it is.

## Where the tables live

Every table is one attribute tree on **Roll Tables Data**:

```
TABLE`<NAME>`DIE           a roll() formula, weight, or none
TABLE`<NAME>`TITLE         what it is called
TABLE`<NAME>`LOCK          optional lock key: who may read it
TABLE`<NAME>`PAGE          the wiki page +table/publish wrote
TABLE`<NAME>`ROW`<n>       one row's result, evaluated when rolled
TABLE`<NAME>`ROW`<n>`KEY   its key: a number or range, a weight, or a name
```

**One attribute per row** (and one for its key) rather than one attribute holding the whole table:

- A keeper edits, examines or removes one row with `&`, `examine` and `@edit` without touching the
  rest, and a result may hold any text, `|` included, since nothing is split.
- An upgrade of the package merges row by row, so a game's own changes to a shipped table survive.
- Rolling stays cheap at hundreds of rows. Each command reads the table once into a list (a die
  table's faces, `11:4 12:4 ...`, found with `grab()`; a weight table's deck, picked with one
  `rand()`), and every draw after that is a single lookup. On a test server a 500-row d500 table
  rolls 20 times in one command in under half a second, well inside the function invocation limit.

Row numbers are names, not places: removing row 3 leaves 1, 2, 4, and a new row takes the next number.

## Publishing to the wiki

`+table/publish weather=main:coast_weather` renders the table with `datacolumns()` (the column form
of `datatable()`) through `render(...,markdown)` and writes it with `@wiki/create`, or `@wiki/edit`
when this table published that page before. A page of that name that the table did not create is
left alone. The Markdown render format arrives with **MarkupString 2.20**; on a server built against
an older MarkupString, `render()` refuses the format and the command says so without writing anything.

## Example tables

Four original tables, written for this package: `weather` (d20, the coast road, whose wind and storm
rows roll `wind` and `squall`), `wind` (weights), `squall` (d6) and `tide` (`none`, looked up by
`high`, `ebb`, `low` and `flood`). Delete or rewrite them freely.
