# atomic-robo-config

Registers the Atomic Robo settings and its `modes` and `scales` tables with the `+config`
registry, so staff see and change them with `+config atomic-robo`. Without it the package still
reads its settings; nothing changes them but `&`. A bridge between
[`atomic-robo`](../atomic-robo/) and `plus-config`.
