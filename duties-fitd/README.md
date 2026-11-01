# duties-fitd

A Duties roll provider called `fitd`, over [`sheet-fitd`](../sheet-fitd/). Pick it with
`+config duties/system=fitd`. A bridge between `duties` and `sheet-fitd`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the sheet's actions; every one is `always`, since an action rated 0 still rolls |
| `` FN`DUTIES`TIERS `` | `fail partial success crit-success` |
| `` FN`DUTIES`DC `` | `Risky`, `Desperate, 1 die fewer`, or `No roll`: the position and dice for the difficulty word |
| `` FN`DUTIES`FALLBACK `` | the roller's highest-rated action |
| `` FN`DUTIES`CHECK `` | the action's dice against the position. A difficulty whose position is `none` succeeds with no roll. The first helper in `%<mods>` (`{"helpers":[...]}`) assists: +1 die, and they take 1 stress. `{"invokes":<n>}` above 0 pushes: +1 die for 2 stress. `system` holds `position`, `effect`, `dice`, `highest`, `sixes`, `assist` and `push` |
| `` FN`DUTIES`REWARDS `` | `coin` (`amount`), `stress` (`amount` cleared) |
| `` ON`DUTIES`GRANT `` | gives the coin or clears the stress, and tells the player |

No `FN`DUTIES`TRAINED`: every action rolls. The provider is **Duties FitD Provider**, inside the
FitD Sheet, WIZARD so it may call the sheet's API; its writes are stress and coin, through the
sheet's `` API`STRESS `` and `` API`AWARD ``.
