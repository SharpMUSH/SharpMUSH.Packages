# fate-system-toolkit

An unofficial Fate System Toolkit pack: six of the toolkit's rules for the [Fate sheet](../sheet-fate/).
Conditions that soak stress, a Wealth track for money, Stormcallers, magic drawn from five great
storms, super skills with fate-point bids between powers, gadgets and magic items, and cyberware.

Based on the Fate System Toolkit SRD under CC BY 3.0: see [NOTICE.md](NOTICE.md). The in-game
`+help toolkit credits` topic carries the attribution. It is an unofficial fan package, not affiliated
with or endorsed by Evil Hat Productions.

Depends on [`sheet-fate`](../sheet-fate/) 1.6 or later, whose `` SOAK` `` hooks count a player's clear
conditions against a hit and whose `` RATE` `` hooks roll a stepped-back super skill lower. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`fate-system-toolkit-help`](../fate-system-toolkit-help/) | the `+help condition`, `+help wealth`, `+help storm`, `+help super`, `+help gadget`, `+help aug` and `+help toolkit` topics |
| [`fate-system-toolkit-config`](../fate-system-toolkit-config/) | the settings and the `conditions`, `storms` and `augs` lists in `+config toolkit` |

## Commands

| Command | Who | What |
|---|---|---|
| `+condition [<name>]` | all | Your conditions, or someone's whose sheet you may read |
| `+condition/list` | all | The game's conditions |
| `+condition/take <condition> [<condition>...]` | all | Check conditions off to soak a hit |
| `+condition/recover <condition>` | all | Clear one you are over; a lasting one after treatment |
| `+condition/treat [<name>/]<condition>=<skill>[+<n>]` | all | Treat a lasting condition against the `treat` difficulty; a tie or better starts its recovery |
| `+condition/give <name>=<condition>...`, `/clear <name>=<condition>\|all` | GM | Say someone suffers a condition, or clear it |
| `+wealth [<name>]`, `/log [<name>]` | all | Wealth boxes and the ledger |
| `+wealth/spend <box>[=<what for>]` | all | Check a box for +box on a roll |
| `+wealth/roll <box>=<skill>[+<n>][=<opposition>]` | all | Check a box and roll with it |
| `+wealth/aspect [<name>/]<slot>` | before approval, keeper | Count an aspect about wealth for one more box; again takes it back |
| `+wealth/gain <name>=<parcel> <why>` | keeper | A parcel of Wealth: clears the checked boxes worth the most it covers |
| `+wealth/void <name>/<entry>=<reason>` | keeper | Take a ledger entry back |
| `+storm [<storm>]`, `/list` | all | Your storms, one storm, or every storm |
| `+storm/attune [<name>/]<storm>`, `/unattune` | before approval, keeper | Attune to a storm for `storm_cost` refresh, or give it up |
| `+storm/attack`, `/defend`, `/barrier`, `/overcome`, `/advantage` `[<storm>] [<words>][=<opposition>]` | attuned | Roll Stormcalling with the storm's modifiers |
| `+super [<name>]` | all | Super skills, their ratings and how far each has stepped back |
| `+super/add [<name>/]<skill>`, `/remove` | before approval, keeper | Make a skill a super skill for `super_cost` refresh, or ordinary again |
| `+super/use <skill>[+<n>][=<opposition>]` | all | Spend a fate point to roll a super skill doubled; it steps back by one |
| `+super/refresh` | all | A new scene: super skills come back, unless exhausted |
| `+super/recharge <name>[=<skill>]` | GM | Bring back an exhausted super skill, or every one |
| `+super/bid [<power>]` | all | Show the room's power bid, or bid a fate point on a power |
| `+super/cancel [<how>]`, `/raise <power>`, `/yield` | bidders | Answer a bid with 1 or 2 points, or give up |
| `+super/end` | opener, GM | Let an unanswered power stand; a GM ends any bid as though the side to answer yielded |
| `+gadget [<name>]` | all | Gadgets with their function, flaws, stunts and cost |
| `+gadget/make [<name>/]<gadget>=<function>/<flaw>` | before approval, keeper | Make a gadget |
| `+gadget/stunt`, `/flaw [<name>/]<gadget>=<text>` | before approval, keeper | A stunt for 1 refresh, or a flaw for 1 off |
| `+gadget/unstunt`, `/unflaw [<name>/]<gadget>=<n>`, `/scrap [<name>/]<gadget>` | before approval, keeper | Take a stunt, a flaw or the gadget away |
| `+aug [<name>]`, `/list` | all | Cyberware installed, or every aug |
| `+aug/install [<name>/]<aug>[=<choice>]`, `/remove` | before approval, keeper | Install cyberware, the cyber-heart first, or take it out |
| `+aug/surgery <aug>[=<choice>][ with <approach>][ +<n>]` | approved | Pay for an aug in play: roll `aug_skill` against `aug_minor` or `aug_major`, and recover with a consequence |

GM is whoever runs the encounter the player's play goes to, and sheet keepers (`softcode.fate.admin`)
anywhere. After approval, `+sheet/advance wealth <slot>=<aspect>` spends a milestone to rewrite an
aspect as one about wealth.

## How it fits the sheet

- Conditions are play, as stress is: an encounter copies them (`` PLAY`CONDITION ``), and they stay
  only if the GM keeps the encounter. `+encounter/harm` counts the clear ones in what a player can
  take (`` SOAK`CONDITION ``). A game that uses conditions in place of consequences takes the
  consequence slots away with `+config/remove fate/consequences/<slot>`.
- Wealth is money, apart from the build: every check and parcel is an entry on the character's
  ledger with who, when and why, and the checked boxes are worked out from it. `+sheet/clear` leaves
  the ledger alone and takes away the aspects counted for Wealth (`` BUILD`TOOLKIT ``).
- A storm is part of the build: attuning writes a refresh grant from source `STORM_<KEY>` on the
  sheet's ledger, which `+sheet/clear` takes away with the rest. The Stormcaller skill joins the
  skill list; a game of approaches rolls the approach named with `with`.
- A super skill is part of the build, charged from source `SUPER_<KEY>`. How far it has stepped
  back is play (`` PLAY`SUPER ``), so an encounter's steps last only if the GM keeps it, but an
  exhausted skill stays exhausted on the sheet until `+super/recharge`. `` RATE`SUPER `` takes the
  steps off every roll of it. A power bid lives on the store, one per room, and moves fate points
  through play.
- A gadget is part of the build, charged from source `GADGET_<n>`: 1 refresh a stunt, 1 off a flaw
  past the first, at least 1 with any stunt.
- Cyberware is part of the build, charged together from source `CYBER`: 1 for the heart, 1 a major
  aug, 1 for every `aug_per_refresh` minor augs, a choice past the included ones counting as a minor
  aug. Surgery writes Recovering from Surgery into the `aug_minor_harm` or `aug_major_harm`
  consequence slot, and waits while that slot is taken or the player is in an encounter.
- `+sheet` shows conditions, Wealth, storms, super skills, gadgets and cyberware; `+chargen` offers
  Wealth, a storm, super skills, gadgets and cyberware as optional steps. `+sheet/clear` takes the
  super skills, gadgets and cyberware away with the rest of the build.

## Where the data lives

```
character  FATE`CONDITION`<KEY>        boxes checked (1, or 2 on a lasting one)
           FATE`WEALTH`ASPECTS         aspect slots about wealth
           FATE`WEALTH`LEDGER`<n>      spend <box> | gain <parcel>, with BY AT WHY CLEARED VOID
           FATE`WEALTH`MARKED          the checked boxes, from the ledger
           FATE`STORM`<KEY>            attuned; FATE`GRANT`STORM_<KEY>`REFRESH`ALL its cost
           FATE`SUPER`<KEY>            a super skill, with STEP (play) and OUT (exhausted)
           FATE`GADGET`<n>             name, with FUNCTION, FLAW`<m>, STUNT`<m>
           FATE`AUG`<KEY>              installed, with OPTIONS (choice numbers) or SLOT (the heart's aspect)
store      COND`<KEY>                  name, KIND CLEARS ORDER
           STORM`<KEY>                 name, ASPECT PASSIVE INVOKE COMPEL CREATE ATTACK DEFEND OVERCOME FADE,
                                       BARRIERMOD DEFENDMOD OVERCOMEMOD ZONE SPREAD CHAIN SURROUND SEAL
                                       LENGTHS FREEZE ORDER
           AUG`<KEY>                   name, SIZE TEXT OPTIONS INCLUDED ORDER
           BID`<room number>           the opener's power, OPENER FOE LAST MOVE POWER POT AT
```
