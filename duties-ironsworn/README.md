# duties-ironsworn

A Duties roll provider called `ironsworn`, over [`sheet-ironsworn`](../sheet-ironsworn/). Pick it
with `+config duties/system=ironsworn`. A bridge between `duties` and `sheet-ironsworn`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | the five stats, every one `always` |
| `` FN`DUTIES`TIERS `` | `crit-fail fail partial success crit-success`: a miss with a match, a miss, a weak hit, a strong hit, a strong hit with a match |
| `` FN`DUTIES`DC `` | `Hard (-1)`: what the difficulty word adds to the action score |
| `` FN`DUTIES`FALLBACK `` | the roller's highest stat |
| `` FN`DUTIES`CHECK `` | an action roll with the stat. A helper in `%<mods>` (`{"helpers":[...]}`) adds 1. `margin` is the action score less the higher challenge die. `system` holds `action`, `challenge`, `match`, `stat`, `adds` and `helped` |
| `` FN`DUTIES`REWARDS `` | `experience` (`amount`), `momentum` (`amount`) |
| `` ON`DUTIES`GRANT `` | marks the experience or gains the momentum, and tells the player |

No `FN`DUTIES`TRAINED`: Ironsworn has no training. The provider is **Duties Ironsworn Provider**,
inside the Ironsworn Sheet, WIZARD so it may call the sheet's API; its only writes are rewards,
through the sheet's `` API`ADJUST ``.
