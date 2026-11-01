**Wealth** is money as a stress track. When cash would help, you check a Wealth box for a bonus on your roll: box 1 adds +1, box 2 adds +2. Haggling for a hover-speeder and fail? Check a box and pay too much. Need gear for the heist? Check a box and you had it all along. It is succeeding at a cost, and the cost is money.

## Your boxes

You start with two boxes. Each aspect about how well off you are adds one more, up to three more. Before approval, `+wealth/aspect <slot>` counts one of your aspects. Later, the only way to add a box is at a milestone, rewriting an aspect as one about wealth: `+sheet/advance wealth <slot>=<aspect>`.

## Spending

- `+wealth/spend <box>` checks a box for a roll you made or are making.
- `+wealth/roll <box>=<skill>=<opposition>` checks a box and rolls with it.

## Getting it back

A checked box does not clear on its own. It clears when you come into loot: gold, credits, barter. Staff give a **parcel** of Wealth with `+wealth/gain`, and it clears the checked boxes whose values add up to no more than the parcel. A parcel of 3 clears box 3, or boxes 1 and 2, but never box 4: that much is not enough to make a difference to you.

Every check and every parcel is an entry on your ledger, with who, when and why: `+wealth/log`.

---

*Rules based on the Fate System Toolkit SRD under CC BY 3.0. An unofficial fan package. See [[Fate System Toolkit License Notice|help:fate_system_toolkit_license_notice]].*
