# ninefold-app

An **application package** (`kind: application`): it registers [`ninefold`](../ninefold/) as a portal page at
`/apps/ninefold`. It owns no objects. `ninefold` serves the routes the page reads, and decides what each viewer
sees and may do:

| Address | Who | What it shows |
|---|---|---|
| `/apps/ninefold` | anyone with a character | the game they are in, their cards, a form to choose their hand of five, and the rules where they stand; for a card keeper, links to the editors |
| `/apps/ninefold/card/<id>` | anyone with a character | one card: its picture, text art, edges, tier and affinity |
| `/apps/ninefold/cards` | card keepers | every card, how many players hold it, and a form to make one |
| `/apps/ninefold/card/<id>` | card keepers | the card editor: name, name on the board, tier, affinity, starter copies, edges, picture (upload or pick from the image library) and text art with a preview |
| `/apps/ninefold/rules` | card keepers | the rule sets, where they apply, the default, the event, and forms to change each |
| `/apps/ninefold/rules/<key>` | card keepers | one rule set: title, stakes, rules and what it does as an event |

Everything here can also be done in the game with `+nf`.
