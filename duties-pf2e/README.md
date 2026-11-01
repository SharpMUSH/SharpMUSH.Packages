# duties-pf2e

A Duties roll provider called `pf2e`, over [`pf2e`](../pf2e/). Pick it with
`+config duties/system=pf2e`. A bridge between `duties` and `pf2e`.

| Contract attribute | Answer |
|---|---|
| `` FN`DUTIES`TRAITS `` | every skill, Perception and the three saves, all `always` |
| `` FN`DUTIES`TIERS `` | `crit-fail fail success crit-success` |
| `` FN`DUTIES`DC `` | `Level DC +2 (hard)`: the roller's level DC with the difficulty's adjustment |
| `` FN`DUTIES`FALLBACK `` | the roller's statistic with the highest modifier |
| `` FN`DUTIES`TRAINED `` | trained or better in the statistic |
| `` FN`DUTIES`REWARDS `` | `xp`, `gp`, `sp` and `cp`, each with `amount` |
| `` ON`DUTIES`GRANT `` | an entry in the character's experience or money ledger, written by pf2e's `` TRIG`PURSE`PUT ``, which tells the player |
| `` FN`DUTIES`CHECK `` | 1d20 plus the statistic's stacked modifiers against the level DC; a helper in `%<mods>` is Aid, +1. `system` holds `dc`, `total`, `natural`, `degree` and `helpers` |

Difficulty words use the level DC for the roller's level, adjusted as Pathfinder adjusts DCs: trivial
-10 (incredibly easy), easy -2, standard +0, hard +2, extreme +5.

The provider is **Duties PF2e Provider**, inside PF2e Rules, WIZARD so it may read each character's
ledger. Its only writes are rewards. Duties reads `` PROVIDER`PF2E `` on the Duties object with `u()`.
