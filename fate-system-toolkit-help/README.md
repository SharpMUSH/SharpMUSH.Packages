# fate-system-toolkit-help

Puts the Fate System Toolkit topics into `+help` (`+help condition`, `+help condition treat`,
`+help condition gm`, `+help wealth`, `+help wealth staff`, `+help storm`, `+help storm rolls`,
`+help super`, `+help super bid`, `+help super gm`, `+help gadget`, `+help aug`, `+help aug surgery`,
`+help toolkit`, and the settings and credits topics) by registering the package's help object with
the `plus-help` librarian, and points its "no such switch" and storm-roll messages at `+help`. A
bridge between [`fate-system-toolkit`](../fate-system-toolkit/) and `plus-help`.
