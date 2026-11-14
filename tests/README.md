# Package behaviour tests

Each file here is one behaviour test of a package: `tests/<package>/<name>.yaml`. The engine's
integration tests (`PackageLibraryScenarioTests` in SharpMUSH) read every file, boot a test game,
install the packages a file names from this checkout, play its steps as connected players and check
what each step printed. Then they take the packages out again.

The `validate` workflow runs them against SharpMUSH `main`, and against its latest release when that
release has their runner. SharpMUSH's own CI runs them against this repository's `main`. A test is not part of a package, so adding or
changing one needs no new package version.

## Running them

From a SharpMUSH checkout, with Docker running (the test game uses NATS in a container):

```bash
SHARPMUSH_PACKAGES_PATH=/path/to/SharpMUSH.Packages \
  dotnet run --project SharpMUSH.Tests.Integration -- \
  --treenode-filter "/*/SharpMUSH.Tests.PackageLibrary/*/*" --output Detailed
```

A failing test names the file, the step, what it expected and what was printed. The output of every
step before it is under "Standard output".

## A test file

```yaml
# What the test shows, in a sentence or two.
install: [radio, radio-help, radio-config]
cleanup: ["@feed/undefine radio"]
players:
  admin: { roles: [radio-admin] }
  ann:
  bo: { room: bridge }
unique: [said]
steps:
  - as: admin
    run: +radio/create Police
    sees: Created Police.
  - as: ann
    run: +radio/join Police
  - as: ann
    run: +radio Police=${said}
  - heard: bo
    containing: ${said}
    lines: []
    because: bo is not tuned in
```

| Key | What it does |
|---|---|
| `install` | Packages installed before anything else, in order. A name that is not in this repository is installed from the packages the server bundles (`chargen`, `scene`), unless the game has it already. |
| `players` | Connected players, created after the installs. Each gets a room of its own; players naming the same `room` share one. `roles` are assigned with `@role/assign`. |
| `unique` | Words made unique to this run, for text a step looks for. |
| `steps` | Run in order. The test stops at the first step that does not show what it should. |
| `cleanup` | Commands God runs at the end, pass or fail, after the installed packages are taken out. |

Every package the test installed is uninstalled at the end, newest first.

### Steps

Each step has one of these:

| Key | What runs | Its output |
|---|---|---|
| `as: <player>` with `run: <command>` | The player types the command | What the player was told while it ran |
| `god: <command>` | God types the command | What the command returned |
| `eval: <expression>` | God evaluates the expression | Its value; `render: html` gives it as HTML |
| `heard: <player>` with `containing: <text>` | Nothing | Checks every line the player heard so far that contains the text |
| `install: <package>` | Installs a package at this point | |
| `uninstall: <package>` | Takes out a package this test installed, with any bridge over it | |

An `as`, `god` or `eval` step may check its output with `sees`, `not_sees`, `is` and `capture`; a
`heard` step takes `lines` or `count`. A key on the wrong kind of step fails the test.

| Key | Passes when |
|---|---|
| `sees: <text>` or a list | The output contains each text |
| `not_sees: <text>` or a list | The output contains none of them |
| `is: <text>` | The output, trimmed, is exactly the text |
| `lines: [...]` | (`heard`) The lines heard are exactly these, in order; `[]` for none |
| `count: <n>` | (`heard`) That many lines were heard, for a line not known in full, such as a die roll |
| `capture: <name>` | Always; keeps the trimmed output as `${name}` for later steps (not a player's name or `n`) |
| `because: <text>` | Shown when the step fails |
| `repeat: <n>` | Runs the step n times (1 or more) |

### Substitutions

`${...}` in a command, an expression or an expected text is replaced before the step runs:

| Write | For |
|---|---|
| `${ann}` | The player's dbref, `#123` |
| `${ann.name}` | The player's name |
| `${said}` | A word from `unique`, or an output kept with `capture` |
| `${object:radio/radio}` | The dbref of a package's object, by its `ref` in the package |
| `${n}`, `${n:00}` | The count of a `repeat`, plain or zero-padded |

A name that matches nothing fails the test.

### PF2e tests

The files in `pf2e/` are written by `tools/pf2e-tests/build.py` from `tools/pf2e-tests/scenarios`: a
scenario names the Foundry items it reads (`feed: [classes/Cleric, heritages/Dhampir]`), and the build puts
steps first that load those items, and what they bring, from `pf2e-feed` the way the updater does. Edit the
scenario, then run `python3 -I tools/pf2e-tests/build.py`; the `checks` job fails a test that is not what its
scenario gives.

### Writing one

- Look for text that only this test can produce: a player's name or a `unique` word, never "the
  last line". Tests share one game with every other integration test.
- Roll results are random. Check the parts that are not (`"${ann.name} rolls Climb (75%): 1d100["`),
  and count room lines with `count`.
- Quote a value that holds `: ` or ` #`, or starts with `@`, `#`, `[`, `{`, `'`, `"`, `*`, `&`, `!`, `%` or a
  backtick. Inside a `[...]` list, also quote an item holding `,`, `[`, `]`, `{` or `}`.
- Package commands are global, so these tests run one at a time. A fixed table or frequency name is
  fine as long as the test removes it or uninstalls the package.
