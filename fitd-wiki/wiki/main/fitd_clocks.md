A clock is a circle cut into segments that tracks progress toward something: guards growing suspicious, a
rival's plan coming together, a ritual nearly done. Each step toward it fills a segment, and when the clock is
full, the thing happens.

- `+clock` lists the game's clocks; `+clock <name>` shows one.
- `+clock/new Alarm=4` starts a clock of 4, 6, 8 or 12 segments. More segments mean a longer road.
- `+clock/tick Alarm` fills one segment; `+clock/tick Alarm=2` fills two, and a number below 0 empties some.
- `+clock/remove Alarm` takes it away.

Anyone may read the clocks. Whoever started one, and sheet keepers, change it.

## Example

`+clock/tick alarm=2`

Output: `[CLOCK] Alice ticks a clock: Alarm [##..] 2/4`


---

*Based on the Blades in the Dark SRD (CC BY 3.0). See [[About these pages|help:fitd_license_notice]].*
