# fate-adversary-toolkit-config

Registers the Fate Adversary Toolkit settings and its `adversaries` and `obstacles` libraries with
the `+config` registry, so staff see and change them with `+config adversary`. Without it the
package still reads its settings; nothing changes them but `&`. A bridge between
[`fate-adversary-toolkit`](../fate-adversary-toolkit/) and `plus-config`.
