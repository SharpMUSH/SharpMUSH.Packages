# duties-pbta

A Duties roll provider called `pbta`, over [`sheet-pbta`](../sheet-pbta/). Pick it with
`+config duties/system=pbta`. A bridge between `duties` and `sheet-pbta`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the sheet's stats and moves (`move-<key>`); every stat and every basic move is `always` |
| `` FN`DUTIES`TIERS `` | `fail partial success`, plus `crit-success` when the sheet's `critical` setting is on |
| `` FN`DUTIES`DC `` | `+1`, `+0`, `-1`, `-2`: what easy to extreme add (`+config pbta/modifiers`); `No roll` for trivial |
| `` FN`DUTIES`FALLBACK `` | the roller's highest stat |
| `` FN`DUTIES`CAN `` | refuses a playbook move the roller does not have |
| `` FN`DUTIES`CHECK `` | trivial: `success` with no roll. Otherwise 2d6 plus the stat (for a move with several, the roller's best), the difficulty's modifier, the roller's forward (spent) and ongoing, and +1 for each helper in `%<mods>` (`{"helpers":[...]}`), as aid. `margin` is empty; `system` holds `rolled`, `move`, `stat`, `total`, `aid`, `forward`, `ongoing` and `outcome` (the move's text for the result) |
| `` FN`DUTIES`REWARDS `` | `xp`, with an `amount` |
| `` ON`DUTIES`GRANT `` | gives an `xp` reward's amount (1 when none) through the sheet's `` API`AWARD `` and tells the player |

No `FN`DUTIES`TRAINED`: PbtA has no training. Invokes in `%<mods>` are ignored. The provider is
**Duties PbtA Provider**, inside the PbtA Sheet, WIZARD so it may call the sheet's API; it writes only
through that API (`` API`SPEND `` and `` API`AWARD ``).
