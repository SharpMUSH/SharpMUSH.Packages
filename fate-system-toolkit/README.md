# fate-system-toolkit

An unofficial Fate System Toolkit pack: three of the toolkit's rules for the [Fate sheet](../sheet-fate/).
Conditions that soak stress, a Wealth track for money, and Stormcallers, magic drawn from five great
storms.

Based on the Fate System Toolkit SRD under CC BY 3.0: see [NOTICE.md](NOTICE.md). The in-game
`+help toolkit credits` topic carries the attribution. It is an unofficial fan package, not affiliated
with or endorsed by Evil Hat Productions.

Depends on [`sheet-fate`](../sheet-fate/) 1.5 or later, whose `` SOAK` `` hooks count a player's clear
conditions against a hit. Bridges add the rest:

| Bridge | Adds |
|---|---|
| [`fate-system-toolkit-help`](../fate-system-toolkit-help/) | the `+help condition`, `+help wealth`, `+help storm` and `+help toolkit` topics |
| [`fate-system-toolkit-config`](../fate-system-toolkit-config/) | the settings and the `conditions` and `storms` lists in `+config toolkit` |

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
- `+sheet` shows conditions, Wealth and storms; `+chargen` offers Wealth and a storm as optional
  steps.

## Where the data lives

```
character  FATE`CONDITION`<KEY>        boxes checked (1, or 2 on a lasting one)
           FATE`WEALTH`ASPECTS         aspect slots about wealth
           FATE`WEALTH`LEDGER`<n>      spend <box> | gain <parcel>, with BY AT WHY CLEARED VOID
           FATE`WEALTH`MARKED          the checked boxes, from the ledger
           FATE`STORM`<KEY>            attuned; FATE`GRANT`STORM_<KEY>`REFRESH`ALL its cost
store      COND`<KEY>                  name, KIND CLEARS ORDER
           STORM`<KEY>                 name, ASPECT PASSIVE INVOKE COMPEL CREATE ATTACK DEFEND OVERCOME FADE,
                                       BARRIERMOD DEFENDMOD OVERCOMEMOD ZONE SPREAD CHAIN SURROUND SEAL
                                       LENGTHS FREEZE ORDER
```
