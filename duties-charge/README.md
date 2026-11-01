# duties-charge

A Duties roll provider called `charge`, over [`sheet-charge`](../sheet-charge/). Pick it with
`+config duties/system=charge`. A bridge between `duties` and `sheet-charge`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the sheet's actions; every one is `always`, since an action with no dots still rolls |
| `` FN`DUTIES`TIERS `` | `fail partial success crit-success` |
| `` FN`DUTIES`DC `` | `Moderate risk`, `High risk, 1 die fewer`, or `No roll`: the risk and dice for the difficulty word |
| `` FN`DUTIES`FALLBACK `` | the roller's action with the most dots |
| `` FN`DUTIES`CHECK `` | the action's dice against the risk. A difficulty whose risk is `none` succeeds with no roll. The first helper in `%<mods>` (`{"helpers":[...]}`) who holds momentum assists: +1 die for 1 of their momentum. `{"invokes":<n>}` above 0 pushes when the roller holds 2 momentum: +1 die for 2. A roll that spent no momentum gains it, as `+check` does. `system` holds `risk`, `effect`, `dice`, `highest`, `sixes`, `assist`, `push` and `momentum` (gained) |
| `` FN`DUTIES`REWARDS `` | `momentum` (`amount`), `milestone` (`amount`), `stress` (`amount` recovered) |
| `` ON`DUTIES`GRANT `` | gives the momentum or milestones or clears the stress, and tells the player |

No `FN`DUTIES`TRAINED`: every action rolls. The provider is **Duties Charge Provider**, inside the
Charge Sheet, WIZARD so it may call the sheet's API; its writes are momentum, milestones and stress,
through the sheet's `` API`MOMENTUM ``, `` API`MILESTONE `` and `` API`STRESS ``.

A duty always rolls and writes on the character's own sheet, never on an encounter's copy, so a duty
and an encounter never touch each other: every call passes the sheet API's `live` argument.
