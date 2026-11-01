# duties-fate

A Duties roll provider called `fate`, over [`sheet-fate`](../sheet-fate/). Pick it with
`+config duties/system=fate`. A bridge between `duties` and `sheet-fate`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the sheet's skills or approaches; every one is `always`, since an unrated one rolls at Mediocre |
| `` FN`DUTIES`TIERS `` | `fail partial success crit-success`: a tie is partial, three shifts success with style |
| `` FN`DUTIES`DC `` | `Fair (+2)`: the sheet's opposition for the difficulty word, a ladder word, or a number |
| `` FN`DUTIES`FALLBACK `` | the roller's highest-rated skill or approach |
| `` FN`DUTIES`CHECK `` | 4dF plus the rating against the opposition. Teamwork: each helper in `%<mods>` (`{"helpers":[...]}`) rated Average or better in the skill adds +1. Invokes: `{"invokes":<n>}` spends that many fate points, as many as the roller has, for +2 each. `system` holds `shifts`, `opposition`, `ladder`, `teamwork` and `invokes` |
| `` FN`DUTIES`REWARDS `` | `fate-point` (`amount`) |
| `` ON`DUTIES`GRANT `` | `{"kind":"fate-point","amount":<n>}` gives the fate points and tells the player |

No `FN`DUTIES`TRAINED`: Fate has no training. The provider is **Duties Fate Provider**, inside the
Fate Sheet, WIZARD so it may call the sheet's API; its only writes are fate points, through the
sheet's `` API`AWARD ``.
