# fate-system-toolkit-config

Registers the Fate System Toolkit settings and its `conditions` and `storms` lists with the `+config`
registry, so staff see and change them with `+config toolkit`. Without it the package still reads its
settings; nothing changes them but `&`. A bridge between
[`fate-system-toolkit`](../fate-system-toolkit/) and `plus-config`.
