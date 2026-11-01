# duties-brp

A Duties roll provider called `brp`, over [`sheet-brp`](../sheet-brp/). Pick it with
`+config duties/system=brp`. A bridge between `duties` and `sheet-brp`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the characteristic rolls and the skills; `always` for the rolls and every skill with a base above 0 |
| `` FN`DUTIES`TIERS `` | `crit-fail fail success crit-success`: a fumble, a failure, a success or special, a critical |
| `` FN`DUTIES`DC `` | `Difficult (halved)`: the level for the difficulty word |
| `` FN`DUTIES`FALLBACK `` | the roller's highest roll or skill |
| `` FN`DUTIES`TRAINED `` | 1 when the skill stands above its base |
| `` FN`DUTIES`CHECK `` | 1d100 under the chance at the level. A helper in `%<mods>` (`{"helpers":[...]}`) makes it one step easier, as an augment does. `margin` is the chance less the roll. `system` holds `level`, `chance`, `rating`, `total`, `difficulty` and `augmented` |
| `` FN`DUTIES`REWARDS `` | `skill` (`skill`, `amount` in percent), `heal` (`amount` hit points) |
| `` ON`DUTIES`GRANT `` | raises the skill or gives back hit points, and tells the player |

The provider is **Duties BRP Provider**, inside the BRP Sheet, WIZARD so it may call the sheet's
API; its writes are rewards, through the sheet's `` API`RAISE `` and `` API`HEAL ``.
