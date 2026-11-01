# duties-d20

A Duties roll provider called `d20`, over [`sheet-d20`](../sheet-d20/). Pick it with
`+config duties/system=d20`. A bridge between `duties` and `sheet-d20`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the sheet's traits; the six abilities are `always` |
| `` FN`DUTIES`TIERS `` | `crit-fail fail success crit-success`, or `fail success` with the sheet's `crits` off |
| `` FN`DUTIES`DC `` | `DC 15`: the sheet's DC for the difficulty word, or a number as given |
| `` FN`DUTIES`FALLBACK `` | the roller's best ability |
| `` FN`DUTIES`TRAINED `` | the sheet's training: a skill above untrained, or any ability |
| `` FN`DUTIES`REWARDS `` | `coin` (`amount`) and `item` (`item`, `amount`) |
| `` ON`DUTIES`GRANT `` | puts the coin or the item on the sheet, through `` API`COIN `` and `` API`GEAR ``, and tells the player |
| `` FN`DUTIES`CHECK `` | 1d20 plus the trait against the DC; any helper in `%<mods>` (`{"helpers":[...]}`) gives advantage, two dice with the higher kept. `system` holds `dc`, `total`, `natural` and `helpers` |

The provider is **Duties D20 Provider**, inside the D20 Sheet, WIZARD so it may call the sheet's
API. Its only writes are rewards, through the sheet's API. Duties reads `` PROVIDER`D20 `` on the Duties object with `u()`, since the
package manager writes it as a reference.
