# duties-salvage-union

A Duties roll provider called `salvage`, over [`sheet-salvage-union`](../sheet-salvage-union/). Pick it
with `+config duties/system=salvage`. A bridge between `duties` and `sheet-salvage-union`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the bare die (`die`, `always`), and every ability, system and module that is not passive (`ability-<key>`, `system-<key>`, `module-<key>`) |
| `` FN`DUTIES`TIERS `` | `crit-fail fail partial success crit-success`: Cascade Failure (1), Failure (2-5), Tough Choice (6-10), Success (11-19), Nailed It (20) |
| `` FN`DUTIES`DC `` | `Hard (the die is never modified)`: Salvage Union has no target numbers |
| `` FN`DUTIES`CAN `` | 1 when the pilot has the ability, or their mech the system or module |
| `` FN`DUTIES`FALLBACK `` | the bare die |
| `` FN`DUTIES`CHECK `` | one d20 through the sheet's `` API`CHECK ``, which spends the AP, EP and heat the trait costs (1 for an X cost) and makes the heat check at the mech's Heat Capacity. Helpers change nothing. `margin` is the die less 11. `system` holds `die`, `kind`, `heatcheck` and `overload` |
| `` FN`DUTIES`REWARDS `` | `tp` (`amount`), `scrap` (`amount`, `tech`): `scrap once 3 2` is 3 Tech 2 scrap, `scrap once 3` Tech 1 |
| `` ON`DUTIES`GRANT `` | gives the Training Points, or puts the scrap in the Union Crawler's hold, and tells the player |

No `FN`DUTIES`TRAINED`: owning the ability or the part is what `CAN` asks. The provider is **Duties
Salvage Union Provider**, inside the Salvage Union Sheet, WIZARD so it may call the sheet's API.
