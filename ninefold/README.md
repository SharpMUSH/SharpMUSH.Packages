# ninefold

**Ninefold** is a card game for two, in the spirit of the card games tucked inside classic JRPGs. Each player
brings a hand of five cards and takes turns putting one on an empty square of a three-by-three board. A card has
four edges, 1 to 10 (10 shows as A). A card takes each touching card of the other player's colour whose facing
edge is lower. When the board is full, each player scores the cards of their colour on the board and the one left
in hand.

Every player starts with the starter set. Card keepers give out more cards, take them back, and make and change
cards: name, edges, tier, affinity, picture and text art. The rules of a game come from where it is played: the
room's rule set, else its zone's, else the game's default, and a game-wide event can replace them or add to them.

## Players

| Command | What it does |
|---|---|
| `+nf` or `+nf/board` | The game you are in, or your cards when you are not in one |
| `+nf/cards` | Your cards, how many of each, and which are in your hand |
| `+nf/card <card>` | One card, with its picture and its text art |
| `+nf/deck [<card>, ...]` | Shows or chooses your hand of five; places left empty are filled with your strongest cards |
| `+nf/rules` | The rule set that applies where you stand, and why |
| `+nf/challenge <player>` | Challenges someone in the room; `+nf/accept`, `+nf/decline`, `+nf/withdraw` answer it |
| `+nf/play <card>=<square>` | Puts a card down: by its number in your hand or its name, on square 1 to 9 |
| `+nf/forfeit` | Gives the game up |
| `+nf/claim [<card>]` | Under Winner Picks, takes one card from the loser's hand |

`+ninefold` is the same command as `+nf`. The player who accepts a challenge goes first.

## Rules and stakes

| Rule | Key | What it does |
|---|---|---|
| Face Up | `faceup` | Both hands are shown to both players |
| Blind Draw | `blind` | Each hand is five cards dealt at random from the player's cards |
| Twin | `twin` | A card whose edges equal the edges they touch on two or more cards takes those cards |
| Balance | `balance` | A card whose edge sums with two or more touching cards are the same takes those cards |
| Cascade | `cascade` | Cards taken by Twin or Balance go on to take the cards they beat |
| Hard Edges | `walls` | For Twin, the edge of the board counts as an A |
| Terrain | `terrain` | A few squares carry an affinity: a card of it gains 1 on every edge there, any other loses 1 |
| Overtime | `overtime` | A draw is played again, each player holding the cards of their colour (up to 3 rounds) |

Stakes are `friendly` (nothing changes hands), `pick` (Winner Picks: the winner takes one card of the loser's
hand) or `spoils` (every card on the board goes to the player whose colour it shows).

The package seeds four rule sets: **Standard** (Face Up, Friendly; the default), **Tavern Rules** (Face Up and
Twin, Winner Picks), **High Stakes** (Twin, Balance, Cascade and Hard Edges, Spoils) and **Festival of
Elements** (Terrain and Overtime, Friendly; as an event it adds its rules).

## Card keepers

The `softcode.ninefold.admin` permission, held by the **Card Keeper** role, lets a character keep the cards.

| Command | What it does |
|---|---|
| `+nf/grant <player>=<card>[,<count>]`, `+nf/revoke ...` | Gives cards or takes them back; both are logged |
| `+nf/log [<player>]`, `+nf/collection <player>` | The last 20 changes; a player's cards |
| `+nf/new <name>=<top> <right> <bottom> <left>` | Makes a card |
| `+nf/set <card>/<field>=<value>` | Changes `name`, `short`, `edges`, `tier`, `affinity`, `starter`, `image` or `art` |
| `+nf/delete <card>=yes` | Removes a card and every copy players hold |
| `+nf/rulesets`, `+nf/ruleset <key>[/<field>]=<value>` | Lists, makes and changes rule sets |
| `+nf/default`, `+nf/room`, `+nf/zone` | Where a rule set applies |
| `+nf/event <rule set>=<how long>`, `+nf/event none` | A game-wide event |
| `+nf/games`, `+nf/end <game>` | The games being played; ends one without paying its stakes |

A card keeps its number when it is renamed, so what players hold never breaks. Ownership is stored by the
player's objid and the card's number.

## The 30 cards

The cards, their names and their text art are placeholders, five tiers of six, one per affinity (`ember`,
`tide`, `gale`, `stone`, `bloom`, `shade`). Pictures are empty; a card keeper uploads them in the portal
(`ninefold-app`) or sets an address with `+nf/set <card>/image=`. Cards 1 to 7 and 10 are the starter set,
one copy each.

## Related packages

- [`ninefold-help`](../ninefold-help/): the `+help ninefold` topics.
- [`ninefold-config`](../ninefold-config/): the settings in `+config ninefold` (how long a challenge waits, the
  Overtime rounds, how many log lines are kept).
- [`ninefold-app`](../ninefold-app/): the portal page at `/apps/ninefold`.
