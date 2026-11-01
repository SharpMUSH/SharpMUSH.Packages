# duties-fabula

A Duties roll provider called `fabula`, over [`sheet-fabula`](../sheet-fabula/). Pick it with
`+config duties/system=fabula`. A bridge between `duties` and `sheet-fabula`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the ten pairs of attributes, every one `always` |
| `` FN`DUTIES`TIERS `` | `crit-fail fail success crit-success`: a fumble, a failure, a success, a critical success |
| `` FN`DUTIES`DC `` | `Hard (13)`: the Difficulty Level of the difficulty word |
| `` FN`DUTIES`FALLBACK `` | the roller's two largest dice now |
| `` FN`DUTIES`CHECK `` | the pair's dice against the Difficulty Level. Each helper in `%<mods>` (`{"helpers":[...]}`) adds 1, and the strongest bond a helper has named for the roller adds its strength, as a group check does. `{"invokes":<n>}` spends up to that many Fabula Points, at most 3 in one check, so one duty roll cannot empty a character's points, rerolling after each failure that is not a fumble. A fumble gives the roller a Fabula Point. `margin` is the total less the Difficulty Level. `system` holds `total`, `hr`, `dice`, `sizes`, `dl`, `helpers`, `bond` and `invokes` |
| `` FN`DUTIES`REWARDS `` | `experience` (`amount`), `zenit` (`amount`), `fabula-point` (`amount`) |
| `` ON`DUTIES`GRANT `` | gives the experience, zenit or Fabula Points and tells the player; experience and zenit go on the sheet's ledger with `Duty <id>` as their source |

No `FN`DUTIES`TRAINED`: every character can roll every pair. The provider is **Duties JRPG
Provider**, inside the JRPG Sheet, WIZARD so it may call the sheet's API; its only writes are Fabula
Points, experience and zenit, through the sheet's `` API`ADJUST ``.

Requires the Fabula Ultima Core Rulebook; see [the sheet's NOTICE](../sheet-fabula/NOTICE.md).
