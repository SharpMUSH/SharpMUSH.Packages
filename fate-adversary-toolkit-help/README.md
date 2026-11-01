# fate-adversary-toolkit-help

Puts the Fate Adversary Toolkit topics into `+help` (`+help adversary`, `+help adversary build`,
`+help adversary mob`, `+help obstacle`, `+help obstacle gm`, `+help obstacle constraints`,
`+help countdown`, and the settings and credits topics) by registering the package's help object
with the `plus-help` librarian, and points its "no such switch" message at `+help`. A bridge between
[`fate-adversary-toolkit`](../fate-adversary-toolkit/) and `plus-help`.
