# roll-tables-help

A bridge between [`roll-tables`](../roll-tables/) and
[`plus-help`](https://github.com/SharpMUSH/SharpMUSH/tree/main/examples/packages/plus-help). It registers
the roll table topics with the `+help` librarian, so `+help tables` and its subtopics work, and makes an
unknown `+table` switch point at `+help tables`.

Install it on a game that has both packages. Uninstalling it takes the topics out of `+help`; neither
package changes.
