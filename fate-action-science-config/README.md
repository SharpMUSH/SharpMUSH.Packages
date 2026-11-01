# fate-action-science-config

Registers the action science settings and its `modes` and `scales` tables with the `+config`
registry, so staff see and change them with `+config fate-science`. Without it the package still
reads its settings; nothing changes them but `&`. A bridge between
[`fate-action-science`](../fate-action-science/) and `plus-config`.
